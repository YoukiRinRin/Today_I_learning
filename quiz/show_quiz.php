<?php

function f_showquiz($mondai,$Q1,$Q2,$Q3,$Q4){
    echo 
    '<p>'.$mondai.'</p>
    <div class="btn_kaitou">
        <form action ="quiz.php" method="post">
            <input type = "submit" class = "inp_kaitou1" name = "kaitou1" value='.$Q1.'>
            <input type = "submit" class = "inp_kaitou2" name = "kaitou2" value='.$Q2.'>
            <input type = "submit" class = "inp_kaitou3" name = "kaitou3" value='.$Q3.'>
            <input type = "submit" class = "inp_kaitou4" name = "kaitou4" value='.$Q4.'>
        </form>    
    </div>';



}

?>