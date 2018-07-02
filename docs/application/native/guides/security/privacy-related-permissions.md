# Privacy-related Permissions


You can check current permissions for privacy-related privileges and request user permission to use specified privileges.

Before Tizen 4.0, the pop-up requesting the user's consent to use privacy-related privileges was triggered by first access to protected resources or functionality. Since Tizen 4.0, you can decide the moment in the application life-cycle when permissions are granted. It can be at the application startup, or at the moment when some additional functionality is to be used. For example, a notepad application where the user can enter both text notes and photographs does not automatically require camera access in order to be used (maybe the user only wants to add text notes). Optimally, the application requests the user to grant camera access permission only when the user needs the camera.

The main features of the Privacy Privilege Manager API include:

- Checking privilege status

  If the application declares privacy-related privileges in its manifest file, you must [determine the current status](#req) of a privacy-related privilege during the application runtime. This allows the application to make sure that the user has granted permission to use the needed privileges.

- Requesting privileges

  If a required permission is missing, you can [request the user to grant it](#req) to be able to use privileged features.

For a list of privacy-related privileges, see [Security and API Privileges](../../tutorials/details/sec-privileges.md).

## Prerequisites

To enable your application to use the privacy-related privileges functionality:

1. To use the functions and data types of the Privacy Privilege Manager API (in [mobile](../../api/mobile/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) applications), include the `<privacy_privilege_manager.h>` header file in your application:

    ```
    #include <privacy_privilege_manager.h>
    ```

 To ensure that a Privacy Privilege Manager function has been executed properly, make sure that the return value is equal to `PRIVACY_PRIVILEGE_MANAGER_ERROR_NONE`. If the function returns an error, handle it accordingly.

2. Call the Privacy Privilege Manager functions from the context of the application's main event loop.

   It means that the functions can be employed in any UI event callback (such as button callbacks, timer callbacks, handlers for system events, and application state change event callbacks). If you want to resolve privileges during application startup, call these functions from the resume event callback (`app_resume_cb()`).

   > **Note**
   >
   > The Privacy Privilege Manager functions are not thread-safe.

<a name="req"></a>
## Requesting Permissions

To check whether an application has permission to use a privilege, and to request permission if required:

1. To check whether an application has permission to use a particular privilege, use the `ppm_check_permission()` function:

    ```
    void
    app_check_and_request_permission()
    {
        ppm_check_result_e result;
        const char *privilege = "http://tizen.org/privilege/camera";

        int ret = ppm_check_permission(privilege, &result);
    ```

    The result of the call is stored in the variable passed as the second parameter (for available results, see the `ppm_check_result_e` enumeration in [mobile](../../api/mobile/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html#ga41f409d8b9d4c27d41b907bdb0975f0c) and [wearable](../../api/wearable/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html#ga41f409d8b9d4c27d41b907bdb0975f0c) applications).

2. React to the permission check appropriately:

   - If the result value is `PRIVACY_PRIVILEGE_MANAGER_CHECK_RESULT_ALLOW`, the application is allowed to perform operations related to the privilege. For example, the application can enable additional UI elements or functionalities.

     ```
         if (ret == PRIVACY_PRIVILEGE_MANAGER_ERROR_NONE) {
             switch (result) {
                 case PRIVACY_PRIVILEGE_MANAGER_CHECK_RESULT_ALLOW:
                     /* Update UI and start accessing protected functionality */
                     break;
     ```

   - If the result value is `PRIVACY_PRIVILEGE_MANAGER_CHECK_RESULT_DENY`, the application is not allowed to perform operations related to the privilege. Any attempt to use such functionality without the user's consent fails. Usually, this means that invoking any API function that involves the privilege results in an error.

     ```
                 case PRIVACY_PRIVILEGE_MANAGER_CHECK_RESULT_DENY:
                     /* Show a message and terminate the application */
                     break;
     ```

   - If the result value is `PRIVACY_PRIVILEGE_MANAGER_CHECK_RESULT_ASK`, the application must request permission from the user with the `ppm_request_permission()` function, which displays a dialog box. You can pass user data as the third parameter of the function, as a pointer to an application context instance. When the user makes a decision, a callback defined as the second parameter is invoked.

     The dialog box asking for user permission is shown only if the `ppm_request_permission()` function returns without an error.

     ```
                 case PRIVACY_PRIVILEGE_MANAGER_CHECK_RESULT_ASK:
                     ret = ppm_request_permission(privilege, app_request_response_cb, NULL);
                     /* Log and handle errors */
                     break;
             }
         }
         else {
             /* ret != PRIVACY_PRIVILEGE_MANAGER_ERROR_NONE */
             /* Handle errors */
         }
     }
     ```

3. If you need to request user permission, handle the user decision within the callback.

   The user decision is returned in the callback as a value of the `ppm_request_result_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html#ga0be419f8be0a398fd6e9af29f9c3e29b) and [wearable](../../api/wearable/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html#ga0be419f8be0a398fd6e9af29f9c3e29b) applications).

   ```
   void
   app_request_response_cb(ppm_call_cause_e cause, ppm_request_result_e result,
                                const char *privilege, void *user_data)
   {
       if (cause == PRIVACY_PRIVILEGE_MANAGER_CALL_CAUSE_ERROR) {
           /* Log and handle errors */

           return;
       }

       switch (result) {
           case PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_ALLOW_FOREVER:
               /* Update UI and start accessing protected functionality */
               break;
           case PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_DENY_FOREVER:
               /* Show a message and terminate the application */
               break;
           case PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_DENY_ONCE:
               /* Show a message with explanation */
               break;
       }
   }
   ```

   - If the user decision is `PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_ALLOW_FOREVER` or `PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_DENY_FOREVER`, the decision is definitive and the application can react appropriately. It can finish its execution (if denied permission) or start to use protected APIs (if granted permission).
   - If the user decision is `PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_DENY_ONCE`, the decision is not definitive. In this case, access to protected functionality is still prohibited. This decision can be interpreted as a cancel action on behalf of the user, indicating that the user is not sure what the purpose of the request is. Therefore, consider providing some additional information to explain why the permission is required.

   If the decision is definitive, any subsequent `ppm_request_permission()` calls result in an immediate response with an appropriate result: `PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_ALLOW_FOREVER` or `PRIVACY_PRIVILEGE_MANAGER_REQUEST_RESULT_DENY_FOREVER`. However, the user can change the status of privacy-related privileges later by modifying the privacy settings on the device. For this reason, the application must always check the status of privacy-related privileges before using protected functionality.

> **Note**
>
> Since the privileges are grouped, the user's decision regarding one privilege applies to the whole group of related privileges. For example, if the user has granted permission to use the `http://tizen.org/privilege/account.read` privilege, permission is automatically granted to the `http://tizen.org/privilege/account.write` privilege also. Be aware that both privileges need to be declared in the application manifest file. If you declare only one of them, the above rule does not apply.

## Related Information
- Dependencies
  - Tizen 2.3 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
