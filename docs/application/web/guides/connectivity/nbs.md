Network Bearer Selection
========================

You can set a cellular network as a preferred route for Internet connections with specified domains.

This feature is supported in mobile applications only.

The main features of the Network Bearer Selection API include:

-   Requesting a route

    You can [request a preferred network](#request) for the Internet connection with a specified domain.

    The request implements a routing policy for Internet connections from the application that demanded them, as well as from other programs.

- Releasing a route

    You can [cancel the preference](#release) for a particular network for the Internet connection with a specified domain.

    The routing policy can be terminated any time. All rules requested by the application are terminated at the end of the application life-cycle.


Prerequisites
-------------

To use the [Network Bearer Selection](../../api/latest/device_api/mobile/tizen/networkbearerselection.html) API, the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/internet"/>
<tizen:privilege name="http://tizen.org/privilege/networkbearerselection"/>
```


<a name="request"></a>

## Requesting a Route

To request a preferred route for Internet connection with the "www.tizen.org" host:

1.  Define the needed callbacks:

    ```
    var statuscb = {
        onsuccess: function() {
            console.log('Routing policy requested');
        },
        ondisconnected: function() {
            console.log('Disconnected');
        }
    };

    function onerror(error) {
        console.log(error.code + ' error occurred: ' + error.message);
    }
    ```

2. To request a routing policy, use the `requestRouteToHost()` method of the [NetworkBearerSelection](../../api/latest/device_api/mobile/tizen/networkbearerselection.html#NetworkBearerSelection) interface:

    ```
    tizen.networkbearerselection.requestRouteToHost('CELLULAR', 'www.tizen.org', statuscb, onerror);
    ```


<a name="release"></a>
## Releasing a Route

To cancel the routing policy for the connection with the "www.tizen.org" host:

1.  Define the needed callbacks:

    ```
    function onsuccess() {
        console.log('Routing policy cancelled');
    }

    function onerror(error) {
        console.log(error.code + ' error occurred: ' + error.message);
    }
    ```

2. To terminate the policy, use the `releaseRouteToHost()` method of the [NetworkBearerSelection](../../api/latest/device_api/mobile/tizen/networkbearerselection.html#NetworkBearerSelection) interface:

    ```
    tizen.networkbearerselection.releaseRouteToHost('CELLULAR', 'www.tizen.org', onsuccess, onerror);
    ```

## Related Information
* Dependencies    
    - Tizen 2.4 and Higher for Mobile
