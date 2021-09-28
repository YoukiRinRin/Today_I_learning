<!DOCTYPE html>
<head>
    <meta charset = "utf-8"/>
    <title>あらちゃんねる</title>
    <link rel="stylesheet" href="style.css">
</head>

<html>




<?php

$board_id = $_GET["board"];

$dsn = 'mysql:host=localhost;dbname=test';
$your_name = 'test';
$db_name = 'test';
$password ='test';


$cone_db = new PDO($dsn,$your_name,$password);

$sele_que_thread = "SELECT * FROM bbs_thread where board_id =".$board_id[0];
$stmt_thread = $cone_db->query($sele_que_thread);


while($row = $stmt_thread->fetch(PDO::FETCH_ASSOC)){
    echo '<a href = "thread.php?thre%5B%5D='.$row["id"].'">'.$row["thread"].'</a><br>';
}
?>