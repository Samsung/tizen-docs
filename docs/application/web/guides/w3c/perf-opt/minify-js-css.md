# JavaScript and CSS Minification

File minification improves application performance as unnecessary data is being removed. For example, page loading time can be decreased by reducing the number of JavaScript and CSS files.

Minifying tools, such as [Closure Compiler](https://developers.google.com/closure/compiler/) and [Grunt](http://gruntjs.com/), include features that can combine and reduce JavaScript file. The following table shows Closure Compiler and Grunt features in comparison.

**Table: Comparison of minifying tools**

<table>
	<tbody>
		<tr>
			<th>Item</th>
			<th>Closure Compiler</th>
			<th>Grunt</th>
		</tr>
		<tr>
			<td>Summary</td>
			<td>JavaScript-optimized compiler created by Google</td>
			<td>Task-based automatic JavaScript build tool</td>
		</tr>
		<tr>
			<td>Features</td>
			<td><ul>
				<li>File compilation, minimizing size</li>
				<li>Can be integrated with Ant Builder for automatic features</li>
			</ul></td>
			<td><ul>
					<li>File compilation plug-in</li>
					<li>Minimizing JavaScript and CSS</li>
					<li>Various plug-ins (JavaScript, CSS compilation, and compression)</li>
					<li>Application performance improvement based on the decrease of request count, transferred data, and transfer time</li>
			</ul></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><ul>
				<li>Java applications<p>Provided as a <code>.jar</code> file, used as a command line.</p></li>
				<li><a href="http://closure-compiler.appspot.com/home" target="_blank">Web application</a></li>
				<li>RESTful API</li>
			</ul></td>
			<td><ul>
				<li><code>Node.js</code> installation</li>
				<li><code>grunt-cli</code> installation</li>
				<li><code>package.json</code> must be inserted to the project root</li>
				<li>Task definition in the <code>gruntfile.js</code> file</li>
			</ul></td>
		</tr>
	</tbody>
</table>

Grunt has advantages in terms of expandability by providing various plug-ins. For more information on Grunt, see:

- [Installing and using Grunt](#installing-and-using-grunt)
- [Improvement through Grunt](#improvement-through-grunt)

## Installing and Using Grunt

The Grunt tool provides application performance improvement based on the decrease of request count, transferred data, and transfer time.

### Prerequisites

The commands used for installing and using Grunt work in the same manner, without any changes, across most of the major operating systems. To run the commands, you may need to use sudo (for Linux and BSD), or run your command shell as Administrator (for Windows&reg;).

### Installing Grunt

1. Install the [Node.js](http://www.nodejs.org/) platform. The platform includes the Node.js package manager, npm, which is used to install Grunt CLI (command line interface).

2. Install Grunt CLI:

   ```
   npm install -g grunt-cli /* -g: global type */
   ```

### Using Grunt

1. Change to the root directory of the project:

   ```
   cd <Project root>
   ```

2. Install Grunt and create the `Gruntfile.js` file:

   ```
   npm install grunt --save-dev
   ```

3. Create the `package.json` file: 

   When executing the following command, interactive prompt that receives information on the project is executed. Through the information entered, the `package.json` file is created.
   
   ```
   npm init
   ```

4. Install Grunt plug-in:

   ```
   /* Install grunt concat */
   npm install grunt-contrib-concat --save-dev

   /* Install grunt contrib uglify */
   npm install grunt-contrib-uglify --save-dev

   /* Install grunt contrib cssmin */
   npm install grunt-contrib-cssmin --save-dev
   ```

5. Run the Grunt plug-in:

   ```
   grunt
   ```

   Using the `Gruntfile.js` file, tasks, such as `concat`, `uglify`, and `cssmin`, are registered.

## Improvement through Grunt

After running the Grunt plug-in, the following comparison result is shown through the inspector in the Google Chrome&trade; browser. The expected results vary depending on the application, but since the improvement effects are certain, it is recommended to use Grunt.

> **Note**  
> For the sake of comparing improvement, in the following examples, 2 Web applications have been arbitrarily chosen and named App#1 and App#2.

**Table: Result for App #01**

<table border="1">
	<tbody>
		<tr>
			<th colspan="2" rowspan="2">Item</th>
			<th colspan="2">Request (count)</th>
			<th colspan="2">Transferred data (mb)</th>
			<th colspan="2">Onload time (s)</th>
		</tr>
		<tr>
			<th>Result</th>
			<th>Improvement</th>
			<th>Result</th>
			<th>Improvement</th>
			<th>Result</th>
			<th>Improvement</th>
		</tr>
		<tr>
			<td colspan="2" align="center">Original</td>
			<td>254</td>
			<td>-</td>
			<td>6.66</td>
			<td>-</td>
			<td>3.28</td>
			<td>-</td>
		</tr>
		<tr>
			<td rowspan="3" align="center">Minification applied (accumulated result)</td>
			<td><code>#01_grunt_concat</code></td>
			<td><strong>68</strong></td>
			<td><strong>-186</strong></td>
			<td>6.62</td>
			<td>-0.04</td>
			<td><strong>2.43</strong></td>
			<td><strong>-0.85</strong></td>
		</tr>
		<tr>
			<td><code>#02_grunt_uglify</code></td>
			<td><strong>68</strong></td>
			<td>-</td>
			<td><strong>1.90</strong></td>
			<td><strong>-4.72</strong></td>
			<td><strong>1.59</strong></td>
			<td><strong>-0.85</strong></td>
		</tr>
		<tr>
			<td><code>#03_grunt_cssmin</code></td>
			<td><strong>68</strong></td>
			<td>-</td>
			<td><strong>1.87</strong></td>
			<td><strong>-0.03</strong></td>
			<td><strong>1.61</strong></td>
			<td><strong>0.02</strong></td>
		</tr>
		<tr>
			<td colspan="2" align="center">Total improvement</td>
			<td colspan="2" align="center">73.23% improvement</td>
			<td colspan="2" align="center">71.92% improvement</td>
			<td colspan="2" align="center">51.07% improvement</td>
		</tr>
	</tbody>
</table>





**Table: Result for App #02**

<table border="1">
	<tbody>
		<tr>
			<th colspan="2" rowspan="2">Item</th>
			<th colspan="2">Request (count)</th>
			<th colspan="2">Transferred data (mb)</th>
			<th colspan="2">Onload time (s)</th>
		</tr>
		<tr>
			<th>Result</th>
			<th>Improvement</th>
			<th>Result</th>
			<th>Improvement</th>
			<th>Result</th>
			<th>Improvement</th>
		</tr>
		<tr>
			<td colspan="2" align="center">Original</td>
			<td>235</td>
			<td>-</td>
			<td>7.89</td>
			<td>-</td>
			<td>5.80</td>
			<td>-</td>
		</tr>
		<tr>
			<td rowspan="3" align="center">Minification applied (accumulated result)</td>
			<td><code>#01_grunt_concat</code></td>
			<td><strong>106</strong></td>
			<td><strong>-129</strong></td>
			<td>7.87</td>
			<td>-0.02</td>
			<td><strong>5.15</strong></td>
			<td><strong>-0.65</strong></td>
		</tr>
		<tr>
			<td><code>#02_grunt_uglify</code></td>
			<td><strong>106</strong></td>
			<td>-</td>
			<td><strong>5.85 </strong></td>
			<td><strong>-2.02</strong></td>
			<td><strong>4.95</strong></td>
			<td><strong>-0.19</strong></td>
		</tr>
		<tr>
			<td><code>#03_grunt_cssmin</code></td>
			<td><strong>106</strong></td>
			<td>-</td>
			<td><strong>5.84</strong></td>
			<td><strong>-0.01</strong></td>
			<td><strong>4.89</strong></td>
			<td><strong>-0.06</strong></td>
		</tr>
		<tr>
			<td colspan="2" align="center">Total improvement</td>
			<td colspan="2" align="center">54.89% improvement</td>
			<td colspan="2" align="center">25.98% improvement</td>
			<td colspan="2" align="center">15.63% improvement</td>
		</tr>
	</tbody>
</table>


## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
