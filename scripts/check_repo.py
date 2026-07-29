#!/usr/bin/env python3
"""Validate the public repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


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
        "templates/video-script-spec-template.md",
        "docs/images/video-script-builder-hero.png",
        "docs/images/workflow.svg",
        "docs/images/handoff-boundary.svg",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")


def check_skill_contract() -> None:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
        return

    parts = text.split("---\n", 2)
    if len(parts) != 3:
        fail("SKILL.md frontmatter is not closed")
        return

    keys = {
        match.group(1)
        for line in parts[1].splitlines()
        if (match := re.match(r"^([A-Za-z][A-Za-z0-9_-]*):", line))
    }
    if keys != {"name", "description"}:
        fail(f"SKILL.md frontmatter keys must be name + description only, got {sorted(keys)}")

    if "name: video-script-builder" not in parts[1]:
        fail("SKILL.md name must be video-script-builder")
    if "video-spec-hf.md only" not in parts[1]:
        fail("frontmatter description must state the single-deliverable boundary")
    if len(text.splitlines()) > 500:
        fail(f"SKILL.md must stay at or below 500 lines, got {len(text.splitlines())}")
    if "# Video Script Builder v1.3.0" not in text:
        fail("SKILL.md release version is not v1.3.0")
    if "spec 通过 12 条阻断后" not in text:
        fail("SKILL.md must keep the 12-gate delivery check")

    referenced = set(
        re.findall(r"`((?:references|templates)/[^`]+\.md)`", text)
    )
    for relative in sorted(referenced):
        if not (ROOT / relative).is_file():
            fail(f"SKILL.md references missing file: {relative}")


def iter_text_files() -> list[Path]:
    suffixes = {".md", ".yaml", ".yml", ".json", ".txt"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in suffixes
        and ".git" not in path.parts
    ]


def check_local_links() -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            target = target.strip()
            if (
                not target
                or target.startswith(("http://", "https://", "#", "mailto:"))
                or " " in target
            ):
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
        if re.search(r"repeat\s*:\s*-1", text):
            fail(f"infinite GSAP repeat found in {relative}")


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
        referenced.update(
            re.findall(
                r"npx\s+hyperframes\s+add\s+([a-z0-9-]+)",
                path.read_text(encoding="utf-8"),
            )
        )
    unknown = sorted(referenced - verified)
    if unknown:
        fail(f"unverified HyperFrames registry items: {', '.join(unknown)}")


def check_visuals() -> None:
    for relative in [
        "docs/images/workflow.svg",
        "docs/images/handoff-boundary.svg",
    ]:
        try:
            ET.parse(ROOT / relative)
        except ET.ParseError as exc:
            fail(f"invalid SVG {relative}: {exc}")

    hero = ROOT / "docs/images/video-script-builder-hero.png"
    if hero.is_file() and hero.stat().st_size < 100_000:
        fail("README hero image looks unexpectedly small")


def main() -> int:
    check_required_files()
    check_skill_contract()
    check_local_links()
    check_privacy_and_stale_names()
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
