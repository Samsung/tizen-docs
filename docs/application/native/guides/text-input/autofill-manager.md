# Autofill Manager

Tizen autofill framework allows more than one or more autofill services to be installed in a Tizen device. Autofill manager is a module for managing the installed autofill services. Application developers can use autofill manager to get the current autofill service or change the autofill service.

The main features of the Autofill Manager API include:

- [Getting the installed autofill service list](#getting-the-installed-autofill-service-list)

  Use the `autofill_manager_foreach_autofill_service()` function to get the installed autofill service list in your device.
  As a result, the `autofill_manager_autofill_service_cb()` callback function is invoked and you can get the installed autofill services.

- [Getting the current autofill service](#getting-the-current-autofill-service)

  Use the `autofill_manager_get_autofill_service()` function to get the current autofill service.

- [Setting the autofill service](#setting-the-autofill-service)

  Use the `autofill_manager_set_autofill_service()` function to set the autofill service.

## Prerequisites

1. To use the Autofill Manager API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__AUTOFILL__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__AUTOFILL__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```xml
   <privileges>
      <privilege>http://tizen.org/privilege/autofillmanager</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Autofill Manager API, include the `<autofill_manager.h>` header file in your application:

    ```c
    #include <autofill_manager.h>
    ```

3. To use the Autofill manager library, create an autofill manager handle.

   The autofill manager handle is used in other autofill manager functions as a parameter.

   ```c
   void
   create_autofill_manager_handle()
   {
       autofill_manager_h amh;
       int ret;
       ret = autofill_manager_create(&amh);
       if (ret != AUTOFILL_ERROR_NONE)
           /* Error handling */
   }
   ```

4. When you no longer need the autofill manager library, destroy the autofill manager handle using the `autofill_manager_destroy()` function:

   ```c
   void
   destroy_autofill_manager_handle(autofill_manager_h amh)
   {
       int ret;

       ret = autofill_manager_destroy(amh);
       if (ret != AUTOFILL_ERROR_NONE)
           /* Error handling */
   }
   ```

   > **Note**
   >
   > Do not use the `autofill_manager_destroy()` function in a callback function.

5. After you create the autofill manager handle, connect the background autofill daemon with the `autofill_manager_connect()` function.
   The function is asynchronous and you can get the result with callback function that registered as the second parameter of `autofill_manager_connect()`.

   ```c
   static void manager_connection_status_changed_cb(autofill_manager_h amh, autofill_manager_connection_status_e status, void *user_data)
   {
       switch (status) {
           case AUTOFILL_MANAGER_CONNECTION_STATUS_CONNECTED:
               dlog_print(DLOG_INFO, LOG_TAG, "connected");
               break;
           case AUTOFILL_MANAGER_CONNECTION_STATUS_DISCONNECTED:
               dlog_print(DLOG_INFO, LOG_TAG, "disconnected");
               break;
           case AUTOFILL_MANAGER_CONNECTION_STATUS_REJECTED:
               dlog_print(DLOG_INFO, LOG_TAG, "rejected");
               break;
           default:
               break;
   }

   void
   connect_autofill_daemon(autofill_manager_h amh)
   {
       int ret;
       ret = autofill_manager_connect(amh, manager_connection_status_changed_cb, NULL);
       if (ret != AUTOFILL_ERROR_NONE)
           /* Error handling */
   }
   ```

   You can use the autofill manager functions after receiving `AUTOFILL_MANAGER_CONNECTION_STATUS_CONNECTED` in `manager_connection_status_changed_cb()`.

## Getting the installed autofill service list

To get the installed autofill service list:

1. Create the `autofill_service_info_cb()` callback function, which is invoked for each installed autofill service application and is used to access autofill service information:

```c
#include <app_manager.h>

static bool autofill_service_info_cb(const char* app_id, void* user_data)
{
    app_info_h app_h;
    char *label = NULL;

    app_info_create(app_id, &app_h);
    app_info_get_label(app_h, &label);

    dlog_print(DLOG_INFO, LOG_TAG, "app id : %s, label : %s", app_id, label);

    if (label)
        free(label);

    app_info_destroy(app_h);

    return true;
}
```

2. Use the `autofill_manager_foreach_autofill_service()` function to get the installed autofill service by invoking a callback function for each installed autofill service application:

```c
    ret = autofill_manager_foreach_autofill_service(amh, autofill_service_info_cb, NULL);
    if (AUTOFILL_ERROR_NONE != ret)
        /* Error handling */
```

## Getting the current autofill service

To get the application ID of the current used autofill service, use the `autofill_manager_get_autofill_service()` function.

```c
void get_autofill_service(autofill_manager_h amh)
{
    char *active_autofill_service_app_id = NULL;
    int ret = autofill_manager_get_autofill_service(g_amh, &active_autofill_service_app_id);
    if (AUTOFILL_ERROR_NONE == ret) {
        dlog_print(DLOG_INFO, LOG_TAG, "app id : %s", active_autofill_service_app_id);
        if (active_autofill_service_app_id) {
            free(active_autofill_service_app_id);
        }
    }
}
```

## Setting the autofill service

To change autofill service as the other autofill service, use the `autofill_manager_set_autofill_service()` function.

```c
void set_autofill_service(autofill_manager_h amh, const char *autofill_service_app_id)
{
    dlog_print(DLOG_INFO, LOG_TAG, "index : %d", index);

    int ret = autofill_manager_set_autofill_service(amh, autofill_service_app_id);
    if (ret != AUTOFILL_ERROR_NONE)
           /* Error handling */
}
```

## Related Information

* Dependencies
  - Tizen 5.5 and Higher
