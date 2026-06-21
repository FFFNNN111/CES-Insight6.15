# CONTEXT

- 当前项目：CES 感知情感分析 GitHub + Cloudflare Pages 发布版。
- 入口：`index.html`，内置本地 CES 分类树与关键词数据。
- AI：Cloudflare Pages 环境通过 `functions/api/chat.js` 代理 DeepSeek、Kimi AI 和 MIMO ASR；Key 不写入仓库。
- 构建：`npm run build` 输出 `dist/`；`npm run check` 验证页面、代理地址和 Key 扫描。
- 验证：静态检查、构建、代理地址白名单与本地 HTTP 页面访问均已通过。
- 最新修改：`index.html` 的 Kimi AI 改为三级策略：完整结构化优先、轻量结构化补充、计划 B 自然语言分析；已成功的倾向或频率结果不会被后续层级覆盖。
- 最新修改：双模型对比改为模型级数据驱动的感知频率、感知倾向并列图；“可能原因”由 DeepSeek 单独生成；页面显示不再使用“复核”、PVj、PFj、Nj、N 或 DS 简写。
- 最新验证：HTML 语法、Kimi 五种流程、双模型图表数据和本地 HTTP 页面访问均已通过。
