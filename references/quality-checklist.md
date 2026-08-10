---
name: quality-checklist
description: 输出 HyperFrames 或 Remotion 分镜 spec 前的 12 条硬性自检清单。任何一条未通过，不交付。
---

# 双后端质量自检清单

先锁定 `renderer`，再检查共同门禁和对应框架门禁。一次只检查并交付一种 spec。

## 1. 框架绑定

- [ ] `hyperframes` 只输出 `video-spec-hf.md`；`remotion` 只输出 `video-spec-remotion.md`。
- [ ] 开篇明确声明目标框架、时间模型与下游交接对象。
- [ ] spec 没有混写两套实现：HF Scene 不出现 `useCurrentFrame()`；Remotion Scene 不出现 GSAP timeline 或 `data-start`。
- [ ] 迁移任务生成目标框架新 spec，不做字符串替换式“伪迁移”。

## 2. 单一交付

- [ ] 本次只交付一个 `.md` spec。
- [ ] 未创建 `index.html`、`Root.tsx`、composition、脚手架、配置、素材下载或 MP4。
- [ ] spec 不包含可直接复制成完整项目的 HTML/TSX。

## 3. 结构完整

- [ ] 意图卡 5 字段齐全：视觉人格、情绪-视觉映射、视觉母题、参考拆解、反调预警。
- [ ] §1–10 全部存在；未知内容写 `[待用户确认]`、`[待获取]`、`[待转录]` 或 `[需渲染端实现/复核]`，不留空。
- [ ] 核心信息 ≤12 字；同质化反例至少覆盖视觉、叙事、节奏。
- [ ] 品味自检说明全片最空镜、最满镜与金句前的“吸气点”。

## 4. 时间闭合

- [ ] Scene 起点、时长均非负，按顺序覆盖全片，不存在无意的空洞。
- [ ] 结尾与目标总时长一致（允许人类参考秒数 ±0.5s）。
- [ ] 旁白字数与 Scene 时长匹配；停顿有明确用途。
- [ ] HF：最后镜 `data-start + data-duration = 总时长`。
- [ ] Remotion：`startFrame`、`durationInFrames`、转场均为整数帧；普通 Sequence 才将 startFrame 映射为 `from`，TransitionSeries 的 startFrame 只作派生审计坐标；`总帧数 = Σ sceneFrames - Σ transitionFrames`，Overlay 不扣时长。

## 5. 镜头覆盖

- [ ] 每镜至少绑定一个真实素材、HF 官方组件，或 Remotion 组件契约。
- [ ] 所有“已有/本地”素材路径真实；待获取项写清来源、关键词、用途、许可/验收和 fallback。
- [ ] 纯文字镜 ≤20%；素材/视觉主导镜 ≥80%。
- [ ] 不存在把占位图、虚构组件或未核实包名说成可用实现的情况。

## 6. 开镜锚点

- [ ] Hook 落在前 3 秒（教程型最多放宽到 5 秒）。
- [ ] Hook 有占主体面积的组件/素材/可实现组件契约，不是纯文字或只有底板。
- [ ] 金句与首尾呼应也有真实视觉方案和 fallback。

## 7. 字幕去重

- [ ] 屏显文字只有 1–4 个关键词，不逐字重复字幕/旁白。
- [ ] 全片至少两种字幕表现，切换理由与段落情绪一致。
- [ ] 无真实词级时间戳时标 `[待转录]`，未按字数伪造精确时间。
- [ ] 字幕安全区、行宽、字号与画幅适配。

## 8. 动画确定性

- [ ] 所有动画输入区间落在 Scene 局部时间内。
- [ ] HF：只用绝对 position、transform + `autoAlpha`；无链式 delay、布局属性 tween、`opacity` 或 `repeat:-1`。
- [ ] HF：GSAP 只编排跨组件显隐/切换，不重写组件内部动画。
- [ ] Remotion：只用 `useCurrentFrame()` + `interpolate()` / `spring()` 等帧驱动值；无 CSS transition、`setTimeout`、wall-clock 或未设 seed 的随机数。
- [ ] Remotion：每个 `interpolate()` 说明 clamp；spring 写清 fps、局部 frame、config 或时长边界。

## 9. 多样性与真实能力

- [ ] 同一主组件/构图连续不超过 3 镜；连续两镜不靠同一理由选型。
- [ ] 全片至少两种转场；任一强转场 ≤镜数 30%，闪白与 glitch 各 ≤2 次。
- [ ] 转场不是每镜强制添加；普通 cut 有明确位置。
- [ ] HF：组件名在 catalog/官方 registry 中可核对，无法核对就标 `[需渲染端复核]`；L1 3D/VFX 至少两种（底板不计）。
- [ ] HF：每个依赖逐项写完整 `npx hyperframes add <真实组件名>`；交付文件中不存在 `<name>`、`<组件名>` 等模板占位。
- [ ] Remotion：自定义组件写清 props、素材、动画与验收；3D/WebGL/额外库标 `[需渲染端选库/复核许可]`。

## 10. 意图一致

- [ ] 每镜的“为什么”≤20 字，并对应意图卡中的具体一条。
- [ ] 视觉母题在 hook、主体、收尾至少各出现一次，且形态有变化。
- [ ] 删除母题后叙事会损失含义，而不是装饰性贴图。
- [ ] 参考拆解写的是可执行特征，不是只报品牌/作者名。

## 11. 节奏与密度

- [ ] 最空镜与最满镜密度差 ≥2 档；密镜 ≤总镜数 25%。
- [ ] 连续两镜不完全同密度；连续三镜不完全同冷暖。
- [ ] 相邻镜时长有变化；素材镜有足够阅读时间。
- [ ] 至少有一段 ≥2 秒的“空/疏”呼吸区；高潮前有蓄力。
- [ ] 音效只强调关键动作，不盖过旁白；BGM、旁白、音效起止与音量齐全。

## 12. 可交接

- [ ] 每镜的路径、依赖、fallback、开放问题无歧义。
- [ ] HF：安装命令与 GSAP 胶水可由 HyperFrames 渲染 Agent 复核执行。
- [ ] Remotion：Composition 参数、Sequence 帧区间、组件契约、素材绑定、转场 overlap 与音频帧区间齐全。
- [ ] §10 留给对应渲染 Agent 回填：直接可执行项、修改项、理解偏差和框架版本。
- [ ] 收尾只报告 spec 统计与下一步交接，然后停止。

任何一项失败都先修正，不把问题推给渲染端。
