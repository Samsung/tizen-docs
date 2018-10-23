# OpenAL


OpenAL is a software interface to audio hardware, which allows you to specify the objects and operations in producing high quality audio output. Tizen offers OpenAL as a native API, since OpenAL can be used for a variety of audio playback tasks (such as sound effects in games), and it has an excellent performance for real-time rendering. For more information, see [OpenAL 1.1 specification](http://www.openal.org/documentation/openal-1.1-specification.pdf).

OpenAL has three fundamental objects:

- Sources

  Sources store various attributes, such as velocity, position, direction, and intensity of the sound, that are used for rendering and have an associated buffer which contains audio data for playback.

- Buffers

  Buffers store compressed or uncompressed audio data in PCM format. It also stores in 8-bit or 16-bit in mono or stereo format.

- Single listener

  Each audio context consists of one listener. Use listener attribute to represent where the user is hearing the audio from.

Each object can be changed independently. Ensure that the setting of one object does not affect the settings of other object.

The main features of the OpenAL API include:

- Creating a context

  You must first open an audio device through which your audio stream flows. After the device is successfully opened, create and activate a context. Once your device is associated with a current context, your commands are applied to that context.

  To create a context:

  ```
  /* Open default device */
  device = alcOpenDevice(NULL);
  if (device != NULL) {
      /* Create context */
      context=alcCreateContext(device, NULL);
      if (context != NULL) {
          /* Set active context */
          alcMakeContextCurrent(context);
      }
  }
  ```

  When your audio stream is no longer needed or inactive for a long time, destroy the context by calling the `alcDestroyContext()` function.

  > **Note**  
  > The device cannot fall into a sleep state while the context is not destroyed. To avoid unwanted battery consumption, destroy the context punctually.
  >
  > Since 3.0, extension `alcDevicePauseSOFT()` was introduced to allow applications to pause a playback device explicitly.
  > The main purpose is to silence output, stop processing, and to allow audio hardware to go into low-power mode.
  > Additionally, you can use `alcDeviceResumeSOFT()` function to resume playback of a paused device.  
  > For more information, see [here](http://kcat.strangesoft.net/openal-extensions/SOFT_pause_device.txt).

- Requesting a source and buffer

  To play a sound, a source object is required. Through the source, you can update the stream attributes, such as the default gain and the position of the sound.

  In addition, you need to [request an audio buffer](#request) that contains your audio data.

- Controlling the audio stream

  When the source and buffer are ready, you can [manage the playback](#play) by playing, stopping, rewinding, or pausing your audio stream. All the control commands are operated with the source you have acquired.

To use OpenAL, you must create a context and the initial set of buffers, load the buffers with sample data, create sources, attach the buffers to the sources, set the locations and directions for the listener and sources, and set the initial values for the OpenAL state global. You can also [queue buffers](#buffer).

For additional OpenAL code samples, see [Example Code](http://kcat.strangesoft.net/openal.html#examples).

## Prerequisites

To enable your application to use the OpenAL functionality:

1. To use the functions and data types of the OpenAL API (in [mobile](../../api/mobile/latest/group__OPENSRC__OPENAL__FRAMEWORK.html) and [wearable](../../api/wearable/latest/group__OPENSRC__OPENAL__FRAMEWORK.html) applications), include the `<AL/al.h>` and `<AL/alc.h>` header files in your application:

   ```
   #include <AL/al.h>
   #include <AL/alc.h>
   ```

2. Retrieve the default device name, and open the default device.

   The following example code verifies that a given extension is available, retrieves the names of all available devices and the name of the default device using the `alcGetString()` function, and opens the default device using the `alcOpenDevice()` function:

   ```
   /* Verify that a given extension is available for the current context */
   enumeration = alcIsExtensionPresent(NULL, "ALC_ENUMERATION_EXT");
   if (enumeration == AL_FALSE)
       LOGI("[%s] enumeration extension not available", __func__);

   /*
      Retrieve a list of available devices
      Each device name is separated by a single NULL character
      and the list is terminated with 2 NULL characters
   */
   deviceNameList = alcGetString(NULL, ALC_DEVICE_SPECIFIER));

   /* Retrieve the default device name */
   defaultDeviceName = alcGetString(NULL, ALC_DEFAULT_DEVICE_SPECIFIER);

   /* Open the default device */
   device = alcOpenDevice(defaultDeviceName);
   if (!device) {
       LOGI("[%s] unable to open default device", __func__);

       return;
   }

   LOGI("[%s] Device: %s ", __func__, alcGetString(device, ALC_DEVICE_SPECIFIER));
   ```

   The `alcOpenDevice()` function opens the audio device through the PulseAudio.

   > **Note**  
   > Tizen 3.0 works with a stream information concept. To integrate OpenAL with stream information, use the `alcOpenDeviceNew()` function (since Tizen 3.0) instead of the `alcOpenDevice()` function, and give the sound stream information handle as a parameter. To create the handle, include the `sound_manager.h` header file and call the `sound_manager_create_stream_information()` function.

3. If the device is opened successfully, create a context for the device using the `alcCreateContext()` function, and set the context as active using the `alcMakeContextCurrent()` function:

   ```
   /* Create context */
   context = alcCreateContext(device, NULL);
   if (context == NULL) {
       alcCloseDevice(device);
       LOGI("[%s] failed to create context", __func__);

       return;
   }

   /* Set active context */
   if (!alcMakeContextCurrent(context)) {
       alcDestroyContext(context);
       alcCloseDevice(device);
       LOGI("[%s] failed to make default context", __func__);

       return;
   }
   ```

   Once the device is associated with an active context, the AL commands are applied to that context.

<a name="request"></a>
## Requesting a Source and Audio Buffer

Playback requires a source object for controlling the playback, and a buffer object for storing the audio data to be played.

To request a source and audio buffer:

1. Request the source using the `alSources()` function, and update the source attributes, such as the default gain and sound position:

   ```
   /* Request a source name */
   alGenSources((ALuint)1, &source);

   /* Set the default volume */
   alSourcef(source, AL_GAIN, 1);

   /* Set the default position of the sound */
   alSource3f(source, AL_POSITION, 0, 0, 0);
   ```

2. Request the audio buffer, and specify the allocated PCM buffer and size:

   ```
   /* Request a buffer name */
   alGenBuffers(1, &buffer);

   ALuint frequency = 22050;
   ALenum format = AL_FORMAT_MONO8;

   /* Specify sample data using alBufferData */
   alBufferData(buffer, format, _data_buffer, dataSize, frequency);
   ```

   In the above example code, the `_data_buffer` parameter points to the audio sample data. The memory for the data has been allocated using the `malloc()` function. The `dataSize` parameter defines the amount of data to be buffered.

   The following table lists the supported audio sample formats:

   **Table: Supported audio sample formats**

   | Format               | Description                              |
   |----------------------|------------------------------------------|
   | `AL_FORMAT_MONO8`    | Unsigned 8-bit mono audio sample         |
   | `AL_FORMAT_MONO16`   | Unsigned 16-bit mono audio sample        |
   | `AL_FORMAT_STEREO8`  | Unsigned 8-bit stereo audio sample (interleaved) |
   | `AL_FORMAT_STEREO16` | Unsigned 16-bit stereo audio sample (interleaved) |

<a name="play"></a>
## Controlling Audio Stream Playback

To control the playback, use the following state transition functions:

- `alSourcePlay()`: Play, replay, or resume a source.
- `alSourceStop()`: Stop 1 or more sources.
- `alSourceRewind()`: Rewind a source (set the playback position to the beginning).
- `alSourcePause()`: Pause a source.

To start and stop playback:

1. To play the audio stream, implement the start event of the playback action (for example, a start button click).

   In the following example code, the whole audio buffer is allocated and filled before the playback starts using the `alSourcei()` function. The second parameter specifies the source type as static. Start the playback after changing the state to play.

   ```
   /* Function: _on_click1() */
   /* Source specifies the current buffer object */
   alSourcei(source, AL_BUFFER, buffer);

   /* Change the state to play */
   alSourcePlay(source);
   ```

2. When a stop event is triggered, change the playback state to stop to end the playback:

   ```
   /* Function: _on_click2() */
   /* Change the state to stop */
   alSourceStop(source);
   ```

3. When the playback is finished, release the resources by cleaning up the source, buffer, context, and device:

   ```
   alDeleteSources(1, &source);
   alDeleteBuffers(1, &buffer);
   device = alcGetContextsDevice(context);
   alcMakeContextCurrent(NULL);
   alcDestroyContext(context);
   alcCloseDevice(device);
   ```

<a name="buffer"></a>
## Using Buffer Queuing for Stream Playback

OpenAL provides a buffer queuing method for the streamed audio source, in which 1 or more buffers can be queued and dequeued after consumed.

To queue and play multiple buffers:

1. Submit 1 or more buffers before starting the playback:

   ```
   #define DATA_CHUNK_SIZE (1024)

   /* This example uses 4 buffers and 1 source */
   static ALuint buffer[4], source;

   alGenSources((ALuint)1, &source);
   alGenBuffers(4, buffer);

   /* Fill all the buffers with audio data from the wave file */
   for (iLoop = 0; iLoop < 4; iLoop++) {
       alBufferData(buffer[iLoop], AL_FORMAT_MONO8, pData, DATA_CHUNK_SIZE, 22050);
       alSourceQueueBuffers(source, 1, &buffer[iLoop]);
   }
   ```

2. Start the playback stream, and push the buffer (for example, 1024 bytes) periodically on click events.

   If a loop detects a consumed buffer (`iBuffersProcessed`) by querying `AL_BUFFERS_PROCESSED`, dequeue the consumed buffer using the `alSourceUnqueueBuffers()` function. To continue the playback, fill and queue the buffer again using the `alSourceQueueBuffers()` function. Run the loop in a thread separate from the application main thread.

   ```
   /* Start playing the streamed audio */
   alSourcePlay(source);
   LOGI("[%s] alSourcePlay", __func__);

   /* Buffer queuing loop must operate in a new thread */
   iBuffersProcessed = 0;
   while (!thread_finish) {
       usleep(10 * 1000); /* Sleep 10 msec periodically */

       alGetSourcei(source, AL_BUFFERS_PROCESSED, &iBuffersProcessed);

       iTotalBuffersProcessed += iBuffersProcessed;
       LOGI("Buffers Processed %d", iTotalBuffersProcessed);

       /*
          For each processed buffer, remove it from the source queue,
          read the next chunk of audio data from the file,
          fill the buffer with new data, and add it to the source queue
       */
       while (iBuffersProcessed) {
           /*
              Remove the buffer from the queue
              (uiBuffer contains the buffer ID for the dequeued buffer)
           */
           uiBuffer = 0;
           alSourceUnqueueBuffers(source, 1, &uiBuffer);

           /* Read more pData audio data (if there is any) */

           /* Copy audio data to buffer */
           alBufferData(uiBuffer, AL_FORMAT_MONO8, pData, DATA_CHUNK_SIZE, 22050);
           /* Insert the audio buffer to the source queue */
           alSourceQueueBuffers(source, 1, &uiBuffer);

           iBuffersProcessed--;
       }
   }
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
