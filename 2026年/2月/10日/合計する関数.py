
#参考URL：https://www.miraiserver.ne.jp/column/about_python-coding-method/
def sum(numbers):
    total = 0

    for i in numbers:
        total = total + i
        return total
    

a = [1,2,3,4,5]
b = [1,10,100,1000]
c = [5,10,20,25]

d = sum(a)
e = sum(b)
f = sum(c)

print(d,e,f)