# Privacy-related Permissions

You can check current permissions for privacy-related privileges and request user permission to use specified privileges.

This feature is optional.

Before Tizen 4.0, the pop-up requesting the user's consent to use privacy-related privileges was triggered by first access to protected resources or functionality. Since Tizen 4.0, you can decide the moment in the application life-cycle when permissions are granted. It can be at the application startup, or at the moment when some additional functionality is to be used. For example, a notepad application where the user can enter both text notes and photographs does not automatically require camera access in order to be used (maybe the user only wants to add text notes). Optimally, the application requests the user to grant camera access permission only when the user needs the camera.

> [!NOTE]
> Since Tizen 8.0, all Privacy Privilege Manager APIs are deprecated for mobile and wearable profiles and will be removed without any alternative.

> [!NOTE]
> Since Tizen 10.1, the Privacy Privilege Manager API is available for TV profile. New permission types are also available for more granular control: session-based permissions and in-use permissions. These provide additional flexibility for managing user privacy.

The main features of the Privacy Privilege API include the following:

-   Checking privilege status

    You must [determine the current status](#requesting) of a privacy-related privilege during the application runtime. This allows the application to make sure that the user has granted permission to use the needed privileges.

- Requesting privileges

    If a required permission is missing, you can [request the user to grant it](#requesting) to be able to use privileged features.

For a list of privacy-related privileges, see [Security and API Privileges](../../tutorials/sec-privileges.md).

> [!NOTE]
> Since Tizen 5.5, if the caller application component type is UI application, then the pop-ups by `requestPermission()` and `requestPermissions()` are launched as `group mode` with the caller application.
> If the pop-up is terminated without full response, all the remaining requests that are not responded by the user will be interpreted as **Deny** action on behalf of the user. In this case, the app gets `PPM_DENY_ONCE` response to those permissions. The app can again request for those **automatically denied** permissions anytime it needs.
> Use `requestPermissions()` to request multiple privileges instead of calling `requestPermission()` multiple times.

<a name="requesting"></a>
## Request permissions

To verify whether an application has permission to use a privilege, and to request permission if required, follow these steps:

1.  To verify whether an application has permission to use a particular privilege, use the `checkPermission()` method:

    ```
    var cameraPrivilege = "http://tizen.org/privilege/camera";
    var result = tizen.ppm.checkPermission(cameraPrivilege);
    ```

    The result of the call is returned as a value of the `PermissionType` enumeration.

2. React to the permission check appropriately:
    - If the result value is `PPM_ALLOW`, the application is allowed to perform operations related to the privilege. For example, the application can enable additional UI elements or functionalities:

      ```
      switch (result) {
	      case "PPM_ALLOW":
		      /* Update UI and start accessing protected functionality */
		      break;
      ```

    - If the result value is `PPM_DENY`, the application is not allowed to perform operations related to the privilege. Any attempt to use such functionality without the user's consent fails. Usually, this means that invoking any API method that involves the privilege results in an error:

      ```
	      case "PPM_DENY":
		      /* Show a message and terminate the application */
		      break;
      ```

    - If the result value is `PPM_ASK`, the application must request permission from the user with the `requestPermission()` method, which displays a dialog box. When the user makes a decision, a callback defined as the second parameter is invoked.

      The dialog box asking for user permission is shown only if the `requestPermission()` method does not throw an exception:

      ```
	      case "PPM_ASK":
		      /* Request permission */
		      break;
      }
      ```

    - If the result value is `PPM_ALLOW_SESSION`, the application has permission to use the privilege for the current application session only. The permission will be reset when the application terminates:

      ```
      case "PPM_ALLOW_SESSION":
          /* Access protected functionality for current session only */
          break;
      ```

    - If the result value is `PPM_DENY_SESSION`, the application doesn't have permission to use the privilege for the current session. This is a temporary denial that resets when the application restarts:

      ```
      case "PPM_DENY_SESSION":
          /* Show a message - permission denied for this session */
          break;
      ```

    - If the result value is `PPM_ALLOW_IN_USE`, the application has permission to use the privilege only while it is in the foreground (being actively used by the user). When the application goes to the background, access to the protected functionality is restricted:

      ```
      case "PPM_ALLOW_IN_USE":
          /* Access protected functionality only while app is in foreground */
          break;
      ```

3. If you need to request user permission, handle the user decision within the `PermissionSuccessCallback` callback used in the `requestPermission()` method.

    The user decision is returned in the first parameter of the callback as a value of the `PermissionRequestResult` enumeration. The second parameter contains the permission that is being requested:

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
    - If the user decision is `PPM_ALLOW_SESSION`, the user granted permission for the current application session only. The permission will be reset when the application terminates.
    - If the user decision is `PPM_DENY_SESSION`, the user denied permission for the current application session. This denial is temporary and resets when the application restarts.
    - If the user decision is `PPM_ALLOW_IN_USE`, the user granted permission only when the application is being actively used (on top). When the application goes to the background, access to the protected functionality is restricted.

    If the decision is definitive (`PPM_ALLOW_FOREVER` or `PPM_DENY_FOREVER`), any subsequent `requestPermission()` calls result in an immediate response with an appropriate result. However, the user can change the status of privacy-related privileges later by modifying the privacy settings on the device. For this reason, the application must always check the status of privacy-related privileges before using protected functionality.

    The following example shows how to handle all possible permission request results:

    ```
    /* Define PermissionSuccessCallback */
    function permissionSuccess(result, privilege)
    {
        switch (result) {
            case "PPM_ALLOW_FOREVER":
                console.log("Permission granted permanently for " + privilege);
                break;
            case "PPM_DENY_FOREVER":
                console.log("Permission denied permanently for " + privilege);
                break;
            case "PPM_DENY_ONCE":
                console.log("Permission denied once for " + privilege);
                break;
            case "PPM_ALLOW_SESSION":
                console.log("Permission granted for session only for " + privilege);
                break;
            case "PPM_DENY_SESSION":
                console.log("Permission denied for session only for " + privilege);
                break;
            case "PPM_ALLOW_IN_USE":
                console.log("Permission granted in-use only for " + privilege);
                break;
        }
    }
    ```

4. Since Tizen 5.0 you can check and request multiple privacy privileges at once. To do that please use `checkPermissions` and `requestPermissions`.

> [!NOTE]
> Since the privileges are grouped, the user's decision regarding 1 privilege applies to the whole group of related privileges. For example, if the user has granted permission to use the `http://tizen.org/privilege/account.read` privilege, permission is automatically granted to the `http://tizen.org/privilege/account.write` privilege also. Be aware that both privileges need to be declared in the application manifest file. If you declare only 1 of them, the above rule does not apply.

## Related information
- Dependencies
  - Tizen 4.0 and Higher
  - Tizen 5.0 and Higher (for `checkPermissions()` and `requestPermissions()` methods)
  - Tizen 10.1 and Higher (for TV profile and session-based/in-use permission types: `PPM_ALLOW_SESSION`, `PPM_DENY_SESSION`, `PPM_ALLOW_IN_USE`)
