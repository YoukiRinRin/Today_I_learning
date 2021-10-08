import pprint


food_dic={}
food =''
calorie = ''

calorie_total = 0
a = ''

age_key = ''

m_BMR = {'1-2':61,'3-5':54.8,'6-7':44.3,'8-9':40.8,'10-11':37.4,'12-14':31.0,'15-17':27.0,'18-29':24.0,'30-49':22.3,'50-69':21.5,'70-':21.5}
f_BMR = {'1-2':59.7,'3-5':52.2,'6-7':41.9,'8-9':38.3,'10-11':34.4,'12-14':29.6,'15-17':25.3,'18-29':22.1,'30-49':21.7,'50-69':20.7,'70-':20.7}

age = int(input('年齢を入力してください'))
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


if age == 1 and age == 2:
    age_key = '1-2'
elif age >= 3 and age <= 5:
    age_key = '3-5'
elif age >= 6 and age <= 7:
    age_key = '6-7'
elif age >= 8 and age <= 9:
    age_key = '8-9'
elif age >= 10 and age <= 11:
    age_key = '10-11'
elif age >= 12 and age <= 14:
    age_key = '12-14'
elif age >= 15 and age <= 17:
    age_key = '15-17'
elif age >= 18 and age <= 29:
    age_key = '18-29'
elif age >= 30 and age <= 49:
    age_key = '30-49'
elif age >= 50 and age <= 69:
    age_key = '50-69'
elif age >= 70:
    age_key = '70-'





print(m_BMR[age_key])

if sex == 'm':
    if calorie_total > m_BMR[age]:
        print('摂取カロリーが基礎代謝を'+calorie_total-m_BMR[age_key]+'オーバーしています')
    elif calorie_total < m_BMR[age]:
        print('摂取カロリーが基礎代謝を'+m_BMR[age_key]-calorie_total+'下回っています')
    else:
        print('摂取カロリーと基礎代謝が一致しています。')
elif sex == 'f':
    if calorie_total > m_BMR[age_key]:
        print('摂取カロリーが基礎代謝を'+calorie_total-f_BMR[age_key]+'オーバーしています')
    elif calorie_total < m_BMR[age_key]:
        print('摂取カロリーが基礎代謝を'+f_BMR[age_key]-calorie_total+'下回っています')
    else:
        print('摂取カロリーと基礎代謝が一致しています。')





print(calorie_total)

