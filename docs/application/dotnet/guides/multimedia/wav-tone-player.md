# WAV and Tone Player

You can play different audio formats.

The main media playback features are described below:

- Using the WAV player

    Enables you to play audio in the [WAVE format](#wav).

- Using the tone player

    Enables you to play [tones](#tone).

These players support only simple audio playback. If you need more advanced features, please refer to [Media Playback](media-playback.md).

<a name="wav"></a>
## WAV player

The [Tizen.Multimedia.WavPlayer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.WavPlayer.html) class allows you to play audio resources (media files stored on the device). Use it to [play audio and control playback](#start_wav). You can use the WAV and OGG audio formats.

Multiple instances of the WAV player can be used to play several audio data streams concurrently. This means that your application can play multiple uncompressed audio files, such as WAV, at the same time.

<a name="tone"></a>
## Tone player

You can play a tone or a list of tones using the [Tizen.Multimedia.TonePlayer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.TonePlayer.html) class.

To play tones, use a DTMF (Dual Tone Multi Frequency) preset frequency. The possible values are defined in the [Tizen.Multimedia.ToneType](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.ToneType.html) enumeration.

You can [start and stop playing a tone](#play_tone), and [play a tone for a specified duration](#duration).

## Prerequisites

To use the methods and properties of the media playback classes, include the [Tizen.Multimedia](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.html) namespace in your application:

```csharp
using Tizen.Multimedia;
```


<a name="start_wav"></a>
## Start and stop the WAV player

To start and stop the WAV player, proceed as follows:

1.  To play a WAV file, use the `StartAsync()` method of the [Tizen.Multimedia.WavPlayer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.WavPlayer.html) class:

    ```csharp
    await WavPlayer.StartAsync(wavPath, new AudioStreamPolicy(AudioStreamType.Media));
    ```

    To set the path of your WAV file, you potentially need to retrieve the default path for audio files.

2.  To stop the WAV player, use the `StartAsync()` method with the `cancellationToken` parameter:

    ```csharp
    var cancellationTokenSource = new CancellationTokenSource();

    WavPlayer.StartAsync(wavPath, new AudioStreamPolicy(AudioStreamType.Media), cancellationTokenSource);

    cancellationTokenSource.Cancel();
    ```

<a name="play_tone"></a>
## Playing a tone

To start and stop playing a tone, proceed as follows:

1.  To start playback, use the `StartAsync()` method of the [Tizen.Multimedia.TonePlayer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.TonePlayer.html) class.

    The first parameter defines the tone type as a value of the [Tizen.Multimedia.ToneType](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.ToneType.html) enumeration:

    ```csharp
    await TonePlayer.StartAsync(ToneType.Default, new AudioStreamPolicy(AudioStreamType.Media), -1);
    ```

2.  To stop playback, use the `StartAsync()` method with the `cancellationToken` parameter:

    ```csharp
    var cancellationTokenSource = new CancellationTokenSource();

    TonePlayer.StartAsync(ToneType.Default, new AudioStreamPolicy(AudioStreamType.Media), -1, cancellationTokenSource);

    cancellationTokenSource.Cancel();
    ```

<a name="duration"></a>
## Playing a tone for a specified duration

To play a tone for a specified duration, use the `StartAsync()` method of the [Tizen.Multimedia.TonePlayer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.TonePlayer.html) class with the duration parameter (the number of milliseconds you want playback to last). When you set the duration to a specified time, playback stops automatically after that time:

```csharp
await TonePlayer.StartAsync(ToneType.Default, new AudioStreamPolicy(AudioStreamType.Media), duration);
```

## Related information
* Dependencies
  -   Tizen 4.0 and Higher
