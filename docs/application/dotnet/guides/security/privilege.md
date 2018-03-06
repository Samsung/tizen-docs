# Privilege Information


Tizen provides privilege information for user notification.

With the [Tizen.Security.Privilege](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.Privilege.html) class, you can [retrieve the following privilege information](#get):

-   Privilege name: Privilege description in a simple present participle form.
-   Privilege description: Detailed information on permissions, including accessible resources and functionality, that the application can get with this privilege. It also contains information related to billing or device performance, such as cost or increased battery usage.
-   Privacy name: Privacy name represents a group of privileges that are related to a certain privacy feature.

Since Tizen 3.0, some privileges are categorized as privacy-related. The user can switch those privileges on and off as needed by changing certain privileges' status to allow or deny them at runtime. This means that the application calling a privileged method can be prevented from using it even if the required privilege is declared in its manifest file. Specific methods can be used to check the privacy-related privilege's current status and get the privacy name that includes the privilege. For example, you can use the methods to check the privilege's current status before calling a method that requires the privilege, and if the status is off, display a guide message to the user to ask them to go to the device privacy settings and switch the required privacy on.

## Prerequisites


To use the methods and properties of the [Tizen.Security.Privilege](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.Privilege.html) class, include the [Tizen.Security](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Security.html) namespace in your application. If you want to designate a privilege's type, include the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace too.

```
using Tizen.Security;
using Tizen.Applications;
```
<a name="get"></a>
## Getting Privilege Information

To get various privilege information:

-   Get the privilege display name using the `GetDisplayName()` method of the `Tizen.Security.Privilege` class:

    ```
    try
    {
        var displayName = Privilege.GetDisplayName("4.0", "http://tizen.org/privilege/internet");
        var displayNamePkgType = Privilege.GetDisplayName("4.0", "http://tizen.org/privilege/internet", PackageType.TPK);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get the privilege description using the `GetDescription()` method of the `Tizen.Security.Privilege` class:

    ```
    try
    {
        var description = Privilege.GetDescription("4.0", "http://tizen.org/privilege/internet");
        var descriptionPkgType = Privilege.GetDescription("4.0", "http://tizen.org/privilege/internet", PackageType.TPK);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get the privacy display name using the `GetPrivacyDisplayName()` method of the `Tizen.Security.Privilege` class:

    ```
    try
    {
        var privacyDisplayName = Privilege.GetPrivacyDisplayName("http://tizen.org/privilege/account.read");
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   Get the privacy-related privilege's status using the `GetPrivacyPrivilegeStatus()` method of the `Tizen.Security.Privilege` class:

    ```
    try
    {
        bool isAllowed = Privilege.GetPrivacyPrivilegeStatus("http://tizen.org/privilege/account.read");
        if (isAllowed)
        {
            /// Call privacy privileged methods
        }
        else
        {
            /// If the privilege is not allowed, take proper action,
            /// such as show a privacy request popup to the user (for example, "To use
            /// Account, enable it in Settings > Privacy and Security > Privacy Setting.")
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
