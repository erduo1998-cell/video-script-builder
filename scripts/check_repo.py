#!/usr/bin/env python3
"""Validate the public repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
HF_TEMPLATE = ROOT / "templates/video-script-spec-template.md"
REMOTION_TEMPLATE = ROOT / "templates/video-script-spec-remotion-template.md"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def check_required_files() -> None:
    required = [
        "SKILL.md",
        "README.md",
        "README.en.md",
        "LICENSE",
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "agents/openai.yaml",
        "references/remotion-patterns.md",
        "templates/video-script-spec-template.md",
        "templates/video-script-spec-remotion-template.md",
        "docs/images/video-script-builder-hero.png",
        "docs/images/workflow.svg",
        "docs/images/handoff-boundary.svg",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
        return None
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        fail("SKILL.md frontmatter is not closed")
        return None
    return parts[1], parts[2]


def check_skill_contract() -> None:
    text = SKILL.read_text(encoding="utf-8")
    split = split_frontmatter(text)
    if split is None:
        return
    frontmatter, body = split

    keys = {
        match.group(1)
        for line in frontmatter.splitlines()
        if (match := re.match(r"^([A-Za-z][A-Za-z0-9_-]*):", line))
    }
    if keys != {"name", "description"}:
        fail(f"SKILL.md frontmatter keys must be name + description only, got {sorted(keys)}")
    if "name: video-script-builder" not in frontmatter:
        fail("SKILL.md name must be video-script-builder")

    outputs = set(re.findall(r"video-spec-[a-z0-9-]+\.md", frontmatter))
    expected_outputs = {"video-spec-hf.md", "video-spec-remotion.md"}
    if outputs != expected_outputs:
        fail(f"frontmatter deliverables must be exactly {sorted(expected_outputs)}, got {sorted(outputs)}")
    if "exactly one" not in frontmatter.lower():
        fail("frontmatter must state the exactly-one deliverable boundary")
    if len(text.splitlines()) >= 500:
        fail(f"SKILL.md must stay below 500 lines, got {len(text.splitlines())}")
    if "# Video Script Builder v1.4.0" not in body:
        fail("SKILL.md release version is not v1.4.0")

    gate_match = re.search(r"## 12 条硬阻断\n(?P<section>.*?)(?=\n## )", body, re.S)
    if gate_match is None:
        fail("SKILL.md is missing the 12-gate section")
    else:
        gates = [int(value) for value in re.findall(r"(?m)^(\d+)\. \*\*", gate_match.group("section"))]
        if gates != list(range(1, 13)):
            fail(f"SKILL.md gates must be numbered 1-12 exactly, got {gates}")

    routing_tokens = [
        "新项目且用户未指定时，为兼容旧行为直接默认 HyperFrames",
        "同时找到两种 spec 或多个候选时",
        "迁移模式",
        "框架继承不等于允许修改已有文件",
        "你是想在这个基础上改，还是新开一份？",
        "不得覆盖现有 spec",
        "禁止生成“通用双框架 spec”",
        "templates/video-script-spec-template.md",
        "templates/video-script-spec-remotion-template.md",
    ]
    for token in routing_tokens:
        if token not in body:
            fail(f"SKILL.md routing contract is missing: {token}")

    referenced = set(re.findall(r"`((?:references|templates)/[^`]+\.md)`", text))
    for relative in sorted(referenced):
        if not (ROOT / relative).is_file():
            fail(f"SKILL.md references missing file: {relative}")


def numbered_sections(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?m)^## (\d+)\. ([^\n]+)$", text)


def check_backend_templates() -> None:
    hf = HF_TEMPLATE.read_text(encoding="utf-8")
    remotion = REMOTION_TEMPLATE.read_text(encoding="utf-8")
    expected_headings = [
        ("1", "视频基本盘"),
        ("2", "叙事结构"),
        ("3", "表达手段"),
        ("4", "视觉与渲染规范"),
        ("5", "素材清单"),
        ("6", "分镜表"),
        ("7", "音频时间轴"),
        ("8", "参考与反例"),
        ("9", "开放问题"),
    ]
    for name, text in [("HyperFrames", hf), ("Remotion", remotion)]:
        headings = numbered_sections(text)
        if headings[:9] != expected_headings:
            fail(f"{name} template does not preserve the shared sections 1-9: {headings[:9]}")
        if len(headings) != 10 or headings[-1][0] != "10" or "渲染反馈" not in headings[-1][1]:
            fail(f"{name} template must end with section 10 渲染反馈")

    hf_required = [
        "v1.4.0",
        "video-spec-hf.md",
        "🔒 渲染框架：HyperFrames",
        "data-start",
        "data-duration",
        "npx hyperframes add",
        "GSAP",
    ]
    remotion_required = [
        "v1.4.0",
        "video-spec-remotion.md",
        "🔒 渲染框架：Remotion",
        "Composition",
        "Sequence",
        "useCurrentFrame",
        "interpolate",
        "spring",
        "staticFile",
        "Audio",
        "TransitionSeries",
        "startFrame",
        "durationInFrames",
        "Σ Scene.sequenceDurationInFrames - Σ Transition.durationInFrames",
        "duration 是正整数；offset 是有限整数",
        "staticFile('audio/voice.wav')",
    ]
    for token in hf_required:
        if token not in hf:
            fail(f"HyperFrames template is missing: {token}")
    for token in remotion_required:
        if token not in remotion:
            fail(f"Remotion template is missing: {token}")

    for forbidden in ["useCurrentFrame", "durationInFrames", "<Composition", "staticFile("]:
        if forbidden in hf:
            fail(f"HyperFrames template contains Remotion execution token: {forbidden}")
    for forbidden in ["npx hyperframes add", "data-start", "data-duration", "GSAP"]:
        if forbidden in remotion:
            fail(f"Remotion template contains HyperFrames execution token: {forbidden}")
    if "S01 from +" in remotion or "[from + duration]" in remotion:
        fail("Remotion TransitionSeries audit table must use derived startFrame, not from")


def check_bilingual_release_contract() -> None:
    zh = read("README.md")
    en = read("README.en.md")
    stable_tokens = ["1.4.0", "HyperFrames", "Remotion", "video-spec-hf.md", "video-spec-remotion.md"]
    for relative, text in [("README.md", zh), ("README.en.md", en)]:
        for token in stable_tokens:
            if token not in text:
                fail(f"{relative} is missing release contract token: {token}")
    if "一次任务只会交付一个" not in zh:
        fail("README.md must state the one-spec-per-run contract")
    if "exactly one" not in en:
        fail("README.en.md must state the exactly-one contract")
    if "不是视频渲染器" not in zh or "does **not** render video" not in en:
        fail("bilingual READMEs must keep the non-renderer boundary")

    openai = read("agents/openai.yaml")
    if "HyperFrames or Remotion" not in openai:
        fail("agents/openai.yaml is still renderer-specific")
    changelog = read("CHANGELOG.md")
    if not changelog.startswith("# Changelog\n\n## 1.4.0 — 2026-08-10"):
        fail("CHANGELOG.md must start with the v1.4.0 release")
    security = read("SECURITY.md")
    if "`1.4.x`" not in security:
        fail("SECURITY.md maintained version is not 1.4.x")


def iter_text_files() -> list[Path]:
    suffixes = {".md", ".yaml", ".yml", ".json", ".txt"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in suffixes and ".git" not in path.parts
    ]


def check_local_links() -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "#", "mailto:")) or " " in target:
                continue
            clean = target.split("#", 1)[0]
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                fail(f"broken local link in {path.relative_to(ROOT)}: {target}")


def check_privacy_and_stale_names() -> None:
    absolute_home = re.compile(r"/Users/[A-Za-z0-9._-]+/")
    token_patterns = [
        re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
        re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    ]
    stale_transition = re.compile(
        r"(?<!transitions-)\b(?:3d|blur|cover|destruction|dissolve|distortion|"
        r"grid|light|mechanical|other|push|radial|scale)-transitions\b"
    )
    stale_contracts = [
        "唯一交付物仍是 `video-spec-hf.md`",
        "唯一交付物始终是 `video-spec-hf.md`",
        "single-deliverable boundary: `video-spec-hf.md` only",
    ]

    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if absolute_home.search(text):
            fail(f"absolute user path found in {relative}")
        if any(pattern.search(text) for pattern in token_patterns):
            fail(f"possible secret found in {relative}")
        if stale_transition.search(text):
            fail(f"stale HyperFrames transition bundle name found in {relative}")
        if "caption-pillar-karaoke" in text:
            fail(f"stale caption component name found in {relative}")
        if relative.as_posix() != "CHANGELOG.md":
            for phrase in stale_contracts:
                if phrase in text:
                    fail(f"stale single-backend contract found in {relative}: {phrase}")


def check_delivery_boundary() -> None:
    forbidden_files = {
        "video-spec-hf.md",
        "video-spec-remotion.md",
        "index.html",
        "preview.html",
        "Root.tsx",
        "hyperframes.json",
    }
    forbidden_suffixes = {".mp4", ".mov", ".webm"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if path.is_file() and (path.name in forbidden_files or path.suffix.lower() in forbidden_suffixes):
            fail(f"out-of-scope renderer artifact found: {relative}")
        if path.is_file() and path.name.startswith("remotion.config."):
            fail(f"out-of-scope Remotion config found: {relative}")
        if path.is_dir() and path.name == "compositions":
            fail(f"out-of-scope compositions directory found: {relative}")


def check_hyperframes_items() -> None:
    verified_file = ROOT / "tests/verified-hyperframes-items.txt"
    verified = {
        line.strip()
        for line in verified_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    referenced: set[str] = set()
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        referenced.update(re.findall(r"npx\s+hyperframes\s+add\s+([a-z0-9-]+)", path.read_text(encoding="utf-8")))
    unknown = sorted(referenced - verified)
    if unknown:
        fail(f"unverified HyperFrames registry items: {', '.join(unknown)}")


def check_visuals() -> None:
    for relative in ["docs/images/workflow.svg", "docs/images/handoff-boundary.svg"]:
        try:
            ET.parse(ROOT / relative)
        except ET.ParseError as exc:
            fail(f"invalid SVG {relative}: {exc}")
    workflow = read("docs/images/workflow.svg")
    handoff = read("docs/images/handoff-boundary.svg")
    for token in ["HyperFrames", "Remotion"]:
        if token not in workflow or token not in handoff:
            fail(f"README diagrams must mention both renderers; missing {token}")

    hero = ROOT / "docs/images/video-script-builder-hero.png"
    if hero.is_file() and hero.stat().st_size < 100_000:
        fail("README hero image looks unexpectedly small")


def main() -> int:
    check_required_files()
    check_skill_contract()
    check_backend_templates()
    check_bilingual_release_contract()
    check_local_links()
    check_privacy_and_stale_names()
    check_delivery_boundary()
    check_hyperframes_items()
    check_visuals()

    if ERRORS:
        print("Repository validation failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
