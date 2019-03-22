# Test Tizen .NET Application on a Gear device

To publish a Tizen .NET Application to Samsung Gallaxy Apps store, you have to test it on Samsung Gear devices.
Since Samsung Gear does not have a USB port, Tizen provides a support to publish the app to the app store over Wi-Fi.

Therefore, you must connect the Gear device to Wi-Fi and the host PC to Wi-Fi or the Unshielded-Twisted-Pair (UTP) cable to the same local network.

![Host PC and the gear connect in local network](media/gear_wifi_connect.png)

## Prepare Gear Device

To debug an application on the Samsung Gear device:

1. Execute the **Settings** application.

2. Scroll to the bottom of the menu and tap **About watch**.

![About Watch](media/testing_your_app_on_gear1.png)

3. Tap **Debugging** to turn on.

![Debugging menu](media/testing_your_app_on_gear2.png)

4. Press the back button of the hardware, scroll to the **Connections**  menu, and tap it.

![Connections menu](media/testing_your_app_on_gear3.png)

5. Tap **Wi-Fi** to turn it on.

![Enable Wi-Fi](media/testing_your_app_on_gear4.png)

![Select Wi-Fi AP](media/testing_your_app_on_gear5.png)

![Connect Wi-fi Network](media/testing_your_app_on_gear6.png)

![IP Adress](media/testing_your_app_on_gear7.png)

## Debugging over Wi-Fi

You can install and execute your application on the Samsung Gear device over Wi-Fi.

1. Open Visual Studio 2017 app on your developer computer.

2. Select **Tizen** > **Tizen Device Manager** > **Remote Device Manager**.

![Device Manager-Remote Device Manager](media/testing_your_app_on_gear8.png)

3. Click **Scan Devices** to search for remote Samsung Gear devices. You can see a list of available remote devices.

![Scan Device](media/testing_your_app_on_gear9.png)
![Remote Device Manager](media/testing_your_app_on_gear10.png)

4. Select the IP of Samsung Gear Device that you want to connect to.
![Remote Device Manager - Enable Connection](media/testing_your_app_on_gear11.png)

    The connected Gear device appears on the Device Manager Explorer window.
    ![Device Manager - connected device list](media/testing_your_app_on_gear12.png)

## Connecting via the SDB command

You can connect to Gear device via SDB command.

Open the Command Prompt in the Host PC and enter the following command:

```
$ sdb connect [Gear S2 IP address]:26101
```

Example

```
$ sdb connect 192.168.0.71:26101
```
	

You can see the states of the connected Gear devices using SDB command.

```
$ sdb devices
List of devices attached
192.168.0.71:26101      device       SM-R805U
```
