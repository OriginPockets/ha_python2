# Pythonについて

### 1. 必須のルール
- 改行して処理を切る！

```python
print("Hello Python") # 改行して切る
print("Hello Programming")
```


- まとまった処理はインデント（字下げ）を作って指定する！
```python
n = 1

if n == 1:
    print(n)
```
- 大文字と小文字は区別されるため使用には気を付ける！
```python
Print("Hello Python")
```

---

### 2. プログラムを書くときに使えるコツ

- コメントを使う（#記号）
- [PEP8](https://pep8-ja.readthedocs.io/ja/latest/)を参考にする
    - Pythonの標準コーディング規約
    - プログラムを書く際のマナー（お作法）みたいなもの

---

### 3．変数について

__変数__:1つのデータを保管しておく入れ物
```python
n = 100

print(n)
```

#### 変数名のルール
- 英小文字（a ~ z）
- 単語の区切りに _
```md
○ name, student_no
```
- 1文字目に数字は使えない
- 使えないキーワードがある
```md
× 1st_number, forなど
```

#### ⚠️"="は「代入」の意味！
```md
# A = B
→ BをAに代入する（右から左へ）
```

#### 参照する：値を見る
```md
# 変数名（→値に置き換わる）
print(変数名)
```

#### 変数の値は更新できる！
```python
n = 100
print(n)

n = 200
print(n)

n = "Hello Python"
print(n)
```

---

### データの型

```md
データの型の基本4つ

1. int型：数値,数字（1, 2, 3,...）
2. str型：文字列型（"文字"）
3. float型：小数点（3.14）
4. bool型：真偽値（True, False）
```
#### サンプル
```python
a = 30
b = 50
c = "100"
d = "100"
c_1 = int(c) # strからintへ
d_1 = int(d) # strからintへ

print(a + b) # 80と出る
print(a, c)  # 30100とでる
print(a + c) # エラー
print(c + d) # 100100
print(C_1 + d_1)
```

---

### 演算記号
1. +： 足し算（int型）,連結・結合（str型）

2. -： 引き算（int型）

3. *： 掛け算（int型）※アスタリスク

4. **： べき乗 (2 ** 3)

5. /： わり算（float型）

6. //： わり算（int型）

7. ==： イコール（等しい）

8. !=： イコールでない（等しくない）

9. A > B： AがBより大きい

10. A < B： AがBより小さい

11. A >= B： AがB以上(A=Bも成り立つ)

12. A <= B： AがB以下(A=Bも成り立つ)

13. A and B：AとB, AかつB

14. A or B：AまたはB, どちらか片方

#### サンプル
```python
# 足す
a = 100 # int
b = 200 # int
c = a + b

print(c)       # 300
print(type(c)) # int

# 引き算
print(b - a) # 100

# 掛け算
print(a * b) # 200000

# わり算
print(b / a) # 2.0
print(b // a) # 2
```

---

### 配列（リスト）
- 配列：複数のデータをまとめて管理
- リスト(list)の使い方

```md
配列名 = [値1, 値2, 値3, ・・・]
score = [80, 100, 75]
player = ["マリオ", 100]
```

#### 参照する
```md
# 配列名[添え字]

要素→ 80,  100,  75
添字→ [0]  [1]   [2]

score[1] = 100
```

#### リストの便利なメソッド
**関数**：処理をまとめたもの
```md
組込み関数
print()
input()
：

リストの中で使える組込み関数
append()
clear()
：

辞書で使える組込み関数
get()
clear()
：
```

- append(値)：追加
　score.append(85)

- insert(添え字, 値)：挿入
　score.insert(2, 90)

- remove(値)：削除
　score.remove(75)

- clear()：全削除
　score.clear()

#### サンプル
```python
pokemon = ["ピカチュウ", "ホゲータ", "クワッス", "ニャオハ"]

print(pokemon[2]) # クワッスと出力
print(pokemon[:3]) #[0], [1], [2]の要素が出力

pokemon.append("パチリス")
print(pokemon) # パチリスが追加される

pokemon.insert(1, "ゲンガー")
print(pokemon) # ゲンガーが[1]番目に追加される

pokemon.remove("ゲンガー")
print(pokemon)

pokemon.clear()
print(pokemon) # 全削除
```

---
