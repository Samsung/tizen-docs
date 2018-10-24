# Creating Applications with Connectivity and Network

If you want to create applications that offer connectivity and network
features to the user, Tizen provides various options for you.

Connectivity in the application allows the user to access various
networks to use data services, or connect to other devices. Optimal use
of the connectivity features allows your application to manage data
connections and ensure cost-efficient control over the usage of network
resources.

When creating a connectivity application, you can implement the
following features:

-   [Network operations](app-connectivity-operation.md)
    -   To handle network operations, you must know which networks are
        currently available and in use. You can access the network
        connection state through a connection handle.
    -   You can download HTTP content from the Internet through a
        network connection. You can use an open source
        [libcurl](http://curl.haxx.se/libcurl/) library, or a Tizen
        [Download](../../api/mobile/latest/group__CAPI__WEB__DOWNLOAD__MODULE.html)
        API for the download tasks.
    -   When you use the data services of various networks, the
        responses are often composed in XML or JSON format. To handle
        the data in the responses, you need to parse XML and JSON.
-   [Network usage](app-connectivity-usage.md)
    -   When the connection changes from one network to another or the
        mobile network service details change, the application must
        receive a notification and take actions to ensure that only
        tasks appropriate for a specific network or service state
        are processed. For example, you do not want to perform expensive
        download operations if the mobile home network changes to
        another network (roaming).
    -   You can access information about the state of the specific
        network connection, for example, whether the Wi-Fi connection is
        active or inactive.
    -   You can retrieve statistical information about the network
        usage, such as the amount of sent or received data.
-   [P2P connections with Wi-Fi Direct&reg;](app-connectivity-p2p.md)
    -   You can find nearby Wi-Fi Direct devices and form a Wi-Fi Direct
        group to communicate with them.
    -   Tizen also supports TDLS, which operates in the background of a
        Wi-Fi network to optimize performance.
