<!-- This file Displays the current locations of the devices in google map-->

<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      #map {
        height: 100%;
      }
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
<?php
$myfile = fopen("locationfile.csv", "r") or die("Unable to open file!");
$dev=array();
$lat=array();
$lon=array();
while(!feof($myfile)) {
	$line=fgets($myfile);
	$arr = explode(",", $line);
	if (count($arr)==3){
		if (!in_array($arr[0], $dev)){ 
		array_push($dev, $arr[0]);
                array_push($lat, floatval($arr[1]));
                array_push($lon, floatval($arr[2]));
}}
}

$cen=[28.644800,77.216721];
if (count($dev)>0){
$cen=[array_sum($lat)/count($lat), array_sum($lon)/count($lon)];
}
fclose($myfile);
?>
      var map;
      function initMap() {


        map = new google.maps.Map(document.getElementById('map'), {
         center: {lat: <?php echo $cen[0];?>, lng: <?php echo $cen[1];?>},
         zoom: 4
        });
<?php
for ($i=0;$i<count($dev);$i++){
?>
        var marker<?php echo $i;?> = new google.maps.Marker({
          position: {lat: <?php echo $lat[$i];?>, lng: <?php echo $lon[$i];?>},
          map: map,
          title: '<?php echo $dev[$i];?>'
        });

     
<?php }
?>}
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC7e_AqHeO5KGK1HFWpXjupGTtcgL5o45A&callback=initMap"
    async defer></script>
  </body>
</html>
