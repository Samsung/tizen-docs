# Telephony Information


Through the telephony service, you can access various telephony features, such as call, SIM, network, and modem information.

The main Tizen.Telephony namespace features are:

-   Telephony manager

    You can manage the initialization and deinitialization of the telephony slot handle with the [Tizen.Telephony.Manager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Manager.html) class. The handle is used to create instances of the [Tizen.Telephony.Call](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Call.html), [Tizen.Telephony.Sim](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Sim.html), [Tizen.Telephony.Network](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Network.html), and [Tizen.Telephony.Modem](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Modem.html) classes, which allow you to access telephony information. If a dual-SIM device is used, you have a separate slot handle for each SIM card.

    You can also access the current telephony state of the device, and monitor the state change events.

    By using the [Tizen.Telephony.SlotHandle](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.SlotHandle.html) class to register for specific notification IDs, you can receive notifications for various information change events related to call, SIM card, network, and modem information. Register for the notifications with the `SetNotificationId()` method, by specifying the notification ID. The available notification IDs are defined in the [Tizen.Telephony.ChangeNotificationEventArgs.Notification](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.ChangeNotificationEventArgs.Notification.html) enumeration.

-   Call information

    You can [retrieve information about the current call](#call_use) by using the `Tizen.Telephony.Call` class to retrieve a list of current call handles. You can also access voice and video call states, and use the state information in call-related actions.

    The call handles are instances of the [Tizen.Telephony.CallHandle](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.CallHandle.html) class, which allows you to access the number, type, and status of the call. You can also determine the call direction (mobile-originated or mobile-terminated) and whether the call is a conference call.

-   SIM information

    You can [extract information stored on a SIM card](#sim_use) using the `Tizen.Telephony.Sim` class. You can get, for example, the ICC-ID (Integrated Circuit Card Identification), operator, and SPN (Service Provider Name) information.

-   Network information

    You can [retrieve information about the current cellular network and telephony service](#network_use) using the `Tizen.Telephony.Network` class. You can get, for example, the cell ID, LAC (Location Area Code), network type, and network name of the current cellular network and telephony service.

-   Modem information

    You can [access information about the modem](#modem_use) using the `Tizen.Telephony.Modem` class. You can get the IMEI (International Mobile Station Equipment Identity), MEID (Mobile Equipment Identifier), and power status of the modem.



> **Note**   
> You can only access the SIM card, network, and modem information. You cannot modify it.



## Prerequisites


To enable your application to use the telephony functionality:

1.  To use the [Tizen.Telephony](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
        <privilege>http://tizen.org/privilege/telephony</privilege>
        <privilege>http://tizen.org/privilege/location.coarse</privilege>
    </privileges>
    ```

2.  Retrieve the slot handle with the `Init()` method of the [Tizen.Telephony.Manager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Manager.html) class.

    In a dual-SIM scenario, the method returns a separate handle for each SIM card. The `handle[0]` instance means the primary SIM and `handle[1]` means the secondary SIM. To send call, network, modem, or SIM card requests to a specific subscription (SIM card), use the applicable handle.

    ```
    IEnumerable<SlotHandle> simList = Manager.Init();
    ICollection<SlotHandle> c = simList as ICollection<SlotHandle>;
    for (int i = 0; i < c.Count; i++)
    {
        Log.Info(Globals.LogTag, "handle = " + simList.ElementAt(i));
    }
    ```

3.  When no longer needed, deinitialize the slot handles:

    ```
    IEnumerable<SlotHandle> simList = Manager.Deinit();
    ```

<a name="call_use"></a>
## Retrieving Call Information

To get information about the current call and monitor when the user makes a voice or video call or hangs up the phone, use the [Tizen.Telephony.Call](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Call.html) class:

-   Get the current call information:
    1.  To get the current call list, retrieve the current call handle with the `GetCallHandleList()` method:

        ```
        IEnumerable<SlotHandle> simList = Manager.Init();
        Call _call = new Call(simList.ElementAt(0));
        IEnumerable<CallHandle> _list = _call.GetCallHandleList();
        ```

    2.  Use the handle to retrieve the call information you need (such as handle ID, number, type, status, direction, and conference status):

        ```
        foreach (CallHandle CallHandle in _list)
        {
            Log.Info(Globals.LogTag, "handleid = " + CallHandle.HandleId);
            Log.Info(Globals.LogTag, "number = " + CallHandle.Number);
            Log.Info(Globals.LogTag, "type = " + CallHandle.Type);
            Log.Info(Globals.LogTag, "status = " + CallHandle.Status);
            Log.Info(Globals.LogTag, "Direction = " + CallHandle.Direction);
            Log.Info(Globals.LogTag, "Conference = " + CallHandle.ConferenceStatus);
        }
        ```

-   Monitor call state changes:
    1.  To receive call state change notifications asynchronously, register a callback with the `SetNotificationId()` method of the [Tizen.Telephony.SlotHandle](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.SlotHandle.html) class.

        You must register the callback separately for each call state, using the applicable `VoiceCallXXX` or `VideoCallXXX` notification value in the `SetNotificationID()` method parameter. The available values are defined in the [Tizen.Telephony.ChangeNotificationEventArgs.Notification](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.ChangeNotificationEventArgs.Notification.html) enumeration.

        ```
        void RegisterCallbackNotification()
        {
            List<ChangeNotificationEventArgs.Notification> list = new List<ChangeNotificationEventArgs.Notification>();
            list.Add(ChangeNotificationEventArgs.Notification.VoiceCallStatusIdle);
            list.Add(ChangeNotificationEventArgs.Notification.VoiceCallStatusActive);
            list.Add(ChangeNotificationEventArgs.Notification.VoiceCallStatusHeld);
            list.Add(ChangeNotificationEventArgs.Notification.VoiceCallStatusDialing);
            list.Add(ChangeNotificationEventArgs.Notification.VoiceCallStatusAlerting);
            list.Add(ChangeNotificationEventArgs.Notification.VoiceCallStatusIncoming);
            simListElementAt(0).ChangeNotification += ChangeNotificationDelegate;
            simList.ElementAt(0).SetNotificationId(list);
        }
        ```

    2.  Define the callback:

        ```
        private ChangeNotificationEventArgs.Notification _eventType;

        private static void ChangeNotificationDelegate(object sender, ChangeNotificationEventArgs args)
        {
            switch (_eventType)
            {
            case ChangeNotificationEventArgs.Notification.VoiceCallStatusIdle:
                Log.Info(Globals.LogTag, "Noti !!! Voice call status idle");
                break;
            case ChangeNotificationEventArgs.Notification.VoiceCallStatuActive:
                Log.Info(Globals.LogTag, "Noti !!! Voice call status active");
                break;
            case ChangeNotificationEventArgs.Notification.VoiceCallStatusHeld:
                Log.Info(Globals.LogTag, "Noti !!! Voice call status held");
                break;
            case ChangeNotificationEventArgs.Notification.VoiceCallStatusDialing:
                Log.Info(Globals.LogTag, "Noti !!! Voice call status dialing");
                break;
            case ChangeNotificationEventArgs.Notification.VoiceCallStatusAlerting:
                Log.Info(Globals.LogTag, "Noti !!! Voice call status alerting");
                break;
            case ChangeNotificationEventArgs.Notification.VoiceCallStatusIncoming:
                Log.Info(Globals.LogTag, "Noti !!! Voice call status incoming");
                break;
            default:
                Log.Info(Globals.LogTag, "Unknown Noti !!!");
                break;
           }
        }
        ```

    3.  When the notifications are no longer needed, deregister the callback for each call state with the `RemoveNotificationId()` method:

        ```
        simList.ElementAt(0).RemoveNotificationId(list);
        ```

<a name="sim_use"></a>
## Retrieving SIM Card Information

To retrieve information from a SIM card and monitor when the SIM state changes, use the [Tizen.Telephony.Sim](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Sim.html) class.


> **Note**   
> Before retrieving information from the SIM card, check the SIM card state. You can get SIM-related information only if the SIM state is `Available`.


-   Get SIM card details:
    1.  Retrieve the SIM card state with the `CurrentState` property of the `Tizen.Telephony.Sim` class. It returns the SIM state using the values of the [Tizen.Telephony.Sim.State](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Sim.State.html) enumeration.

        ```
        IEnumerable<SlotHandle> simList = Manager.Init();
        Sim _sim = new Sim(simList.ElementAt(0));
        Log.Info(Globals.LogTag, "State = " + _sim.CurrentState);
        ```

    2.  Retrieve various SIM card details, such as the ICC-ID, using the `Tizen.Telephony.Sim` instance properties:

        ```
        Log.Info(Globals.LogTag, "Iccid = " + _sim.IccId);
        ```

-   Monitor SIM state changes:
    1.  To receive SIM state change notifications asynchronously, register a callback with the `SetNotificationId()` method of the [Tizen.Telephony.SlotHandle](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.SlotHandle.html) class.

        You must register the callback separately for each SIM state, using the applicable `SimXXX` notification value in the `SetNotificationID()` method parameter. The available values are defined in the [Tizen.Telephony.ChangeNotificationEventArgs.Notification](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.ChangeNotificationEventArgs.Notification.html) enumeration.

        ```
        void RegisterCallbackNotification()
        {
            List<ChangeNotificationEventArgs.Notification> list = new List<ChangeNotificationEventArgs.Notification>();
            list.Add(ChangeNotificationEventArgs.Notification.SimStatus);
            simListElementAt(0).ChangeNotification += ChangeNotificationDelegate;
            simList.ElementAt(0).SetNotificationId(list);
        }
        ```

    2.  Define the callback:

        ```
        private static void ChangeNotificationDelegate(object sender, ChangeNotificationEventArgs args)
        {
            Log.Info(Globals.LogTag, "Sim state = " + args.NotificationData);
        }
        ```

    3.  When the notifications are no longer needed, deregister the callback with the `RemoveNotificationId()` method:

        ```
        simList.ElementAt(0).RemoveNotificationId(list);
        ```

<a name="network_use"></a>
## Retrieving Network Information

To retrieve current cellular network and telephony service details, and monitor when the network service state changes, use the [Tizen.Telephony.Network](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Network.html) class.



> **Note**   
> Before retrieving information about the current cellular network and telephony service, check the network service state. You can get network-related information only if the service state is `InService`.



-   Get network details:
    1.  Retrieve the network state with the `NetworkServiceState` property of the `Tizen.Telephony.Network` class. It returns the network service state using the values of the [Tizen.Telephony.Network.ServiceState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Network.ServiceState.html) enumeration.

        ```
        IEnumerable<SlotHandle> simList = Manager.Init();
        Network _network = new Network(simList.ElementAt(0));
        Log.Info(Globals.LogTag, "State = " + _network.NetworkServiceState);
        ```

    2.  Retrieve various network details, such as the cell ID and MNC information, using the `Tizen.Telephony.Network` instance properties:

        ```
        Log.Info(Globals.LogTag, "CellId = " + _network.CellId);
        Log.Info(Globals.LogTag, "Mnc = " + _network.Mnc);
        ```

-   Monitor network state changes:
    1.  To receive network service state change notifications asynchronously, register a callback with the `SetNotificationId()` method of the [Tizen.Telephony.SlotHandle](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.SlotHandle.html) class.

        You must register the callback separately for each service state, using the applicable `NetworkXXX` notification value in the `SetNotificationID()` method parameter. The available values are defined in the [Tizen.Telephony.ChangeNotificationEventArgs.Notification](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.ChangeNotificationEventArgs.Notification.html) enumeration.

        ```
        void RegisterCallbackNotification()
        {
            List<ChangeNotificationEventArgs.Notification> list = new List<ChangeNotificationEventArgs.Notification>();
            list.Add(ChangeNotificationEventArgs.Notification.NetworkServiceState);
            simListElementAt(0).ChangeNotification += ChangeNotificationDelegate;
            simList.ElementAt(0).SetNotificationId(list);
        }
        ```

    2.  Define the callback:

        ```
        private static void ChangeNotificationDelegate(object sender, ChangeNotificationEventArgs args)
        {
            Log.Info(Globals.LogTag, "Network service state = " + args.NotificationData);
        }
        ```

    3.  When the notifications are no longer needed, deregister the callback for each service state with the `RemoveNotificationId()` method:

        ```
        simList.ElementAt(0).RemoveNotificationId(list);
        ```

<a name="modem_use"></a>
## Retrieving Modem Information

To access information about the modem, such as its IMEI, use the [Tizen.Telephony.Modem](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Telephony.Modem.html) class:

```
IEnumerable<SlotHandle> simList = Manager.Init();
Modem _modem = new Modem(simList.ElementAt(0));
Log.Info(Globals.LogTag, "Imei = " + _modem.Imei);
```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
