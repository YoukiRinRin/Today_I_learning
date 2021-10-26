import re
import vowel

inp_str = input('文字列を入力してね')

char_list = list(inp_str)

regex_hira = '[\u3041-\u309F]'
regex_kata = '[\u30A1-\u30FF]'
result_hira =''
result_kata = ''

list_vowel = []




for i in range(len(char_list)):       
        result_hira = re.match(regex_hira,char_list[i])
        result_kata = re.match(regex_kata,char_list[i])

        if result_hira:
                list_vowel.append(vowel.hira[char_list[i]])
        elif result_kata:
                list_vowel.append(vowel.kata[char_list[i]])

print(''.join(list_vowel))