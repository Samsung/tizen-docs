# Additional Requirements

This page explains the summary of various requirements that are necessary to configure your development environment for optimal and seamless development experience. 

Tizen studio tools such as Emulator, Web Inspector, and various other tools need to be configured specifically on your development hardware, such that the dependent development processes work efficiently. 

The following sections provides a quick overview of the additional requirements for various tools to run seamlessly:

## Tizen Studio Emulator 

Tizen Studio emulator simulates Tizen based devices on your computer so that you can test your Tizen applications without having the requirement of each physical device. Tizen Studio emulator provides almost all of the capabilities of a real Tizen based device.

To use Tizen Studio emulator, ensure that your development hardware meets the following configurations:

<table>
<thead>
<tr style="height: 18px;">
<th style="width: 205.783px; height: 18px;"><strong>Component</strong></th>
<th style="width: 505.217px; height: 18px;"><strong>Requirements&nbsp;</strong></th>
</tr>
</thead>
<tbody>
<tr style="height: 18px;">
<td style="width: 205.783px; height: 18px;"><strong>CPU</strong></td>
<td style="width: 505.217px; height: 18px;">Support for Intel Virtualization Technology (VTx)</td>
</tr>
<tr style="height: 18px;">
<td style="width: 205.783px; height: 18px;"><strong>Screen Resolution</strong></td>
<td style="width: 505.217px; height: 18px;">1280 x 1024</td>
</tr>
<tr style="height: 165px;">
<td style="width: 205.783px; height: 165px;">
<p><strong>NVIDIA&reg; Graphics Card</strong></p>
<p>&nbsp;</p>
</td>
<td style="width: 505.217px; height: 165px;">
<p>If the host machine uses the NVIDIA&reg; Optimus&reg; technology, the emulator works with the onboard graphics card. To prevent this, either disable the Optimus&reg; technology or set the emulator to run with the external NVIDIA graphics card.</p>
<p><b>Note</b></p> You must upgrade to the latest vendor-provided version of the graphics card driver for OpenGL&reg; ES acceleration.</p>
</td>
</tr>
<tr style="height: 92.6px;">
<td style="width: 205.783px; height: 188.6px;" rowspan="2"><strong>System Drivers</strong>&nbsp;</td>
<td style="width: 505.217px; height: 92.6px;">
<p>Windows&reg;:</p>
<p>To check and install the latest drivers, open&nbsp;<strong>Control Panel &gt; System and Security &gt; Windows Update</strong>.</p>
</td>
</tr>
<tr style="height: 96px;">
<td style="width: 505.217px; height: 96px;">
<p>Ubuntu&reg;:&nbsp;</p>
<p>To check and install the latest Ubuntu&nbsp;drivers, open&nbsp;<strong>System Settings &gt; Software &amp; Updates &gt; Additional Drivers</strong>.</p>
</td>
</tr>
<tr style="height: 114px;">
<td style="width: 205.783px; height: 114px;"><strong>Webcam</strong></td>
<td style="width: 505.217px; height: 114px;">
<p>Use the emulator with an inbuilt webcam. The webcam must support the USB Video Class (UVC) driver.</p>
<p>The&nbsp;supported image formats are: &nbsp;<strong>UYYY, YYU420, YUY420,</strong> and <strong>YUYY.</strong></p>
</td>
</tr>
</tbody>
</table>

## Google Chrome&reg; Browser 

You can use the Web Inspector tool in the Google Chrome browser for debugging your applications. For more information, see [Web Inspector](../web-tools/web-inspector.md). The Web Inspector server uses the Web core of the platform.

> [!NOTE]
> You must use Google Chrome&trade; browser version 52 or lower, such that all the functions of the Web Inspector work properly. For more information, see [Google Chrome&trade;](http://www.slimjet.com/chrome/google-chrome-old-version.php).

## T-Trace 

The T-Trace tool is a Tizen profiling tool that is used to optimize the performance of an application.

The following table lists the requirements that you must ensure to use the T-Trace tool:

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<b>T-Trace</b> 
</td>
<td>To use T-trace in Windows&reg; 8 and higher, you must install Python 2.7.X or higher.
<br> <br>
To download and install Python, follow these steps: <br>
<br>
<ol>
<li> Download an appropriate Python version for your hardware and Windows&reg;. For more information, see the  <a href="https://www.python.org/downloads/">Python website.</a>
</li>

<li>Run the downloaded installer file and follow the on-screen instructions.</li>
</ol>

<br><strong>Note</strong>

To use Python in native command prompt, set the <code>%PATH%</code> environment variable in <strong>My Computer > Properties > Advanced > Environment Variables</strong>.
</td>
</tr>
</tbody>
</table>
