# Audio Management


You can control the audio behavior of the application. You can control the output volume and sound conflict scenarios. You can also query various information from sound devices. You can also use OpenAL to specify the objects and operations in producing low-latency audio output.

You can use the following audio management features in your native applications:

- [OpenAL](openal.md)

  You can use OpenAL software interface to audio hardware for a variety of audio playback tasks (such as sound effects in games). You can create a context, request a source and buffer, and control the audio stream with OpenAL.

- [Sound Manager](sound-manager.md)

  You can control the output volume of a specific volume type (aka sound type). You can define which stream type is used for a playback or recording handle in your application, and manage sound conflict senarios by using stream focus. You can also query for various information related to the connected sound devices, for example, type, name, id, direction and state.

- [Sound Pools](sound-pool.md)

  You can use sound pools, which are basically collections of sounds. You can load multiple sound sources to a sound pool and manage their playback as a group.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
