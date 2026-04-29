# Accumulate-PPTs

个人 HTML 演示文稿（PPT）仓库，用于存放和管理基于 HTML 的幻灯片作品、论文精读汇报与相关制作技能。

## 简介

本仓库是一个专注于 HTML 幻灯片制作的个人项目集合，支持将 Markdown 内容或论文阅读材料整理为可直接浏览器播放的单文件 HTML 演示文稿。根目录的 `index.html` 会读取 `slides-manifest.json`，将 `paper-slides/` 中收录的论文类演示文稿渲染为导航画廊。

## 项目结构

```
Accumulate-PPTs/
├── index.html            # HTML Slides Gallery 导航页
├── slides-manifest.json  # paper-slides 演示文稿清单
├── paper-slides/         # 论文精读、答辩与研究汇报类 HTML PPT
│   ├── maize_tassels_presentation.html
│   ├── SAHI.html
│   ├── sugarcane_thesis_presentation.html
│   ├── YOLO-Master_Presentation.html
│   └── YOLOv12.html
├── html-slides/          # HTML 幻灯片模板与技能文档

├── html-slides-xmu/      # 其他技能/模板文档
├── raw/                  # 原始内容（Markdown 格式）
└── output/               # 生成的 HTML 演示文稿
```

## 当前收录的论文演示

| 标题 | 文件 | 类型 | 内容概述 |
| --- | --- | --- | --- |
| Maize Tassels Detection: A Benchmark of the State of the Art | `paper-slides/maize_tassels_presentation.html` | Research PPT | 玉米雄穗检测研究演示，聚焦遥感/视觉检测方法与基准对比。 |
| SAHI - 切片辅助超推理与微调小目标检测 | `paper-slides/SAHI.html` | HTML PPT | SAHI 切片辅助超推理与微调小目标检测主题演示。 |
| 低空航拍可见光图像快速检测甘蔗幼苗群体数量 | `paper-slides/sugarcane_thesis_presentation.html` | Thesis PPT | 面向低空航拍可见光图像的甘蔗幼苗群体数量检测论文汇报。 |
| YOLO-Master Presentation | `paper-slides/YOLO-Master_Presentation.html` | Paper Reading | YOLO-Master 论文演示，聚焦基于 MoE 加速的专业化 Transformer 实时目标检测方法。 |
| YOLOv12 论文精读 | `paper-slides/YOLOv12.html` | Paper Reading | YOLOv12 论文精读演示，聚焦以注意力为中心的实时目标检测器、Area Attention 与 R-ELAN 等核心设计。 |


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

1. **准备内容**：在 `raw/` 目录下创建 Markdown 格式的原始内容，或整理论文/答辩材料。
2. **生成 PPT**：根据 `html-slides/SKILL.md` 的规范，将内容转换为单文件 HTML。
3. **收录到画廊**：将 HTML 文件放入 `paper-slides/`，并在 `slides-manifest.json` 中补充标题、路径、简介、类型与主题色。
4. **预览画廊**：在浏览器中打开 `index.html`，通过导航页进入对应演示文稿。
5. **演示播放**：打开具体 HTML 文件后，使用键盘方向键或页面按钮翻页。

## 技术栈

- HTML5 + CSS3
- Vanilla JavaScript（无需框架依赖）
- CSS Grid / Flexbox 布局
- CSS Variables 主题管理
- Google Fonts 字体加载

## 许可证

本项目为个人学习作品，仅供学习交流使用。

---

*Last Updated: 2026-04-29*

