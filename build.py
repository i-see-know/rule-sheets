r"""早見表のサイトを組む（data\<slug>.json → docs\<slug>\index.html と一覧 docs\index.html）。

    python build.py

- 中身（data\*.json）はインスト動画の各ジョブが書き出す（inst-video の jobs\<job>\make_sheet.py）。ここは見た目だけを持つ。
- docs\ が GitHub Pages の公開物（設定は Settings → Pages → main の /docs）。docs\ は手で直さない。
"""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
SITE_TITLE = "ボードゲーム ルール早見表"

# 卓の上のメモ（動画の右パネルと同じ紙・墨・赤ペン・金）
CSS = """
:root {
  --paper: #fbf6e6; --sheet: #fffdf6; --ink: #3c3228; --mute: #7d7263; --rule: #e3d9c1; --pen: #c8463a; --gold: #946516;
  --display: "Zen Maru Gothic", "BIZ UDPGothic", sans-serif; --body: "BIZ UDPGothic", "Hiragino Sans", "Yu Gothic", sans-serif;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) { :root {
  --paper: #1d1a16; --sheet: #26221d; --ink: #efe6d3; --mute: #a89d8b; --rule: #3a342c; --pen: #f07c6c; --gold: #e2b860; color-scheme: dark } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--body); line-height: 1.7;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.wrap { max-width: 860px; margin: 0 auto; padding-block: 24px 64px; display: grid; gap: 18px; }
h1 { font-family: var(--display); font-weight: 700; font-size: clamp(1.5rem, 4vw, 2.1rem); margin: 0; text-wrap: balance; }
h1 small { display: block; font-size: .5em; color: var(--gold); font-weight: 500; letter-spacing: .06em; }
.lead { margin: 0; color: var(--mute); font-size: .92rem; max-width: 62ch; }
.back { font-size: .85rem; color: var(--mute); }
.back a, footer a { color: var(--gold); }
nav { display: flex; flex-wrap: wrap; gap: 6px; }
nav a { font-size: .85rem; color: var(--ink); text-decoration: none; border: 1px solid var(--rule); background: var(--sheet); border-radius: 999px; padding: 2px 12px; }
nav a:hover, nav a:focus-visible { border-color: var(--pen); outline: none; }
section { background: var(--sheet); border: 1px solid var(--rule); border-radius: 6px; padding: 14px 18px 16px; min-width: 0; }
h2 { font-family: var(--display); font-weight: 700; font-size: 1.15rem; margin: 0 0 8px; padding-bottom: 4px; border-bottom: 3px solid var(--pen); display: inline-block; }
ol.items { margin: 0; padding-left: 1.3em; display: grid; gap: 6px; }
.t { display: block; }
.src { display: block; font-size: .78rem; color: var(--mute); font-variant-numeric: tabular-nums; }
.src a { color: var(--gold); }
ul.tbl { list-style: none; margin: 6px 0 10px; padding: 0; border-top: 1px solid var(--rule); }
ul.tbl li { padding: 5px 4px; border-bottom: 1px solid var(--rule); font-variant-numeric: tabular-nums; }
ul.games { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
ul.games a { display: block; background: var(--sheet); border: 1px solid var(--rule); border-radius: 6px; padding: 12px 16px; color: var(--ink); text-decoration: none; }
ul.games a:hover, ul.games a:focus-visible { border-color: var(--pen); outline: none; }
ul.games b { font-family: var(--display); font-size: 1.1rem; }
ul.games span { display: block; font-size: .85rem; color: var(--mute); }
footer { font-size: .8rem; color: var(--mute); }
"""


def doc(title: str, body: str, desc: str) -> str:
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700&family=BIZ+UDPGothic:wght@400;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{body}
</div>
</body>
</html>
"""


def cite(srcs: list[dict]) -> str:
    out = []
    for s in srcs:
        lab = html.escape(s["label"])
        out.append(f'<a href="{html.escape(s["url"])}" target="_blank" rel="noopener">{lab}</a>' if s.get("url") else lab)
    return "・".join(out)


def game_page(g: dict) -> str:
    secs = []
    for i, sec in enumerate(g["sections"]):
        parts, cur = [], []
        for it in sec["items"]:
            if "table" in it:
                if cur:
                    parts.append('<ol class="items">' + "".join(cur) + "</ol>"); cur = []
                parts.append('<ul class="tbl">' + "".join(f"<li>{html.escape(x)}</li>" for x in it["table"]) + "</ul>")
            else:
                cur.append(f'<li><span class="t">{html.escape(it["text"])}</span><span class="src">{cite(it.get("src", []))}</span></li>')
        if cur:
            parts.append('<ol class="items">' + "".join(cur) + "</ol>")
        secs.append(f'<section id="s{i}"><h2>{html.escape(sec["h"])}</h2>{"".join(parts)}</section>')
    nav = "".join(f'<a href="#s{i}">{html.escape(s["h"])}</a>' for i, s in enumerate(g["sections"]))
    video = f'・<a href="{html.escape(g["video_url"])}" target="_blank" rel="noopener">ルール説明動画</a>' if g.get("video_url") else ""
    body = f"""  <p class="back"><a href="../">{SITE_TITLE}</a>{video}</p>
  <header style="display:grid;gap:10px">
    <h1>{html.escape(g["title"])} 早見表<small>{html.escape(g.get("kicker", "ルール説明動画の補足"))}</small></h1>
    <p class="lead">{html.escape(g["lead"])}</p>
    <nav aria-label="目次">{nav}</nav>
  </header>
  {"".join(secs)}
  <footer>{html.escape(g.get("footer", ""))}</footer>"""
    return doc(f'{g["title"]} 早見表', body, g["lead"])


def index_page(games: list[dict]) -> str:
    items = "".join(f'<li><a href="{html.escape(g["slug"])}/"><b>{html.escape(g["title"])}</b>'
                    f'<span>{html.escape(g.get("title_en", ""))}</span></a></li>' for g in games)
    body = f"""  <header style="display:grid;gap:10px">
    <h1>{SITE_TITLE}<small>ルール説明動画の補足</small></h1>
    <p class="lead">ルール説明動画で省いた枚数・表・細かい決まりと、間違えやすいところをまとめています。動画の制作者が AI の手を借りてまとめた非公式の資料です。迷ったら各ゲームのルールブックを見てください。</p>
  </header>
  <ul class="games">{items}</ul>"""
    return doc(SITE_TITLE, body, "ボードゲームのルール説明動画の補足の早見表")


def main():
    games = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(DATA.glob("*.json"))]
    games.sort(key=lambda g: g.get("published", ""), reverse=True)
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    for g in games:
        d = DOCS / g["slug"]; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(game_page(g), encoding="utf-8")
    (DOCS / "index.html").write_text(index_page(games), encoding="utf-8")
    print(f"{len(games)} 件 → {DOCS}")


if __name__ == "__main__":
    main()
