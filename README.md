# 6.15 CES GitHub Pages 部署版

这是一个纯静态网页项目，可以本地直接打开，也可以上传到 GitHub 后用 GitHub Pages 部署。

## 本地使用

双击：

`启动项/CES情感分析.html`

不需要启动 Python，不需要打开 bat。

也可以打开根目录的：

`index.html`

它会自动跳转到主页面。

## GitHub Pages 部署

1. 把本目录 `6.15ces软件` 上传到 GitHub 仓库。
2. 进入仓库 `Settings`。
3. 打开 `Pages`。
4. Source 选择 `Deploy from a branch`。
5. Branch 选择 `main`，目录选择 `/root`。
6. 保存后等待 GitHub 生成访问网址。

## Cloudflare Pages 部署

Cloudflare Pages 可以直接连接这个 GitHub 仓库。

构建设置：

```text
Build command: npm run build
Build output directory: dist
Root directory: 留空
```

项目已经包含 `package.json` 和 `wrangler.toml`，用于解决 Cloudflare 默认执行 `npm run build` 时找不到 `package.json` 的问题。

部署到 Cloudflare 后，页面会优先请求本站的 `/api/chat`，再由 Cloudflare Pages Function 转发到 DeepSeek 或 MiMo。这样可以避免浏览器直接跨域请求外部 API 被拦截。

## 保留内容

- `index.html`：GitHub Pages 首页入口。
- `启动项/CES情感分析.html`：主页面。
- `启动项/ces_browser_dataset.js`：浏览器本地 CES 分类树和关键词数据。
- `functions/api/chat.js`：Cloudflare Pages Function，用于代理 DeepSeek / MiMo / MiMo ASR。
- `package.json`、`wrangler.toml`、`scripts/build-static.js`：Cloudflare Pages 静态构建配置。
- `.nojekyll`、`.gitignore`、`.gitattributes`：GitHub Pages 和编码辅助配置。

## 已移除内容

- 机器学习模型。
- 完整训练数据。
- 训练脚本。
- Python 后端代理。
- 启动 bat / ps1。
- 缓存和测试文件。

## 当前工作方式

- DeepSeek：Cloudflare 部署后经 `/api/chat` 转发到 `https://api.deepseek.com`，本地双击 HTML 时浏览器直连。
- MIMO V2.5pro：Cloudflare 部署后经 `/api/chat` 转发到 `https://api.xiaomimimo.com/v1`，本地双击 HTML 时浏览器直连。
- MiMo 2.5 ASR：Cloudflare 部署后经 `/api/chat` 转发到 `https://api.xiaomimimo.com/v1/chat/completions`，本地双击 HTML 时浏览器直连。
- 本地 CES：使用 `ces_browser_dataset.js` 做轻量分类兜底。
- CES 感知倾向：可单独运行，也可和感知频率一起运行；本地数据集先给出候选 CES 类别和关键词命中，deepseek v4 pro / MIMO V2.5pro 再给出倾向分值、依据和人工复核标记。
- AI 感知频率复核：可单独运行，也可和感知倾向一起运行；本地数据集先给出关键词命中，deepseek v4 pro / MIMO V2.5pro 再按 `PFj = Nj / N` 输出语义级命中片段、判断原因和人工复核标记。
- 双模型模式：deepseek v4 pro 与 MIMO V2.5pro 按 3:1 权重合成情感概率。
- 分析历史：感知倾向和感知频率分开保存，每类最多保留 100 条，保存在当前浏览器 `localStorage`。

页面不会在代码里保存真实 Key。用户填写 Key 后，只保存在当前浏览器的 `localStorage`，输入框会直接显示普通字符。

## 重要说明

本地 CES 兜底只基于分类树和关键词，不是原来的 Python 机器学习模型。

感知倾向功能使用的是轻量 CES 分类树、关键词和统计信息，不读取完整训练明细，也不运行机器学习模型。

本地感知频率是关键词命中频率；AI 感知频率复核是语义辅助结果，不读取完整训练明细，也不替代人工复核。

如果 DeepSeek 或 MiMo 服务端不允许浏览器跨域直连，AI 功能会失败，但本地 CES 兜底仍可用。
