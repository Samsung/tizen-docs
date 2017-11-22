

Tizen Web Application Model
===========================

The [Tizen Studio](../../../tizen-studio/cover-page.md)
enables you to create Web applications for mobile, wearable, and TV
devices. A Web application consists of HTML, JavaScript, and CSS
combined in a package, which can be installed on the Tizen device.

A [Web application package](../process/app-dev-process-w.md#package)
includes all the support files that are needed by the Web application.
Therefore, a Web application can run without any additional external
resources or network connectivity after installation.

The application model supports a rich set of standard W3C/HTML5
features, which include various JavaScript APIs as well as additional
HTML markups and CSS features. These features, along with the Tizen
Device APIs and UI framework support, can be used to create rich Web
applications in a variety of categories, such as contacts, messaging,
device information access, multimedia, graphics, and games.

Tizen supports both [Web application packages](#wap) and [hybrid
application packages](#hap), which combine a Web application and 1 or
more native service applications.

Applications in the same package follow the same installation
life-cycle, handled by the [application package manager](#package).

Application Package Manager <a name="package"></a>
---------------------------

The application package manager is one of the core modules of the Tizen
application framework, and is responsible for installing, uninstalling,
and updating packages, and storing their information. Using the package
manager, you can also retrieve information related to the packages that
are installed on the device.

The application package manager module is expandable to support various
types of applications, and designated installation modules can be added
to it.

**Figure: Application package manager**

![Application package
manager](./media/application-package-manager.png)

### Web Package Configuration <a name="config"></a>

Each Web application package has a configuration file, `config.xml`,
which indicates a packaging format and metadata for the application.

The Tizen Web application must follow the guidelines of [W3C Widget
Packaging and XML
Configuration](https://www.w3.org/TR/2011/REC-widgets-20110927/) and
Tizen extended configuration (in
[mobile](../../../tizen-studio/web-tools/config-editor-w.md#mw_extend)
and
[wearable](../../../tizen-studio/web-tools/config-editor-w.md#ww_extend)
applications).

For more information on the configuration elements, see [Configuration
Element
Hierarchy](../../../tizen-studio/web-tools/config-editor-w.md#hierarchy).

### Web Application Package <a name="wap"></a>

The Tizen platform supports Web applications based on HTML, JavaScript,
and CSS, and packaged according to the W3C specification. The platform
also provides device APIs to access the platform capabilities, enabling
a rich Web application development environment.

A Web application package must conform to the following conventions:

-   Package format and file extension
    -   File format: ZIP archive file format
    -   File extension: `.wgt` (for example, `sample.wgt`)
    -   MIME type: `application/widget`
-   Application ID
    -   The application ID cannot be changed after the application
        is published.
-   Package content
    -   File and folders: The root of the Web package is the path of the
        ZIP archive and contains files and folders, some of which
        are reserved. The following table shows the content of
        a package.

        **Table: Package content**
<table>
<tr>
  <th> Name </th>
  <th> Type </th>
  <th> Description </th>
</tr>
<tr>
  <td> `config.xml` </td>
  <td> File </td>
  <td> Application configuration document </td>
</tr>
<tr>
  <td>       `icon.gif`   </td>
  <td> File  </td>
  <td> Application default icon </td>
</tr>
<tr>
  <td>    `icon.ico`   </td>
  <td> File  </td>
  <td> Application default icon </td>
</tr>
<tr>
  <td>        `icon.jpg`    </td>
  <td> File  </td>
  <td> Application default icon </td>
</tr>
<tr>
  <td>         `icon.png`     </td>
  <td> File  </td>
  <td> Application default icon </td>
</tr>
<tr>
  <td>         `icon.svg`     </td>
  <td> File  </td>
  <td> Application default icon </td>
</tr>
<tr>
  <td>        `index.html`    </td>
  <td> File  </td>
  <td>  Application default start file </td>
</tr>
<tr>
  <td>     `index.htm`     </td>
  <td> File  </td>
  <td>  Application default start file </td>
</tr>
<tr>
  <td>          `index.svg`      </td>
  <td> File  </td>
  <td>  Application default start file </td>
</tr>
<tr>
  <td>             `index.xhtml`      </td>
  <td> File  </td>
  <td>  Application default start file </td>
</tr>
<tr>
  <td>       `index.xht`     </td>
  <td> File  </td>
  <td>  Application default start file </td>
</tr>
<tr>
  <td>        `locales`    </td>
  <td>  Folder   </td>
  <td>  Container for localized content </td>
</tr>
</table>        



-   Directory hierarchy (after installation on device)

    The following figure and table illustrate the Web application
    package directory structure.

    **Figure: Web application directory structure**

    ![Web application directory
    structure](./media/web-app-directory-structure.png)

    **Table: Web application package structure**

    <table>
<tr>
  <th> Package </th>
  <th> Root directory </th>
  <th> Application ID </th>
  <th> Core XML file </th>
</tr>
<tr>
  <td>`App`</td>
  <td> `home/owner/apps_rw/<Package ID>` <br>
  (For example: <br>
    `home/owner/apps_rw/qik37po9ck`) </td>
  <td> `<Package ID>.<Name>` <br>
  (For example: <br>
    `qik37po9ck.Sample`) </td>
  <td> `opt/share/packages/<Package ID>.xml` <br>
  (For example: <br>
    `opt/share/packages/qik37po9ck.xml`)
  </td>
</tr>
    </table>



### Hybrid Application Package <a name="hap"></a>

A hybrid application package must conform to the following conventions:

-   Package format and file extension
    -   File format: ZIP archive file format
    -   File extension: `.wgt` (for example, `sample.wgt`)
-   Package content
    -   File and folders: The root of the hybrid package is the path of
        the ZIP archive and contains reserved folders. The following
        table shows the content of a package.

        **Table: Package content**

<table>
<tr>
  <th>Name</th>
  <th>Type</th>
  <th>Description</th>
</tr>
<tr>
  <td>`bin`</td>
  <td>Folder</td>
  <td>Native application executable binary</td>
</tr>
<tr>
  <td>`data`</td>
  <td>Folder</td>
  <td>Web or native application private data</td>
</tr>
<tr>
  <td>`info`</td>
  <td>Folder</td>
  <td>Native application metadata</td>
</tr>
<tr>
  <td>`lib`</td>
  <td>Folder</td>
  <td>Native application libraries</td>
</tr>
<tr>
  <td>    `res`</td>
  <td> Folder </td>
  <td> Native application resources or Web application content</td>
</tr>
<tr>
  <td>    `res/wgt`</td>
  <td>Folder</td>
  <td> Web application project root</td>
</tr>
<tr>
  <td>    `res/wgt/index.html`</td>
  <td> File </td>
  <td>  Default HTML file for the Web application</td>
</tr>
<tr>
  <td>    `setting`   </td>
  <td>     Folder </td>
  <td>  Native application setting</td>
</tr>
<tr>
  <td>    `shared`  </td>
  <td>   Folder  </td>
  <td> Native application shared resources</td>
</tr>

</table>



-   Directory hierarchy (after installation on device)

    The following figure and table illustrate the hybrid application
    package directory structure.

    **Figure: Hybrid application directory structure**

    ![Hybrid application directory
    structure](./media/hybrid-app-package-manager.png)

    **Table: Hybrid application package structure**

<table>
<tr>
  <th>Package  </th>
  <th>Root directory  </th>
  <th>Application ID  </th>
  <th> Core XML file     </th>
</tr>
<tr>
  <td> `App1`<br>(Web) </td>
  <td> `home/owner/apps_rw/<Package ID>` <br>
  (For example:  <br>
    `home/owner/apps_rw/qik37po9ck`)   </td>
  <td>`<Package ID>.<Name>`     <br>
   (For example:  <br>
     `qik37po9ck.Sample`)    </td>
  <td>`opt/share/packages/<Package ID>.xml`        <br>
  (For example: <br>
    `opt/share/packages/qik37po9ck.xml`)  </td>
</tr>
<tr>
  <td> `App2` <br> (Native)  </td>
  <td>  Same as for `App1`</td>
  <td> `<Package ID>.<ExecutableName1>`<br>
   (For example:<br>
     `qik37po9ck.Service`)  </td>
  <td> Same as for `App1`</td>
</tr>
<tr>
  <td> `App3` <br> (Native)   </td>
  <td> Same as for `App1` </td>
  <td> `<Package ID>.<ExecutableName2>` <br>
  (For example: <br>
     `qik37po9ck.Downloader`)     </td>
  <td> Same as for `App1`</td>
</tr>
</table>
