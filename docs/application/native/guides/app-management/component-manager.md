# Component Manager

Component manager provides information about installed and running components.

The main features of Component Manager API include:

- Managing component context

  You can retrieve the running component context and operate on it. The `component_context_h` handle of Component Context API (in [mobile](../../api/mobile/latest/group__CAPI__COMPONENT__CONTEXT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__COMPONENT__CONTEXT__MODULE.html) applications) is related to the running components and can be used to [manage the component context](#manage_context).

- Managing component information

  The `component_info_h` handle of Component Information API (in [mobile](../../api/mobile/latest/group__CAPI__COMPONENT__INFO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__COMPONENT__INFO__MODULE.html) applications) is related to the available components that are installed but not necessarily running.

Iterator functions are used to travel through a list of components. `component_manager_foreach_component_context()` is used in running components and `component_manager_foreach_component_info()` is used in available components. Each function calls a callback function `component_manager_component_context_cb()` or `component_manager_component_info_cb()`, passing the handle for each component.

## Prerequisites

To enable your application to use the component management functionality:

1. To use Component Manager API (in [mobile](../../api/mobile/latest/group__CAPI__COMPONENT__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__COMPONENT__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
      <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
      <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
    </privileges>
    ```

2. To use the functions and data types of Component Manager API, include the `<component_manager.h>` header file in your application:

    ```
    #include <component_manager.h>
    ```
<a name="manage_context"></a>
## Managing Component Context

To get the running component context and its details, and to operate on the context:

1. Get the context of the currently running component with `component_manager_get_component_context()`. Use the obtained component ID and `component_context_h` handle of the component with received context as the parameter.

   To get a component's context, the component must be running.
   ```
   component_context_h component_context = NULL;
   int ret = component_manager_get_component_context(`Your Component ID`, &component_context);
   ```
   If it is executed correctly, the function returns `COMPONENT_MANAGER_ERROR_NONE` and `component_context` variable contains the handle to the defined component context.

2. Operate on the context:

   - Get the component ID from the context:

     ```
     char *component_id;
     ret = component_context_get_component_id(component_context, &component_id);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get component ID. error(%d)", ret);
        return;
     }
     ```

     When `component_id` is no longer needed, release it using `free()`.

   - Get the application ID from the context:

     ```
     char *app_id;
     ret = component_context_get_app_id(component_context, &app_id);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get application ID. error(%d)", ret);
         return;
     }
     ```

     When `app_id` is no longer needed, release it using `free()`.

   - Check whether the component with the given component context is terminated:

     ```
     bool terminated = false;

     ret = component_context_is_terminated(component_context, &terminated);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to check whether the component is terminated or not. error(%d)", ret);
         return;
     }

     if (terminated == true)
         dlog_print(DLOG_INFO, LOG_TAG, "The component is terminated");
     else
         dlog_print(DLOG_INFO, LOG_TAG, "The component is not terminated");
     ```

   - Clone the given context handle:

     ```
     component_context_h component_context_cloned = NULL;

     ret = component_context_clone(&component_context_cloned, component_context);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to clone component context. error(%d)", ret);
         return;
     }
     ```

   - Get the state of the component:

     ```
     component_state_e state;

     ret = component_context_get_component_state(component_context, &state);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get component state. error(%d)", ret);
         return;
     }

     dlog_print(DLOG_INFO, LOG_TAG, "Component State: %d", state);
     ```

   - Check whether the component is running as a sub component of the group:

     ```
     bool is_subcomponent = false;
     ret = component_context_is_subcomponent(component_context, &is_subcomponent);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to check whether the component is running as sub component of the group. error(%d)", ret);
         return;
     }
     ```
   - Resume the running component:

     ```
     ret = component_manager_resume_component(component_context);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to resume component. error(%d)", ret);
         return;
     }
     ```
     When the component is frame-component, it will appear on the screen.

   - Terminate the running component in the background:

     ```
     ret = component_manager_terminate_bg_component(component_context);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to terminate bg component. error(%d)", ret);
         return;
     }
     ```

3. When you no longer need the component context, call `component_context_destroy()` to remove the handle and release all resources to prevent memory leaks:

   ```
   ret = component_context_destroy(component_context);
   if (ret != COMPONENT_MANAGER_ERROR_NONE) {
       dlog_print(DLOG_ERROR, LOG_TAG, "Failed to destroy component context. error(%d)", ret);
       return;
   }
   ```

<a name="filter"></a>
## Managing Component Information

To get the installed information and its details, and to operate on the information:

1. Get the information of the currently-installed component with `component_manager_get_component_info()`. Use the obtained component ID and `component_info_h` handle of the component with received information as the parameter.

   To get a component's information, the component must be installed.
   ```
   component_info_h component_info = NULL;
   int ret = component_manager_get_component_info(`Your Component ID`, &component_info);
   if (ret != COMPONENT_MANAGER_ERROR_NONE) {
       dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get component info. error(%d)", ret);
       return;
   }
   ```

2. Operate on the information:

   - Get the component ID from the handle:

     ```
     char *component_id;
     ret = component_info_get_component_id(component_info, &component_id);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get component ID. error(%d)", ret);
         return;
     }
     ```
     When `component_id` is no longer needed, release it using `free()`.

   - Get the application ID from the handle:

     ```
     char *app_id;
     ret = component_info_get_app_id(component_info, &app_id);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get application ID. error(%d)", ret);
         return;
     }
     ```

     When `app_id` is no longer needed, release it using `free()`.

   - Get the component type from the handle:

     ```
     component_info_component_type_e type;
     ret = component_info_get_component_type(component_info, &type);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Falied to get component type. error(%d)", ret);
         return;
     }

     if (type == COMPONENT_INFO_COMPONENT_TYPE_FRAME)
         dlog_print(DLOG_INFO, LOG_TAG, "Component type: frame");
     else if (type == COMPONENT_INFO_COMPONENT_TYPE_SERVICE)
         dlog_print(DLOG_INFO, LOG_TAG, "Component type: service");
     ```

   - Get the icon path and verify whether the icon of the component appears on the home screen or not:

     ```
     char *icon;
     ret = component_info_get_icon(component_info, &icon);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get icon path. error(%d)", ret);
         return;
     }

     bool icon_display = false;
     ret = component_info_is_icon_display(component_info, &icon_display);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to check whether the icon is displayed or not. error(%d)", ret);
         return;
     }

     dlog_print(DLOG_INFO, LOG_TAG, "Icon path: %s", icon);
     dlog_print(DLOG_INFO, LOG_TAG, "Icon is displayed on the home screen: %s", icon_display ? "true" : "false");
     ```
     When `icon` is no longer needed, release it using `free()`.

   - Check whether the component should be managed by task-manager or not:

     ```
     bool managed = false;
     ret = component_info_is_managed_by_task_manager(component_info, &managed);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to check the component is managed by task-manager. error(%d)", ret);
         return;
     }

     dlog_print(DLOG_INFO, LOG_TAG, "Component is managed by task manager: %s", managed ? "true" : "false");
     ```

   - Get the label of the component from the handle:

     ```
     char *label;
     ret = component_info_get_label(component_info, &label);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get component label. error(%d)", ret);
         return;
     }

     dlog_print(DLOG_INFO, LOG_TAG, "Component Name: %s", label);
     ```
     When `label` is no longer needed, release it using `free()`.

   - Get the localized label with 'en-us' locale from the handle.

     ```
     char *localized_label;
     ret = component_info_get_localized_label(component_info, 'en-us', &localized_label);
     if (ret != COMPONENT_MANAGER_ERROR_NONE) {
         dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get localized label. error(%d)", ret);
         return;
     }

     dlog_print(DLOG_INFO, LOG_TAG, "Component Name: %s", localized_label);
     ```
     When `localized_label` is no longer needed, release it using `free()`.

3. When you no longer need the component information, call `component_info_destroy()` to remove the handle and release all resources to prevent memory leaks:

   ```
   ret = component_info_destroy(component_info);
   if (ret != COMPONENT_MANAGER_ERROR_NONE) {
       dlog_print(DLOG_ERROR, LOG_TAG, "Failed to destroy component info. error(%d)", ret);
       return;
   }
   ```

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable