# CONTEXT

- 当前项目：CES 感知情感分析 GitHub + Cloudflare Pages 发布版。
- 入口：`index.html`，内置本地 CES 分类树与关键词数据。
- AI：Cloudflare Pages 环境通过 `functions/api/chat.js` 代理 DeepSeek、Kimi AI 和 MIMO ASR；Key 不写入仓库。
- 构建：`npm run build` 输出 `dist/`；`npm run check` 验证页面、代理地址和 Key 扫描。
- 验证：静态检查、构建、代理地址白名单与本地 HTTP 页面访问均已通过。
