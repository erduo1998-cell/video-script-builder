# Video Script Builder

Turn a Chinese voiceover transcript into a precise, component-first HyperFrames storyboard specification.

> The Chinese [README](./README.md) is the primary beginner guide and includes illustrated installation, workflow, troubleshooting, and handoff instructions.

## What it does

The skill helps an AI coding agent:

- extract narrative beats and an emotion curve from a transcript;
- define an executable visual intent card;
- inventory assets before designing scenes;
- select HyperFrames blocks and components;
- plan exact scene timing, GSAP glue, captions, and transitions;
- enforce 12 hard quality gates;
- deliver one file: `video-spec-hf.md`.

It does **not** render video, create `index.html`, download assets, or output an MP4.

## Install

Claude Code:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/erduo1998-cell/video-script-builder.git \
  ~/.claude/skills/video-script-builder
```

Codex:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/erduo1998-cell/video-script-builder.git \
  ~/.codex/skills/video-script-builder
```

Start a new agent session after installation.

## Use

```text
Use video-script-builder to turn the following Chinese transcript into a
HyperFrames storyboard spec.
Platform: TikTok/Douyin
Aspect ratio: 9:16
Visual direction: high contrast, generous negative space, restrained technology

[Paste transcript here]
```

If automatic discovery fails, ask the agent to read `video-script-builder/SKILL.md` explicitly. Clients that support `$skill-name` invocation may use `$video-script-builder`.

## Requirements

- The skill itself needs no API key, Node.js, FFmpeg, or renderer.
- The downstream HyperFrames agent needs the current HyperFrames toolchain.
- A transcript should ideally contain at least 100 Chinese characters, three semantic turns, and a concise ending takeaway.
- Registry items change over time. Recheck component names against the current [official HyperFrames registry](https://github.com/heygen-com/hyperframes/tree/main/registry) before rendering.

## Validate

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

See [CONTRIBUTING.md](./CONTRIBUTING.md), [SECURITY.md](./SECURITY.md), and the [MIT License](./LICENSE).
