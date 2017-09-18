<?php

$dir_path = "Upload/";

if(is_dir($dir_path)){
	$files = scandir($dir_path);
	{
		for($i = 0; $i < count($files); $i++){
			if($files[$i] != '.' && $files[$i] != '..' ){
				
				echo "<form action='download.php' method='post'>
						<label for=".$files[$i].">".$files[$i]."</label>
						<input type='hidden' name='file1' value=".$files[$i].">
						<input type='submit' value='download'>
					</form>";

			}
		}
	}
}

?>