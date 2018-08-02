# RPC Port

Tizen applications can communicate with each other using RPC ports. Applications can send and receive data after making a connection.

**Note**
APIs will be used by [TIDLC](tidl.md) which is a compiler in order to generate source files using this. We strongly recommand to use [TIDL](tidl.md) instead of using RPC Port APIs directly.

## RPC Port API include:

- Proxy APIs

  These APIs are for an application which wants to connect to an application and invoke some functions then return the results.

- Stub APIs

  These APIs are for an application which wants to provide some methods to use at other processes like RPC (Remote Procedure Call)

- Parcel APIs

  These APIs provides methods to make mashalling and unmashalling parcel from native type format.


## The main features of RPC Port API include:

- Connection oriented communication

  You should make a connection between proxy and stub application to send and receive data.
  Once it is disconnected, the callback for disconnected event which was registered before will be called.
  Some other events such as connected and rejected events are supported as well.

- Access control

  Stub application can register the privileges to check if the application which is trying to connect has proper privileges.

- Trusted communication

  Stub application can register the flag for the trusted communication to allow only trusted applications.


## Prerequisites

To use rpc_port_proxy_connect() API

  The application has to request permission. Add the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
       <privilege>http://tizen.org/privilege/datasharing</privilege>
    </privileges>
    ```


## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
