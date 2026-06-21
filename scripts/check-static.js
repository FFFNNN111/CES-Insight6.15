import { existsSync, readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const required = ["index.html", "functions/api/chat.js", "package.json", "wrangler.toml"];
for (const file of required) {
  if (!existsSync(resolve(root, file))) throw new Error(`缺少必需文件：${file}`);
}

const html = readFileSync(resolve(root, "index.html"), "utf8");
const proxy = readFileSync(resolve(root, "functions/api/chat.js"), "utf8");
if (/sk-[A-Za-z0-9_-]{10,}/.test(html + proxy)) throw new Error("发现疑似真实 API Key");
if (!html.includes("window.CES_BROWSER_DATASET")) throw new Error("缺少内置 CES 本地数据集");
if (!html.includes('return location.protocol!=="file:";')) throw new Error("页面未启用部署环境代理");
for (const endpoint of ["api.deepseek.com", "api.moonshot.cn", "api.xiaomimimo.com"]) {
  if (!proxy.includes(endpoint)) throw new Error(`代理白名单缺少：${endpoint}`);
}

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map((match) => match[1]).join("\n");
new vm.Script(scripts, { filename: "index.html" });
console.log("静态项目检查通过");
