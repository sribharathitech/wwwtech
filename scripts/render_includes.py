#!/usr/bin/env python3
"""
Inlines the shared partials in _includes/ (header.html, footer.html) into
every page listed below, between marker comments. Run this any time you
edit a file in _includes/ so the change propagates to all pages.

This project has no server-side templating (plain static HTML on GitHub
Pages, previewed with `python -m http.server`), so partials can't be
resolved at request time -- this script resolves them at edit time instead.

Usage:
    python scripts/render_includes.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGES = [
    "index.html",
    "about/index.html",
    "case-studies/index.html",
    "contact/index.html",
    "products/index.html",
    "products/chemtech/index.html",
    "products/securator-gosafe/index.html",
    "products/suryavidya/index.html",
    "products/usip/index.html",
    "services/index.html",
    "services/artificial-intelligence/index.html",
    "services/ibm-mainframe-data-migration/index.html",
    "services/java-spring-boot-development/index.html",
    "services/mobile-app-development/index.html",
    "services/software-testing-qa/index.html",
]

PARTIALS = ["header.html", "footer.html"]


def marker_re(name):
    begin = re.escape(f"<!-- include:{name} -->")
    end = re.escape(f"<!-- /include:{name} -->")
    return re.compile(rf"([ \t]*{begin}\r?\n)(.*?)([ \t]*{end}\r?\n)", re.DOTALL)


def main():
    partial_content = {}
    for name in PARTIALS:
        path = ROOT / "_includes" / name
        with open(path, "r", encoding="utf-8", newline="") as f:
            partial_content[name] = f.read()

    changed = 0
    for rel in PAGES:
        path = ROOT / rel
        with open(path, "r", encoding="utf-8", newline="") as f:
            content = f.read()
        orig = content

        for name in PARTIALS:
            pattern = marker_re(name)
            matches = pattern.findall(content)
            if len(matches) != 1:
                print(f"[WARN] {rel}: expected 1 marker block for {name}, found {len(matches)}")
                continue
            content = pattern.sub(
                lambda m: m.group(1) + partial_content[name] + m.group(3),
                content,
                count=1,
            )

        if content != orig:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(content)
            print(f"[UPDATED] {rel}")
            changed += 1
        else:
            print(f"[unchanged] {rel}")

    print(f"\nDone. {changed} file(s) updated.")


if __name__ == "__main__":
    main()
