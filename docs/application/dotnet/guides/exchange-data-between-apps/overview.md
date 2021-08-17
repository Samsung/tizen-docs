# Exchange data between applications

With increasing complexity of the project, it is important to separate an application functionality into smaller, independent components. The advantage of this is: 
- Create reusable code.
- Improved fault tolerance.
- Easier maintenance.
- Improved code readability.

For this purpose, Tizen .NET API introduce few mechanisms for developers to implement communication process between processes:
- [Application Control](./app-controls.md)
- [Data Control](./data-control.md)
- [Event Broadcast and Subscription](./event.md)
- [Message Port](./message-port.md)

## The Application Control

An application control (app control) is a way of sharing an application’s functionality. Using another application’s features through application controls, reduces the time and effort needed to develop your own application.

You can use operations such as calling, web browsing, and playing media items in your application, that are exported by other applications. This mechanism allows you to conveniently launch other applications whose functionalities you need in your application. If you need to use functionality from another application, launching an application control allows you to request the system to launch that application according to your requirements. You can launch applications based on your immediate needs - you do not need to know their identifiers or specifications. You can use application controls by creating an application control request. The request allows you to launch other applications to use their functionalities.

![App Control](./media/overview_app_ctrl.gif)

## The Data Control

Data control allows you to read and modify data stored and provided by another application, and monitor changes in that data. The application storing and controlling the data is called as DataControl provider application. The application using the data is called as DataControl consumer application. A single DataControl provider can serve multiple DataControl consumers.

![Data Control](./media/overview_data_ctrl.png)

## Events Broadcast and Subscription

Event is a broadcast message sent by application and all applications which want to listen receive this event. A set of specific platform events provided by the Tizen operating system are as follows: 

| Name                                     | Condition                                |
|------------------------------------------|------------------------------------------|
| `SystemEvents.BatteryChargerStatus.EventName` | When the charger state is `SystemEvents.BatteryChargerStatus.StatusValueConnected`. |
| `SystemEvents.UsbStatus.EventName`         | When the USB state is `SystemEvents.UsbStatus.StatusValueConnected`.     |
| `SystemEvents.EarjackStatus.EventName`     | When the earjack state is `SystemEvents.EarjackStatus.StatusValueConnected`. |
| `SystemEvents.IncomingMsg.EventName`       | When the `SystemEvents.IncomingMsg.TypeKey` and `SystemEvents.IncomingMsg.IdKey` exist.  |
| `SystemEvents.WifiState.EventName`         | When the Wi-Fi state is `SystemEvents.WifiState.StateValueConnected`.   |

Events used to launch app are called as `launch events`.  

![Event Broadcast](./media/overview_event.png)

## Message Port

Message port provides encrypted communication using author certificate. If data exchanged between two applications should be secured, you could use Message Port API. Secure connection could be established only for applications using the same certificate. The following picture shows possible trusted data exchange between two apps. Possible connection is marked using green color. Communication between apps using `A certificate` and `B certificate` is not allowed.

![Message Port](./media/overview_msgport.png)

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher