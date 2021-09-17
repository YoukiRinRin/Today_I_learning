<?php


function show_title($flg_aiko){
    if($flg_aiko == 0){
        echo '<div class ="str_title">
                <h2>ジャンケンゲーム</h2>
            </dim>
            <div class="sentence">
                <p>出す手を選んでね</p>
            </div>';
    }else if($flg_aiko == 1){
        echo '<div class="sentence">
                <p>あ～いこで、</p>
                <p>出す手を選んでね</p>
               </div>';
    }
}

function show_hand(){    
echo
'<div class="hand">
    <div class = "gu">
        <form action = "janken.php" method="POST">
            <input class=input-monster-img type="submit" name="select-gu" alt="送信する" value="gu" id="btn_gu" onclick ="gu_click()">
            <img  src = "img/janken_gu.png">
        </form>
        <p>グー</p>
    
    </div>

    <div class = "choki">
        <form action = "janken.php" method="POST">
            <input class=input-monster-img type="submit" name="select-choki" alt="送信する" value="choki" id="btn_choki" onclick ="choki_click()">
            <img id="choki"src = "img/janken_choki.png" class= "img_choki">
            <p>チョキ</p>
        </form>
    </div>

    <div class = "pa">
        <form action = "janken.php" method="POST">
            <input class=input-monster-img type="submit" name="select-pa" alt="送信する" value="pa" id="btn_gu" onclick ="pa_click()">
            <img  id="pa" src = "img/janken_pa.png" class= "img_pa">
        </form>
        <p>パー</p>
    </div>
</div>';
}
?>