#pythonのコードを綺麗にするイディオム
# #リストの処理
#参考URL：https://hachibeechan.hateblo.jp/entry/Python-idiom-101#google_vignette


#インデックスを取り出しながら値も欲しい場合
#悪い例
datas = ['a','b','c']
for i in range(len(datas)):
    print(i)
    print(datas[i])
#良い例

for i, data in enumerate(datas):
    print(i)
    print(data)

"""
eumerate()関数
forループの中でリストやタブルなどの
イテラブルオブジェクトの要素と同時に、
インデックス番号（カウント、順番）を取得できる

イテラブルオブジェクト
iterable 反復可能であるの意
つまりfor文などで要素を１ずつ取り出し処理できるような
オブジェクトのこと
例：リスト、辞書、タプル、文字列

"""
