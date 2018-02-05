# Creating Applications with Sensors

A sensor is a device that detects or senses various signals or stimuli,
such as acceleration, distance, orientation, and magnetic field
strength, and transmits the resulting measurement. If you want to create
applications that offer sensor features to the user, Tizen provides
various options for you.

In a smart device application UI, sensors are useful in monitoring user
gestures and motions.

When creating a sensor application, you can implement the following
features:

-   [Accelerator sensor usage](app-sensor-accelerator.md)

    The accelerator sensor is used to measure changes in force resulting
    from fall, tilt, positioning, shock, and vibration. Smart devices
    rotate their display between portrait and landscape mode depending
    on how the user tilts the phone.

    -   To avoid annoyance, you can determine whether the accelerator
        sensor is supported on the device before displaying the
        application features to the user.
    -   You can request accelerator sensor events to be delivered to the
        application, where you can process and display them.
    -   You can save the maximum acceleration value of the device
        during testing.

        
- [Proximity sensor usage](app-sensor-proximity.md)

    The proximity sensor measures the distance of an object from the
    front of the phone. It is commonly used on smart devices to detect
    (and skip) accidental touchscreen taps when held to the ear during
    a call.

    -   To avoid annoyance, you can determine whether the proximity
        sensor is supported on the device before displaying the
        application features to the user.
    -   You can request proximity sensor events to be delivered to the
        application, where you can process and display them.
