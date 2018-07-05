# OAuth 2.0


The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and the HTTP service, or by allowing the third-party application to obtain access on its own behalf.

The main features of the OAuth 2.0 API include:

- Creating an OAuth 2.0 request

  You can [create a request handle, set and retrieve request parameters, and pass the request to the OAuth 2.0 manager](#request) to request a token.

- Sending the request to the server to ask for a [grant or token](#grant)

  You can [request the authorization server for the required OAuth 2.0 grant or token](#token) using various methods and grant types.

- Managing the server response

  You can [obtain information from the OAuth 2.0 response handle](#response) returned in a callback.

**Figure: Protocol flow**

![Protocol flow](./media/oauth2_protocol_flow.png)

The OAuth 2.0 specification is defined in [[RFC 6749\]](http://tools.ietf.org/html/rfc6749) and it builds on the OAuth 1.0 [[RFC 5849\]](http://tools.ietf.org/html/rfc5849) deployment experience, as well as additional use cases and extensibility requirements gathered from the wider IETF community. The OAuth 2.0 protocol is not backward-compatible with OAuth 1.0.

<a name="grant"></a>
## Authorization Grant

An authorization grant is a credential representing the resource owner's authorization (to access its protected resources) used by the client to obtain an access token.

The specification defines the following 4 grant types as well as an extensibility mechanism for defining additional types:

- Authorization code

  The [authorization code is obtained](#req_code) by using an authorization server as an intermediary between the client and resource owner. Instead of requesting authorization directly from the resource owner, the client directs the resource owner to an authorization server, which in turn directs the resource owner back to the client with the authorization code.

  The authorization code provides some important security benefits, such as the ability to authenticate the client, as well as the transmission of the access token directly to the client without passing it through the resource owner's user-agent and potentially exposing it to others, including the resource owner.

  **Figure: Authorization code flow**

  ![Authorization code flow](./media/oauth2_auth_code.png)

- Implicit

  In the implicit flow, the client is issued an access token directly (as a result of the resource owner authorization). The grant type is implicit, as no intermediate credentials (such as an authorization code) are issued.

  Implicit grants improve the responsiveness and efficiency of some clients (such as a client implemented as an in-browser application), since it reduces the number of round trips required to obtain an access token.

  **Figure: Implicit grant flow**

  ![Implicit grant flow](./media/oauth2_implicit.png)

- Resource owner password credentials

  The resource owner password credentials (such as username and password) can be used directly as an authorization grant to obtain an access token.

  Even though this grant type requires direct client access to the resource owner credentials, the resource owner credentials are used for a single request and are exchanged for an access token. This grant type can eliminate the need for the client to store the resource owner credentials for future use, by exchanging the credentials with a long-lived access token or refresh token.

  **Figure: Resource owner password credentials flow**

  ![Resource owner password credentials flow](./media/oauth2_password.png)

- Client credentials

  The client credentials can be used as an authorization grant when the authorization scope is limited to the protected resources under the control of the client, or to protected resources previously arranged with the authorization server. Client credentials are typically used as an authorization grant when the client is acting on its own behalf (the client is also the resource owner) or is requesting access to protected resources based on an authorization previously arranged with the authorization server.

  **Figure: Client credentials flow**

  ![Client credentials flow](./media/oauth2_client_credentials.png)

To request an access token for the implicit, resource owner password credentials, or client credentials grant type, follow the [direct access token request instructions](#direct_token).

## Prerequisites

To enable your application to use the OAuth 2.0 functionality:

1. To use the OAuth 2.0 API (in [mobile](../../api/mobile/latest/group__CAPI__OAUTH2__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__OAUTH2__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/internet</privilege>
   </privileges>
   ```

2. To use the functions and data types of the OAuth 2.0 API, include the `<oauth2.h>` header file in your application:

   ```
   #include <oauth2.h>
   ```

   To ensure that an OAuth 2.0 function has been executed properly, make sure that the return is equal to `ACCOUNT_ERROR_NONE`.

3. Declare the necessary global variables and create the manager handle using the `oauth2_manager_create()` function:

   ```
   static oauth2_manager_h mgr = NULL;
   int ret = OAUTH2_ERROR_NONE;
   ret = oauth2_manager_create(&mgr)
   ```

4. When you no longer need it, free the OAuth 2.0 manager handle with the `oauth2_manager_destroy()` function:

    ```
    ret = oauth2_manager_destroy(mgr);
    ```

<a name="request"></a>
## Creating and Managing an OAuth 2.0 Request

To make a request with the OAuth 2.0 manager:

1. Create an `oauth2_request_h` request handle and use the `oauth2_request_create()` function to create the OAuth 2.0 request:

    ```
    oauth2_request_h request = NULL;
    ret = oauth2_request_create(&request);
    ```

2. Set the parameters needed for making the request.

   You can set various request properties, such as end points for authentication and token, grant type, user name, and password.

   ```
   char* auth_url = "https://accounts.google.com/o/oauth2/auth";
   char* token_url = "https://accounts.google.com/o/oauth2/token";
   char* user_name = "username";
   char* password = "password";

   ret = oauth2_request_set_auth_end_point_url(request, auth_url);

   ret = oauth2_request_set_token_end_point_url(request, token_url);

   ret = oauth2_request_set_grant_type(request, OAUTH2_GRANT_TYPE_AUTH_CODE);

   ret = oauth2_request_set_user_name(request, user_name);

   ret = oauth2_request_set_password(request, password);
   ```

   You can also retrieve request parameters from an existing request handle:

   ```
   char* auth_url = NULL;
   char* token_url = NULL;
   char* user_name = NULL;
   char* password = NULL;
   oauth2_grant_type_e grant_type;

   ret = oauth2_request_get_auth_end_point_url(request, &auth_url);

   ret = oauth2_request_get_token_end_point_url(request, &token_url);

   ret = oauth2_request_get_grant_type(request, &grant_type)

   ret = oauth2_request_get_user_name(request, &user_name);

   ret = oauth2_request_get_password(request, &password);
   ```

3. When you no longer need it, free the request handle with the `oauth2_request_destroy()` function:
   ```
   ret = oauth2_request_destroy(request);
   ```

<a name="token"></a>
## Requesting the Server for a Grant or Token

To obtain the required authorization code or access token:

<a name="req_code"></a>
- Request the authorization code.

  The authorization code grant type is used to obtain both access tokens and refresh tokens. It is a redirection-based flow that requires the client to interact with the server and receive the incoming requests (through redirection) from the authorization server.

  To request the authorization code, use the `oauth2_manager_request_authorization_grant()` function:

  ```
  void
  grant_response_cb(oauth2_response_h response, void* user_data)
  {
      /* Authorization code response callback */
      char *auth_code = NULL;
      oauth2_response_get_authorization_code(response, &auth_code);
  }

  void
  request_auth_code(void)
  {
      oauth2_manager_h mgr = NULL;
      int ret = oauth2_manager_create(&mgr);

      oauth2_request_h request = NULL;
      ret = oauth2_request_create(&request);

      /*
         Set all the required parameters needed as per the Web server's
         OAuth 2.0 authentication policy before making the request
      */

      /* Set the response_type as "code" */
      ret = oauth2_request_set_response_type(request, OAUTH2_RESPONSE_TYPE_CODE);

      /* Set the application client ID registered in the server */
      ret = oauth2_request_set_client_id(request, "app_client_id");

      /*
         Set the redirect URI for the server
         to redirect the flow after the authentication
      */
      ret = oauth2_request_set_redirection_url(request, "https://developer.tizen.org");

      /*
         Request the server for the authorization grant;
         the response from the server is returned in the callback
      */
      ret = oauth2_manager_request_authorization_grant(mgr, request, grant_response_cb, user_data);
  }
  ```

- Request the access token.

  Access tokens are credentials used to access protected resources. An access token is a string representing an authorization issued to the client. Tokens represent specific access scopes and durations, granted by the resource owner, and enforced by the resource server and authorization server.

  - Request the access token with the authorization code.

    In the authorization code grant type, instead of requesting authorization directly from the resource owner, the client directs the resource owner to an authorization server, which in turn directs the resource owner back to the client with the authorization code.

    1. [Request the authorization code](#req_code) with the `oauth2_manager_request_authorization_grant()` function. The authorization code is returned in the callback.

        ```
        void
        request_auth_code(void)
        {
            oauth2_manager_h mgr = NULL;
            int ret = oauth2_manager_create(&mgr);

            oauth2_request_h request = NULL;
            ret = oauth2_request_create(&request);

            /*
               Set all the required parameters needed as per the Web server's
               OAuth 2.0 authentication policy before making the request
            */

            ret = oauth2_request_set_auth_end_point_url(request, "https://login.live.com/oauth20_authorize.srf");

            ret = oauth2_request_set_token_end_point_url(request, "https://login.live.com/oauth20_token.srf");

            ret = oauth2_request_set_redirection_url(request, "https://developer.tizen.org");

            ret = oauth2_request_set_client_id(request, "WINDOWS_CLIENT_ID");

            ret = oauth2_request_set_client_secret(request, "WINDOWS_CLIENT_SECRET");

            ret = oauth2_request_set_scope(request, "wl.basic");

            ret = oauth2_request_set_response_type(request, OAUTH2_RESPONSE_TYPE_CODE);

            if (mgr && request)
                ret = oauth2_manager_request_authorization_grant(mgr, request, grant_response_cb, request);
        }
        ```

    2. Use the authorization code to request the access token by calling the `oauth2_manager_request_access_token()` function. The response from the server is returned in a callback function where the access token can be retrieved:

        ```
        void
        access_token_cb(oauth2_response_h response, void* user_data)
        {
            /* Access token response callback */

            char *access_token = NULL;
            oauth2_response_get_access_token(response, &access_token);
        }

        void
        grant_response_cb(oauth2_response_h response, void* user_data)
        {
            /* Authorization code response callback */

            char *auth_code = NULL;
            oauth2_response_get_authorization_code(response, &auth_code);

            if (auth_code) {
                oauth2_manager_h mgr = NULL;
                int ret = oauth2_manager_create(&mgr);

                /* Request handle was passed as the user data */
                oauth2_request_h request = (oauth2_request_h) user_data;

                ret = oauth2_request_set_authorization_code(request, auth_code);

                if (mgr && request)
                    ret = oauth2_manager_request_access_token(mgr, request, access_token_cb, NULL);
            }
        }
        ```

  - Request the access token directly.

    You can request an access token in a single step without obtaining the authorization code explicitly. For the authorization code grant type, the code is obtained after authentication and passed to the server to obtain the access token internally. For implicit, resource owner password credentials, and client credentials grant types, you can obtain the access token directly.

    To obtain the access token directly, use the `oauth2_manager_request_token()` function. The response from the server is included in the callback.

    ```
    void
    token_response_cb(oauth2_response_h response, void* user_data)
    {
        /* Access token response callback */

        char *access_token = NULL;
        oauth2_response_get_access_token(response, &access_token);
    }

    void
    request_access_token(void)
    {
        oauth2_manager_h mgr = NULL;
        int ret = oauth2_manager_create(&mgr);

        oauth2_request_h request = NULL;
        ret = oauth2_request_create(&request);

        /*
           Set all the required parameters needed as per the Web server's
           OAuth 2.0 authentication policy before making the request
        */

        ret = oauth2_request_set_auth_end_point_url(request, "https://www.facebook.com/dialog/oauth");

        ret = oauth2_request_set_redirection_url(request, "https://developer.tizen.org");

        ret = oauth2_request_set_client_id(request, "SAMPLE_CLIENT_ID");

        ret = oauth2_request_set_scope(request, "read_stream");

        ret = oauth2_request_set_response_type(request, OAUTH2_RESPONSE_TYPE_TOKEN);

        if (mgr && request) {
            ret = oauth2_manager_request_token(mgr, request, token_response_cb, request);
            if (ret != OAUTH2_ERROR_NONE)
                dlog_print(DLOG_ERROR, LOG_TAG, "Access Token request failed");
        }
    }
    ```

- Refresh the access token.

  Refresh tokens are credentials used to obtain access tokens. Refresh tokens are issued to the client by the authorization server and are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with an identical or narrower scope.

  To refresh an access token, use the `oauth2_manager_refresh_access_token()` function. The response from the server is included in the callback.

  ```
  void
  token_response_cb(oauth2_response_h response, void* user_data)
  {
      /* Access token response callback */

      char *access_token = NULL;
      oauth2_response_get_access_token(response, &access_token);
  }

  void
  refresh_token_response_cb(oauth2_response_h response, void* user_data)
  {
      char *acc_token = NULL;
      oauth2_response_get_access_token(response, &acc_token);

      char *ref_token = NULL;
      oauth2_response_get_refresh_token(response, &ref_token);

      char *auth_code = NULL;
      oauth2_response_get_authorization_code(response, &auth_code);
      if (auth_code) {
          oauth2_manager_h mgr = (oauth2_manager_h) user_data;

          oauth2_request_h request = NULL;

          int ret = oauth2_request_create(&request);

          /*
             Set all the required parameters needed as per the Web server's
             OAuth 2.0 authentication policy before making the request
          */

          ret = oauth2_request_set_refresh_token_url(request, "https://www.googleapis.com/oauth2/v3/token");

          ret = oauth2_request_set_refresh_token(request, ref_token);

          ret = oauth2_request_set_client_id(request, "GOOGLE_CLIENT_ID");

          ret = oauth2_request_set_client_secret(request, "GOOGLE_CLIENT_SECRET");

          ret = oauth2_request_set_grant_type(request, OAUTH2_GRANT_TYPE_REFRESH);

          ret = oauth2_request_set_client_authentication_type(request, OAUTH2_CLIENT_AUTHENTICATION_TYPE_REQUEST_BODY);

          if (mgr && request)
              ret = oauth2_manager_refresh_access_token(mgr, request, token_response_cb, NULL);
      }
  }

  void
  request_access_token(void)
  {
      oauth2_manager_h mgr = NULL;
      int ret = oauth2_manager_create(&mgr);

      oauth2_request_h request = NULL;
      ret = oauth2_request_create(&request);

      /*
         Set all the required parameters needed as per the Web server's
         OAuth 2.0 authentication policy before making the request
      */

      ret = oauth2_request_set_auth_end_point_url(request, "https://accounts.google.com/o/oauth2/auth");

      ret = oauth2_request_set_token_end_point_url(request, "https://accounts.google.com/o/oauth2/token");

      ret = oauth2_request_set_redirection_url(request, "https://localhost:8080");

      ret = oauth2_request_set_client_id(request, "GOOGLE_CLIENT_ID");

      ret = oauth2_request_set_client_secret(request, "GOOGLE_CLIENT_SECRET");

      ret = oauth2_request_set_scope(request, "email");

      ret = oauth2_request_set_response_type(request, OAUTH2_RESPONSE_TYPE_CODE);

      if (mgr && request)
          ret = oauth2_manager_request_token(mgr, request, refresh_token_response_cb, mgr);
  }
  ```

<a name="response"></a>
## Managing an OAuth 2.0 Response

The response from the server is bundled in the `oauth2_response_h` handle and returned in the callbacks, from which all the various response parameters can be obtained.

To manage the OAuth 2.0 response:

1. Retrieve the response parameters from the response handle.

   You can get various response information, such as the authorization code, access token, state, and token type.

   ```
   char* auth_code = NULL;
   char* access_token = NULL;
   char* state = NULL;
   char* token_type = NULL;

   ret = oauth2_response_get_authorization_code(response, &auth_code);

   ret = oauth2_response_get_access_token(response, &access_token);

   ret = oauth2_response_get_state(response, &state);

   ret = oauth2_response_get_token_type(response, &token_type);
   ```

2. Handle response errors.

   If the created request is incorrect or missing required permissions, the server response contains an error. Retrieve the error information from the response handle to check the issue:

   ```
   oauth2_error_h e_handle = NULL;
   int error_code = 0;
   int platform_error_code = 0;
   char *description = NULL;
   char *uri = NULL;
   char *error_val = NULL;

   oauth2_response_get_error(response, &e_handle);

   oauth2_error_get_code(e_handle, &error_code, &platform_error_code);

   oauth2_error_get_description(e_handle, &description);

   oauth2_error_get_uri(e_handle, &uri);

   oauth2_error_get_custom_data(e_handle, "error", &error_val);
   ```

3. When you no longer need it, free the response handle with the `oauth2_response_destroy()` function:

    ```
    ret = oauth2_response_destroy(response);
    ```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
