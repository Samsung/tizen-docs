# RPC Port

Tizen applications can communicate with each other using RPC ports. Applications can send and receive data after establishing a connection.

>**Note**
>
> APIs will be used in generated source files by TIDLC which is an Interface Definition Language (IDL) compiler for Tizen.
> **Samsung strongly recommends to use [TIDL](tidl.md) instead of using RPC Port APIs directly.**

## RPC Port APIs

- Proxy APIs
  
  These APIs are for an application that wants to connect to an application, invoke some functions, and return the results.

- Stub APIs

  These APIs are for an application that wants to provide some methods to other processes, which includes Remote Procedure Call (RPC).

- Parcel APIs

  These APIs provides methods to create marshalling and unmarshalling parcel from the native type format.

## Features of RPC Port API

- Connection oriented communication

  You must create a connection between proxy and stub application to send and receive data.
  After the connection is disconnected, the callback for disconnected event, which was registered earlier will be called.
  Some other events such as connected and rejected events are supported as well.

- Access control

  Stub application can register the privileges to verify whether the application that is trying to connect has proper privileges.

- Trusted communication

  Stub application can register the flag for the trusted communication to allow only trusted applications.

## Prerequisites

To enable your application to use `rpc_port_proxy_connect()` API:

  To use the `rpc_port_proxy_connect()` API, the application has to request permission by adding the following privilege to `tizen-manifest.xml` file:

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
