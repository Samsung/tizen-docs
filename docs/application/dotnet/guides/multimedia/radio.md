# Radio

You can control the radio hardware in a device to provide radio playback in your application.

The main features of the `Tizen.Multimedia.Radio` class include:

-   Switching the radio on and off

    You can switch the radio on and off using the `Start()` and `Stop()` methods of the `Tizen.Multimedia.Radio` class.

-   Scanning for radio frequencies

    You can [scan for all available frequencies](#scan).

-   Tuning the radio

    You can [select and start playing a radio frequency](#tune) by using the `Frequency` property of the `Tizen.Multimedia.Radio` class.

-   Searching for an adjacent channel

    You can [seek an adjacent channel](#seek) with the `SeekUpAsync()` and `SeekDownAsync()` methods.

You can only have one radio instance active at a time. Radio playback can be interrupted by another radio application.

## Prerequisites


To enable your application to use the radio functionality:

1.  To use the methods and properties of the [Tizen.Multimedia.Radio](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Radio.html) class, include the [Tizen.Multimedia](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.html) namespace in your application:

    ```
    using Tizen.Multimedia;
    ```

2.  Create an instance of the `Tizen.Multimedia.Radio` class:

    ```
    Radio radio = new Radio();
    ```

3.  To receive notifications when radio playback is interrupted, register an event handler for the `Interrupted` event of the `Tizen.Multimedia.Radio` class. Radio playback is interrupted, for example, when the radio application moves to the background.

    ```
    radio.Interrupted += OnRadioInterrupted;

    void OnRadioInterrupted(object sender, RadioInterruptedEventArgs args)
    {
        switch (args.Reason)
        {
            case RadioInterruptedReason.ResourceConflict:
                /// Application that was the source of the conflict is now closed
                /// Restart the radio playback here
                break;
            default:
                /// Radio listening is interrupted
                /// Release the application resources or save the current state here
                break;
        }
    }
    ```

<a name="scan"></a>
## Scanning for Radio Frequencies

To scan for all available radio frequencies:

1.  Register and define event handlers for the events of the [Tizen.Multimedia.Radio](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Radio.html) class:
    -   To receive a notification each time the scan finds a new frequency, register an event handler for the `ScanUpdated` event. The event provides the kHz value of the found frequency.

        ```
        radio.ScanCompleted += OnScanCompleted;

        void OnScanUpdated(object sender, ScanUpdatedEventArgs args)
        {
            /// Store the radio channels in the array
            /// Frequency values represent the kHz of the channel
            Tizen.Log.Info("Radio", $"Frequency: {args.Frequency}");
        }
        ```

         > **Note**   
		 > Do not use radio operations (such as changing the `Frequency` property value or calling the `Start()` method) in the scan updated event handler.


    -   To receive a notification when the scan is complete, register an event handler for the `ScanCompleted` event:

        ```
        radio.ScanCompleted += OnScanCompleted;

        void OnScanCompleted(object sender, EventArgs args)
        {
            /// Frequency scanning is completed
            /// Tune in to one of the scanned frequencies and start listening
        }
        ```

2.  Start scanning using the `StartScan()` method of the `Tizen.Multimedia.Radio` class:

    ```
    radio.StartScan();
    ```

    The scanning time depends on the environment (the strength of the radio signal).

    To cancel the scan before it completes, use the `StopScan()` method.

<a name="tune"></a>
## Tuning the Radio

To select and start playing a frequency:

1.  Set the frequency you want to play using the `Frequency` property of the [Tizen.Multimedia.Radio](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Radio.html) class:

    ```
    radio.Frequency = newFrequncey;
    ```

2.  Start playing the frequency using the `Start()` method of the `Tizen.Multimedia.Radio` class:

    ```
    radio.Start();
    ```

    If the radio emits no sound, check the signal strength with the `SignalStrength` property of the `Tizen.Multimedia.Radio` class. The property returns the current signal strength as a dBuV value.

<a name="seek"></a>
## Searching for an Adjacent Channel

To search for and tune in to an adjacent channel, use the `SeekUpAsync()` and `SeekDownAsync()` methods of the [Tizen.Multimedia.Radio](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Multimedia.Radio.html) class. This is similar to the scanning operation, but only the nearest active frequency is searched for. Once the maximum frequency is reached in either direction, the search ends, and the radio is set to that frequency.

For example, to seek down, use the `SeekDownAsync()` method:

```
var newFrequncey = await radio.SeekDownAsync();

/// Search is complete, and the radio is tuned in to the new frequency
/// Application sets the new frequency and updates the user interface
```

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
