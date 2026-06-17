# CONTEXT

- 当前任务：两篇深圳城市公园 CES 独立论文已生成“直接修订稿_标黄批注”和修改说明 Word。
- 已完成：重新联网核对关键来源；在不覆盖原稿的情况下生成 `literature_reports/revised_docs/5,31基于大语言模型的城市生态系统文化服务供需评价与优化研究——以深圳市城市公园为例(1)_修订稿_标黄批注.docx`、`literature_reports/revised_docs/百姓园林导向下城市公园生态系统文化服务感知供需研究——以深圳市为例_修订稿_标黄批注.docx` 和 `literature_reports/revised_docs/2026-06-01_two_paper_revised_change_log.docx`。
- 关键改动：修正关键词空格、图表题名空格、作者引用写法、百度情感分析过强表述、`Fij=CijCi` 公式、`p<0.013` 写法、DeepSeek-R1 正式文献、声景文献作者名、第二篇中英文译文独立编号问题；新增 GB/T 7714-2025 预排参考文献。
- 验收状态：两份修订稿均含黄色高亮和 Word 批注；新增参考文献已写入文末；图片和表格数量与原稿一致；原稿未被覆盖；本机缺少 LibreOffice/`soffice` 和 `pdftoppm`，未完成截图级版式验收。
- 最新网页修复：`CES情感分析_fixed.html` 的双模型对比已改为从 `perception_tendency` 和 `perception_frequency_ai` 的 `source_model` 提取 DeepSeek/MIMO 结果，不再错误读取 `ai_models`；新增 DeepSeek 对比总结区。
- 最新网页修复：文本分析模型已从 MIMO V2.5pro 替换为 Kimi k2.7，默认接口为 https://api.moonshot.cn，默认模型 ID 为 kimi-k2.7-code-highspeed；MIMO ASR 语音识别保持不变；Kimi Key 不写入 HTML，需在页面输入框填写后使用。
- 最新网页修复：Moonshot 测试确认 kimi-k2.7-code/highspeed 当前返回 400，已把文本分析默认模型改为可用的 moonshot-v1-auto，页面显示名改为 Kimi AI，并自动迁移旧缓存中的 Kimi 2.x code 模型值。
