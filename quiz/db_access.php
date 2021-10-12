<?php


function get_mondai(){
    
    $dsn = 'mysql:dbname=test;host=localhost';
    $user = "test";
    $pass = "test";

    $query = "SELECT * FROM quiz";

    $cone_db = new PDO($dsn,$user,$pass);

    $ix = 0;

    try{
        $stmt_cate = $cone_db->query($query);
        
        // 表示処理
        while($row = $stmt_cate->fetch(PDO::FETCH_ASSOC)){

            $out_mondai[$ix] =$row["mondai"];
            $out_seikai[$ix] = $row["seikai"];
            $out_kaitou1[$ix] =$row["kaitou1"];
            $out_kaitou2[$ix] =$row["kaitou2"];
            $out_kaitou3[$ix] =$row["kaitou3"];
            $out_kaitou4[$ix] =$row["kaitou4"];

            echo $out_mondai[$ix];
            echo $out_seikai[$ix];
            echo $out_kaitou1[$ix]; 
            echo $out_kaitou2[$ix];
            echo $out_kaitou3[$ix];
            echo $out_kaitou4[$ix];

            
            $ix += 1;
        }
    }catch(PDOException $e){
        print("データベースの接続に失敗しました".$e->getMessage());
        die();
    }

   


}

?>