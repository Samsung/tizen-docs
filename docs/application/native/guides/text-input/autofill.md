# Autofill

Autofill is a feature that allows you to fill commonly entered information automatically, such as email, account, and address in a text input field.
The Autofill functions is used to retrieve previously entered data by the user or request to store data in an Autofill service.

The main features of the Autofill API include:

- Autofill Data and Autofill Authentication Information

  You can request to [get the autofill service information](#autofill-data-and-autofill-authentication-information), such as Autofill service name, service message, and service logo image. You can get the existing Autofill data for each view in the Autofill service information received.

- Data Entered and Stored in Autofill Service

  You can [retrieve the data](#data-entered-and-stored-in-autofill-service) that was stored in the Autofill service.

- Save Autofill Data

  You can [store](#save-autofill-data) the data entered by the user in an Autofill service.

## Prerequisites

1. To configure the Autofill Service:

   Set Autofill Service in the Setting Application from **Settings > Language and input > Input Assistance > Autofill service**.
   In some other environments, the Autofill Service can be found within the system configuration.

2. To use the Autofill API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__AUTOFILL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__AUTOFILL__MODULE.html) applications), include the `<autofill.h>` header file in your application:

   ```c
   #include <autofill.h>
   ```

## Initialization

To use the Autofill library:

1. Create an Autofill handle:

   The Autofill handle is used in other Autofill functions as a parameter:

   ```c
   void
   create_autofill_handle()
   {
       autofill_h ah;
       int ret;
       ret = autofill_create(&ah);
       if (ret != AUTOFILL_ERROR_NONE)
           /* Error handling */
   }
   ```

2. After you create the Autofill handle, connect the background Autofill daemon with the `autofill_connect()` function.
   The function is asynchronous and you can get the result with callback function that registered as the second parameter of `autofill_connect()`:

   ```c
   static void connection_status_changed_cb(autofill_h ah, autofill_connection_status_e status, void *user_data)
   {
       switch (status) {
       case AUTOFILL_CONNECTION_STATUS_CONNECTED:
           dlog_print(DLOG_INFO, LOG_TAG, "connected");
           break;
       case AUTOFILL_CONNECTION_STATUS_DISCONNECTED:
           dlog_print(DLOG_INFO, LOG_TAG, "disconnected");
           break;
       case AUTOFILL_CONNECTION_STATUS_REJECTED:
           dlog_print(DLOG_INFO, LOG_TAG, "rejected");
           break;
       default:
           break;
   }

   void
   connect_autofill_daemon(autofill_h ah)
   {
       int ret;
       ret = autofill_connect(ah, connection_status_changed_cb, NULL);
       if (ret != AUTOFILL_ERROR_NONEt)
           /* Error handling */
   }
   ```

   You can use the Autofill functions after receiving the status from AUTOFILL_CONNECTION_STATUS_CONNECTED in the `connection_status_changed_cb()` function.

## Autofill Data and Autofill Authentication Information

To get the presence of Autofill data and Autofill authentication information:

1. Create a callback function using the `auth_info_received_cb()` function:

   You need to implement the UI elements to display the name, service message, logo, and image of Autofill service, in case the authentication is required:

    ```c
    static void
    auth_info_received_cb(autofill_h ah, autofill_auth_info_h auth_info_h, void *data)
    {
        bool autofill_data_present = false;
        bool authentication_needed = false;
        char *service_name = NULL;
        char *service_message = NULL;
        char *service_logo_image_path = NULL;
        char *view_id = NULL;

        autofill_auth_info_get_view_id(auth_info_h, &view_id);
        autofill_auth_info_get_autofill_data_present(auth_info_h, &autofill_data_present);
        autofill_auth_info_get_authentication_needed(auth_info_h, &authentication_needed);

        dlog_print(DLOG_INFO, LOG_TAG, "view id : %s, exist autofill data : %d, need authentication : %d", view_id, autofill_data_present, authentication_needed);

        if (view_id)
            free(view_id);

        if (!autofill_data_present)
            return;

        if (authentication_needed) {
            autofill_auth_info_get_service_name(auth_info_h, &service_name);
            autofill_auth_info_get_service_message(auth_info_h, &service_message);
            autofill_auth_info_get_service_logo_image_path(auth_info_h, &service_logo_image_path);

            dlog_print(DLOG_INFO, LOG_TAG, "service name : %s, logo path : %s, message : '%s'", service_name, service_logo_image_path, service_message);

            /* create authentication popup */
            ...

            if (service_message)
                free(service_message);

            if (service_name)
                free(service_name);

            if (service_logo_image_path)
                free(service_logo_image_path);
        }
    }

    /* Set callback function for receiving authentication information */
    autofill_auth_info_set_received_cb(ah, auth_info_received_cb, NULL);
    ```

2. Create Autofill data for each input field and view information to include several Autofill data:

    ```c
    int ret;
    autofill_view_info_h vi_h;
    autofill_item_h ai_h;
    char *app_id = NULL;

    app_get_id(&app_id);

    /* create autofill item */
    autofill_item_create(&ai_h);
    autofill_item_set_autofill_hint(ai_h, AUTOFILL_HINT_ID);
    autofill_item_set_id(ai_h, "id");
    autofill_item_set_label(ai_h, "label");
    autofill_item_set_sensitive_data(ai_h, false);

    /* create autofill view info */
    autofill_view_info_create(&vi_h);
    autofill_view_info_set_app_id(vi_h, app_id);
    autofill_view_info_set_view_id(vi_h, "login");

    /* append autofill item in autofill view */
    autofill_view_info_add_item(vi_h, ai_h);

    if (app_id)
        free(app_id);
    ```

3. The function `autofill_auth_info_request()` must be called when pressing UI to show the Autofill service information. It retrieves the data previously entered by the user that is stored in an Autofill service related storage. Request with the `autofill_auth_info_request()` function, to get the authentication information:

    ```c
    /* Send request to get authentication information */
    ret = autofill_auth_info_request(ah, vi_h);
    if (ret != AUTOFILL_ERROR_NONE)
        /* Error handling */
    ```

## Data Entered and Stored in Autofill Service

1. To retrieve the data previously entered using the `fill_response_item_cb()` function, create the callback function:

   Autofill service can send more than one autofill response for the requested view ID.
   To support this case, the `autofill_fill_response_foreach_group()` function is used to receive the multiple autofill response group. Each group has the autofill data for the requested view ID to be filled.

   The following code snippet shows how to receive multiple Autofill response data to have two Autofill responses that consists of of user ID and user password in this case:

    ```c
    static bool fill_response_item_cb(autofill_fill_response_item_h item, void *user_data)
    {
        char *id = NULL;
        char *value = NULL;
        char *presentation_text = NULL;

        autofill_fill_response_item_get_id(item, &id);
        autofill_fill_response_item_get_presentation_text(item, &presentation_text);
        autofill_fill_response_item_get_value(item, &value);

        dlog_print(DLOG_INFO, LOG_TAG, "id : %s, value : %s, presentation text : %s", id, value, presentation_text);

        if (id)
            free(id);

        if (value)
            free(value);

        if (presentation_text)
            free(presentation_text);

        return true;
    }

    static bool fill_response_group_cb(autofill_fill_response_group_h group_h, void *user_data)
    {
        autofill_fill_response_group_foreach_item(group_h, fill_response_item_cb, group_h);

        return true;
    }

    static void
    fill_response_received_cb(autofill_h ah, autofill_fill_response_h fill_response, void *data)
    {
        /* get fill response group count */
        int count;
        autofill_fill_response_get_group_count(fill_response, &count);
        dlog_print(DLOG_INFO, LOG_TAG, "group count : %d", count);

        autofill_fill_response_foreach_group(fill_response, fill_response_group_cb, &count);
    }

    /* Set callback function for receiving fill response */
    autofill_fill_response_set_received_cb(ah, fill_response_received_cb, NULL);
    ```

2. To include several Autofill data, create Autofill data for each input field and view information:

    ```c
    autofill_view_info_h vi_h;
    autofill_item_h ai_id, ai_password;
    char *app_id = NULL;

    app_get_id(&app_id);

    /* create autofill item for entering an user ID */
    autofill_item_create(&ai_id);
    autofill_item_set_autofill_hint(ai_id, AUTOFILL_HINT_ID);
    autofill_item_set_id(ai_id, "id");
    autofill_item_set_label(ai_id, "Enter your ID");
    autofill_item_set_sensitive_data(ai_id, false);

    /* create autofill item for entering an user password */
    autofill_item_create(&ai_password);
    autofill_item_set_autofill_hint(ai_password, AUTOFILL_HINT_PASSWORD);
    autofill_item_set_id(ai_password, "password");
    autofill_item_set_label(ai_password, "Enter your password");
    autofill_item_set_sensitive_data(ai_password, true);

    /* create autofill view info */
    autofill_view_info_create(&vi_h);
    autofill_view_info_set_app_id(vi_h, app_id);
    autofill_view_info_set_view_id(vi_h, "login");

    autofill_view_info_add_item(vi_h, ai_id);
    autofill_view_info_add_item(vi_h, ai_password);
    ```

3. To get the data previously entered by the user and stored in an Autofill service, request using the `autofill_fill_request()` function:

    ```c
    /* Send request to get fill response */
    int ret = autofill_fill_request(ah, vi_h);
    if (ret != AUTOFILL_ERROR_NONE)
        /* Error handling */
    ```

## Save Autofill Data

To store entered data by the user in the Autofill service:

1. Create an Autofill data for each input fields, to save:

    ```c
    autofill_save_item_h si_h;

    /* create autofill item for saving */
    autofill_save_item_create(&si_h);
    autofill_save_item_set_autofill_hint(si_h, AUTOFILL_HINT_ID);
    autofill_save_item_set_id(si_h, "id");
    autofill_save_item_set_label(si_h, "Input your ID");
    autofill_save_item_set_sensitive_data(si_h, false);
    autofill_save_item_set_value(si_h, "myID");
    ```

2. Create an Autofill view data, to include multiple Autofill items:

    ```c
    char *app_id;

    /* create autofill save view info */
    app_get_id(&app_id);

    autofill_save_view_info_create(&svi_h);
    autofill_save_view_info_set_app_id(svi_h, app_id);
    autofill_save_view_info_set_view_id(svi_h, "login");

    /* append autofill save item in autofill save view */
    autofill_save_view_info_add_item(svi_h, si_h);

    if (app_id)
        free(app_id);
    ```

3. Request with the `autofill_commit()` function, to store the data in an Autofill service:

    ```c
    int ret;

    /* Send request to save autofill data */
    ret = autofill_commit(ah, svi_h);
    if (ret != AUTOFILL_ERROR_NONE)
        /* Error handling */

    autofill_save_view_info_destroy(svi_h);
    ```

## Release Resources

1. Incase, the Autofill view info handle is not needed in your application, you must destroy the Autofill view info handle using the `autofill_view_info_destroy()` function:

    ```c
    autofill_view_info_destroy(vi_h);
    ```

2. Incase, the Autofill save view handle is not needed in your application, you must destroy the Autofill save view handle using `autofill_save_view_info_destroy()` function:

    ```c
    autofill_save_view_info_destroy(vi_h);
    ```

3. After you have finished working with the Autofill library, destroy the the Autofill handle:

   ```c
   void
   destroy_autofill_handle(autofill_h ah)
   {
       int ret;

       ret = autofill_destroy(ah); /* ah is the autofill handle */
       if (ret != AUTOFILL_ERROR_NONEt)
           /* Error handling */
   }
   ```

   > **Note**
   >
   > It is not recommended to use the `autofill_destroy()` function in a callback function.

## Related Information

- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable