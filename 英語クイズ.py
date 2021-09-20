import random

arr_a = {'apple':'りんご','banana':'バナナ'}
arr_q = {1:'apple',2:'banana'}

ram_min = 1
ram_max = len(arr_q)

ary_num = random.randint(ram_min,ram_max)

print(ary_num)
ans = input(str(ary_num)+"は日本語でなんでしょう")

if ans == a[b[ary_num]]:
    print('正解です。') 
else:
    print('不正解です。')

