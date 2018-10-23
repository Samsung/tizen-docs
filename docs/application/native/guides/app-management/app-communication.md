# Application Data Exchange


The application data exchange features cover the various methods you have to communicate with other applications. You can exchange data between applications through message ports and data controls, and use data bundles to package the data to be communicated.

You can use the following application data exchange features in your native applications:

- [Message Port](message-port.md)

  Applications communicate with each other using message ports. You can send and receive messages using the map data format and trusted or untrusted message port instances.

- [Data Control](data-control.md)

  You can exchanging SQL- or key-value-type data between applications. All applications can request data shared by other applications, but only service applications can provide their own data.

- [Data Bundle](data-bundles.md)

  You can package data with a bundle, which is a string-based dictionary abstract data type. You can create bundles, manage their content, access their content through iteration, and encode and decode them.

- [PRC Port](rpc-port.md)

  Tizen applications can communicate with each other using RPC Port APIs, which allows applications to send and receive data after a connection is established.

- [TIDL](tidl.md)

  You can define interface with TIDL, which is a programming language to define interfaces for communicating among applications in Tizen.


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
