flg_retry = 0
while(1):
    if flg_retry == 0:
        print('吾輩は最強じゃんけんAIだ！\n吾輩に勝てる者はいない！!!')
        while(1):
            inp_sele = input('勝負するか？；Y/N')
            if inp_sele == 'Y' or inp_sele == 'y':
                print('おっけー')
                break
            elif inp_sele == 'N' or inp_sele == 'n':
                print('怖気ついたか！グハハハハ！！！')
                exit()
            else:
                print('正しい値を入力するがよい・・・そうしないと吾輩と対戦できないぞ・・')
    else:
        print('何度やっても同じことよ・・・')            

    print('それではいくぞ・・・じゃーん、けーん・・・')

    while(1):
        inp_hand = input('出す手を入力してね\n1:グー 2:チョキ 3:パー')
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
        else:     
            print('正しい値を入力してね。')

    print('おまえの負け―！！！！\nやはり吾輩に勝てるものなどいないのだ！！！！\nグハハハハハハハハハ！！！！！！！！！！！')

    inp_sele2 =input('負けました・・・\nもう一回挑戦しますか？Y/N')
    if inp_sele2 == 'Y' or inp_sele2 == 'y':
        flg_retry = 1
    elif inp_sele2 == 'N' or inp_sele2 == 'n':
        print('終了します。')
        exit()
