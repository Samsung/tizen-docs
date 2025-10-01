# Sound and Vibration Feedback


You can play feedback with a specific pattern or play it with a specific type and pattern. You can also check whether a specific pattern is supported.

The main features of the Feedback API include:

- Playing a specific feedback pattern

  You can [play a sound or vibrate with a specific pattern, or both](#play).

- Playing feedback for a specific type and pattern

  You can [play a sound and vibrate with a specific type and pattern](#playtype).

- Checking for pattern support

  You can [determine whether a specific pattern is supported](#support).

- Stopping vibration feedback play

  You can [stop a vibration feedback pattern](#stop).

You can play a feedback pattern using sound or vibration:

- Sound management

  You can request the sound-server to play a sound by using the mm-keysound library.

  You can use sound feedback with the `feedback_play()` or `feedback_play_type()` function. The attribute for the sound type is `FEEDBACK_TYPE_SOUND`.

- Vibration management

  You can request the device to vibrate by using a dbus method call. A haptic monotone or haptic effect is requested to device, based on the vibration data type in the `vibration.conf` configuration.

  You can use vibration feedback with the `feedback_play()` or `feedback_play_type()` function. The attribute for the vibration type is `FEEDBACK_TYPE_VIBRATION`.

## Prerequisites

To use the functions and data types of the [Feedback API](../../api/common/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html), include the `<feedback.h>` header file in your application. And also use `feedback_initialize()` and `feedback_deinitialize()`:

```
#include <feedback.h>

// Call before use feedback function.
int ret = feedback_initialize();
if (ret == FEDDBACK_ERROR_NONE) {
  // If no longer need to user feedback, then deinitialize.
  feedback_deinitialize();
}
```

<a name="play"></a>
## Playing Feedback with a Specific Pattern

To play a sound and vibrate with a specific pattern, use the `feedback_play()` function.

Internally, the function invokes the `sound_play` or `vibrator_play` feedback type. It returns success when the pattern enum is valid.

```
int ret = feedback_initialize();
if (ret == FEEDBACK_ERROR_NONE) {
    ret = feedback_play(pattern);
    feedback_deinitialize();
}
```

The return value defines whether playing the feedback was successful.

<a name="playtype"></a>
## Playing Feedback with a Specific Type and Pattern

To play a sound and vibrate with a specific type and pattern, use the `feedback_play_type()` function.

Internally, the function invokes the `sound_play` or `vibrator_play` feedback type. It returns success when the pattern enum is valid.

```
static int ret;
ret = feedback_initialize();
if (ret == FEEDBACK_ERROR_NONE) {
    ret = feedback_play_type(type, pattern);
    feedback_deinitialize();
}
```

The return value defines whether playing the feedback was successful.

<a name="support"></a>
## Checking for Pattern Support

To determine whether a specific pattern is supported for a specific feedback type, use the `feedback_is_supported_pattern()` function.

Internally, the function invokes the `sound_is_supported` or `vibrator_is_supported` feedback type.

```
static int ret;
bool status;
ret = feedback_is_supported_pattern(type, pattern, &status);
```

The return value defines whether retrieving the feedback information was successful.

<a name="stop"></a>
## Stopping Vibrate Feedback Play
To stop vibration patterns, user the `feedback_stop()` function.
But this function does not support to stop media sound actions.

```
int ret = feedback_initialize();
if (ret == FEEDBACK_ERROR_NONE) {
    feedback_play_type(FEEDBACK_TYPE_HAPTIC, FEEDBACK_PATTERN_TAP);
    feedback_stop();
    feedback_deinitialize();
}
```

## Related Information
- Dependencies
  - Since Tizen 2.4
- API References
  - [Feedback API](../../api/common/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html)
