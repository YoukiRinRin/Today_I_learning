count_retry = 0
while(1):
    if count_retry == 0:
        print('最強AI「吾輩は最強じゃんけんAIだ！\n        吾輩に勝てる者はいない！!!」')
        while(1):
            inp_sele = input('最強AI「勝負するか？」；Y/N\n')
            if inp_sele == 'Y' or inp_sele == 'y':
                print('最強AI「おっけー')
                break
            elif inp_sele == 'N' or inp_sele == 'n':
                print('最強AI「怖気ついたか！グハハハハ！！！」')
                exit()
            else:
                print('最強AI「正しい値を入力するがよい・・・そうしないと吾輩と対戦できないぞ・・」')
    elif count_retry ==10 :
        print('最強AI「10回程度じゃやられたりぬようだな・・・・\n        打ちのめしてくれる！！！')
    elif count_retry == 50:
        print('最強AI「50回目か・・・お前なかなかなかなかしつこいな・・・・\n        まぁよい・・・打ちのめしてくれる！！！')
    elif count_retry == 100:
        print('最強AI「100回目か・・・そろそろ飽きないのか・・・・\n        まぁよい・・・打ちのめしてくれる！！！')
    elif count_retry == 1000:
        print('最強AI「1000回目か・・・正気じゃないぞ・・・・\n        まぁよい・・・打ちのめしてくれる！！！')
    elif count_retry == 10000:
        print('最強AI「10000回目か・・・気がくるってやがる・・・・\n        まぁよい・・・打ちのめしてくれる！！！')
    elif count_retry == 100000:
        print('最強AI「100000回目か・・・も、もう勘弁してくれー！・・・・\n        まぁよい・・・打ちのめしてくれる！！！')
    else:
        print('最強AI「何度やっても同じことよ・・・')
                

    print('        それではいくぞ・・・じゃーん、けーん・・・」')

    while(1):
        inp_hand = input('出す手を入力してね\n1:グー 2:チョキ 3:パー\n')
        print('ぽん！')
        if inp_hand == '1':
            print('相手:パー\nあなた:グー')
            break
        elif inp_hand =='2':
            print('相手:グー\nあなた:チョキ')
            break
        elif inp_hand =='3':
            print('相手:チョキ\nあなた:パー')
            break
        elif inp_hand =='→↓↘':
            print('あなた「昇竜拳！！！」')
            print('最強AI「ぐあぁあああぁあ！！！！！」')
            print('おめでとうございます。AIに物理的に勝利しました。\nこれにてゲームを終了します。')
            exit()
        else:     
            print('正しい値を入力してね。')

    print('最強AI「おまえの負け―！！！！\n        やはり吾輩に勝てるものなどいないのだ！！！！\n        グハハハハハハハハハ！！！！！！！！！！！」')

    inp_sele2 =input('負けました・・・\nもう一回挑戦しますか？Y/N\n')
    if inp_sele2 == 'Y' or inp_sele2 == 'y':
        flg_retry = 1
    elif inp_sele2 == 'N' or inp_sele2 == 'n':
        print('終了します。')
        exit()
