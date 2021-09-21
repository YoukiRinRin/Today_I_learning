<?php


$dsn      = 'mysql:dbname=test;host=localhost';
$user     = 'youki';
$password = 'ykif5515';

$No = '1';
$Name = $_POST["name"];
$Date = date('Y-m-d H:i:s');
$Text = $_POST["sentence"];


try{
    $dbh = new PDO($dsn,$user,$password);

    // クエリの実行
    $stmt = $dbh->prepare('INSERT INTO board_table(No,Name,Date,main_text) VALUES(:No,:Name,:Date,:main_text)');

    $stmt->bindValue(':No', $No);
    $stmt->bindValue(':Name', $Name);
    $stmt->bindValue(':Date', $Date);
    $stmt->bindValue(':main_text', $Text);
    // 表示処理
    $stmt->execute();

}catch(PDOException $e){
    print("データベースの接続に失敗しました".$e->getMessage());
    die();
}



?>