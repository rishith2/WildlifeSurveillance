<!-- This file Displays the images captured by devices in 'most recent one first' order-->





<!DOCTYPE html>
<html lang="en">
<head>
	<title>Recorded images</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>

	<div class="bg-contact2" style="background-image: url('images/bg-01.jpg');">
		<div class="container-contact2">
			<div class="wrap-contact2">
				


<form class="contact2-form validate-form" ">
					<span class="contact2-form-title">
						Recorded images
					</span>





<?php
$handle = file("uploaddata.csv");
if (count($handle)>0) {
    $n=count($handle);
	for($i=0;$i<$n;$i++) {
        $line=$handle[$n-$i-1];
        $ims = explode(",,", $line);
		if (count($ims)==4){
		    	echo " <div class='wrap-input2' >";
echo "<h4> Received from Device ".$ims[1]."</h4><br>";
echo "<h5> Detected ".$ims[2]."</h5><br>";
echo "<h5> Time Stamp ".$ims[0]."</h5><br>";
echo "<img src='".$ims[3]."' alt='File Missing from server'><br><br><br><br></div>";

		}}}
?>




					


</form>

			</div>
		</div>
	</div>




<!--===============================================================================================-->
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13"></script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'UA-23581568-13');
	</script>

</body>
</html>

