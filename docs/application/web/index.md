
# Tizen Web Application

The [Tizen Studio](../tizen-studio/index.md) enables you to create Web applications for mobile, wearable, and TV devices. A Web application consists of HTML, JavaScript, and CSS combined in a package, which can be installed on the Tizen device.  

A [Web application package](./tutorials/process/app-dev-process.md#package) includes all the support files that are needed by the Web application.
Therefore, a Web application can run without any additional external resources or network connectivity after installation.

The application model supports a rich set of standard W3C/HTML5 features, which include various JavaScript APIs as well as additional
HTML markups and CSS features. These features, along with the Tizen Device APIs and UI framework support, can be used to create rich Web
applications in a variety of categories, such as contacts, messaging, device information access, multimedia, graphics, and games.

Tizen supports both [Web application packages](#wap) and [hybrid application packages](#hap), which combine a Web application and 1 or
more native service applications.

Applications in the same package follow the same installation life-cycle, handled by the [application package manager](#package).

<a name="package"></a>
## Application Package Manager

The application package manager is one of the core modules of the Tizen application framework, and is responsible for installing, uninstalling, and updating packages, and storing their information. Using the package manager, you can also retrieve information related to the packages that are installed on the device.

The application package manager module is expandable to support various types of applications, and designated installation modules can be added to it.

**Figure: Application package manager**

![Application package
manager](./media/application_package_manager.png)

<a name="config"></a>
### Web Package Configuration

Each Web application package has a configuration file, `config.xml`, which indicates a packaging format and metadata for the application.

The Tizen Web application must follow the guidelines of [W3C Widget Packaging and XML Configuration](https://www.w3.org/TR/2011/REC-widgets-20110927/) and
Tizen extended configuration (in [mobile](../tizen-studio/web-tools/config-editor.md#mw_extend)
and
[wearable](../tizen-studio/web-tools/config-editor.md#ww_extend) applications).

For more information on the configuration elements, see [Configuration Element Hierarchy](../tizen-studio/web-tools/config-editor.md#hierarchy).

<a name="wap"></a>
### Web Application Package

The Tizen platform supports Web applications based on HTML, JavaScript, and CSS, and packaged according to the W3C specification. The platform also provides device APIs to access the platform capabilities, enabling a rich Web application development environment.

A Web application package must conform to the following conventions:

- Package format and file extension
    - File format: ZIP archive file format
    - File extension: `.wgt` (for example, `sample.wgt`)
    - MIME type: `application/widget`
- Application ID
    - The application ID cannot be changed after the application is published.
- Package content
    - File and folders: The root of the Web package is the path of the     ZIP archive and contains files and folders, some of which are reserved. The following table shows the content of a package.

    **Table: Package content**

  | Name | Type | Description |
  |-----|-------|--------|
  | `config.xml` |File | Application configuration document |
  | `icon.gif` | File  | Application default icon |
  | `icon.ico` | File  | Application default icon |
  | `icon.jpg`| File | Application default icon |
  | `icon.png` | File  | Application default icon |
  | `icon.svg` | File  | Application default icon |
  | `index.html` | File  |  Application default start file |
  | `index.htm`   | File  |  Application default start file |
  | `index.svg`  | File  |  Application default start file |
  | `index.xhtml`  | File  | Application default start file |
  | `index.xht`   | File  | Application default start file |
  | `locales`  | Folder | Container for localized content |

- Directory hierarchy (after installation on device)

    The following figure and table illustrate the Web application package directory structure.

    **Figure: Web application directory structure**

    ![Web application directory structure](./media/web_app_directory_structure.png)

    **Table: Web application package structure**

  |  Package | Root directory | Application ID | Core XML file |
  |-----|-----|-----|-----|
  | `App` | `home/owner/apps_rw/<Package ID>` <br> (For example:<br> `home/owner/apps_rw/qik37po9ck`) | `<Package ID>.<Name>`<br> (For example:<br>   `qik37po9ck.Sample`) | `opt/share/packages/<Package ID>.xml` <br> (For example: <br>    `opt/share/packages/qik37po9ck.xml`) |

<a name="hap"></a>
### Hybrid Application Package

A hybrid application package must conform to the following conventions:

- Package format and file extension
  - File format: ZIP archive file format
  - File extension: `.wgt` (for example, `sample.wgt`)
- Package content
  - File and folders: The root of the hybrid package is the path of   the ZIP archive and contains reserved folders. The following     table shows the content of a package.


  **Table: Package content**

 | Name  | Type | Description |
 |-----|-----|------|
 | `bin` | Folder | Native application executable binary |
 | `data` | Folder | Web or native application private data |
 | `info` | Folder |Native application metadata |
 | `lib` |Folder|Native application libraries |
 | `res`| Folder | Native application resources or Web application content |
 | `res/wgt`|Folder| Web application project root|
 | `res/wgt/index.html`| File |  Default HTML file for the Web application |
 | `setting`   |     Folder |  Native application setting |
 | `shared` |   Folder | Native application shared resources |

- Directory hierarchy (after installation on device)

    The following figure and table illustrate the hybrid application package directory structure.

    **Figure: Hybrid application directory structure**

    ![Hybrid application directory structure](./media/hybrid_app_package_manager.png)

    **Table: Hybrid application package structure**

  | Package | Root directory | Application ID | Core XML file    |
  |-----|-----|-----|-----|
  | `App1`<br>(Web) |  `home/owner/apps_rw/<Package ID>` <br> (For example:  <br>    `home/owner/apps_rw/qik37po9ck`)  |  `<Package ID>.<Name>`     <br>   (For example:  <br> `qik37po9ck.Sample`)    |  `opt/share/packages/<Package ID>.xml`        <br>  (For example: <br> `opt/share/packages/qik37po9ck.xml`)  |
  |  `App2` <br> (Native) |   Same as for `App1` |   `<Package ID>.<ExecutableName1>`<br>   (For example:<br>     `qik37po9ck.Service`)  |   Same as for `App1` |
  |   `App3` <br> (Native) |  Same as for `App1` |   `<Package ID>.<ExecutableName2>` <br>  (For example: <br>     `qik37po9ck.Downloader`)     |  Same as for `App1` |
