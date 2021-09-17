<!DOCTYPE html>
<head>
    <meta charset = "utf-8"/>
    <title>ジャンケンゲーム</title>
    <link rel="stylesheet" href="style.css">
    
</head>
<html>

<?php
require'show_hand.php';
show_title(0);
show_hand();
?>

</html>


<script type="text/javascript">
    function gu_click() {
        alert("クリックされました:グー");
    }
    function choki_click() {
        alert("クリックされました:チョキ");
    }
    function pa_click() {
        alert("クリックされました:パー");
    }
</script>

