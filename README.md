# sabiowl-home-pages

[Sabiowl](https://github.com/Subaru7105/sabiowl)（習慣化を楽しく支援する RPG 風アプリ）の法的文書を公開する GitHub Pages リポジトリです。

## 📄 公開ドキュメント

- [プライバシーポリシー](https://subaru7105.github.io/sabiowl-home-pages/privacy_policy.html)
- [利用規約](https://subaru7105.github.io/sabiowl-home-pages/terms_of_service.html)

## 🛠 構成

- **静的サイト生成**: Jekyll（GitHub Pages 標準）
- **テーマ**: minima
- **言語**: 日本語
- **ライセンス**: 法的文書のため CC0 / Public Domain（自由参照可、引用時は出典明記推奨）

## 🔄 更新方法

```bash
# 1. clone
git clone git@github.com:Subaru7105/sabiowl-home-pages.git
cd sabiowl-home-pages

# 2. 該当 Markdown を編集
code privacy_policy.md

# 3. プレビュー（任意、ローカル Jekyll 必要）
bundle exec jekyll serve

# 4. commit + push
git add privacy_policy.md
git commit -m "doc: update privacy policy (YYYY-MM-DD)"
git push origin main
```

push 後、約 1〜2 分で [https://subaru7105.github.io/sabiowl-home-pages/](https://subaru7105.github.io/sabiowl-home-pages/) に反映されます。

## 📋 改訂履歴

- **2026-05-21**: 初版公開（Sabiowl リリース前準備）
  - PostHog / Firebase Auth / FCM / Google Calendar / Resend / Render の全外部サービス開示
  - データ削除パイプライン（Django + Firebase Auth + PostHog 3 段階）の明記

過去の変更は git commit history で追跡可能です。

## 🔗 関連リポジトリ

- [Sabiowl アプリ本体](https://github.com/Subaru7105/sabiowl)（Private）

## 📞 お問い合わせ

法的文書に関するお問い合わせは、Sabiowl アプリ内「マイページ → お問い合わせ」よりご連絡ください。
