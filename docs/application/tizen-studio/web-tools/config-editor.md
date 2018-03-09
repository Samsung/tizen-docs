# Configuring Applications

The Tizen Web application configuration file is composed of XML elements, including the `<widget>` element as its root and other elements. These elements represent application information, such as [configuration elements](#elements) and Tizen extending configuration elements for [mobile](#mw_extend) and [wearable](#ww_extend) applications.

This configuration information is used when you install or run the Tizen Web application on the Tizen platform. The Tizen Web application project must have the `config.xml` file in the project root directory.

The configuration file can be easily edited with the [Web application configuration editor](#edit) (form editor), or you can modify the XML structure directly using the configuration source editor. With the form editor, you can set the project configuration (manifest), even if you have no experience with developing a Tizen Web application project. If you are fluent with the configuration file XML structure, you can create the configuration file directly through the configuration source editor.

> **Note**  
> The `config.xml` must conform to both the XML file format and the W3C specification requirements. Editing the file XML structure with the configuration source editor is intended for advanced users only.


<a name="edit"></a>
## Editing the config.xml File

There are 2 different ways to edit the `config.xml` file:

- Use the **Source** tab:

  1. Double-click the `config.xml` file in the **Project Explorer** view.

  2. Select the **Source** tab.

  **Figure: Source tab**

  ![Source tab](./media/config_text.png)

- Use the form tabs:

  1. Double-click the `config.xml` file in the **Project Explorer** view.

  2. Select one of the form tabs (**Overview**, **Features**, **Privileges**, **Localization**, **Policy**, **Preferences**, **Tizen**).

  **Figure: Form tabs**

  ![Form tabs](./media/config_form.png)


<a name="hierarchy"></a>
## Configuration Element Hierarchy

The Tizen Web application configuration file consists of XML elements organized in a hierarchy. The following tree structure shows the relationship between the elements of the `config.xml` file.

<table>
	<colgroup>
		<col width="5%" />
		<col width="5%" />
		<col width="5%" />
		<col width="85%" />
	</colgroup>
	<tbody>
		<tr>
			<td colspan="4"><code><a href="#widget">&lt;widget&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#access">&lt;access&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:icon&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:display-name&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:capability&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:account&gt;</code> (in <a href="#mw_account">mobile</a> or <a href="#ww_account">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:allow-navigation&gt;</code> (in <a href="#mw_navigation">mobile</a> or <a href="#ww_allownavigation">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:app-control&gt;</code> (in <a href="#mw_appcontrol">mobile</a> or <a href="#appcontrol">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:src&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:operation&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:uri&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:mime&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:privilege&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#ww_webwidget">&lt;tizen:app-widget&gt;</a></code> (in wearable only)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_widget-label">&lt;tizen:widget-label&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_widget-content">&lt;tizen:widget-content&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td><code><a href="#ww_widget-size">&lt;tizen:widget-size&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_widget-metadata">&lt;tizen:widget-metadata&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:appdefined-privilege&gt;</code> (in <a href="#mw_appdefined_privilege">mobile</a> or <a href="#ww_appdefined_privilege">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:application&gt;</code> (in <a href="#mw_application">mobile</a> or <a href="#ww_application">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#author">&lt;author&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#span">&lt;span&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:background-category&gt;</code> (in <a href="#mw_bg_category">mobile</a> or <a href="#ww_bg_category">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#ww_category">&lt;tizen:category&gt;</a></code> (in wearable only)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#content_element">&lt;content&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:content&gt;</code> (in <a href="#mw_webapp">mobile</a> or <a href="#ww_tizencontent">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:content-security-policy&gt;</code> (in <a href="#mw_sec">mobile</a> or <a href="#ww_contentsecpolicy">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:content-security-policy-report-only&gt;</code> (in <a href="#mw_secreport">mobile</a> or <a href="#ww_contentsecpolicyreport">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#description">&lt;description&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#span">&lt;span&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;feature&gt;</code> (in <a href="#mw_feature">mobile</a> or <a href="#ww_feature">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#param">&lt;param&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#icon">&lt;icon&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#ww_ime">&lt;tizen:ime&gt;</a></code> (in wearable only)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:uuid&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code>&lt;tizen:languages&gt;</code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td><code><a href="#ww_language">&lt;tizen:language&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#license">&lt;license&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#span">&lt;span&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:metadata&gt;</code> (in <a href="#mw_metadata">mobile</a> or <a href="#ww_metadata">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#name">&lt;name&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#span">&lt;span&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#preference">&lt;preference&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:privilege&gt;</code> (in <a href="#mw_privilege">mobile</a> or <a href="#ww_privilege">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:provides-appdefined-privilege&gt;</code> (in <a href="#mw_provides_appdefined_privilege">mobile</a> or <a href="#ww_provides_appdefined_privilege">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:profile&gt;</code> (in <a href="#mw_profile">mobile</a> or <a href="#ww_profile">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#ww_service">&lt;tizen:service&gt;</a></code> (in wearable only)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_service-name">&lt;tizen:name&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_service-icon">&lt;tizen:icon&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_service-content">&lt;tizen:content&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_service-description">&lt;tizen:description&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_service-metadata">&lt;tizen:metadata&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="2"><code><a href="#ww_service-category">&lt;tizen:category&gt;</a></code></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code>&lt;tizen:setting&gt;</code> (in <a href="#mw_setting">mobile</a> or <a href="#ww_setting">wearable</a>)</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td colspan="3"><code><a href="#mw_trust-anchor">&lt;tizen:trust-anchor&gt;</a></code> (in <a href="#mw_trust-anchor">mobile</a> or <a href="#ww_trust-anchor">wearable</a>)</td>
		</tr>
	</tbody>
</table>

<a name="elements"></a>
## Configuration Elements

The following tables summarize the W3C configuration elements used in the `config.xml` file of a Web application. For more information on the W3C element details, see [Widget Packaging and XML Configuration](https://www.w3.org/TR/2011/REC-widgets-20110927/) (the details of the Tizen extending configuration elements are described in [Extending Configuration Elements in Mobile Applications](#mw_extend) and [Extending Configuration Elements in Wearable Applications](#ww_extend)). For a quick view of the element hierarchy, see [Configuration Element Hierarchy](#hierarchy).

<table id="widget">
	<thead>
		<tr>
			<th>&lt;widget&gt; element</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Represents the root element of a configuration document.
			<p><strong>Expected children:</strong></p>
			<p><code>&lt;access&gt;</code>, <code>&lt;tizen:account&gt;</code>, <code>&lt;tizen:app-control&gt;</code>, <code>&lt;tizen:appdefined-privilege&gt;</code>, <code>&lt;tizen:application&gt;</code>, <code>&lt;author&gt;</code>, <code>&lt;content&gt;</code>, <code>&lt;tizen:content&gt;</code>, <code>&lt;description&gt;</code>, <code>&lt;feature&gt;</code>, <code>&lt;icon&gt;</code>, <code>&lt;license&gt;</code>, <code>&lt;name&gt;</code>, <code>&lt;preference&gt;</code>, <code>&lt;tizen:privilege&gt;</code>, <code>&lt;tizen:provides-appdefined-privilege&gt;</code>, <code>&lt;tizen:profile&gt;</code>, and <code>&lt;tizen:setting&gt;</code></p>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>id</code></li>
				<li><code>version</code>
				<p>Specific version of the Tizen package. The expected value is <code>[0-255].[0-255].[0-65535]</code>.</p>
				</li>
				<li><code>height</code></li>
				<li><code>width</code></li>
				<li><code>viewmodes</code></li>
				<li><code>defaultlocale</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="access">
	<thead>
		<tr>
			<th>&lt;access&gt; element</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Used to control network access from within a Web application and to request access to certain network resources from the user agent.
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>origin</code></li>
				<li><code>subdomains</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="author">
	<thead>
		<tr>
			<th>&lt;author&gt; element</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Represents the person who created the Web application.
			<p><strong>Expected children:</strong></p>
			<p>&lt;span&gt; and &lt;text node&gt;</p>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>href</code></li>
				<li><code>email</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="content_element">
	<thead>
		<tr>
			<th>&lt;content&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Represents the boot-strapping mechanism used to point to the main file of the Web application.
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>encoding</code></li>
				<li><code>src</code></li>
				<li><code>type</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="description">
	<thead>
		<tr>
			<th>&lt;description&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Represents text describing the purpose of the Web application.
			<p><strong>Expected children:</strong></p>
			<p>&lt;span&gt; and &lt;text node&gt;</p>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="icon">
	<thead>
		<tr>
			<th>&lt;icon&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Represents the Web application icon.
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>src</code></li>
				<li><code>width</code></li>
				<li><code>height</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="license">
	<thead>
		<tr>
			<th>&lt;license&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Represents the license under which the Web application is distributed.
			<p><strong>Expected children:</strong></p>
			<p>&lt;span&gt; and &lt;text node&gt;</p>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>href</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="name">
	<thead>
		<tr>
			<th>&lt;name&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Represents the Web application name used, for example, in the application menu.
			<p><strong>Expected children:</strong></p>
			<p>&lt;span&gt; and &lt;text node&gt;</p>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>short</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="param">
	<thead>
		<tr>
			<th>&lt;param&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to declare parameters to be used with a feature in <a href="#mw_feature">mobile</a> and <a href="#ww_feature">wearable</a> applications.
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
				<li><code>name</code></li>
				<li><code>value</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="preference">
	<thead>
		<tr>
			<th>&lt;preference&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to declare preferences as key-value pairs for the Web application for use at runtime.
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>The maximum length can be limited to 80 bytes. In that case, leftover bytes are ignored.</p>
				</li>
				<li><code>value</code>
				<p>The maximum length can be limited to 8192 bytes. In that case, leftover bytes are ignored.</p>
				</li>
				<li><code>readonly</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="span">
	<thead>
		<tr>
			<th>&lt;span&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Represents the generic container used mainly for internationalization.
			<p><strong>Expected children:</strong></p>
			<p>&lt;span&gt; and &lt;text node&gt;</p>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code></li>
				<li><code>dir</code></li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_extend"></a>
## Extending Configuration Elements in Mobile Applications

The following sections show additional configuration elements used in the `config.xml` file of a Web application, but not included in the [Widget Packaging and XML Configuration guidelines](https://www.w3.org/TR/2011/REC-widgets-20110927/). For a quick view of the entire element hierarchy, see [Configuration Element Hierarchy](#hierarchy).

> **Note**  
> The extension elements are denoted as though the `xmlns:tizen="http://tizen.org/ns/widgets"` namespace declaration is in effect.

The maximum length of the attribute and the element (except `<tizen:metadata>`, W3C preference element) can be limited to 2048 bytes. In this case, leftover bytes are ignored.

<a name="mw_account"></a>
### Tizen Account

<table>
	<thead>
		<tr>
			<th>&lt;tizen:account/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to register account provider information.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><code>icon</code>
				<p>Mandatory. Since the icons are used on the device under <strong>Settings &gt; Accounts</strong>, place them in a shared directory.</p>
				<p>Attributes:</p>
				<ul>
					<li><code>Account</code>: File path of the account provider icon. The icon size is 72 x 72 pixels.</li>
					<li><code>AccountSmall</code>: File path of the account provider small icon. The icon size is 45 x 45 pixels.</li>
				</ul>
				</li>
				<li><code>display-name</code>
				<p>Mandatory; display name of the account provider</p>
				</li>
				<li><code>capability</code>
				<p>Optional; capability of the account provider. Capabilities are defined in the http://&lt;VENDOR_INFORMATION&gt;/accounts/capability/&lt;NAME&gt; IRI format.</p>
				</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>multiple-account-support</code>
				<p>Mandatory; indicates whether multiple accounts are supported (available values: <code>true</code>, <code>false</code>)</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:account multiple-account-support="false"&gt;
   &lt;tizen:icon section="Account"&gt;account_provider_icon.png&lt;/tizen:icon&gt;
   &lt;tizen:icon section="AccountSmall"&gt;account_provider_small_icon.png&lt;/tizen:icon&gt;
   &lt;tizen:display-name xml:lang="en"&gt;AccountProviderExample&lt;/tizen:display-name&gt;
   &lt;tizen:capability&gt;http://tizen.org/account/capability/contact &lt;/tizen:capability&gt;
&lt;/tizen:account&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_navigation"></a>
### Tizen Navigation Policy

<table>
	<thead>
		<tr>
			<th>&lt;tizen:allow-navigation/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define a list of URL domains that are allowed to be navigated in using the Web application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is applied.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:allow-navigation&gt;tizen.org *.tizen.org&lt;tizen:allow-navigation/&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_appcontrol"></a>
### Tizen Application Control

<table>
	<thead>
		<tr>
			<th>&lt;tizen:app-control/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to indicate that the Web application can handle a specific operation with the specified MIME type and URI. For more information, see <a href="../../web/guides/app-management/app-controls.md">Application Information and Controls</a>.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Attributes:</p>
				<ul>
					<li><code>name</code>
					<p>Mandatory; page handling the requests</p>
					</li>
					<li><code>reload</code>
					<p>Optional; sets whether the page is reloaded when it is already loaded (available values: <code>enable</code> (default), <code>disable</code>)<p>
					<p><strong>Since: 2.4</strong></p>
					<blockquote><p><strong>Note</strong><br>
                    The <code>reload</code> attribute is supported since Tizen 2.4. If the <code>required_version</code> in the application's <code>config.xml</code> file is set to a version older than Tizen 2.4, and the <code>reload</code> attribute is used, the application installation fails</p></blockquote>
					</li>
				</ul>
				</li>
				<li><code>operation</code>
				<p>Mandatory; string that defines the action to be performed</p>
				</li>
				<li><code>uri</code> and <code>mime</code>
				<p>Optional; additional parameters used for resolving application control requests</p>
				</li>
				<li><code>privilege</code>
				<p>Optional; additional parameter used for getting required API access privileges for application control requests</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:app-control&gt;
   &lt;tizen:src name="view.html" reload="disable" /&gt;
   &lt;tizen:operation name="http://tizen.org/appcontrol/operation/view" /&gt;
   &lt;tizen:uri name="http" /&gt;
   &lt;tizen:mime name="image/jpeg" /&gt;
   &lt;tizen:privilege name="http://tizen.org/privilege/alarm" /&gt;
&lt;/tizen:app-control&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_appdefined_privilege"></a>
### Tizen App-defined Privilege

<table>
	<thead>
		<tr>
			<th>&lt;tizen:appdefined-privilege/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to get the required access privileges provided by a provider package.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; name of the app-defined privilege</p>
				</li>
				<li><code>license</code>
				<p>Optional; name of the license file used to verify the privilege</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:appdefined-privilege name="http://{provider_pkgid}/appdefined/exampleprivilege1" /&gt;
&lt;tizen:appdefined-privilege license="example_license" name="http://{provider_pkgid}/appdefined/exampleprivilege2" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_application"></a>
### Tizen Application ID

<table>
	<thead>
		<tr>
			<th>&lt;tizen:application/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to uniquely identify a Tizen application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>id</code>
				<p>Mandatory; Tizen application ID, which is a combination of the Tizen package ID and project name. The application ID is unique among applications on the device.</p>
				<p>The project name is a set of characters (0~9, a~z, A~Z) randomly generated by the Tizen Studio. The minimum value is 1 byte and the maximum value is 52 bytes.</p>
				</li>
				<li><code>package</code>
				<p>Mandatory; Tizen package ID generated by the Tizen Studio, consisting of 10 characters (0~9, a~z, A~Z). The package ID is unique in the Tizen Store.</p>
				</li>
				<li><code>required_version</code>
				<p>Mandatory; Tizen API version required for running the Web application</p>
				</li>
				<li><code>launch_mode</code>
				<p>Optional; sets which launch mode is supported (available values: <code>single</code> (default), <code>group</code>, <code>caller</code><p>
				<ul>
					<li><code>single</code>: launched as a main application</li>
					<li><code>group</code>: launched as a sub application</li>
					<li><code>caller</code>: caller application defines the launch mode with the <code>app_control_set_launch_mode()</code> method</li>
				</ul>
				<p><strong>Since: 2.4</strong></p>
				<blockquote><p><strong>Note</strong><br>
                The <code>launch_mode</code> attribute is supported since Tizen 2.4. If the <code>required_version</code> in the application's <code>config.xml</code> file is set to a version older than Tizen 2.4, and the <code>launch_mode</code> attribute is used, the application installation fails.</p></blockquote>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:application id="1234abcDEF.projectname"
                   package="1234abcDEF"
                   required_version="2.4"
                   launch_mode="caller" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_bg_category"></a>
### Tizen Background Category

<table>
	<thead>
		<tr>
			<th>&lt;tizen:background-category/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to represent the category of an application that is allowed to run in the background.
			<blockquote><p><strong>Note</strong><br>
            In addition to declaring the <code>&lt;background-category&gt;</code> element, you must <a href="#mw_setting">set the <code>&lt;tizen:setting background-support&gt;</code> attribute to <code>enable</code></a> to run Web applications in the background.</p></blockquote>
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>value</code>
				<p>Mandatory; <a href="../../native/guides/app-management/efl-ui-app.md#allow_bg_table">background category</a></p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:background-category value="media" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_webapp"></a>
### Tizen-hosted Web Application

<table>
	<thead>
		<tr>
			<th>&lt;tizen:content/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to point to a document which is hosted on an external server and acts as the Web application start page. The Tizen WRT allows the start page to be hosted on an external server.
			<p>If the start page is contained in the widget package, it is defined with the <a href="#content_element">&lt;content&gt; W3C element</a>. If both <code>&lt;content&gt;</code> and <code>&lt;tizen:content/&gt;</code> elements are defined, the <code>&lt;tizen:content/&gt;</code> element is used.</p>
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1 <code>&lt;tizen:content/&gt;</code> element is specified, the first instance of the element is used.</p>
				</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Mandatory; URI of the external start page</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:content src="https://www.tizen.org/" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_sec"></a>
### Tizen Content Security Policy

<table>
	<thead>
		<tr>
			<th>&lt;tizen:content-security-policy/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define an additional content security policy for a packaged or hosted application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is applied.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:content-security-policy&gt;script-src 'self'&lt;/tizen:content-security-policy&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_secreport"></a>
### Tizen Content Security Policy Report Only

<table>
	<thead>
		<tr>
			<th>&lt;tizen:content-security-policy-report-only/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define an additional content security policy, for monitoring purposes, for a packaged or hosted application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is applied.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:content-security-policy-report-only&gt;
   script-src 'self'; report-uri="http://example.com/report.cgi"
&lt;/tizen:content-security-policy-report-only&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_feature"></a>
### Tizen Feature

<table>
	<thead>
		<tr>
			<th>&lt;feature/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define hardware and software components for a Tizen application. This attribute is only used in the Tizen Store for filtering purposes. It is ignored by the Web Runtime installation procedure.
			<blockquote><p><strong>Note</strong><br>
            Even though the <code>&lt;feature/&gt;</code> element is defined in the Widget Packaging and XML Configuration guidelines, an extended version is used in Tizen.</p></blockquote>
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; <a href="../../web/tutorials/process/setting-properties.md#feature">feature key</a> URI</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;feature name="http://tizen.org/feature/network.bluetooth" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_metadata"></a>
### Tizen Metadata

<table>
	<thead>
		<tr>
			<th>&lt;tizen:metadata/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define metadata information shared with other Web applications. The defined metadata can be accessed (read-only) through the Tizen <a href="https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/device_api/mobile/tizen/application.html">Application</a> API.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>key</code>
				<p>Mandatory; unique key string.</p>
				<p>The maximum length can be limited to 80 bytes. In this case, leftover bytes are ignored.</p>
				</li>
				<li><code>value</code>
				<p>Optional; string.</p>
				<p>The maximum length can be limited to 8192 bytes. In this case, leftover bytes are ignored.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:metadata key="key1" /&gt;
&lt;tizen:metadata key="key2" value="value/&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_privilege"></a>
### Tizen Privilege

<table>
	<thead>
		<tr>
			<th>&lt;tizen:privilege/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to get the required API access privileges for a Web application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more (if duplicates, the first occurrence is considered and all others ignored)</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; URI of the Device API privilege</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:privilege name="http://tizen.org/privilege/application.launch" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_provides_appdefined_privilege"></a>
### Tizen Provided App-defined Privilege

<table>
	<thead>
		<tr>
			<th>&lt;tizen:provides-appdefined-privilege/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to specify the app-defined access privileges provided by a provider package.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; name of the app-defined privilege</p>
				</li>
				<li><code>license</code>
				<p>Optional; name of the license file used to verify the privilege</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:provides-appdefined-privilege name="http://{provider_pkgid}/appdefined/exampleprivilege1" /&gt;
&lt;tizen:provides-appdefined-privilege license="example_license" name="http://{provider_pkgid}/appdefined/exampleprivilege2" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_profile"></a>
### Tizen Profile

<table>
	<thead>
		<tr>
			<th>&lt;tizen:profile/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the application profile.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; string</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:profile name="mobile" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_setting"></a>
### Tizen Settings

<table>
	<thead>
		<tr>
			<th>&lt;tizen:setting/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define additional application settings.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>screen-orientation</code>
				<p>Optional; viewport orientation lock (available values: <code>portrait</code> (default), <code>landscape</code> auto-rotation</p>
				If the system auto rotation setting is on, the Web application viewport orientation is changed accordingly by default.</li>
				<li><code>context-menu</code>
				<p>Optional; context menu is displayed when the user clicks, for example, an image, text, or link (available values: <code>enable</code> (default), <code>disable</code>)</p>
				</li>
				<li><code>background-support</code>
				<p>Optional; application execution continues when it is moved to the background (available values: <code>enable</code> (execution continues in the background), <code>disable</code> (default; application is suspended))</p>
				<blockquote><p><strong>Note</strong><br>
                Since Tizen 2.4, the system manages background processes more tightly. Even if the <code>background-support</code> attribute is set to <code>enable</code>, a Web application process can be suspended in the background. To guarantee that the application runs in the background, <a href="#mw_bg_category">add at least one background category</a> for the application with the <code>&lt;tizen:background-category&gt;</code> element. Only the background categories declared in the system can be used.</p></blockquote>
				</li>
				<li><code>encryption</code>
				<p>Optional; Web application resources (HTML, JavaScript, and CSS files) are stored encrypted (available values: <code>enable</code>, <code>disable</code> (default))</p>
				</li>
				<li><code>install-location</code>
				<p>Optional; application installation location (available values: <code>auto</code> (default), <code>internal-only</code>, <code>prefer-external</code>)</p>
				<ul>
					<li><code>auto</code>: the system defines the installation location</li>
					<li><code>internal-only</code>: the application is installed in the device's internal storage</li>
					<li><code>prefer-external</code>: the application is installed in the external storage (if available)</li>
				</ul>
				</li>
				<li><code>hwkey-event</code>
				<p>Optional; a hardware key event is sent to the Web application when the user presses the hardware key (available values: <code>enable</code> (default), <code>disable</code>)<p>
				<p>If this option is enabled, the <code>tizenhwkey</code> custom event is sent to the Web application. The <code>tizenhwkey</code> event object has a <code>keyName</code> attribute (available values: <code>menu</code> and <code>back</code>).</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;!--Viewport orientation is locked to "landscape"--&gt;
&lt;tizen:setting screen-orientation="landscape" /&gt;
&lt;!--Context menu is not displayed--&gt;
&lt;tizen:setting context-menu="disable" /&gt;
&lt;!--Web application execution is not suspended--&gt;
&lt;!--when the application is sent to the background--&gt;
&lt;tizen:setting background-support="enable" /&gt;
&lt;!--Web applications resources are stored encrypted by the WRT--&gt;
&lt;tizen:setting encryption="enable" /&gt;
&lt;!--Installation location is set to "internal-only"--&gt;
&lt;tizen:setting install-location="internal-only" /&gt;
&lt;!--Hardware key event is sent to the Web application when the hardware key is pressed--&gt;
&lt;tizen:setting hwkey-event="enable" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="mw_trust-anchor"></a>
### Tizen Trust-anchor

<table>
	<thead>
		<tr>
			<th>&lt;tizen:trust-anchor/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to assign your own SSL root certificates for the application's HTTPS communication.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or 1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>use-system-certs</code>
				<p>Mandatory; indicates whether system certificates are used (available values: <code>true</code>, <code>false</code>)</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:trust-anchor use-system-certs="false" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_extend"></a>
## Extending Configuration Elements in Wearable Applications

<p>The following sections show additional configuration elements used in the `config.xml` file of a Web application, but not included in the <a href="https://www.w3.org/TR/2011/REC-widgets-20110927/" target="_blank">Widget Packaging and XML Configuration guidelines</a>. For a quick view of the entire element hierarchy, see <a href="#hierarchy">Configuration Element Hierarchy</a>.</p>

> **Note**  
> The extension elements are denoted as though the `xmlns:tizen="http://tizen.org/ns/widgets"` namespace declaration is in effect.
>
> The maximum length of the attribute and the element (except `tizen:metadata`, W3C preference element) can be limited to 2048 bytes. In that case, leftover bytes are ignored.

<a name="ww_account"></a>
### Tizen Account

<table>
	<thead>
		<tr>
			<th>&lt;tizen:account/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to register account provider information.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><code>display-name</code>
				<p>Mandatory; display name of the account provider</p>
				</li>
				<li><code>capability</code>
				<p>Optional; capability of the account provider. Capabilities are defined in the <code>http://&lt;VENDOR_INFORMATION&gt;/accounts/capability/&lt;NAME&gt;</code> IRI format.</p>
				</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>multiple-account-support</code>
				<p>Mandatory; indicates whether multiple accounts are supported (available values: <code>true</code>, <code>false</code>)</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:account multiple-account-support="false"&gt;
   &lt;tizen:display-name xml:lang="en"&gt;AccountProviderExample&lt;/tizen:display-name&gt;
   &lt;tizen:capability&gt;http://tizen.org/account/capability/contact &lt;/tizen:capability&gt;
&lt;/tizen:account&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_allownavigation"></a>
### Tizen Navigation Policy

<table>
	<thead>
		<tr>
			<th>&lt;tizen:allow-navigation/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define a list of URL domains that are allowed to be navigated in using the Web application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is applied.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:allow-navigation&gt;tizen.org *.tizen.org&lt;tizen:allow-navigation/&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="appcontrol"></a>
### Tizen Application Control

<table>
	<thead>
		<tr>
			<th>&lt;tizen:app-control/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to indicate that the Web application can handle a specific operation with the specified MIME type and URI. For more information, see <a href="../../web/guides/app-management/app-controls.md">Application Information and Controls</a>.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Attributes:</p>
				<ul>
					<li><code>name</code>
					<p>Mandatory; page handling the requests</p>
					</li>
					<li><code>reload</code>
					<p>Optional; sets whether the page is reloaded when it is already loaded (available values: <code>enable</code> (default), <code>disable</code>)</p>
					<p><strong>Since: 2.4</strong></p>
					<blockquote><p><strong>Note</strong><br>
                    The <code>reload</code> attribute is supported since Tizen 2.4. If the <code>required_version</code> in the application's <code>config.xml</code> file is set to a version older than Tizen 2.4, and the <code>reload</code> attribute is used, the application installation fails.</p></blockquote>
					</li>
				</ul>
				</li>
				<li><code>operation</code>
				<p>Mandatory; string that defines the action to be performed</p>
				</li>
				<li><code>uri</code> and <code>mime</code>
				<p>Optional; additional parameters used for resolving application control requests</p>
				</li>
				<li><code>privilege</code>
				<p>Optional; additional parameter used for getting required API access privileges for application control requests</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:app-control&gt;
   &lt;tizen:src name="view.html" reload="disable" /&gt;
   &lt;tizen:operation name="http://tizen.org/appcontrol/operation/view" /&gt;
   &lt;tizen:uri name="http" /&gt;
   &lt;tizen:mime name="image/jpeg" /&gt;
   &lt;tizen:privilege name="http://tizen.org/privilege/alarm" /&gt;
&lt;/tizen:app-control&gt;
             </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_webwidget"></a>
### Tizen Web Widget

<table>
	<thead>
		<tr>
			<th>&lt;tizen:app-widget/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the basic information for a Web widget.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><a href="#ww_widget-label">&lt;tizen:widget-label/&gt;</a></li>
				<li><a href="#ww_widget-content">&lt;tizen:widget-content/&gt;</a></li>
				<li><a href="#ww_widget-metadata">&lt;tizen:widget-metadata/&gt;</a></li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>id</code>
				<p>Mandatory; unique ID of the Web widget in the &lt;TIZEN_APPLICATION_ID&gt;.&lt;STRING&gt; format, where &lt;STRING&gt; consists of 1 or more characters (0~9, a~z, A~Z)</p>
				</li>
				<li><code>primary</code>
				<p>Mandatory; defines a primary Web widget among the Web widgets in a Web application (available values: <code>true</code>, <code>false</code>)</p>
				</li>
				<li><code>max-instance</code>
				<p>Optional; limits the number of widget instances concurrently executable for a Web application. When omitted or its value is 0, unlimited number of widget instances are supported. The expected value is <code>integer</code>.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:app-widget id="EHtuCWfzcr.Widget.Widget" primary="true" max-instance="0"&gt;
   &lt;tizen:widget-label&gt;Hello Web Widget!&lt;/tizen:widget-label&gt;
   &lt;tizen:widget-content src="index.html"&gt;
      &lt;tizen:widget-size preview="preview.png"&gt;2x2&lt;/tizen:widget-size&gt;
   &lt;/tizen:widget-content&gt;
   &lt;tizen:widget-metadata key="index" value="2" /&gt;
&lt;/tizen:app-widget&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_widget-label">
	<thead>
		<tr>
			<th>&lt;tizen:widget-label/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the name of the Web widget.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code>
				<p>Optional; specifies the language of the box label (for available values, see <a href="http://www.iana.org/assignments/language-subtag-registry" target="_blank">the IANA Language Subtag</a>)</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_widget-content">
	<thead>
		<tr>
			<th>&lt;tizen:widget-content/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the starting page of the Web widget.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><a href="#ww_widget-size">&lt;tizen:widget-size/&gt;</a></li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Mandatory; local file path, relative to the source Web application directory of the widget starting page</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_widget-size">
	<thead>
		<tr>
			<th>&lt;tizen:widget-size/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the size of the Web widget.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>preview</code>
				<p>Mandatory; image file path, relative to the source Web application directory of the box content displayed in the widget viewer</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_widget-metadata">
	<thead>
		<tr>
			<th>&lt;tizen:widget-metadata/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define a (key, value) pair that can be read by a Web widget through the WidgetService API. Its main use is to allow you to define a constant to be read by a Web widget.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>key</code>
				<p>Mandatory; string.</p>
				</li>
				<li><code>value</code>
				<p>Mandatory; string.</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_appdefined_privilege"></a>
### Tizen App-defined Privilege

<table>
	<thead>
		<tr>
			<th>&lt;tizen:appdefined-privilege/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to get the required access privileges provided by a provider package.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; name of the app-defined privilege</p>
				</li>
				<li><code>license</code>
				<p>Optional; name of the license file used to verify the privilege</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:appdefined-privilege name="http://{provider_pkgid}/appdefined/exampleprivilege1" /&gt;
&lt;tizen:appdefined-privilege license="example_license" name="http://{provider_pkgid}/appdefined/exampleprivilege2" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_application"></a>
### Tizen Application ID

<table>
	<thead>
		<tr>
			<th>&lt;tizen:application/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to uniquely identify a Tizen wearable application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>id</code>
				<p>Mandatory; Tizen application ID, which is a combination of the Tizen wearable package ID and project name. The application ID is unique among applications on the device.</p>
				<p>The project name is a set of characters (0~9, a~z, A~Z) randomly generated by the Tizen Studio. The minimum value is 1 byte and the maximum value is 52 bytes.</p>
				</li>
				<li><code>package</code>
				<p>Mandatory; Tizen wearable package ID generated by the Tizen Studio, consisting of 10 characters (0~9, a~z, A~Z). The package ID is unique in the Samsung Apps.</p>
				</li>
				<li><code>required_version</code>
				<p>Mandatory; Tizen API version required for running the Web application</p>
				</li>
				<li><code>ambient_support</code>
				<p>Optional; sets whether the Web application supports the ambient mode (available values: <code>enable</code>, <code>disable</code> (default))</p>
				<p>If this option is enabled, the application can be shown in the ambient mode.</p>
				<strong>Since: 2.3.1</strong>
				<blockquote><p><strong>Note</strong><br>
                The <code>ambient_support</code> option is only used for watch applications, and ignored in all non-watch applications.<br>
               <br>
				The <code>ambient_support</code> attribute is supported since Tizen 2.3.1. If the <code>required_version</code> in the application's <code>config.xml</code> file is set to a version older than Tizen 2.3.1, and the <code>ambient_support</code> attribute is used, the application installation fails.</p><blockquote>
				</li>
				<li><code>launch_mode</code>
				<p>Optional; sets which launch mode is supported (available values: <code>single</code> (default), <code>group</code>, <code>caller</code>)</p>
				<ul>
					<li><code>single</code>: launched as a main application</li>
					<li><code>group</code>: launched as a sub application</li>
					<li><code>caller</code>: caller application defines the launch mode with the <code>app_control_set_launch_mode()</code> method</li>
				</ul>
				<p><strong>Since: 2.4</strong></p>
				<p><strong>Note</strong><br>
                The <code>launch_mode</code> attribute is supported since Tizen 2.4. If the <code>required_version</code> in the application's <code>config.xml</code> file is set to a version older than Tizen 2.4, and the <code>launch_mode</code> attribute is used, the application installation fails.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:application id="1234abcDEF.projectname"
                   package="1234abcDEF"
                   required_version="2.4"
                   ambient_support="enable" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_bg_category"></a>
### Tizen Background Category

<table>
	<thead>
		<tr>
			<th>&lt;tizen:background-category/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to represent the category of an application that is allowed to run in the background.
			<p><strong>Note</strong><br>
            In addition to declaring the &lt;background-category&gt; element, you must <a href="#ww_setting">set the &lt;tizen:setting background-support&gt; attribute to <code>enable</code></a> to run Web applications in the background.</p>
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>value</code>
				<p>Mandatory; <a href="../../native/guides/app-management/efl-ui-app.md#allow_bg_table">background category</a></p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:background-category value="media" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_category"></a>
### Tizen Category

<table>
	<thead>
		<tr>
			<th>&lt;tizen:category/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the categories to which the service application belongs.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; string</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>&lt;tizen:category name="http://tizen.org/category/wearable_clock" /&gt;</code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_tizencontent"></a>
### Tizen Content

<table>
	<thead>
		<tr>
			<th>&lt;tizen:content/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define a start page hosted on an external server.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is considered and all others ignored.</p>
				</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Mandatory; URI of an external start page</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:content src="https://www.tizen.org" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_contentsecpolicy"></a>
### Tizen Content Security Policy

<table>
	<thead>
		<tr>
			<th>&lt;tizen:content-security-policy/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define an additional content security policy for a packaged or hosted application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is applied.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:content-security-policy&gt;script-src 'self'&lt;/tizen:content-security-policy&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_contentsecpolicyreport"></a>
### Tizen Content Security Policy Report Only

<table>
	<thead>
		<tr>
			<th>&lt;tizen:content-security-policy-report-only/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define an additional content security policy, for monitoring purposes, for a packaged or hosted application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more
				<p>If more than 1, the first occurrence is applied.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:content-security-policy-report-only&gt;
   script-src 'self'; report-uri="http://example.com/report.cgi"
&lt;/tizen:content-security-policy-report-only&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_feature"></a>
### Tizen Feature

<table>
	<thead>
		<tr>
			<th>&lt;feature/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the hardware and software components for a Tizen wearable Web application. This attribute is only used in the Samsung Apps for filtering purposes. It is ignored by the Web Runtime installation procedure.
			<p><strong>Note</strong><br>
            Even though the <code>&lt;feature/&gt;</code> element is defined in the Widget Packaging and XML Configuration guidelines, an extended version is used in Tizen.</p>
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; <a href="../../web/tutorials/process/setting-properties.md#feature">feature key</a> URI</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;feature name="http://tizen.org/feature/network.bluetooth" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_ime"></a>
### Tizen IME

<table>
	<thead>
		<tr>
			<th>&lt;tizen:ime/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the properties of an IME (Input Method Editor) type application, which is used when you want to create your own keyboard module for the Tizen platform.
			<p><strong>Note</strong><br>
            <code>&lt;tizen:category name="http://tizen.org/category/ime" /&gt;</code> must be defined to activate &lt;tizen:ime&gt;.</p>
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or 1</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><code>uuid</code>
				<p>Mandatory; universally unique, a unique identifier that distinguishes an IME from each other, displayed in the form of a standard UUID (8-4-4-4-12 for a total of 36 characters)</p>
				</li>
				<li><code>languages</code>
				<p>Mandatory; list of input languages that the current IME supports</p>
				<p><strong>Note</strong><br>
                <code>&lt;tizen:language/&gt;</code> elements are provided as the child elements of this element.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:ime&gt;
   &lt;tizen:uuid&gt;6135122a-a428-40d2-8feb-a75f462c202c&lt;/tizen:uuid&gt;
   &lt;tizen:languages&gt;
      &lt;tizen:language&gt;en-us&lt;/tizen:language&gt;
      &lt;tizen:language&gt;de-de&lt;/tizen:language&gt;
   &lt;/tizen:languages&gt;
&lt;/tizen:ime&gt;

&lt;tizen:category name="http://tizen.org/category/ime" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_language">
	<thead>
		<tr>
			<th>&lt;tizen:language/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the supported input language of the current IME type application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1 or more</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:languages&gt;
   &lt;tizen:language&gt;en-us&lt;/tizen:language&gt;
   &lt;tizen:language&gt;de-de&lt;/tizen:language&gt;
&lt;/tizen:languages&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_metadata"></a>
### Tizen Metadata

<table>
	<thead>
		<tr>
			<th>&lt;tizen:metadata/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define metadata information shared with other Web applications. The defined metadata can be accessed (read-only) through the Tizen <a href="https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/device_api/wearable/tizen/application.html">Application</a> API.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>key</code>
				<p>Mandatory; unique key string.</p>
				<p>The maximum length can be limited to 80 bytes. In that case, leftover bytes are ignored.</p>
				</li>
				<li><code>value</code>
				<p>Optional; string.</p>
				<p>The maximum length can be limited to 8192 bytes. In that case, leftover bytes are ignored.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:metadata key="key1" /&gt;
&lt;tizen:metadata key="key2" value="value/&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_privilege"></a>
### Tizen Privilege

<table>
	<thead>
		<tr>
			<th>&lt;tizen:privilege/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to get the required API access privileges for the Web application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; URI of the Device API privilege</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:privilege name="http://tizen.org/privilege/application.launch" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_provides_appdefined_privilege"></a>
### Tizen Provided App-defined Privilege

<table>
	<thead>
		<tr>
			<th>&lt;tizen:provides-appdefined-privilege/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to specify the app-defined access privileges provided by a provider package.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; name of the app-defined privilege</p>
				</li>
				<li><code>license</code>
				<p>Optional; name of the license file used to verify the privilege</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:provides-appdefined-privilege name="http://{provider_pkgid}/appdefined/exampleprivilege1" /&gt;
&lt;tizen:provides-appdefined-privilege license="example_license" name="http://{provider_pkgid}/appdefined/exampleprivilege2" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_profile"></a>
### Tizen Profile

<table>
	<thead>
		<tr>
			<th>&lt;tizen:profile/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the application profile.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; string</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<code>
&lt;tizen:profile name="wearable" /&gt;
            </code>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_service"></a>
### Tizen Service

<table>
	<thead>
		<tr>
			<th>&lt;tizen:service/&gt; element</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Used to define a Web service application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Expected children:</strong></p>
			<ul>
				<li><a href="#ww_service-content">&lt;tizen:content/&gt;</a></li>
				<li><a href="#ww_service-name">&lt;tizen:name/&gt;</a></li>
				<li><a href="#ww_service-icon">&lt;tizen:icon/&gt;</a></li>
				<li><a href="#ww_service-description">&lt;tizen:description/&gt;</a></li>
				<li><a href="#ww_service-metadata">&lt;tizen:metadata/&gt;</a></li>
				<li><a href="#ww_service-category">&lt;tizen:category/&gt;</a></li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>id</code>
				<p>Mandatory; Tizen service ID, which is a combination of the Tizen wearable package ID and service name.</p>
				<p>The service ID is a set of characters (0~9, a~z, A~Z) and unique among service applications on the device. The minimum value is 1 byte and the maximum value is 52 bytes.</p>
				</li>
				<li><code>on-boot</code>
				<p>Optional; sets whether the service application is launched automatically on device boot (available values: <code>true</code>, <code>false</code> (default))</p>
				<p><strong>Note</strong><br>
                This attribute is not supported on Tizen wearable devices. Since Tizen 2.4, this attribute is not supported on all Tizen devices.</p>
				</li>
				<li><code>auto-restart</code>
				<p>Optional; sets whether the service application is relaunched automatically when it is terminated (available values: <code>true</code>, <code>false</code> (default))</p>
				<p><strong>Note</strong><br>
                This attribute is not supported on Tizen wearable devices. Since Tizen 2.4, this attribute is not supported on all Tizen devices.</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:service id="webService.application" auto-restart="true" on-boot="false"&gt;
   &lt;tizen:content src="service/service.js" /&gt;
   &lt;tizen:name&gt;WebService&lt;/tizen:name&gt;
   &lt;tizen:icon src="service-icon.png" /&gt;
   &lt;tizen:description&gt;Web Service Application&lt;/tizen:description&gt;
   &lt;tizen:metadata key="key1" value="value1" /&gt;
   &lt;tizen:category name="http://tizen.org/category/service" /&gt;
&lt;tizen:service&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_service-content">
	<thead>
		<tr>
			<th>&lt;tizen:content/&gt; element</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Used to define the start page of the Web service application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Mandatory; start JavaScript file path of the Web service application. The path is relative to the source Web application directory.</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_service-name">
	<thead>
		<tr>
			<th>&lt;tizen:name/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the name of the Web service application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>1 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>xml:lang</code>
				<p>Optional; specifies the language of the service name (for available values, see <a href="http://www.iana.org/assignments/language-subtag-registry" target="_blank">the IANA Language Subtag</a>)</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_service-icon">
	<thead>
		<tr>
			<th>&lt;tizen:icon/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the icon for the Web service application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or 1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>src</code>
				<p>Mandatory; file path of the Web service application icon. The path is relative to the source Web application directory.</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_service-description">
	<thead>
		<tr>
			<th>&lt;tizen:description/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the description for the Web service application.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or 1</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_service-metadata">
	<thead>
		<tr>
			<th>&lt;tizen:metadata/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define metadata information shared with other Web applications. The defined metadata can be accessed (read-only) through the Tizen Application API.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>key</code>
				<p>Mandatory; unique key string</p>
				</li>
				<li><code>value</code>
				<p>Optional; string</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<table id="ww_service-category">
	<thead>
		<tr>
			<th>&lt;tizen:category/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define the categories that the service application belongs to.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>name</code>
				<p>Mandatory; string</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_setting"></a>
### Tizen Settings

<table>
	<thead>
		<tr>
			<th>&lt;tizen:setting/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to define additional application settings.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or more</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>background-support</code>
				<p>Optional; application execution continues when it is moved to the background (available values: <code>enable</code> (execution continues in the background), <code>disable</code> (default; application is suspended))</p>
				<p><strong>Note</strong><br>
                Since Tizen 2.4, the system manages background processes more tightly. Even if the <code>background-support</code> attribute is set to <code>enable</code>, a Web application process can be suspended in the background. To guarantee that the application runs in the background, <a href="#ww_bg_category">add at least one background category</a> for the application with the &lt;tizen:background-category&gt; element. Only the background categories declared in the system can be used.</p>
				</li>
				<li><code>context-menu</code>
				<p>Optional; sets whether the context menu is shown (available values: <code>enable</code> (default), <code>disable</code>)</p>
				<p>If this option is enabled, the context menu is visible to the user.</p>
				</li>
				<li><code>encryption</code>
				<p>Optional; sets whether Web application resources are encrypted (available values: <code>enable</code>, <code>disable</code> (default))</p>
				<p>If this option is enabled, the application resources (HTML, JS and CSS files) are encrypted.</p>
				</li>
				<li><code>screen-orientation</code>
				<p>Optional; sets whether it locks the orientation of the Web application (available values: <code>portrait</code> (default), <code>landscape</code>, <code>auto-rotation</code></p>
				<ul>
					<li><code>portrait</code> or <code>landscape</code>: orientation is locked to portrait or landscape respectively</li>
					<li><code>auto-rotation</code>: follows the device orientation setting</li>
				</ul>
				</li>
				<li><code>install-location</code>
				<p>Optional; application installation location (available values: <code>auto</code> (default), <code>internal-only</code>, <code>prefer-external</code>)</p>
				<ul>
					<li><code>auto</code>: the system defines the installation location</li>
					<li><code>internal-only</code>: the application is installed in the device's internal storage</li>
					<li><code>prefer-external</code>: the application is installed in the external storage (if available)</li>
				</ul>
				</li>
				<li><code>hwkey-event</code>
				<p>Optional; a hardware key event is sent to the Web application when the user presses the hardware key (available values: <code>enable</code> (default), <code>disable</code>)</p>
				<p>If this option is enabled, the <code>tizenhwkey</code> custom event is sent to the Web application. The <code>tizenhwkey</code> event object has a <code>keyName</code> attribute (available value: <code>back</code>).</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre><code>
&lt;tizen:setting background-support="enable" /&gt;
&lt;tizen:setting context-menu="disable" /&gt;
&lt;tizen:setting encryption="enable" /&gt;
&lt;tizen:setting screen-orientation="landscape" /&gt;
&lt;tizen:setting install-location="internal-only" /&gt;
&lt;tizen:setting hwkey-event="enable" /&gt;
            </code></pre>
			</td>
		</tr>
	</tbody>
</table>

<a name="ww_trust-anchor"></a>
### Tizen Trust-anchor

<table>
	<thead>
		<tr>
			<th>&lt;tizen:trust-anchor/&gt; element</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>Used to assign your own SSL root certificates for the application's HTTPS communication.
			<p><strong>Occurrences:</strong></p>
			<ul>
				<li>0 or 1</li>
			</ul>
			<p><strong>Attributes:</strong></p>
			<ul>
				<li><code>use-system-certs</code>
				<p>Mandatory; indicates whether system certificates are used (available values: <code>true</code>, <code>false</code>)</p>
				</li>
			</ul>
			<p><strong>Example:</strong></p>
			<pre class="prettyprint">
&lt;tizen:trust-anchor use-system-certs="false" /&gt;
</pre>
			</td>
		</tr>
	</tbody>
</table>
