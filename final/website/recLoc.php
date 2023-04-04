<?php // This file records the location data of all the devices in server
if (isset($_POST['DeviceID']) and isset ($_POST['lat'])  and isset ($_POST['lon'])){
$id = $_POST['DeviceID'];
$lat = $_POST['lat'];
$lon = $_POST['lon'];
$fp = fopen('locationfile.csv', 'a');
$savestring = $id . ',' . $lat. ',' . $lon.PHP_EOL;
fwrite($fp, $savestring);
fclose($fp);
echo 'done';
}
else
{echo 'not done';}
?>

