"""【FEAT-519 Phase 1】言語切替リンクの対応表が実ページと一致しているか検証する。

## なぜ必要か

`_layouts/page_with_lang.html` は `_data/i18n.yml` の `pairs` を
**`page.url` と完全一致**で引く。1 文字でもずれると

  - 切替リンクが出ない (対応表に無い扱いになる)
  - リンク先が 404 になる

のどちらかが起きるが、**Jekyll はビルドエラーにしない**。
GitHub Pages 側でビルドされるためローカルで気づく機会も無い。

さらに `_data/i18n.yml` には「英語版ページを追加したらここに 1 行足すこと」
という **人間が忘れる種類の約束** がある (アプリ側の `app_urls.dart` と同型)。
これを機械で縛る。

## 使い方

    python scripts/verify_i18n_links.py

push 前に実行する。終了コード 0 で OK。
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent


def front_matter(path: Path) -> dict[str, str]:
    """front matter を素朴に読む (ネストの無い `key: value` だけを想定)。"""
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}
    end = text.index('\n---', 3)
    out = {}
    for line in text[3:end].split('\n'):
        m = re.match(r'^(\w+):\s*(.*)$', line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def page_url(path: Path, fm: dict[str, str]) -> str:
    """Jekyll が付ける `page.url` を再現する。

    permalink があればそれ。無い場合、index.md はサイトルート `/`。
    """
    if 'permalink' in fm:
        return fm['permalink']
    if path.stem == 'index':
        return '/'
    return f'/{path.stem}.html'


def load_pairs() -> list[dict[str, str]]:
    """`_data/i18n.yml` の pairs を読む (PyYAML 非依存の素朴パーサ)。"""
    text = (ROOT / '_data/i18n.yml').read_text(encoding='utf-8')
    pairs, cur = [], None
    in_pairs = False
    for raw in text.split('\n'):
        line = raw.rstrip()
        if re.match(r'^\w+:', line):
            in_pairs = line.startswith('pairs:')
            if not in_pairs and cur:
                pairs.append(cur)
                cur = None
            continue
        if not in_pairs:
            continue
        m = re.match(r'^\s*-\s*ja:\s*(\S+)', line)
        if m:
            if cur:
                pairs.append(cur)
            cur = {'ja': m.group(1)}
            continue
        m = re.match(r'^\s*en:\s*(\S+)', line)
        if m and cur:
            cur['en'] = m.group(1)
    if cur:
        pairs.append(cur)
    return pairs


def main() -> int:
    pages = {p: front_matter(p) for p in sorted(ROOT.glob('*.md'))
             if p.name != 'README.md'}
    urls = {page_url(p, fm): p.name for p, fm in pages.items()}
    pairs = load_pairs()

    errors: list[str] = []

    # ① 対応表の URL がすべて実在すること
    for pair in pairs:
        for side in ('ja', 'en'):
            url = pair.get(side)
            if url is None:
                errors.append(f'pairs に {side} が欠けている: {pair}')
            elif url not in urls:
                errors.append(
                    f'対応表の {side}: {url} に該当ページが無い '
                    f'(リンク切れになる)。実在 URL: {sorted(urls)}')

    # ② 英語ページが漏れなく対応表に載っていること
    #    ← 「英語版を追加したら 1 行足す」を忘れると切替リンクが出ない
    listed_en = {pair.get('en') for pair in pairs}
    for p, fm in pages.items():
        if fm.get('lang') == 'en' and page_url(p, fm) not in listed_en:
            errors.append(
                f'{p.name} は lang: en だが _data/i18n.yml の pairs に無い。'
                f'切替リンクが出ない')

    # ③ 英語ページに lang: en が付いていること
    #    ← minima は page.lang を見る。無いと <html lang="ja"> のまま配信され、
    #      スクリーンリーダーが英文を日本語として読む
    for url in listed_en:
        name = urls.get(url)
        if name is None:
            continue
        fm = next(fm for p, fm in pages.items() if p.name == name)
        if fm.get('lang') != 'en':
            errors.append(f'{name}: lang: en が無い (<html lang="ja"> で配信される)')

    # ④ 全ページが切替リンク付きの layout を使っていること
    for p, fm in pages.items():
        if fm.get('layout') != 'page_with_lang':
            errors.append(
                f'{p.name}: layout が {fm.get("layout")!r}。'
                f'page_with_lang でないと切替リンクが出ない')

    print(f'ページ {len(pages)} 件 / 対応表 {len(pairs)} 組を検証\n')
    if errors:
        print('❌ 問題あり:')
        for e in errors:
            print(f'  - {e}')
        return 1

    print('✅ 対応表と実ページが一致')
    covered = {u for pair in pairs for u in pair.values()}
    missing = sorted(set(urls) - covered)
    if missing:
        print('\n英語版が未整備のページ (切替リンクは'
              '「English version not available」表示):')
        for u in missing:
            print(f'  {u:42s} {urls[u]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
