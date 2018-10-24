# Creating Applications with Content Sharing

If you want to create applications that offer content sharing features
to the user, Tizen provides various options for you.

You can share various types of content (text, binaries, and files)
between applications on the same device using the application control
features, which allow you to use features in other applications, or
advertise your own features and allow others to use them. In addition,
you can exchange simple NDEF messages (such as business cards)
wirelessly with closely coupled devices using a Near Field Communication
(NFC) P2P connection.

When creating a content sharing application, you can implement the
following features:

-   [Sending content to other applications](app-contentshare-send.md)
    -   You can send text to other applications. For example, a browser
        application can share the URL of a recently visited site with a
        messenger or email application.
    -   You can share single or multiple binary items with
        other applications.
    -   You can share files with other applications. For example, you
        can send an image file to a viewer application to allow the user
        to see it.
-   [Receiving content from other
    applications](app-contentshare-receive.md)
    -   To allow other applications to find and use your application
        features (such as share various data with you), you must
        advertise your available features by exporting them as
        application controls.
    -   When another application sends content to you, your application
        is automatically launched, and you must handle the incoming data
        using the application control callback.
    -   If the incoming request contains extra data, you must read it
        and react to it appropriately.
-   [Sharing through NFC](app-contentshare-nfc.md)
    -   To share data with other devices, you must first ensure that the
        device supports NFC and then initialize the NFC feature.
    -   You can send and receive simple NDEF messages through the NFC
        P2P connection.

To share content through application controls, you must use the App
Control API (in
[mobile](../../api/mobile/latest/group__CAPI__APP__CONTROL__MODULE.html)
and
[wearable](../../api/wearable/latest/group__CAPI__APP__CONTROL__MODULE.html)
applications). Application controls are a way of sharing an
application's functionality in Tizen. The App Control API provides
functions for launching other applications with a specific operation,
URI, MIME type, and extra data, and for settings and getting the
details:

-   The mandatory operation information defines the action to
    be performed.
-   The URI and MIME type contain information about the content to
    be handled.
-   The extra data consists of key-value pairs, which provide additional
    information for the operation.

By specifying a proper operation with the content information, your
application can share the content with other applications. On the other
hand, to allow other applications to find and launch your application,
you can advertise your application features by declaring your
application control information in the `tizen-manifest.xml` file.
