# Curl


You can implement URL-related transfer activities in Tizen without a Web browser using the open source [libcurl](http://curl.haxx.se/libcurl/) library, version 7.40. libcurl is a client-side URL transfer library that supports, among other protocols, HTTP, HTTPS, FTP, and file URIs.

The main features of the Curl API include:

- Initializing the HTTP and HTTPS request connection

  To allow the application to handle HTTP and HTTPS requests with various options, you must initialize the libcurl library and the connection.

  > **Note**  
  > In some cases, such as with Internet access, your application requires some privileges. For more information on which privileges to set in the application manifest file, see [Non-API Bound Privileges](../../tutorials/details/sec-privileges.md#nonAPI).

- Managing the proxy address

  You can [get and set the proxy address](#manage) in multiple ways.

  > **Note**  
  > In a proxy environment, the libcurl library does not know the proxy address. To handle HTTP and HTTPS requests in a proxy environment, first get the proxy address using the [connection manager](connection.md), and then set the proxy address using the Curl API.

- Transferring HTTP requests

  You can [transfer HTTP requests](#request) using the `curl_easy_setopt()` function.

## Prerequisites

To enable your application to use the Curl functionality:

1. To use the Curl API (in [mobile](../../api/mobile/latest/group__OPENSRC__CURL__FRAMEWORK.html) and [wearable](../../api/wearable/latest/group__OPENSRC__CURL__FRAMEWORK.html) applications) and the libcurl library, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/internet</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Curl API, include the `<curl.h>` header file in your application. You must also add the `<net_connection.h>` header file to get the proxy address.

   ```
   #include <curl.h>
   #include <net_connection.h>
   ```

3. Initialize the Curl library and the Curl handle using the `curl_easy_init()` function:

   ```
   CURL *curl;
   CURLcode curl_err;
   curl = curl_easy_init();
   ```

4. Create and initialize a connection handle by calling the `connection_create()` function:

   ```
   connection_h connection;
   int conn_err;
   conn_err = connection_create(&connection);
   if (conn_err != CONNECTION_ERROR_NONE) {
       /* Error handling */

       return;
   }
   ```

5. When no longer needed, clear the Curl and connection handle to finish the HTTP transaction:

   ```
   curl_easy_cleanup(curl);
   connection_unset_proxy_address_changed_cb(connection);
   connection_destroy(connection);
   ```

<a name="manage"></a>
## Managing the Proxy Address

There are 2 ways for getting and setting the proxy address:

- To get the proxy address directly, use the `connection_get_proxy()` function of the Connection Manager API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html) applications):
    ```
    char *proxy_address;
    conn_err = connection_get_proxy(connection, CONNECTION_ADDRESS_FAMILY_IPV4, &proxy_address);
    ```
  To set the proxy address, use the `curl_easy_setopt()` function with the `CURLOPT_PROXY` parameter:
    ```
    if (conn_err == CONNECTION_ERROR_NONE && proxy_address)
        curl_easy_setopt(curl, CURLOPT_PROXY, proxy_address);
    ```
- To be notified whenever the proxy address changes, register a callback with the `connection_set_proxy_address_changed_cb()` function of the Connection Manager API:
    ```
    conn_err = connection_set_proxy_address_changed_cb(connection,
                                                       __proxy_address_changed_cb, NULL);
    if (conn_err != CONNECTION_ERROR_NONE) {
        /* Error handling */

        return;
    }
    ```
  The new proxy address is passed in the callback parameters. To set the proxy address, use the `curl_easy_setopt()` function with the `CURLOPT_PROXY` parameter:
    ```
    static void
    __proxy_address_changed_cb(const char *ipv4_address,
                               const char *ipv6_address, void *user_data)
    {
        curl_easy_setopt(curl, CURLOPT_PROXY, ipv4_address);
    }
    ```

<a name="request"></a>
## Transferring HTTP Requests

To transfer HTTP requests, set the URL with the `curl_easy_setopt()` function and start the transfer with the `curl_easy_perform()` function:

```
curl_easy_setopt(curl, CURLOPT_URL, "https://www.tizen.org/");
curl_err = curl_easy_perform(curl);
if (curl_err != CURLE_OK)
    /* Error handling */
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
