# sabiowl-home-pages

[Sabiowl](https://sabiowl.com)（習慣化を楽しく支援する RPG 風アプリ）の**公式サイト**です。
GitHub Pages + Jekyll で構築し、独自ドメイン **[sabiowl.com](https://sabiowl.com)** で公開しています。

法的文書だけでなく、TOP・使い方ガイド・FAQ・リリースノートを含みます。

## 📄 公開ページ (全 7 トピック、日英)

| トピック | 日本語 | English |
|---|---|---|
| TOP | [/](https://sabiowl.com/) | [/en/](https://sabiowl.com/en/) |
| 使い方ガイド | [/help.html](https://sabiowl.com/help.html) | [/en/help.html](https://sabiowl.com/en/help.html) |
| よくあるご質問 | [/faq.html](https://sabiowl.com/faq.html) | [/en/faq.html](https://sabiowl.com/en/faq.html) |
| リリースノート | [/release_notes.html](https://sabiowl.com/release_notes.html) | [/en/release_notes.html](https://sabiowl.com/en/release_notes.html) |
| プライバシーポリシー | [/privacy_policy.html](https://sabiowl.com/privacy_policy.html) | [/privacy_policy_en.html](https://sabiowl.com/privacy_policy_en.html) |
| 利用規約 | [/terms_of_service.html](https://sabiowl.com/terms_of_service.html) | [/terms_of_service_en.html](https://sabiowl.com/terms_of_service_en.html) |
| 特定商取引法に基づく表示 / 販売者情報 | [/specified_commercial_transactions.html](https://sabiowl.com/specified_commercial_transactions.html) | [/legal_consumer_info_en.html](https://sabiowl.com/legal_consumer_info_en.html) |

## 🔴 URL を動かしてはいけない

**法務 3 ページの URL は固定です。**

- App Store Connect にプライバシーポリシー URL として登録済み
- **プライバシーポリシーは Google OAuth 審査の根拠文書**
- アプリ本体 (`mobile/lib/core/constants/app_urls.dart`) が直リンクしており、
  CI テスト `app_urls_locale_test.dart` が縛っている

動かすと **ストア審査とアプリの両方が壊れます**。英語版の命名が
`*_en.html`（法務）と `/en/...`（それ以外）で揃っていないのは、この制約による
**意図的な不統一**です。詳細は [`_data/i18n.yml`](_data/i18n.yml) の冒頭コメント。

## 🛠 構成

- **静的サイト生成**: Jekyll（GitHub Pages 標準）
- **テーマ**: minima
- **言語**: 日本語 + English（全 7 トピックに英語版あり）
- **ドメイン**: sabiowl.com（[`CNAME`](CNAME) による独自ドメイン、2026-07-19 切替）
- **言語切替**: [`_layouts/page_with_lang.html`](_layouts/page_with_lang.html) が
  [`_data/i18n.yml`](_data/i18n.yml) の対応表を引いて出力
- **ライセンス**: 法的文書のため CC0 / Public Domain（自由参照可、引用時は出典明記推奨）

## 🔄 更新方法

```bash
# 1. clone
git clone git@github.com:sabiowl/sabiowl-home-pages.git
cd sabiowl-home-pages

# 2. 該当 Markdown を編集（日本語版と英語版は必ずセットで直す）
code privacy_policy.md privacy_policy_en.md

# 3. プレビュー（任意、ローカル Jekyll 必要）
bundle exec jekyll serve

# 4. ★ push 前に必ず実行 ★
python scripts/verify_i18n_links.py

# 5. commit + push
git add privacy_policy.md privacy_policy_en.md
git commit -m "doc: update privacy policy (YYYY-MM-DD)"
git push origin main
```

push 後、約 1〜2 分で [https://sabiowl.com/](https://sabiowl.com/) に反映されます。

### ⚠️ `verify_i18n_links.py` を飛ばさないこと

`_data/i18n.yml` には「**英語版ページを追加したら 1 行足す**」という、人間が忘れる
種類の約束があります。ずれると切替リンクが消えるか 404 になりますが、
**Jekyll はビルドエラーにしません**（ビルドは GitHub Pages 側で走るため、
ローカルで気づく機会もありません）。この約束を機械で縛る唯一の手段が本スクリプトです。

同種の約束はアプリ側の `app_urls.dart` にもあり、そちらは CI で縛られています。

## 📋 改訂履歴

- **2026-08-11**: 実装との突き合わせ監査。iOS のみ配信への統一 / 「マイページ」表記の是正 /
  廃止済み「称号」報酬の削除 / 出陣チケット・仮メモの説明追加 / リリースノートを v1.0.5 まで追随
- **2026-08-06**: 全 7 トピックに英語版を整備（FEAT-519 Phase 1-3）、言語切替リンク +
  `verify_i18n_links.py` 導入
- **2026-07-19**: 独自ドメイン sabiowl.com へ切替（Google OAuth verification 要件）
- **2026-06-27**: 配信元を subaru7105 → sabiowl 組織へ移管
- **2026-06-14**: 旧 sabiowl-legal-pages を本リポジトリに統合、リリースノート / FAQ を追加
- **2026-05-21**: 初版公開（Sabiowl リリース前準備）
  - PostHog / Firebase Auth / FCM / Google Calendar / Resend / Render の全外部サービス開示
  - データ削除パイプライン（Django + Firebase Auth + PostHog 3 段階）の明記

過去の変更は git commit history で追跡可能です。

## 🔗 関連リポジトリ

- [Sabiowl アプリ本体](https://github.com/Subaru7105/sabiowl)（Private）

## 📞 お問い合わせ

本サイトの内容に関するお問い合わせは、Sabiowl アプリ内「設定 → お問い合わせ」
または support@sabiowl.com までご連絡ください。
