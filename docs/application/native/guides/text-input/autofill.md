# Autofill

Autofill is a feature that allows you to fill out commonly-entered information such as email, account and address in a text input field. email, account and address in a text input field.
Using autofill functions, you can get the retrieve the data previously entered by the user and stored or request to store data in an autofill service.

The main features of the Autofill API include:

- [Requesting to get the presence of autofill data and autofill authentication information](#requesting-to-get-the-presence-of-autofill-data-and-autofill-authentication-information)

  You can get the autofill service information such as autofill service name, service message and service logo image to use `autofill_auth_info_request()`.
  You can get the presence of autofill data for each view in autofill service information to be received.

- [Retrieving the data previously entered by the user and stored in an autofill service](#retrieving-the-data-previously-entered-by-the-user-and-stored-in-an-autofill-service)

  Use the `autofill_fill_request()` function to retrieve the data previously entered by the user and stored in an autofill service

- [Requesting to store the data entered by the user in autofill service](#requesting-to-store-the-data-entered-by-the-user-in-autofill-service)

  Use the `autofill_commit()` function to store the data entered by the user in autofill service

## Prerequisites

1. Configure autofill service:

   Set autofill service in Settings > Language and input > Input Assistance > Autofill setting.
   In some environment, the autofill service can be designated according to the system configuration.

2. To use the autofill API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__AUTOFILL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__AUTOFILL__MODULE.html) applications), include the `<autofill.h>` header file in your application:

   ```c
   #include <autofill.h>
   ```

3. To use the autofill library, create an autofill handle:

   The autofill handle is used in other autofill functions as a parameter.

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

4. When you no longer need the autofill library, destroy the autofill handle using the `autofill_destroy()` function:

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
   > Do not use the `autofill_destroy()` function in a callback function.

5. After you create the autofill handle, connect the background autofill daemon with the `autofill_connect()` function:
   The function is asynchronous and you can get the result with callback function that registered as the second parameter of `autofill_connect()`.

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
   connect_autofill_daemon(autofill_h amh)
   {
       int ret;
       ret = autofill_connect(amh, connection_status_changed_cb, NULL);
       if (ret != AUTOFILL_ERROR_NONEt)
           /* Error handling */
   }
   ```

   You can use the autofill functions after receiving `AUTOFILL_CONNECTION_STATUS_CONNECTED` in `connection_status_changed_cb()`.

## Requesting to get the presence of autofill data and autofill authentication information

1. Create the callback function to get the presence of autofill data and autofill authentication information:

   You have to implement the UI to display the name, service message, and logo image of autofill service if the authentication is necessary.
   In addition, `autofill_auth_info_request()` to retrieve the data previously entered by the user and stored in an autofill service should be called when pressing UI to show autofill service information.

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

        if (authentication_needed)
        {
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

2. Create autofill data for each input field and view information to include several autofill data:

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

3. Request to get the authentication information:

    ```c
    /* Send request to get authentication information */
    ret = autofill_auth_info_request(ah, vi_h);
    if (ret != AUTOFILL_ERROR_NONE)
        /* Error handling */
    ```

4. When you no longer need the autofill view handle, call `autofill_view_info_destroy()` to release autofill view handle:

    ```c
    autofill_view_info_destroy(vi_h);
    ```

## Retrieving the data previously entered by the user and stored in an autofill service

To Retrieve the data previously entered by the user and stored in an autofill service:

1. Create the callback function to get the data previously entered by the user and stored in an autofill service:

   Autofill service can send more than one autofill response for the view ID to be requested.
   To support this case, `autofill_fill_response_foreach_group()` function is used to receive the multiple autofill response group. Each group has the autofill data for the requested view ID to be filled.

   The following example code shows how to receive multiple autofill response data to have 2 autofill response to be consisted of user ID and user password:

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

        if (id) {
            free(id);
        }

        if (value) {
            free(value);
        }

        if (presentation_text) {
            free(presentation_text);
        }

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

    /* Set callback function for receiving autofill fill response */
    autofill_fill_response_set_received_cb(ah, fill_response_received_cb, NULL);
    ```

2. Create autofill data for each input field and view information to include several autofill data:

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

3. Request to get the data previously entered by the user and stored in an autofill service:

    ```c
    /* Send request to get autofill fill response */
    int ret = autofill_fill_request(ah, vi_h);
    if (ret != AUTOFILL_ERROR_NONE)
        /* Error handling */
    ```

4. When you no longer need the autofill view handle, call `autofill_view_info_destroy()` to release autofill view handle:

    ```c
    autofill_view_info_destroy(vi_h);
    ```

## Requesting to store the data entered by the user in autofill service

1. Create autofill data for each input field for saving:

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

2. Create autofill view data to include multiple autofill items:

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

3. Request to store the data in an autofill service using `autofill_commit()`:

    ```c
    int ret;

    /* Send request to save autofill data */
    ret = autofill_commit(ah, svi_h);
    if (ret != AUTOFILL_ERROR_NONE)
        /* Error handling */

    autofill_save_view_info_destroy(svi_h);
    ```

4. When you no longer need the autofill save view handle, call `autofill_view_info_destroy()` to release autofill save view handle:

    ```c
    autofill_save_view_info_destroy(vi_h);
    ```

## Related Information

* Dependencies
  - Tizen 5.5 and Higher
