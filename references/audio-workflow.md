---
name: audio-workflow
description: HyperFrames/Remotion 双后端的旁白、BGM、字幕时间戳与音效规划。只写入 spec，不在分镜阶段执行生成或转码。
---

# BGM / TTS / 音频时间轴

## 共同原则

- 本 Skill 只规划音频，不执行 TTS、转录、转码或素材下载。
- 没有真实逐词时间戳时写 `[待转录]`，禁止按字数均分伪造时间戳。
- 语速基准：中文约 4 字/秒，最终以真实音频时长和转录结果为准。

## HyperFrames 下游工作流

本 Skill 只在 spec 中规划音频，不执行以下命令。命令由渲染端在用户批准后运行。

```bash
# 1. 使用本地 Kokoro 生成中文 TTS 旁白
npx hyperframes tts "逐字稿全文" --voice zf_xiaobei --speed 1.0 -o assets/narration.wav

# 2. 转录中文时间戳（如需逐词高亮；禁止使用 .en 模型）
npx hyperframes transcribe assets/narration.wav --model small --language zh

# 3. 根据时间戳对齐 GSAP 字幕动画
```

`--speed` 用于调整语速；实际可用参数由渲染端按当前 CLI 复核。

## Remotion 下游契约

Remotion spec 不绑定某个 TTS 提供商。已有音频放入下游项目 `public/`，用 `staticFile()` 引用；音频组件优先使用 `@remotion/media` 的 `<Audio>`。

```yaml
旁白:
  src: staticFile("audio/narration.wav")
  from: 0
  durationInFrames: [整数]
  trimBefore: 0
  trimAfter: [整数帧或 null]
  volume: 1
BGM:
  src: staticFile("audio/bgm.mp3")
  from: 0
  durationInFrames: [总帧数]
  volume: [静态值或 frame-driven 函数契约]
字幕时间戳: [真实词级数据路径或 `[待转录]`]
```

- `from`、`durationInFrames`、trim 均以整数帧为真源。
- 音量变化写成 `frame → interpolate() → volume` 契约，不使用 CSS/运行时时钟。
- 远程音频必须记录稳定 URL、许可与本地 fallback；不要假定渲染时网络可用。

## BGM 参数模板

```yaml
类型: 氛围电子 (ambient electronic)
特征: 低沉 sub-bass pad + 轻微 rhythmic pulse (80-90 bpm)
旁白存在时 volume: 0.12 (作为底色, 不抢旁白)
旁白静默时 volume: 0.20
段落切换 swell: 0.12 → 0.22 → 0.12, 0.5s 内完成
来源: Pixabay Music / YouTube Audio Library
```

## 音效使用纪律

- 仅用于关键动效的同步强调（弹入/闪屏/揭晓）
- 每个音效标注触发时间码（对齐 GSAP timeline position）
- volume: 0.15-0.35，不盖过旁白
- 无音效的 Scene 必须写 `🔒 音效: 无`

## 音频标签示例

```html
<!-- BGM: 全片 -->
<audio id="bgm" data-start="0" data-duration="411"
  data-track-index="4" src="assets/bgm.mp3" loop data-volume="0.12">
</audio>

<!-- TTS 旁白: 全片 -->
<audio id="narration" data-start="0" data-duration="411"
  data-track-index="5" src="assets/narration.wav" data-volume="1">
</audio>
```
