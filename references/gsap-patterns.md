---
name: gsap-patterns
description: GSAP 编排 Pattern 代码示例。v1.2：GSAP 是胶水，不是画笔。组件负责自身动画，GSAP 只负责跨组件编排。
---

# GSAP 编排 Pattern

## 目录

- [核心理念](#核心理念)
- [Pattern 速查](#pattern-速查)
- [旧 Pattern 迁移指引](#旧-pattern-迁移指引)
- [Easing 速查](#easing-速查)
- [禁止事项](#禁止事项)

## 核心理念

**GSAP 是胶水，不是画笔。**

v1.2 开始，动画不再手写。官方组件（通过 `data-composition-src` 引用）负责自身的入场/退场/循环动画。GSAP 的唯一职责：协调组件之间、素材之间、字幕之间的时序关系。

- 组件自己动 → GSAP 只管什么时候让它出现/消失
- 素材（图片/视频）→ GSAP 负责入场微动效（scale + autoAlpha）
- 字幕 → GSAP 负责在正确的时间点切换文本

## Pattern 速查

```javascript
// ═══════════════════════════════════════
// Pattern 1: 组件入场编排
// 组件自身有入场动画，GSAP 只控制显示时机
// ═══════════════════════════════════════
// HTML: <div data-composition-src="compositions/data-chart.html"
//       data-start="12.0" data-duration="8.0">
tl.set("#scene-03", { autoAlpha: 1 }, 12.0);

// ═══════════════════════════════════════
// Pattern 2: 素材交叉淡入淡出
// 淡出旧素材，同时淡入新素材（overlap = crossfade）
// ═══════════════════════════════════════
tl.to("#scene-A-material", { autoAlpha: 0, duration: 0.4 }, 8.5);
tl.from("#scene-B-material", { autoAlpha: 0, duration: 0.4 }, "<");

// ═══════════════════════════════════════
// Pattern 3: 字幕文本切换
// 在旁白时间点切换字幕内容
// ═══════════════════════════════════════
tl.call(() => {
  document.getElementById("caption-text").textContent = "新的字幕";
}, [], 15.0);

// ═══════════════════════════════════════
// Pattern 4: Shader 转场触发
// Shader 转场作为子 composition 引用，GSAP 只管显隐
// ═══════════════════════════════════════
tl.set("#transition-glitch", { autoAlpha: 1 }, 20.0);
tl.set("#transition-glitch", { autoAlpha: 0 }, 24.0);

// ═══════════════════════════════════════
// Pattern 5: 素材/截屏入场
// 图片或视频素材入场，微 scale 增加纵深感
// ═══════════════════════════════════════
tl.from("#scene-material", {
  scale: 1.05,
  autoAlpha: 0,
  duration: 0.6,
  ease: "power2.out"
}, 5.0);

// ═══════════════════════════════════════
// Pattern 6: 组件退场编排
// 组件自身有退场动画，GSAP 控制在何时触发隐藏
// ═══════════════════════════════════════
tl.set("#scene-03", { autoAlpha: 0 }, 20.0);
```

## 旧 Pattern 迁移指引

v1.1 手写动画 pattern 已被官方组件取代：

| v1.1 Pattern | v1.2 替代方案 |
|-------------|-------------|
| anim-slam | `caption-kinetic-slam`（全屏大字 slam）或 GSAP `back.out(1.7)` 手动实现 |
| anim-cascade | `caption-clip-wipe`（逐词 clip-path 揭示）或 `caption-pill-karaoke`（逐词高亮） |
| anim-breathe | 任何组件自带呼吸态；若需手写，按 Scene 时长计算有限 `repeat`，禁止无限循环 |
| anim-flash | `caption-highlight`（TikTok 式高亮扫过）或 GSAP 颜色 flash |
| anim-weight | `caption-weight-shift`（字重渐变过渡） |
| anim-track | `caption-editorial-emphasis`（字距/大小对比）或 GSAP `letterSpacing` |
| anim-scribe | `caption-gradient-fill`（下划线效果）或 GSAP `scaleX` 手写 |
| 手写 crossfade | `light-leak` 或 `transitions-dissolve`（shader 转场，视觉效果远超 CSS） |
| 手写 line-sweep | `whip-pan` 或 `transitions-push`（shader 转场替代扫换） |
| 手写 卡片光晕 | `shimmer-sweep` + `vignette` 组合，或 `liquid-glass-widgets` |

## Easing 速查

| ease | 感觉 | 适用场景 |
|------|------|---------|
| `"power2.out"` | 减速停止 | 最常用，通用入场 |
| `"power3.out"` | 更强减速 | 需要力度感的入场 |
| `"power4.in"` | 加速启动 | 退场、消失 |
| `"back.out(1.7)"` | 超出再回弹 | 弹入效果，强调元素 |
| `"elastic.out(1,0.3)"` | 弹性晃动 | 趣味性入场，少用 |
| `"sine.inOut"` | 平滑对称 | 呼吸态、循环动画 |

## 禁止事项

- ❌ 不用 `delay` 链式调用 — 用 timeline position parameter
- ❌ 不用 `opacity` — 用 `autoAlpha`
- ❌ 不动 `width/height/top/left` — 用 `x/y/scale`
- ❌ 不创建 tweens 在 DOM 元素存在之前
- ❌ 不手写组件内部动画 — 交给官方组件
- ❌ 不用 GSAP 做复杂视觉特效 — 用 shader 转场组件
