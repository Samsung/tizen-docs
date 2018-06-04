# Notifications

You can provide notifications to the user about application events.

This feature is supported in mobile and wearable applications only.

The main features of the Notification API include:

- Creating simple notifications   

  You can [create a simple notification](#creating-simple-notifications) that provides the user information about their events.

- Creating progress notifications  

  You can [create a progress notification](#creating-progress-notifications) that informs the user about the progress of an activity.

- Managing notifications   

  You can [retrieve, update, and remove posted notifications](#managing-notifications).

- Managing notification templates   

  You can [create a template](#managing-notification-templates) that can be reused in multiple notifications.

To display a notification, you need to create a `Notification` object (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#Notification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#Notification) applications), or its subtype.

> **Note**  
> The `StatusNotification` subtype (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#StatusNotification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#StatusNotification) applications) is deprecated since Tizen 4.0. To display notifications in the status bar, use the `UserNotification` subtype (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#UserNotification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#UserNotification) applications).

## Prerequisites

To use the Notification API (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/notification"/>
```

## Creating Simple Notifications

Learning how to create notifications allows you to design interactive applications that provide the user information about their events:

1. Define the notification properties of the `UserNotificationInit` interface (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#UserNotificationInit) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#UserNotificationInit) applications):

   ```
   /* Application control */
   var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/create_content',
                                                 null, 'image/jpg', null, null);

   var notificationGroupDict = {
       /* Notification content */
       content: 'This is a simple notification.',
       images: {
           /* Path to the notification icon */
           iconPath: 'images/image1.jpg'
       },
       actions: {
           /* Path to the sound file to be played when the notification is displayed */
           soundPath: 'music/Over the horizon.mp3',
           /* Device vibrates when the notification is displayed */
           vibration: true,
           /* Application control to be launched when the user selects the notification */
           appControl: appControl
       }
   };
   ```

   The path in the `iconPath` and `soundPath` parameters means a relative file location defined in the Filesystem API (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html) and [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html) applications). The path is not an absolute file location, but instead uses a [virtual root location](../data/file-system.md#supported-virtual-roots) (such as `images` in `images/image1.jpg`).

2. To be able to display the notification, create a `UserNotification` object (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#UserNotification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#UserNotification) applications) with the notification type, title, and the additional notification properties defined in the previous step.

   ```
   var notification = new tizen.UserNotification('SIMPLE', 'Simple notification', notificationGroupDict);
   ```

3. To post the notification, use the `post()` method of the `NotificationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#NotificationManager) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#NotificationManager) applications):

   ```
   tizen.notification.post(notification);
   ```

## Creating Progress Notifications

Learning how to create progress notifications allows you to design interactive applications that inform the user about the progress of an activity:

1. Define the notification properties of the `UserNotificationInit` interface (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#UserNotificationInit) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#UserNotificationInit) applications):

   ```
   /* Application control */
   var appControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/create_content',
                                                 null, 'image/jpg', null, null);

   var notificationGroupDict = {
       content: 'This is a progress notification.',
       images: {
           iconPath: 'images/image1.jpg'
       },
       actions: {
           vibration: false,
           appControl: appControl
       },
       textContents: {
           progressType: 'PERCENTAGE',
           progressValue: 0
       },
   };
   ```

   The path in the `iconPath` parameter means a file location defined in the Filesystem API (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html) and [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html) applications). The path is not an absolute file location, but instead uses a [virtual root location](../data/file-system.md#supported-virtual-roots) (such as `images` in `images/image1.jpg`).

2. To be able to display the notification, create a `UserNotification` object (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#UserNotification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#UserNotification) applications) with the notification type, title, and the additional notification properties defined in the previous step:

   ```
   var notification = new tizen.UserNotification('PROGRESS', 'Progress notification', notificationGroupDict);
   ```

3. Define a function which uses the `update()` method of the `NotificationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#NotificationManager) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#NotificationManager) applications) to update the posted notification every second:

   ```
   function updateProgressNotification(progress) {
       if (progress <= 100) {
           notification.textContents.progressValue = progress;
           tizen.notification.update(notification);
           setTimeout(function() {
               updateProgressNotification(progress + 10);
           }, 1000);
       } else {
           tizen.notification.remove(notification.id);
       }
   }
   ```

4. To post the notification, use the `post()` method of the `NotificationManager` interface. If the progress value is set, the progress bar is displayed in the notification. The progress value can change the amount of progress as it moves forward or backward.

   The application must keep the progress value for its job, because the saved value in the notification panel can be different (rounded) from the exact progress value.

   ```
   tizen.notification.post(notification);
   updateProgressNotification(0);
   ```

## Managing Notifications

Learning how to manage notifications allows you to design interactive applications that provide the user information about their events:

1. To retrieve notifications:

   - To retrieve a previously posted notification, use the `getNotification()` method of the `NotificationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#NotificationManager) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#NotificationManager) applications with the notification ID as a parameter:
     ```
     var myId = notification.id;
     var myNotification = tizen.notification.getNotification(myId);
     ```

   - To retrieve all previously posted notifications, use the `getAllNotifications()` method, which returns all the notifications as an array:

     ```
     var notifications = tizen.notification.getAllNotifications();
     var index = 0;

     /* For each notification, write the ID and title in the console log */
     for (index = 0; index < notifications.length; index++) {
         console.log(notifications[index].id);
         console.log(notifications[index].title);
     }
     ```

2. To update a previously posted notification, use the `update()` method by specifying the updated notification object:

   ```
   myNotification.content = 'My notification';
   tizen.notification.update(myNotification);
   ```

3. To remove notifications:    

   - To remove a previously posted notification, use the `remove()` method with the notification ID as a parameter:

     ```
     tizen.notification.remove(myNotification.id);
     ```

   - To remove all notifications previously posted by the current application, use the `removeAll()` method:

     ```
     tizen.notification.removeAll();
     ```

## Managing Notification Templates

Learning how to manage notification templates allows you to create a template from an existing notification, and reuse that template later to quickly create other notifications with the same pattern:

- To create a template:  

  1. Create a [simple](#creating-simple-notifications) or [progress](#creating-progress-notifications) notification to be used as a template.  
     You do not need to post the notification to save it as a template.

     ```
     /* Assume that myNotification is a valid tizen.UserNotification object */
     var myNotification;
     ```

  2. Save the template with the `saveNotificationAsTemplate()` method of the `NotificationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#NotificationManager) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#NotificationManager) applications):

     ```
     try {
         var templateName = 'importantNoti';
         tizen.notification.saveNotificationAsTemplate(templateName, myNotification);
     } catch (e) {
         console.log('Error ' + e.message + ' occurred');
     }
     ```

- To use the template when creating a new notification, use the `createNotificationFromTemplate()` method of the `NotificationManager` interface:

  ```
  try {
      var newTemplateNotification = tizen.notification.createNotificationFromTemplate(templateName);
      console.log('Content of new notification: '  + newTemplateNotification.content);
  } catch (e) {
      console.log('Error ' + e.message + ' occurred');
  }
  ```

  This method returns a `UserNotification` object (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#UserNotification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#UserNotification) applications), even if the template was created based on a `StatusNotification` object (in [mobile](../../api/latest/device_api/mobile/tizen/notification.html#StatusNotification) and [wearable](../../api/latest/device_api/wearable/tizen/notification.html#StatusNotification) applications).

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
