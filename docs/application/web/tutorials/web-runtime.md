
# Web Runtime

The Web Runtime (WRT) engine allows Web applications to run outside the
browser. You can install Web applications and use them as standalone
applications.

The Web Runtime features include the following:

-   [Managing Web Applications](#manage)

    Provides information on supported Web application types and managing
    Web applications.

-   [Web Runtime API Support](#runtime)

    Provides information on APIs and features supported by the
    Web Runtime.

-   [Web Application Security and Privacy](#security)

    Provides information on the key security and privacy considerations
    for Web applications.

<a name="manage"></a>
## Managing Web Applications

The Web Runtime supports the following Web application types:  
-   Packaged Web applications

-   Hosted Web applications

All Web applications must be packaged according to the [Widget Packaging and XML Configuration
guidelines](https://www.w3.org/TR/2011/REC-widgets-20110927/). However, unlike packaged Web applications, the hosted Web applications have an externally hosted document as their starting page. For more information, see Extending Configuration Elements (in
[mobile](../../tizen-studio/web-tools/config-editor.md#mw_extend)
and [wearable](../../tizen-studio/web-tools/config-editor.md#ww_extend) applications).

You can manage Web applications by:

-   Installing Web applications

    To install a Web application, see the [guidelines for processing a
    Web application
    package](https://www.w3.org/TR/2011/REC-widgets-20110927/#steps-for-processing-a-widget-package).
    After the installation is completed, the WRT sends a notification of
    the result.

    The Web Runtime also registers the Web application on the device's
    idle screen. It fetches the Web application name and icon from the
    application package using the rules defined in the Widget Packaging
    and XML Configuration guidelines.

    If a Web application installation fails due to power failure, the
    Web Runtime reinstalls it on next boot. The Web Runtime aborts the
    installation in the following situations:

    -   Tizen Web API version supported by the Web Runtime is lower than
        the minimum version required by the Web application.
    -   Web application privilege level is Public, and 1 or more Partner
        or Platform level API privileges are declared in the
        configuration file.

  > **Note**  
  > A Web application can be installed from the Tizen Store or
    side-loaded (for example, through a browser or Bluetooth). The
    `<feature>` element is ignored in the Tizen Web application
    installation process.

-   Updating Web applications

    The WRT supports updating Web applications when there is a new
    version available.

    The following rules apply during the Web application updating
    process:

    -   If the Web application that is being updated has a Tizen AppID,
        it is not updated unless the new version has the exact same
        Tizen AppID.
    -   If the Web application that is being updated has an author
        signature, it is not updated unless the new version has been
        signed by the same author.
    -   If the Web application that is being updated has no author
        signature, it is not updated if the new version has an
        author signature.
    -   The updating process is similar to the installation process.
    -   Web application data, such as Tizen settings, cookies, and local
        storage are preserved across updates. You must ensure that the
        old data in your application is still usable after the update.
-   Uninstalling Web applications

    The WRT supports the uninstallation of Web applications. During the
    uninstallation process, all Web application data, such as
    preferences, local storage data, cookies, and the local storage
    folder, are removed.

-   Managing Web application life-cycle

    The WRT supports W3C DOM load and unload, and the [Page
    Visibility](http://www.w3.org/TR/page-visibility/) events for
    all pages.

    When a Web application is sent to the background or hidden, the
    JavaScript execution and rendering, including CSS animations, is
    suspended, unless the application is specifically configured to be a
    background service.

    When a Web application returns to the foreground, the JavaScript
    execution and rendering is resumed.

    The Web Runtime supports the following URI schemes: `sms://`,
    `mmsto://`, and `mailto://`.

    For each supported URI scheme, the Web Runtime launches a registered
    platform scheme handler with appropriate parameters.

    Content localization is supported according to the [Widget Packaging
    and XML Configuration
    recommendations](https://www.w3.org/TR/2011/REC-widgets-20110927/).

<a name="runtime"></a>
## Web Runtime API Support

The main functionality of the Web Runtime is to provide the following
Tizen Web APIs to Web applications:

-   [W3C/HTML5
    APIs](../api/latest/w3c_api/w3c_api_cover.html)

-   [Tizen Device
    API](../api/latest/device_api/device_api_cover.html)

It also supports multiple browsing context creation within a single Web
application using, for example, the `window.open()` method, or hyperlink
navigation.

Tizen Web APIs can be accessed in the top-level browsing context, such
as main document window, and nested browsing contexts, such as iframes.

> **Note**  
> Tizen Device API can only be used with a locally packaged page.
Tizen Device APIs are not available in cross-origin pages.

To access the host page of your Web application, add the domain for
access in the `config.xml` file. For more information, see [Content
Security Policy](#content_sec).

The Web Runtime also supports the following features:

-   [Widget Interface](http://www.w3.org/TR/widgets-apis/)

-   `maximized` and `fullscreen` view modes of the ['view-mode' Media
    Feature](http://www.w3.org/TR/view-mode/).

<a name="security"></a>
## Web Application Security and Privacy

The Web application security consists of the following elements:

-   [Web Application Signature](#signature)
-   [Web Application Protection](#protect)
-   [Private Storage Support](#storage)
-   [HTML5 API Security Policy](#html5)
-   [Tizen Device API Security Policy](#device)
-   [Content Security Policy](#content_sec)

<a name="signature"></a>
### Web Application Signature

The Web Runtime follows the [XML digital widget
signature](http://www.w3.org/TR/2011/PR-widgets-digsig-20110811/)
process:

-   Web application can be signed by the author and distributors.
-   The first valid Tizen distributor signature, `signature1.xml`,
    determines the privilege level of the Web application, which is
    either Public, Partner, or Platform.
-   Web application is installed as a trusted application when it is
    signed with valid signatures and its privilege level is Public,
    Partner, or Platform.
-   Web application is installed as an untrusted application if it is:
    -   Not signed by an author or distributor signature.
    -   Signed with a valid signature, but its privilege level is not
        Public, Partner, or Platform.
-   If the signature of a Web application is invalid, it cannot
    be installed.

<a name="protect"></a>
### Web Application Protection

For Web applications that explicitly turn on encryption (in
[mobile](../../tizen-studio/web-tools/config-editor.md#mw_setting)
and
[wearable](../../tizen-studio/web-tools/config-editor.md#ww_setting)
applications) using the `<tizen:setting/>` element in the configuration
file, the Web Runtime provides the following protection features:
-   HTML, JavaScript, and CSS files of the Web application stored by the    device are encrypted.
-   When the Web application is launched, the WRT decrypts all of its   resources in a manner which is transparent to the Web    application itself.

<a name="storage"></a>
### Private Storage Support

Each Web application has its own private storage space that is not
accessible to any other application.

<a name="html5"></a>
### HTML5 API Security Policy

The Web applications can use HTML5 APIs, some of which need user
permission to execute the API call. For such APIs, the Web Runtime
supports specific privileges.

The following table summarizes distributor signature type to API
privilege level behavior mapping.

**Table: HTML5 API privileges and behavior**

<table>
<tr>
<th>API</th>
<th>Privilege</th>
<th>Privilege behavior</th>
</tr>
<tr>

<td>

Geolocation (in **mobile and wearable applications only**)</td>
<td>

`http://tizen.org/privilege/location`</td>
<td>

**Local domain**: Grant permission if defined, otherwise block execution.<br>
**Remote domain**: Popup user prompt if defined, otherwise block execution.
</td>
</tr>
<tr>

<td>

Getusermedia (in **mobile and wearable applications only**)</td>
<td>

`http://tizen.org/privilege/mediacapture`</td>
<td>

**Local domain**: Grant permission if defined, otherwise block execution.<br>
**Remote domain**: Popup user prompt if defined, otherwise block execution.
</td>
</tr>
<tr>

<td>

Web Notifications (in **mobile applications only**)</td>
<td>

`http://tizen.org/privilege/notification`</td>
<td>

**Local domain**: Grant permission if defined, otherwise popup user prompt.<br>
**Remote domain**: Popup user prompt.
</td>
</tr>
<tr>

<td>

Storage (in **mobile and wearable applications only**)<br>(IndexedDB, FileSystem capacity, quota exceeding WebDatabase)
</td>
<td>

`http://tizen.org/privilege/unlimitedstorage`</td>
<td>

**Local domain**: Grant permission if defined, otherwise popup user prompt.<br>
**Remote domain**: Popup user prompt.
</td>
</tr>
<tr>

<td>

FullScreen (in **mobile and TV applications only**)</td>
<td>

`http://tizen.org/privilege/fullscreen`</td>
<td>If defined, launch in fullscreen mode. If not defined, launch fullscreen mode according to user input (which depends on the content).</td>
</tr>
<tr>
<td>

Audio Recording (in **wearable applications only**)</td>
<td>

`http://tizen.org/privilege/audiorecorder`</td>
<td>

**Local domain**: Grant permission if defined, otherwise block execution.<br>
**Remote domain**: Block execution.
</td>
</tr>
<tr>

<td>

Video Recording (in **wearable applications only**)</td>
<td>

`http://tizen.org/privilege/camera`</td>
<td>

**Local domain**: Grant permission if defined, otherwise block execution.<br>
**Remote domain**: Block execution.
</td>
</tr>
</table>

<a name="device"></a>
### Tizen Device API Security Policy

Web Runtime also provides access to sensitive Device API features after
consulting the platform-defined security policy. A Web application or an
individual user cannot elevate the permissions set by the
platform-defined security policy. The mapping between each Tizen Device
API and the corresponding privilege is defined in the API definitions in
the [Tizen Device API
Reference](../api/latest/device_api/device_api_cover.html).

The following table summarizes distributor signature type to API
privilege level behavior mapping:

**Table: Distributor signature type to API privilege level behavior
mapping**

<table>
<tr>
<th rowspan="2">API privilege level</th>

<th colspan="3">

Distributor signature type (`signature1.xml`)</th>
<th rowspan="2">Untrusted</th>
</tr>
<tr>
<th>Platform</th>
<th>Partner</th>
<th>Public</th>
</tr>
<tr>
<th>Platform</th>
<td>Allowed</td>

<td>

Security error for runtime use (direct API call without `config.xml` declaration)<br>
Installation fail for `config.xml` use
</td>
<td>

Security error for runtime use (direct API call without `config.xml` declaration)<br>
Installation fail for `config.xml` use
</td>
<td>

Security error for runtime use (direct API call without `config.xml` declaration)<br>
Installation fail for `config.xml` use
</td>
</tr>
<tr>
<th>Partner</th>
<td>Allowed</td>
<td>Allowed</td>

<td>

Security error for runtime use (direct API call without `config.xml` declaration)<br>
Installation fail for `config.xml` use
</td>
<td>

Security error for runtime use (direct API call without `config.xml` declaration)<br>
Installation fail for `config.xml` use
</td>
</tr>
<tr>
<th>Public</th>
<td>Allowed</td>
<td>Allowed</td>
<td>Allowed</td>

<td>

Security error for runtime use (direct API call without `config.xml` declaration)<br>
Installation fail for `config.xml` use
</td>
</tr>
</table>

<a name="content_sec"></a>
### Content Security Policy

The Web applications can mitigate various kinds of content injection
vulnerabilities, such as cross-site scripting (XSS). The content
security policy (CSP) is a declarative policy that lets the author or
server administrator of a Web application inform the client from where
the application expects to load resources. To mitigate XSS, for example,
a Web application can declare from where it expects to load scripts,
allowing the client to detect and block malicious scripts injected into
the application by an attacker.

Web application configuration can include 1 or more
`<tizen:content-security-policy>`,
`<tizen:content-security-policy-report-only>`, or
`<tizen:allow-navigation>` elements. If these are included, the Web
application is set to the **CSP-based security mode**.

In the CSP-based security mode, the Web Runtime provides content
security as per **Content Security Policy Level 2** (in mobile
applications) and **Content Security Policy 1.0** (in wearable
applications). CSP policies can be delivered from the following sources:

-   Default policy (enforced by WRT, if required):
    `default-src *; script-src 'self'; style-src 'self'; object-src 'none';`
-   `config.xml`: `<tizen:content-security-policy>` or
    `<tizen:content-security-policy-report-only>`

    If the CSP is defined in the `config.xml` file, the
    configuration-based CSP policy is enforced and the default CSP
    is ignored.

    If the CSP policy is not defined in the `config.xml` file, the
    default CSP policy is enforced.

-   HTTP header: `Content-Security-Policy` or
    `Content-Security-Policy-Report-Only`

    If a CSP is present in the HTTP header, the most restrictive policy
    in the configuration-based CSP and HTTP-based CSP is applied.

Otherwise, the Web application is set to the **WARP-based security
mode**. In this mode, the Web application network and content security
is enforced by the legacy `<access>` tag according to [Widget Access
Request Policy](http://www.w3.org/TR/2012/REC-widgets-access-20120207/).

> **Note**  
> The default CSP enforcement is subject to change in the future.

> **Note**  
> If a Web application declares the `<tizen:allow-navigation>`
element in its configuration document, the main resource navigation
(through the `window.open()` method or a hyperlink) to an external URL
is allowed or restricted accordingly.
