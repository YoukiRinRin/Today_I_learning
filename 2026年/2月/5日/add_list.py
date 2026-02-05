#pythonのコードを綺麗にするイディオム
# #リストの処理
#参考URL：https://hachibeechan.hateblo.jp/entry/Python-idiom-101#google_vignette


#要素をリストに追加していきたい
# #悪い例

li = []
for i in range(10):
    li.append(i)

#いい例

li = [i for i in range(10)]