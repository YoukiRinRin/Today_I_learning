import pprint


food_dic={}
food =''
calorie = ''

calorie_total = 0
a = ''

age_key = ''

m_BMR = {'1-2':61,'3-5':54.8,'6-7':44.3,'8-9':40.8,'10-11':37.4,'12-14':31.0,'15-17':27.0,'18-29':24.0,'30-49':22.3,'50-69':21.5,'70-':21.5}
f_BMR = {'1-2':59.7,'3-5':52.2,'6-7':41.9,'8-9':38.3,'10-11':34.4,'12-14':29.6,'15-17':25.3,'18-29':22.1,'30-49':21.7,'50-69':20.7,'70-':20.7}

age = input('年齢を入力してください')
sex = input('性別を入力してください')

while(1):
    food = input('食べたものを入力してね')
    calorie = int(input('そのカロリーを入力してね'))
    food_dic.setdefault(food,calorie)
    a = input('まだ入力しますか？')
    if a == 'n' or a == 'N':
        break

for food_calorie in food_dic.values():
    calorie_total += food_calorie


if age == 1 or age == 2:
    age_key = '1-2'
elif age >= 3 or age <= 5:
    age_key = '3-5'

    
def get_BMR(sex,age):








print(calorie_total)

