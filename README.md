# japancode

japancode は、日本の都道府県・市区町村名や各種番号・記号（全国地方公共団体コードなど）を取得・変換するための Python ライブラリです。

## 現在の対応データ

(現在は都道府県レベルのみ対応しています)

- 都道府県名 (漢字、ひらがな、カタカナ)
- [全国地方公共団体コード](https://ja.wikipedia.org/wiki/%E5%85%A8%E5%9B%BD%E5%9C%B0%E6%96%B9%E5%85%AC%E5%85%B1%E5%9B%A3%E4%BD%93%E3%82%B3%E3%83%BC%E3%83%89) ([LGコード](https://fukuno.jig.jp/3356))
- [JIS X 0401](https://ja.wikipedia.org/wiki/%E5%85%A8%E5%9B%BD%E5%9C%B0%E6%96%B9%E5%85%AC%E5%85%B1%E5%9B%A3%E4%BD%93%E3%82%B3%E3%83%BC%E3%83%89#%E9%83%BD%E9%81%93%E5%BA%9C%E7%9C%8C%E3%82%B3%E3%83%BC%E3%83%89) (都道府県コード)
- [ISO 3166-2](https://ja.wikipedia.org/wiki/ISO_3166-2)

## インストール

```bash
pip install japancode
```

## 使い方

### 都道府県名のローマ字表記

```python
from japancode import roman

print(roman("東京都"))  # => 'tokyo'
print(roman("東京都", capitalize=True))  # => 'Tokyo'
```

### 都道府県名のひらがな・カタカナ表記

```python
from kana import kana

print(kana("東京都"))  # => 'とうきょうと'
print(kana("東京都", katakana=True))  # => 'トウキョウト'
```

### 全国地方公共団体コード

```python
from japancode import lgcode

print(lgcode.tocode("東京都"))  # => '130001'
print(lgcode.reverse("130001"))  # => '東京都'
```

### JIS X 0401 (都道府県コード)

```python
from japancode import jiscode

print(jiscode.tocode("東京都"))  # => '13'
print(jiscode.reverse("13"))  # => '東京都'
```

### ISO 3166-2

```python
from japancode import isocode

print(isocode.tocode("東京都"))  # => 'JP-13'
print(isocode.reverse("JP-13")) # => '東京都'
```

## 開発・テスト

```bash
poetry install
poetry run pytest poetry run pytest ./japancode --doctest-modules --cov -vs
```

## ロードマップ

- [ ] 郵便番号
- [ ] 市区町村レベルのコード
- [ ] 地域メッシュ
- [ ] ローマ字の長音表記対応
- [ ] `normalize`
- [ ] `shorten`
- [ ] ドキュメントの整備

## クレジット

- [code4fukui/localgovjp](https://github.com/code4fukui/localgovjp) : list of local government in Japan (日本の地方自治体一覧オープンデータ) JSON/CSV (CC0)

## ライセンス

MIT

<!-- japancode-postal -->
