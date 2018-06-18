# Service Application

A service application is a type of Tizen Web application that provides an environment for running JavaScript in the background without a graphical user interface (the application follows the [ECMA-262 specification](http://www.ecma-international.org/publications/standards/Ecma-262.htm)). The service application is used to perform tasks that need to run periodically or continuously, but do not require any user interaction. For example, a service application can be used for getting data or listening for platform events in the background. As service applications do not have UI components, they run on top of a more light-weight runtime than UI applications. Therefore, you can expect them to perform better and consume less memory.

> **Note**  
> This feature is supported in TV applications only. The Web service application is an optional feature, which means that it may not be supported on all TV devices. You can check the device capability by using the `getCapability()` method of the [SystemInfo](../../api/latest/device_api/tv/tizen/systeminfo.html#SystemInfo) interface. For more information, see [Application Filtering](../../tutorials/app-filtering.md).

The main features of the service application include:

- Managing the life-cycle

  To manage a service application life-cycle, you must [define various callbacks](#create) to enable the application to be initialized and handle incoming requests.

  While the service application is running, you can [use the supported Web Device APIs](#fund) to interact with the platform or other service applications.

- Packaging applications

  You must always [package a service application](#package) with a UI application in a Web application package file. You can include multiple service applications in the same package with a single UI application.

- Launching applications

  You can [launch service applications](#launch) through another application by using the `launch()` and `launchAppControl()` methods of the [Application](../../api/latest/device_api/tv/tizen/application.html) API by using an explicit application ID. You can also register service applications to be launched automatically at boot time.

- Terminating applications

  The service application can [terminate itself](#terminate) when it receives a certain request.

The device main menu does not contain any icons for service applications, because the applications run in the background. The task switcher does not show them either. Service applications can run simultaneously with other service and UI applications.

> **Note**  
> The TV service application requires [partner-level certification](../../tutorials/sign-certificate.md) in Tizen 3.0.

## Prerequisites

To enable your application to use the service application functionality:

1. To make your application visible in the Tizen Store only for devices that support the Web service application, the application must specify the following feature in the `config.xml` file:

   ```
   <widget>
      <tizen:feature name="http://tizen.org/feature/web.service"/>
   </widget>
   ```

2. To ensure that a service application is acknowledged by the platform, you must add a service application extension element (`<tizen:service>`) to the `config.xml` file of the application:

   ```
   <widget>
      <tizen:service id="[App_ID]" auto-restart="true" on-boot="true">
         <tizen:content src="[Start_JS_File]"/>
         <tizen:name>[App_Name]</tizen:name>
         <tizen:icon src="[App_Icon]"/>
         <tizen:description>[Description]</tizen:description>
      </tizen:service>
   </widget>
   ```

   The `<tizen:service>` element is a child of the `<widget>` element in the `config.xml` file. With the `<tizen:service>` element attributes, you can set the traits of a service application, such as application ID, auto restart, and boot launching capability. With the `<tizen:service>` child elements, you can set the starting script, name, and icon for the service application.  

   The definition of all service elements is listed and explained in the [Extending Configuration Elements](../../../tizen-studio/web-tools/config-editor.md#ww_extend).

3. To use the [Application](../../api/latest/device_api/mobile/tizen/application.html) API, the application has to request permission by adding the following privilege to the `config.xml` file:

   ```
   <tizen:privilege name="http://tizen.org/privilege/application.launch"/>
   ```

> **Note**  
> No privileges need to be separately defined for service applications, since the service application is always packaged with a UI application, and a privilege defined for the UI application covers the entire application package.

<a name="create"></a>
## Managing the Service Application Life-cycle

To run a service application, you must export a number of callbacks using the [CommonJS Modules](http://wiki.commonjs.org/wiki/Modules/1.1) API. The callbacks need to be added to the `module.exports` object, which is provided by the environment. The following callbacks are called when there are life-cycle changes or application control events which are triggered by the application management framework:

- `onStart()`: The entry point of the service. It is called after the service runtime finishes the set-up.
- `onRequest()`: The listener for application control callbacks. It is provided to handle requests from other applications. You can understand the intention of the request and reply to it using the `tizen.application.getCurrentApplication().getRequestedAppControl()` method. This callback is also called when the application is first launched as an application launch is considered to be a request as well.
- `onExit()`: This is called when the [service ends](#terminate). You can release resources or save the context by using this callback.

**Figure: State transitions**

![State transitions](./media/service_app.png)

Learning how to manage service application callbacks is a basic application management skill:

1. Create the service entry point with the `onStart()` callback.

   The callback is invoked when the service is launched. Within the callback, you can prepare resources and initialize whatever the service application needs during the execution.

   ```
   module.exports.onStart = function() {
       console.log('service start');

       var remoteMsgPort = tizen.messageport.requestRemoteMessagePort('websvcapp0.WebServiceApplication', 'SERVICE_SAMPLE1');
       var localMsgPort = tizen.messageport.requestLocalMessagePort('SERVICE_SAMPLE2');

       function onreceived(data, remoteMsgPort) {
           for (var i = 0; i < data.length; i++) {
               if (data[i].value == 'SERVICE_EXIT') {
                   localMsgPort.removeMessagePortListener(watchId);
                   tizen.application.getCurrentApplication().exit();
               }
           }
       }
       var watchId = localMsgPort.addMessagePortListener(onreceived);
   }
   ```

2. Write the request handler with the `onRequest()` callback.

    The callback is invoked to handle incoming service requests. Within the callback, write code for each request from other applications and the platform. To obtain the request, use the `getRequestedAppControl()` method in the [Application](../../api/latest/device_api/tv/tizen/application.html) API.

   ```
   module.exports.onRequest = function() {
       var reqAppControl = tizen.application.getCurrentApplication().getRequestedAppControl();
       if (reqAppControl) {
           if (reqAppControl.appControl.operation == 'http://tizen.org/appcontrol/operation/service') {
               try {
                   tizen.systeminfo.addPropertyValueChangeListener('DEVICE_ORIENTATION', onDeviceOrientationSuccess);
               }
           }
       }
   }
   ```

3. Write the termination with the `onExit()` callback.

    The callback is invoked when the service is about to be stopped. All resources can be cleared and backed up within the callback.

   ```
   module.exports.onExit = function() {
       console.log('service terminate');
   }
   ```

<a name="package"></a>
## Packaging a Service Application

A Web application package can contain 1 Web UI application and several service applications. Each application in the Web application package shares the same package ID and has a unique application ID. In the following example, you can use the `<tizen:application>` element to define information for the Web UI application. The `<tizen:service>` element is used to define information about the service application. The UI application and the service application have the same package ID and different application IDs.

The Web application package file is installed, updated, and uninstalled as a single [package](../../index.md#package), making the life-cycles of the service applications and the UI application synchronous.

To package the service application with a UI application, define the service in the `config.xml` file. The `<tizen:service>` element allows you to define the characteristics of the service application. For example, you can specify the name, icon, and starting JavaScipt file of the service application.

```
<?xml version="1.0" encoding="TF-8"?>
<widget xmlns="http://www.w3.org/ns/widgets" xmlns:tizen="http://tizen.org/ns/widgets"
        id="http://yourdomain/WebServiceApplication" version="1.0.0" viewmodes="maximized">
   <tizen:application id="websvcapp0.WebServiceApplication" package="websvcapp0" required_version="3.0"/>
   <content src="index.html"/>
   <feature name="http://tizen.org/feature/screen.size.all"/>
   <icon src="icon.png"/>
   <name>WebServiceApplication</name>
   <tizen:service id="websvcapp0.service1" auto-restart="true" on-boot="false">
      <tizen:content src="service/service1.js"/>
      <tizen:name>WebServiceApplication1</tizen:name>
      <tizen:icon src="icon1.png"/>
      <tizen:description>WebServiceApplication1</tizen:description>
   </tizen:service>
</widget>
```

<a name="launch"></a>
## Launching a Service Application

Learning how to launch a service application is a basic application management skill:

- Launch by other applications

  The Web application launches a service application by calling the `launch()` or `launchAppControl()` method with the service application ID:

  ```
  tizen.application.launchAppControl(new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/service'), 'websvcapp0.service1', function() {
      console.log('Launch Service succeeded');
  }, function(e) {
      console.log('Launch Service failed: ' + e.message);
  });
  ```

- Launch by the system

  A service application can start automatically if the `on-boot` attribute is set to `true`. This requires partner-level certification.

  ```
  <tizen:service id="websvcapp0.service1" on-boot="true">
  ```

<a name="terminate"></a>
## Terminating a Service Application

Learning how to terminate a service application is a basic application management skill:

1. The service application can terminate itself when it receives a particular request. The following example code uses the [Message Port](../../api/latest/device_api/tv/tizen/messageport.html) API to send such a request to the service application.

   The application sends a message by calling the `sendMessage()` method.

   ```
   var remoteMsgPort = tizen.messageport.requestRemoteMessagePort('websvcapp0.service1', 'SERVICE_SAMPLE2');
   remoteMsgPort.sendMessage([{key: 'key', value: 'SERVICE_EXIT'}]);
   ```

2. The service application can terminate itself by calling the `exit()` method after getting a signal through the message port:

   ```
   var localMsgPort = tizen.messageport.requestLocalMessagePort('SERVICE_SAMPLE2');
   function onreceived(data, remoteMsgPort) {
       for (var i = 0; i < data.length; i++) {
           if (data[i].value == 'SERVICE_EXIT') {
               localMsgPort.removeMessagePortListener(watchId);
               tizen.application.getCurrentApplication().exit();
           }
       }
   }
   var watchId = localMsgPort.addMessagePortListener(onreceived);
   ```

<a name="fund"></a>
## Supported APIs for Service Applications

You can use a selection of the following Tizen TV Web Device APIs to interact with the platform or other service applications. More Device APIs for service applications are supported in the next release.

**Table: Supported APIs**

| API                                      | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Tizen](../../api/latest/device_api/tv/tizen/tizen.html) | The base object for accessing the Tizen TV Web Device APIs. |
| [Alarm](../../api/latest/device_api/tv/tizen/alarm.html) | This API provides methods for setting and unsetting alarms. |
| [Application](../../api/latest/device_api/tv/tizen/application.html) | This API provides information about the currently-running and installed applications and ways to launch other applications.<br>Note that the `getRequestedAppControl()` method is only valid inside the `onRequest()` callback. |
| [Package](../../api/latest/device_api/tv/tizen/package.html) | This API provides methods to install and uninstall Tizen packages and to get information about installed packages. |
| [Filesystem](../../api/latest/device_api/tv/tizen/filesystem.html) | This API provides methods to access the file system of a device and to read, write, copy, move, and delete files. |
| [Message Port](../../api/latest/device_api/tv/tizen/messageport.html) | This API provides methods for an application to communicate with other applications. |
| [System Information](../../api/latest/device_api/tv/tizen/systeminfo.html) | This API provides information about the device's display, network, storage, and other capabilities. |

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for TV
