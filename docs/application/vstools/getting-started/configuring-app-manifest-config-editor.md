# Manifest & Config Editor

## Manifest Editor

Tizen application project includes a manifest file named **tizen-manifest.xml**, which defines essential application details such as version, privileges, and other metadata. This file follows an XML structure with a root **&lt; manifest &gt;** element and various child elements that describe application attributes.

### Methods to Edit the Manifest File

There are two ways to edit the tizen-manifest.xml file:

1. **Using the Manifest Editor** (Recommended)
<br>The Manifest Editor provides a structured form-based interface for modifying the manifest without editing raw XML.<br>Steps:
    1. In **Solution Explorer**, locate **tizen-manifest.xml**.
    2. **Double-click** the file to open it in the **Manifest Editor**.
    3. Modify the necessary fields in the form.
    4. Save the changes (Ctrl + S).

<img alt="Manifest Editor" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_manifest_editor_1.png" />
<p></P>

2. **Using the XML (Text) Editor**
<br>The  editor allows direct modifications to the manifest’s raw XML structure.<br>Steps: 
    1. In **Solution Explorer**, right-click **tizen-manifest.xml**.
    2. Select Open with **XML (Text) Editor**.
    3. Make necessary changes to the XML elements.
    4. Ensure the file maintains valid XML syntax and follows Tizen’s application specifications.
    5. Save the changes (Ctrl + S).

<img alt="XML Editor" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_manifest_editor_2.png" />
<p></P>

**⚠ Caution:** Editing XML directly is recommended only for advanced users.Incorrect modifications can lead to validation errors or installation failures.

## Config Editor
In **Tizen Web** applications, the **config.xml** file acts as the configuration file, defining essential application settings such as name, icons, content, permissions, and required features. This XML file follows the **W3C Widget Specification** and includes **Tizen-specific elements**.

### Editing the config.xml File

In **Visual Studio**, you can modify config.xml in raw XML structure.

Steps:
1. In **Solution Explorer**, locate **config.xml**.
2. **Double-click** the file to open it.
3. Modify the necessary fields.
4. Ensure the XML structure remains valid.
5. Save the changes (Ctrl + S).

<img alt="Config Editor" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_config_editor.png" />
<p></P>

**Structure of config.xml**
<br>Below is an example of a config.xml file for a Tizen Web application:

```

<?xml version="1.0" encoding="UTF-8"?>
<widget xmlns="http://www.w3.org/ns/widgets" xmlns:tizen="http://tizen.org/ns/widgets" id="http://yourdomain/TizenWeb" version="1.0.0" viewmodes="maximized">
   <name>TizenWeb</name>
   <icon src="icon.png"></icon>
   <content src="index.html"></content>
   <feature name="http://tizen.org/feature/screen.size.all"></feature>
   <tizen:application id="xcp8d1FyB6.TizenWeb" package="xcp8d1FyB6" required_version="9.0"></tizen:application>
   <tizen:profile name="tizen"></tizen:profile>
</widget>

```
**Key Elements:**

 - **&lt; widget &gt;**: Root element defining the widget (application).
 - **&lt; name &gt;**: Defines the application name displayed to users.
 - **&lt; icon &gt;**: Specifies the app’s icon file.
 - **&lt; content &gt;**: Defines the main HTML file (index.html) for launching the app.
 - **&lt; feature &gt;**: Declares hardware or software features the app requires (e.g., screen size).
 - **&lt; tizen:application &gt;**: Specifies the app’s ID, package name, and required Tizen version.
 - **&lt; tizen:profile &gt;**: Defines the Tizen profile the app is built for.