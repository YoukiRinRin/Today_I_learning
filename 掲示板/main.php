<!DOCTYPE html>
<head>
    <meta charset = "utf-8"/>
    <title>ひとこと掲示板</title>
    <link rel="stylesheet" href="style.css">
    
</head>
<html>
<h1>No</h1>
<h1>名前</h1>
<h1>2021/09/16/</h1>
<h1>本文</h1>
<form action ="db_update.php" method="post">
    <label for="name">お名前：</label>
    <input type ="text" name = "name">
    <label for="name">E-mail：</label>
    <input type ="text" name = "E-mail">
    <input type ="text" name = "sentence">
    <input type ="submit" name = "btn" value = "書き込む">
</form>

</html>

<?php
$dsn      = 'mysql:dbname=test;host=localhost';
$user     = 'youki';
$password = 'ykif5515';

$a = 'unko';
echo'<p>'.$a.'</p>';

// DBへ接続
try{
    $dbh = new PDO($dsn,$user,$password);

    // クエリの実行
    $query = "SELECT * FROM board_table";
    $stmt = $dbh->query($query);

    // 表示処理
    while($row = $stmt->fetch(PDO::FETCH_ASSOC)){
        echo '<h4>'.$row["No"].'</h4>';
        echo '<h4>'.$row["Name"].'</h4><br>';
        echo '<h4>'.$row["Date"].'</h4><br>';
        echo '<h4>'.$row["main_text"].'</h4><br>';
    }

}catch(PDOException $e){
    print("データベースの接続に失敗しました".$e->getMessage());
    die();
}

// 接続を閉じる
$dbh = null;

?>


