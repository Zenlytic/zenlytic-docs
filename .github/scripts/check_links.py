#!/usr/bin/env python3
"""Check internal links across every docs section.

Written because three separate classes of broken link reached production,
each invisible to the check that existed at the time:

1. Directory-style links with no .md suffix (../5_data_modeling/model/)
2. HTML <a href> inside GitBook card tables, not Markdown [](...)
3. GitBook's own /broken/pages/<id> and broken-reference markers

GitBook does not fail a build on any of these. An unresolvable relative
link is silently rewritten into a github.com URL that 404s, so the page
renders normally and the reader is sent off-site. Checking file existence
by hand is the only way to catch it, and it has to cover every link form.
"""
import os
import re
import sys
import urllib.parse
from pathlib import Path

SECTIONS = ["docs", "changelog", "developers", "resources"]

# GitBook emits these when it cannot resolve a link. They are never valid.
BROKEN_MARKERS = ("/broken/pages/", "broken-reference")

LINK_PATTERNS = [
    r'(?<!!)\[[^\]]*\]\(<([^>]+)>\)',   # [text](<path with spaces>)
    r'(?<!!)\[[^\]]*\]\(([^)<>]+)\)',   # [text](path)
    r'<a[^>]+href="([^"]+)"',           # HTML anchors, incl. card tables
    r"<a[^>]+href='([^']+)'",
]

problems = []


def check(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    for marker in BROKEN_MARKERS:
        if marker in text:
            problems.append(f"{path}: contains GitBook broken-link marker '{marker}'")

    for pattern in LINK_PATTERNS:
        for raw in re.findall(pattern, text):
            # strip an optional markdown link title:  (file.md "Title")
            href = re.sub(r'\s+"[^"]*"$', "", raw.strip())
            href = href.split("#")[0].strip()
            if not href or href.startswith(
                ("http://", "https://", "mailto:", "#", "data:", "tel:")
            ):
                continue
            target = urllib.parse.unquote(href)
            resolved = (path.parent / target).resolve()
            if (
                resolved.exists()
                or resolved.with_suffix(".md").exists()
                or (resolved / "README.md").exists()
            ):
                continue
            problems.append(f"{path}: unresolved link -> {href}")


for section in SECTIONS:
    root = Path(section)
    if not root.is_dir():
        continue
    for md in root.rglob("*.md"):
        if ".gitbook" in md.parts:
            continue
        check(md)

if problems:
    print(f"Link check failed ({len(problems)} problem(s)):\n")
    for p in sorted(set(problems)):
        print(f"  - {p}")
    print(
        "\nCross-section links must be absolute URLs. Relative paths do not "
        "resolve across a section boundary and GitBook rewrites them into "
        "github.com links that 404."
    )
    sys.exit(1)

print("Link check passed — all internal links resolve.")
