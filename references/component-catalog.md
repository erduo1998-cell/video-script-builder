---
name: 组件目录
description: HyperFrames 官方组件完整目录，用于分镜制作时的组件选型。按场景类型映射推荐组件，是 Step 2（组件选型）的核心参考文档。
---

# 组件目录

## 目录

- [如何使用本目录](#如何使用本目录)
- [场景到组件映射表](#场景--组件映射表)
- [完整组件列表](#完整组件列表)
- [安装说明](#安装说明)
- [找不到匹配组件](#找不到匹配组件)

## 如何使用本目录

在 Step 2（组件选型）阶段，Agent 按照分镜表逐一为每个镜头匹配组件。工作流程：

1. 识别当前镜头的场景类型（Hook/概念/数据/对比/产品/流程/氛围/CTA/社媒/地图/过渡）
2. 查下表找到对应行，首选组件为推荐方案
3. 若首选不匹配具体需求（风格冲突、镜头时长特殊等），选择备选
4. 若整行都不匹配，跳转到文末「找不到匹配组件」章节
5. 安装组件：`npx hyperframes add <name>`

## 场景 → 组件映射表

| 场景类型 | 首选组件 | 备选 | 何时用 |
|---------|---------|------|--------|
| Hook 开场 | vfx-text-cursor | caption-kinetic-slam | 前 3s 抓注意力 |
| 概念/定义 | data-chart | flowchart, liquid-glass-widgets | 抽象概念具象化 |
| 数据揭示 | data-chart | us-map, world-map | 数字/统计 |
| 对比/反差 | vfx-shatter | grid-pixelate-wipe | A vs B |
| 产品展示 | vfx-iphone-device | app-showcase, ios26-liquid-glass | 展示界面/设备 |
| 流程/步骤 | flowchart | liquid-glass-media-controls | 1→2→3 步骤 |
| 氛围/情绪 | grain-overlay + vignette | vfx-liquid-background | 建立 mood |
| CTA 收尾 | logo-outro | caption-kinetic-slam | 行动召唤 |
| 社媒引用 | x-post | reddit-post, spotify-card | 引用社交媒体内容 |
| 地图/地理 | world-map | us-map-bubble, nyc-paris-flight | 地理位置相关 |
| 过渡/桥接 | parallax-zoom | parallax-unzoom, grid-pixelate-wipe | 段落间过渡 |

## 完整组件列表

### 独立 Shader 转场（14 个）
详见 `references/shader-transitions.md`。此处列出名称以便索引：

| 组件名 | 类型 | 时长 | 安装命令 |
|--------|------|------|----------|
| glitch | block | 0.5s | `npx hyperframes add glitch` |
| whip-pan | block | 0.5s | `npx hyperframes add whip-pan` |
| light-leak | block | 0.6s | `npx hyperframes add light-leak` |
| cinematic-zoom | block | 0.6s | `npx hyperframes add cinematic-zoom` |
| thermal-distortion | block | 0.5s | `npx hyperframes add thermal-distortion` |
| swirl-vortex | block | 0.6s | `npx hyperframes add swirl-vortex` |
| domain-warp-dissolve | block | 0.6s | `npx hyperframes add domain-warp-dissolve` |
| ridged-burn | block | 0.5s | `npx hyperframes add ridged-burn` |
| sdf-iris | block | 0.5s | `npx hyperframes add sdf-iris` |
| cross-warp-morph | block | 0.6s | `npx hyperframes add cross-warp-morph` |
| flash-through-white | block | 0.4s | `npx hyperframes add flash-through-white` |
| chromatic-radial-split | block | 0.6s | `npx hyperframes add chromatic-radial-split` |
| gravitational-lens | block | 0.6s | `npx hyperframes add gravitational-lens` |
| ripple-waves | block | 0.5s | `npx hyperframes add ripple-waves` |

### 转场展示集（13个）
每套包含多种同风格转场变体，用于需要风格统一但具体方向未定的场景。

| 组件名 | 类型 | 安装命令 |
|--------|------|----------|
| transitions-3d | block | `npx hyperframes add transitions-3d` |
| transitions-blur | block | `npx hyperframes add transitions-blur` |
| transitions-cover | block | `npx hyperframes add transitions-cover` |
| transitions-destruction | block | `npx hyperframes add transitions-destruction` |
| transitions-dissolve | block | `npx hyperframes add transitions-dissolve` |
| transitions-distortion | block | `npx hyperframes add transitions-distortion` |
| transitions-grid | block | `npx hyperframes add transitions-grid` |
| transitions-light | block | `npx hyperframes add transitions-light` |
| transitions-mechanical | block | `npx hyperframes add transitions-mechanical` |
| transitions-push | block | `npx hyperframes add transitions-push` |
| transitions-radial | block | `npx hyperframes add transitions-radial` |
| transitions-scale | block | `npx hyperframes add transitions-scale` |
| transitions-other | block | `npx hyperframes add transitions-other` |

### 字幕组件（16个）
详见 `references/caption-components.md`。

| 组件名 | 类型 | 时长 | 安装命令 |
|--------|------|------|----------|
| caption-kinetic-slam | component | N/A | `npx hyperframes add caption-kinetic-slam` |
| caption-matrix-decode | component | N/A | `npx hyperframes add caption-matrix-decode` |
| caption-particle-burst | component | N/A | `npx hyperframes add caption-particle-burst` |
| caption-pill-karaoke | component | N/A | `npx hyperframes add caption-pill-karaoke` |
| caption-neon-glow | component | N/A | `npx hyperframes add caption-neon-glow` |
| caption-glitch-rgb | component | N/A | `npx hyperframes add caption-glitch-rgb` |
| caption-editorial-emphasis | component | N/A | `npx hyperframes add caption-editorial-emphasis` |
| caption-parallax-layers | component | N/A | `npx hyperframes add caption-parallax-layers` |
| caption-highlight | component | N/A | `npx hyperframes add caption-highlight` |
| caption-gradient-fill | component | N/A | `npx hyperframes add caption-gradient-fill` |
| caption-clip-wipe | component | N/A | `npx hyperframes add caption-clip-wipe` |
| caption-texture | component | N/A | `npx hyperframes add caption-texture` |
| caption-weight-shift | component | N/A | `npx hyperframes add caption-weight-shift` |
| caption-emoji-pop | component | N/A | `npx hyperframes add caption-emoji-pop` |
| caption-neon-accent | component | N/A | `npx hyperframes add caption-neon-accent` |
| caption-blend-difference | component | N/A | `npx hyperframes add caption-blend-difference` |

### 3D/VFX 组件

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| vfx-iphone-device | block | GLTF 3D 模型：iPhone 15 Pro Max + MacBook Pro，可旋转展示 | `npx hyperframes add vfx-iphone-device` |
| ios26-liquid-glass | block | 3D iPhone + iOS 26 液态玻璃风格界面 | `npx hyperframes add ios26-liquid-glass` |
| macos-tahoe-liquid-glass | block | 3D MacBook + macOS 桌面液态玻璃风格 | `npx hyperframes add macos-tahoe-liquid-glass` |
| vfx-shatter | block | 元素碎裂解体效果，适合对比/反差镜头 | `npx hyperframes add vfx-shatter` |
| vfx-portal | block | 传送门视觉特效 | `npx hyperframes add vfx-portal` |
| vfx-liquid-background | block | WebGL 流体模拟背景，适合氛围/情绪镜头 | `npx hyperframes add vfx-liquid-background` |
| vfx-text-cursor | block | 色散阴影文字 + 光标辉光，打字机风格，适合 Hook 开场 | `npx hyperframes add vfx-text-cursor` |
| vfx-magnetic | block | 磁吸动效，元素跟随鼠标/触摸点 | `npx hyperframes add vfx-magnetic` |
| app-showcase | block | 3 个悬浮手机屏幕展示 App 界面 | `npx hyperframes add app-showcase` |

### Liquid Glass 系列

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| liquid-glass-notification | block | iOS 液态玻璃风格通知卡片 | `npx hyperframes add liquid-glass-notification` |
| liquid-glass-context-menu | block | 液态玻璃风格右键菜单 | `npx hyperframes add liquid-glass-context-menu` |
| liquid-glass-media-controls | block | 液态玻璃风格媒体控制面板，适合流程/步骤镜头 | `npx hyperframes add liquid-glass-media-controls` |
| liquid-glass-widgets | block | 液态玻璃风格小组件集合，适合概念具象化 | `npx hyperframes add liquid-glass-widgets` |

### 数据可视化

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| data-chart | block | 带动画的柱状图 + 折线图，适合数据揭示和概念镜头 | `npx hyperframes add data-chart` |
| flowchart | block | 决策树 + SVG 连线，适合流程/步骤展示 | `npx hyperframes add flowchart` |
| world-map | block | 世界地图可视化 | `npx hyperframes add world-map` |
| us-map | block | 美国地图（基础版） | `npx hyperframes add us-map` |
| us-map-bubble | block | 美国地图气泡版 | `npx hyperframes add us-map-bubble` |
| us-map-hex | block | 美国地图六边形热力版 | `npx hyperframes add us-map-hex` |
| us-map-flow | block | 美国地图流向图 | `npx hyperframes add us-map-flow` |
| spain-map | block | 西班牙地图可视化 | `npx hyperframes add spain-map` |

### 社交媒体

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| instagram-follow | block | Instagram 关注按钮动效 | `npx hyperframes add instagram-follow` |
| tiktok-follow | block | TikTok 关注按钮动效 | `npx hyperframes add tiktok-follow` |
| yt-lower-third | block | YouTube 风格下三分之一字幕条 | `npx hyperframes add yt-lower-third` |
| x-post | block | X（Twitter）帖子卡片 | `npx hyperframes add x-post` |
| reddit-post | block | Reddit 帖子卡片 | `npx hyperframes add reddit-post` |
| spotify-card | block | Spotify 播放卡片 | `npx hyperframes add spotify-card` |
| macos-notification | block | macOS 风格通知弹窗 | `npx hyperframes add macos-notification` |

### 展示案例

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| apple-money-count | block | Apple 风格金额跳动计数动画 | `npx hyperframes add apple-money-count` |
| vpn-youtube-spot | block | VPN 主题 YouTube 广告位 | `npx hyperframes add vpn-youtube-spot` |
| blue-sweater-intro-video | block | 蓝色毛衣产品介绍视频模板 | `npx hyperframes add blue-sweater-intro-video` |
| nyc-paris-flight | block | 纽约→巴黎航班路线动画 | `npx hyperframes add nyc-paris-flight` |
| north-korea-locked-down | block | 朝鲜封锁主题数据可视化 | `npx hyperframes add north-korea-locked-down` |
| ui-3d-reveal | block | 3D UI 界面揭示动画 | `npx hyperframes add ui-3d-reveal` |

### 氛围/装饰

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| grain-overlay | component | CSS 关键帧驱动的胶片颗粒叠加层，配合 vignette 建立氛围 | `npx hyperframes add grain-overlay` |
| shimmer-sweep | component | CSS 渐变遮罩光泽扫过效果 | `npx hyperframes add shimmer-sweep` |
| vignette | component | 电影级径向暗角效果 | `npx hyperframes add vignette` |
| grid-pixelate-wipe | component | 网格像素化擦除效果，也可作转场 | `npx hyperframes add grid-pixelate-wipe` |
| texture-mask-text | component | 66 种 PBR 纹理遮罩文字（素材来自 ambientCG） | `npx hyperframes add texture-mask-text` |
| parallax-zoom | component | 视差推进效果，适合段落间过渡/桥接 | `npx hyperframes add parallax-zoom` |
| parallax-unzoom | component | 视差拉远效果，parallax-zoom 的反向变体 | `npx hyperframes add parallax-unzoom` |

### 品牌/收尾

| 组件名 | 类型 | 描述 | 安装命令 |
|--------|------|------|----------|
| logo-outro | block | 电影级 Logo 揭示 + 辉光绽放，适合 CTA 收尾 | `npx hyperframes add logo-outro` |

## 安装说明

所有组件统一通过 `npx hyperframes add <name>` 安装。

- **block** 类型：安装后生成子合成（sub-composition），在 HTML 中通过 `data-composition-src` 属性引用
- **component** 类型：安装后生成 CSS/JS 代码片段，引入到镜头对应的 HTML 元素中使用

## 找不到匹配组件

如果某个镜头在所有官方组件中都找不到匹配项，按以下优先级处理：

1. **重新审视镜头设计**：是否可以用已有组件的组合来实现？例如 `grain-overlay` + `vignette` + 自定义文字可以构成多种氛围场景
2. **使用 GSAP 手写**：参考 `references/gsap-patterns.md` 中的动画模式，用纯 HTML/CSS + GSAP 实现
3. **极简处理**：如果镜头时长很短（<2s），纯文字 + 基础淡入淡出也是可接受的方案

手写 CSS 是**最后手段**，优先始终是官方组件选型。
