# Tizen 5.0 M2


[The second milestone (M2) release of Tizen 5.0](../../release-notes/tizen-5-0-m2.md) was released in October 2018. Tizen has expanded its horizon from smart devices to IoT devices. Currently Tizen is used for the various kinds of smart devices.
Adding the enhancement on service with Tizen 5.0 provides the opportunity to develop applications which are related to service centric. When it comes to users, they will get various experiences with more enhanced applications. Tizen 5.0 provides APIs such as TIDL(Tizen Interface Definition Language), RPC-port for easy integration of various kinds of services (eg. Smart-things ) and core open sources such as Blink, GStreamer, EFL, Wayland etc. are upgraded. So the latest standard specification can be used in Tizen.

The key features are as follows:
* **TIDL, rpc-port**: TIDL is Tizen Interface Definition Language. Service application can communicate with other service application or service deamon with this API set. Rpc-port provides application IPC mechanism.
Applications can expose RPC style service interface to other applications with TIDL.

* **Core Open source Upgrade**: In Tizen 5.0, many core open sources are upgraded as follows:
 Blink M56 which is the core web engine in Tizen is upgraded to M63.
   . Provide new W3C Standard (Animated PNG, Full featured Indexed DB, CSS grid layout, Web USB, MSE/EME and so on).
   . Enhancement standard web features (WebRTC, ARIA 1.1)
   . Web performance enhancement (V8 : ES 6 performance enhancement, Web Assembly default enabling)
GStreamer, Pulseaudio are upgraded to latest stable release
    EFL version 1.16 is upgraded to 1.20
Wayland is upgraded to 1.15.0 version.
.NET Core(Runtime) is upgraded
  .Coreclr 2.1.1 is upgraded to 2.1.4.
  .Corefx 2.1.1 is upgraded to 2.1.4.
  .Xamarin.Froms is upgraded to 3.2.0.
Etc.

* **Tizen Circular UI for Watch** : Tizne 5.0 provides easy watch app development with Tizen Circular UI APIs and provides "Tizne Wearalbe App" project template for creating Watch circular applicaiton easily.

![img](media/5.0_introduction_TizenCircularUIforWatch.png)
![img](media/5.0_introduction_TizenCircularUIforWatch_template.png)

* **C# API enhancement in TizenFX**: Many APIs in TizenFX are added.
   - MediaController API set for playlist, event, and capabilities...
   - AudioManager API set for USB Audio output device ...
   - AudioIO API set and enum for sample type and changed maximum sample rate.
   - MediaPlayer API set to set or get the video ROI area.
   - Multimedia API set for the rotation, zoom level ...
   - Nlp API set for new Namespace and Class.
   - InputMethod API set for floating keyboard and to hide or launch IME.
   - Wi-Fi API set for forgetting access point (AP), BssidScan, RawSsid, CountryCode, and WPS connection cancellation.
   - NUI API set for KeyboardRepeatInfo and TextPredition...

    and so on.

  ![img](media/5.0_introduction_TizenFXAPI_v5.png)

For more information about open source upgrade, see release note [M1](../../release-notes/tizen-5-0-m1.md) and [M2](../../release-notes/tizen-5-0-m2.md).
