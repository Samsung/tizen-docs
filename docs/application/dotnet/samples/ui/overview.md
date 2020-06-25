# UI

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
			<td><img alt="" height="267" src="media/m10applicationstoreui.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/ApplicationStoreUI" target="_blank"><strong>(M) Application Store UI</strong></a></p>
			<p>This sample application demonstrates how to create a complex view.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m38basiccalculator.png" width="150"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/BasicCalculator" target="_blank"><strong>(M) BasicCalculator</strong></a></p>
			<p>This sample application demonstrates how to create a calculator with basic mathematical operations using the Xamarin.Forms library.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m11calculator.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/Calculator" target="_blank"><strong>(M) Calculator</strong></a></p>
			<p>This sample application demonstrates the regular calculator and the scientific calculator.<br />
			This sample follows the Portable Class Libraries (PCL) application model. It uses some of the Xamarin.Forms features such as XAML files for GUI, custom renderers for the image buttons, and subsystem ports using the dependency service.</p>
			<p>In addition, there is similar web sample application.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/web/General/Calculator" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m12clock.png" width="150"/></td>
			<td>
			<p><strong>(M) Clock</strong> [In progress]</p>
			<p>This sample application demonstrates how to use the clock.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m5emailui.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/EmailUI" target="_blank"><strong>(M) Email UI</strong></a></p>
			<p>This sample application demonstrates how to configure the screen using a variety of objects.<br />
			(This sample only demonstrates how to create your UI application only, not the functionality of your application.)</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m6galleryui.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/GalleryUI" target="_blank"><strong>(M) Gallery UI</strong></a></p>
			<p>This sample application demonstrates how to configure the screen using a variety of objects.<br />
			(This sample only demonstrates how to create your UI application only, not the functionality of your application.)</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m7puzzle.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/Puzzle" target="_blank"><strong>(M) Puzzle</strong></a></p>
			<p>This sample application demonstrates the basic UI sample application.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m9settingsui.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/Settings" target="_blank"><strong>(M) Settings UI</strong></a></p>
			<p>This sample application demonstrates how to configure the screen using a variety of objects.<br />
			(This sample only demonstrates how to create your UI application only, not the functionality of your application.)</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m8snsui.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/UI/SNSUI" target="_blank"><strong>(M) SNS UI</strong></a></p>
			<p>This sample application demonstrates how to configure the screen using a variety of objects.<br />
			It also shows how to compose the view using a scroller, a toolbar, and a drawer.<br />
			(This sample only demonstrates how to create your UI application only, not the functionality of your application.)</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<!-- Tab content -->
<div class="tabcontent" id="Wearable">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/wcalculator.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/Calculator" target="_blank"><strong>(W) Calculator</strong></a></p>
			<p>This sample application demonstrates the regular calculator. This is using some Xamarin.Forms features such as XAML files for GUI and Custom Renderers for the image buttons.</p>
			<p>In addition, there are similar native and web sample applications.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/UI/%28Circle%29_Calculator" target="_blank">Native version</a></li>
				<li><a href="https://developer.tizen.org/development/sample/web/General/Calculator_1" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="180" src="media/wimagereader.png" width="180"/></p>
			</td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/ImageReader" target="_blank"><strong>(W) ImageReader</strong></a></p>
			<p>This sample application demonstrates how to use an image in the Tizen .Net application.
			This application is based on the <a href="https://developer.xamarin.com/samples/xamarin-forms/WorkingWithImages/" target="_blank">Xamarin sample application</a> and is modified according to the Tizen Wearable UI using <a href="https://samsung.github.io/Tizen.CircularUI/api/index.html" target="_blank">Tizen.Wearable.CircularUI</a>.</p>
			<p>For more information, see <a href="https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/images" target="_blank">Xamarin.Forms.Images</a>.</p>
			<p><strong>Prerequisites</strong><br>
			Network connection is required for DownloadImage.</p>
			<p>To use network connection in an application,<br>
			you must have the following privileges:<br>
			<ul>
				<li><code>http://tizen.org/privilege/internet</code></li>
				<li><code>http://tizen.org/privilege/network.get</code></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wrotarytimer.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/RotaryTimer" target="_blank"><strong>(W) RotaryTimer</strong></a></p>
			<p>This sample application demonstrates how to use Rotary Bezel.</p>
			<p>In addition, there are similar native and web sample applications.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/UI/Rotary_Timer" target="_blank">Native version</a></li>
				<li><a href="https://developer.tizen.org/development/sample/web/General/Rotary_Timer" target="_blank">Web version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="180" src="media/wskiasharp2d.png" width="180"/></p>
			</td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/SkiaSharp2DSample" target="_blank"><strong>(W) SkiaSharp2DSample</strong></a></p>
			<p>This sample application demonstrates how to use <code>SkiaSharp</code> API in Tizen <code>Xamarin.Forms</code> applications.
			<ul>
				<li>Drawing Basics (DrawCircle)</li>
				<li>SkiaSharp Path (DrawPath)</li>
				<li>SkiaSharp Transforms (Translate, Scale, RotateDegrees)</li>
			</ul>
			This application uses <a href="https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp" target="_blank">SkiaSharp API</a>.
			<ul>
				<li><a href="https://docs.microsoft.com/en-us/dotnet/api/skiasharp.skcanvas" target="_blank">Class SKCanvas</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wxstopwatch.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/XStopWatch" target="_blank"><strong>(W) XStopWatch</strong></a></p>
			<p>This sample application demonstrates how to use a stopwatch and how to create circular UI using <a href="https://samsung.github.io/Tizen.CircularUI/api/index.html" target="_blank">Tizen.Wearable.CircularUI</a>.</p>
			<p>In addition, there is similar native sample application.<br>
			<ul>
				<li><a href="https://developer.tizen.org/development/sample/native/UI/%28Circle%29_Stopwatch" target="_blank">Native version</a></li>
			</ul></p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/wxuicomponent.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/XUIComponents" target="_blank"><strong>(W) XUIComponents</strong></a></p>
			<p>This sample application demonstrates how to use various kinds of Tizen Wearable UI controls using the Xamarin.Forms and <a href="https://samsung.github.io/Tizen.CircularUI/api/index.html" target="_blank">Tizen.Wearable.CircularUI</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w46_animationsample_nui.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/AnimationsSample" target="_blank"><strong>(W) AnimationSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to animate NUI objects using the NUI animation.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w47imagesample_nui.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/ImageSample" target="_blank"><strong>(W) ImageSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to load and control images.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w48scriptlayoutsample_nui.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/ScriptLayoutSample" target="_blank"><strong>(W) ScriptLayoutSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to set the theme of an application using script file.
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w49texteditorsample_nui3.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/TextEditorSample" target="_blank"><strong>(W) TextEditorSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to control the TextEditor properties.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w50textfieldsample_nui.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/TextFieldSample" target="_blank"><strong>(W) TextFieldSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to control the TextField properties.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w51textlabelsample_nui2.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/TextLabelSample" target="_blank"><strong>(W) TextLabelSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to control the TextLabel properties.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w52uicontrolsample_nui.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/UIControlSample" target="_blank"><strong>(W) UIControlSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to generate and control individual NUI UI control objects.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="180" src="media/w53visualssample_nui.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/VisualsSample" target="_blank"><strong>(W) VisualSample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use various kinds of visuals.</p>
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
			<p><img alt="" height="225" src="media/tv19basiccalculator.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/BasicCalculator" target="_blank"><strong>(T) BasicCalculator</strong></a></p>
			<p>This sample application demonstrates how to create a calculator with basic mathematical operations using the Xamarin.Forms library.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv1musicplayerui.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/MusicPlayerUI" target="_blank"><strong>(T) Music Player UI</strong></a></p>
			<p>This sample application demonstrates how to use ListViews and a TabbedPage to create intuitive and complex layouts on a TV.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv13stopwatch.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/Stopwatch" target="_blank"><strong>(T) Stopwatch</strong></a></p>
			<p>This sample application demonstrates how to create an application that measures the amount of time taken for a task. This application is created using the Xamarin.Forms.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv4animationsample.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/AnimationSample" target="_blank"><strong>(T) Animation Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use the animation class to create and cancel animations.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv22ChannelList.png" width="400" /></p>
			</td>
			<td>
            <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/ChannelList" target="_blank"><strong>(T) ChannelList (NUI)</strong></a></p>
			<p>This sample application demonstrates how to obtain and filter TV channel information.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv24firstscreen.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/FirstScreen" target="_blank"><strong>(T) FirstScreen (NUI)</strong></a></p>
            <p>This sample application demonstrates how to launch the apps on the TV.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv7flexcontainersample.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/FlexContainerSample" target="_blank"><strong>(T) FlexContainer Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use FlexContainer and shows results of  applied properties.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv6imagesample.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/ImageSample" target="_blank"><strong>(T) Image Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use image view and shows some properties of image view.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv8scriptlayoutsample.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/ScriptLayoutSample" target="_blank"><strong>(T) Script Layout Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use JSON files to create styles.<br />
            Application often contains multiple controls that have an identical appearance.<br />
			Setting the appearance of each individual control can be repetitive and error prone.<br />
			Therefore, you can create styles that customizes and controls appearance by grouping and setting properties available on the control type.
			</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv5textsample.png" width="400" /></p>
			</td>
			<td>
            <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/TextSample" target="_blank"><strong>(T) Text Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use the text controls and common text entry scenarios.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv3uicontrolsample.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/UIControlSample" target="_blank"><strong>(T) UIControl Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how NUI views work on TV.<br />
			You can navigate and interact NUI views.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv9visualsample.png" width="400" /></p>
			</td>
			<td>
            <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/VisualSample" target="_blank"><strong>(T) Visual Sample (NUI)</strong></a></p>
			<p>This sample application demonstrates how to use various kinds of visuals.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv28ball3d.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/Ball3D" target="_blank"><strong>(T) Ball3D (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to draw a spherical 3D model, add texture to the model, and realize rotation of the model.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv29cubetexture.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/CubeTexture" target="_blank"><strong>(T) CubeTexture (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to draw a 3D model (cube), realize rotation of the model, and add texture to the model.</p>
                        <p>It also demonstrates how the application implements two cubes independently drawn using two programs.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv36cubewithskiasharp.png" width="400" /></p>
			</td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/CubeWithSkiaSharp" target="_blank"><strong>(T) CubeWithSkiaSharp (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to draw a text with SkiaSharp on the target memory, to generates 2D texture on the target memory block, and to shows 2D texture in the OpenTK app (drawing text on a rotating cube).</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv30graffiti.png" width="400" /></p>
			</td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/Graffiti" target="_blank"><strong>(T) Graffiti (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to respond to click events or button events and how to draw a dot or line at the corresponding position on the screen.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv31panorama.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/Panorama360" target="_blank"><strong>(T) Panorama360 (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to achieve 360-degree panorama effect.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv32particledynamic.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/ParticleDynamic" target="_blank"><strong>(T) ParticleDynamic (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to implement a dynamic particle scenario.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv33scratchpaper.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/ScratchPaper" target="_blank"><strong>(T) ScratchPaper (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to respond to click events or button events and how to draw corresponding textures at the corresponding position on the screen.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv34star.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/Star" target="_blank"><strong>(T) Star (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to implement shaders loading, program creation, linking, vertex data loading, texture data loading, and other preliminary operations of drawing. It also demonstrates how to draw a multilateral graph (five-pointed star) with the DrawElements API.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p><img alt="" height="225" src="media/tv35triangle.png" width="400" /></p>
			</td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/TV/Triangle" target="_blank"><strong>(T) Triangle (OpenTK)</strong></a></p>
			<p>This sample application demonstrates how to implement shaders loading, program creation, linking, vertex data loading, texture data loading, and other preliminary operations of drawing. It also demonstrates how to implement a basic graph drawing (drawing triangles) with the DrawArrays API.</p>
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
