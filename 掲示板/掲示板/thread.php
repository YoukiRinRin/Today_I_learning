<!DOCTYPE html>
<head>
    <meta charset = "utf-8"/>
    <title>あらちゃんねる</title>
    <link rel="stylesheet" href="style.css">
</head>

<html>

<section class = "kakikomi">
<div>
    <h1>No</h1>
</div>
<div>
    <h1>名前</h1>
</div>
<div>
    <h1>2021/09/16/</h1>
</div>
<div>
    <h1>本文</h1>
</div>
</section>

</html>

<?php

$dsn = 'mysql:host=localhost;dbname=test';
$your_name = 'test';
$db_name = 'test';
$password ='test';
$thread_id = $_GET["thre"];

const sele_que_res = "SELECT * FROM bbs_response where thread_id =";
$res_id = sele_que_res.$thread_id[0];


$cone_db = new PDO($dsn,$your_name,$password);

$stmt_res = $cone_db->query($res_id);

while($row = $stmt_res->fetch(PDO::FETCH_ASSOC)){
    echo '<p>No</p>';
    echo '<p>名前'.$row["name"].'</p>';
    echo '<p>本文'.$row["response"].'</p>';
    echo '<p>投稿日時'.$row["create_dt"].'</p>';
}








?>
    