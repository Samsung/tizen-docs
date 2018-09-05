# Watch

(M) : for mobile profile, (W) : for wearable profile, (T) : for TV profile
<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/wambientwatch.png" width="180"/></td>
			<td>
			<p><strong>(W) AmbientWatch</strong> [In progress]</p>
			<p>This sample application demonstrates how to create a watch application that supports ambient mode in Tizen wearable device. It also demonstrates how to create a circular watch face using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.<br>
			To extend battery life, a watch application can display a limited UI in the ambient mode by detecting ambient mode changes.<br>
			</p>
			<p>In <strong>tizen-manifest.xml</strong> file, set <code>ambient-support</code> attribute to true:<br>
			For more information, see ambient-support attribute.
			<br>
			<code>
			&lt;watch-application appid&equals;&quot;org.tizen.example.AmbientWatch&quot;  exec&equals;&quot;AmbientWatch.dll&quot; type&equals;&quot;dotnet&quot;  ambient-support&equals;&quot;true&quot;&gt;</code>
			</p>
			<p>
			You can get details about <a href="../../../tizen-studio/native-tools/manifest-text-editor.md" target="_blank">ambient-support attribute</a>.
			</p>
			<p>
			To use the ambient mode, you must enable it in the application settings. Launch <strong>Settings</strong> > <strong>Watch faces and styles</strong> > <strong>Watch always on</strong> > enable it. After screen timeout, the wearable device turns into ambient mode. In addition, the ambient mode activates only if you are wearing the watch on your wrist.</p>
			<p>In addition, there are similar native and web sample applications.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/Watch/Ambient_Analog_Watch" target="_blank">Native version</a></li>
				<li><a href="https://developer.tizen.org/development/sample/web/Watch/Ambient_Watch" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wclassicwatch.png" width="180"/></td>
			<td>
			<p><strong>(W) ClassWatch</strong> [In progress]</p>
			<p>This sample application demonstrates how to create a circular watch face, which consists of moving hands. It also demonstrates how to use watch face API using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.</p>
			<p>In addition, there are similar native and web sample applications.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/Watch/Classic_Watch" target="_blank">Native version</a></li>
				<li><a href="https://developer.tizen.org/development/sample/web/Watch/Classic_Watch" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wchronograph.png" width="180"/></td>
			<td>
			<p><strong>(W) ChronographWatch</strong> [In progress]</p>
			<p>This sample application demonstrates how to create a circular watch with continuously moving hands. It also demonstrates how to use watch face API using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.<br>
            This sample application includes the watch and stopwatch functionality.</p>
			<p>In addition, there are similar native and web sample applications.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/Watch/Chronograph_Watch" target="_blank">Native version</a></li>
				<li><a href="https://developer.tizen.org/development/sample/web/Watch/Chronograph_Watch" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wweatherwatch.png" width="180"/></td>
			<td>
			<p><strong>(W) WeatherWatch</strong> [In progress]</p>
			<p>This sample application demonstrates how to create a watch face application with weather information for Tizen wearable devices. It also demonstrates how to use watch face API using <a href="https://github.com/Samsung/Tizen.CircularUI/" target="_blank">Tizen.Wearable.CircularUI C# API</a>.<br>
			You can get detailed information from <a href="https://github.com/Samsung/Tizen-CSharp-Samples/blob/master/Wearable/WeatherWatch/README.md" target="_blank"><strong>readme file</strong> of WeatherWatch</a>.</p>
			<p>In addition, there are similar native and web sample applications.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/Watch/Weather_Watch" target="_blank">Native version</a></li>
				<li><a href="https://developer.tizen.org/development/sample/web/Watch/Weather_Watch" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>		
	</tbody>
</table>