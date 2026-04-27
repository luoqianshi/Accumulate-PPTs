# Accumulate-PPTs

个人HTML演示文稿（PPT）仓库，用于存放和管理基于HTML的幻灯片作品及相关制作技能。

## 简介

本仓库是一个专注于HTML幻灯片制作的个人项目集合，采用苹果风/Notion风的设计风格，将Markdown内容转换为精美的HTML演示文稿，可用于视频分镜、技术分享、学习笔记等场景。

## 项目结构

```
Accumulate-PPTs/
├── html-slides/          # HTML幻灯片模板与技能文档
│   ├── SKILL.md          # HTML演示文稿生成器技能文档
│   └── templates/        # HTML模板文件
├── raw/                  # 原始内容（Markdown格式）
│   └── Review.md         # LeetCode Hot 100 学习笔记
├── output/               # 生成的HTML演示文稿
│   └── hot100.html       # LeetCode Hot 100 演示文稿
└── html-ppts/            # 其他HTML幻灯片存放目录
```

## 核心技术特点

### 设计风格
- **配色方案**：纯黑背景 + 紫色标题 + 黄色强调
- **字体规范**：Noto Sans SC（中文）+ Inter（英文/数字）
- **页面比例**：16:9 标准宽屏比例
- **动画效果**：淡入动画、平滑翻页过渡

### 功能组件
- Slide Engine - 分页切换逻辑
- 底部翻页控制 + 页码计数器
- 顶部进度条
- 右侧导航点
- 卡片、徽章、高亮条、步骤流等可复用组件

## 使用方法

1. **准备内容**：在 `raw/` 目录下创建Markdown格式的原始内容
2. **生成PPT**：根据 `html-slides/SKILL.md` 的规范，将Markdown转换为HTML
3. **预览效果**：直接在浏览器中打开 `output/` 目录下的HTML文件
4. **演示播放**：使用键盘方向键或点击按钮进行翻页

## 示例作品

### LeetCode Hot 100 渐进式扫盲手册
- **原始文件**：`raw/Review.md`
- **生成文件**：`output/hot100.html`
- **内容概述**：涵盖哈希表、双指针、滑动窗口、二叉树、动态规划等算法主题的LeetCode Hot 100解题笔记

## 技术栈

- HTML5 + CSS3
- Vanilla JavaScript（无需框架依赖）
- CSS Grid / Flexbox 布局
- CSS Variables 主题管理
- Google Fonts 字体加载

## 本地预览

```bash
# 克隆仓库
git clone <repository-url>
cd Accumulate-PPTs

# 直接用浏览器打开HTML文件
# 或使用本地服务器预览
npx serve output/
```

## 注意事项

1. 由于使用了 `file://` 协议，Google Fonts 可能无法正常加载，建议使用系统字体作为 fallback
2. 翻页动画依赖CSS `!important` 优先级，确保样式正确覆盖
3. 推荐在Chrome、Edge等现代浏览器中查看以获得最佳效果

## 许可证

本项目为个人学习作品，仅供学习交流使用。

---

*Last Updated: 2026*
