# System Settings

You can access and modify some [system settings properties](#system-settings-properties), such as the home screen and lock screen wallpaper image, incoming call ringtone, and email notification tone.

This feature is supported in mobile and wearable applications only.

The main features of the System Setting API include:

- Device wallpaper management

  You can [set the wallpaper](#managing-the-device-wallpapers) of the home and lock screen.

- Device ringtone and notification tone management

  You can [set the ringtone](#managing-ringtones-and-notification-tones) for incoming calls and [the tone for email notifications](#managing-ringtones-and-notification-tones).

## Prerequisites

To use the System Setting API (in [mobile](../../api/latest/device_api/mobile/tizen/systemsetting.html) and [wearable](../../api/latest/device_api/wearable/tizen/systemsetting.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/setting"/>
```

## Managing the Device Wallpapers

You can change the home and lock screen images by using the `setProperty()` method of the `SystemSettingManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/systemsetting.html#SystemSettingManager) and [wearable](../../api/latest/device_api/wearable/tizen/systemsetting.html#SystemSettingManager) applications). Similarly, you can retrieve information about them by using the `getProperty()` method.

To set the device wallpaper and get information about it:

- To set the specified image as the lock screen wallpaper, use the `setProperty()` method:

  ```
  function setLockscreenWallpaper() {
      tizen.filesystem.resolve('images/Background.jpg', function(imageFile) {
          try {
              tizen.systemsetting.setProperty('LOCK_SCREEN',
                                              imageFile.toURI().replace('file://', ''),
                                              successCB, errorCB);
          } catch (error) {
              console.log('Error: ' + error);
          }
      });
  }
  ```

- To get the current system setting information for the home screen wallpaper, use the `getProperty()` method:

  ```
  function getHomescreenWallpaper() {
      try {
          tizen.systemsetting.getProperty('HOME_SCREEN', successCB, errorCB);
      } catch (error) {
          console.log('Error: ' + error);
      }
  }
  ```

## Managing Ringtones and Notification Tones

You can modify the incoming call ringtone and notification email tone sound by using the `setProperty()` method of the `SystemSettingManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/systemsetting.html#SystemSettingManager) and [wearable](../../api/latest/device_api/wearable/tizen/systemsetting.html#SystemSettingManager) applications). Similarly, you can retrieve information about them by using the `getProperty()` method.

To set ringtones and notification tones:

- To set the specified audio file as the notification tone for emails, use the `setProperty()` method of the `SystemSettingManager` interface:

  ```
  function onSet() {
      console.log('It\'s set');
  }

  tizen.filesystem.resolve('music/Favorite track.mp3', function(musicFile) {
      try {
          tizen.systemsetting.setProperty('NOTIFICATION_EMAIL',
                                          musicFile.toURI().replace('file://', ''),
                                          onSet);
      } catch (error) {
          console.log('Error: ' + error);
      }
  });
  ```

- To get the current system setting information for the incoming call ringtone, use the `getProperty()` method:

  ```
  function onGet(value) {
      console.log('Current setting option value is: ' + value);
  }

  try {
      tizen.systemsetting.getProperty('INCOMING_CALL', onGet);
  } catch (error) {
      console.log('Error: ' + error);
  }
  ```

## System Settings Properties

The following table lists the supported system settings properties.

**Table: Available properties**

| Property             | Description                              |
| -------------------- | ---------------------------------------- |
| `HOME_SCREEN`        | Provides information about the home screen image of the device. |
| `LOCK_SCREEN`        | Provides information about the lock screen image of the device. |
| `INCOMING_CALL`      | Provides information about the incoming call ringtone sound of the device. |
| `NOTIFICATION_EMAIL` | Provides information about the notification email tone sound of the device. |

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
