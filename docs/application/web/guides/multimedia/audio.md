# Audio Management

You can control the volume level of several sound types and get information about the current sound mode and the state of the current sound devices. The available sound types include, for example, system, notifications, alarms, and media.

This feature is optional.

The main features of the Sound API include the following:

- Managing the volume level and sound mode

  You can [set the volume level of a specific sound type](#manage-volume-and-sound-mode) with the `setVolume()` method. You can also [retrieve the current sound mode](#manage-volume-and-sound-mode) with the `getSoundMode()` method.

- Getting a list of the current sound devices in a specified state

  You can [retrieve a list of the current sound devices which are in a specified state](#manage-sound-devices) by using the `getConnectedDeviceList()` method.

- Monitoring changes in the volume level and sound mode

  You can [monitor changes in the volume level and sound mode](#monitor-volume-and-sound-mode-changes) by registering appropriate listeners.

- Monitoring changes in the sound device state

  You can [monitor changes in the state of sound devices](#monitor-the-sound-device-state) with the `addDeviceStateChangeListener()` method.

## Prerequisites

To use the Sound API, the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/volume.set"/>
```

## Manage volume and sound mode

Managing volume levels and sound modes is a basic multimedia management skill, follow these steps to manage volume and sound mode:

1. Get the current volume level using the `getVolume()` method:

   ```
   var vol = tizen.sound.getVolume('RINGTONE');
   ```

2. Set a new volume level using the `setVolume()` method.

   The following example increases the ringtone volume by 10% of the maximum volume level:

   ```
   tizen.sound.setVolume('RINGTONE', vol + 0.1);
   ```

3. Get the current sound mode using the `getSoundMode()` method:

   ```
   var mode = tizen.sound.getSoundMode();
   console.log('Sound Mode is ' + mode);
   ```

## Monitor volume and sound mode changes

Managing volume and sound mode changes is a basic multimedia management skill, follow these steps to monitor volume and sound mode:

1. Register the volume change listener to track changes in the volume level:

   ```
   function onsuccessCB(type, volume) {
       console.log('SoundType is ' + type);
       console.log('Volume is ' + volume);
       tizen.sound.unsetVolumeChangeListener();
   }

   tizen.sound.setVolumeChangeListener(onsuccessCB);
   ```

2. Register the sound mode change listener to track changes in the sound mode:

   ```
   function onsuccessCB(mode) {
       console.log('Mode is ' + mode);
       tizen.sound.unsetSoundModeChangeListener();
   }

   tizen.sound.setSoundModeChangeListener(onsuccessCB);
   ```

## Manage sound devices

Learning how to list connected and activated sound devices allows you to manage sound devices more effectively, follow these steps to manage sound devices:

1. Get a list of the current sound devices in a connected state using the `getConnectedDeviceList()` method:

   ```
   var infoArr = tizen.sound.getConnectedDeviceList();

   for (var i = 0; i < infoArr.length; i++) {
       console.log(infoArr[i].device);
   }
   ```

2. Get a list of the current sound devices in a running state using the `getConnectedDeviceList()` method and checking the isRunning property:

   ```
   var infoArr = tizen.sound.getConnectedDeviceList();

   for (var i = 0; i < infoArr.length; i++) {
       if(infoArr[i].isRunning) {
           console.log(infoArr[i].device);
       }
   }
   ```

## Monitor the sound device state

Learning how to monitor changes in the sound device state makes it easier for you to manage the sound devices:

1. Add a sound device state change listener to track changes in the sound device state:

   ```
   function onchangedCB(info) {
       if (info.isConnected) {
           console.log(info.device + ' is connected');
       } else {
           console.log(info.device + ' is not connected');
       }

       if (info.isActivated) {
           console.log(info.device + ' is activated');
       } else {
           console.log(info.device + ' is not activated');
       }
   }

   var listenerId = tizen.sound.addDeviceStateChangeListener(onChangedCB);
   ```

2. When no longer needed, use the listener ID to remove the sound device state change listener:

   ```
   tizen.sound.removeDeviceStateChangeListener(listenerId);
   ```

## Related information
* Dependencies
  - Tizen 2.4 and Higher
