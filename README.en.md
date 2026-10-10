# Video Script Builder

Turn a Chinese voiceover transcript into a precise, renderer-bound storyboard specification for **HyperFrames or Remotion**.

> The Chinese [README](./README.md) is the primary beginner guide and includes the full illustrated workflow, troubleshooting, and handoff instructions.

[Membership & help](#membership-help)

## What changed in v1.4.0

The skill now separates shared directing decisions from renderer-specific implementation contracts:

- visual intent, narrative beats, asset inventory, pacing, captions, and taste are shared;
- HyperFrames uses registry components, seconds, and GSAP glue;
- Remotion uses React component contracts, integer frames, and deterministic frame-driven animation.

Each run delivers **exactly one** selected file:

| Renderer | Deliverable | Timing source of truth | Implementation contract |
|---|---|---|---|
| HyperFrames | `video-spec-hf.md` | seconds, `data-start`, `data-duration` | official components + GSAP glue |
| Remotion | `video-spec-remotion.md` | integer `startFrame` / `durationInFrames` | React components + `useCurrentFrame()` / `interpolate()` / `spring()` |

It never emits a mixed “universal” spec. For backward compatibility, a new project still defaults to HyperFrames unless Remotion is explicitly requested.

## What it does

The skill helps an AI coding agent:

- extract narrative beats and an emotion curve from a Chinese transcript;
- define an executable visual intent card and recurring motif;
- inventory real assets before designing scenes;
- select HyperFrames components or define implementable Remotion component contracts;
- plan exact scene timing, animation, captions, transitions, and audio;
- enforce 12 renderer-aware quality gates;
- hand one Markdown spec to the matching renderer agent.

It does **not** render video, create an HTML/React composition, install dependencies, download assets, or output an MP4.

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

Start a new agent session after installation or update.

## Use

HyperFrames (also the default when the renderer is omitted):

```text
Use video-script-builder to turn the following Chinese transcript into a
HyperFrames storyboard spec.
Platform: TikTok/Douyin
Aspect ratio: 9:16
Visual direction: high contrast, generous negative space, restrained technology

[Paste transcript here]
```

Remotion:

```text
Use video-script-builder to turn the following Chinese transcript into a
Remotion storyboard spec.
Platform: TikTok/Douyin
Aspect ratio: 9:16
Frame rate: 30fps
Visual direction: high contrast, generous negative space, restrained technology

[Paste transcript here]
```

If automatic discovery fails, ask the agent to read `video-script-builder/SKILL.md` explicitly. Clients that support `$skill-name` invocation may use `$video-script-builder`.

## Renderer contracts

### HyperFrames

The output records registry component names, `npx hyperframes add` dependencies, scene seconds, material bindings, GSAP glue, captions, and shader transitions. The existing `video-spec-hf.md` iteration workflow remains compatible with v1.3.

### Remotion

The output records Composition settings, integer scene frames, React component names and serializable props, `staticFile()` asset bindings, frame-driven animation formulas, Sequence or TransitionSeries timing, transition overlap, and Audio frame ranges.

Remotion is not treated as a built-in visual component library. Missing components or third-party libraries are marked for downstream implementation and license review instead of being invented.

## Routing behavior

1. An explicitly requested renderer wins.
2. A single existing `video-spec-hf.md` or `video-spec-remotion.md` keeps its renderer, but is not modified unless the user confirms iteration.
3. Multiple candidates are listed for selection.
4. A new project with no renderer specified defaults to HyperFrames.
5. Cross-renderer migration reuses directing decisions but creates a new target spec; it does not overwrite or search-and-replace the source.

If one spec already exists and the user supplies a new transcript without explicitly asking to modify it, the agent must ask whether to iterate or start in a new project directory. It never silently overwrites the existing spec.

## Requirements and sources of truth

- The skill itself needs no API key, Node.js, FFmpeg, or renderer installation.
- A transcript should ideally contain at least 100 Chinese characters, three semantic turns, and a concise ending takeaway.
- Recheck HyperFrames components against the current [official registry](https://github.com/heygen-com/hyperframes/tree/main/registry) before rendering.
- Recheck Remotion APIs and the target project version against the current [official documentation](https://www.remotion.dev/docs/) before implementation.

<a id="membership-help"></a>

## Membership & help

Erduo’s **无限涌动 SURGE Seed Membership** offers lifetime membership status, project resources, video examples, ongoing updates, and text-based Q&A. You can also connect your own AI to the member resources you are entitled to use. It is an optional resource for learning storyboarding and visual storytelling; available materials and current benefits are listed on the website.

[Explore membership](https://erduo.art/site/join) · [Register / sign in and purchase](https://login.erduo.art/purchase/checkout) · [Discuss custom services](https://erduo.art/site/business)

Using this project, including commercially under its [MIT License](./LICENSE), does not require membership. Text-based Q&A excludes remote installation, hands-on engineering troubleshooting, and one-to-one done-for-you work. Video production and other custom services require separate scope and pricing discussions with the author through the website. This skill still delivers one storyboard spec; rendering belongs to the matching renderer agent.

## Validate

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

See [CONTRIBUTING.md](./CONTRIBUTING.md), [SECURITY.md](./SECURITY.md), and the [MIT License](./LICENSE).
