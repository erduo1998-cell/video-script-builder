---
name: 字幕组件
description: HyperFrames 16 种官方字幕组件完整参考，用于分镜制作时根据情绪/场景选择字幕展示风格。替代旧版手写 CSS 字幕方案。
---

# 字幕组件

## 字幕设计哲学

HyperFrames 的字幕不是简单的"底部文字条"。16 种官方字幕组件覆盖了从极简（weight-shift）到爆炸（kinetic-slam）的完整情绪光谱。

**核心理念**：字幕风格必须匹配镜头的情绪强度。柔和的内容配柔和的字幕，冲击力内容配冲击力字幕。不要让字幕与画面情绪打架。

## 字幕风格选择表

| 情绪/场景 | 推荐字幕组件 | 视觉效果 |
|-----------|------------|---------|
| Hook/冲击 | caption-kinetic-slam | 全屏大字交替方向弹入 |
| 数据/事实 | caption-highlight | TikTok 式红色背景扫过关键词 |
| 技术/AI感 | caption-matrix-decode | 字符乱码后解码揭示 |
| 游戏/赛博 | caption-glitch-rgb | RGB 色散+CRT 扫描线 |
| 温暖/人文 | caption-weight-shift | 优雅字重渐变过渡 |
| 高端/品牌 | caption-editorial-emphasis | 双字体+戏剧性大小对比 |
| 氛围/沉浸 | caption-texture | 流动纹理遮罩（6种纹理可选） |
| 专业/讲解 | caption-pill-karaoke | 药丸容器+逐词卡拉OK |
| 能量/爆发 | caption-particle-burst | 关键词触发彩色粒子爆炸 |
| 简约/干净 | caption-clip-wipe | 左到右 clip-path 逐词揭示 |
| 3D/深度 | caption-parallax-layers | 背后3D文字层叠+纵向拉伸 |
| 夜店/霓虹 | caption-neon-glow | 青色+品红霓虹发光 |

### 补充组件

以下组件用于上述表格未覆盖的特殊场景：

| 组件名 | 适用场景 | 视觉效果 | 安装命令 |
|--------|---------|---------|----------|
| caption-gradient-fill | 渐变品牌风格 | 渐变色填充文字 | `npx hyperframes add caption-gradient-fill` |
| caption-emoji-pop | 轻松/社交媒体风格 | Emoji 弹跳伴随文字 | `npx hyperframes add caption-emoji-pop` |
| caption-neon-accent | 霓虹强调（比 glow 更克制） | 单色霓虹描边 | `npx hyperframes add caption-neon-accent` |
| caption-blend-difference | 实验性/艺术风格 | mix-blend-mode 差异混合 | `npx hyperframes add caption-blend-difference` |

## 字幕 vs 屏显文字

**关键规则：不要用字幕组件展示屏显文字。**

```
屏显文字（Screen Text）：
- 1-4 个关键词
- 出现在画面中央或特定位置
- 通常使用 vfx-text-cursor 或其他 VFX 组件
- 是画面的有机组成部分

字幕（Subtitle）：
- 完整的口播文案
- 出现在画面底部区域
- 使用本页的 16 种字幕组件之一
- 是配音的文字伴随
```

**特殊情况**：当使用 `caption-kinetic-slam` 或 `caption-particle-burst` 时，字幕本身已经具有强烈的视觉冲击力，此时**字幕就是屏显文字**——不要再另外放一份相同内容的屏显文字，会导致画面冗余。

## 字幕轨道管理

每个镜头使用**一种**字幕组件。组件之间可以切换：

- 同一段落内：字幕组件保持不变，保证视觉一致性
- 段落切换时：可以更换字幕组件以匹配新的情绪基调
- 全片建议不超过 3 种字幕组件（开篇 1 种、主体 1 种、结尾可选 1 种）

所有字幕组件通过 `npx hyperframes add <name>` 安装，安装后引入对应的 CSS/JS 代码片段即可使用。
