# Component Manager


The component manager provides information about installed and running components.

The main features of the Component Manager API include:

- Managing the component context

  You can retrieve the running component context and operate on it. The `component_context_h` handle is related to the running components and can be used to [manage the component context](#manage_context).

  For more information on the functions that use the `component_context_h` handle, see the Component Context API (in [mobile](../../api/mobile/latest/group__CAPI__COMPONENT__CONTEXT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__COMPONENT__CONTEXT__MODULE.html) applications).

- Getting the component information

  The `component_info_h` handle is related to the available components (installed, but not necessarily running), see the Component Information API (in [mobile](../../api/mobile/latest/group__CAPI__COMPONENT__INFO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__COMPONENT__INFO__MODULE.html) applications).

Iterator functions are used to travel through a list of components. The `component_manager_foreach_component_context()` function is used in running components and the `component_manager_foreach_component_info()` function is used in available components. Each function calls a callback function (`component_manager_component_context_cb()` or `component_manager_component_info_cb()`), passing the handle for each component.


## Prerequisites

1. To use the functions and data types of the Component Manager API (in [mobile](../../api/mobile/latest/group__CAPI__COMPONENT__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__COMPONENT__MANAGER__MODULE.html) applications), the application has to request permission. Add the following privilege to the `tizen-manifest.xml` file:

```
<privileges>
  <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
  <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
</privileges>
```

2. Include the `<component_manager.h>` header file in your application:

```
#include <component_manager.h>
```
<a name="manage_context"></a>
## Managing the Component Context

To get the running component context and its details, and to operate on the context:

1. Get the context of the currently-running component with the `component_manager_get_component_context()` function. Its parameters are the ID of the component from which the context is being obtained, and the handle (`component_context_h`) to the component context which is filled with the received context.

   When an component is not running, it is impossible to get its context.
   ```
   component_context_h component_context = NULL;
   int ret = component_manager_get_component_context(`Your Component ID`, &component_context);
   ```
   If the function returns `COMPONENT_MANAGER_ERROR_NONE`, it has executed correctly and the `component_context` variable now contains the handle to the defined component context.

2. Operate on the context:

   - Get the component ID from the context:

     ```
     char *component_id;
     ret = component_context_get_component_id(component_context, &component_id);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
     	/* Error handling */
     ```
     
     When `component_id` is no longer needed, release it using the `free()` function.
     
   - Get the application ID from the context:
   
     ```
     char *app_id;
     ret = component_context_get_app_id(component_context, &app_id);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
     	/* Error handling */
     ```

     When `app_id` is no longer needed, release it using the `free()` function.

   - Check whether the component with the given component context is terminated:

     ```
     bool terminated = false;

     ret = component_context_is_terminated(component_context, &terminated);

     if (false == terminated)
         /* Application is running */
     else
         /* Application is terminated */
     ```

   - Clone the given context handle:

     ```
     component_context_h component_context_cloned = NULL;

     ret = component_context_clone(&component_context_cloned, component_context);
     ```

   - Get the state of the component:

     ```
     component_state_e state;

     ret = component_context_get_component_state(component_context, &state);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
         /* Error handling */
     
     if (state == COMPONENT_STATE_RESUMED)
         /* Component is visible */
     else
         /* Component is invisible */
     ```
     
   - Check whether the component is running as sub component of the group:
    
     ```
     bool is_subcomponent = false;
     ret = component_context_is_subcomponent(component_context, &is_subcomponent);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
         /* Error handling */
     ```
   - Resume the running component:
     
     ```
     ret = component_manager_resume_component(component_context);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
         /* Error handling */
     ```
     When the component is frame-component, it will be shown on the screen.
   
   - Terminate the running component in the background:

     ```
     ret = component_manager_terminate_bg_component(component_context);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
        /* Error handling */
     ```

3. When you no longer need the component context, call the `component_context_destroy()` function to remove the handle and release all resources to prevent memory leaks:

   ```
     ret = component_context_destroy(component_context);
     if (ret != COMPONENT_MANAGER_ERROR_NONE)
         /* Error handling */
   ```

<a name="filter"></a>
## Getting the Component Information

To get the installed information and its details, and to operate on the information:

1. Get the information of the currently-installed component with the `component_manager_get_component_info()` function. Its parameters are the ID of the component from which the information is being obtained, and the handle (`component_info_h`) to the component information which is filled with the received information. When a component is not installed, it is impossible to get its information.

   ```
   component_info_h component_info = NULL;
   int ret = component_manager_get_component_info(`Your Component ID`, &component_info);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
   ```

2. Operate on the information:
 - Get the component ID from the handle:

   ```
   char *component_id;
   ret = component_info_get_component_id(component_info, &component_id);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
   ```
   When `component_id` is no longer needed, release it using the `free()` function.
   
 - Get the application ID from the handle:
   
   ```
   char *app_id;
   ret = component_info_get_app_id(component_info, &app_id);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
   ```
   
   When `app_id` is no longer needed, release it using the `free()` function.
   
 - Get the component type from the handle:

   ```
   component_info_component_type_e type;
   ret = component_info_get_component_type(component_info, &type);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
   
   if (type == COMPONENT_INFO_COMPONENT_TYPE_FRAME)
       dlog_print(DLOG_INFO, LOG_TAG, "Component type: frame");
   else if (type == COMPONENT_INFO_COMPONENT_TYPE_SERVICE)
       dlog_print(DLOG_INFO, LOG_TAG, "Component type: service");
   ```
   
 - Get the icon path and check whether the icon of the component is displayed on the home screen or not:
   
   ```
   char *icon;
   ret = component_info_get_icon(component_info, &icon);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
       
   bool icon_display = false;
   ret = component_info_is_icon_display(component_info, &icon_display);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
   
   dlog_print(DLOG_INFO, LOG_TAG, "Icon path: %s", icon);
   dlog_print(DLOG_INFO, LOG_TAG, "Icon is displayed on the home screen: %s", icon_display ? "true" : "false");
   ```
   When `icon` is no longer needed, release it using the `free()` function.
   
 - Check whether the component should be managed by task-manager or not:
   
   ```
   bool managed = false;
   ret = component_info_is_managed_by_task_manager(component_info, &managed);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
       
   dlog_print(DLOG_INFO, LOG_TAG, "Component is managed by task manager: %s", managed ? "true" : "false");
   ```

 - Get the label of the component from the handle:
   
   ```
   char *label;
   ret = component_info_get_label(component_info, &label);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
       
   dlog_print(DLOG_INFO, LOG_TAG, "Component Name: %s", label);
   ```
   When `label` is no longer needed, release it using the `free()` function.
   
 - Get the localized label with 'en-us' locale from the handle.
   
   ```
   char *localized_label;
   ret = component_info_get_localized_label(component_info, 'en-us', &localized_label);
   if (ret != COMPONENT_MANAGER_ERROR_NONE)
       /* Error handling */
       
   dlog_print(DLOG_INFO, LOG_TAG, "Component Name: %s", localized_label);
   ```
   When `localized_label` is no longer needed, release it using the `free()` function.
   
3. When you no longer need the component information, call the `component_info_destroy()` function to remote the handle and release all resources to prevent memory leaks:

	```
    ret = component_info_destroy(component_info);
    if (ret != COMPONENT_MANAGER_ERROR_NONE)
        /* Error handling */
	```

## Related Information
- Dependencies
  - Tizen 5.5