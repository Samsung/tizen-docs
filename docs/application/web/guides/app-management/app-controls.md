# Application Controls

You can use various application management features, including application launching, event handling, and information retrieval.

The Application API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main application management features are:

- Application management

  You can [manage applications](#managing-applications) by launching and stopping other applications, and hiding or exiting the current application.

- Application information retrieval

  You can display a list of applications that are currently installed or running on the device, and [retrieve application information](#retrieving-application-information), such as application name, application ID, and context ID.

- Application controls

  An application control (app control) is a way of sharing an application's functionality. Using another application's features through application controls reduces the time and effort needed to develop your own application.

  You can use in your application operations, such as calling, Web browsing, and playing media items, which are exported by other applications. This mechanism allows you to conveniently launch other applications whose functionalities you need in your application. If you need to use functionality from another application, launching an application control allows you to request the system to launch that application according to your requirements. You can launch applications based on your immediate needs - you do not need to know their identifiers or specifications. You can use application controls by creating an [application control request](#application-control-request). The request allows you to [launch other applications](#launching-applications-with-the-application-control) to use their functionalities.

  If you want to allow other applications to use your application functionalities, you must [export your application controls](#application-control-export) and be prepared to [receive requests and respond to them](#receiving-and-replying-to-application-control-requests).

- Event handling

  You can [send and receive events](#broadcasting-and-listening-for-events) between 2 applications using events. Your application can broadcast its own events, and listen for events broadcast by others.

- Background execution

  Usually, when a Web application moves to the background, it gets suspended. To enable [background execution](#background-execution), you must declare a background category for your application.

- Application status monitoring

  You can monitor the installed applications and [be notified when their status changes](#monitoring-the-application-status).

## Application Control Request

The application control can be used to describe either an action to be performed by other applications, or the results of the operation performed by a launched application. You can request other applications to perform specific operations using the `ApplicationControl` (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControl), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControl), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControl) applications) and `RequestedApplicationControl` (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#RequestedApplicationControl), [wearable](../../api/latest/device_api/wearable/tizen/application.html#RequestedApplicationControl), and [TV](../../api/latest/device_api/tv/tizen/application.html#RequestedApplicationControl) applications) interfaces. The operations can be, for example, making a phone call, browsing local files so the user can pick an image of their choosing, or playing a video in a video player.

The application control consists of an operation, URI, MIME type, and some data, and it describes the request to be performed by the newly launched application. This information is used to resolve the application control. When the system gets an application control request, it finds the proper provider application by resolving the application control, and then launches the provider application. Once the provider application has performed the requested task, it must pass control back to the calling application and provide the result of the operation. Basically, the application control process flows as follows:

1. The calling application launches the application control with the `launchAppControl()` method of the `Application` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#Application), [wearable](../../api/latest/device_api/wearable/tizen/application.html#Application), and [TV](../../api/latest/device_api/tv/tizen/application.html#Application) applications).
2. The provider application calls the `getRequestedAppControl()` method of the `Application` interface to get the reference of the `RequestedApplicationControl` object. This object contains the application control passed by the `launchAppControl()` method from the calling application.
3.  The provider application calls either the `replyResult()` method (on success) or the `replyFailure()` method (on failure) of the `RequestedApplicationControl` interface to return control back to the calling application. The result of the provided operation (if any), is delivered as an array of `ApplicationControlData` objects (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControlData), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControlData), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControlData) applications).
4. The calling application receives the result through the `ApplicationControlDataArrayReplyCallback` event handler (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControlDataArrayReplyCallback), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControlDataArrayReplyCallback), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControlDataArrayReplyCallback) applications).

The application control uses the following primary information:

- Application ID

  Used to identify the provider application of the requested application control. Besides the application ID, a [common application control](#common-application-controls) has a special alias name for the application ID with the prefix `tizen`. For example, the platform phone application has the alias application ID of `tizen.phone`.

  Used to identify the provider application of the requested application control.

  > **Note**  
  > Since Tizen 2.4, the platform-defined application controls and aliased application IDs which were defined in previous Tizen versions may not be supported. If they are used, the application control behavior is undefined and cannot be guaranteed.

- Operation

  Describes an action to be performed by the provider application. The operation ID of the platform-provided operation is in the `http://tizen.org/appcontrol/operation/<verb>` format. For example, `http://tizen.org/appcontrol/operation/view`.

  For more information on valid operations, see [Common Application Controls](common-appcontrols.md). You can also see which operations allow a URI to be specified and which MIME types an operation supports.

An application can be launched by the user from the Launcher or by another application. Each application has a launch mode, which determines how the application is launched: in a separate instance or in the same group as the calling application. For more information on the launch modes, see [Application Groups](./app-group.md).

There are different types of application control requests for [launching other applications](#launching-applications-with-the-application-control):

- [Explicit launch](#explicit-launch)  
   You determine which application must be launched by explicitly specifying an application ID. The application ID determines which application is launched and the application performs the operation as specified in the application control request.
- [Implicit launch](#implicit-launch)  
   You provide information to describe the request to be performed by the newly launched application without specifying the application ID. The system uses the information to resolve the application control. It does this by trying to find a proper application to perform the application control request and then launching the selected application.

You can take advantage of the Tizen [common application functionalities](#common-application-controls) through the application control feature. You can also [export your application functionality](#application-control-export) to allow other applications to launch your application.

### Explicit Launch

If you specify the exact application ID of the application for the `launchAppControl()` method of the `Application` interface, you can request the application control from a specific application. The application ID determines which application is launched and the application performs the operation as specified in the control request.

> **Note**  
> An explicit launch request cannot be completed if the user does not have the specified application on their device. Hence implicit launches can be more effective, because the system can find an available application to complete the request. The implicit launch can also enhance the user experience because it allows the user to select a preferred application to complete the task.

### Implicit Launch

If you do not explicitly provide an exact application ID with the application control request in the `launchAppControl()` method of the `Application` interface, you must provide enough information for the system to determine which of the available applications can best handle the control request. For example, the nature of the service or the file types that the application can handle.

The application control consists of an operation ID, URI, MIME type, some additional data, and a launch mode setting. The system compares some of the attributes of the control request against the service descriptions of the installed applications to determine which of the available applications are suitable for the request. The request is resolved only if all specified information matches the service descriptions retrieved from the installed applications. The application control `data` attribute is not used in resolving the control request.

The following attributes are used to resolve application control requests:

- Operation

  Mandatory string that defines the action to be performed by the application control. You can define your own operation to describe a specific action of your application.

- URI scheme

  Data on which the action is performed. For example, if you want to use the `http://tizen.org/appcontrol/operation/view` operation to view a specific image, the URI must be the URI of the image (which can be obtained using the `toURI()` method after resolving the file path). The same operation can be used to launch a Web page in a browser, except that the URI in that case is the URL of the Web site, such as `https://www.tizen.org/`.

- MIME type

  Specific type of the URI. For example, if you want to view only JPEG images, you must use the `image/jpeg` MIME type. The MIME type can be important because it ensures that the system finds an application that is capable of supporting a specified MIME type.

The following code example shows an `ApplicationControl` instance that launches an application to pick images:

```
var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/pick',
                                              null, 'image/*', null, null);

tizen.application.launchAppControl(appControl, null, successCb, errCb, null);
```

When you make an implicit launch request, there can be multiple applications that can fulfill the request. In that case, the system shows a pop-up which allows the user to select the application of their choice. If you want to select a specific application among the available applications that provide a specific operation, you can use the `findAppControl()` method of `Application` interface to search for applications which provide the functionalities that you need. The following code example demonstrates an explicit launch of an application to provide the image view operation that is found using the `findAppControl()` method:

```
/*
   Assuming that the filesystem virtual root 'images'
   has been resolved and saved in variable images
*/
var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/view',
                                              images.resolve('image12.jpg').toURI(),
                                              'image/*', null, null);

tizen.application.findAppControl(appControl, function(appInfos, appCtrl) {
    if (appInfos.length >= 1) {
        tizen.application.launchAppControl(appCtrl, appInfos[0].id, successCB, errCB, null);
    }
}, function(e) {
    /* Error handling */
});
```

### Common Application Controls

The Tizen common application controls specify a standard protocol for sharing application functionalities. You can use the common application controls to perform some basic tasks, such as selecting a file or taking a picture.

The following common application controls are available:

- [Browser](common-appcontrols.md#browser)
- [Calendar](common-appcontrols.md#calendar)
- [Call](common-appcontrols.md#call)
- [Camera](common-appcontrols.md#camera)
- [Contact](common-appcontrols.md#contact)
- [Email](common-appcontrols.md#email)
- [File Storage](common-appcontrols.md#file-storage)
- [Input Delegator](common-appcontrols.md#input-delegator)
- [Map](common-appcontrols.md#map)
- [Message](common-appcontrols.md#message)
- [Multimedia](common-appcontrols.md#multimedia)
- [System Settings](common-appcontrols.md#system-settings)
  * [Settings for Bluetooth](common-appcontrols.md#settings-for-bluetooth)
  *	[Settings for Location](common-appcontrols.md#settings-for-location)
  *	[Settings for NFC](common-appcontrols.md#settings-for-nfc)
  *	[Settings for Wi-Fi](common-appcontrols.md#settings-for-wi-fi)
- [Voice Recorder](common-appcontrols.md#voice-recorder)

## Application Control Export

Your application can export application control functionality. This means that the application can register itself as a provider application, allowing it to receive application control requests from other applications. You can [handle an incoming application control request](#receiving-and-replying-to-application-control-requests) using the `getRequestedAppControl()` method of the `Application` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#Application), [wearable](../../api/latest/device_api/wearable/tizen/application.html#Application), and [TV](../../api/latest/device_api/tv/tizen/application.html#Application) applications), and respond to the incoming request using the `RequestedApplicationControl` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#RequestedApplicationControl), [wearable](../../api/latest/device_api/wearable/tizen/application.html#RequestedApplicationControl), and [TV](../../api/latest/device_api/tv/tizen/application.html#RequestedApplicationControl) applications).

The system compares the attributes of the application control request against the service descriptions of installed applications to determine which of the available applications are suitable for the request. The service description of the installed applications contains information about the requests that they can handle. The request is resolved only if all specified information in the request matches with the service description retrieved from an installed application. The application control `data` attribute is not used in resolving the control request.

To advertise your application features to other applications, allow other applications to use the functionalities of your application, and launch your application implicitly without an application ID, you can define 1 or more application control service descriptions in the `config.xml` file of your application. Each description specifies the operation, URI scheme, and MIME type of the application control service your application can offer.

The following code example shows a service description which allows an application to handle requests to view JPEG images:

- The `src` field describes the application page (usually an HTML file) that handles the request.
- The `operation` field is mandatory, while the `uri` and `mime` fields are optional. If the value of `uri` field is `file`, the value can be left out.
- The `uri` field in the service description is used to inform the platform about how to interpret and process the rest of the URI. For example, the `http` URI scheme informs the platform to interpret and process the URI as a Web resource using HTTP. However, if the `uri` field value is set to `file`, leave the attribute out of the service description.

```
<tizen:app-control>
   <src name="view.html"/>
   <operation name="http://tizen.org/appcontrol/operation/view"/>
   <uri name="file"/>
   <mime name="image/jpeg"/>
</tizen:app-control>
```

For example, consider the following example of an `ApplicationControl` instance (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControl), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControl), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControl) applications):

```
/*
   Assuming that the filesystem virtual root 'images'
   has been resolved and saved in variable images
*/
var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/view',
                                              images.resolve('image12.jpg').toURI(),
                                              null, null, null);
```

When the system attempts to resolve the request and find the application to be launched, it checks the service descriptions. In the following example, the application with the first service description is not launched, since the `uri` information does not match the request. However, the application with the second service description is a match and can be launched:

```
<!--First service description: not a match-->
<tizen:app-control>
   <operation name="http://tizen.org/appcontrol/operation/view"/>
   <uri name="file"/>
   <mime name="image/*"/>
</tizen:app-control>

<!--Second service description: a match-->
<tizen:app-control>
   <operation name="http://tizen.org/appcontrol/operation/view"/>
   <mime name="image/*"/>
</tizen:app-control>
```

If your application offers the same service (operation) with different parameters (for example, different MIME types), you must define each set of parameters separately in their own service description. For example, if your application can handle both image and audio file MIME types with the view operation, 2 `<tizen:app-control>` elements with different MIME types and the same `http://tizen.org/appcontrol/operation/view` operation are required. The following example shows how to define the service descriptions for 2 MIME types for the same operation in the `config.xml` file:

```
<tizen:app-control>
   <operation name="http://tizen.org/appcontrol/operation/view"/>
   <mime name="image/*"/>
</tizen:app-control>

<tizen:app-control>
   <operation name="http://tizen.org/appcontrol/operation/view"/>
   <mime name="audio/*"/>
</tizen:app-control>
```

### Preventing Page Reloads for Incoming Requests

When a Web application receives an application control request from another application, the receiving application finds the proper page for that request and loads that page. If the found page is already loaded and displayed, the page is reloaded (refreshed) to process the incoming application control request. However, in some cases, a Web application is able to handle the application control request without reloading the page in order to keep the previous context.

Since Tizen 2.4, the Web runtime provides a way to handle application control requests without page reloading by extending the `<tizen:app-control>` element of the `config.xml` file and sending a new `appcontrol` event to the receiving application.

The following code example demonstrates a service description in the `config.xml` file, which can handle an image editing application control request without reloading the Web page:

```
<tizen:app-control>
   <src name="edit.html" reload="disable"/>
   <operation name="http://tizen.org/appcontrol/operation/edit"/>
   <mime name="image/*"/>
</tizen:app-control>
```

The `reload` attribute is added to the `src` element (in [mobile](../../../tizen-studio/web-tools/config-editor.md#mw_appcontrol) and [wearable](../../../tizen-studio/web-tools/config-editor.md#appcontrol) applications), and used to set whether the page must be reloaded when an application control request is received. The `reload` attribute is optional and the default value is `enable`. If the attribute is not set, the page reloads.

If the currently loaded page is selected by an incoming application control request, and the `reload` attribute of the service description is set to `disable`, an `appcontrol` event is dispatched to that page instead of reloading it. By using an `appcontrol` event listener, the Web application can get the requested information by calling the `getRequestedAppControl()` method of the `Application` interface. An `appcontrol` event is dispatched only if the `reload` attribute of the service description is set to `disable`.

The following example demonstrates adding an `appcontrol` event listener and handling an event:

```
window.addEventListener('appcontrol', function onAppControl() {
    var reqAppControl = tizen.application.getCurrentApplication.getRequestedAppControl();
    if (reqAppControl) {
        /* Handle the application control request */
    }
});
```

## Prerequisites

To use the Application API (in [mobile](../../api/latest/device_api/mobile/tizen/application.html), [wearable](../../api/latest/device_api/wearable/tizen/application.html), and [TV](../../api/latest/device_api/tv/tizen/application.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/application.info"/>
<tizen:privilege name="http://tizen.org/privilege/appmanager.kill"/>
```

## Retrieving Application Information

You can retrieve information about applications in various ways:

- Retrieve information about installed applications with the `getAppInfo()` and `getAppsInfo()` methods of the `ApplicationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationManager), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationManager), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationManager) applications).

  These methods can be used to access the `ApplicationInformation` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationInformation), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationInformation), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationInformation) applications) to retrieve information about installed applications, such as their name, icon path, and version.

- Retrieve information about running applications with the `getAppContext()` and `getAppsContext()` methods of the `ApplicationManager` interface.

  These methods can be used to access the `ApplicationContext` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationContext), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationContext), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationContext) applications) to retrieve the application ID and context ID of the running application.

  The application ID can be used to retrieve application information, or to launch an application. The context ID is a unique identifier given by the platform to a running application.

- Retrieve information about battery usage per application with the `getBatteryUsageInfo()` method of the `ApplicationManager` interface **in mobile and wearable applications only**.

  You can retrieve battery usage information starting from a specific number of days ago, or since the battery was last fully charged. You can also select the number of applications included in the returned `ApplicationBatteryUsage` data array (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationBatteryUsage) and [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationBatteryUsage) applications).

- Retrieve information about usage statistics per application with the `getAppsUsageInfo()` method of the `ApplicationManager` interface **in mobile and wearable applications only**.

  The statistics include the most frequently or recently used applications. You can retrieve application usage information from a specific time period, or starting from a specific number of days ago. You can also select the number of applications included in the returned `ApplicationUsage` data array (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationUsage) and [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationUsage) applications).

Learning how to retrieve information about installed and running applications allows you to manage all the device applications from your application:

- To retrieve a list of installed applications, use the `getAppsInfo()` method of the `ApplicationManager` interface:

  ```
  function onListInstalledApplications(applications) {
      console.log('The number of installed applications is ' + applications.length);
  }
  tizen.application.getAppsInfo(onListInstalledApplications);
  ```

  The list of applications is returned to the `ApplicationInformationArraySuccessCallback` event handler as an array of `ApplicationInformation` objects.

- To retrieve a list of running applications, use the `getAppsContext()` method of the `ApplicationManager` interface:

  ```
  function onRunningApplicationContexts(contexts) {
      console.log('The number of running applications is ' + contexts.length);
  }
  tizen.application.getAppsContext(onRunningApplicationContexts);
  ```

  The list of application contexts is returned to the given event handler as an array of the `ApplicationContext` objects.

- To retrieve basic application information, use the `getAppInfo()` method of the `ApplicationManager` interface.

  Provide the application ID of the application whose information you want as a parameter for the method. If no application ID is set, the method uses the details of the application calling the method.

  ```
  var appinfo = tizen.application.getAppInfo('org.tizen.application');
  console.log('The application icon path: ' + appinfo.iconPath);
  console.log('The application name: ' + appinfo.name);
  ```

- To retrieve application context information, use the `getAppContext()` method of the `ApplicationManager` interface.

  Provide the context ID of the application whose context information you want as a parameter for the method. If no context ID is set, the method uses the details of the application calling the method.

  ```
  var appContext = tizen.application.getAppContext();
  console.log('Application context retrieved for app ' + appContext.id);
  ```

- To retrieve application battery usage information, use the `getBatteryUsageInfo()` method of the `ApplicationManager` interface.

  To retrieve the battery usage information for a limited time period starting from a specific number of days ago, set the number of days in the third parameter of the method. If you leave the parameter at `null`, the time period since the battery was last fully charged is used.

  ```
  var successCallback = function(batteryUsageInfoArray) {
      batteryUsageInfoArray.forEach(function(abuInfo) {
          console.log('ApplicationID: ' + abuInfo.appId + ', usage: ' + abuInfo.batteryUsage);
      });
  };
  tizen.application.getBatteryUsageInfo(successCallback);
  ```

  You can expand the obtained data by calling the `getAppInfo()` method with the `ApplicationId` parameter you have received from the returned array.

- To retrieve application usage statistics, use the `getAppsUsageInfo()` method of the `ApplicationManager` interface. Define the type of statistics (most frequently or recently used applications) in the third parameter.

  To retrieve the statistics from between specific start and end dates, or for a limited time period starting from a specific number of days ago, set the time filter in the fourth parameter of the method. If you leave the parameter at `null`, a time period starting from 30 days ago is used.

  ```
  var successCallback = function(appsUsageInfo) {
      appsUsageInfo.forEach(function(auInfo) {
          console.log("ApplicationID: " + auInfo.appId + ", count: " + auInfo.totalCount +
                      ", duration: " + auInfo.totalDuration + ", last used at: " + auInfo.lastTime);
      });
  };

  var errorCallback = function(err) {
      console.error(err);
  }

  tizen.application.getAppsUsageInfo(successCallback, errorCallback, "RECENTLY");
  ```

> **Note**  
> Statistics are available for the last 90 days. If you set a time filter that starts from more than 90 days ago, only the period that falls within the last 90 days is included in the returned array.

## Managing Applications

You can manage and retrieve information about the current application with the `Application` object (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#Application), [wearable](../../api/latest/device_api/wearable/tizen/application.html#Application), and [TV](../../api/latest/device_api/tv/tizen/application.html#Application) applications). The `Application` object is retrieved using the `getCurrentApplication()` method of the `ApplicationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationManager), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationManager), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationManager) applications). You can exit or hide the current application using the `Application` interface.

Learning how to launch and stop other applications, and hide or exit applications running on the device, allows you to manage all the device applications from your application:

1. To launch or stop another application, you need the application ID (for launching) or context ID (for stopping) to identify the application.

   To launch an application, use the `launch()` method of the `ApplicationManager` interface, and to stop an application, use the `kill()` method.

   In the following example, the application to be launched and stopped is an alarm, with the `"samplealarm"` ID.

   ```
   /* Launch the application */
   tizen.application.launch('samplealarm', onsuccess);

   /* Stop the application */
   function onGetAppsContextSuccess(appcontexts) {
       for (int i = 0; i < appcontexts.length; i++) {
           if (appcontexts[i].appId === 'samplealarm') {
               tizen.application.kill(appcontexts[i].id);
           }
       }
   }

   tizen.application.getAppsContext(onGetAppsContextSuccess);
   ```

   You can also [launch an application using the application control](#launching-applications-with-the-application-control).

2. To retrieve the current application, use the `getCurrentApplication()` method:

   ```
   var currApp = tizen.application.getCurrentApplication();
   ```

3. To hide the current application, use the `hide()` method:

   ```
   currApp.hide();
   ```

4. To exit the current application, use the `exit()` method:

   ```
   currApp.exit();
   ```

## Launching Applications with the Application Control

With the application control, you can send a request to launch other applications based on their functionality using the `launchAppControl()` method of the `ApplicationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationManager), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationManager), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationManager) applications) (which can also contain some data).

Any installed application can provide a service which can be identified by the operation name. When other applications request the provided service of the provider application (and optionally passing some data to the service), the provider application is launched and performs a specific operation. The provider application also sends back a response to the request with an `ApplicationControlData` instance (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControlData), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControlData), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControlData) applications) (which can also contain some data).

Learning to use application controls to launch other applications from your application allows you to take advantage of the functionality of other device applications.

1. To use the application control mechanism to pick image files from a list of images, create an `ApplicationControl` object (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControl), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControl), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControl) applications).

   Define the functionality required from the external application which you want to launch. The application control request must have an operation type suitable for selecting images, with the URI set as `null`, and the MIME type set as `image/*`.

   ```
   var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/pick', null, 'image/*');
   ```

2. Define the format of the reply you want to receive from the application control:

   ```
   var appControlReplyCB = {
       /* Reply is sent if the requested operation is successfully delivered */
       onsuccess: function(reply) {
           for (var num = 0; num < reply.length; num++) {
               if (reply[num].key == 'http://tizen.org/appcontrol/data/path') {
                   console.log('picked image path: ' + reply[num].value[0]);
               }
           }
       }
   }
   ```

3. Call the `launchAppControl()` method to find a suitable application to select the images:

   ```
   tizen.application.launchAppControl(appControl, null, function() {
       console.log('launch appControl succeeded');
   }, function(e) {
       /* Error handling */
   }, appControlReplyCB);
   ```

## Receiving and Replying to Application Control Requests

Learning how to handle requests from other applications allows you to create Web applications that can be called from other applications to perform specific actions.

Web applications can provide a service which can be identified by an operation name. Other applications can request and use the provided service of other applications (and optionally pass some data to the service). The provider application receives the request, performs some actions, and sends the result to the caller application in an `ApplicationControlData` array (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControlData), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControlData), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationControlData) applications).

1. To enable an application to receive application control requests, open the [Web application configuration editor](../../tutorials/process/setting-properties.md#set_widget) in the Tizen Studio and add an operation in the `app-control` section of the **Tizen** tab.

   In this example, the name of the operation is `http://example.tizen.org/operation/get_time`. The `config.xml` file contains a [&lt;tizen:app-control&gt;](../../../tizen-studio/web-tools/config-editor.md#mw_appcontrol) element:

   ```
   <tizen:app-control>
      <tizen:src name="index.html"/>
      <tizen:operation name="http://example.tizen.org/operation/get_time"/>
   </tizen:app-control>
   ```

   For more information, see [Application Control Export](#application-control-export).

2. To retrieve an object of the `RequestedApplicationControl` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#RequestedApplicationControl), [wearable](../../api/latest/device_api/wearable/tizen/application.html#RequestedApplicationControl), and [TV](../../api/latest/device_api/tv/tizen/application.html#RequestedApplicationControl) applications), use the `getCurrentApplication()` method of  the `ApplicationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationManager), [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationManager), and [TV](../../api/latest/device_api/tv/tizen/application.html#ApplicationManager) applications) and the `getRequestedAppControl()` method of the `Application` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#Application), [wearable](../../api/latest/device_api/wearable/tizen/application.html#Application), and [TV](../../api/latest/device_api/tv/tizen/application.html#Application) applications):

   ```
   var reqAppControl = tizen.application.getCurrentApplication().getRequestedAppControl();

   if (reqAppControl && reqAppControl.callerAppId) {
       console.log('Requester AppID: ' + reqAppControl.callerAppId + '\nwith operation: ' + reqAppControl.appControl.operation);
   } else {
       console.log('The application was not launched with Application Control.');
   }
   ```

3. To send a reply to the caller application, use the `replyResult()` method of the `RequestedApplicationControl` interface:

   ```
   try {
       /* Construct result data */
       var data = new tizen.ApplicationControlData('current-time', [new Date().toString()]);
       /* Reply to caller */
       reqAppControl.replyResult([data]);
   }
   ```

If the provider application is not already running when the application control request is made, it is automatically launched. If the application control [request arrives from the push service](../messaging/push.md#handling-a-launch-by-the-push-service), you can use the `appControl` object of the `RequestedApplicationControl` interface in the launched application to recognize the launch reason:

- If the application is launched because a push notification with the `LAUNCH` option has arrived, the `http://tizen.org/appcontrol/data/push/launch_type` data key of the `appControl` object is set to `notification`.
- If the push registration state has changed, the data key is set to `registration_change`.

```
var reqAppControl = tizen.application.getCurrentApplication().getRequestedAppControl();

if (reqAppControl) {
    var retData = reqAppControl.appControl.data;
    var i = retData.length;
    while (--i >= 0) {
        var dat = retData[i];
        if (dat.key === 'http://tizen.org/appcontrol/data/push/launch_type') {
            console.log('Cause of application wake-up: ' + JSON.stringify(dat.value))
        }
    }
}
```

## Broadcasting and Listening for Events

Since Tizen 2.4, Web applications can broadcast their own events to all listeners who are listening for these events. Web applications can also broadcast trusted events for trusted listeners who have the same certificate as the sender application.

To manage event broadcasting:

- You can broadcast an event with the `broadcastEvent()` or `broadcastTrustedEvent()` method.
- You can receive event data from other applications with the `addEventListener()` method.
- You can stop receiving event data from other applications with the `removeEventListener()` method.

Learning how to broadcast and listen for events allows you to create Web applications that can send and receive data between each other:

- The first application can broadcast an event.

  To broadcast events, use the `broadcastEvent()` method:

  ```
  var app = tizen.application.getCurrentApplication();
  var appEvent = {name: 'first_app_event_1'};
  var data = {foo: 'bar'};

  app.broadcastEvent(appEvent, data);
  ```

  Web applications can also broadcast trusted events for trusted listeners with the same certificate as the sender application. To broadcast trusted events, use the `broadcastTrustedEvent()` method:

  ```
  app.broadcastTrustedEvent(appEvent, data);
  ```

- The second application can listen to the first application and receive data.

  To receive data from the first application, use the `addEventListener()` method with the sender application ID and event name:

  ```
  var app = tizen.application.getCurrentApplication();

  var watchId = app.addEventListener({appId: 'a234567890.FirstApp', name: 'first_app_event_1'},
                                     function(event, data) {
      /* Data from first app must be received here */
      console.log('Data: ' + JSON.stringify(data));
  });
  ```

  To stop receiving data from the first application, use the `removeEventListener()` method with the proper `watchId`:

  ```
  app.removeEventListener(watchId);
  ```

## Background Execution

When a Web application becomes invisible (moves to the background), it is suspended. Before Tizen 2.4, to continue to execute the application in the background, you had to set the `background-support` attribute of the `<tizen:setting>` element to `enable` in the `config.xml` file (in [mobile](../../../tizen-studio/web-tools/config-editor.md#mw_setting) and [wearable](../../../tizen-studio/web-tools/config-editor.md#ww_setting) applications).

Since Tizen 2.4, the background process management policy has been changed. The system does not allow applications to run in the background except when they are explicitly declared to do so by having a specific background category. For more information on the available background categories, see the [Allowed background application policy](../../../native/guides/app-management/efl-ui-app.md#allow_bg_table) table.

> **Note**  
> To guarantee that a Web application runs in the background, at least 1 `background-category` element must be declared in the `config.xml` file (in [mobile](../../../tizen-studio/web-tools/config-editor.md#mw_bg_category) and [wearable](../../../tizen-studio/web-tools/config-editor.md#ww_bg_category) applications), and the `background-support` attribute of the `<tizen:setting>` element must be set to `enable`.

The following `config.xml` file example shows how an application can be configured to run in the background:

```
<?xml version="1.0" encoding="UTF-8"?>
<widget xmlns="http://www.w3.org/ns/widgets" xmlns:tizen="http://tizen.org/ns/widgets"
        id="http://yourdomain/BackgroundCategory" version="1.0.0" viewmodes="maximized">
   <tizen:application id="background.category" package="background" required_version="2.4"/>
   <content src="index.html"/>
   <icon src="icon.png"/>
   <name>BackgroundCategoryTest</name>
   <tizen:background-category value="media"/>
   <tizen:background-category value="download"/>
   <tizen:background-category value="background-network"/>
   <tizen:setting background-support="enable"/>
</widget>
```

## Monitoring the Application Status

Learning how to receive notifications allows you to monitor when the status of an application installed on a device is changed (it is enabled or disabled):

1. To receive status change notifications for installed applications, add a listener that is triggered each time the application status changes.

   If you want to monitor the status of a specific application (instead of all installed applications), provide the application ID as a second parameter to the `addAppStatusChangeListener()` method.

   ```
   var watchId;
   function appStatusEventCallback(appId, isActive) {
       console.log('The application ' + appId + ' has been ' + (isActive ? 'activated' : 'deactivated'));
   }

   try {
       watchId = tizen.application.addAppStatusChangeListener(appStatusEventCallback, 'app1test.BasicMobileApp');
   } catch (err) {
       console.log('Exception: ' + err.name);
   }
   ```

2. When notifications are no longer needed, remove the listener using the watch ID retrieved by the `addAppStatusChangeListener()` method:

   ```
   try {
       tizen.application.removeAppStatusChangeListener(watchId);
       console.log('Listener with id ' + watchId + ' has been removed');
   } catch (err) {
       console.log('Exception: ' + err.name);
   }
   ```

## Related Information
* Dependencies
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
