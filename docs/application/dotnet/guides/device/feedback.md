# Sound and Vibration Feedback


You can play sound and vibration feedback with a specific pattern.

The main features of the `Tizen.System.Feedback` class are:

-   Playing a specific feedback pattern

    You can [play a sound or vibrate with a specific pattern](#playtype), or both. For a list of supported feedback patterns, see the [Tizen.System.Feedback](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Feedback.html) class reference.

-   Checking for pattern support

    You can [determine whether a specific pattern is supported](#support) for a given feedback type.

## Prerequisites

To enable your application to use the feedback functionality:

1.  To use vibration feedback, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/haptic</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the `Tizen.System.Feedback` class, include the [Tizen.System](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.html) namespace in your application:

    ```
    using Tizen.System;
    ```

<a name="playtype"></a>
## Playing Feedback with a Specific Type and Pattern

To play a specific feedback pattern with a specific feedback type:

1.  Create a new instance of the [Tizen.System.Feedback](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Feedback.html) class:

    ```
    Feedback feedback = new Feedback();
    ```

2.  Play the feedback with the `Play()` method of the `Tizen.System.Feedback` class. As parameters, enter the feedback type (defined by the [Tizen.System.FeedbackType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.FeedbackType.html) enumeration), and a string to denote the pattern to be played:

    ```
    feedback.Play(FeedbackType.Sound, "Tap");
    ```

3.  To stop the feedback, use the `Stop()` method:

    ```
    feedback.Stop();
    ```

<a name="support"></a>
## Checking for Pattern Support

To determine whether a specific pattern is supported for a specific feedback type, use the `IsSupportedPattern()` method of the [Tizen.System.Feedback](https://developer.tizen.org/dev-guide/csapi/api/Tizen.System.Feedback.html) class:

```
bool support;
Feedback feedback = new Feedback();
support = feedback.IsSupportedPattern(FeedbackType.Vibration, "Key0");
```

The return value defines whether the pattern is supported for the feedback type.



## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
