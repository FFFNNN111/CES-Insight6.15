# 两篇独立论文联网审查报告

任务日期：2026-06-01

检查文件：

- 论文一：`D:\仲恺文件\论文\ing\深圳园\中国园林\5,31基于大语言模型的城市生态系统文化服务供需评价与优化研究——以深圳市城市公园为例(1).docx`
- 论文二：`D:\仲恺文件\论文\ing\深圳园\风景园林\百姓园林导向下城市公园生态系统文化服务感知供需研究\百姓园林导向下城市公园生态系统文化服务感知供需研究——以深圳市为例.docx`

说明：本报告只给审查意见、插入位置和参考文献建议；未修改两篇原 Word，也未修改任何参考文献库。GB/T 7714-2025 格式按现有公开信息预排，正式投稿时仍建议按目标期刊模板复核。

## 一、总览结论

- 两篇 Word 均未发现批注和修订，未发现明显断链交叉引用文本；主要问题集中在表述、编号、方法验证和参考文献支撑。
- 论文一最大风险：以“大语言模型+社交媒体评论+CES供需”为创新点，但 2025-2026 年已有高度相近文献，需在引言和讨论中主动说明与最新研究的差异。
- 论文二最大风险：参考文献编号结构比论文一更不稳，[4]-[5] 实际是同一文献的中英文题录，却被正文当成两条基础文献引用，容易造成引文错位。
- 两篇共同风险：百度情感分析“准确率较高”的写法支撑不足，官方文档只能支撑接口参数，不能证明本文语料上的准确率。
- 两篇共同风险：`Fij=CijCi` 公式缺少除号和下标格式，应改为 `F_{ij}=C_{ij}/C_i`。
- 两篇共同风险：`p<0.013` 写法不规范，应按统计输出改成 `p=0.013` 或按显著性阈值写 `p<0.05`。
- 两篇均存在零宽字符、图表题名缺空格、作者引用位置不规范等小 bug，应在投稿前统一清理。

## 二、论文一独立审查

论文一：《基于大语言模型的城市公园生态系统文化服务供需评价研究——以深圳市为例》

### 2.1 结构与标注检查

- 正文段落：407；粗略字词数：12890。
- 批注：0；修订：插入 0、删除 0、移动 0。
- 交叉引用/字段：44 个；未在提取文本中发现 `Error! Reference source not found`。
- 图片媒体：6 个；脚注/尾注：0/0。
- 参考文献区段：提取到 71 段；其中包含正文编号文献和中文文献英文译文。

### 2.2 标注、格式和排版问题

- 段 7 `文章编号：`、首页 `DOI：`、`收稿日期：`、`修回日期：` 等模板字段为空；若投稿模板不要求作者保留，应删除或填写。
- 段 16 `Key words:Cultural...` 缺少空格，建议改为 `Key words: Cultural...`。
- 段 25 `公园选址和分类` 缺少 `1.1` 编号；论文二同处已有编号，建议统一。
- 段 96 `表3百度智能云API平台情感感知倾向分析参数`、段 240 `图2总体要素感知频率和感知倾向箱图` 缺少题名前后空格，建议统一为 `表3 百度...`、`图2 总体...`。
- 段 367 `注释：` 为空，段 444 有 `(编辑/)` 残留，应删除。
- 段 139、303、315、321、333、347 发现零宽字符；段 404 英文题录含不间断空格，建议全文清理不可见字符。

### 2.3 表述、逻辑和方法问题

- 段 49 `Costanza[15]等、Mónica[16]等` 引用方式不规范，应改为 `Costanza 等[15]、Hernández-Morcillo 等[16]`；不要用作者名中的名作为学术引用。
- 表 1 三类公园的“类别特点”疑似重复，需要核对自然公园、基干公园、特色公园是否填入了相同描述。
- 段 90 写“人工抽查97条样本”，段 228 又写“随机抽查不少于5%的候选句”；两者口径不清。若 5% 是对 9624 条有效评论，样本应约 481 条；若是对候选句，应补充候选句总量。
- 段 94 百度情感分析“准确率较高”缺少本文语料验证依据。建议改为“该接口返回 sentiment、confidence、positive_prob、negative_prob 等参数；本文另以人工复核检验其适用性”。
- 段 230 `Fij=CijCi` 缺少除号和下标，建议改为 `F_{ij}=C_{ij}/C_i`。
- 段 265 `p<0.013` 不规范，建议按原始输出改为 `p=0.013`；若只表达显著性，写 `p<0.05`。
- 段 344、356 中，IPA 把文化遗产、沉浸体验、环境与游憩适宜度和空间承载归为低需低供，但回归结果又强调空间开敞与通行服务正向显著。建议解释为“当前不是短板，但属于长期增益要素”，避免读者认为结论矛盾。

### 2.4 参考文献问题

- [12] 孙伟博、张斌 2020 只能支撑 NLP 概述，不足以支撑 GPT-4.5、少样本提示、DeepSeek-R1 或 LLM 分类流程。
- [24] 谢秋逸等 2021 是百度 AI 平台应用案例，不能直接证明本文公园评论情感分类“准确率较高”。
- [26] DeepSeek-R1 目前建议优先引用 Nature 正式论文；若保留 arXiv，也应作为补充而不是唯一来源。
- [27] Luo 2025 是核心保留文献，但引言还缺 Zheng 2026、Zhao 2026 等更贴近“社交媒体+LLM+CES”的近作。
- [28] 作者写作 `Young J H, Yong J J` 错误，规范作者应为 `HONG J Y, JEON J Y`；且该文只适合支撑声景/沉浸体验，不宜支撑城市公园类型或 CES 供需主结论。

## 三、论文二独立审查

论文二：《百姓园林导向下城市公园生态系统文化服务感知供需研究——以深圳市为例》

### 3.1 结构与标注检查

- 正文段落：443；粗略字词数：15395。
- 批注：0；修订：插入 0、删除 0、移动 0。
- 交叉引用/字段：49 个；未在提取文本中发现 `Error! Reference source not found`。
- 图片媒体：6 个；脚注/尾注：0/0。
- 参考文献区段：提取到 72 段；其中包含正文编号文献和中文文献英文译文。

### 3.2 标注、格式和排版问题

- 英文摘要采用 `[Objective] [Methods] [Results] [Conclusion]`，但 `Abstract：` 与各小节分段过碎，且 `[Objective]Against` 缺空格，应统一结构式摘要格式。
- 图表英文题名存在 `Fig.1`、`Table.1:`、`Tab.2`、`Figure 5` 混用，应统一一种格式。
- 段 126 `表3百度智能云API平台情感感知倾向分析参数` 缺少空格，应改为 `表3 百度...`。
- 段 55、74、87、99、103、111、171、339、351、357、369、384 等发现零宽字符；段 445 英文题录含不间断空格，建议全文清理不可见字符。
- 文末 `图表来源(Sources of Figures and Tables)：图、表均由作者绘制；` 可以保留，但需确认是否符合目标期刊格式。

### 3.3 表述、逻辑和方法问题

- 段 45 `研究通过系统梳理...研究在类别设定...` 重复“研究”，建议压缩为“本文系统梳理...并在类别设定上参考...”。
- 段 45 `Costanza[16]等、Mónica[17]等` 同样应改为 `Costanza 等[16]、Hernández-Morcillo 等[17]`。
- 段 45 “形成候选类别”重复出现，建议删去一次。
- 段 121 `人工抽查97条样本` 与后文验证集逻辑不清，应说明 97 条是数据有效性抽查，500 条是模型识别验证集，否则会被认为样本量前后矛盾。
- 段 125 百度情感分析“准确率较高”同样缺少本文验证依据，建议改为接口参数说明和本地验证说明。
- 段 260-263 公式问题同论文一，应改为 `F_{ij}=C_{ij}/C_i`。
- 段 301 `p<0.013` 不规范，应改为 `p=0.013` 或 `p<0.05`。
- 段 403 把空间开敞与通行服务放入低需低供区，但段 301 又显示它对总体感知有显著正向解释力；建议明确“短期不是紧迫短板，长期仍是质量提升方向”。

### 3.4 参考文献问题

- [4] 中文题录为“李如生,WANG Hui”，作者名中英文混排，应核对原刊中文作者名，建议改为中文姓名。
- [5] 是 [4] 的英文译文，却被独立编号；正文 `[4-5]` 会被读者理解为两条不同文献。建议中英文题录合并为一条，或按目标期刊双语参考文献规则处理，不能让译文独占编号。
- [6] 刘悦来等 2026 是“百姓园林”实践基础文献，但因 [5] 占号，正文编号容易整体错位，应统一重排。
- [13] 孙伟博、张斌 2020 同样只能作为 NLP 背景，不能支撑本文具体 LLM 方法。
- [22] 或 [23] 处用于支撑百度 API 准确率不足；应以百度官方文档支撑接口参数，以人工验证支撑本文适用性。
- 引言和方法缺少 2025-2026 年 LLM+CES 近作，会削弱创新性说明。

## 四、共同参考文献问题

- 两篇都需要把“工具来源”和“方法有效性”分开：OpenAI、DeepSeek、百度官方文档负责说明工具来源；人工标注、抽样复核和一致性指标负责说明本文方法可靠。
- 两篇都需要补充最新同题文献，尤其是 Zheng 2026、Zhao 2026、Luo 2025，否则“大语言模型识别 CES”会显得没有充分回应前沿进展。
- 两篇都需要补充社交媒体 CES 的综述或批判性文献，如 Ghermandi 2026，用于解释平台偏差、代表性和数据伦理边界。
- 两篇都需要突出深圳案例已有供需研究，如 Dang & Li 2023，否则“深圳城市公园 CES 供需”的地方创新性说明不足。
- GB/T 7714-2025 即将替代旧版，现阶段建议按 2025 版思路整理，但投稿时以期刊最新模板为准。

## 五、建议插入文献表

| 文章 | 插入位置 | 用途 | 推荐文献 | GB/T 7714-2025 引文 | 依据 | 访问状态 |
|---|---|---|---|---|---|---|
| 论文一 | 引言中 CES 评价与网络评论研究缺口段后 | 补强社交媒体 CES 研究脉络和深圳案例基础 | Ghermandi 2026；Dang & Li 2023；Tu 等 2023；Zhang 等 2025 | GHERMANDI A, et al. Digital windows into nature's values: a critical review of cultural ecosystem services research with social media data[J]. Ecosystem Services, 2026: 101839. DOI:10.1016/j.ecoser.2026.101839.；DANG A R, LI X. Supply-demand relationship and spatial flow of urban cultural ecosystem services: the case of Shenzhen, China[J]. Journal of Cleaner Production, 2023: 138765. DOI:10.1016/j.jclepro.2023.138765.；TU X, HUANG G, WU J, et al. How do visitors' perceptions differ from the supply of cultural ecosystem services in urban parks? The case of Beijing[J]. International Journal of Sustainable Development & World Ecology, 2023. DOI:10.1080/13504509.2023.2234479.；ZHANG X, ZHAO Y, HU Y. Assessing perception and equity of cultural ecosystem services in urban parks using social media data[J]. Scientific Reports, 2025. DOI:10.1038/s41598-025-18288-0. | 近作直接讨论社交媒体 CES、城市公园供需、深圳 CES 空间流动与感知公平。 | 出版社/DOI 元数据；部分仅基于摘要/元数据判断 |
| 论文一 | 1.3.1 百度情感分析段 94-95 | 替换“准确率较高”的弱支撑，改为官方接口参数来源 | 百度智能云官方文档 | 百度智能云. NLP-Python-SDK：情感倾向分析[EB/OL]. [2026-06-01]. https://cloud.baidu.com/doc/NLP/s/tk6z52b9z.；百度智能云. 情感倾向分析_情感倾向分析算法[EB/OL]. [2026-06-01]. https://cloud.baidu.com/product/nlp_apply/sentiment_classify. | 官方文档可支撑 sentiment、confidence、positive_prob、negative_prob 等参数；不能直接证明本文公园评论准确率。 | 官方网页 |
| 论文一 | 1.3.2 大语言模型识别段 158-159 | 补强 GPT-4.5、Few-shot、DeepSeek-R1 和 LLM+CES 方法依据 | OpenAI 2025；Brown 2020；Guo 等 2025；Luo 等 2025；Zheng 等 2026；Zhao 等 2026 | OPENAI. OpenAI GPT-4.5 system card[EB/OL]. (2025-02-27)[2026-06-01]. https://openai.com/index/gpt-4-5-system-card/.；BROWN T B, MANN B, RYDER N, et al. Language models are few-shot learners[C]//Advances in Neural Information Processing Systems. 2020, 33: 1877-1901.；GUO D Y, YANG D, ZHANG H W, et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning[J]. Nature, 2025, 645: 633-638. DOI:10.1038/s41586-025-09422-z.；LUO H, ZHANG Z, ZHU Q, et al. Using large language models to investigate cultural ecosystem services perceptions: a few-shot and prompt method[J]. Landscape and Urban Planning, 2025, 258: 105323. DOI:10.1016/j.landurbplan.2025.105323.；ZHENG S W, REN Y Y, ZHU C Y, et al. Quantifying cultural ecosystem services in urban parks using social media and large language models: insights for Beijing's Garden City initiative[J]. Urban Forestry & Urban Greening, 2026: 129263. DOI:10.1016/j.ufug.2026.129263.；ZHAO Z R, MA Z H, CHEN B Y, et al. Understanding public perceptions of cultural ecosystem services in urban coastal wetland ecological restoration areas: a social media-based large language model approach[J]. Journal of Environmental Management, 2026: 128816. DOI:10.1016/j.jenvman.2026.128816. | 这些文献分别支撑模型来源、少样本提示、推理型模型、CES 识别方法和同类最新应用。 | 官方网页/出版社/DOI 元数据 |
| 论文一 | 讨论或局限性段 360 附近 | 说明平台偏差、代表性和算法解释限制 | Ghermandi 2026；Zhang 等 2025 | GHERMANDI A, et al. Digital windows into nature's values: a critical review of cultural ecosystem services research with social media data[J]. Ecosystem Services, 2026: 101839. DOI:10.1016/j.ecoser.2026.101839.；ZHANG X, ZHAO Y, HU Y. Assessing perception and equity of cultural ecosystem services in urban parks using social media data[J]. Scientific Reports, 2025. DOI:10.1038/s41598-025-18288-0. | 社交媒体数据不能等同全体公众，应说明样本偏差和公平性。 | 出版社/DOI 元数据；部分仅基于摘要/元数据判断 |
| 论文一 | 参考文献 [28] 或声音/沉浸体验语境 | 修正作者名并限定用途 | Hong & Jeon 2013 | HONG J Y, JEON J Y. Designing sound and visual components for enhancement of urban soundscapes[J]. The Journal of the Acoustical Society of America, 2013, 134(3): 2026-2036. DOI:10.1121/1.4817924. | 原文 `Young J H, Yong J J` 不是规范作者写法；该文只适合支撑声景/视觉组件，不宜泛化到公园类型差异。 | DOI 元数据 |
| 论文二 | 引言段 15 百姓园林基础文献后 | 修正文献编号结构 | 李如生、王辉 2026；刘悦来等 2026 | 建议保留中文正式题录，英文译文不独立编号；英文作者拼写仅放在双语题录中。 | 当前 [4]-[5] 实际是同一文献的中文和英文译文，导致正文 [4-5] 指向错位。 | 本地参考文献结构检查 |
| 论文二 | 段 16-17 CES 与供需关系综述后 | 补强供需、规划和社交媒体 CES 研究 | Dang & Li 2023；Tu 等 2023；Ghermandi 2026；Park 2026 | DANG A R, LI X. Supply-demand relationship and spatial flow of urban cultural ecosystem services: the case of Shenzhen, China[J]. Journal of Cleaner Production, 2023: 138765. DOI:10.1016/j.jclepro.2023.138765.；TU X, HUANG G, WU J, et al. How do visitors' perceptions differ from the supply of cultural ecosystem services in urban parks? The case of Beijing[J]. International Journal of Sustainable Development & World Ecology, 2023. DOI:10.1080/13504509.2023.2234479.；GHERMANDI A, et al. Digital windows into nature's values: a critical review of cultural ecosystem services research with social media data[J]. Ecosystem Services, 2026: 101839. DOI:10.1016/j.ecoser.2026.101839.；PARK S, et al. Operationalizing cultural ecosystem services in urban green planning: a systematic review[J]. Frontiers in Sustainable Cities, 2026. DOI:10.3389/frsc.2026.1768123. | 与城市公园 CES 供需、感知差异和规划应用直接相关。 | 出版社/DOI 元数据；部分仅基于摘要/元数据判断 |
| 论文二 | 1.3.1 段 125/158 | 替换百度 API 准确率表述 | 百度智能云官方文档 | 百度智能云. NLP-Python-SDK：情感倾向分析[EB/OL]. [2026-06-01]. https://cloud.baidu.com/doc/NLP/s/tk6z52b9z.；百度智能云. 情感倾向分析_情感倾向分析算法[EB/OL]. [2026-06-01]. https://cloud.baidu.com/product/nlp_apply/sentiment_classify. | 官方文档能证明接口和返回参数，不能替代本文本地验证集准确率。 | 官方网页 |
| 论文二 | 1.3.2 段 189-190 | 补强 LLM 识别、少样本提示和同类 CES 应用 | OpenAI 2025；Brown 2020；Guo 等 2025；Luo 等 2025；Zheng 等 2026；Zhao 等 2026 | OPENAI. OpenAI GPT-4.5 system card[EB/OL]. (2025-02-27)[2026-06-01]. https://openai.com/index/gpt-4-5-system-card/.；BROWN T B, MANN B, RYDER N, et al. Language models are few-shot learners[C]//Advances in Neural Information Processing Systems. 2020, 33: 1877-1901.；GUO D Y, YANG D, ZHANG H W, et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning[J]. Nature, 2025, 645: 633-638. DOI:10.1038/s41586-025-09422-z.；LUO H, ZHANG Z, ZHU Q, et al. Using large language models to investigate cultural ecosystem services perceptions: a few-shot and prompt method[J]. Landscape and Urban Planning, 2025, 258: 105323. DOI:10.1016/j.landurbplan.2025.105323.；ZHENG S W, REN Y Y, ZHU C Y, et al. Quantifying cultural ecosystem services in urban parks using social media and large language models: insights for Beijing's Garden City initiative[J]. Urban Forestry & Urban Greening, 2026: 129263. DOI:10.1016/j.ufug.2026.129263.；ZHAO Z R, MA Z H, CHEN B Y, et al. Understanding public perceptions of cultural ecosystem services in urban coastal wetland ecological restoration areas: a social media-based large language model approach[J]. Journal of Environmental Management, 2026: 128816. DOI:10.1016/j.jenvman.2026.128816. | 支撑模型、提示方法、推理模型和 CES 语义识别的合法来源。 | 官方网页/出版社/DOI 元数据 |
| 论文二 | 局限与展望段 407-410 | 补充代表性、平台偏差和规划转化边界 | Ghermandi 2026；Zhang 等 2025；Park 2026 | GHERMANDI A, et al. Digital windows into nature's values: a critical review of cultural ecosystem services research with social media data[J]. Ecosystem Services, 2026: 101839. DOI:10.1016/j.ecoser.2026.101839.；ZHANG X, ZHAO Y, HU Y. Assessing perception and equity of cultural ecosystem services in urban parks using social media data[J]. Scientific Reports, 2025. DOI:10.1038/s41598-025-18288-0.；PARK S, et al. Operationalizing cultural ecosystem services in urban green planning: a systematic review[J]. Frontiers in Sustainable Cities, 2026. DOI:10.3389/frsc.2026.1768123. | 帮助把“百姓园林”价值判断与数据偏差、规划应用边界分开。 | 出版社/DOI 元数据；部分仅基于摘要/元数据判断 |

## 六、联网检索记录

| 检索主题 | 关键词/检索式 | 主要来源 | 时间范围 | 结果用途 |
|---|---|---|---|---|
| GB/T 7714-2025 | `GB/T 7714-2025 文后参考文献著录规则 实施 2026-07-01` | 国家标准信息相关页面、标准公开信息 | 2025-2026 | 确认按 2025 新标预排，正式以期刊模板为准 |
| LLM+CES 最新近作 | `Quantifying cultural ecosystem services in urban parks using social media and large language models`；`10.1016/j.ufug.2026.129263` | ScienceDirect/DOI 元数据 | 2026 | 识别论文一、论文二创新性风险 |
| LLM+CES 湿地恢复 | `Understanding public perceptions of cultural ecosystem services... large language model approach`；`10.1016/j.jenvman.2026.128816` | ScienceDirect/DOI 元数据 | 2026 | 补充大模型识别公众感知的近作 |
| Few-shot CES 方法 | `Using large language models to investigate cultural ecosystem services perceptions`；`10.1016/j.landurbplan.2025.105323` | Landscape and Urban Planning/DOI 元数据 | 2025 | 支撑少样本提示和 CES 识别方法 |
| 社交媒体 CES 综述 | `Digital windows into nature's values cultural ecosystem services social media data`；`10.1016/j.ecoser.2026.101839` | Ecosystem Services/DOI 元数据 | 2026 | 支撑平台偏差和局限性 |
| 深圳 CES 供需 | `Supply-demand relationship and spatial flow of urban cultural ecosystem services Shenzhen`；`10.1016/j.jclepro.2023.138765` | Journal of Cleaner Production/DOI 元数据 | 2023 | 补充深圳案例基础 |
| 百度情感分析 | `百度智能云 NLP 情感倾向分析 sentiment confidence positive_prob negative_prob` | 百度智能云官方文档 | 2026-06-01 访问 | 支撑接口参数，不支撑本文准确率泛化 |
| GPT-4.5 | `OpenAI GPT-4.5 system card` | OpenAI 官方页面 | 2025 | 支撑模型来源 |
| DeepSeek-R1 | `DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning Nature` | Nature/DOI 元数据 | 2025 | 替换 arXiv 预印本或作为正式来源 |

## 七、GB/T 7714-2025 引文清单

1. BROWN T B, MANN B, RYDER N, et al. Language models are few-shot learners[C]//Advances in Neural Information Processing Systems. 2020, 33: 1877-1901.
2. OPENAI. OpenAI GPT-4.5 system card[EB/OL]. (2025-02-27)[2026-06-01]. https://openai.com/index/gpt-4-5-system-card/.
3. GUO D Y, YANG D, ZHANG H W, et al. DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning[J]. Nature, 2025, 645: 633-638. DOI:10.1038/s41586-025-09422-z.
4. LUO H, ZHANG Z, ZHU Q, et al. Using large language models to investigate cultural ecosystem services perceptions: a few-shot and prompt method[J]. Landscape and Urban Planning, 2025, 258: 105323. DOI:10.1016/j.landurbplan.2025.105323.
5. ZHENG S W, REN Y Y, ZHU C Y, et al. Quantifying cultural ecosystem services in urban parks using social media and large language models: insights for Beijing's Garden City initiative[J]. Urban Forestry & Urban Greening, 2026: 129263. DOI:10.1016/j.ufug.2026.129263.
6. ZHAO Z R, MA Z H, CHEN B Y, et al. Understanding public perceptions of cultural ecosystem services in urban coastal wetland ecological restoration areas: a social media-based large language model approach[J]. Journal of Environmental Management, 2026: 128816. DOI:10.1016/j.jenvman.2026.128816.
7. GHERMANDI A, et al. Digital windows into nature's values: a critical review of cultural ecosystem services research with social media data[J]. Ecosystem Services, 2026: 101839. DOI:10.1016/j.ecoser.2026.101839.
8. DANG A R, LI X. Supply-demand relationship and spatial flow of urban cultural ecosystem services: the case of Shenzhen, China[J]. Journal of Cleaner Production, 2023: 138765. DOI:10.1016/j.jclepro.2023.138765.
9. TU X, HUANG G, WU J, et al. How do visitors' perceptions differ from the supply of cultural ecosystem services in urban parks? The case of Beijing[J]. International Journal of Sustainable Development & World Ecology, 2023. DOI:10.1080/13504509.2023.2234479.
10. PARK S, et al. Operationalizing cultural ecosystem services in urban green planning: a systematic review[J]. Frontiers in Sustainable Cities, 2026. DOI:10.3389/frsc.2026.1768123.
11. ZHANG X, ZHAO Y, HU Y. Assessing perception and equity of cultural ecosystem services in urban parks using social media data[J]. Scientific Reports, 2025. DOI:10.1038/s41598-025-18288-0.
12. 百度智能云. NLP-Python-SDK：情感倾向分析[EB/OL]. [2026-06-01]. https://cloud.baidu.com/doc/NLP/s/tk6z52b9z.
13. 百度智能云. 情感倾向分析_情感倾向分析算法[EB/OL]. [2026-06-01]. https://cloud.baidu.com/product/nlp_apply/sentiment_classify.
14. HONG J Y, JEON J Y. Designing sound and visual components for enhancement of urban soundscapes[J]. The Journal of the Acoustical Society of America, 2013, 134(3): 2026-2036. DOI:10.1121/1.4817924.

## 八、验收说明

- 本报告生成时已重新提取两篇指定 Word 的结构信息。
- 本报告未修改两篇原论文 Word。
- 本报告中的“仅基于摘要/元数据判断”表示未绕过付费墙，未声称已阅读全文。
- Word 结构检查已通过：章节、两篇论文分节、建议插入文献表、联网检索记录和 GB/T 7714-2025 引文清单均可读取。
- 截图级版式验收未完成：本机未找到 LibreOffice/`soffice` 和 `pdftoppm`，`render_docx.py` 无法生成页面 PNG。
- 两篇原论文的修改时间在报告生成前后保持不变，说明本任务未改动原稿。
