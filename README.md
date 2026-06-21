# CES 感知情感分析

这是一个可上传到 GitHub、并部署到 Cloudflare Pages 的 CES 感知分析网页。页面内置本地 CES 分类树和关键词数据，支持 DeepSeek、Kimi AI 与 MIMO V2.5 ASR。

## 项目结构

- `index.html`：主页面和本地 CES 分类数据。
- `functions/api/chat.js`：Cloudflare Pages AI 请求代理。
- `scripts/`：无依赖的构建与检查脚本。

## 本地使用

直接双击 `index.html` 可使用本地 CES 分类。AI 功能需要在页面填写自己的 API Key；直接打开文件时，浏览器会直接请求 AI 服务。

## GitHub 与 Cloudflare Pages 部署

1. 将本目录内容上传到 GitHub 仓库根目录。
2. 在 Cloudflare Pages 连接该仓库。
3. 构建命令填写 `npm run build`，输出目录填写 `dist`，根目录留空。
4. 部署完成后访问 Cloudflare 提供的网址。

Cloudflare 部署环境会通过 `/api/chat` 转发请求，避免浏览器跨域限制。代理只允许 DeepSeek、Moonshot/Kimi 和小米 MIMO 的固定接口地址，不保存或记录用户 Key。

## Key 规则

所有 API Key 默认空白。填写后仅保存在当前浏览器的 `localStorage`，不会写入代码或上传到 GitHub。

## 检查命令

```powershell
npm run check
npm run build
```
