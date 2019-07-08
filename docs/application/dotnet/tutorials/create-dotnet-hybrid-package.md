# Packaging a .NET and Web Hybrid Application

Tizen Platform allows you to create hybrid application packages to combine .NET application and Web application.

You can develop the .NET application using Visual Studio and Web application using Tizen Studio. Therefore, you cannot create a hybrid application package using the existing project connection method provided by Tizen Studio.

Therefore, you can create a hybrid application package by merging Web application and .NET application packages. You can merge using the CLI tool provided in Tizen Studio:
(Currently, only command-line interface is provided for .NET and Web hybrid application package.)

**Figure: Create .NET and Web Hybrid Application Package**

![.NET Hybrid Packaging](./media/net_hybrid_packaging_cs.png)

The Web application package (wgt) file that contains the Web Widget application and the Web UI application, is created with the same .NET and Web hybrid application package.

The .NET and Web hybrid application package follows the same conventions, which are defined for [Web and Native hybrid application package](../../web/index.md#hybrid-application-package).

The .NET and Web hybrid application package is a type of a merge between a .NET application based on a Web application. Therefore, the Package ID of the Web application generates the Package ID for the hybrid application.

Use the following command to create hybrid application packages:

```bash
$[TIZEN_STUDIO_DIR]/tools/ide/bin$ ./tizen package -t wgt -s [CERTIFICATE_PROFILE_NAME] -r [TPK_FILE_PATH] -- [WGT_FILE_PATH]
```

>**Note**
>
>`[CERTIFICATE_PROFILE_NAME]` means certificate profile name not certificate file name.

## Example

1. Create Web Widget Sample Application

    ![Create Web Widget 1](./media/create_web_sample_cs_1.png)

    ![Create Web Widget 2](./media/create_web_sample_cs_2.png)

    ![Create Web Widget 3](./media/create_web_sample_cs_3.png)

    ![Create Web Widget 4](./media/create_web_sample_cs_4.png)

2. Check manifest file of web application

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <widget xmlns="http://www.w3.org/ns/widgets" xmlns:tizen="http://tizen.org/ns/widgets" id="http://yourdomain/WorldClockWidget" version="1.0.0" viewmodes="maximized">
        <access origin="*" subdomains="true"></access>
        <tizen:app-widget id="TestHybrid.WorldClockWidget.WorldClockWidget" primary="true">
            <tizen:widget-label>World Clock Widget</tizen:widget-label>
            <tizen:widget-content src="widget/Widget/index.html">
                <tizen:widget-size preview="widget/Widget/preview.png">2x2</tizen:widget-size>
            </tizen:widget-content>
        </tizen:app-widget>
        <tizen:application id="TestHybrid.WorldClockWidget" package="TestHybrid" required_version="2.3.2"/>
        <content src="index.html"/>
        <feature name="http://tizen.org/feature/screen.size.all"/>
        <icon src="icon.png"/>
        <name>WorldClockWidget</name>
        <tizen:privilege name="http://tizen.org/privilege/application.launch"/>
        <tizen:profile name="wearable"/>
    </widget>
    ```
    package id of web application is set like below :
     __*package="TestHybrid"*__

3. Create .NET Sample Application

    ![Create .NET App 1](./media/create_dotnet_sample_cs_1.png)

    ![Create .NET App 2](./media/create_dotnet_sample_cs_2.png)

4. Check manifest of .NET application

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns="http://tizen.org/ns/packages" api-version="4" package="org.tizen.example.CrossTemplate1.Tizen" version="1.0.0">
    <profile name="common" />
    <ui-application appid="org.tizen.example.CrossTemplate1.Tizen"
                    exec="CrossTemplate1.Tizen.dll"
                    type="dotnet"
                    multiple="false"
                    taskmanage="true"
                    nodisplay="false"
                    launch_mode="single">
    <label>CrossTemplate1.Tizen</label>
    <icon>CrossTemplate1.Tizen.png</icon>
    </ui-application>
    </manifest>  
    ```

    package id of .NET application is set like below :
    __package="org.tizen.example.CrossTemplate1.Tizen"__

5. Create hybrid package with CLI tool

    ```bash
    /home/test/tizen-studio/tools/ide/bin$ ./tizen package -t wgt -s test_cert_profile -r /home/test/hybrid/org.tizen.example.CrossTemplate1.Tizen-1.0.0.tpk – /home/test/hybrid/WebWidgetSample.wgt

    Author certficate: /home/test/tizen-studio-data/keystore/author/test_cert_profile.p12
    Distributor1 certificate : /home/test/tizen-studio/tools/certificate-generator/certificates/distributor/sdk-partner/tizen-distributor-signer.p12
    Package( /home/test/hybrid/WebWidgetSample.wgt ) is created successfully.
    ```

    > **Note**
    >
    > Newly generated hybrid application package file overrides previous web application package file.

6. Check created manifest file in the WebWidgetSample.wgt file.

    You can find the package name is changed from `org.tizen.example.CrossTemplate1.Tizen` to `TestHybrid`

    ```xml
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <widget xmlns="http://www.w3.org/ns/widgets" xmlns:tizen="http://tizen.org/ns/widgets" id="http://yourdomain/WorldClockWidget" version="1.0.0" viewmodes="maximized">
        <access origin="*" subdomains="true"/>
        <tizen:app-widget id="TestHybrid.WorldClockWidget.WorldClockWidget" primary="true">
            <tizen:widget-label>World Clock Widget</tizen:widget-label>
            <tizen:widget-content src="widget/Widget/index.html">
                <tizen:widget-size preview="widget/Widget/preview.png">2x2</tizen:widget-size>
            </tizen:widget-content>
        </tizen:app-widget>
        <tizen:application id="TestHybrid.WorldClockWidget" package="TestHybrid" required_version="2.3.2"/>
        <content src="index.html"/>
        <feature name="http://tizen.org/feature/screen.size.all"/>
        <icon src="icon.png"/>
        <name>WorldClockWidget</name>
        <tizen:privilege name="http://tizen.org/privilege/application.launch"/>
        <tizen:profile name="wearable"/>
    </widget>
    ```
