# CLAUDE.md — rule-sheets

> 概要 → `README.md` ／ 現況・残タスク → `STATUS.md` ／ 詳細 → README.md の文書マップ。
> ここには「AI が作業するとき必ず守ること」だけを書く（規約: `C:\ai\work\DOC_STANDARD.md`）。

- **公開リポジトリ（GitHub Pages）。ここに入れた物は全部、誰でも読める。** README・STATUS・CLAUDE.md も含む。
  個人の事情・ほかのプロジェクトの話・社内の話・パスワード類は書かない。push の前に
  `python C:\ai\platform\control\secrets_scan.py --repo C:\ai\work\boardgame\rule-sheets` の出力が「検出なし」か読む（終了コードは見ない）。
- **中身は inst-video のジョブが書き出す `data\*.json`。ここで中身を手で直さない**（直すのはジョブの `make_sheet.py`）。`docs\` は `build.py` の出力。
- **権利**: 自分の言葉の要約と、英語版ルールブックのページ番号だけ。ルールブックの図版・和訳の全文・カードの絵は載せない。
  AI の手を借りた非公式の資料であること、BGG の回答は非公式であることを各ページに書く。
- 外部の読み込みは Google Fonts だけ（書体が無くても読める）。スクリプトは使わない。
- push・公開設定の変更は外向きの操作なので、本人に確かめてから。
