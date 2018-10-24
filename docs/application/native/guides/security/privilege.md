# Privilege Information


Tizen provides [privilege](../../tutorials/details/sec-privileges.md) information for user notification.

With the Privilege Info API, you can [retrieve the following privilege information](#get):

- Privilege name: Privilege description in a simple present participle form.
- Privilege description: Detailed information on permissions, including accessible resources and functionality, that the application can get with this privilege. It also contains information related to billing or device performance, such as cost or increased battery usage.
- Privacy name: Privacy name represents a group of privileges that are related to a certain privacy feature.

Since Tizen 3.0, some privileges are categorized as privacy-related. The user can switch those privileges on and off as needed by changing certain privileges' status to allow or deny them at runtime. This means that the application calling a privileged API can be prevented from using it even if the required privilege is declared in its manifest file. Specific APIs can be used to check the privacy-related privilege's current status and get the display name of the privacy that includes the privilege. For example, you can use the APIs to check the privilege's current status before entering a function that requires the privilege, and if the status is off, display a guide message to the user to ask them to go to the device settings and switch the required privacy on.

> **Note**  
> Since Tizen 4.0, the status of privacy-related privileges can be [resolved at runtime](../requesting-permissions.md) using the Privacy Privilege Manager API (in [mobile](../../api/mobile/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) applications).

## Prerequisites

To use the functions and data types of the Privilege Info API (in [mobile](../../api/mobile/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html) applications), include the `<privilege_information.h>` header file in your application:

```
#include <privilege_information.h>
```

<a name="get"></a>
## Getting Privilege Information

To get various privilege information:

- Get the privilege display name using the `privilege_info_get_display_name()` function:

    ```
    char* display_name = NULL;
    int ret = privilege_info_get_display_name("2.2",
                                              "http://tizen.org/privilege/application.launch",
                                              &display_name);
    ```

- Get the privilege display name by package type using the `privilege_info_get_display_name_by_pkgtype()` function:

    ```
    char* display_name = NULL;
    int ret = privilege_info_get_display_name_by_pkgtype("PRVINFO_PACKAGE_TYPE_WEB",
                                                         "2.2",
                                                         "http://tizen.org/privilege/application.launch",
                                                         &display_name);
    ```

- Get the privilege description using the `privilege_info_get_description()` function:

    ```
    char* description = NULL;
    int ret = privilege_info_get_description("2.2",
                                             "http://tizen.org/privilege/application.launch",
                                             &description);
    ```

- Get the privilege description by package type using the `privilege_info_get_description_by_pkgtype()` function:

    ```
    char* description = NULL;
    int ret = privilege_info_get_description_by_pkgtype("PRVINFO_PACKAGE_TYPE_WEB",
                                                        "2.2",
                                                        "http://tizen.org/privilege/application.launch",
                                                        &description);
    ```

- Get the privacy display name using the `privilege_info_get_privacy_display_name()` function:

    ```
    char* privacy_display_name = NULL;
    int ret = privilege_info_get_privacy_display_name("http://tizen.org/privilege/account.read",
                                                      &privacy_display_name);
    ```

- Get the privacy-related privilege's status using the `privilege_info_get_privacy_privilege_status()` function:

    ```
    bool status = NULL;
    int ret = privilege_info_get_privacy_privilege_status("http://tizen.org/privilege/account.read",
                                                          &status);
    ```

The above functions return a `privilege_info_error_e` enum value (in [mobile](../../api/mobile/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html#gae50b814d4efe1b1d7218b6d68cdcadd6) and [wearable](../../api/wearable/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVILEGE__INFO__MODULE.html#gae50b814d4efe1b1d7218b6d68cdcadd6) applications) that indicates the value retrieval result. They also store the requested privilege display name or description, privacy display, and privacy privilege status in their last parameter.

## Related Information
- Dependencies
  - Tizen 2.3 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
