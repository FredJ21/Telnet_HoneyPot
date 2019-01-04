<!DOCTYPE html>
<html>
	<head>
		<title>Telnet HoneyPot - Statistics | By Fred J.</title>
		<meta name="description" content="Telnet HoneyPot - Statistics" />
		
		<!-- amCharts javascript sources -->
		<script type="text/javascript" src="https://www.amcharts.com/lib/3/amcharts.js"></script>
		<script type="text/javascript" src="https://www.amcharts.com/lib/3/serial.js"></script>
		<script type="text/javascript" src="https://www.amcharts.com/lib/3/pie.js"></script>
		<script type="text/javascript" src="https://www.amcharts.com/lib/3/themes/black.js"></script>
		
		<?php

			$CONF = parse_ini_file("/home/Telnet_HoneyPot/www/conf.ini");
			
			$username   = $CONF[LOGIN];
			$password   = $CONF[PASS];
			$dbname     = $CONF[DB];
			$servername = $CONF[SRV];
			$table	    = "telnet";

			$conn = new mysqli($servername, $username, $password, $dbname);
			if ($conn->connect_error) {       die("Connection failed: " . $conn-connect_error); }

			$sql = "SELECT count(*) FROM ".$table;
			$result = $conn->query($sql); $row = $result->fetch_array();
			$NB_TOTAL = $row[0];

			$sql = "SELECT count(*) FROM ". $table ." WHERE timeout=1";
			$result = $conn->query($sql); $row = $result->fetch_array();
			$NB_TIMEOUT = $row[0];

			$sql = "SELECT date FROM ". $table ." order by date asc limit 1";
			$result = $conn->query($sql); $row = $result->fetch_array();
			$DATE_FIRST = $row[0];

			$sql = "SELECT date FROM ". $table ." order by date desc limit 1";
			$result = $conn->query($sql); $row = $result->fetch_array();
			$DATE_LAST = $row[0];

			# connexion by HOUR
			$sql = "SELECT DATE_FORMAT(date,'%Y-%m-%d %H') as date2, count(*) from telnet group by date2 order by date2 desc limit 168";
			$result = $conn->query($sql); 
			$result_hour = array();
			while($row = $result->fetch_array()) {  	array_push($result_hour, $row);	}

			# connexion by DAY
			$sql = "SELECT DATE_FORMAT(date,'%Y-%m-%d') as date2, count(*) from telnet group by date2 order by date2 desc";
			$result = $conn->query($sql); 
			$result_day = array();
			while($row = $result->fetch_array()) {  	array_push($result_day, $row);	}

			# Login TOP10
			$sql = "select login, count(*) as nb from telnet where timeout=0 group by login order by nb desc limit 10";
			$result_login = $conn->query($sql); 

			# Password TOP10
			$sql = "select pass, count(*) as nb from telnet where timeout=0 and pass!='' group by pass order by nb desc limit 10";
			$result_pass = $conn->query($sql); 


		?>


		<!-- amCharts javascript code -->
		<script type="text/javascript">
			AmCharts.makeChart("chartdiv-1",
				{
					"type": "serial",
					"categoryField": "date",
					"dataDateFormat": "YYYY-MM-DD HH",
					"maxSelectedSeries": -1,
					"theme": "black",
					"categoryAxis": {
						"autoRotateAngle": 0,
						"minPeriod": "hh",
						"parseDates": true
					},
					"chartCursor": {
						"enabled": true,
						"categoryBalloonDateFormat": "D MMM JJ:NN",
						"tabIndex": 1
					},
					"trendLines": [],
					"graphs": [
						{
							"bullet": "round",
							"bulletSize": 5,
							"id": "AmGraph-1",
							"title": "",
							"valueField": "column-1"
						}
					],
					"guides": [],
					"valueAxes": [
						{
							"id": "ValueAxis-1",
							"title": ""
						}
					],
					"allLabels": [],
					"balloon": {},
					"titles": [
						{
							"id": "Title-1",
							"size": 15,
							"text": "Number of connections by HOUR (Last Week)"
						}
					],
					"dataProvider": [
		
					   <?php	
	
						for ($a=count($result_hour)-1; $a>=1; $a--) {		# the last value is not printed

							print '{ "date": "'. $result_hour[$a][0] .'","column-1": '. $result_hour[$a][1] .' },';
						}
					   ?>
					]
				}
			);

			AmCharts.makeChart("chartdiv-2",
				{
					"type": "serial",
					"categoryField": "date",
					"dataDateFormat": "YYYY-MM-DD",
					"maxSelectedSeries": -1,
					"theme": "black",
					"categoryAxis": {
						"autoRotateAngle": 0,
						"minPeriod": "hh",
						"parseDates": true
					},
					"chartCursor": {
						"enabled": true,
						"categoryBalloonDateFormat": "D MMM YYYY",
						"tabIndex": 1
					},
					"trendLines": [],
					"graphs": [
						{
							"bullet": "round",
							"bulletSize": 5,
							"id": "AmGraph-1",
							"title": "",
							"valueField": "column-1"
						}
					],
					"guides": [],
					"valueAxes": [
						{
							"id": "ValueAxis-1",
							"title": ""
						}
					],
					"allLabels": [],
					"balloon": {},
					"titles": [
						{
							"id": "Title-1",
							"size": 15,
							"text": "Number of connections by DAY (All data)"
						}
					],
					"dataProvider": [
		
					   <?php	
	
						for ($a=count($result_day)-1; $a>=1; $a--) {		# the last value is not printed

							print '{ "date": "'. $result_day[$a][0] .'","column-1": '. $result_day[$a][1] .' },';
						}
					   ?>
	
					]
				}
			);

			AmCharts.makeChart("chartdiv-3",
				{
					"type": "pie",
					"balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
					"titleField": "login",
					"valueField": "nb",
					"theme": "black",
					"borderAlpha": 0.80,
					"borderColor": "#FF0000",
					"fontSize": 13,
					"outlineAlpha": 0.50,
					"allLabels": [],
					"balloon": {},
					"legend": {
						"enabled": true,
						"fontSize": 10,
						"align": "center",
						"marginLeft": 0,
						"markerType": "circle",
						"verticalGap": 5
					},
					"titles": [
						{
							"id": "Title-1",
							"size": 14,
							"text": "Login - Top 10 (last mouth)"
						}
					],
					"dataProvider": [
						<?php						
							while($row = $result_login->fetch_array()) {

								print '{ "login": "'. $row[0] .'","nb": '. $row[1] .' },';
							}
						?>
					]
				}
			);

			AmCharts.makeChart("chartdiv-4",
				{
					"type": "pie",
					"balloonText": "[[title]]<br><span style='font-size:14px'><b>[[value]]</b> ([[percents]]%)</span>",
					"titleField": "login",
					"valueField": "nb",
					"theme": "black",
					"borderAlpha": 0.80,
					"borderColor": "#FF0000",
					"fontSize": 13,
					"outlineAlpha": 0.50,
					"allLabels": [],
					"balloon": {},
					"legend": {
						"enabled": true,
						"fontSize": 10,
						"align": "center",
						"marginLeft": 0,
						"markerType": "circle",
						"verticalGap": 5
					},
					"titles": [
						{
							"id": "Title-1",
							"size": 14,
							"text": "Password - Top 10 (last mouth)"
						}
					],
					"dataProvider": [
						

						<?php						
							while($row = $result_pass->fetch_array()) {

								print '{ "login": "'. $row[0] .'","nb": '. $row[1] .' },';
							}
						?>

					]
				}
			);


		</script>
	</head>
	<style type="text/css">
		span {
			color: #FF0000;
		}
	</style>

	<body  style="background-color: #444444;color: #aaaaaa"">

		<h1 style="text-align: center;">Telnet HoneyPot - Statistics</h1>
		<div style="display: flex; width: 90%; margin: auto;background-color: #222222">
			<div style="width: 48%;margin-left: 30px;padding: 10px">
				Number of connexion attempt : <span><?php echo $NB_TOTAL; ?></span> <br/>
				Number of connecion timeout : <span><?php echo $NB_TIMEOUT; ?></span> <br/>
			</div>
			<div style="width: 48%;;margin-left: 30px; padding: 10px">
				First data : <span><?php echo $DATE_FIRST; ?></span> <br/>
				Last data : <span><?php echo $DATE_LAST; ?></span> <br/>
			</div>
		</div>
		<div style="height: 5px"></div>
		<div id="chartdiv-1" style="width: 90%; height: 250px; background-color: #222222; margin: auto;" ></div>
		<div style="height: 3px"></div>
		<div id="chartdiv-2" style="width: 90%; height: 250px; background-color: #222222; margin: auto;" ></div>
		<div style="height: 5px"></div>
		<div style="display: flex; width: 90%; margin: auto;">
			<div id="chartdiv-3" style="width: 49%; height: 450px; background-color: #222222;margin: auto;" ></div>
  			<div id="chartdiv-4" style="width: 49%; height: 450px; background-color: #222222;margin: auto;" ></div>
		</div>

	</body>
</html>
