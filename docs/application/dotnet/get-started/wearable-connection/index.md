# Connect Your Wearable

To publish a Tizen .NET application to the Samsung Galaxy Store, you have to first test your application on the Samsung Gear devices.
Since Samsung Gear does not have a USB port, Tizen provides support to publish your app to the app store over Wi-Fi.

Therefore, you must connect the Gear device and the host PC to Wi-Fi, or the Unshielded-Twisted-Pair (UTP) cable to the same local network.

![Host PC and the gear connect in local network](media/gear_wifi_connect.png)

## Prepare Gear Device

To debug an application on the Samsung Gear device:

1. Execute the **Settings** application.

2. Scroll to the bottom of the menu and tap **About watch**.

    ![About Watch](media/testing_your_app_on_gear1.png)

3. Tap **Debugging** to turn it on.

    ![Debugging menu](media/testing_your_app_on_gear2.png)

4. Press the back button of the hardware, scroll to the **Connections**  menu, and tap it.

    ![Connections menu](media/testing_your_app_on_gear3.png)

5. Tap **Wi-Fi** to turn it on.

    ![Enable Wi-Fi](media/testing_your_app_on_gear4.png)

    ![Select Wi-Fi AP](media/testing_your_app_on_gear5.png)

    ![Connect Wi-fi Network](media/testing_your_app_on_gear6.png)

    ![IP Address](media/testing_your_app_on_gear7.png)

## Debugging over Wi-Fi

To install and execute your application on the Samsung Gear device over Wi-Fi, follow these steps:

1. In the Visual Studio menu, select **Tizen** > **Tizen Device Manager** > **Remote Device Manager**.

    ![Device Manager-Remote Device Manager](media/testing_your_app_on_gear8.png)

2. To search for remote Samsung Gear devices, click **Scan Devices**. A list of available remote devices appears.

    ![Scan Device](media/testing_your_app_on_gear9.png)

    ![Remote Device Manager](media/testing_your_app_on_gear10.png)

3. Select the IP of the Samsung Gear device that you want to connect to.

    ![Remote Device Manager - Enable Connection](media/testing_your_app_on_gear11.png)

    The connected Gear device appears on the Device Manager Explorer window.
	
    ![Device Manager - connected device list](media/testing_your_app_on_gear12.png)

## Connecting via the SDB command

To connect to the Samsung Gear device using the SDB command, follow this step:

Open the Command Prompt in the host PC and enter the following command:

```bash
$ sdb connect [Gear S2 IP address]:26101
```

Example:

```bash
$ sdb connect 192.168.0.71:26101
```
	

The list of devices that are connected to the Gear devices appears:

```bash
$ sdb devices
List of devices attached
192.168.0.71:26101      device       SM-R805U
```
