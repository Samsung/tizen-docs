# STC


STC means Smart Traffic Control. It provides extensible packet-level control services, including per-app data usage, total data quota, and background app's data saving. STC Library provides APIs fulfilling below mentioned features for application development.

This feature is supported in mobile, tv and wearable profile.

The main features of the STC API include:

- Retrieve Data Usage For System

  You can [retrieve network data consumed by system](#retrieve-data-usage-for-system).

- Retrieve Data Usage For Applications

  You can [retrieve network data consumed by applications](#retrieve-data-usage-for-applications).


> **Note**  
> You can test the STC functionality on a target device only. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the STC API:

1.  To use the [Tizen.Network.Stc](https://samsung.github.io/TizenFX/latest/api/Tizen.Network.Stc.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/network.get</privilege>
       <privilege>http://tizen.org/privilege/network.set</privilege>
       <privilege>http://tizen.org/privilege/network.profile</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Network.Stc namespace, include it in your application:

    ```
    using Tizen.Network.Stc;
    ```
