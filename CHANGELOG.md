# Changelog

## 1.4.0 — 2026-08-10

- Added a first-class Remotion storyboard path with integer-frame timing, React component contracts, deterministic animation rules, `staticFile()` asset bindings, audio timing, and transition-overlap accounting.
- Preserved the existing HyperFrames path and its default behavior for requests that do not specify a renderer.
- Split renderer output into two mutually exclusive deliverables: `video-spec-hf.md` or `video-spec-remotion.md`, exactly one per run.
- Added cross-renderer migration rules that preserve directing decisions without overwriting the source spec.
- Updated both templates, 12 quality gates, bilingual documentation, diagrams, community templates, and repository contract tests.

## 1.3.0 — 2026-07-29

First public release.

- Added the visual intent card and taste layer.
- Added 12 hard storyboard quality gates.
- Clarified the single-deliverable boundary: `video-spec-hf.md` only.
- Updated HyperFrames transition bundle names against the official registry.
- Corrected downstream Chinese TTS and transcription examples.
- Added Codex interface metadata, beginner documentation, diagrams, CI, tests, security policy, and contribution guidance.
