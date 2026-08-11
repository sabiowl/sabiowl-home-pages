---
layout: page_with_lang
title: 使い方ガイド
permalink: /help.html
---

# 使い方ガイド

<p style="color: #666; font-size: 0.9em;">最終更新日: 2026 年 8 月 9 日</p>

---

Sabiowl をお使いいただきありがとうございます 🪶
本ページでは、アプリの各画面の使い方を短い動画と手順でご案内しております。

お知りになりたい画面を目次からお選びください。
本ページに記載のない内容については、アプリ内「設定 → お問い合わせ」よりお気軽にご連絡ください。

### 画面の開き方について

本ページでは 2 つの入り口をご案内します。あらかじめ場所をご確認いただくと、以降の手順が読みやすくなりますよ 🪶

| 呼び方 | 場所 | ここから開けるもの |
|---|---|---|
| **下部メニュー** | 画面下のタブ | ホーム / チャレンジ / ギルド / カレンダー |
| **メニュー (☰)** | ホーム画面 **右上** のアイコン | 使い方ガイド / 眠る世界 / ステータス / キャラ変更 / 実績 / ガチャ / フレンド / ダイヤを購入 / お知らせ / 設定 |

---

## 目次

- [🏠 ホーム画面](#-ホーム画面)
- [📝 タスク・予定・習慣の登録](#-タスク予定習慣の登録)
- [🌙 眠る世界 (ライフラグ)](#-眠る世界-ライフラグ)
- [🎯 チャレンジ](#-チャレンジ)
- [⚔️ ギルド (バトル)](#️-ギルド-バトル)
- [📅 カレンダー](#-カレンダー)
- [🦉 キャラクター](#-キャラクター)
- [🎰 ガチャ](#-ガチャ)
- [💎 ダイヤの購入 (プレミアム)](#-ダイヤの購入-プレミアム)
- [❓ よくあるご質問](faq.html)

<style>
/* 【FEAT-485 (2026-07-08)】YouTube iframe を mobile 幅に追従させる responsive wrapper。
   WebView (iOS/Android) から開くと画面幅 375-1080px と変動するため、
   aspect-ratio で 16:9 を維持しつつ 100% 幅に fit させる。 */
.video-wrapper {
  position: relative;
  width: 100%;
  max-width: 720px;
  aspect-ratio: 16 / 9;
  margin: 16px 0;
  background: #000;
  border-radius: 8px;
  overflow: hidden;
}
.video-wrapper iframe {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
.video-placeholder-note {
  color: #999;
  font-size: 0.85em;
  font-style: italic;
  margin: 4px 0 16px;
}
.step-list {
  background: #f7f7f9;
  border-left: 3px solid #7C6AF7;
  padding: 12px 16px;
  margin: 12px 0;
}
.step-list ol {
  margin: 0;
  padding-left: 20px;
}
.step-list li {
  margin: 4px 0;
}
.back-to-toc {
  text-align: right;
  margin: 8px 0 24px;
}
.back-to-toc a {
  color: #7C6AF7;
  font-size: 0.85em;
  text-decoration: none;
}
</style>

---

## 🏠 ホーム画面

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 (例: dQw4w9WgXcQ 等 11 文字の video ID) -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_HOME"
    title="ホーム画面の使い方"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

ホーム画面は、あなたの一日の中心となる場所です。
上部の額縁 (ワールドフレーム) にはあなたが向き合っている景色が映し出され、
その下には今日の習慣・ToDo・予定が並びます。

**主な操作**

<div class="step-list">
<ol>
<li>額縁を眺めて、今日の景色を感じましょう</li>
<li>習慣カードの「+1」で今日の一歩を刻みます</li>
<li>タイムラインで一日の予定を確認できます</li>
</ol>
</div>

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 📝 タスク・予定・習慣の登録

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_ADD"
    title="タスク・予定・習慣の登録方法"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

Sabiowl では「習慣」「ToDo」「予定」の 3 種類を登録できます。

| 種類 | 特徴 | 例 |
|---|---|---|
| **習慣** | 繰り返し実施するもの | 朝の散歩 / 読書 / 筋トレ |
| **ToDo** | 1 回で完了するタスク | 銀行手続き / 書類提出 |
| **予定** | 時刻付きの用事 | 会議 / 病院 / 約束 |

**登録の流れ (共通)**

<div class="step-list">
<ol>
<li>ホーム画面右下の「+」ボタンをタップ</li>
<li>「習慣を追加」「ToDo を追加」「予定を追加」から選択</li>
<li>タイトルを入力 (よく使うタイトルは候補から選択も可能)</li>
<li>カテゴリ・頻度・時間帯などを設定</li>
<li>「保存」で登録完了、ホーム画面へ反映</li>
</ol>
</div>

> 「仮メモ機能」をオンにされている場合、右下のボタンはメモ入力に変わります
> (詳しくは下記「[仮メモ](#仮メモ)」をご覧ください)。

### 達成の記録タイミング

タップしたその瞬間に達成として記録されます。
1 日に複数回達成いただいた場合は、回数も記録されます。

**3 種類の記録方式**

| 型 | 使いどころ | 記録方法 |
|---|---|---|
| **カウント型** | 「腕立て 30 回」のように回数を数えたい | 「+1」ボタンで回数を加算 |
| **チェックリスト型** | 「朝の 5 つの支度」のように複数項目を順にこなしたい | 各項目のチェックボックスをタップ |
| **ToDo 型** | 「銀行手続き」のように 1 回で完了する | 完了マークを一度タップ |

習慣の性質に合わせてお選びいただけます 🪶

### ストリーク (連続記録) を守るには

「設定 → 連続記録の保護」より「自動で連続記録を保護する」をオンにいただくと、
在庫があるうちは途切れた瞬間に **自動でストリーク保護石を消費** して連続記録を守ります。

ストリーク保護石はショップで 💎 30 / 個 でお買い求めいただけます。
継続の途中で体調を崩された時など、あなたの積み重ねを穏やかにお守りする仕組みです 🪶

### 仮メモ

決める前に、まず書き留めておくための機能です。
「思いついたけれど、予定にするか習慣にするかはまだ決めていない」ものを、
そのまま書き留めておける場所です。ふりわけは後からで構いません 🪶

**使いはじめ方**

<div class="step-list">
<ol>
<li>「設定 → 仮メモ機能」をオンにする</li>
<li>ホーム画面右下のボタンがメモ入力に変わります</li>
<li>浮かんだことを、そのまま書き留める</li>
<li>後からメモをタップして「予定として登録」「ToDo として登録」「習慣として登録」を選ぶ</li>
</ol>
</div>

**声で書き留める**

入力欄のマイクをタップいただくと、話した内容がそのまま文字になります。
音声の文字起こしはお使いの端末の OS が行い、**音声そのものが当社サーバーへ送られることはありません**。
詳しくは[プライバシーポリシー](privacy_policy.html)第 2 条をご覧ください。

**探す・戻す**

- 画面上部の検索欄で、表示中のメモから絞り込めます (一致箇所は黄色で強調表示)
- 削除したメモはゴミ箱に移り、後から復元いただけます

> 仮メモ機能を使わない場合は、「設定 → 仮メモ機能」からオフにしていただけます。
> オフの間、ホーム画面右下のボタンは通常どおり「+」(追加) として動作します。

### アーカイブとゴミ箱の違い

習慣カードを左右にスワイプいただくと、以下の 2 種類の整理方法をお使いいただけます:

| 操作 | 動作 | 復元 |
|---|---|---|
| **アーカイブ** (右スワイプ) | リストから一時的に外す | いつでも復元可能 |
| **ゴミ箱** (左スワイプ) | 削除予約 | 30 日以内なら復元可能、30 日経過で完全削除 |

どちらも誤操作防止のため、実行前に確認ダイアログが表示されます。
ホーム画面の習慣リスト上部にある絞り込みバーから「アーカイブ」を開くと、
「アーカイブ」「削除済み（ゴミ箱）」の 2 つのタブでそれぞれ確認・復元いただけます。

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 🌙 眠る世界 (ライフラグ)

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_WORLD"
    title="眠る世界の遊び方"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

眠る世界は、あなたの日々の積み重ねが「景色」として姿を現す場所です。
習慣を達成するごとに「かけら」が集まり、シーンが完成すると景色が動き出します。

**かけらの集め方**

<div class="step-list">
<ol>
<li>その日初めての習慣達成で「輪郭のかけら」(灰色) が 1 つ生まれます</li>
<li>その日のバトル勝利で「彩りのかけら」(色つき) に変わります</li>
<li>すべてのかけらが色づくとシーンが完成、景色が動き出します</li>
</ol>
</div>

シーンを完成させた後は、SceneSelectionPage (シーン選択) から次に取り組むシーンを選べます。
完成した景色はホーム画面の額縁で引き続き楽しめます 🪶

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 🎯 チャレンジ

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_CHALLENGE"
    title="チャレンジの参加方法"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

チャレンジは、月ごとに全ユーザーで挑む共通の目標です。
特別な操作は不要で、対象カテゴリの習慣を達成すればあなたの一手が自動的に加算されます。

**参加の流れ**

<div class="step-list">
<ol>
<li>下部メニューから「チャレンジ」を開く</li>
<li>その月の対象カテゴリ (例: 運動 / 学習) を確認</li>
<li>該当する習慣を達成 (1 日 1 回まで加算)</li>
<li>3 段階の達成目標 (🥉 ブロンズ / 🥈 シルバー / 🥇 ゴールド) を経て EXP 報酬を獲得</li>
</ol>
</div>

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## ⚔️ ギルド (バトル)

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_GUILD"
    title="ギルド・バトルの始め方"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

ギルドでは、受付のリリアが相手を紹介してくれます。
バトルに勝利すると EXP・コイン・武器・彩りのかけらが手に入ります。

**バトルの流れ**

<div class="step-list">
<ol>
<li>下部メニューから「ギルド」を開く</li>
<li>掲示板から相手を選択 (自分のレベルに近い相手が挑戦しやすいです)</li>
<li>「挑戦する」でバトル開始</li>
<li>ATB ゲージが溜まったらタップで攻撃 / スキル発動</li>
<li>勝利すると報酬とかけらが届きます</li>
</ol>
</div>

**バトル倍速モード**

バトル画面 AppBar から 1x / 1.5x / 2x / 3x の 4 段階で速度を切り替えられます。
急ぎたいときは倍速、じっくり味わいたいときは等速でお楽しみください 🪶

### 出陣チケットについて

ギルドへの出陣には、**出陣チケットが 3 枚**必要です。
このチケットは、**習慣を 1 つ達成するごとに 1 枚**たまっていきます (最大 30 枚 = 10 戦分)。

つまり「バトルに行くための力は、その日の積み重ねから生まれる」設計です。
日々の一歩が、そのまま戦う準備になっているのですね 🪶

下部メニューのギルドのアイコンには、現在の状態が小さく表示されます:

| 表示 | 意味 |
|---|---|
| **✓ × N** | 出陣できます (N は挑戦できる回数) |
| **🔒** | 本日の挑戦回数の上限に達しています |
| 表示なし | チケットがまだ 3 枚に届いていません |

ギルド画面には「あと N 回の習慣達成で出陣可能」と、次の出陣までの残りをご案内しています。

### 1 日の挑戦回数について

出陣チケットとは別に、1 日に挑める回数にも上限がございます (基本 10 回 / 日)。
ショップで挑戦枠を最大 5 枠まで拡張いただくこともできますよ。

「今日はもう挑戦できません」と表示された場合は、翌日の日付切替 (0:00) までお待ちください。

### 敵の弱点・耐性の表示について

敵の弱点・耐性情報は、**一度でも勝利していただいた敵にのみ表示** される仕様です。
強さが未知数な状態でご挑戦いただく緊張感を大切にしているためです。

一度倒した相手には、次回から戦い方のヒント (弱点属性 / 耐性属性) を表示いたしますね 🪶

### 回復薬の使い方

戦闘前のシートで使用予定数 (0-3 個) を設定いただくと、
**HP が 30% 以下になった際に自動で 1 個ずつ使用** されます。

戦闘中に手動で使うタイミングを考える必要はなく、あなたは攻撃のリズムに集中できます。
回復薬はショップで 💎 でお買い求めいただけます。

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 📅 カレンダー

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_CALENDAR"
    title="カレンダーの見方"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

カレンダーでは、日々の積み重ねを月表示で振り返ることができます。
過去の達成記録や統計を確認したり、これからの予定を追加したりできます。

**主な操作**

<div class="step-list">
<ol>
<li>下部メニューから「カレンダー」を開く</li>
<li>マスをタップすればその日の記録が表示されます</li>
<li>「30 日統計」でここまでの歩みをグラフで振り返れます</li>
<li>右上の「+」で予定を追加できます</li>
</ol>
</div>

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 🦉 キャラクター

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_CHARACTER"
    title="キャラクターの育て方・変更"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

Sabiowl では、あなたの相棒となるキャラクター 1 体を選んで冒険します。
キャラクターごとに得意な戦い方 (ジョブ) があり、あなたの成長がそのままキャラクターの強さになります。

**主な操作**

<div class="step-list">
<ol>
<li>メニュー (☰) → 「キャラ変更」で所持キャラを確認</li>
<li>気に入ったキャラを選んで「使う」で相棒交代</li>
<li>ステータス画面で 6 つの能力値の成長を確認できます</li>
<li>レベルアップ時にステータスポイントを手動配分することも可能です</li>
</ol>
</div>

**キャラクターの入手経路**

- ガチャ (Weekly の SSR キャラ / Monthly の未所持 SSR キャラ確定)
- ダイヤ購入 (Shop → キャラ購入、6000 ダイヤ)
- Monthly 21 日達成報酬 (SSR 確定チケット)

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 🎰 ガチャ

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_GACHA"
    title="ガチャの引き方"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

ガチャは、日々の積み重ねへのささやかなご褒美として設計されています。

**3 種類のガチャ**

| 種類 | チケット入手 | 主な報酬 |
|---|---|---|
| **デイリー** | ログイン + 習慣達成 | 経験値 / XP ブースト / 武器 |
| **ウィークリー** | 週間ミッション達成 | ダイヤ / XP ブースト / 武器 / **SSR キャラ (0.5%)** |
| **マンスリー** | 当月 21 日達成で SSR 確定 | **未所持 SSR キャラ確定** |

**引き方の流れ**

<div class="step-list">
<ol>
<li>メニュー (☰) → 「ガチャ」でガチャ画面を開く</li>
<li>チケット枚数に応じて「引く」ボタンをタップ</li>
<li>演出後、報酬が獲得されます (履歴からいつでも確認可能)</li>
</ol>
</div>

### 月間 21 日達成の SSR 確定チケットについて

その月の累計達成日数 (**連続でなくて構いません**) が **21 日に達した瞬間** に、
SSR 確定ガチャチケットを 1 枚お贈りいたします。

ガチャ画面でこのチケットをお使いいただくと、**未開放の SSR キャラクターが必ず 1 体獲得** できます。
月末ではなく達成した瞬間に届くため、日々の積み重ねへのご褒美として自然に受け取っていただけますよ 🪶

**入手経路のまとめ**

- 継続 21 日達成 (月 1 枚) — 未所持 SSR キャラ確定
- Weekly ガチャ (0.5% 確率) — サプライズ的な出会い
- Shop でのダイヤ購入 (💎 6,000) — 好きなキャラを狙って入手

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## 💎 ダイヤの購入 (プレミアム)

<div class="video-wrapper">
  <!-- TODO: 実際の YouTube 動画 ID に置換 -->
  <iframe
    src="https://www.youtube.com/embed/PLACEHOLDER_DIAMOND"
    title="ダイヤの購入方法"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
</div>
<p class="video-placeholder-note">▲ 動画 ID は仮設定です。実際の解説動画は近日公開予定です 🪶</p>

ダイヤは、キャラ購入・拡張枠・休息の果実などにお使いいただけるアプリ内通貨です。
無料でも十分にお楽しみいただけますが、応援いただける方は課金でダイヤをお求めいただくこともできます。

**3 種類のダイヤパック**

| 商品 | 価格 | 内容 |
|---|---:|---|
| ダイヤ 120 | 120 円 | 120 個 |
| ダイヤ 660 | 600 円 | 660 個 (+10% ボーナス) |
| ダイヤ 1440 | 1,200 円 | 1,440 個 (+20% ボーナス) |

**購入の流れ**

<div class="step-list">
<ol>
<li>メニュー (☰) → 「ダイヤを購入」を開く</li>
<li>ご希望のパックを選択</li>
<li>Apple ID で認証</li>
<li>購入完了後、ダイヤが自動的に加算されます</li>
</ol>
</div>

**購入前にご確認ください**

- 未成年の方は、必ず保護者の同意を得てからご購入ください
- 購入内容は復元 (再インストール時) が可能です
- 返品・返金は Apple の規約に準じます (詳細は[特定商取引法に基づく表示](specified_commercial_transactions.html)を参照)

<p class="back-to-toc"><a href="#目次">↑ 目次に戻る</a></p>

---

## その他

- ❓ [よくあるご質問](faq.html) — 課金・トラブル対応・アカウント運用の Q&A
- 📝 [リリースノート](release_notes.html) — 各バージョンの主な変更点
- 🪶 [プライバシーポリシー](privacy_policy.html) — 個人情報の取り扱いについて
- 📜 [利用規約](terms_of_service.html) — 本サービスのご利用条件について

ご不明な点がございましたら、アプリ内「設定 → お問い合わせ」よりお気軽にご連絡ください。
あなたが穏やかに Sabiowl の世界を楽しんでいただけますよう、心を込めてお手伝いさせていただきます 🪶

<p style="color: #666; font-size: 0.9em; text-align: center; margin-top: 40px;">
  © 2026 Sabiowl. All rights reserved.
</p>
