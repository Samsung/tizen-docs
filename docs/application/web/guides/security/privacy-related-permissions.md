# Privacy-related Permissions

You can check current permissions for privacy-related privileges and request user permission to use specified privileges.

This feature is supported in mobile and wearable applications only.

Before Tizen 4.0, the pop-up requesting the user's consent to use privacy-related privileges was triggered by first access to protected resources or functionality. Since Tizen 4.0, you can decide the moment in the application life-cycle when permissions are granted. It can be at the application startup, or at the moment when some additional functionality is to be used. For example, a notepad application where the user can enter both text notes and photographs does not automatically require camera access in order to be used (maybe the user only wants to add text notes). Optimally, the application requests the user to grant camera access permission only when the user needs the camera.

The main features of the Privacy Privilege API include:

-   Checking privilege status

    You must [determine the current status](#requesting) of a privacy-related privilege during the application runtime. This allows the application to make sure that the user has granted permission to use the needed privileges.

- Requesting privileges

    If a required permission is missing, you can [request the user to grant it](#requesting) to be able to use privileged features.

For a list of privacy-related privileges, see [Security and API Privileges](../../tutorials/sec-privileges.md).


<a name="requesting"></a>
## Requesting Permissions

To check whether an application has permission to use a privilege, and to request permission if required:

1.  To check whether an application has permission to use a particular privilege, use the `checkPermission()` method:

    ```
    var cameraPrivilege = "http://tizen.org/privilege/camera";
    var result = tizen.ppm.checkPermission(cameraPrivilege);
    ```

    The result of the call is returned as a value of the `PermissionType` enumeration (in [mobile](../../api/latest/device_api/mobile/tizen/ppm.html#PermissionType) and [wearable](../../api/latest/device_api/wearable/tizen/ppm.html#PermissionType) applications).

2. React to the permission check appropriately:
    - If the result value is `PPM_ALLOW`, the application is allowed to perform operations related to the privilege. For example, the application can enable additional UI elements or functionalities.

      ```
      switch (result) {
	      case "PPM_ALLOW":
		      /* Update UI and start accessing protected functionality */
		      break;
      ```

    - If the result value is `PPM_DENY`, the application is not allowed to perform operations related to the privilege. Any attempt to use such functionality without the user's consent fails. Usually, this means that invoking any API method that involves the privilege results in an error.

      ```
	      case "PPM_DENY":
		      /* Show a message and terminate the application */
		      break;
      ```

    - If the result value is `PPM_ASK`, the application must request permission from the user with the `requestPermission()` method, which displays a dialog box. When the user makes a decision, a callback defined as the second parameter is invoked.

      The dialog box asking for user permission is shown only if the `requestPermission()` method does not throw an exception.

      ```
	      case "PPM_ASK":
		      /* Request permission */
		      break;
      }
      ```

3. If you need to request user permission, handle the user decision within the `PermissionSuccessCallback` callback used in the `requestPermission()` method.

    The user decision is returned in the first parameter of the callback as a value of the `PermissionRequestResult` enumeration (in [mobile](../../api/latest/device_api/mobile/tizen/ppm.html#PermissionRequestResult) and [wearable](../../api/latest/device_api/wearable/tizen/ppm.html#PermissionRequestResult) applications). The second parameter contains the permission that is being requested.

    ```
    /* Define PermissionSuccessCallback */
    function permissionSuccess(result, privilege)
    {
        console.log("User's action for privilege " + privilege + " was to: " + result);
    }

    /* Define ErrorCallback */
    function errorCallback(response)
    {
        console.log("The following error occurred: " + response.name);
    }

    var cameraPrivilege = "http://tizen.org/privilege/camera";
    tizen.ppm.requestPermission(cameraPrivilege, permissionSuccess, errorCallback);
    ```

    - If the user decision is `PPM_ALLOW_FOREVER` or `PPM_DENY_FOREVER`, the decision is definitive and the application can react appropriately. It can finish its execution (if denied permission) or start to use protected APIs (if granted permission).
    - If the user decision is `PPM_DENY_ONCE`, the decision is not definitive. In this case, access to protected functionality is still prohibited. This decision can be interpreted as a cancel action on behalf of the user, indicating that the user is not sure what the purpose of the request is. Therefore, consider providing some additional information to explain why the permission is required.

    If the decision is definitive, any subsequent `requestPermission()` calls result in an immediate response with an appropriate result: `PPM_ALLOW_FOREVER` or `PPM_DENY_FOREVER`. However, the user can change the status of privacy-related privileges later by modifying the privacy settings on the device. For this reason, the application must always check the status of privacy-related privileges before using protected functionality.

> **Note**  
> Since the privileges are grouped, the user's decision regarding 1 privilege applies to the whole group of related privileges. For example, if the user has granted permission to use the `http://tizen.org/privilege/account.read` privilege, permission is automatically granted to the `http://tizen.org/privilege/account.write` privilege also. Be aware that both privileges need to be declared in the application manifest file. If you declare only 1 of them, the above rule does not apply.

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
