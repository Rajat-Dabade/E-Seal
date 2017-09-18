<?php
// 	$item='';
//     $tmp = shell_exec("python EncryptFile.py Upload/119680rajat.txt");
//     echo $tmp;
//
$pyscript = 'C:\\xampp\\htdocs\\authentication\\EncryptFile.py';
$python = 'C:\\Python27\\python.exe';
$filePath = 'C:\\xampp\\htdocs\\authentication\\Upload\\119680rajat.txt';
$up = '119680rajat.txt';
echo `$python $pyscript $filePath $up`;
?>