

<?php

if(isset($_POST["lat"])){
$myfile = fopen("addloc.csv", "w") or die("Unable to open file!");

$no=$_POST["no"];
for($i=0;$i<$no;$i++){
if(!empty($_POST["lat".$i]) and !empty($_POST["lon".$i])){
$txt = $_POST["lat".$i]."##". $_POST["lon".$i]."\n";
fwrite($myfile, $txt);

}

}


if(!empty($_POST["lat"]) and !empty($_POST["lon"])){
$txt = $_POST["lat"]."##". $_POST["lon"]."\n";
fwrite($myfile, $txt);
}
fclose($myfile);


}
?>



<html>
<body>

<form action="gpsset.php" method="post">
<?php 
$i=0;
$handle = fopen("addloc.csv", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        echo "<h3>Location of point ".$i." </h3>";
        $loca = explode("##", $line);	
	echo "Lat: <input type='text' value='".$loca[0]."' name='lat".$i."'><br>";
        echo "Lon: <input type='text' value='".$loca[1]."' name='lon".$i."'><br>";
	$i=$i+1;	

    }
echo "<input type='hidden' value='".$i."' name='no'><br>";

 echo "<h3>Location of new point </h3>";
    fclose($handle);
} else {
    // error opening the file.
} 
?>

Lat: <input type="text" name="lat"><br>
Lon: <input type="text" name="lon"><br>
<input type="submit">
</form>

</body>
</html>
