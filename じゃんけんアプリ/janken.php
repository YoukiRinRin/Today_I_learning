<link rel="stylesheet" href="style.css"></link>
<?php

$select_hand ="";
$cpu_hand = "";

$cpu_rand = mt_rand(1,3);


switch($cpu_rand){
case 1:
    $cpu_hand = "gu";
    break;
case 2:
    $cpu_hand = "choki";
    break;
case 3:
    $cpu_hand = "pa";
    break;
}

//選択した手を取得
if( isset($_POST["select-gu"]) ){
    $select_hand = $_POST["select-gu"];
}else if(isset($_POST["select-choki"])){
    $select_hand = $_POST["select-choki"];
}else if(isset($_POST["select-pa"])){
    $select_hand = $_POST["select-pa"];
}

//プレイヤーが勝ちの場合
if ((($select_hand == "gu" ) && ( $cpu_hand == "choki"))or
    (($select_hand == "choki") && ($cpu_hand == "pa"))or
    (($select_hand == "pa") && ($cpu_hand == "gu"))){
        f_juge($select_hand,$cpu_hand,'kati');
}else if//cpuが勝ちの場合
((($cpu_hand == "gu") && ($select_hand == "choki"))or
(($cpu_hand == "choki") && ($select_hand == "pa"))or
(($cpu_hand == "pa") && ($select_hand == "gu"))){
    f_juge($select_hand,$cpu_hand,'make');
}


//あいこの場合
if($select_hand == $cpu_hand){
    f_juge($select_hand,$cpu_hand,'aiko');
    require("show_hand.php");
        show_title(1);
        show_hand();
}

function f_juge($f_hand,$f_cpu_hand,$f_result){ 
    echo'<div class = "str_title">
        <p>ポン！</p>
        </div>'; 

    #相手の手を表示
    echo '<div class = "f_img_hand">';
    echo '<div class = "img_cpu">';
    if($f_cpu_hand == "gu"){
        echo '<img  id="pa" src = "img/janken_gu.png" class= "img_gu"><br>';
    }else if($f_cpu_hand =="choki"){
        echo '<img  id="pa" src = "img/janken_choki.png" class= "img_choki"<br>';
    }else if($f_cpu_hand == "pa"){
        echo '<img  id="pa" src = "img/janken_pa.png" class= "img_pa"><br>';
    }   
    echo '</div>';

    #自分の手を表示
    echo '<div class = "img_you">';
    if($f_hand == "gu"){
        echo '<img  id="pa" src = "img/janken_gu.png" class= "img_gu"><br>';
    }else if($f_hand =="choki"){
        echo '<img  id="pa" src = "img/janken_choki.png" class= "img_choki"><br>';
    }else if($f_hand == "pa"){
        echo '<img  id="pa" src = "img/janken_pa.png" class= "img_pa"><br>';
    }  
    echo '</div>';
    echo '</div>';

    #結果表示
    echo'<div class = "sentence">';
    if ($f_result == "kati" ){
        echo '  <p>あなたの勝ちです！！</p>';
    }else if($f_result == "make"){
        echo '  <p>あなたの負けです！！</p>';
    }else if($f_result == "aiko"){
        echo '  <p>あいこです</p>';
    }
    echo'</div>';
}
?>