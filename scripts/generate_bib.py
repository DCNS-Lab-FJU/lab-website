#!/usr/bin/env python3
"""
generate_bib.py
Converts data/publications.yaml → static/publications.bib
Run from repo root: python scripts/generate_bib.py
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Please install PyYAML: pip install pyyaml")

YAML_PATH = Path("data/publications.yaml")
BIB_PATH  = Path("static/publications.bib")


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower().replace(" ", ""))


def first_author_last(authors: str) -> str:
    first = authors.split(",")[0].strip()
    parts = first.split()
    return parts[-1] if parts else "unknown"


def make_key(entry: dict, kind: str) -> str:
    last = first_author_last(entry.get("authors", "unknown"))
    year = str(entry.get("year", "0000"))
    words = entry.get("title", "").split()
    title_word = slugify(words[0]) if words else "x"
    return f"{last}{year}{title_word}"


def entry_to_bib(entry: dict, bib_type: str) -> str:
    key = make_key(entry, bib_type)
    authors = entry.get("authors", "")
    # Convert "A, B, C" → "A and B and C" for BibTeX
    authors_bib = " and ".join(a.strip() for a in authors.split(","))
    lines = [f"@{bib_type}{{{key},"]
    lines.append(f'  author  = {{{authors_bib}}},')
    lines.append(f'  title   = {{{{{entry.get("title", "")}}}}},'  )
    lines.append(f'  year    = {{{entry.get("year", "")}}},')
    venue = entry.get("venue", "")
    if bib_type == "article":
        lines.append(f'  journal = {{{venue}}},')
    else:
        lines.append(f'  booktitle = {{{venue}}},')
    if entry.get("link"):
        lines.append(f'  url     = {{{entry["link"]}}},')
    lines.append("}")
    return "\n".join(lines)


def main():
    if not YAML_PATH.exists():
        sys.exit(f"Cannot find {YAML_PATH}. Run from repo root.")

    with YAML_PATH.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    blocks = []
    for entry in (data.get("journal_articles") or []):
        blocks.append(entry_to_bib(entry, "article"))
    for entry in (data.get("conference_papers") or []):
        blocks.append(entry_to_bib(entry, "inproceedings"))
    for entry in (data.get("patents") or []):
        blocks.append(entry_to_bib(entry, "misc"))
    for entry in (data.get("technical_reports") or []):
        blocks.append(entry_to_bib(entry, "techreport"))

    BIB_PATH.parent.mkdir(parents=True, exist_ok=True)
    BIB_PATH.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"Generated {len(blocks)} entries → {BIB_PATH}")


if __name__ == "__main__":
    main()
