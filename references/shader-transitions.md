---
name: Shader 转场
description: HyperFrames 官方 WebGL Shader 转场参考，覆盖 14 个独立转场和 13 个转场展示集。用于分镜制作时根据场景情绪选择转场效果。
---

# Shader 转场

## 目录

- [核心概念](#核心概念)
- [转场选择表](#转场选择表)
- [使用规则](#使用规则)
- [完整转场列表](#完整转场列表)
- [CSS 降级方案](#css-降级方案)

## 核心概念

本参考覆盖官方 registry 当前的 14 个独立 Shader 转场；另有 13 个 `transitions-*` 转场展示集可按风格安装。所有转场通过 `npx hyperframes add <name>` 安装。

**为什么用 Shader 而不是 CSS 过渡？**

- Shader 转场是逐像素计算的，可以实现光效、色散、扭曲等 CSS 无法实现的效果
- GPU 加速，性能优异
- 与 HyperFrames 渲染管线原生集成

## 转场选择表

| 使用场景 | 推荐转场 | 情绪 | 替代选项 |
|---------|---------|------|---------|
| 段落内递进（最常用） | light-leak | 有机、胶片感 | CSS crossfade（降级方案） |
| 概念递进 | cinematic-zoom | 聚焦、进入 | sdf-iris |
| 情绪转折 | glitch | 碎裂、不安 | thermal-distortion |
| 大段落切换 | flash-through-white | 干净、权威 | domain-warp-dissolve |
| 数据→结论 | whip-pan | 速度、动感 | swirl-vortex |
| 危机/紧张 | chromatic-radial-split | 色散、不稳定 | gravitational-lens |
| 揭示/揭晓 | ripple-waves | 涟漪扩散 | cross-warp-morph |
| 主题升华 | light-leak | 向上、温暖 | ridged-burn |

## 使用规则

### 安装与引用

```bash
npx hyperframes add <name>
```

安装后的 shader 转场作为 block 存在，在 HTML 中通过 `data-composition-src` 属性引用。

### 时长控制

转场时长控制在 **0.4s - 0.8s** 之间。Shader 转场视觉信息量大，拖太长反而显得拖沓。

### 数量限制

- **全片 1-2 种主转场**：段落间 1 种，段落内 1 种
- `flash-through-white`：全片最多 2 次，间隔至少 8 秒
- `glitch`：全片最多 2 次（效果太强烈，用多了显得廉价）
- `chromatic-radial-split`：全片最多 1 次（留给最高潮的情绪转折）

### 搭配原则

- 段落内递进用"轻"转场（light-leak, cinematic-zoom）
- 段落间切换用"重"转场（flash-through-white, domain-warp-dissolve）
- 情绪转折用"裂"转场（glitch, chromatic-radial-split）

## 完整转场列表

### 段落内递进型（轻）

| 转场名 | 描述 | 时长建议 | 安装命令 |
|--------|------|---------|----------|
| light-leak | 模拟胶片漏光效果，温暖有机 | 0.6s | `npx hyperframes add light-leak` |
| cinematic-zoom | 电影级推进聚焦，配合景深虚化 | 0.6s | `npx hyperframes add cinematic-zoom` |
| sdf-iris | SDF 虹膜光圈收缩/展开 | 0.5s | `npx hyperframes add sdf-iris` |
| ripple-waves | 涟漪波纹从中心扩散 | 0.5s | `npx hyperframes add ripple-waves` |
| cross-warp-morph | 交叉扭曲变形过渡 | 0.6s | `npx hyperframes add cross-warp-morph` |

### 情绪转折型（裂）

| 转场名 | 描述 | 时长建议 | 安装命令 |
|--------|------|---------|----------|
| glitch | 数字故障艺术效果，RGB 通道分离+块位移 | 0.5s | `npx hyperframes add glitch` |
| chromatic-radial-split | 径向色散分裂，不稳定感 | 0.6s | `npx hyperframes add chromatic-radial-split` |
| thermal-distortion | 热浪扭曲变形，不安定感 | 0.5s | `npx hyperframes add thermal-distortion` |
| gravitational-lens | 引力透镜弯曲效果 | 0.6s | `npx hyperframes add gravitational-lens` |

### 段落切换型（重）

| 转场名 | 描述 | 时长建议 | 安装命令 |
|--------|------|---------|----------|
| flash-through-white | 闪白过渡，干净权威 | 0.4s | `npx hyperframes add flash-through-white` |
| domain-warp-dissolve | 域扭曲溶解，超现实感 | 0.6s | `npx hyperframes add domain-warp-dissolve` |
| ridged-burn | 脊状灼烧过渡 | 0.5s | `npx hyperframes add ridged-burn` |

### 速度/动感型

| 转场名 | 描述 | 时长建议 | 安装命令 |
|--------|------|---------|----------|
| whip-pan | 快速摇摄模糊过渡，速度感十足 | 0.5s | `npx hyperframes add whip-pan` |
| swirl-vortex | 漩涡扭曲吸入效果 | 0.6s | `npx hyperframes add swirl-vortex` |

## CSS 降级方案

如果因环境限制无法安装 shader 转场，使用 GSAP 交叉淡入淡出作为降级方案：

```js
// CSS 降级：GSAP 交叉淡入淡出
gsap.fromTo(
  nextSlide,
  { autoAlpha: 0 },
  { autoAlpha: 1, duration: 0.4, ease: "power2.inOut" }
);
```

这是**可接受但视觉效果有损**的方案。优先始终是官方 shader 转场。
