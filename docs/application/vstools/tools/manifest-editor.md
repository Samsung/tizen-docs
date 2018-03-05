# Manifest Editor

A Tizen .NET application project contains a manifest file, called `tizen-manifest.xml`, which is used to describe the application information. The manifest file is composed of XML elements, which include the root [`<manifest>`](#manifest) element and its child elements representing application information, such as `<version>`, and `<privileges>`. The [child elements are organized into a specific hierarchy](#hierarchy). The elements can have attributes associated with them, providing more information on the element.

<a name="editing"></a>
## Editing the Manifest File
There are 2 different ways to edit the `tizen-manifest.xml` file:

- Use the Manifest Editor to modify the manifest in a form editor:

  Double-click the `tizen-manifest.xml` file in the **Solution Explorer** view.

  **Figure: Manifest Editor**

  ![Manifest Editor](./media/manifest-overview.png)

- Use the text editor to modify the XML structure directly:

  1. Right-click the `tizen-manifest.xml` file in the **Solution Explorer** view.
  2. Select **Open with &gt; XML (Text) Editor**.

  **Figure: Text editor**

  ![Text editor](./media/manifest-text-editor.png)

> **Note**
>
> The `tizen-manifest.xml` file must conform to both the standard XML file format and the Tizen .NET application specification requirements. Editing the manifest file XML structure with the text editor is intended for advanced users only. If the file does not conform to the standard and the requirements, errors can occur during installation.


<a name="hierarchy"></a>
## Manifest Element Hierarchy

The Tizen .NET application manifest file consists of XML elements organized in a hierarchy. The following tree structure shows the relationship between the elements of the `tizen-manifest.xml` file.

| `<manifest>` |                                   |                          |                  |
|--------------|-----------------------------------|--------------------------|------------------|
|              | `<author>`                        |                          |                  |
|              | `<description>`                   |                          |                  |
|              | `<profile>`                       |                          |                  |
|              | `<ui-application>`                |                          |                  |
|              |                                   | `<label>`                |                  |
|              |                                   | `<icon>`                 |                  |
|              |                                   | `<app-control>`          |                  |
|              |                                   | `<metadata>`             |                  |
|              |                                   | `<datacontrol>`          |                  |
|              |                                   |                          | `<privilege>`    |
|              |                                   | `<background-category>`  |                  |
|              |                                   | `<splash-screens>`       |                  |
|              |                                   |                          | `<splash-screen>`|
|              | `<watch-application>`             |                          |                  |
|              |                                   |  `<label>`               |                  |
|              |                                   |  `<icon>`                |                  |
|              | `<widget-application>`            |                          |                  |
|              |                                   |  `<icon>`                |                  |
|              |                                   |  `<label>`               |                  |
|              |                                   |  `<support-size>`        |                  |
|              |                                   |  `<widget-class>`        |                  |
|              |                                   |                          | `<icon>`         |
|              |                                   |                          | `<label>`        |
|              |                                   |                          | `<support-size>` |
|              | `<shortcut-list>`                 |                          |                  |
|              |                                   | `<shortcut>`             |                  |
|              |                                   |                          | `<icon>`         |
|              |                                   |                          | `<label>`        |
|              | `<account>`                       |                          |                  |
|              |                                   | `<account-provider>`     |                  |
|              |                                   |                          | `<icon>`         |
|              |                                   |                          | `<label>`        |
|              |                                   |                          | `<capability>`   |
|              | `<privileges>`                    |                          |                  |
|              |                                   | `<privilege>`            |                  |
|              |                                   | `<appdefined-privilege>` |                  |
|              | `<provides-appdefined-privileges>`|                          |                  |
|              |                                   | `<appdefined-privilege>` |                  |
|              | `<feature>`                       |                          |                  |


<a name="manifest"></a>
## Manifest Elements

The following sections summarize the elements used in the `tizen-manifest.xml` file of a Tizen .NET application.

<a name="manifest_element"></a>
### &lt;manifest&gt; Element

This element contains the manifest information for a Tizen .NET application. The `<manifest>` element is an easily-readable description of the Tizen package and serves as a container for the other elements of the configuration document.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1

**Expected children (in the following order):**

| Child element           | Occurrences          |
|-------------------------|----------------------|
| `<author>`              | 1 (optional)         |
| `<description>`         | 1 or more (optional) |
| `<profile>`             | 1 or more (optional) |
| `<ui-application>`      | 1 (optional)         |
| `<watch-application>`   | 1 (optional)         |
| `<widget-application>`  | 1 (optional)         |
| `<shortcut-list>`       | 1 (optional)         |
| `<account>`             | 1 (optional)         |
| `<privileges>`          | 1 (optional)         |
| `<provides-appdefined-privileges>` |  1 (optional) |
| `<feature>`             | 1 or more (optional) |


**Attributes:**

- `api-version`

  API version number for the application (available value: number in the "x" format, for example, `4`)

- `install-location`

  Installation location for the application (available value: `"auto"`)

  > **Note**  
  > This attribute is read-only. Do not attempt to modify it.

- `package`

  Package of the application (available value: `"org.tizen.<PackageName>"`)

- `type`

  Package type of the application (available value: `"tpk"`)

  > **Note**  
  > This attribute is read-only. Do not attempt to modify it.

- `version`

  Version number of the application (available value: number in the "x.y.z" format, where 0 &lt;= x &lt;= 255, 0 &lt;= y &lt;= 255, and 0 &lt;= z &lt;= 65535)

**For example:**

```xml
<manifest xmlns="http://tizen.org/ns/packages" api-version="4" package="org.tizen.uiapp" version="1.0.0">
   <author>.....</author>
   <description>.....</description>
   <profile name="common"/>
   <ui-application>.....</ui-application>
   <shortcut-list>.....</shortcut-list>
   <account>.....</account>
   <privileges>.....</privileges>
   <provides-appdefined-privileges>.....</provides-appdefined-privileges>
   <feature>.....</feature>
</manifest>
```

<a name="author"></a>
### &lt;author&gt; Element

This element represents the creator of the Tizen package.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 (optional)

**Attributes:**

- `email`

  Email of the package creator (available value: any valid email ID string value)

- `href`

  Web site of the package creator, such as a homepage or a profile on a social network (available value: any valid Web site string value)

**Expected value:**

- Package creator name in string

**For example:**

```xml
<author email="email@email.com" href="http://test.com">author</author>
```

<a name="description"></a>
### &lt;description&gt; Element

This element contains an easily readable description of the Tizen package.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Attributes:**

- `xml:lang`

    Language and country code (available value: "&lt;2-letter lowercase language code (ISO 639-1)&gt;-&lt;2-letter lowercase country code (ISO 3166-1 alpha-2)&gt;")

**Expected value:**

- Description value in string

**For example:**

```xml
<description xml:lang="en-us">This is a sample</description>
```

<a name="profile_element"></a>
### &lt;profile&gt; Element

In a Tizen .NET application, the `<profile>` element must be set to `common`. This element has no child elements.

**Occurrences:**

- 1

**Attributes:**

-   `name`

    Profile name (available values: `common`, `mobile`, `tv`, `wearable`)

**For example:**

```xml
<profile name="common"/>
```

<a name="ui"></a>
### &lt;ui-application&gt; Element

This element contains the manifest information for a Tizen .NET UI application with a graphical user interface (GUI).

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Expected children (in the following order):**

| Child element           | Occurrences          |
|-------------------------| ---------------------|
| `<label>`               | 1 or more (optional) |
| `<icon>`                | 1 or more (optional) |
| `<app-control>`         | 1 or more (optional) |
| `<metadata>`            | 1 or more (optional) |
| `<datacontrol>`         | 1 or more (optional) |
| `<background-category>` | 1 or more (optional) |
| `<splash-screens>`      | 1 or more (optional) |

**Attributes:**

- `appid`  

  Application unique ID (string)  

  This can be used for launching or terminating the application explicitly.

- `exec`

  Application executable file path (string)

- `hw-acceleration`

  Indicates the application hardware acceleration status (available values: not defined (depends on the system setting), `on` (use hardware acceleration), `off` (do not use hardware acceleration))
  By default, this value is not defined.


- `launch_mode`

   Application launch mode (available values: `single` (launched as a main application), `group` (launched as a sub application), `caller` (caller application))

   By default, this value is set to `single`.

- `multiple`

  Indicates whether the application can be launched as a multiple (available values: `true`, `false`)
  > **Note**  
  > This attribute is read-only. Do not attempt to modify it.

- `nodisplay`

  Indicates whether the application is shown in the app tray (available values: `true`, `false`)

- `taskmanage`

  Indicates whether the application is shown in the task manager (available values: `true`, `false`)

- `type`

  Tizen application type (available values: `dotnet`)

  > **Note**  
  > This attribute is read-only. Do not attempt to modify it.

**For example:**

```xml
<ui-application appid="org.tizen.uiapp" exec="uiapp" hw-acceleration="on" launch_mode="single"
                multiple="false" nodisplay="false" taskmanage="true" type="dotnet">
   <label>uiapplication</label>
   <label xml:lang="en-gb">testlang</label>
   <icon>uiapp.png</icon>
   <app-control>
      <operation name="http://tizen.org/appcontrol/operation/dial"/>
      <mime name="application/vnd.ms-excel"/>
   </app-control>
   <metadata key="testkey" value="testvalue"/>
   <datacontrol access="ReadOnly"
                providerid="http://uiapp.com/datacontrol/provider/uiapp" type="Sql"/>
   <splash-screens>
      <splash-screen src="uiapp.jpg" type="img" dpi="hdpi" orientation="portrait" indicator-display="true"/>
   </splash-screens>
</ui-application>
```


<a name="watch_app"></a>
### &lt;watch-application&gt; Element

This element contains the settings for a watch application.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 (optional)

**Expected children:**

| Child element | Occurrences |
|---------------| ------------|
| `<label>`     | 1 or more   |
| `<icon>`      | 1 or more   |

**Attributes:**

-   `ambient-support`

    Indicates whether the application draws the ambient mode UI itself (available values: `true`, `false`)

    If the value is `false`, the system default ambient mode UI is shown when the device enters the ambient mode.

-   `appid`

    Watch application unique ID (string)

-   `exec`

    Watch application executable file path (string)

-   `type`

    Tizen application type (available value: `dotnet`)

```
<watch-application ambient-support="true" appid="org.tizen.watchsample" exec="watchsample.dll" type="dotnet">
   <label>.....</label>
   <icon>.....</icon>
</watch-application>
```

<a name="watch_label"></a>
#### &lt;label&gt; Element

This element contains the watch application text.

**Occurrences:**

-   1

**Expected value:**

-   Label value in string

**For example:**

```
<label>watchsample</label>
```

<a name="watch_icon"></a>
#### &lt;icon&gt; Element

This element contains the watch application icon image.

**Occurrences:**

-   1

**Expected value:**

-   Icon file name

```
<icon>watchsample.png</icon>
```

<a name="widget_app"></a>
### &lt;widget-application&gt; Element

This element contains the settings for a widget application.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

-   1 (optional)

**Expected children:**

|  Child element  |   Occurrences |
|-----------------|---------------|
|  `<label>`      |   1 or more   |
|  `<icon>`       |   1 or more   |
| `<support-size>`|   1      |
| `<widget-class>`|   1 or more (optional) |

**Attributes:**

-   `appid`

    Widget application unique ID (string)

-   `exec`

    Widget application executable file name (string)

-   `main`

    Indicates which widget application is the main application (available values: `true`, `false`)

-   `update-period`

    Indicates the update period in seconds (available values: time in seconds)

    Multiples of 1800 only allowed

-   `setup-appid`

    Widget application setup application ID (string)

-   `max-instance`

    Indicates the maximum number of widget instances that can be created in the widget application

**For example:**

```
<widget-application appid="org.tizen.test" exec="test" main="true" update-period="0" max-instance="5" setup-appid="org.tizen.widget-setting">
   <label>.....</label>
   <icon>.....</icon>
   <support-size>.....</support-size>
   <widget-class>.....</widget-class>
</widget-application>
```

<a name="widget_label"></a>
#### &lt;label&gt; Element

This element contains the widget application text.

**Occurrences:**

-   1 or more

**Expected value:**

-   Label value in string

**For example:**

```
<label>test</label>
```

<a name="widget_icon"></a>
#### &lt;icon&gt; Element

This element contains the widget application icon image.

**Occurrences:**

-   1 or more

**Expected value:**

-   Icon file name

**For example:**

```
<icon>icon.png</icon>
```

<a name="widget_supportsize"></a>
#### &lt;support-size&gt; Element

This element contains the size supported by the widget application.

**Occurrences:**

-   1

**Attributes:**

-   `preview`

    Relative path to the preview image (available values: file name)

    The image is shown on the home screen when the user tries to select the widget.

**Expected value:**

-   `2x2` (in mobile and wearable)
-   `4x1` (in mobile)
-   `4x2` (in mobile)
-   `4x3` (in mobile)
-   `4x4` (in mobile)

**For example:**

```
<support-size preview="preview.png">2x2</support-size>
```

<a name="widget_class"></a>
#### &lt;widget-class&gt; Element

This element contains the settings for the widget class. After adding this element, you can use the `widget_app_class_add()` function to create widget instances in the widget application (maximum number of instances is defined in the `max-instance` attribute of the `<widget-application>` element).

**Occurrences:**

-   1 or more (optional)

**Expected children:**

| Child element |   Occurrences |
|---------------|---------------|
| `<label>`     |     1 or more |
| `<icon>`      |     1 or more  |
| `<support-size>` |  1   |

**Attributes:**

-   `classid`

    Widget application class unique ID (string)

-   `update-period`

    Indicates the update period in seconds (available values: time in seconds)

    Multiples of 1800 only allowed

-   `setup-appid`

    Widget application setup application ID (string)

**For example:**

```
<widget-class classid="class1" update-period="0" setup-appid="org.tizen.widget-setting">
   <label>.....</label>
   <icon>.....</icon>
   <support-size>.....</support-size>
</widget-class>
```

<a name="shortcut-list"></a>
### &lt;shortcut-list&gt; Element

This element contains the shortcut template list used for adding a shortcut to the home screen.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 (optional)

**Expected children:**

| Child element | Occurrences |
|---------------| ------------|
| `<shortcut>`  | 1 or more   |

**For example:**

```xml
<shortcut-list>
   <shortcut>.....</shortcut>
</shortcut-list>
```

<a name="shortcut"></a>
#### &lt;shortcut&gt; Element

This element contains the information that indicates the shortcut for the application on the home screen.

**Occurrences:**

- 1 (optional)

**Expected children:**

| Child element | Occurrences |
|---------------|-------------|
| `<icon>`      | 1 or more   |
| `<label>`     | 1 or more   |

**Attributes:**

- `appid`

  Application unique ID (string)

  This can be used for launching or terminating the application explicitly.

- `extra_data`

  Data for user content (string)

  Shortcut element property in the manifest file.

- `extra_key`

  Key for user content (string)

  Shortcut element property in the manifest file.

**For example:**

```xml
<shortcut appid="org.example.shortcut" extra_data="data" extra_key="key">
   <icon>shortcut.png</icon>
   <label>shortcut</label>
   <label xml:lang="en-us">short</label>
</shortcut>
```
<a name="account"></a>
### &lt;account&gt; Element

This element contains a set of user accounts and account provider-related information for a Tizen application.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 (optional)

**Expected children:**

| Child element        | Occurrences |
|----------------------|-------------|
| `<account-provider>` | 1 or more   |

**For example:**

```xml
<account>
   <account-provider>.....</account-provider>
</account>
```
<a name="accountprovider"></a>
#### &lt;account-provider&gt; Element

This element contains specific service provider or user account protocol-related information.

**Expected children:**

| Child element  | Occurrences          |
|----------------|----------------------|
| `<icon>`       | 1 or more            |
| `<label>`      | 1 or more            |
| `<capability>` | 1 or more (optional) |

**Attributes:**

- `appid`

  Application unique ID (string)

  This can be used for launching or terminating the application explicitly.

- `multiple-accounts-support`

  Indicates whether multiple accounts are supported (available values: `true`, `false`)

- `providerid`

  ID of the account provider (string)

**For example:**

```xml
<account-provider appid="org.tizen.uiapp" multiple-accounts-support="false" providerid="org.tizen.uiapp">
   <icon>.....</icon>
   <label>.....</label>
   <capability>.....</capability>
</account-provider>
```

#### &lt;icon&gt; Element

This element contains the account provider icon image. Since the icons are used on the device under **Settings &gt; Accounts**, place them in a shared directory.

**Attributes:**

- `section`

  Usage information for the icon image (available values: `account` (image size: 72 x 72 for density xhigh and 48 x 48 for density high), `account-small` (image size: 45 x 45 for density xhigh and 30 x 30 for density high))

**Expected value:**

- Icon file name

**For example:**

```xml
<icon section="account">uiapp.png</icon>
<icon section="account-small">uiapp.png</icon>
```

<a name="capability"></a>
#### &lt;capability&gt; Element

This element contains the account provider capability. The capabilities are defined as `http://<VENDOR_INFORMATION>/account/capability/<NAME>`.

**Expected value:**

- IRI string

**For example:**

```xml
<capability>http://tizen.org/account/capability/calendar</capability>
```

<a name="privileges"></a>
### &lt;privileges&gt; Element

This element contains the set of required privileges for a Tizen application.

Applications that use sensitive APIs must declare the required privileges in the `tizen-manifest.xml` file.

Click **Add** to open the **Privileges** dialog.

**Figure: Editing the &lt;privileges&gt; element in the Manifest Editor**

![Editing the feature element in the Manifest Editor](media/vs_manifest_privileges.png)

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 (optional)

**Expected children:**

| Child element             | Occurrences          |
|---------------------------|----------------------|
| `<privilege>` | 1 or more (optional) |
| `<appdefined-privilege>` | 1 or more (optional) |

**For example:**

```xml
<privileges>
   <privilege>.....</privilege>
   <appdefined-privilege>.....</appdefined-privilege>
</privileges>
```

<a name="privilege"></a>
#### &lt;privilege&gt; Element

This element contains a required privilege for a Tizen application.

**Occurrences:**

- 1 or more (optional)

**Expected value:**

Name (mandatory, the URI of the Device API privilege)

For example:

- `http://tizen.org/privilege/application.admin`
- `http://tizen.org/privilege/appmanager.launch`
- `http://tizen.org/privilege/account.read`

For more information on the expected values, see [Security and API Privileges](../../native/tutorials/details/sec-privileges.md).

**For example:**

```xml
<privilege>http://tizen.org/privilege/application.admin</privilege>
<privilege>http://tizen.org/privilege/appmanager.launch</privilege>
<privilege>http://tizen.org/privilege/account.read</privilege>
```

<a name="appdefined-privilege"></a>
#### &lt;appdefined-privilege&gt; Element

This element is used to get the required access privileges provided by a consumer package.

**Occurrences:**

- 1 or more (optional)

**Attributes:**

- `license`

  Optional name of the license file used to verify the privilege

**Expected value:**

- Name (mandatory, the name of the app-defined privilege)

**For example:**

```xml
<appdefined-privilege license="example_license">
   http://{provider-pkgid}/appdefined/exampleprivilege1
</appdefined-privilege>
<appdefined-privilege>http://{provider-pkgid}/appdefined/exampleprivilege2</appdefined-privilege>
```

<a name="provides-appdefined-privileges"></a>
### &lt;provides-appdefined-privileges&gt; Element

This element specifies the app-defined access privileges provided by a provider package.

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 (optional)

**Expected children:**

| Child element                                      | Occurrences |
|----------------------------------------------------|----------------------|
| `<appdefined-privilege>` | 1 or more (optional) |

**For example:**

```xml
<provides-appdefined-privileges>
   <appdefined-privilege>.....</appdefined-privilege>
   <appdefined-privilege>.....</appdefined-privilege>
</provides-appdefined-privileges>
```
<a name="appdefined-privilege2"></a>
#### &lt;appdefined-privilege&gt; Element

This element is used to get the required access privileges provided by a provider package.

**Occurrences:**

-   1 or more (optional)

**Attributes:**

- `license`

  Optional name of the license file used to verify the privilege

**Expected value:**

- Name (mandatory, the name of the app-defined privilege)

**For example:**

```xml
<appdefined-privilege license="example_license">
   http://{provider-pkgid}/appdefined/exampleprivilege1
</appdefined-privilege>
<appdefined-privilege>http://{provider-pkgid}/appdefined/exampleprivilege2</appdefined-privilege>
```

<a name="feature"></a>
### &lt;feature&gt; Element

This element contains a list of required features for feature-based filtering in the Tizen Store.

The element is used to define the hardware and software components for the Tizen application. In order to use or access an API that is specialized for each vendor or platform, the feature must be declared. This element has no child elements.

**Figure: Editing the &lt;feature&gt; element in the Manifest Editor**

![Editing the feature element in the Manifest Editor](media/vs_manifest_features.png)

For more information on the relationship between the elements, see the [element hierarchy](#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Attributes:**

- `name`  (mandatory, a feature key URI)

  Item name used in feature-based filtering in the Tizen Store, for example, `"http://tizen.org/feature/camera"` or `"http://tizen.org/feature/fmradio"`

**Expected value:**

- `true`

**For example:**

```xml
<feature name="http://tizen.org/feature/camera">true</privilege>
<feature name="http://tizen.org/feature/fmradio">true</privilege>
```
