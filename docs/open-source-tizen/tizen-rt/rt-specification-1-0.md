# Tizen RT 1.0 Specification

## IoT Data Management
Tizen RT manages data in the following ways:
- File system support  
Tizen RT supports not only the SmartFS lightweight file system, but also a virtual file system (VFS). The VFS can provide a common interface set in the form of the POSIX API. Standard libc APIs are already supported. In addition, some advanced features are also included:
    - Proc File System for debugging, and ROM File System for read-only data
    - SmartFS for a flash file system with wear-leveling, bad sector management, and transaction-logging-based journaling
    - MTD (Memory Technology Device) and MTD Partition
- Database (AraStorage) support  
AraStorage, a lightweight database, can manipulate collected sensor data with SQL-compatible interfaces. AraStorage also provides some advanced features, such as:
    - b+ tree-based indexing algorithm
    - Cursor structure to improve usability for the application layer

## Device Management

Tizen RT incorporates the OMA-based Lightweight M2M (LWM2M) protocol for device management. LWM2M is an application layer communication protocol between an LWM2M server and an LWM2M client that typically resides on a resource-constrained device. The LWM2M protocol can be briefly described in the context of its interface and stack design:

- LWM2M interfaces
  - Bootstrap: The LWM2M client obtains information about the LWM2M server from the LWM2M bootstrap server. The LWM2M bootstrap server holds the credentials of all registered LWM2M servers, and can provide the details either on request (client-initiated bootstrap), or explicitly (server-initiated bootstrap). At present, client-initiated bootstrap is already developed and verified. Server-initiated bootstrapping is planned to be included.
  - Registration: Once the LWM2M client has the necessary information about an LWM2M server, it opens a connection to the server and registers itself as an LWM2M device. Registration, in this context, also includes providing details of the LWM2M objects that the client has created during initialization.
  - Device management and service enablement: The LWM2M server uses this interface for query (read and discover), modify (write), and execute operations, as well as for creating and deleting attributes on a registered LWM2M client object. While basic read operations are currently verified, support for other operations is to be provided later.
  - Information reporting: The LWM2M server uses this interface to periodically query the registered LWM2M client to send updates on an object attribute (such as a sensor value or communication signal strength). Alternatively, the LWM2M server can also direct the LWM2M client to notify it about changes in attribute values over a programmable time interval. The LWM2M protocol allows the LWM2M server to specify the observation time interval, and the range of permissible attribute values, beyond which a notification must be sent.
- LWM2M protocol stack
  - CoAP protocol: The LWM2M entities (client, server, and bootstrap server) use the CoAP (Constrained Application Protocol) for implementing the 4 LWM2M interfaces described above. CoAP offers the advantage of an efficient payload structure, which is necessary for resource-constrained client devices. In this context, LWM2M-based request and response messages are mapped on to appropriate CoAP methods (such as GET, PUT, and POST), as described in [RFC 7252](https://tools.ietf.org/html/rfc7252).
  - DTLS security: While LWM2M optionally functions in a 'NoSec' (no security) mode, it also allows the use of DTLS (Datagram Transport Layer Security) to ensure authentication, data confidentiality, and integrity between an LWM2M client and an LWM2M server or bootstrap server. The LWM2M client has the option of bootstrapping with a pre-shared secret, or with public certificates (either raw public keys or X.509v3). In all cases, the LWM2M client must possess a unique key for securing communication with the LWM2M bootstrap server and the LWM2M server. These features are planned to be supported on Tizen RT.
  - UDP: LWM2M allows the use of both UDP and SMS protocols for communication between a client and server. The lightweight M2M component in Tizen RT uses UDP binding over port 5683. Reliability over UDP is achieved using the CoAP retransmission mechanism.

## IP Network

For the TCP, UDP, and IPv4 protocols, LWIP is already ported on Tizen RT and successfully verified. As for IPv6, the uIP-based stack is already implemented and was granted the "[IPv6 Ready Logo](https://www.ipv6ready.org/db/index.php/public/logo/02-C-001400/)" by the IPv6 Forum. To increase maintainability, a common base for the network stack is needed. Both IPv4 and IPv6 based on the common project (such as LWIP or uIP) are to be released.

Transition between IPv4 and IPv6 is also required. Suppose that sensor devices are equipped with only IPv6 over IEEE 802.15.4 or IPSP/BLE. These devices need to connect to the Internet directly or through hubs or other IoT devices. Tizen RT is preparing to fit into these relaying IoT devices by implementing transition functions between IPv4 and IPv6.

## IoTivity

Tizen RT 1.0 currently supports IoTivity 1.1.0. The next release updates IoTivity support to version 1.2.

### IoTivity 1.2 Base Layer Support (OCF 1.0 Base Layer Ready)

Tizen RT supports the IoTivity base layer for constrained-device communication in the IoT world. It supports IoTivity 1.2 release as base code with the OCF 1.0 spec ready.

IP transport (TCP/UDP over Wi-Fi) is currently supported in the Connectivity Abstraction (CA) layer.

The following figure shows the IoTivity base layer architecture. The architecture can be divided into discovery, messaging, and security modules.

**Figure: IoTivity base layer architecture**

![IoTivity base layer architecture)](media/iotivity-baseline-architecture.png)

The following table describes the IoTivity 1.2 features in Tizen RT.

**Table: Iotivity features**

| Module (base layer) | Feature                              | Description                              |
| ------------------- | ------------------------------------ | ---------------------------------------- |
| Discovery           | Multicast Discovery, Device Presence | Discovers resources, and checks for device presence. |
|                     | Resource Introspection               | Manages resource types and properties.   |
| Messaging           | CoAP Messaging                       | Transmits messages between devices.      |
|                     | Message switching                    | Not supported by Tizen RT. |
|                     | Connectivity Abstraction             | Currently Supports Wi-Fi transport. Support is planned for more protocols, such as BT, BLE, and NFC. |
|                     | Block-wise transfer                  | Provides block data transfer (more than 1 KB data). |
|                     | CoAP over TCP                        | Provides reliable transmission. It can be used for messaging between a device and cloud. |
| Security            | DTLS                                 | Provides a secure channel with data encryption for UDP. |
|                     | Security Resource Manager            | Provides an access control mechanism.    |
|                     | Security Provisioning Manager        | Transmits credentials for authentication. |

### IoTivity 1.2 Feature Support

Tizen RT supports:

- IoTivity 1.2.0 base layer stack (csdk layer) with Wi-Fi transport
- Resource creation and publishing for resource discovery (resource registration, discovery, update, and delete)
- Device-to-device communication with UDP over a secured DTLS channel
- Wi-Fi transport over IPv4 (supported in Tizen 4.0)
- CoAP over TCP for communicating with the IoT cloud (resource registration, discovery, update, and delete)
- TLS for TCP to enable security for cloud communication
- Presence for the server side and presence callback for the client side
- Onboarding (Wi-Fi provisioning) for new devices to enable easy setup onto the network
- Cloud provisioning to connect a device to the cloud and to publish a resource to it
- Keep-alive mechanism to keep the cloud session active with CoAP over TCP
- Direct pairing support for credential delivery to transfer device ownership for easy setup
- Multiple ownership transfer and multiple ownership structure in the Security Resource Model
- Message-oriented communication interface for the cloud. This interface can be used for a publish/subscribe-based information exchange. A resource model for a CoAP-based message broker is to be provided.


## IoTBus Framework

The IoTBus Framework supports system I/O APIs, including the following 5 API categories:

- GPIO (General Purpose Input/Output)  
Provides functions to control generic pins. They can be configured for input or output, because GPIO pins have no predefined purpose.
- I2C (Inter Integrated Circuit)  
Provides functions to read values of I2C devices or write commands to I2C devices. These APIs are typically used to connect sensor devices or for intra-board communications.
- SPI (Serial Peripheral Interface)  
Provides functions to communicate with SPI devices. These APIs support synchronous serial communication interfaces used for short-distance communication. Full duplex modes using a master-slave architecture with a single master are also served.
- PWM (Pulse Width Modulation)  
Provides functions to get and set duty cycles and periods of PWM devices. These APIs are typically used to control servo motors or LEDs.
- UART (Universal Asynchronous Receiver/Transmitter)  
Provides functions to read and write for asynchronous serial communication. These APIs are usually used in conjunction with communication standards, such as RS-232, RS-422, and RS-485.

## Device Management Framework

The following features are to be made available under the Device Management Framework:

- Configuration  
The LWM2M client is configured with a set of parameters that include the LWM2M bootstrap server address, bootstrap server port, and LWM2M session lifetime. Alternatively, if a direct connection to the LWM2M server is preferred, the client can be configured with the LWM2M server address and port information.
- Temporary Halt and Resumption  
Wireless links, especially in indoor deployments, are prone to intermittent failures, and can momentarily halt an ongoing LWM2M session. Taking this into account, the Device Management Framework must gracefully close all LWM2M sessions with their respective servers, and also logically resume the sessions once the wireless link is restored.
- Support for Multiple Servers  
The LWM2M specification allows multiple servers to perform device management with a registered LWM2M client. To this end, the framework must facilitate the seamless addition of LWM2M server information.
- Device Management Services  
Services provided under Device Management can be broadly categorized into 4 types:
    - Connectivity monitoring, which relates to connectivity details, such as client IP address, network type, signal strength, and effective data rate.
    - Power monitoring, which relates to the available power states of a device, its current power state, and the time spent in different power states.
    - Error reporting, which relates to out-of-memory conditions, and also temporary wireless connection losses.
    - Software update, which relates to querying a firmware repository for updates, version checking, downloading, and installing firmware packages.

  Tizen RT 1.0 supports the first 3 service types. Software update is to be included in the next version.
