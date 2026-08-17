
# Application Filtering


The Tizen platform provides a wide range of features across a variety of
hardware and software components. Among the features, some can be selectively supported by the Tizen device manufacturer. For
application stores to correctly select your application for installation
on an appropriate device, the feature and profile information must be
correctly declared in your application.

<a name="filter_n"></a>
## Feature-based filtering


Some features can be selectively supported by the Tizen device
manufacturer. To prevent problems when the user is trying to run your
application on a device that does not support all the features your
application is using, do one of the following:

-   When the application is running, check whether the device supports
    the needed features. If not, the application can use other features,
    which are supported by the device, as a workaround.

    For example, if an application wants to use location information, it
    can check the device capability by using the `system_info_get_XXX()`
    function of the System Information API (in
    [mobile](../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html)
    and
    [wearable](../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html) applications).
    If the device supports GPS, the application uses GPS information,
    and if the device supports WPS only, the application uses WPS
    information instead of GPS.

- Use feature-based filtering to prevent your application from being
    shown in the application list on the official site for Tizen applications, if the user's
    device does not support all the features of your application. This
    way you can prevent the application from being installed on an
    unsupported device in the first place.

    Be careful when defining the feature list for
    feature-based filtering. The feature list can dramatically reduce
    your chances of getting the application downloaded by reducing the
    number of devices which can support the application.

If the `tizen-manifest.xml` file of the application package includes a
feature list, the store compares the capabilities of the device
with the required feature conditions of the application. The store only
lists the applications whose conditions match the capabilities of the
device and thus prevents incompatible applications from being
installed.

**Figure: Feature-based filtering**

![Feature-based filtering](./media/app_filtering_basic_flow.png)

When multiple features are defined in the feature list for feature-based
filtering, the store creates the filtering condition for all using
the "AND" operation. For example, if there are
`http://tizen.org/feature/network.nfc` and
`http://tizen.org/feature/network.bluetooth` features in the feature
list of the application package, only a device that has both those
features can show the application on the store application list
for downloading.

<a name="screen_size"></a>
### Screen size feature

The screen size feature is the only exception to the normal feature
handling process described above. When the screen size is defined in the
feature list, the store creates the filtering condition with the
"OR" operation. For example, if the
`http://tizen.org/feature/screen.size.normal.480.800` and
`http://tizen.org/feature/screen.size.normal.720.1280` features are
defined in your application feature list, a device that supports one or
the other of those features can show the application on the store
application list.

If you do not specify a proper screen size in the `tizen-manifest.xml`
file, your application can be rejected from the store.

The following table lists the available screen size features:

**Table: Available screen size features**

| Feature key                              | Description                              | Since |
|----------------------------------------|----------------------------------------|-----|
| `http://tizen.org/feature/screen.size.normal` | Specify this key, if the application supports all possible current and future resolutions on the normal screen size.<br><br>You cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously. If you do, only the most specific resolution key is considered and the less specific resolution keys are ignored. For example, if you specify both `http://tizen.org/feature/screen.size.normal` and `http://tizen.org/feature/screen.size.normal.320.480` keys, only the `http://tizen.org/feature/screen.size.normal.320.480` key is applied.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.240.400` | Specify this key, if the application supports the 240 x 400 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.320.320` | Specify this key, if the application supports the 320 x 320 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.3   |
| `http://tizen.org/feature/screen.size.normal.320.480` | Specify this key, if the application supports the 320 x 480 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.360.360` | Specify this key, if the application supports the 360 x 360 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.3.2 |
| `http://tizen.org/feature/screen.size.normal.360.480` | Specify this key, if the application supports the 360 x 480 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.3   |
| `http://tizen.org/feature/screen.size.normal.480.800` | Specify this key, if the application supports the 480 x 800 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.540.960` | Specify this key, if the application supports the 540 x 960 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.600.1024` | Specify this key, if the application supports the 600 x 1024 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.720.1280` | Specify this key, if the application supports the 720 x 1280 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.1080.1920` | Specify this key, if the application supports the 1080 x 1920 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.all` | Specify this key, if the application supports all possible current and future screen sizes and all possible current and future resolutions per screen size.<br><br>You cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously. If you do, only the most specific resolution key is considered and the less specific resolution keys are ignored. For example, if you specify both `http://tizen.org/feature/screen.size.all` and `http://tizen.org/feature/screen.size.normal.320.480` keys, only the `http://tizen.org/feature/screen.size.normal.320.480` key is applied.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |

<a name="hierarchy"></a>
### Feature hierarchy

The feature keys have a hierarchy. For example, consider the
`http://tizen.org/feature/location`,
`http://tizen.org/feature/location.gps`, and
`http://tizen.org/feature/location.wps` features. How the hierarchy for these features work is described below:

-   If the feature list includes the
    `http://tizen.org/feature/location.gps` feature, only a device which
    has the `http://tizen.org/feature/location.gps` feature can show the
    application on the store application list.
- If the feature list includes the `http://tizen.org/feature/location`
    feature, a device which has the
    `http://tizen.org/feature/location.gps`,
    `http://tizen.org/feature/location.wps`, or
    `http://tizen.org/feature/location` feature can show the application
    on the store application list.

    This means that the store considers the
    `http://tizen.org/feature/location` feature as the
    `http://tizen.org/feature/location.gps OR http://tizen.org/feature/location.wps` feature.
    (If the feature list includes the
    `http://tizen.org/feature/location.gps` and
    `http://tizen.org/feature/location.wps` features together, only a
    device which supports both those features can show the application.)

<a name="adding"></a>
### Add the feature list

To enable filtering for your native application, follow the steps below to add the feature list
for the application `tizen-manifest.xml` file:

1.  To open the manifest editor in Tizen Studio, double-click the
    `tizen-manifest.xml` file in the **Project Explorer** view.
2. Select the features you need, one at a time:

    -   In the **Features** tab, click **+**.
    -   Select a feature.
    -   Click **OK**.

    The manifest file (`tizen-manifest.xml`) is updated automatically.

The following table shows the available requirements for an application
package:

**Table: Available IoT-only native requirements**

| Feature key                              | Description                              | Since |
|----------------------------------------|----------------------------------------|-----|
| `http://tizen.org/feature/device_update` | Specify this key, if the application requires Device Update API to control the system software update of the device. | 5.0   |
| `http://tizen.org/feature/peripheral_io.adc` | Specify this key, if the application requires Analog-to-Digital Converter (ADC) API to communicate with peripheral devices. | 5.0   |
| `http://tizen.org/feature/peripheral_io.gpio` | Specify this key, if the application requires General-Purpose Input/Output (GPIO) API to communicate with peripheral devices. | 4.0   |
| `http://tizen.org/feature/peripheral_io.i2c` | Specify this key, if the application requires Inter-Integrated Circuit (I2C) API to communicate with peripheral devices. | 4.0   |
| `http://tizen.org/feature/peripheral_io.pwm` | Specify this key, if the application requires Pulse-Width Modulation (PWM) API to communicate with peripheral devices. | 4.0   |
| `http://tizen.org/feature/peripheral_io.spi` | Specify this key, if the application requires Serial Peripheral Interface (SPI) API to communicate with peripheral devices. | 4.0   |
| `http://tizen.org/feature/peripheral_io.uart` | Specify this key, if the application requires Universal Asynchronous Receiver-Transmitter (UART) API to communicate with peripheral devices. | 4.0   |
| `http://tizen.org/feature/network.zigbee` | Specify this key, if the application requires Zigbee API to control Zigbee end-devices. | 5.0  |

<a name="profile_n"></a>
## Profile-based filtering


A Tizen profile describes the requirements for a category of Tizen
devices that have a common application execution environment.
Applications are created for a single specific target profile, and
can run on devices compliant with that profile.

Use profile-based filtering to ensure that your application is only
downloaded on the appropriate device profile. To ensure this, declare
the intended profile by adding the `profile name` element in the
`tizen-manifest.xml` file.

The following table lists the Tizen profiles and related profile name
attributes.

**Table: Tizen profiles and profile name attributes**

| Tizen profile | Profile name attribute |
|-------------|----------------------|
| Common        | `common`               |

In a native application, the profile name element can be added to the
`tizen-manifest.xml` file as follows:

```xml
<manifest xmlns="http://tizen.org/ns/packages" api-version="2.3.1" ... >
   <profile name="common"/>
```

The official site for Tizen applications compares the device profile and the `profile name`
element in an application. The store only shows the applications with a profile name matching the device profile to prevent unsupported
applications from being installed.
