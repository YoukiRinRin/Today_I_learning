<!DOCTYPE html>
<html lang="en">
<head>
    <title>楽しいクイズ</title>
    <meta charset="UTF-8">
</head>
<html>

</html>

<?php


    $select_kaitou = "あ";
    echo $select_kaitou;
    
    if( isset($_POST["kaitou1"]) ){
        $select_kaitou = 1;
    }else if(isset($_POST["kaitou2"])){
        $select_kaitou = 2;
    }else if(isset($_POST["kaitou3"])){
        $select_kaitou = 3;
    }else if(isset($_POST["kaitou4"])){
        $select_kaitou = 4;
    }

    echo $select_kaitou;


    require'db_access.php';
    if($select_kaitou == $out_seikai[0]){
        echo '正解';
    }else{
        echo '不正解';
    }





?>