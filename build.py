"""Render notes/*.md into the NOTES object inside index.html. Run: python3 build.py"""
import re, json, html, pathlib
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t
def md(src):
    out, lst = [], None
    def close():
        nonlocal lst
        if lst: out.append(f"</{lst}>"); lst = None
    for line in src.strip().splitlines():
        s = line.strip()
        if not s: close(); continue
        m = re.match(r"^(#{2,3}) (.*)", s)
        if m:
            close(); lvl = len(m.group(1)) + 1
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); continue
        m = re.match(r"^(-|\d+\.) (.*)", s)
        if m:
            kind = "ul" if m.group(1) == "-" else "ol"
            if lst != kind: close(); out.append(f"<{kind}>"); lst = kind
            out.append(f"<li>{inline(m.group(2))}</li>"); continue
        close(); out.append(f"<p>{inline(s)}</p>")
    close()
    return "".join(out)
notes = {p.stem: md(p.read_text()) for p in sorted(pathlib.Path("notes").glob("*.md"))}
page = pathlib.Path("index.html").read_text()
page = re.sub(r"/\*NOTES\*/.*?/\*END\*/", lambda m: "/*NOTES*/" + json.dumps(notes, ensure_ascii=False).replace("</", "<\\/") + "/*END*/", page, flags=re.S)
pathlib.Path("index.html").write_text(page)
print(len(notes), "sessions embedded")
