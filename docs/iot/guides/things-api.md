# Things SDK API

Developing "Things" which are market-ready (with cloud support) has been a challenge for most of the companies and individual developers. The SmartThings&trade; Things SDK API helps you to create new IoT devices easily. The version number of the first release is 0.9, which is the preview version.

The 2 core components for creating a new device are:

-   SmartThings&trade; Things JSON Configuration file (`device_definition.json`)

    For more information on the configuration file details, see [Device Definition](things-api-device.md).

-   Application logic and user interaction

    For more information on using the SmartThings&trade; Things SDK API, see [API Usage](things-api-guide.md).

**Figure: Creating a new device**

![Creating a new device](media/thing_api_new_device.png)

The SmartThings&trade;(ST) Things SDK provides you an easy and configurable option to build and deploy your own devices quickly:

-   The ST Things SDK provides JSON-based things definition, which:
    -   Defines device and platform information.
    -   Defines resources that the thing is supporting.
    -   Defines an easy-setup configuration.
-   The ST Things SDK provides spec-agnostic APIs, which:
    -   Hide the interface and resource type details in a request data.
    -   Divide a collection resource request into single resource requests.
    -   Provide the "property_key" in case of the GET request.

The SmartThings&trade; Things SDK API provides the following benefits for you:

-   Supporting pin-based and UserConfirm(Certificate)-based OTM in EasySetup.
-   Providing a JSON-based device/resource definition method in a single file:
    -   Includes Single resource and Collection resource support.
-   Resources that are defined in a JSON file/string are made internally.
-   Easy APIs to handle requests and responses:
    -   Supports request methods: GET and POST.
    -   You only need to make a representation (bundle of property values) for a response.
    -   You do not need to handle interfaces, as they are handled internally.
    -   The request to a collection resource is divided into individual requests to single resources.
-   Cloud setup (Sign-up/Sign-in/Sign-out/Resource publish to cloud) is handled internally.
-   Following operations are handled internally:
    -   To respond to an Access Point List (APList) request from a client.
    -   To start and stop softAP.
    -   To connect to a target WiFi AP (Enroller).
    -   To make the whole response data according to the interfaces (such as `oic.if.baseline`, `oic.if.b`, and `oic.if.ll`).
