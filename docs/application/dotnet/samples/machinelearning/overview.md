---
keyword: Tizen, Mobile, Wearable, TV, Sample, Application, Machine Learning
---

# Machine Learning

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
			<td><img alt="" height="267" src="media/m62textclassification.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/Xamarin.Forms/MachineLearning/TextClassification" target="_blank"><strong>(M) TextClassification</strong></a></p>
			<p>This sample application demonstrates how to use the NNStreamer single-shot API using <a href="/application/dotnet/api/TizenFX/latest/api/Tizen.MachineLearning.Inference.SingleShot.html" target="_blank">Tizen.MachineLearning.Inference.SingleShot</a>.</p>
			<p>Based on the given sentences, the text is classified into predefined groups. These predefined groups serve as an input to the pre-trained models to predict whether a paragraph is positive or negative.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="tabcontent" id="Wearable">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/w83orientationdetection.png" width="180"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/Xamarin.Forms/MachineLearning/OrientationDetection" target="_blank"><strong>(W) OrientationDetection</strong></a></p>
			<p>This sample application demonstrates how to use machine learning and sensor data using <a href="/application/dotnet/api/TizenFX/latest/api/Tizen.MachineLearning.Inference.Pipeline.html" target="_blank">Tizen.MachineLearning.Inference.Pipeline</a>.</p>
			<p>It passes accelerometer sensor data stream to a neural network (tensorflow-lite model) and predicts one of four orientations of the device: <br>
			<ul start="1">
				<li>12 o'clock is upward.</li>
				<li>3 o'clock is upward.</li>
				<li>6 o'clock is upward.</li>
				<li>9 o'clock is upward.</li>
			</ul></p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="tabcontent" id="TV">
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
