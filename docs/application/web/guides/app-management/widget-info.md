# Widget Information

You can manage installed widgets and widget instances in various ways, such as retrieving information about widgets, or getting the widget instances and receiving notifications when the state of the widget changes.

This feature is supported in mobile and wearable applications only.

> **Note**  
> Do not use "widget" as a name for any of your global variables, as it is the name of a global W3C object.

The main features of the Widget Service API include:

- Widget retrieval   

  You can [retrieve widgets](#widget), for example, get the widgets installed on the device or information about their primary ID or size.

- Widget management   

  You can [manage individual widgets](#management) by getting the widget name and a list of widget instances and widget variants, and by receiving notifications about the widget life-cycle events.

- Widget instance management   

  You can [manage widget instances](#instance) by changing the instance data update interval and managing the instance content.

<a name="widget"></a>
## Widget Retrieval

Using the `WidgetServiceManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetServiceManager) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetServiceManager) applications), you can:

- Retrieve a widget or widgets using the `getWidgets()` method.
- Receive information about the primary widget ID or size related to the specific size type.

<a name="get_widget"></a>
### Retrieving a Widget

Learning how to retrieve the installed widget list is a basic widget management skill:

1. Define a success handler implementing the `WidgetArraySuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetArraySuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetArraySuccessCallback) applications). Optionally, you can specify an error handler too.

   ```
   var successCallback = function(widgets) {
       console.log('There are ' + widgets.length + ' installed widgets');
   };

   var errorCallback = function(error) {
       console.log('Error ' + error.message);
   };
   ```

2. To get a list of all installed widgets, use the `getWidgets()` method of the `WidgetServiceManager` interface. If the optional `packageId` parameter is given, only the widgets belonging to the given package are returned.

   ```
   var packageId = 'org.tizen.contacts';
   tizen.widgetservice.getWidgets(successCallback, errorCallback, packageId);
   ```

   You can also get a specific widget object by using the `getWidget()` method of the `WidgetServiceManager` interface:

   ```
   var myWidget = tizen.widgetservice.getWidget('org.tizen.gallery.widget');
   ```

<a name="info"></a>
### Retrieving ID and Size Information

Learning how to retrieve the primary widget ID or size makes using the Widget Service API easy and convenient:

- To get the primary widget ID of a given application or package ID, use the `getPrimaryWidgetId()` method of the `WidgetServiceManager` interface:

  ```
  var widgetId = tizen.widgetservice.getPrimaryWidgetId('org.tizen.music-player');
  ```

- To get the size of the corresponding size type, use the `getSize()` method of the `WidgetServiceManager` interface, specifying the size type:

  ```
  var widgetSize = tizen.widgetservice.getSize('4x4');
  ```

<a name="management"></a>
## Widget Management

Using the `Widget` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#Widget) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#Widget) applications), you can:

- Get the name of the widget in a given language using the `getName()` method.
- Get all instances belonging to the widget using the `getInstances()` method.
- Get variants of a specified size type.
- Monitor state changes in an installed widget.

<a name="name"></a>
### Retrieving the Widget Name

To retrieve the widget name:

1. Retrieve the widget whose name you need:

   ```
   var myWidget = tizen.widgetservice.getWidget('org.tizen.gallery.widget');
   ```

2. To get the widget name, use the `getName()` method of the `Widget` interface. If the locale parameter is omitted, the system locale is used.

   ```
   var name = myWidget.getName('en-us');
   ```

<a name="instances"></a>
### Retrieving Widget Instances

Learning how to retrieve information about installed widget instances makes the Widget Service API more useful:

> **Note**  
> The `WidgetInstance.id` value (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetInstance::id) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetInstance::id) applications) is volatile and can change after device reboot.

1. Define a success handler implementing the `WidgetInstancesCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetInstancesCallback) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetInstancesCallback) applications). Optionally, you can specify an error handler too.

   ```
   var successCallback = function(instances) {
       console.log('There are ' + instances.length + ' instances');
   };

   var errorCallback = function(error) {
       console.log('Error ' + error.message);
   };
   ```

2. To retrieve a list of all instances belonging to the widget, use the `getInstances()` method of the `Widget` interface:

   ```
   myWidget.getInstances(successCallback, errorCallback);
   ```

<a name="variants"></a>
### Retrieving Widget Variants

To retrieve variants representing all the supported widget size types:

1. Define a success handler implementing the `WidgetVariantsCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetVariantsCallback) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetVariantsCallback) applications). Optionally, you can specify an error handler too.

   ```
   var successCallback = function(variants) {
       console.log('There are ' + variants.length + ' variants of the widget');
   };

   var errorCallback = function(error) {
       console.log('Error ' + error.message);
   };
   ```

2. Retrieve the widget whose variants you need:

   ```
   var myWidget = tizen.widgetservice.getWidget('org.tizen.gallery.widget');
   ```

3. To get a list of all variants, use the `getVariants()` method of the `Widget` interface:

   ```
   myWidget.getVariants(successCallback, errorCallback);
   ```

   You can also get a specific variant by using the `getVariant()` method with one of the supported size types as a parameter:

   ```
   var variant = myWidget.getVariant('4x4');
   ```

<a name="receive"></a>
### Monitoring Widget Changes

Learning to receive notifications when the state of the widget has been changed is a useful widget management skill. There are 4 states that can be noticed: `CREATE`, `DESTROY`, `PAUSE`, and `RESUME`.

1. Define the event handler for state notifications using the `WidgetChangeCallback` listener interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetChangeCallback) applications):

   ```
   var WidgetChangeCallback = function(instance, event) {
       console.log('The instance ' + instance + ' has state ' + event);
   };
   ```

2. Retrieve the widget object using the `getWidget()` method of the `WidgetServiceManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetServiceManager) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetServiceManager) applications):

   ```
   var myWidget = tizen.widgetservice.getWidget('org.tizen.music-player.widget');
   ```

3. Add the listener to use the defined event handler with the `addStateChangeListener()` method of the `Widget` interface:

   ```
   var watchId = myWidget.addStateChangeListener(WidgetChangeCallback);
   ```

4. To stop receiving notifications for the defined listener, use the `removeStateChangeListener()` method of the `Widget` interface with the previously obtained listener ID:

   ```
   myWidget.removeStateChangeListener(watchId);
   ```

<a name="instance"></a>
## Widget Instance Management

Using the `WidgetInstance` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetInstance) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetInstance) applications), you can:

- Change the update period of the instance using the `changeUpdatePeriod()` method.
- Send or get content to and from the widget instance.

> **Note**  
> These features are not supported by Web widgets. You can only use them in Web applications to manage installed widgets. For more information, see [Web Device API supported by Widget Engine](../../api/latest/wearable_widget/web_widget.html#user-content-web-device-api).

<a name="period"></a>
### Changing the Update Period

To change the update interval for the widget instance:

1. Retrieve the widget instance with the `getInstances()` method:

   ```
   var instance;
   var successCallback = function(instances) {
       instance = instances[0];
   };

   var myWidget = tizen.widgetservice.getWidget('org.tizen.gallery.widget');
   myWidget.getInstances(successCallback);
   ```

2. To change the update interval, use the `changeUpdatePeriod()` method of the `WidgetInstance` interface with the new value (in seconds):

   ```
   instance.changeUpdatePeriod(2);
   ```

<a name="content"></a>
### Sending and Getting Content

Learning how to send and get the widget content is a useful widget management skill:

1. Obtain the widget instance with the `getInstances()` method:

   ```
   var instance;
   var successCallback = function(instances) {
       instance = instances[0];
   };

   var myWidget = tizen.widgetservice.getWidget('org.tizen.gallery.widget');
   myWidget.getInstances(successCallback);
   ```

2. To send data to the widget, use the `sendContent()` method of the `WidgetInstance` interface. The second parameter defines whether the instance is updated even if the provider is paused.

   ```
   instance.sendContent(data, true);
   ```

3. To retrieve widget instance content, define a success handler implementing the `WidgetContentCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/widgetservice.html#WidgetContentCallback) and [wearable](../../api/latest/device_api/wearable/tizen/widgetservice.html#WidgetContentCallback) applications). Optionally, you can specify an error handler too.

   ```
   var successCallback = function(object) {
       console.log('Data successfully retrieved');
   };

   var errorCallback = function(error) {
       console.log('Error ' + error.message);
   };
   ```

   Afterwards, use the `getContent()` method of the `WidgetInstance` interface:

   ```
   instance.getContent(successCallback, errorCallback);
   ```


## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for Mobile
   - Tizen 2.3.2 and Higher for Wearable
