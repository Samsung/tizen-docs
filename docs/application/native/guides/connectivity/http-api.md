# HTTP


HTTP (Hypertext Transfer Protocol) is a networking protocol for distributed, collaborative hypermedia information systems. It allows applications to connect to a Web server to fetch and transmit a Web resource.

The main features of the HTTP API include:

- HTTP session

  A session is a set of 1 or more transactions. You must [create an HTTP session](#session) before you can create transactions.

- HTTP transaction

  A transaction represents a single operation between a client and a server (a single request to the Web server). To [request for a resource from a Web server](#transaction), create a transaction handle and open an HTTP transaction from the HTTP session.

- HTTP request

  A request is message sent from a client to a server (for example, a request to fetch a resource from the Web server).

  To send a request, set the remote Web server resource path with the `http_transaction_request_set_uri()` function, and submit the request with the `http_transaction_submit()` function.

- HTTP response

  A response is a message sent from a server to a client.

## Prerequisites

To enable your application to use the HTTP functionality:

1. To use the functions and data types of the HTTP API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__HTTP__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__HTTP__MODULE.html) applications), include the `<http.h>` header file in your application:

   ```
   #include <http.h>
   ```

2. Initialize the HTTP functionality using the `http_init()` function:

   ```
   int ret = HTTP_ERROR_NONE;

   ret = http_init();
   if (ret != HTTP_ERROR_NONE)
       printf("http_init failed: %d", ret);
   ```

   When no longer needed, deinitialize the HTTP functionality:

   ```
   int ret = HTTP_ERROR_NONE;

   ret = http_deinit();
   if (ret != HTTP_ERROR_NONE)
       printf("http_deinit failed: %d", ret);
   ```

<a name="session"></a>
## Managing Sessions

The application can manage multiple sessions at the same time. When creating the session, you can set the session mode:

- The normal mode (`HTTP_SESSION_MODE_NORMAL`) means that the session has only 1 connection. All transactions in the session share that connection, and the transactions are processed one at a time.
- The pipelining mode (`HTTP_SESSION_MODE_PIPELINING`) means that multiple transactions can be processed concurrently. This mode can reduce the network latency.

To manage HTTP sessions:

1. Create an HTTP session handle with the `http_session_create()` function:
    ```
    int ret = HTTP_ERROR_NONE;
    http_session_h session = NULL;

    ret = http_session_create(HTTP_SESSION_MODE_NORMAL, &session);
    if (ret != HTTP_ERROR_NONE)
        printf("http_session_create failed: %d", ret);
    ```

2. Set the auto redirection for the session with the `http_session_set_auto_redirection()` function:
    ```
    int ret = HTTP_ERROR_NONE;
    bool auto_redirect = true;

    ret = http_session_set_auto_redirection(session, auto_redirect);
    if (ret != HTTP_ERROR_NONE)
        printf("http_session_set_auto_redirection failed: %d", ret);
    ```

3. When no longer needed, destroy all transactions and the session:

   ```
   int ret = HTTP_ERROR_NONE;

   ret = http_session_destroy_all_transactions(session);
   if (ret != HTTP_ERROR_NONE)
       printf("http_session_destroy_all_transactions failed: %d", ret);

   ret = http_session_destroy(session);
   if (ret != HTTP_ERROR_NONE)
       printf("http_session_destroy failed: %d", ret);
   ```

<a name="transaction"></a>
## Managing Transactions

To manage HTTP transactions:

1. Create an HTTP transaction handle with the `http_session_open_transaction()` function and the session handle.

   The function requires the HTTP method defined by the `http_method_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__HTTP__MODULE.html#ga43d17339ae0c54fb1b72ec6bb73285ec) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__HTTP__MODULE.html#ga43d17339ae0c54fb1b72ec6bb73285ec) applications) as its first parameter. The main methods are:
   - GET: The application can retrieve a resource from a remote Web server.
   - POST: The application can send data to a Web server.
   - PUT: The application can replace all current representations of the Web server resource with the uploaded content.

   ```
   int ret = HTTP_ERROR_NONE;

   http_transaction_h transaction = NULL;
   ret = http_session_open_transaction(session, HTTP_METHOD_GET, &transaction);
   if (ret != HTTP_ERROR_NONE)
       printf("http_session_open_transaction failed: %d", ret);
   ```
   The transaction handle is used to manage the request and response.

2. Register transaction callbacks to receive the response and monitor the transaction state:

   - Use the `http_transaction_set_received_header_cb()` and `http_transaction_set_received_body_cb()` functions to register callbacks for fetching the Web server resource header information and the response body.
   - Use the `http_transaction_set_uploaded_cb()` function to register a callback for the upload status of the remote Web server resource.
   - Use the `http_transaction_set_completed_cb()` function to register a callback for the completion status of the current transaction.
   - Use the `http_transaction_set_aborted_cb()` function to register a callback for the failure status of the current transaction.

   ```
   /* Callback for receiving the response header */
   void
   header_cb(http_transaction_h transaction, char* header, size_t header_len, void* user_data) {}

   http_transaction_set_received_header_cb(transaction, header_cb, NULL);

   /* Callback for receiving the response body */
   void
   body_cb(http_transaction_h transaction, char* body, size_t size, size_t nmemb, void* user_data) {}

   http_transaction_set_received_body_cb(transaction, body_cb, NULL);

   /* Callback for monitoring data uploads */
   void
   uploaded_cb(http_transaction_h transaction, char* body, int recommended_chunk, void* user_data) {}

   http_transaction_set_uploaded_cb(transaction, uploaded_cb, NULL);

   /* Callback for monitoring transaction completions */
   void
   completed_cb(http_transaction_h transaction, char* body, void* user_data) {}

   http_transaction_set_completed_cb(transaction, completed_cb, NULL);

   /* Callback for monitoring transaction abortions */
   void
   aborted_cb(http_transaction_h transaction, int reason, void* user_data) {}

   http_transaction_set_aborted_cb(transaction, aborted_cb, NULL);
   ```

3. Send a request:

   1. Set the request URI for the transaction:

      ```
      int ret = HTTP_ERROR_NONE;
      char uri[1024] = "www.example.com";

      ret = http_transaction_request_set_uri(transaction, uri);
      if (ret != HTTP_ERROR_NONE)
          printf("http_transaction_request_set_uri failed: %d", ret);
      ```

   2. Set the request method:

      ```
      int ret = HTTP_ERROR_NONE;
      http_method_e method = HTTP_METHOD_GET;

      ret = http_transaction_request_set_method(transaction, method);
      if (ret != HTTP_ERROR_NONE)
          printf("http_transaction_request_set_method failed: %d", ret);
      ```

   3. Set the HTTP version of the transaction:

      ```
      int ret = HTTP_ERROR_NONE;
      http_version_e version = HTTP_VERSION_1_1;

      ret = http_transaction_request_set_version(transaction, version);
      if (ret != HTTP_ERROR_NONE)
          printf("http_transaction_request_set_version failed: %d", ret);
      ```

   4. Submit the transaction for the defined request URI:

      ```
      int ret = HTTP_ERROR_NONE;

      ret = http_transaction_submit(transaction);
      if (ret != HTTP_ERROR_NONE)
          printf("http_transaction_submit failed: %d", ret);
      ```

4. The response arrives in the registered response header and response body callbacks.

   To retrieve response status details:

   - Get the status code of the submitted transaction:

     ```
     int ret = HTTP_ERROR_NONE;
     http_status_code_e status_code = -1;

     ret = http_transaction_response_get_status_code(transaction, &status_code);
     if (ret != HTTP_ERROR_NONE)
         printf("http_transaction_response_get_status_code failed: %d", ret);
     ```

   - Get the status version of the submitted transaction:

     ```
     int ret = HTTP_ERROR_NONE;
     http_version_e version = -1;

     ret = http_transaction_response_get_version(transaction, &version);
     if (ret != HTTP_ERROR_NONE)
         printf("http_transaction_response_get_version failed: %d", ret);
     ```

5. When no longer needed, destroy the transaction:

   ```
   int ret = HTTP_ERROR_NONE;

   ret = http_transaction_destroy(transaction);
   if (ret != HTTP_ERROR_NONE)
       printf("http_transaction_destroy failed: %d", ret);
   ```

The following example shows the code required for a simple HTTP GET, HTTPS GET, or HTTP POST request:

```
int ret = HTTP_ERROR_NONE;
/* Request URI for HTTP GET */
char uri[1024] = "www.example.com";
/*
   Request URI for HTTPS GET:
   char uri[1024] = "https://httpbin.org/get";
   Request URI and data for HTTP POST:
   char uri[1024] = "http://posttestserver.com/post.php";
   const char* post_msg = "name=tizen&project=http";
*/

ret = http_session_create(HTTP_SESSION_MODE_NORMAL, &session);
if (ret != HTTP_ERROR_NONE)
    printf("http_session_create failed: %d", ret);

/* Transaction for HTTP and HTTPS GET */
ret = http_session_open_transaction(session, HTTP_METHOD_GET, &transaction);
/*
   Transaction for HTTP POST:
   ret = http_session_open_transaction(session, HTTP_METHOD_POST, &transaction);
*/
if (ret != HTTP_ERROR_NONE)
    printf("http_session_open_transaction failed: %d", ret);

ret = http_transaction_request_set_uri(transaction, uri);
if (ret != HTTP_ERROR_NONE)
    printf("http_transaction_request_set_uri failed: %d", ret);

/*
   Data management for HTTP POST:
   http_transaction_set_ready_to_write(transaction, TRUE);
   http_transaction_request_write_body(transaction, post_msg);
*/

ret = http_transaction_submit(transaction);
if (ret != HTTP_ERROR_NONE)
    printf("http_transaction_submit failed: %d", ret);
```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
