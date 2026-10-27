# rule-sheets — ボードゲーム ルール早見表

ボードゲームのルール説明動画（YouTube）の概要欄から開く、早見表のサイトです。
動画で省いた枚数・表・細かい決まりと、間違えやすいところを、ゲームごとに 1 ページにまとめています。

公開先: https://i-see-know.github.io/rule-sheets/

## 仕組み（要点）

- `data\<slug>.json` … ゲームごとの中身（章・項目・根拠のページ）。インスト動画の各ジョブ（inst-video の `jobs\<job>\make_sheet.py`）が書き出す。
- `build.py` … `data\` から `docs\<slug>\index.html` と一覧 `docs\index.html` を組む（見た目はここだけが持つ）。
- `docs\` … GitHub Pages の公開物（main ブランチの `/docs`）。手で直さない。

```
python build.py
```

## 文書マップ

| 文書 | 役割 |
|---|---|
| [STATUS.md](STATUS.md) | 現況・残タスク（正典） |
| [CLAUDE.md](CLAUDE.md) | AI 作業時の必須注意 |
