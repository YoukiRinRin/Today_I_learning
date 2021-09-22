import re 
get_str = input('文字列を入力してね')

pattern_yusuke = '[ア-ン]ー[ア-ン]{2}・[ア-ン]{6}'

result = re.match(pattern_yusuke,get_str)

if result:
    print('ユースケ・サンタマリアっぽい')
else:
    print('ユースケ・サンタマリアっぽくない')