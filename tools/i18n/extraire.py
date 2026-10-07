#!/usr/bin/env python3
"""Liste les chaînes visibles des pages françaises (texte + attributs lisibles) à traduire.
Usage : python3 tools/i18n/extraire.py  ->  tools/i18n/chaines-fr.json"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
ATTRS = r'(alt|aria-label|title|placeholder|data-caption|data-tour-title|data-embed-title|data-accent-label)'
TEXT = re.compile(r'>([^<]+)<')
ATTR = re.compile(ATTRS + r'="([^"]*)"')
SKIP = re.compile(r'<(script|style)\b.*?</\1>|<!--.*?-->', re.S)


def chaines(source):
    source = SKIP.sub(lambda m: "<x>", source)
    out = []
    for m in TEXT.finditer(source):
        t = " ".join(m.group(1).split())
        if t and re.search(r"[A-Za-zÀ-ÿ]", t):
            out.append(html.unescape(t))
    for m in ATTR.finditer(source):
        t = " ".join(m.group(2).split())
        if t and re.search(r"[A-Za-zÀ-ÿ]", t):
            out.append(html.unescape(t))
    return out


if __name__ == "__main__":
    vues = {}
    for page in sorted(ROOT.glob("*.html")):
        for c in chaines(page.read_text(encoding="utf-8")):
            vues.setdefault(c, None)
    dest = ROOT / "tools" / "i18n" / "chaines-fr.json"
    dest.write_text(json.dumps(list(vues), ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(vues), "chaînes ->", dest.relative_to(ROOT))
