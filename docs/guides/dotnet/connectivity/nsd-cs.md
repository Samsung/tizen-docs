Network Service Discovery
=========================

## Dependencies

- Tizen 4.0 and Higher

You can use 2 different protocols to perform network service discoveries
to announce local services and search for remote services on a network:
DNS-SD (DNS Service Discovery) and SSDP (Simple Service Discovery
Protocol).

The main features of the Tizen.Network.Nsd namespace include:

-   Managing local services

    Registering a local service announces it over the network, allowing
    other devices to find and use it. You can create and [register local
    services](#registration) through the
    [Tizen.Network.Nsd.DnssdService](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Nsd_1_1DnssdService.html)
    and
    [Tizen.Network.Nsd.SsdpService](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Nsd_1_1SsdpService.html)
    classes, which both implement the
    [Tizen.Network.Nsd.INsdService](https://developer.tizen.org/dev-guide/csapi/interfaceTizen_1_1Network_1_1Nsd_1_1INsdService.html)
    interface:

    -   For the DNS-SD services, you can retrieve service details, such
        as name, type, port number and IP address, through
        related properties. You can also add a text record after
        registering the service, and set the key and value of
        the record. To remove a record, use its key.
    -   For the SSDP services, you can retrieve service details, such as
        name, target, and URL.
- Discovering remote services

    You can [search for remote services](#discovery) on the network
    through the
    [Tizen.Network.Nsd.DnssdBrowser](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Nsd_1_1DnssdBrowser.html)
    and
    [Tizen.Network.Nsd.SsdpBrowser](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Nsd_1_1SsdpBrowser.html)
    classes, which both implement the
    [Tizen.Network.Nsd.INsdBrowser](https://developer.tizen.org/dev-guide/csapi/interfaceTizen_1_1Network_1_1Nsd_1_1%20INsdBrowser.html) interface.
    You can also receive notifications when a service is found by
    registering an event handler for the `ServiceFound` event of the
    applicable class.


Prerequisites
-------------

To enable your application to use the network service discovery
functionality:

1.  To use the
    [Tizen.Network.Nsd](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Nsd.html)
    namespace, the application has to request permission by adding the
    following privilege to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <privilege>http://tizen.org/privilege/internet</privilege>
    </privileges>
    ```

2. To make your application visible in the Tizen Store only for devices
    that support the DNS-SD and SSDP protocols, the application must
    specify the following features in the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <feature name="http://tizen.org/feature/network.service_discovery.dnssd"/>
    <feature name="http://tizen.org/feature/network.service_discovery.ssdp"/>
    ```

3. To use the methods and properties of the Tizen.Network.Nsd
    namespace, include it in your application:

    ``` {.prettyprint}
    using Tizen.Network.Nsd;
    ```


Registering Local Services <a id="registration"></a>
--------------------------

To register and deregister a local DNS-SD service:

1.  Register a service by creating a new instance of the
    [Tizen.Network.Nsd.DnssdService](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Nsd_1_1DnssdService.html)
    class and using its `RegisterService()` method:

    ``` {.prettyprint}
    /// Register service
    INsdService service = new DnssdService("_http._tcp");
    DnssdService dnssdService = (DnssdService)service;
    dnssdService.RegisterService();
    ```

2. Deregister the service by using the `DeregisterService()` method.

    When the `Tizen.Network.Nsd.DnssdService` class instance is no
    longer needed, destroy it with the `Dispose()` method.

    ``` {.prettyprint}
    /// Deregister service
    dnssdService.DeregisterService();
    dnssdService.Dispose();
    ```


Discovering Remote Services <a id="discovery"></a>
---------------------------

To discover remote DNS-SD services:

1.  Start discovery by creating a new instance of the
    [Tizen.Network.Nsd.DnssdBrowser](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Nsd_1_1DnssdBrowser.html)
    class and using its `StartDiscovery()` method:

    ``` {.prettyprint}
    /// Start discovery
    INsdBrowser browser = new DnssdBrowser("_http._tcp");
    DnssdBrowser dnssdBrowser = (DnssdBrowser)browser;
    dnssdBrowser.StartDiscovery();
    ```

2. When you have found the services you need, stop discovery by using
    the `StopDiscovery()` method.

    When the `Tizen.Network.Nsd.DnssdBrowser` class instance is no
    longer needed, destroy it with the `Dispose()` method.

    ``` {.prettyprint}
    /// Stop discovery
    dnssdBrowser.StopDiscovery();
    dnssdBrowser.Dispose();
    ```
