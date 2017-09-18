<?php

$app->get('/admin/example', $admin(), function() use($app){
	$dir_path = "../Upload/";
	if(is_dir($dir_path)){
		$files = scandir($dir_path);
	}
	$app->render('admin/example.php', [
		'files' => $files
	]);
})->name('admin.example');

$app->post('/admin/example', function() use($app){

	$file = basename($_POST['file1']);
	$file = '../Upload/'.$file;

	if(!$file)
	{
		$app->flash('global', 'File not Found');
		return $app->response->redirect($app->urlFor('home'));
	}
	else
	{
		
    	header("Cache-Control: public");
		header("Content-Description: File Transfer");
		header("Content-Disposition: attachment; filename=".$file."");
		header("Content-Type: application/txt");
        header("Content-Type: application/force-download");
		header("Content-Transfer-Encoding: chunked");
        header('Connection: Keep-Alive');
        ob_clean();
        flush();
		readfile($file);
		$app->flash('global', 'Downloaded');
		return $app->response->redirect($app->urlFor('home'));
	}

})->name('example.post');