# Application Manager


The application manager provides information about installed and running applications. It provides functions for obtaining the application name and absolute path to share files among all applications.

The main features of the Application Manager API include:

- Managing the application context

  You can retrieve the application context and operate on it. The `app_context_h` handle is related to the running applications and can be used to [manage the application context](#manage_context).

  For more information on the functions that use the `app_context_h` handle, see the Application Context API (in [mobile](../../api/mobile/latest/group__CAPI__APP__CONTEXT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__APP__CONTEXT__MODULE.html) applications).

- Getting information on filtered applications

  The `app_info_h` handle is related to the available applications (installed, but not necessarily running). To [retrieve information on applications through a filter](#filter), you can also use the `app_info_filter_h` handle.

  For more information on the functions that use the `app_info_h` and `app_info_filter_h` handles, see the Application Information API (in [mobile](../../api/mobile/latest/group__CAPI__APP__INFO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__APP__INFO__MODULE.html) applications).

Iterator functions are used to travel through a list of applications. The `app_manager_foreach_app_context()` function is used in running applications and the `app_manager_foreach_app_info()` function is used in available applications. Each function calls a callback function (`app_manager_app_context_cb()` or `app_manager_app_info_cb()`), passing the handle for each application.

## Prerequisites

To use the functions and data types of the Application Manager API (in [mobile](../../api/mobile/latest/group__CAPI__APPLICATION__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__APPLICATION__MANAGER__MODULE.html) applications), include the `<app_manager.h>` header file in your application:

```
#include <app_manager.h>
```
<a name="manage_context"></a>
## Managing the Application Context

To get the running application context and its details, and to operate on the context:

1. Get the context of the currently-running application with the `app_manager_get_app_context()` function. Its parameters are the ID of the application from which the context is being obtained, and the handle (`app_context_h*`) to the application context which is filled with the received context.

   When an application is not running, it is impossible to get its context.
   ```
   app_context_h app_context = NULL;
   int ret = app_manager_get_app_context(Your App ID, &app_context);
   ```
   If the function returns `APP_MANAGER_ERROR_NONE`, it has executed correctly and the `app_context` variable now contains the handle to the defined application context.

2. Operate on the context:

   - Get the application ID and application process ID from the context:

     ```
     char *app_id;
     int pid = 0;

     ret = app_context_get_app_id(app_context, &app_id);
     ret = app_context_get_pid(app_context, &pid);
     ```

     When `app_id` is no longer needed, release it using the `free()` function.

   - Check whether the application with the given application context is terminated:

     ```
     bool terminated = false;

     ret = app_context_is_terminated(app_context, &terminated);

     if (false == terminated)
         /* Application is running */
     else
         /* Application is terminated */
     ```

   - Clone the given context handle:

     ```
     app_context_h app_context_cloned = NULL;

     ret = app_context_clone(&app_context_cloned, app_context);
     ```

   - Check whether 2 contexts are equal:

     ```
     bool equal = false;

     ret = app_context_is_equal(app_context, app_context_cloned, &equal);

     if (equal)
         /* Contexts are equal */
     else
         /* Contexts are not equal */
     ```

3. When you no longer need the application context, call the `app_context_destroy()` function to remove the handle and release all resources to prevent memory leaks:

   ```
   if (app_context) {
       ret = app_context_destroy(app_context);
       if (APP_MANAGER_ERROR_NONE != ret)
           /* Error handling */

           app_context = NULL;
   }
   ```

<a name="filter"></a>
## Getting Information on Filtered Applications

To get information on filtered applications:

1. Create the `app_info_filter_h` handle using the `app_info_filter_create()` function:
   ```
   app_info_filter_h app_info_filter = NULL;
   int ret = app_info_filter_create(&app_info_filter);
   ```

2. Add filter rules:

   ```
   ret = app_info_filter_add_string(app_info_filter, PACKAGE_INFO_PROP_APP_TYPE, "capp");
   ```

3. Call the `app_info_filter_foreach_appinfo()` function and use its callback to retrieve all filtered applications and print their information:

	```
    bool
    filter_cb(app_info_filter_h app_info, void *user_data)
    {
        int ret;

        char *app_id = NULL;

        if (app_info_get_app_id(app_info, &app_id))
            return false;

        dlog_print(DLOG_INFO, TAG, "app_id \t= [%s]\n", app_id);

        free(app_id);

        return true;
    }

    ret = app_info_filter_foreach_appinfo(filter_cb, NULL);
    if (ret != APP_MANAGER_ERROR_NONE)
        dlog_print(DLOG_ERROR, TAG, "foreach_app_info_filter error: %d", ret);
	```

4. When you no longer need the filter, call the `app_info_filter_destroy()` function to remove the handle and release all resources:
	```
    if (app_info_filter_h) {
        ret = app_info_filter_destroy(app_info_filter_h);
        if (APP_MANAGER_ERROR_NONE != ret)
            /* Error handling */

            app_info_filter_h = NULL;
    }
    ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
