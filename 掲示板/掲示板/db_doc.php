<?php



 $user_name = 'youki';
 $db_name = 'test';
 $host = 'test';
 $password ='test';

 $sele_que_board = "SELECT * FROM bbs_board";
 $sele_que_cate = "SELECT * FROM bbs_category";
 $sele_que_res = "SELECT * FROM bbs_responce";
 $sele_que_thre = "SELECT * FROM bbs_thread";
    
 $cone_db = new PDO();

 function sele_db($query){     
    $stmt =$dbh->query($query);
}

?>