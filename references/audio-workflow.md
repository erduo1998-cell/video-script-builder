---
name: audio-workflow
description: TTS 旁白生成工作流 + BGM 参数模板 + 音效使用纪律。分镜第六步素材绑定时对照使用。
---

# BGM / TTS / 音频时间轴

## 下游 TTS 工作流

本 Skill 只在 spec 中规划音频，不执行以下命令。命令由渲染端在用户批准后运行。

```bash
# 1. 使用本地 Kokoro 生成中文 TTS 旁白
npx hyperframes tts "逐字稿全文" --voice zf_xiaobei --speed 1.0 -o assets/narration.wav

# 2. 转录中文时间戳（如需逐词高亮；禁止使用 .en 模型）
npx hyperframes transcribe assets/narration.wav --model small --language zh

# 3. 根据时间戳对齐 GSAP 字幕动画
```

语速基准：中文 4 字/秒。`--speed` 参数调整。

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
