# Watch

<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/wambientwatch.png" width="180"/></td>
			<td>
			<p><strong>(W) AmbientWatch</strong> [In progress]</p>
			<p>The AmbientWatch application demonstrates how to make a watch application that supports ambient mode in Tizen wearable device.
			To extend battery life, a watch application can display a limited UI in ambient mode by detecting ambient mode changes.<br>
			</p>
			<p>First of all, <i>"ambient-support"</i> attribute should be set to true in <b>tizen-manifest.xml</b> file as follows:<br>
			<code>
			&lt;watch-application appid&equals;&quot;org.tizen.example.AmbientWatch&quot;  exec&equals;&quot;AmbientWatch.dll&quot; type&equals;&quot;dotnet&quot;  ambient-support&equals;&quot;true&quot;&gt;</code>
			</p>
			<p>
			You can get details about <a href="https://developer.tizen.org/development/tizen-studio/native-tools/configuring-your-app/manifest-text-editor" target="_blank">ambient-support attribute</a>.
			</p>
			<p>
			To use the ambient mode, you must enable it in Settings application. Launch "Settings" App -> Select "Watch faces and styles" -> Choose "Watch always on" -> Enable it. After screen timeout, a wearable device turns into ambient mode. In addition, the ambient mode activates only when you are wearing a watch on your wrist.</p>
			<p><a href="https://developer.tizen.org/development/sample/native/Watch/Ambient_Analog_Watch?langswitch=en" target="_blank">Native version</a></p>
			<p><a href="https://developer.tizen.org/development/sample/web/Watch/Ambient_Watch?langswitch=en" target="_blank">Web version</a></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wclassicwatch.png" width="180"/></td>
			<td>
			<p><strong>(W) ClassWatch</strong> [In progress]</p>
			<p>The Classic Watch sample application demonstrates how to create a circular watch face, which consists of moving hands.</p>
			<p><a href="https://developer.tizen.org/development/sample/native/Watch/Classic_Watch" target="_blank">Native version</a></p>
			<p><a href="https://developer.tizen.org/development/sample/web/Watch/Classic_Watch" target="_blank">Web version</a></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wchronograph.png" width="180"/></td>
			<td>
			<p><strong>(W) ChronographWatch</strong> [In progress]</p>
			<p>The Chronograph Watch sample application demonstrates how to create a circular watch with continuously moving hands.
            This sample application includes the watch and stopwatch functionality.</p>
			<p><a href="https://developer.tizen.org/development/sample/native/Watch/Chronograph_Watch" target="_blank">Native version</a></p>
			<p><a href="https://developer.tizen.org/development/sample/web/Watch/Chronograph_Watch" target="_blank">Web version</a></p>
			</td>
		</tr>
	</tbody>
</table>