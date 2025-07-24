# Autofill Service

Autofill Service application is a service application to store the user input and provides stored data. Developers can implement the Autofill Service in their own application to serve the Autofill information.

The main features of the Autofill Service API include:

- Receive Authentication Information

  You can [receive the request of authentication, and send the authentication information](#receive-authentication-information).

- Receive Fill Request and Send Fill Response

  You can [receive the fill request, and send the fill response](#receive-fill-request-and-send-fill-response).

- Receive Request of Saving Autofill Data

  You can [receive the request of saving the autofill data](#receive-request-of-saving-autofill-data).

## Prerequisites

1. To use the Autofill Service API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__AUTOFILL__SERVICE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__AUTOFILL__SERVICE__MODULE.html) applications), the application must have metadata key in the `tizen-manifest.xml` file to be recognized as an Autofill Service:

   ```xml
    <service-application ...>
        <metadata key="autofill-service" value="true"/>
    </service-application>
   ```

2. To use the functions and data types of the Autofill Service API, include the `<autofill_service.h>` header file in your application:

   ```c
   #include <autofill_service.h>
   ```

## Initialization

   1. To use the autofill service library, initialize the autofill service using the `autofill_service_initialize()` function:

      ```c
      bool service_app_create(void *data)
      {
          autofill_service_initialize();

          ...

          return true;
      }
      ```

   2. To receive each request, such as authentication request, fill request, and commit, register the callback functions:

      ```c
      bool service_app_create(void *data)
      {
          autofill_service_initialize();

          autofill_service_set_auth_info_requested_cb(_auth_info_request_received_cb, NULL);
          autofill_service_set_fill_requested_cb(_fill_request_received_cb, NULL);
          autofill_service_set_commited_cb(_commit_received_cb, NULL);

          return true;
      }
      ```

## Receive Authentication Information

1. To receive the request of authentication information, create a callback using the `autofill_service_set_auth_info_requested_cb()` function:

   > **Note**
   >
   > Perform the action to certificate to use a method such as **biometrics or entering password** in this callback function.

    ```c
    static void _auth_info_request_received_cb(int context_id, autofill_view_info_h vi_h, void *user_data)
    {
        char *view_id = NULL;
        char *app_id = NULL;

        /* Get application ID and view ID sent the request of authentication information */
        autofill_view_info_get_app_id(vi_h, &app_id);
        autofill_view_info_get_view_id(vi_h, &view_id);

        autofill_view_info_foreach_item(vi_h, __view_info_item_cb, NULL);

        /* Do the action to certificate to use a method such as biometrics or entering password */

        send_auth_info(context_id);

        if (app_id)
            free(app_id);

        if (view_id)
            free(view_id);
    }

    bool service_app_create(void *data)
    {
        autofill_service_initialize();

        ...

        autofill_service_set_auth_info_requested_cb(_auth_info_request_received_cb, NULL);

        ...

        return true;
    }
    ```

2. Send the result whether the autofill data is present or not and the authentication information with the `autofill_service_send_auth_info()` function:

    ```c
    static void send_auth_info(int context_id, const char *app_id, const char *view_id)
    {
        /* Create authentication information */
        autofill_auth_info_h auth_info;
        autofill_auth_info_create(&auth_info);
        autofill_auth_info_set_app_id(auth_info, app_id);
        autofill_auth_info_set_view_id(auth_info, view_id);

        autofill_auth_info_set_autofill_data_present(auth_info, true);
        autofill_auth_info_set_authentication_needed(auth_info, true);
        autofill_auth_info_set_service_name(auth_info, "Your service name");
        autofill_auth_info_set_service_message(auth_info, "Service message");
        autofill_auth_info_set_service_logo_image_path(auth_info, LOGO_PATH);

        /* Send authentication information */
        autofill_service_send_auth_info(context_id, auth_info);

        autofill_auth_info_destroy(auth_info);
    }
    ```

## Receive Fill Request and Send Fill Response

1. To receive the fill request, create a callback function using the `autofill_service_set_fill_requested_cb()` function and send the fill response with the `autofill_service_send_fill_response()` function:

   > **Note**
   >
   > Autofill Service can have more than one autofill response for the view ID to be requested.
   > To support this case, create autofill data group using the `autofill_fill_response_group_create()` function and fill the data in the each autofill response group.
   > The following example code shows how to provide multiple autofill response data to have two autofill response to be consisted of user ID and user password:

    ```c
    static void _fill_request_received_cb(int context_id, autofill_view_info_h vi_h, void *user_data)
    {
        char *app_id = NULL;
        char *view_id = NULL;
        autofill_fill_response_group_h res_group_h[2];
        autofill_fill_response_item_h res_it_h[2];

        /* Get application ID and view ID sent the request of authentication information */
        autofill_view_info_get_app_id(vi_h, &app_id);
        autofill_view_info_get_view_id(vi_h, &view_id);
        dlog_print(DLOG_INFO, LOG_TAG, "app id : %s, view id : %s", app_id, view_id);

        /* Retrieve the stored user information */

        /* Create fill response */
        autofill_fill_response_h fill_response_h;
        autofill_fill_response_create(&fill_response_h);
        autofill_fill_response_set_app_id(fill_response_h, app_id);
        autofill_fill_response_set_view_id(fill_response_h, view_id);

        if (app_id)
            free(app_id);

        if (view_id)
            free(view_id);

        /* group 1 */
        autofill_fill_response_group_create(&res_group_h[0]);

        /* item 1 */
        autofill_fill_response_item_create(&res_it_h[0]);
        autofill_fill_response_item_set_id(res_it_h[0], "id");
        autofill_fill_response_item_set_presentation_text(res_it_h[0], "tester1");
        autofill_fill_response_item_set_value(res_it_h[0], "tester1");

        /* Add item 1 in group 1 */
        autofill_fill_response_group_add_item(res_group_h[0], res_it_h[0]);

        /* item 2 */
        autofill_fill_response_item_create(&res_it_h[1]);
        autofill_fill_response_item_set_id(res_it_h[1], "password");

        /* Use another presentation text due to sensitive data */
        autofill_fill_response_item_set_presentation_text(res_it_h[1], "tester1's Password");
        autofill_fill_response_item_set_value(res_it_h[1], "testerpw1");

        /* Add item 2 in group 1 */
        autofill_fill_response_group_add_item(res_group_h[0], res_it_h[1]);

        autofill_fill_response_item_destroy(res_it_h[0]);
        autofill_fill_response_item_destroy(res_it_h[1]);

        /* Add group 1 in fill response */
        autofill_fill_response_add_group(fill_response_h, res_group_h[0]);

        autofill_fill_response_group_destroy(res_group_h[0]);

        /* group 2 */
        autofill_fill_response_group_create(&res_group_h[1]);

        /* item 1 */
        autofill_fill_response_item_create(&res_it_h[0]);
        autofill_fill_response_item_set_id(res_it_h[0], "id");
        autofill_fill_response_item_set_presentation_text(res_it_h[0], "tester2");
        autofill_fill_response_item_set_value(res_it_h[0], "tester2");

        /* Add item 1 in group 2 */
        autofill_fill_response_group_add_item(res_group_h[1], res_it_h[0]);

        /* item 2 */
        autofill_fill_response_item_create(&res_it_h[1]);
        autofill_fill_response_item_set_id(res_it_h[1], "password");

        /* Use another presentation text due to sensitive data */
        autofill_fill_response_item_set_presentation_text(res_it_h[1], "tester2's Password");
        autofill_fill_response_item_set_value(res_it_h[1], "testerpw2");

        /* Add item 2 in group 2 */
        autofill_fill_response_group_add_item(res_group_h[1], res_it_h[1]);

        autofill_fill_response_item_destroy(res_it_h[0]);
        autofill_fill_response_item_destroy(res_it_h[1]);

        autofill_fill_response_add_group(fill_response_h, res_group_h[1]);

        autofill_fill_response_group_destroy(res_group_h[1]);

        /* Send fill response */
        autofill_service_send_fill_response(context_id, fill_response_h);

        autofill_fill_response_destroy(fill_response_h);
    }

    bool service_app_create(void *data)
    {
        autofill_service_initialize();

        ...

        autofill_service_set_fill_requested_cb(_fill_request_received_cb, NULL);

        ...

        return true;
    }
    ```

## Receive Request of Saving Autofill Data

1. To receive the request of saving Autofill data, create the callback function using the `void _commit_received_cb()` function:

    ```c
    static void _commit_received_cb(int context_id, autofill_save_view_info_h vi_h, void *user_data)
    {
        char *view_id = NULL;
        autofill_save_view_info_get_view_id(vi_h, &view_id);
        dlog_print(DLOG_INFO, LOG_TAG, "view id : %s", view_id);

        autofill_save_view_info_foreach_item(vi_h, __save_item_cb, NULL);

        if (view_id)
            free(view_id);
    }

    bool service_app_create(void *data)
    {
        autofill_service_initialize();

        ...
        autofill_service_set_commited_cb(_commit_received_cb, NULL);
        ...

        return true;
    }
    ```

2. Store the autofill data received by the callback, in a secure storage:

    ```c
    static bool __save_item_cb(autofill_save_item_h it_h, void *user_data)
    {
        char *id = NULL;
        char *label = NULL;
        char *value = NULL;
        autofill_hint_e autofill_hint;
        bool sensitive_data;

        autofill_save_item_get_id(it_h, &id);
        dlog_print(DLOG_INFO, LOG_TAG, "id : %s", id);

        autofill_save_item_get_label(it_h, &label);
        dlog_print(DLOG_INFO, LOG_TAG, "label : %s", label);

        autofill_save_item_get_value(it_h, &value);
        dlog_print(DLOG_INFO, LOG_TAG, "value : %s", value);

        autofill_save_item_get_autofill_hint(it_h, &autofill_hint);
        dlog_print(DLOG_INFO, LOG_TAG, "autofill hint : %d", autofill_hint);

        autofill_save_item_get_sensitive_data(it_h, &sensitive_data);
        dlog_print(DLOG_INFO, LOG_TAG, "sensitive data : %d", sensitive_data);

        /* Store the autofill data in your secure storage */

        free(id);
        free(label);
        free(value);

        return true;
    }
    ```

## Release Resources

After you have finished working with the Autofill Service library, deinitialize the Autofill Service:

   ```c
   void service_app_terminate(void *data)
   {
       autofill_service_deinitialize();
   }
   ```

## Related Information

- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable