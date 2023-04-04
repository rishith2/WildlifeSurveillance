<?php //This files receives the captured images and detection data and save them in the server 
	
	if (isset($_POST['DeviceID'])){  
		$target="uploadedImages/".$_POST['DeviceID'].date("Y_m_d_h_i_sa").'.jpg';
		move_uploaded_file( $_FILES['image']['tmp_name'], $target);
		$file = fopen("uploaddata.csv", "a") or die("Unable to open file!");
		$txt = date("Y/m/d h:i:sa").",,".$_POST['DeviceID'].",,".$_POST['obj'].",".$target.'\n';
		fwrite($file, $txt.PHP_EOL);
		fclose($file);
		print('done');
		
	}
	else{
	    print('not done');
		
	}
  
?>