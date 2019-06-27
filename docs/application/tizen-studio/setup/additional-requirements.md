# Additional Requirements

This page provides an overview of various post installation requirements required to configure your development environment for optimal development experience. Assuming that you have successfully installed Tizen Studio on your development hardware, perform the configurations to have seamless experience of emulator, Web inspector etc. 

## Emulator Requirements 
To use the Emulator, ensure the following:

**Table: Emulator requirements**

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirements</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td colspan="3">Support for Intel VTx (Virtualization Technology)</td>
</tr>
<tr>
<td>Screen resolution</td>
<td colspan="3"> 1280 x 1024</td>
</tr>
<tr>
<td>Graphics card</td>
<td colspan="3"> The following Graphic cards have passed tests with the emulator.</p>
<p class="Table"><strong>Table: Supported Graphic cards</strong></p>
<table>
<thead>
<tr>
<th>Brand</th>
<th>Product</th>
</tr>
</thead>
<tbody>
<tr>
<td>NVIDIA</td>
<td>NVIDIA&reg; GT 330M, GeForce&reg; GTX 550Ti, NVIDIA&reg; Quadro&reg; NVS 290 and higher</td>
</tr>
<tr>
<td>ATI</td>
<td>RADEON HD 5450 and higher</td>
</tr>
<tr>
<td>Intel</td>
<td> HD Graphics 4000 and higher</td>
</tr>
</tbody>
</table>
<strong>Note:</strong>
<ul>
<li>If the host machine uses the NVIDIA&reg; Optimus&reg; technology, the emulator works with the on-board graphics card. 
<li>To prevent this, either disable the Optimus&reg; technology, or set the emulator to run with the external NVIDIA graphics card.</li>
<li>Integrated graphic cards inside Intel's Q33/Q35/Q43/Q45 motherboards are not supported.</li>
</ul>
</p>
</td>
</tr>
<tr>
<td rowspan="2"><B>Drivers</B></td>
<td colspan="3">You must upgrade to the latest vendor-provided version of the graphics card driver for OpenGL&reg; ES acceleration.</td>
</tr>
<tr>
<td>For Windows, check and install the necessary drivers.<br>
 Open <strong>Control Panel &gt; System and Security &gt; Windows Update</strong>.</td>
<td>     -</td>
<td>To upgrade Ubuntu driver, see the official <a href="https://help.ubuntu.com/community/BinaryDriverHowto/" target="_blank">Ubuntu Web site</a>.<br> Check and install the necessary drivers.<br> Open <strong>System Settings &gt; Software &amp; Updates &gt; Additional Drivers</strong>.</p>
</td>
</tr>
<tr>
<td rowspan="2"><B>Webcam<B></td>
<td colspan="3"><li>To use the emulator with inbuilt webcam, the webcam must support the USB Video Class (UVC) driver.</li> <h4>Supported Image Format</h4></td>
</tr>
<tr>
<td>YUYV or MJPEG</td>
<td>RGB24 or YUY2</td>
<td>UYYY, YYU420, YUY420, or YUYY</td>
</tr>
</tbody>
</table>

## Browser Requirements

### Google Chrome&trade; 

You can Use the Web Inspector tool in Google Chrome browser for debugging your applications. For more information, see [Web Inspector](../web-tools/web-inspector.md) page. The Web Inspector server uses the Web core of the platform.
You must use Google Chrome&trade; browser version 52 or lower, such that all the functions of the Web Inspector work properly. For more information see [Google Chrome&trade;](http://www.slimjet.com/chrome/google-chrome-old-version.php).

### T-Trace Requirements

The following table lists various other requirements that you must ensure before you start developing Tizen applications:

**Table: T-Trace requirements for Microsoft Windows&reg;**

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Install Python to enable the T-trace tool. The T-Trace tools is the Tizen profiling tool used to optimize the application performance.
</td>
<td>To use the T-trace in Windows&reg; 8 and higher, you must install Python 2.7.X or higher version.
<ul>
<li>Visit the official <a href="https://www.python.org/downloads/">Python Website</a>, download the appropriate Python version for your hardware and Windows&reg; version.
</li>
<li>Run the downloaded installer file and follow the on-screen instructions.</li>
</ul>
<strong>Note:</strong> <br>
To use Python in native command prompt, set the <code>%PATH%</code> environment variable in <strong>My Computer > Properties > Advanced > Environment Variables</strong>.
</td>
</tr>
</tbody>
</table>
