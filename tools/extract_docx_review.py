from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def _read_xml(zf: zipfile.ZipFile, name: str) -> ET.Element | None:
    try:
        data = zf.read(name)
    except KeyError:
        return None
    return ET.fromstring(data)


def _node_text(node: ET.Element) -> str:
    parts: list[str] = []
    for child in node.iter():
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "t" and child.text:
            parts.append(child.text)
        elif tag == "tab":
            parts.append("\t")
        elif tag in {"br", "cr"}:
            parts.append("\n")
    return "".join(parts)


def _paragraph_text(p: ET.Element) -> str:
    return _node_text(p).strip()


def _style_id(p: ET.Element) -> str:
    ppr = p.find("w:pPr", NS)
    if ppr is None:
        return ""
    pstyle = ppr.find("w:pStyle", NS)
    if pstyle is None:
        return ""
    return pstyle.attrib.get(f"{{{NS['w']}}}val", "")


def _paragraphs(root: ET.Element | None) -> list[dict[str, str | int]]:
    if root is None:
        return []
    out = []
    for i, p in enumerate(root.findall(".//w:p", NS), 1):
        text = _paragraph_text(p)
        if text:
            out.append({"index": i, "style": _style_id(p), "text": text})
    return out


def _comments(root: ET.Element | None) -> list[dict[str, str]]:
    if root is None:
        return []
    out = []
    for c in root.findall(".//w:comment", NS):
        out.append(
            {
                "id": c.attrib.get(f"{{{NS['w']}}}id", ""),
                "author": c.attrib.get(f"{{{NS['w']}}}author", ""),
                "date": c.attrib.get(f"{{{NS['w']}}}date", ""),
                "text": _node_text(c).strip(),
            }
        )
    return out


def _tracked(root: ET.Element | None) -> dict[str, int]:
    if root is None:
        return {"insertions": 0, "deletions": 0, "moves": 0}
    return {
        "insertions": len(root.findall(".//w:ins", NS)),
        "deletions": len(root.findall(".//w:del", NS)),
        "moves": len(root.findall(".//w:moveFrom", NS)) + len(root.findall(".//w:moveTo", NS)),
    }


def _fields(root: ET.Element | None) -> list[str]:
    if root is None:
        return []
    fields: list[str] = []
    for instr in root.findall(".//w:instrText", NS):
        if instr.text:
            fields.append(re.sub(r"\s+", " ", instr.text.strip()))
    return fields


def _reference_section(paragraphs: list[dict[str, str | int]]) -> list[str]:
    refs: list[str] = []
    start = None
    for i, p in enumerate(paragraphs):
        text = str(p["text"]).strip()
        if re.fullmatch(r"(参考文献|References|REFERENCES|参考文献[:：]?)", text):
            start = i + 1
            break
    if start is None:
        return refs
    for p in paragraphs[start:]:
        text = str(p["text"]).strip()
        if not text:
            continue
        if re.fullmatch(r"(附录|Appendix|致谢|Acknowledgements?)[:：]?", text, re.I):
            break
        refs.append(text)
    return refs


def _suspicious(paragraphs: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    patterns = [
        r"TODO|FIXME|XXX|TBD",
        r"待补|待完善|需要补充|未完成|此处|占位",
        r"错误[!！].{0,10}引用|Error! Reference source not found",
        r"图\s*[Xx?？]|表\s*[Xx?？]",
        r"\?\?|？？",
        r"（\s*）|\(\s*\)",
        r"\[\s*\]|\{\s*\}",
        r"\[\s*(?:citation needed|需要引用)\s*\]",
        r"\d{4}年\d{4}年",
    ]
    rx = re.compile("|".join(patterns), re.I)
    out = []
    for p in paragraphs:
        text = str(p["text"])
        if rx.search(text):
            out.append(p)
    return out


def _citations(text: str) -> dict[str, list[str]]:
    bracket_numeric = sorted(set(re.findall(r"\[[0-9,，\-–—\s]+\]", text)))
    author_year = sorted(
        set(
            re.findall(
                r"[\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z\- ]{0,40}[（(][12][0-9]{3}[a-z]?[）)]",
                text,
            )
        )
    )
    malformed = sorted(set(re.findall(r"\[[^\]]{1,80}\]", text)))
    malformed = [m for m in malformed if not re.fullmatch(r"\[[0-9,，\-–—\s]+\]", m)]
    return {
        "numeric_bracket": bracket_numeric,
        "author_year": author_year,
        "other_brackets": malformed[:200],
    }


def inspect_docx(path: Path) -> dict:
    with zipfile.ZipFile(path) as zf:
        document = _read_xml(zf, "word/document.xml")
        comments = _comments(_read_xml(zf, "word/comments.xml"))
        footnotes = _paragraphs(_read_xml(zf, "word/footnotes.xml"))
        endnotes = _paragraphs(_read_xml(zf, "word/endnotes.xml"))
        paragraphs = _paragraphs(document)
        text = "\n".join(str(p["text"]) for p in paragraphs)
        refs = _reference_section(paragraphs)
        names = set(zf.namelist())
        media = [n for n in names if n.startswith("word/media/")]
        rels = _read_xml(zf, "word/_rels/document.xml.rels")
        hyperlinks: list[str] = []
        if rels is not None:
            for rel in rels:
                if rel.attrib.get("Type", "").endswith("/hyperlink"):
                    hyperlinks.append(rel.attrib.get("Target", ""))
        return {
            "path": str(path),
            "paragraph_count": len(paragraphs),
            "wordish_count": len(re.findall(r"[\u4e00-\u9fff]|[A-Za-z0-9]+", text)),
            "has_reference_section": bool(refs),
            "reference_count": len(refs),
            "references": refs,
            "comments_count": len(comments),
            "comments": comments,
            "tracked_changes": _tracked(document),
            "field_count": len(_fields(document)),
            "fields_sample": _fields(document)[:50],
            "footnotes": footnotes,
            "endnotes": endnotes,
            "media_count": len(media),
            "hyperlinks": hyperlinks,
            "suspicious": _suspicious(paragraphs),
            "citations": _citations(text),
            "paragraphs": paragraphs,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", nargs="+")
    parser.add_argument("--outdir", default="literature_reports/_docx_extract")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    summaries = []
    for item in args.docx:
        path = Path(item)
        data = inspect_docx(path)
        stem = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "_", path.stem).strip("_")[:80]
        (outdir / f"{stem}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        text_lines = [str(p["text"]) for p in data["paragraphs"]]
        (outdir / f"{stem}.txt").write_text("\n".join(text_lines), encoding="utf-8")
        (outdir / f"{stem}_references.txt").write_text("\n".join(data["references"]), encoding="utf-8")
        summaries.append({k: data[k] for k in data if k not in {"paragraphs", "references", "comments", "suspicious"}})
    (outdir / "summary.json").write_text(json.dumps(summaries, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
