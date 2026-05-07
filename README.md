# Accumulate-PPTs

个人 HTML 演示文稿（PPT）仓库，用于存放和管理基于 HTML 的幻灯片作品、论文精读汇报与相关制作技能。

## 简介

本仓库是一个专注于 HTML 幻灯片制作的个人项目集合，支持将论文原文、阅读笔记、Markdown 内容或答辩材料整理为可直接浏览器播放的单文件 HTML 演示文稿。根目录的 `index.html` 会读取 `slides-manifest.json`，将 `paper-slides/` 中收录的论文类演示文稿渲染为导航画廊。

单文件 HTML 幻灯片的底层方案参考自开源项目 [html-presentation](https://github.com/juanjuanjie/html-presentation)，在此基础上进行了主题定制、组件扩展与论文汇报场景适配。

## 项目结构

```
Accumulate-PPTs/
├── index.html            # HTML Slides Gallery 导航页
├── slides-manifest.json  # paper-slides 演示文稿清单
├── README.md             # 项目说明
├── paper-slides/         # 论文精读、答辩与研究汇报类 HTML PPT 成品
│   ├── maize_tassels_presentation.html
│   ├── RT-DETR.html
│   ├── SAHI.html
│   ├── sugarcane_thesis_presentation.html
│   ├── YOLO-Master_Presentation.html
│   ├── YOLO-Master_assets/   # YOLO-Master 演示文稿依赖的静态资源
│   ├── YOLOv12.html
│   ├── YOLOv13.html
│   └── YOLO26.html
├── skills/               # 幻灯片制作技能、脚本与模板文档
│   ├── html-paper-slides/
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── pdf_extractor.py   # 从论文 PDF 中提取核心配图的辅助脚本
│   └── html-slides/
│       ├── SKILL.md
│       └── templates/
│           └── presentation.html
├── assets/               # 通用静态资源
├── raw/                  # 原始论文与素材，保留 PDF 等一手资料
├── ingest/               # 摄取后的 Markdown 中间稿与提取素材
└── output/               # 通用 HTML PPT 输出区，适合草稿、课程或非论文类演示
```

## 论文三重重点提取工作流

本仓库推荐采用 `raw/` -> `ingest/` -> HTML PPT 的三重工作流，将论文从原始材料逐层压缩为可讲述、可演示、可复用的内容资产。

### 1. raw：原始材料归档

`raw/` 用于保存论文 PDF、补充材料、网页链接、作者信息、数据集说明、代码仓库地址和临时摘录。该阶段不追求排版，只要求材料完整、来源清晰、文件命名可追踪。建议按论文主题或文件名保存，并记录标题、年份、会议/期刊、作者、论文链接、代码链接和数据来源。

### 2. ingest：Markdown 重点提取

`ingest/` 是论文理解与内容压缩的核心层。将 `raw/` 中的材料整理为结构化 Markdown，重点提取以下内容：研究问题与动机、核心贡献、方法框架、关键模块、实验设置、核心指标、消融结论、可视化证据、局限性、可复现实践和适合放进 PPT 的讲述主线。每份中间稿应尽量形成“论文信息卡 + 重点摘要 + 方法拆解 + 实验结论 + 汇报大纲”的结构，便于后续直接转为 HTML PPT。

### 3. HTML PPT：演示成品入库

HTML PPT 阶段将 `ingest/` 的结构化内容转化为单文件演示文稿。论文类成品优先放入 `paper-slides/`，课程、练习或通用内容可放入 `output/`。生成时应保留清晰的章节流：封面、背景、问题、方法、实验、消融、结论与展望，并通过卡片、流程图、对比表、指标高亮和导航控件强化阅读节奏。成品入库后，需要同步更新 `slides-manifest.json`，确保 `index.html` 画廊可以正确展示标题、路径、简介、类型与主题色。

### 质量检查

在进入下一阶段前建议检查：`raw/` 是否可追溯到原始来源；`ingest/` 是否已经提炼出足够支撑 8-15 页汇报的主线；HTML PPT 是否可以单文件打开、键盘翻页、视觉层级清晰；`slides-manifest.json` 是否覆盖 `paper-slides/` 下的全部 HTML 文件。

## 当前收录的论文演示

| 标题 | 文件 | 类型 | 内容概述 |
| --- | --- | --- | --- |
| Maize Tassels Detection: A Benchmark of the State of the Art | `paper-slides/maize_tassels_presentation.html` | Research PPT | 玉米雄穗检测研究演示，聚焦目标检测、密度回归与植物表型分析基准。 |
| SAHI - 切片辅助超推理与微调小目标检测 | `paper-slides/SAHI.html` | Paper Reading | IEEE ICIP 2022 SAHI 论文演示，聚焦切片推理、小目标检测与微调流程。 |
| 低空航拍可见光图像快速检测甘蔗幼苗群体数量 | `paper-slides/sugarcane_thesis_presentation.html` | Thesis Defense | 面向低空航拍 RGB 图像的甘蔗幼苗群体数量检测学位论文答辩。 |
| YOLO-Master Presentation | `paper-slides/YOLO-Master_Presentation.html` | Paper Reading | YOLO-Master 论文演示，聚焦基于 MoE 加速的专业化 Transformer 实时目标检测方法。 |
| YOLOv12 论文精读 | `paper-slides/YOLOv12.html` | Paper Reading | YOLOv12 论文精读演示，聚焦以注意力为中心的实时目标检测器、Area Attention 与 R-ELAN 等核心设计。 |
| RT-DETR: DETRs Beat YOLOs on Real-time Object Detection | `paper-slides/RT-DETR.html` | Paper Reading | RT-DETR 论文演示，聚焦 DETR 类实时目标检测器、高效混合编码器与不确定性感知选择。 |
| YOLOv13 论文精读 | `paper-slides/YOLOv13.html` | Paper Reading | YOLOv13论文精读演示，聚焦超图自适应关联增强（HyperACE）、全管线聚合-分发范式（FullPAD）与DS轻量化模块。 |
| YOLO26 论文解读 | `paper-slides/YOLO26.html` | Paper Reading | YOLO26论文精读演示，聚焦移除DFL、NMS-free端到端推理、ProgLoss+STAL训练优化与MuSGD优化器。 |

## 核心技术特点

### 设计风格

- **页面形态**：单文件 HTML 幻灯片，适合本地预览、论文汇报与技术分享
- **字体规范**：Noto Sans SC（中文）+ Inter（英文/数字）等 Web 字体
- **页面比例**：16:9 标准宽屏比例
- **视觉组件**：卡片、徽章、高亮条、步骤流、数据表格、进度条等可复用模块

### 功能组件

- Slide Engine - 分页切换逻辑
- 底部翻页控制 + 页码计数器
- 顶部进度条
- 右侧导航点
- `slides-manifest.json` 驱动的演示文稿导航画廊

## 使用方法

1. **归档原文**：将论文、补充材料、数据集说明和参考链接放入 `raw/`，保留可追溯来源。
2. **摄取提炼**：在 `ingest/` 中整理 Markdown 重点提取稿，形成论文信息卡、方法拆解、实验结论和汇报大纲。
3. **提取配图**（可选）：运行 `skills/html-paper-slides/scripts/pdf_extractor.py`，从 `raw/` 中的论文 PDF 自动提取核心配图，供后续 PPT 使用。
4. **生成 PPT**：根据 `html-slides/SKILL.md` 或既有 `paper-slides/` 样例，将 Markdown 内容转换为单文件 HTML。
5. **收录到画廊**：将论文类 HTML 文件放入 `paper-slides/`，并在 `slides-manifest.json` 中补充或更新标题、路径、简介、类型与主题色。
6. **预览画廊**：在浏览器中打开 `index.html`，通过导航页进入对应演示文稿。
7. **演示播放**：打开具体 HTML 文件后，使用键盘方向键或页面按钮翻页。

## 技术栈

- HTML5 + CSS3
- Vanilla JavaScript（无需框架依赖）
- CSS Grid / Flexbox 布局
- CSS Variables 主题管理
- Google Fonts 字体加载

## 参考与致谢

- [html-presentation](https://github.com/juanjuanjie/html-presentation)：原始 HTML 幻灯片模板与播放引擎参考仓库。

## 许可证

本项目为个人学习作品，仅供学习交流使用。

---

*Last Updated: 2026-05-07*
