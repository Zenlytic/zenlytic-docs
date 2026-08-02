#!/usr/bin/env python3
"""Validate changelog/README.md against .changelog/curation-rules.md.

The changelog is written by a scheduled agent and edited through the GitBook
UI. A rules file only helps if it gets read; this check does not depend on
that. Every failure below has already happened at least once.
"""
import re
import sys
from pathlib import Path

PATH = Path("changelog/README.md")
VOCAB = ["new-features", "improvements", "fixes"]
SUBSECTION_TAG = {
    "New features": "new-features",
    "Improvements": "improvements",
    "Bug fixes": "fixes",
}
H1 = "# Product updates"

errors = []


def fail(msg):
    errors.append(msg)


text = PATH.read_text(encoding="utf-8")

# --- page header, owned by GitBook -----------------------------------------
if not re.search(rf"^{re.escape(H1)}$", text, re.M):
    fail(f'H1 must be exactly "{H1}". GitBook owns the page title; changing it '
         f"moves the page URL.")

fm = re.search(r"^tags:\n((?:  - \S+\n)+)", text, re.M)
if not fm:
    fail("Frontmatter is missing a tags: list. It declares the filter chips; "
         "without it, tags match nothing.")
else:
    declared = re.findall(r"^  - (\S+)$", fm.group(1), re.M)
    if sorted(declared) != sorted(VOCAB):
        fail(f"Frontmatter tags: is {declared}, expected {VOCAB}.")

if "{% updates" not in text:
    fail("No {% updates %} block found.")

# --- entries ----------------------------------------------------------------
entries = list(
    re.finditer(
        r'\{% update date="([^"]*)" tags="([^"]*)" %\}\s*\n(.*?)\{% endupdate %\}',
        text,
        re.S,
    )
)
if not entries:
    fail("No {% update %} entries parsed. Check the block syntax.")

for m in entries:
    date, tags_attr, body = m.group(1), m.group(2), m.group(3)
    label = date or "<no date>"

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        fail(f"[{label}] date must be YYYY-MM-DD.")

    heading = re.search(r"^## (.+)$", body, re.M)
    if not heading:
        fail(f"[{label}] missing a '## ' headline.")
    elif re.match(r"^(Week of |[A-Z][a-z]+ \d{1,2},? \d{4}$)", heading.group(1).strip()):
        fail(f'[{label}] "## {heading.group(1).strip()}" is a date, not a headline. '
             f"The date already renders from the attribute; this heading drives "
             f"the on-page nav and anchor.")

    subs = re.findall(r"^### (.+)$", body, re.M)
    for s in subs:
        if s.strip() not in SUBSECTION_TAG:
            fail(f'[{label}] unexpected subsection "### {s.strip()}". '
                 f"Allowed: {', '.join(SUBSECTION_TAG)}.")

    tags = [t for t in tags_attr.split(",") if t]
    unknown = [t for t in tags if t not in VOCAB]
    if unknown:
        fail(f"[{label}] tag(s) {unknown} outside the vocabulary {VOCAB}.")

    expected = {SUBSECTION_TAG[s.strip()] for s in subs if s.strip() in SUBSECTION_TAG}
    if set(tags) != expected:
        fail(f"[{label}] tags {sorted(tags)} do not match subsections "
             f"{sorted(expected)}. Tags are derived from the ### sections present.")

# --- links ------------------------------------------------------------------
for m in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
    href = m.group(1).strip()
    if href.startswith(("http://", "https://", "#", "mailto:")):
        continue
    fail(f'Relative link "{href}". Cross-section links must be absolute URLs — '
         f"GitBook silently rewrites unresolvable relative paths into GitHub "
         f"links that 404.")

# --- report -----------------------------------------------------------------
if errors:
    print(f"Changelog validation failed ({len(errors)} problem(s)):\n")
    for e in errors:
        print(f"  - {e}")
    print("\nRules: .changelog/curation-rules.md")
    sys.exit(1)

print(f"Changelog OK — {len(entries)} entries, vocabulary {VOCAB}.")
