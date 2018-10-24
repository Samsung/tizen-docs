# RPC Port

Tizen applications can communicate with each other using RPC Port APIs, which allows applications to send and receive data after a connection is established.

>**Note**
>
> APIs will be used in generated source files by TIDLC which is an Interface Definition Language (IDL) compiler for Tizen.
> **[TIDL](tidl.md) is recommended rather than using RPC Port APIs directly.**

## RPC Port APIs

RPC Port APIs compose of three set of APIs:

- **Proxy APIs**:  provide functions to connect a server, invoke functions in the server, and return the results from the server.

- **Stub APIs**:  provide the way to call methods of the server, which executes the methods requested by clients.

- **Parcel APIs**:  provide interfaces to marshall and unmarshall a parcel to/from the native type format.

## Features of RPC Port API

- Connection oriented communication

  You must create a connection between the proxy and the stub applications to send and receive data. After the connection is disconnected, the callback for disconnected event that was registered earlier is called. Some other events such as connected and rejected events are supported as well.

- Access control

  The server application using stub APIs can register the privileges to verify whether the client that is trying to connect has proper privileges.

- Trusted communication

  The server application using stub APIs can allow connections only if the proxy is signed with the required certificate.

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
