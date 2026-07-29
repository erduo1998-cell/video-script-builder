---
name: 组件配方
description: 叙事目的 → 组件组合配方表。每个场景类型 3 档能量配方 + 抽象概念组件化方法。用于防止 Agent 反复使用同一个组件（data-chart 连用 5 镜等）。第二步组件选型时必读。
---

# 组件组合配方

## 目录

- [为什么需要配方](#为什么需要配方)
- [场景类型与三档能量组合](#配方表场景类型--3-档能量组合)
- [字幕组件切换模式](#字幕组件切换模式)
- [转场搭配模式](#转场搭配模式)
- [抽象概念到组件翻译](#抽象概念--组件翻译表)
- [使用检查清单](#使用检查清单)

## 为什么需要配方

`component-catalog.md` 告诉你"有什么组件"，但不告诉你"怎么组合"。Agent 看到表格中"首选"列的第一个选项就停下来，导致全片 data-chart 连用 5 镜、light-leak 用 8 次、caption-pill-karaoke 全片不换。

**本文件的规则**：为每个镜头选择组件时，先看本表。不要直接取 `component-catalog.md` 场景映射表的"首选"列。

---

## 配方表：场景类型 → 3 档能量组合

每个场景类型给出 3 档组合。全片中每档至少用 1 次，确保视觉多样性。

### 数据展示

| 档位 | 组件组合 | 适合情绪 | 时长建议 |
|------|---------|---------|---------|
| 🔋 低能量 | `liquid-glass-widgets` + 数字大字（CSS）| 冷静、介绍 | 4-6s |
| ⚡ 中能量 | `data-chart` + `shimmer-sweep` | 正常、展示 | 5-8s |
| 💥 高能量 | `vfx-shatter` 碎裂 → 碎片重组为数据 + `light-leak` | 紧张、揭示 | 4-7s |

🔒 **data-chart 专用规则**：如果叙事需要进度条从 0% 填到 100%，不要用同一个 data-chart 连做 5 镜。拆成 3 段——低能量引入（widgets）、中能量爬坡（data-chart ×2 镜 max）、高能量冲刺+碎裂（shatter）。每段换一种视觉手段。

### 概念/定义

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | `liquid-glass-widgets` + 标签文字 | 解释、建立认知 |
| ⚡ 中能量 | `flowchart` + `vfx-text-cursor` | 结构化展示 |
| 💥 高能量 | `texture-mask-text` (66 种 PBR 纹理) + `parallax-zoom` | 冲击力、印象 |

🔒 **抽象概念具象化铁律**：不要用 CSS 手写矩形/card 表达核心概念（如"白纸=上下文窗口"）。优先查上表找合适的组件组合。`texture-mask-text` 有 66 种 PBR 纹理（纸纹/金属/布料等），极其适合将抽象概念编译为可感知的材质。

### 产品/界面展示

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | `app-showcase` (3 设备悬浮) | 首次露面 |
| ⚡ 中能量 | `vfx-iphone-device` + 旋转动画 | 功能演示 |
| 💥 高能量 | `ios26-liquid-glass` + `ui-3d-reveal` | 品牌高潮 |

### 流程/步骤

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | `liquid-glass-media-controls` + 数字 | 简洁指引 |
| ⚡ 中能量 | `flowchart` (决策树+SVG连线) | 结构化解释 |
| 💥 高能量 | `grid-pixelate-wipe` 擦除旧步骤 → 新步骤浮现 | 戏剧化过渡 |

### 对比/反差

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | 左右分屏 + 2 组 `liquid-glass-widgets` | 理性对比 |
| ⚡ 中能量 | `data-chart` 双组 + 颜色对立（绿 vs 红）| 数据对比 |
| 💥 高能量 | `vfx-shatter` 左侧碎裂 → `vfx-portal` 右侧浮现 | 戏剧化反转 |

### Hook 开场

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | `vfx-text-cursor` 打字机 + `vignette` | 悬疑、好奇 |
| ⚡ 中能量 | `caption-kinetic-slam` + `shimmer-sweep` | 冲击、震惊 |
| 💥 高能量 | `vfx-portal` + 核心关键词从传送门中推出 | 科幻、颠覆 |

### CTA 收尾

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | `logo-outro` + 辉光 | 品牌、稳重 |
| ⚡ 中能量 | `caption-kinetic-slam`（CTA 大字）+ `parallax-unzoom` 拉远 | 号召力 |
| 💥 高能量 | `vfx-liquid-background` 流体脉冲 + `apple-money-count`（数字跳动） | 转化驱动 |

### 氛围/情绪建立

| 档位 | 组件组合 | 适合情绪 |
|------|---------|---------|
| 🔋 低能量 | `grain-overlay` + `vignette` + 纯色底 | 基础氛围 |
| ⚡ 中能量 | `vfx-liquid-background` + `shimmer-sweep` | 流动、有机 |
| 💥 高能量 | `vfx-liquid-background` + `chromatic-radial-split` 转场进入 | 不安、紧张 |

---

## 字幕组件切换模式

🔒 全片至少用 2 种 caption 组件。切换时机 = 叙事段落切换点（即情绪曲线拐点处）。

### 情绪 → 字幕 对照表

| 情绪拐点 | 切换到的 caption | 效果 |
|---------|-----------------|------|
| Hook/开场 | `caption-kinetic-slam` 或 `vfx-text-cursor`（大字+底部字幕组合） | 建立冲击力 |
| 解释/建立认知 | `caption-pill-karaoke` 或 `caption-weight-shift` | 温和、易懂 |
| 数据/事实 | `caption-highlight` 或 `caption-clip-wipe` | 信息感、干净 |
| 紧张/危机 | `caption-glitch-rgb` 或 `caption-matrix-decode` | 不安、技术感 |
| 转折/方案 | `caption-editorial-emphasis` 或 `caption-gradient-fill` | 权威、自信 |
| 金句/高潮 | `caption-kinetic-slam` 或 `caption-particle-burst` | 最大冲击 |
| CTA/收尾 | `caption-weight-shift` 或 `caption-neon-accent` | 精致、品牌 |

### 反例

❌ 全片 14 镜只用 `caption-pill-karaoke`——观众在第 5 镜就视觉疲劳了。pill-karaoke 适合"解释/建立认知"段，到了"紧张/危机"段（如百分比超过 50%）就应该切成 `caption-glitch-rgb`，到了金句段切 `caption-kinetic-slam`。

---

## 转场搭配模式

### 三段式转场策略

| 段落 | 推荐转场 | 使用次数上限 |
|------|---------|------------|
| Hook → 主体 | `cinematic-zoom` 或 `glitch` | 1 次 |
| 主体内段落递进 | `light-leak` 或 `transitions-dissolve` | ≤ 全片镜数 × 25% |
| 情绪转折 | `glitch` 或 `chromatic-radial-split` | 1-2 次 |
| 危机→方案 | `flash-through-white` 或 `ridged-burn` | 1-2 次 |
| 方案→金句 | `cinematic-zoom` 或 `swirl-vortex` | 1 次 |
| 金句→CTA | `light-leak` 或 `parallax-unzoom` | 1 次 |

### 反例

❌ `light-leak` 全片用 8 次——段落内递进、情绪转折、高潮收束全用同一种。Agent B 看到 14 镜 spec 中 8 个 `light-leak` 转场，不会觉得"这是精心设计的"，会觉得"Agent A 只认识这一种转场"。

---

## 抽象概念 → 组件翻译表

当逐字稿中出现抽象概念时，不要用 CSS 手写矩形模拟。查下表找组件化方案：

| 抽象概念 | 组件化方案 | 示例 |
|---------|-----------|------|
| 白纸/纸张/书写 | `texture-mask-text` (PBR 纸纹理) + `grid-pixelate-wipe` (擦除) | "上下文窗口像一张白纸" |
| 容量/进度/百分比 | `data-chart` + `liquid-glass-widgets` 分段 | "上下文用了 15%" |
| 碎裂/崩溃/破坏 | `vfx-shatter` + `transitions-destruction` | "100% 直接罢工" |
| 重组/方案/重建 | `liquid-glass-widgets` 依次浮现 + `light-leak` | "怎么管理？开新对话" |
| 流动/变化/时间 | `vfx-liquid-background` 加速/减速 + `shimmer-sweep` | "随着对话越来越多" |
| 对比/A vs B | `data-chart` 双色 + `vfx-shatter` 左侧碎裂 | "AI 变聪明 vs 变笨" |
| 聚焦/揭示/真相 | `cinematic-zoom` + `caption-kinetic-slam` | "不是它变笨了" |
| 记忆/遗忘 | `grid-pixelate-wipe` 擦除文字 → 空白 | "把纸腾出来" |

---

## 使用检查清单

对每个 Scene 选完组件后，快速过：

- [ ] 这个组件在本片中已经连续用了 3 镜吗？→ 是：换高/低一档能量配方
- [ ] 这个场景类型在配方表中有 3 档，我只用了同一档吗？→ 是：选不同能量档位
- [ ] 核心视觉锚点（hook/金句/首尾呼应）用了 CSS fallback 吗？→ 是：回上表找组件化方案
- [ ] 当前段落是情绪拐点吗？→ 是：查字幕切换表，换 caption 组件
- [ ] 下个转场已经在本片中用了 >25% 镜数吗？→ 是：换能量匹配的另一种转场
