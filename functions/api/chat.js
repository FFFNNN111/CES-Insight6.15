const JSON_HEADERS = {
  "content-type": "application/json; charset=utf-8",
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "POST, OPTIONS",
  "access-control-allow-headers": "content-type",
};
const DEFAULT_UPSTREAM_TIMEOUT_MS = 25000;
const MAX_UPSTREAM_TIMEOUT_MS = 120000;

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: JSON_HEADERS,
  });
}

function cleanMessage(value) {
  return String(value || "请求失败").replace(/sk-[A-Za-z0-9_-]+/g, "sk-***");
}

function normalizeTimeout(value) {
  const n = Number(value);
  if (!Number.isFinite(n) || n <= 0) {
    return DEFAULT_UPSTREAM_TIMEOUT_MS;
  }
  return Math.max(3000, Math.min(MAX_UPSTREAM_TIMEOUT_MS, Math.floor(n)));
}

function normalizeEndpoint(apiBase) {
  let url;
  try {
    url = new URL(String(apiBase || "").trim());
  } catch (error) {
    throw new Error("API 地址格式错误");
  }

  const path = url.pathname.replace(/\/+$/, "");
  if (url.origin === "https://api.deepseek.com") {
    if (!path || path === "/chat/completions" || path === "/v1" || path === "/v1/chat/completions") {
      return "https://api.deepseek.com/chat/completions";
    }
  }

  if (url.origin === "https://api.xiaomimimo.com") {
    if (path === "/v1" || path === "/v1/chat/completions") {
      return "https://api.xiaomimimo.com/v1/chat/completions";
    }
  }

  throw new Error("不允许转发到该 API 地址");
}

function validatePayload(payload) {
  if (!payload || typeof payload !== "object") {
    throw new Error("请求体不能为空");
  }
  if (!String(payload.api_key || "").trim()) {
    throw new Error("请先填写 API Key");
  }
  if (!String(payload.model || "").trim()) {
    throw new Error("请先填写模型名");
  }
  if (!Array.isArray(payload.messages)) {
    throw new Error("messages 必须是数组");
  }
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: JSON_HEADERS });
}

export async function onRequestPost(context) {
  try {
    const payload = await context.request.json();
    validatePayload(payload);

    const endpoint = normalizeEndpoint(payload.api_base);
    const upstreamPayload = {
      model: String(payload.model).trim(),
      messages: payload.messages,
      temperature: payload.temperature ?? 0.2,
      max_tokens: payload.max_tokens ?? 1000,
      stream: payload.stream || false,
    };
    const timeoutMs = normalizeTimeout(payload.timeout_ms);
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);

    let upstream;
    try {
      upstream = await fetch(endpoint, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          authorization: `Bearer ${String(payload.api_key).trim()}`,
        },
        body: JSON.stringify(upstreamPayload),
        signal: controller.signal,
      });
    } catch (error) {
      if (error && error.name === "AbortError") {
        return json({ ok: false, message: `上游请求超时（${Math.round(timeoutMs / 1000)}秒）` }, 504);
      }
      throw error;
    } finally {
      clearTimeout(timer);
    }
    // 如果是流式请求，直接透传 SSE 流
    if (upstreamPayload.stream && upstream.ok) {
      return new Response(upstream.body, {
        status: upstream.status,
        headers: {
          "content-type": "text/event-stream; charset=utf-8",
          "access-control-allow-origin": "*",
          "cache-control": "no-cache",
          "connection": "keep-alive",
        },
      });
    }

    const text = await upstream.text();
    let data;
    try {
      data = text ? JSON.parse(text) : {};
    } catch (error) {
      data = {
        ok: false,
        message: `上游返回不是 JSON：HTTP ${upstream.status}`,
      };
    }

    if (!upstream.ok && data && typeof data === "object") {
      const upstreamMessage = data.message || data.error?.message || `上游请求失败：HTTP ${upstream.status}`;
      data.message = cleanMessage(upstreamMessage);
      if (data.error && typeof data.error === "object") {
        data.error.message = cleanMessage(data.error.message);
      }
    }

    return json(data, upstream.status);
  } catch (error) {
    return json({ ok: false, message: cleanMessage(error.message) }, 400);
  }
}

export async function onRequest() {
  return json({ ok: false, message: "只支持 POST 请求" }, 405);
}
