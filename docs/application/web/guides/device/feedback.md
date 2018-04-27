# Sound and Vibration Feedback

You can handle feedback patterns (media or vibration) that can be played as a reaction to specified actions.

This feature is supported in mobile and wearable applications only.

The main features of the Feedback API include:

- Checking for pattern support

  You can [determine whether a specified media pattern type is available](#checking-the-pattern).

- Setting a pattern

  You can [set a predefined system pattern to be played as a reaction](#setting-the-media-pattern) to specific actions.

Each feedback pattern can have separate media files of sound and vibration type. For example, when receiving a new email message, a predefined sound and vibration feedback pattern can be played.

## Checking the Pattern

You can check whether a feedback type (sound or vibration) is supported for a specified pattern. To get information about the supported specified system predefined pattern type pairs, use the `isPatternSupported()` method of the `FeedbackManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/feedback.html#FeedbackManager) and [wearable](../../api/latest/device_api/wearable/tizen/feedback.html#FeedbackManager) applications):

```
var pattern = 'BT_CONNECTED', type = 'TYPE_SOUND';
var isSupported = tizen.feedback.isPatternSupported(pattern, type);
var isSupportedStr = '';
if (!isSupported) {
    isSupportedStr = ' not';
}
console.log('pattern ' + pattern + ' is' + isSupportedStr + ' supported');
```

## Setting the Media Pattern

The available predefined system patterns are defined in the `FeedbackPattern` enumeration (in [mobile](../../api/latest/device_api/mobile/tizen/feedback.html#FeedbackPattern) and [wearable](../../api/latest/device_api/wearable/tizen/feedback.html#FeedbackPattern) applications).

To start and stop playing various types of predefined reactions:

1. To set a specified type of reaction for an event, use the `play()` method of the `FeedbackManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/feedback.html#FeedbackManager) and [wearable](../../api/latest/device_api/wearable/tizen/feedback.html#FeedbackManager) applications):

   ```
   try {
       tizen.feedback.play('CHARGERCONN');
   } catch (err) {
       console.log(err.name + ': ' + err.message);
   }
   ```

2. To stop reacting to predefined actions, use the `stop()` method of the `FeedbackManager` interface:

   ```
   tizen.feedback.stop();
   ```

## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for Mobile
   - Tizen 3.0 and Higher for Wearable
