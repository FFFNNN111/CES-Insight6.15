#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地开发服务器：提供静态文件 + /api/chat 代理，解决 CORS 问题。"""
import http.server, json, urllib.request, urllib.error, os, sys, socketserver

PORT = 8765
DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_ORIGINS = {"https://api.deepseek.com", "https://api.xiaomimimo.com"}
ALLOWED_ENDPOINTS = {
    "https://api.deepseek.com": "https://api.deepseek.com/chat/completions",
    "https://api.deepseek.com/v1": "https://api.deepseek.com/chat/completions",
    "https://api.deepseek.com/v1/chat/completions": "https://api.deepseek.com/chat/completions",
    "https://api.deepseek.com/chat/completions": "https://api.deepseek.com/chat/completions",
    "https://api.xiaomimimo.com/v1": "https://api.xiaomimimo.com/v1/chat/completions",
    "https://api.xiaomimimo.com/v1/chat/completions": "https://api.xiaomimimo.com/v1/chat/completions",
}

def resolve_endpoint(api_base):
    url = (api_base or "").strip().rstrip("/")
    if url in ALLOWED_ENDPOINTS:
        return ALLOWED_ENDPOINTS[url]
    raise ValueError("不允许转发到该 API 地址: " + url)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            api_key = (body.get("api_key") or "").strip()
            model = (body.get("model") or "").strip()
            messages = body.get("messages")
            if not api_key:
                raise ValueError("请先填写 API Key")
            if not model:
                raise ValueError("请先填写模型名")
            if not isinstance(messages, list):
                raise ValueError("messages 必须是数组")

            endpoint = resolve_endpoint(body.get("api_base"))
            upstream_payload = {
                "model": model,
                "messages": messages,
                "temperature": body.get("temperature", 0.2),
                "max_tokens": body.get("max_tokens", 1000),
            }
            timeout_s = max(3, min(120, int((body.get("timeout_ms") or 25000) / 1000)))
            req = urllib.request.Request(
                endpoint,
                data=json.dumps(upstream_payload).encode("utf-8"),
                headers={"Content-Type": "application/json", "Authorization": "Bearer " + api_key},
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                    resp_data = json.loads(resp.read().decode("utf-8"))
                    self.send_response(resp.status)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(json.dumps(resp_data).encode("utf-8"))
            except urllib.error.HTTPError as e:
                err_body = e.read().decode("utf-8", errors="replace")
                try:
                    err_data = json.loads(err_body)
                except Exception:
                    err_data = {"ok": False, "message": "上游请求失败: HTTP " + str(e.code)}
                self.send_response(e.code)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(err_data).encode("utf-8"))
            except urllib.error.URLError as e:
                self.send_response(502)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                msg = str(e.reason) if hasattr(e, "reason") else str(e)
                self.wfile.write(json.dumps({"ok": False, "message": "连接上游失败: " + msg}).encode("utf-8"))
        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": False, "message": str(e)}).encode("utf-8"))

class ThreadedServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    server = ThreadedServer(("127.0.0.1", port), Handler)
    print(f"本地服务器已启动: http://127.0.0.1:{port}")
    print(f"请在浏览器打开: http://127.0.0.1:{port}/CES情感分析.html")
    print("按 Ctrl+C 停止")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
