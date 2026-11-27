---
title: ルール早見表サイト
phase: 開発中
health: green
updated: 2026-11-28
detail: インスト動画の概要欄から開く早見表を GitHub Pages で公開
public: true
---

> C:\ai のプロジェクト台帳（`C:\ai\PROJECTS.md`）の素。現状の要約と入口だけを書く。詳細は frontmatter の `detail` の文書へ。

## いま何か

- 公開中（2026-10-27）: https://i-see-know.github.io/rule-sheets/ ・リコール・ゴッズ・プレイグラウンド・メディコの 1 ページ（ゴッズ・プレイグラウンドとメディコは印刷用 PDF つき）と一覧。公開リポジトリ i-see-know/rule-sheets の main の /docs。

## 課題・ブロッカー

- 特になし

## 次のアクション

- [x] リコールの動画のリンクを足した（2026-11-12・data は inst-video の jobs/recall/make_sheet.py から）
- [x] ゴッズ・プレイグラウンドを動画の最終の字幕と突き合わせて直した（2026-11-21・用語をラウンド／アクションに統一・拡大は矢印の先ごと・遠征で振るのは自分の兵ほか）
- [x] メディコのページと印刷用 PDF を足した（2026-11-28・data は inst-video の jobs/medico_rules/make_sheet.py。PDF は和訳の作業で作った早見表で、出版社の絵を使っている＝持ち主の判断で載せた）
- [ ] メディコの動画のリンク（動画を公開してから・make_sheet.py に video_url）
- [ ] ゴッズ・プレイグラウンドの動画のリンク（本人が動画を公開してから・data は inst-video の jobs/gods_playground/make_sheet.py に video_url）
