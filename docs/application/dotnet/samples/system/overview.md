# System

<!--
For MD:
-->

<link href="../css/dotnet-samples.css" ref="stylesheet">

<!--
for TD:

<style type="text/css">
    Please copy dotnet-samples.css and paste it here
</script>
-->

<div class="sampletab">
<button class="tablinks" onclick="openProfile(event, 'Mobile')" id="defaultOpen">Mobile</button> <button class="tablinks" onclick="openProfile(event, 'Wearable')">Wearable</button> <button class="tablinks" onclick="openProfile(event, 'TV')">TV</button>
</div>

<!-- Tab content -->
<div class="tabcontent" id="Mobile">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="267" src="media/m53feedback.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/FeedbackApp" target="_blank"><strong>(M) FeedbackApp</strong></a></p>
			<p>This sample application demonstrates how to play feedback using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Feedback.html"  target="_blank">Tizen.System.Feedback C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m27heartratemonitor.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/HeartRateMonitor" target="_blank"><strong>(M) HeartRateMonitor</strong></a></p>
			<p>This sample application demonstrates how to obtain data provided by the Heart Rate Monitor (HRM) using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.Sensor.html" target="_blank">Tizen.Sensor C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m23sensor.png" width="150"/></td>
			<td>
			<p><strong>(M) Sensor</strong> [In progress]</p>
			<p>This sample application demonstrates how to manage sensors and receive sensor data from the sensor device.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m4systeminfo.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/System-info" target="_blank"><strong>(M) System-info</strong></a></p>
			<p>This sample application demonstrates how to get information about the system properties and capabilities of the device.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m46systeminfo.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/SystemInfo" target="_blank"><strong>(M) SystemInfo</strong></a></p>
			<p>This sample application demonstrates how to obtain the data provided by the system using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html" target="_blank">Tizen.System C# API</a>.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="tabcontent" id="Wearable">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/wcompass.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/Compass" target="_blank"><strong>(W) Compass</strong></a></p>
			<p>This sample application demonstrates how to retrieve information about the physical orientation of the device using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.Sensor.OrientationSensor.html"  target="_blank"> Tizen Orientation Sensor API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wfeedbackapp.png" width="180"/></td>
			<td>
			<p><strong>(W) FeedbackApp</strong> [In progress]</p>
			<p>This sample application demonstrates how to play sound and vibration feedback and how to create circular UI using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wheartratemonitor.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/HeartRateMonitor" target="_blank"><strong>(W) HeartRateMonitor</strong></a></p>
			<p>This sample application demonstrates how to obtain data provided by the Heart Rate Monitor (HRM) sensor using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.Sensor.html" target="_blank">Tizen.Sensor C# API</a> and how to create circular UI using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/metaldetector.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/MetalDetector" target="_blank"><strong>(W) MetalDetector</strong></a></p>
			<p>This sample application demonstrates how to obtain the magnetometer sensor data using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.Sensor.html" target="_blank">Tizen.Sensor C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wsystemInfo.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/SystemInfo" target="_blank"><strong>(W) SystemInfo</strong></a></p>
			<p>This sample application demonstrates how to obtain data provided by the system using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html" target="_blank">Tizen.System C# API</a> and how to use CirclePage of <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wsystem_info.png" width="180"/></td>
			<td>
			<p><strong>(W) SystemInfo2</strong> [In progress]</p>
			<p>This sample application demonstrates how to obtain data provided by the system using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html" target="_blank">Tizen.System C# API</a> and how to use IndexPage of <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="tabcontent" id="TV">
<table>
	<tbody>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv20systeminfo.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/SystemInfo" target="_blank"><strong>(T) SystemInfo</strong></a></p>
			<p>This sample application demonstrates how to obtain data provided by the system using <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html" target="_blank">Tizen.System C# API</a>.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<!--
For MD:
-->
<script src="../js/dotnet-samples.js"></script>

<!--
for TD:

<script>
  Please copy dotnet-samples.js and paste it here
</script>
-->

