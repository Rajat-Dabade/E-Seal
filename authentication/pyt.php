<?php
	$item='Upload/119680rajat.txt';
    $tmp = shell_exec("python EncryptFile.py $item");
    echo $tmp;
?>