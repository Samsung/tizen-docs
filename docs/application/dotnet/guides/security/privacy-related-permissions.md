# Privacy-related Permissions


You can check current permissions for privacy-related privileges and request user permission to use specified privileges.

Before Tizen 4.0, the pop-up requesting the user's consent to use privacy-related privileges was triggered by first access to protected resources or functionality. Since Tizen 4.0, you can decide the moment in the application life-cycle when permissions are granted. It can be at the application startup, or at the moment when some additional functionality is to be used. For example, a notepad application where the user can enter both text notes and photographs does not automatically require camera access in order to be used (maybe the user only wants to add text notes). Optimally, the application requests the user to grant camera access permission only when the user needs the camera.

The main features of the `Tizen.Security.PrivacyPrivilegeManager` class include:

-   Checking privilege status

    If the application declares privacy-related privileges in its manifest file, you must [determine the current status](#requesting) of a privacy-related privilege during the application runtime. This allows the application to make sure that the user has granted permission to use the needed privileges.

-   Requesting privileges

    If a required permission is missing, you can [request the user to grant it](#requesting) to be able to use privileged features.

For a list of privacy-related privileges, see [Security and API Privileges](../../get-started/api-privileges/).

> [!NOTE]
> Since Tizen 5.5, if the caller application component type is UI application, then the pop-ups by `RequestPermission()` and `RequestPermissions()` are launched as `group mode` with the caller application.
> If the pop-up is terminated without full response, all the remaining requests that are not responded by the user will be interpreted as **Deny** action on behalf of the user. In this case, the app gets `RequestResult.DenyOnce` response to those permissions. The app can again request for those **automatically denied** permissions anytime it needs.
> Use `RequestPermissions()` to request multiple privileges instead of calling `RequestPermission()` multiple times.

## Prerequisites

To enable your application to use the privacy-related permissions functionality:

1.  To use the methods and properties of the [Tizen.Security](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.html) namespace, include it in your application:

    ```csharp
    using Tizen.Security;
    ```

2.  Call the `Tizen.Security.PrivacyPrivilegeManager` methods from the context of the application's main event loop.

    It means that the methods can be employed in any UI event handler (such as button click, timer event, system event, and application state change event). If you want to resolve privileges during application startup, call these methods from the Xamarin.Forms resume and start life-cycle methods (`Xamarin.Forms.Application.OnResume()` and `Xamarin.Forms.Application.OnStart()`).

    > [!NOTE]
    > The `Tizen.Security.PrivacyPrivilegeManager` class is not thread-safe.

<a name="requesting"></a>
## Requesting Permissions
To check whether an application has permission to use a privilege, and to request permission if required:

1.  To check whether an application has permission to use a particular privilege, use the `CheckPermission()` method of the [Tizen.Security.PrivacyPrivilegeManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.PrivacyPrivilegeManager.html) class:

    ```csharp
    const string cameraPrivilege = "http://tizen.org/privilege/camera";

    void CheckAndRequestCameraPermission()
    {
        try
        {
            CheckResult result = PrivacyPrivilegeManager.CheckPermission(cameraPrivilege);
    ```

    The result of the call is returned as a value of the [Tizen.Security.CheckResult](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.CheckResult.html) enumeration.

2.  React to the permission check appropriately:

    -   If the result value is `Allow`, the application is allowed to perform operations related to the privilege. For example, the application can enable additional UI elements or functionalities.

        ```csharp
                switch (result)
                {
                    case CheckResult.Allow:
                        /// Update UI and start accessing protected functionality
                        break;
        ```

    -   If the result value is `Deny`, the application is not allowed to perform operations related to the privilege. Any attempt to use such functionality without the user's consent fails. Usually, this means that invoking any method that involves the privilege results in an error.

        ```csharp
                    case CheckResult.Deny:
                        /// Show a message and terminate the application
                        break;
        ```

    -   If the result value is `Ask`, the application must request permission from the user with the `RequestPermission()` method, which displays a dialog box. When the user makes a decision, an event handler is invoked (the event handler must have been [previously registered](#handler)).

        The dialog box asking for user permission is shown only if the `RequestPermission()` method does not throw an exception.

        ```csharp
                    case CheckResult.Ask:
                        PrivacyPrivilegeManager.RequestPermission(cameraPrivilege);
                        break;
                }
        ```

    ```csharp
        }
        catch (Exception e)
        {
            /// Handle exception
        }
    }
    ```

3.  <a name="handler"></a>If you need to request user permission, handle the user decision within an event handler registered for the `ResponseFetched` event of the [Tizen.Security.PrivacyPrivilegeManager.ResponseContext](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.PrivacyPrivilegeManager.ResponseContext.html) class.

    The user decision is returned in the event handler as the `result` property of the [Tizen.Security.RequestResponseEventArgs](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.RequestResponseEventArgs.html) class.

    Make sure the event handler is registered before calling the `RequestPermission()` method of the `Tizen.Security.PrivacyPrivilegeManager` class. For a Xamarin.Forms application, the best place to register the event handler is the `Xamarin.Forms.Application.OnStart()` life-cycle method.

    ```csharp
    private void SetupPPMHandler(string privilege)
    {
        PrivacyPrivilegeManager.ResponseContext context = null;
        if (PrivacyPrivilegeManager.GetResponseContext(privilege).TryGetTarget(out context))
        {
            context.ResponseFetched += PPMResponseHandler;
        }
    }

    protected override void OnStart()
    {
        SetupPPMHandler(cameraPrivilege);
    }

    void PPMResponseHandler(object sender, RequestResponseEventArgs e)
    {
        if (e.cause == CallCause.Error)
        {
            /// Handle errors
            return;
        }

        switch (e.result)
        {
            case RequestResult.AllowForever:
                /// Update UI and start accessing protected functionality
                break;
            case RequestResult.DenyForever:
                /// Show a message and terminate the application
                break;
            case RequestResult.DenyOnce:
                /// Show a message with explanation
                break;
        }
    }
    ```

    -   If the user decision is `AllowForever` or `DenyForever`, the decision is definitive and the application can react appropriately. It can finish its execution (if denied permission) or start to use protected methods (if granted permission).
    -   If the user decision is `DenyOnce`, the decision is not definitive. In this case, access to protected functionality is still prohibited. This decision can be interpreted as a cancel action on behalf of the user, indicating that the user is not sure what the purpose of the request is. Therefore, consider providing some additional information to explain why the permission is required.

    If the decision is definitive, any subsequent `RequestPermission()` calls result in an immediate response with an appropriate result: `AllowForever` or `DenyForever`. However, the user can change the status of privacy-related privileges later by modifying the privacy settings on the device. For this reason, the application must always check the status of privacy-related privileges before using protected functionality.

## Requesting Multiple Permissions

This section describes how to check and request multiple privileges in a single API call.

> [!NOTE]
> Multiple privileges in a single API call are supported from Tizen 5.5.

To check whether an application has permission to use a privilege, and to request permission if required:

1. To verify whether an application has permission to use privileges, use `CheckPermissions()`:

      ```csharp
        string[] privileges = new [] {"http://tizen.org/privilege/account.read",
                                      "http://tizen.org/privilege/alarm"};
        CheckResult[] results = PrivacyPrivilegeManager.CheckPermissions(privileges).ToArray();
      ```

   The results of the call is stored in `CheckResult` array.

2. React to the permissions check appropriately:

      ```csharp
        List<string> privilegesWithAskStatus = new List<string>();
        try {
            for (int iterator = 0; iterator &lt; results.Length; ++iterator)
            {
      ```
   -   If the result value is `Allow`, the application is allowed to perform operations related to the privilege. For example, the application can enable additional UI elements or functionalities.
         ```csharp
                switch (results[iterator])
                {
                case CheckResult.Allow:
                    // Privilege can be used
                    break;
         ```

   -   If the result value is `Deny`, the application is not allowed to perform operations related to the privilege. Any attempt to use such functionality without the user's consent fails. Usually, this means that invoking any method that involves the privilege results in an error.
         ```csharp
                case CheckResult.Deny:
                    // Privilege can't be used
                    break;
         ```

   -   If the result value is `Ask`, the application must request permission from the user with the `RequestPermissions()` method, which displays a dialog box. When the user makes a decision, the answers are returned as
  [Tizen.Security.RequestMultipleResponseEventArgs](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.RequestMultipleResponseEventArgs.html).

         ```csharp
                case CheckResult.Ask:
                    // User permission request required
                    privilegesWithAskStatus.Add(privileges[iterator]);
                    break;
                }
         ```
	  ```csharp
            }
            RequestMultipleResponseEventArgs request;
            request = await PrivacyPrivilegeManager.RequestPermissions(privilegesWithAskStatus);

            if (request.Cause == CallCause.Error)
            {
                // handle errors
            }

            foreach (PermissionRequestResponse response in request.Responses)
            {
                // PermissionRequestResponse contains Privilege name and RequestResult
                switch (response.result)
                {
                    case RequestResult.AllowForever:
                        /// Update UI and start accessing protected functionality
                        break;
                    case RequestResult.DenyForever:
                        /// Show a message and terminate the application
                        break;
                    case RequestResult.DenyOnce:
                        /// Show a message with explanation
                        break;
                }
            }
        } catch (Exception e) {
            // handle exceptions
        }
      ```

> [!NOTE]
> Since the privileges are grouped, the user's decision regarding 1 privilege applies to the whole group of related privileges. For example, if the user has granted permission to use the `http://tizen.org/privilege/account.read` privilege, permission is automatically granted to the `http://tizen.org/privilege/account.write` privilege also. Be aware that both privileges need to be declared in the application manifest file. If you declare only 1 of them, the above rule does not apply.


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
