<!DOCTYPE html>
<head>
    <meta charset = "utf-8"/>
    <title>あらちゃんねる</title>
    <link rel="stylesheet" href="style.css">
</head>

<html>
</html>

<?php

 $dsn = 'mysql:host=localhost;dbname=test';
 $your_name = 'test';
 $db_name = 'test';
 $password ='test';

 const sele_que_board = "SELECT * FROM bbs_board where category_id =";


 $cone_db = new PDO($dsn,$your_name,$password);

try{
    $sele_que_cate = "SELECT * FROM bbs_category";
    $sele_que_board = "SELECT * FROM bbs_board where category_id = ";
  
    
    $stmt_cate = $cone_db->query($sele_que_cate);
    
    // 表示処理
    while($row1 = $stmt_cate->fetch(PDO::FETCH_ASSOC)){
        echo '<h4>'.$row1["category"].'</h4>';

        $board_id = sele_que_board.$row1["id"];
        $stmt_board = $cone_db->query($board_id);
        
        while($row2 = $stmt_board->fetch(PDO::FETCH_ASSOC)){
            echo '<a href = "thread_list.php?board%5B%5D='.$row2["id"].'">'.$row2["board"].'</a><br>';
        }
    }
}catch(PDOException $e){
    print("データベースの接続に失敗しました".$e->getMessage());
    die();
}




?>
    