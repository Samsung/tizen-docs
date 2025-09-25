# Curl


You can implement URL-related transfer activities in Tizen without a Web browser using the open source [libcurl](http://curl.haxx.se/libcurl/) library. libcurl is a client-side URL transfer library that supports, among other protocols, HTTP, HTTPS, FTP, and file URIs.

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

1. To use the [Curl API](../../api/common/latest/group__OPENSRC__CURL__FRAMEWORK.html) and the libcurl library, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

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

- To get the proxy address directly, use the `connection_get_proxy()` function of the [Connection Manager API](../../api/common/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html):
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

To transfer HTTP requests, set the URL with the `curl_easy_setopt()` function and start the transfer with the `curl_easy_perform()` function. The following example shows a complete HTTP request implementation:

```
#include <curl.h>

/* Callback function to write received data */
static size_t
write_callback(void *contents, size_t size, size_t nmemb, void *userp)
{
    size_t realsize = size * nmemb;
    
    /* In a real application, you would handle the received data here */
    /* This example just tracks the size of received data */
    
    return realsize;
}

int
send_http_request(void)
{
    CURL *curl;
    CURLcode curl_err;
    
    /* Initialize Curl library and handle */
    curl = curl_easy_init();
    if (!curl) {
        /* Error handling */
        return -1;
    }
    
    /* Set the target URL for HTTP request */
    curl_easy_setopt(curl, CURLOPT_URL, "http://example.com/");
    
    /* Set callback function to handle received data */
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
    
    /* Enable verbose mode for debugging (optional) */
    /* curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L); */
    
    /* Perform the HTTP request */
    curl_err = curl_easy_perform(curl);
    if (curl_err != CURLE_OK) {
        /* Error handling: request failed */
    } else {
        /* HTTP request completed successfully */
        
        /* Get HTTP response code */
        long http_code = 0;
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &http_code);
        /* HTTP response code available in http_code variable */
    }
    
    /* Clean up Curl handle */
    curl_easy_cleanup(curl);
    
    return (curl_err == CURLE_OK) ? 0 : -1;
}
```

For more advanced HTTP requests, you can set additional options:

- **Custom headers**: Use `CURLOPT_HTTPHEADER` to add custom HTTP headers
    ```
    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "Content-Type: application/json");
    headers = curl_slist_append(headers, "Authorization: Bearer token123");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    /* Don't forget to free the headers list after the request */
    curl_slist_free_all(headers);
    ```

- **POST requests**: Use `CURLOPT_POST` and `CURLOPT_POSTFIELDS` to send POST data
    ```
    curl_easy_setopt(curl, CURLOPT_POST, 1L);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "param1=value1&param2=value2");
    ```

- **Follow redirects**: Use `CURLOPT_FOLLOWLOCATION` to automatically follow HTTP redirects
    ```
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    ```

<a name="https-config"></a>
## HTTPS Configuration

To make HTTPS requests, use the basic HTTP request structure from the [Transferring HTTP Requests](#request) section and add the following SSL/TLS configuration options:

```
/* After setting the URL and before performing the request, add SSL configuration */

/* Configure SSL certificate verification for HTTPS */
curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 1L);  /* Verify the peer's SSL certificate */
curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 2L);  /* Check the host name in the certificate */

/* Set CA certificate path (use system default certificates) */
/* For custom certificates, use: curl_easy_setopt(curl, CURLOPT_CAINFO, "/path/to/cacert.pem"); */

/* For SSL/TLS version control (optional) */
/* curl_easy_setopt(curl, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1_2); */

/* For client certificate authentication (if required by the server) */
/* curl_easy_setopt(curl, CURLOPT_SSLCERT, "/path/to/client.crt"); */
/* curl_easy_setopt(curl, CURLOPT_SSLKEY, "/path/to/client.key"); */
/* curl_easy_setopt(curl, CURLOPT_KEYPASSWD, "private_key_password"); */
```

> **Note**  
> SSL certificate verification is crucial for secure HTTPS communication. In production environments, always keep `CURLOPT_SSL_VERIFYPEER` enabled to ensure secure connections. For testing purposes with self-signed certificates, you can temporarily disable it with `curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);`, but this is not recommended for production applications as it exposes your application to security risks.

Here's a complete example that modifies the HTTP request function for HTTPS:

```
int
send_https_request(const char *url)
{
    CURL *curl;
    CURLcode curl_err;
    
    /* Initialize Curl library and handle */
    curl = curl_easy_init();
    if (!curl) {
        /* Error handling: failed to initialize Curl */
        return -1;
    }
    
    /* Set the target URL for HTTPS request */
    curl_easy_setopt(curl, CURLOPT_URL, url);
    
    /* Configure SSL certificate verification for HTTPS */
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 1L);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 2L);
    
    /* Set callback function to handle received data (same as HTTP example) */
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
    
    /* Perform the HTTPS request */
    curl_err = curl_easy_perform(curl);
    if (curl_err != CURLE_OK) {
        /* Error handling: HTTPS request failed */
    } else {
        /* HTTPS request completed successfully */
        
        /* Get HTTP response code */
        long http_code = 0;
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &http_code);
        /* HTTP response code available in http_code variable */
    }
    
    /* Clean up Curl handle */
    curl_easy_cleanup(curl);
    
    return (curl_err == CURLE_OK) ? 0 : -1;
}
```

## Related information
- Dependencies
  - Since Tizen 2.4
- API References
  - [Curl API](../../api/common/latest/group__OPENSRC__CURL__FRAMEWORK.html)
  - [Connection Manager API](../../api/common/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html)
