<?php
$hight = $_POST["num_Height"];
$weight = $_POST["num_Weight"];
$sex = $_POST["rd_sex"];
$age =$_POST["num_age"];

$M_BMR = 13.397*$weight+4.799*$hight-5.677*$age+88.362;
$F_BMR = 9.247*$weight+3.098*$hight-4.33*$age+447.593;
$BMR = 0;

$hight2 = ($hight / 100) * ($hight /100);


$BMI = $weight / $hight2 ;

if ($sex == 'm'):
    $BMR = $M_BMR;
elseif($sex == 'f'):
    $BMR = $M_BMR;
endif;
echo '<p>あなたのBMIは'.round($BMI,2).'です</p>';
echo '<p>あなたの基礎代謝(BMR)は'.$BMR.'kcalです</p>';


?>