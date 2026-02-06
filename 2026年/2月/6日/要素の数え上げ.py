#pythonのコードを綺麗にするイディオム
# #リストの処理
#参考URL：https://hachibeechan.hateblo.jp/entry/Python-idiom-101#google_vignette


#要素をリストに追加していきたい
# #悪い例

data = ['aaa', 'bbb', 'ccc', 'aaa', 'ddd']

word_and_counts = {}
for word in data:
    if word_and_counts.has_key(word):
        word_and_counts[word] += 1
    else:
        word_and_counts = 1
     
#良い例
from collections import Counter

counter = Counter(data)



