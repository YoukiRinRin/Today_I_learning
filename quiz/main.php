<?php


require'db_access.php';
require'show_quiz.php';
require'global.php';


get_mondai();

f_showquiz($out_mondai[0],$out_kaitou1[0],$out_kaitou2[0],$out_kaitou3[0],$out_kaitou4[0]);





?>