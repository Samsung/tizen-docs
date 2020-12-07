# Audio Management


You can control the audio behavior of your application.

The main features of the `Tizen.Multimedia.AudioManager` class include:

-   Controlling the volume

    You can [control the output volume](#manage) by managing the audio type and its volume level.

-   Querying audio devices

    You can [retrieve various device information](#query_device), such as the device state.

## Prerequisites

To control volume levels, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

```XML
<privileges>
   <privilege>http://tizen.org/privilege/volume.set</privilege>
</privileges>
```

<a name="manage"></a>
## Controlling Volume Levels

You can manage the volume level of a specific audio type. You can set and get a volume level and a maximum volume level of a particular audio type.

Normally, if there is an active output stream, the `VolumeController.CurrentPlaybackType` property of the [Tizen.Multimedia.AudioManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.AudioManager.html) class returns the stream audio type, and if not, it returns `AudioVolumeType.None`.

To control the volume of your application:

-   To receive a notification whenever the volume changes, define and register an event handler for the `VolumeController.Changed` event of the `Tizen.Multimedia.AudioManager` class:

    ```csharp
    void OnVolumeChanged(object sender, VolumeChangedEventArgs args)
    {
        Tizen.Log.Info("AudioManager", $"{args.Type} volume changed to {args.Level}");
    }

    AudioManager.VolumeController.Changed += OnVolumeChanged;
    ```

    When the volume changes, the event handler provides in its parameters the audio type that has changed and the new volume level.

-   To retrieve the current and maximum volumes for a specific audio type, use the `VolumeController.Level` and `VolumeController.MaxLevel` properties of the `Tizen.Multimedia.AudioManager` class:

    ```csharp
    var type = AudioVolumeType.Media;

    var curVol = AudioManager.VolumeController.Level[type];

    var maxVol = AudioManager.VolumeController.MaxLevel[type];
    ```

-   To set the volume level, use the `VolumeController.Level` property.

    In the following example, a value is received from application UI slider, with which the user sets the volume level.

    ```csharp
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
    1.  Retrieve the list of the currently connected audio devices with the `GetConnectedDevices()` method of the [Tizen.Multimedia.AudioManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.AudioManager.html) class:

        ```csharp
        IEnumerable<AudioDevice> connectedDevices = AudioManager.GetConnectedDevices();
        ```

    2.  Retrieve the device information from the [Tizen.Multimedia.AudioDevice](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.AudioDevice.html) class, which has the following properties:
        -   `Type`: Device type
        -   `IoDirection`: Device IO direction
        -   `Id`: Device ID
        -   `Name`: Device name
        -   `IsRunning`: Device running state

-   To get a notification when the audio device connection or state changes, add event handlers for the `DeviceConnectionChanged` and `DeviceRunningChanged` events of the `Tizen.Multimedia.AudioManager` class:
    -   To receive a notification whenever the device connection state changes:

        ```csharp
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

        ```csharp
        void OnDeviceRunningChanged(object sender, AudioDeviceRunningChangedEventArgs args)
        {
            if (args.Device.Type == AudioDeviceType.BluetoothMedia)
            {
                if (args.Device.IsRunning == false)
                    /// Bluetooth device is not running, handle accordingly
                else
                    /// Handle accordingly
            }
            else
            {
                /// Handle accordingly
            }
        }

        AudioManager.DeviceRunningChanged += OnDeviceRunningChanged;
        ```


        > **Note**
        >
        > The initial running state of the connected device is `false`, which means the connected device is not running.

-   To utilize additional functionality for USB audio type and output direction device, use the [Tizen.Multimedia.AudioDevice](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.AudioDevice.html) class:
    -   To get the device of USB audio type and output direction:
        ```csharp
        AudioDevice usbOutputDevice = null;
        foreach(AudioDevice d in AudioManager.GetConnectedDevices())
        {
            if (d.Type == AudioDeviceType.UsbAudio && d.IoDirection == AudioDeviceIoDirection.Output)
            {
                usbOutputDevice = d;
                break;
            }
        }
        ```

    -   To get the supported sample formats and to set the specific sample format:

        1.  Retrieve the list of the currently supported sample formats with the `GetSupportedSampleFormats()` method:

            ```csharp
            IEnumerable<AudioSampleFormat> supportedFormats = usbOutputDevice.GetSupportedSampleFormats();
            ```

        2.  Select one of the supported sample formats, then set it with the `SetSampleFormat()` method:

            ```csharp
            usbOutputDevice.SetSampleFormat(AudioSampleFormat.S16LE);
            ```

    -   To get the supported sample rates and to set the specific sample rate:

        1.  Retrieve the list of the currently supported sample rates with the `GetSupportedSampleRates()` method:

            ```csharp
            IEnumerable<uint> supportedRates = usbOutputDevice.GetSupportedSampleRates();
            ```

        2.  Select one of the supported sample rates, then set it with the `SetSampleRate()` method:

            ```csharp
            usbOutputDevice.SetSampleRate(48000);
            ```
## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
