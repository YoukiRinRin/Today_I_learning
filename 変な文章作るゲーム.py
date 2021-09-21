import random

a = {1:'私',2:''}
b = {1:'は',2:'を'}
c = {1:'りんご'}
d = {1:'食べる'}

e = {1:'e1',2:'e2',3:'e3',4:'e4',5:'e5',6:'e6',7:'e7',8:'e8'}
f = {1:'f1',2:'f2',3:'f3',4:'f4',5:'f5',6:'f6',7:'f7',8:'f8'}
g = {1:'g1',2:'g2',3:'g3',4:'g4',5:'g5',6:'g6',7:'g7',8:'g8'}
h = {1:'h1',2:'h2',3:'h3',4:'h4',5:'h5',6:'h6',7:'h7',8:'h8'}

ran_min = 1
ran_max_e = len(e)
ran_max_f = len(f)
ran_max_g = len(g)
ran_max_h = len(h)

#a_ran = random.randint(ran_min,ran_max_e)
#b_ran = random.randint(ran_min,ran_max_f)
#c_ran = random.randint(ran_min,ran_max_g)
#d_ran = random.randint(ran_min,ran_max_h)



a_ran =  random.sample(range(1,len(e)),3)
a_ran_1 =a_ran[0]
a_ran_2 =a_ran[1]
a_ran_3 =a_ran[2]

b_ran = random.sample(range(1,len(f)),3)
b_ran_1 =b_ran[0]
b_ran_2 =b_ran[1]
b_ran_3 =b_ran[2]

c_ran = random.sample(range(1,len(g)),3)
c_ran_1 =c_ran[0]
c_ran_2 =c_ran[1]
c_ran_3 =c_ran[2]

d_ran = random.sample(range(1,len(h)),3)
d_ran_1 =d_ran[0]
d_ran_2 =d_ran[1]
d_ran_3 =d_ran[2]

array_a = {'1':e[a_ran_1],'2':e[a_ran_2],'3':e[a_ran_3]}
array_b = {'1':f[b_ran_1],'2':e[b_ran_2],'3':f[b_ran_3]}
array_c = {'1':g[c_ran_1],'2':g[c_ran_2],'3':g[c_ran_3]}
array_d = {'1':h[d_ran_1],'2':h[d_ran_2],'3':h[d_ran_3]}

print(array_a)
A = str(input('言葉を選んでね'))

B = str(input(''))
C = str(input(''))
D = str(input(''))


print(array_a[A]+array_b[B]+array_c[C]+array_d[D])
