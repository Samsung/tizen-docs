# Sound and Vibration Feedback


You can play feedback with a specific pattern or play it with a specific type and pattern. You can also check whether a specific pattern is supported.

The main features of the Feedback API include:

- Playing a specific feedback pattern

  You can [play a sound or vibrate with a specific pattern, or both](#play).

- Playing feedback for a specific type and pattern

  You can [play a sound and vibrate with a specific type and pattern](#playtype).

- Checking for pattern support

  You can [determine whether a specific pattern is supported](#support).

You can play a feedback pattern using sound or vibration:

- Sound management

  You can request the sound-server to play a sound by using the mm-keysound library.

  You can use sound feedback with the `feedback_play()` or `feedback_play_type()` function. The attribute for the sound type is `FEEDBACK_TYPE_SOUND`.

- Vibration management

  You can request the device to vibrate by using a dbus method call. A haptic monotone or haptic effect is requested to device, based on the vibration data type in the `vibration.conf` configuration.

  You can use vibration feedback with the `feedback_play()` or `feedback_play_type()` function. The attribute for the vibration type is `FEEDBACK_TYPE_VIBRATION`.

## Prerequisites

To use the functions and data types of the Feedback API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__FEEDBACK__MODULE.html) applications), include the `<feedback.h>` header file in your application:

```
#include <feedback.h>
```

<a name="play"></a>
## Playing Feedback with a Specific Pattern

To play a sound and vibrate with a specific pattern, use the `feedback_play()` function.

Internally, the function invokes the `sound_play` or `vibrator_play` feedback type. It returns success when the pattern enum is valid.

```
int ret;
ret = feedback_play(pattern);
```

The return value defines whether playing the feedback was successful.

<a name="playtype"></a>
## Playing Feedback with a Specific Type and Pattern

To play a sound and vibrate with a specific type and pattern, use the `feedback_play_type()` function.

Internally, the function invokes the `sound_play` or `vibrator_play` feedback type. It returns success when the pattern enum is valid.

```
static int ret;
ret = feedback_play_type(type, pattern);
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

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
