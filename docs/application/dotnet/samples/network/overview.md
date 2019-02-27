# Network

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
			<td><img alt="" height="267" src="media/m16lescanner.jpg" width="150"/></td>
			<td>
			<p><strong>(M) Lescanner</strong> [In progress]</p>
			<p>This sample application demonstrates how to scan the Bluetooth Low Energy (BLE) devices.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m17networkapp.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/NetworkApp" target="_blank"><strong>(M) NetworkApp</strong></a></p>
			<p>This sample application demonstrates how to use <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.html" target="_blank">Tizen.Network.Conncetion C# API</a>, Wi-Fi, and Wi-Fi Direct.<br />
			This application provides network information such as IP address, network state, and list of available networks. Using this information, you can connect to Wi-Fi.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m35nfc.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/NFCSampleApp" target="_blank"><strong>(M) NFC</strong></a></p>
			<p>This sample application demonstrates how to work with Near Field Communication (NFC) API to send information to the nfc p2p device. It also demonstrates how to read and write the nfc tags.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m45servicediscovery.png" width="150"/></td>
			<td>
			<p><strong>(M) ServiceDiscovery</strong> [In progress]</p>
			<p>This sample application demonstrates how to register and discover a Domain Name System - Service Discovery (DNS-SD) service within the local network.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m33smartcard.png" width="150"/></td>
			<td>
			<p><strong>(M) Smartcard</strong> [In progress]</p>
			<p>This sample application demonstrates how to send command to Secure Element (SE) using the Smartcard API.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="tabcontent" id="Wearable">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/wlescanner.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/Lescanner" target="_blank"><strong>(W) Lescanner</strong></a></p>
			<p>This sample application demonstrates how to use <a href="https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.html" target="_blank">Tizen.Network.Bluetooth C# API</a> to connect with Bluetooth Low Energy devices. It also demonstrates how to create circular UI using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wnetworkapp.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/NetworkApp" target="_blank"><strong>(W) NetworkApp</strong></a></p>
			<p>This sample application demonstrates how to verify information about your connection and manage your Wi-Fi settings. It also demonstrates how to create circular UI using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wnfc.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/NFCSampleApp" target="_blank"><strong>(W) NFCSampleApp</strong></a></p>
			<p>This sample application demonstrates how to send and receive a NDEF message from remote Near Field Communication (NFC) device, and read NFC Data Exchange Format (NDEF) message from NFC Tag. It also demonstrates how to create circular UI using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div id="TV" class="tabcontent">
<table>
	<tbody>
		<tr>
			<td>There is no sample.</td>
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
