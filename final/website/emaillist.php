<?php  //This file can be used to view and modify the email list
if(isset($_POST["email"])){
$myfile = fopen("emaillist.txt", "w") or die("Unable to open file!");
$no=$_POST["no"];
for($i=0;$i<$no;$i++){
if(!empty($_POST["email".$i])){
$txt = $_POST["email".$i]."\n";
fwrite($myfile, $txt);
}
}
if(!empty($_POST["email"])){
$txt = $_POST["email"]."\n";
fwrite($myfile, $txt);
}
fclose($myfile);
}
?>




<!DOCTYPE html>
<html lang="en">
<head>
	<title>Contact V2</title>
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
				


<form class="contact2-form validate-form" action="emaillist.php" method="post">
					<span class="contact2-form-title">
						Email List
					</span>







<?php 
$i=0;
$handle = fopen("emaillist.txt", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
	echo " <div class='wrap-input2' >
<input  class='input2' <input type='text' value='".$line."' name='email".$i."'><span class='focus-input2' ></span>
					</div>";
  	$i=$i+1;	
    }
echo "<input type='hidden' value='".$i."' name='no'><br>";
fclose($handle);
} else {
    // error opening the file.
} 
?>
<div class="wrap-input2 ">
<input  class="input2" type="text" name="email"><span class="focus-input2" ></span>
					</div>

<div class="container-contact2-form-btn">
						<div class="wrap-contact2-form-btn">
							<div  class="contact2-form-btn">
							    	<input type="submit" value='Save Changes'>

							</div>
					
						</div>
					</div>
					
					
					


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

