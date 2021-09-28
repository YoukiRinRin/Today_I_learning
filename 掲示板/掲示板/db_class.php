<?php

class cone_db extends PDO{
 Private $user_name = 'youki';
 Private $db_name = 'test';
 Private $host = 'local_host';
 Private $password ='ykif5515';

 Private $sele_que_board = "SELECT * FROM bbs_board";
 Private $sele_que_cate = "SELECT * FROM bbs_category";
 Private $sele_que_res = "SELECT * FROM bbs_responce";
 Private $sele_que_thre = "SELECT * FROM bbs_thread";
    
 function sele_db($query){     
    $stmt =$dbh->query($query);
}
}
?>