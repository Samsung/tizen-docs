# Audio Management


You can control the audio behavior of your application.

The main features of the `Tizen.Multimedia.AudioManager` class include:

-   Controlling the volume

    You can [control the output volume](#manage) by managing the audio type and its volume level.

-   Querying audio devices

    You can [retrieve various device information](#query_device), such as the device state.

## Prerequisites

To control volume levels, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

```
<privileges>
   <privilege>http://tizen.org/privilege/volume.set</privilege>
</privileges>
```

<a name="manage"></a>
## Controlling Volume Levels

You can manage the volume level of a specific audio type. You can set and get a volume level and a maximum volume level of a particular audio type.

Normally, if there is an active output stream, the `VolumeController.CurrentPlaybackType` property of the [Tizen.Multimedia.AudioManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioManager.html) class returns the stream audio type, and if not, it returns `AudioVolumeType.None`.

To control the volume of your application:

-   To receive a notification whenever the volume changes, define and register an event handler for the `VolumeController.Changed` event of the `Tizen.Multimedia.AudioManager` class:

    ```
    void OnVolumeChanged(object sender, VolumeChangedEventArgs args)
    {
        Tizen.Log.Info("AudioManager", $"{args.Type} volume changed to {args.Level}");
    }

    AudioManager.VolumeController.Changed += OnVolumeChanged;
    ```

    When the volume changes, the event handler provides in its parameters the audio type that has changed and the new volume level.

-   To retrieve the current and maximum volumes for a specific audio type, use the `VolumeController.Level` and `VolumeController.MaxLevel` properties of the `Tizen.Multimedia.AudioManager` class:

    ```
    var type = AudioVolumeType.Media;

    var curVol = AudioManager.VolumeController.Level[type];

    var maxVol = AudioManager.VolumeController.MaxLevel[type];
    ```

-   To set the volume level, use the `VolumeController.Level` property.

    In the following example, a value is received from application UI slider, with which the user sets the volume level.

    ```
    var type = AudioVolumeType.Media;
    int value;

    /// Make sure the value is within the system maximum volume
    /// by checking the VolumeController.MaxLevel property

    AudioManager.VolumeController.Level[type] = value;
    ```

<a name="query_device"></a>
## Querying Audio Devices

The audio behavior of your application must change depending on the audio devices that are connected.

To query audio device information:

-   To access device information:
    1.  Retrieve the list of the currently connected audio devices with the `GetConnectedDevices()` method of the [Tizen.Multimedia.AudioManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioManager.html) class:

        ```
        IEnumerable<AudioDevice> connectedDevices = AudioManager.GetConnectedDevices();
        ```

    2.  Retrieve the device information from the [Tizen.Multimedia.AudioDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.AudioDevice.html) class, which has the following properties:
        -   `Type`: Device type
        -   `IoDirection`: Device IO direction
        -   `Id`: Device ID
        -   `Name`: Device name
        -   `State`: Device state

-   To get a notification when the audio device connection or state changes, add event handlers for the `DeviceConnectionChanged` and `DeviceStateChanged` events of the `Tizen.Multimedia.AudioManager` class:
    -   To receive a notification whenever the device connection state changes:

        ```
        void OnDeviceConnectionChanged(object sender, AudioDeviceConnectionChangedEventArgs args)
        {
            if (args.IsConnected)
            {
                if (args.Device.Type == AudioDeviceType.BluetoothMedia)
                    /// Connected device type is Bluetooth, handle accordingly
                else
                    /// Handle accordingly
            }
            else
            {
                if (args.Device.Type == AudioDeviceType.BluetoothMedia)
                    /// Disconnected device type is Bluetooth, handle accordingly
                else
                    /// Handle accordingly
            }
        }

        AudioManager.DeviceConnectionChanged += OnDeviceConnectionChanged;
        ```

    -   To receive a notification whenever the device state changes:

        ```
        void OnDeviceStateChanged(object sender, AudioDeviceStateChangedEventArgs args)
        {
            if (args.Device.Type == AudioDeviceType.BluetoothMedia)
            {
                if (args.Device.State == AudioDeviceState.Deactivated)
                    /// Bluetooth device has been deactivated, handle accordingly
                else
                    /// Handle accordingly
            }
            else
            {
                /// Handle accordingly
            }
        }

        AudioManager.DeviceStateChanged += OnDeviceStateChanged;
        ```


        > **Note**   
		> The initial state of the connected device is `Deactivated`.



## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
