# Application Icons

When an application has new information requiring user attention, such as missed calls or new messages, it has a number in the upper-right corner of the application icon. This number is called a badge. For example, when a new message is received, the badge appears on the application icon. The badge remains until the user reads the message.

This feature is supported in mobile and wearable applications only.

**Figure: Badge**

![Badge](./media/badge.png)

The main features of the Badge API include:

- Managing badges  

  You can [set and get the badge number](#managing-badges).

- Listening for badge changes  

  You can [receive notifications on badge changes](#receiving-notifications-on-badge-changes) to display and react to badges.

## Prerequisites

To use the Badge API (in [mobile](../../api/latest/device_api/mobile/tizen/badge.html) and [wearable](../../api/latest/device_api/wearable/tizen/badge.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/notification"/>
```

## Managing Badges

Getting and setting the badge number is a useful UI management skill:

1. Retrieve application identifier using the `getCurrentApplication()` method:

   ```
   var appId = tizen.application.getCurrentApplication().appInfo.id;
   ```

2. To check the badge number of the current application, use the `getBadgeCount()` method of the `BadgeManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/badge.html#BadgeManager) and [wearable](../../api/latest/device_api/wearable/tizen/badge.html#BadgeManager) applications):

   ```
   var count = tizen.badge.getBadgeCount(appId);
   console.log('Badge count of ' + appId + ' is ' + count);
   ```

3. To change the badge of the current application, use the `setBadgeCount()` method:

   ```
   var appId = tizen.application.getCurrentApplication().appInfo.id;
   tizen.badge.setBadgeCount(appId, 82);
   ```

4. To hide the badge of the current application, use the `setBadgeCount()` method to set the number to 0:

   ```
   tizen.badge.setBadgeCount(appId, 0);
   ```

## Receiving Notifications on Badge Changes

Registering a listener for badge count changes to react to new badges and display your badges is a useful UI management skill:

1. To register an event handler for receiving a notification about badge changes, use the `addChangeListener()` method of the `BadgeManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/badge.html#BadgeManager) and [wearable](../../api/latest/device_api/wearable/tizen/badge.html#BadgeManager) applications), specifying a list of application IDs:

   ```
   function watcher(appId, count) {
       console.log(appId + ' badge number were updated: ' + count);
   }

   tizen.badge.addChangeListener(['BDb5tZJe47.TestSample'], watcher);
   ```

   `BDb5tZJe47.TestSample` is the application ID of the application to monitor. The first argument of the `addChangeListener()` method is an array of application identifiers. This allows you to bind the listener to several applications at same time.

2. To stop receiving notifications about badge changes, use the `removeChangeListener()` method:

   ```
   tizen.badge.removeChangeListener(['BDb5tZJe47.TestSample']);
   ```


## Related information
* Dependencies
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
