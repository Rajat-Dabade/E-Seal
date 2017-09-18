<?php


$app->get('/upload', function() use($app){
	$app->render('uploadpaper/upload.php');
})->name('upload');

$app->post('/upload', function() use($app){


	 if(isset($_FILES['UploadFileField'])){
   	     $uploadName = $_FILES['UploadFileField']['name'];
   	     $uploadName = mt_rand(100000, 999999).$uploadName;
   	     $uploadTmp = $_FILES['UploadFileField']['tmp_name'];
   	     $uploadType = $_FILES['UploadFileField']['type'];
   	     $fileSize =  $_FILES['UploadFileField']['size'];

   	     

   	     if($fileSize > 1250000){
   	     	die("Error File is to large to upload");
   	     }

         if(!$uploadTmp){
         	die("NO file is selected.Please upload again");
         }
         else{
         	move_uploaded_file($uploadTmp, "../Upload/$uploadName");

            $path = '../Upload/'.$uploadName;

            $pyscript = 'C:\\xampp\\htdocs\\authentication\\EncryptFile.py';
            $python = 'C:\\Python27\\python.exe';
            $filePath = 'C:\\xampp\\htdocs\\authentication\\Upload\\'.$uploadName;

            echo `$python $pyscript $filePath $uploadName`;
            
            unlink($path);

         	$app->flash('global', 'The File have been successfully uploaded');
         	return $app->response->redirect($app->urlFor('home'));
         }

   }



})->name('upload.post');