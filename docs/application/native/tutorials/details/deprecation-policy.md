
# API Versioning and Deprecation Policy of the Tizen Platform


As much as the Tizen team wants to have a completely stable API, the
evolution of both hardware technology and software capabilities is
rapid. To be maximally useful, the API set must evolve to reflect those
changes to enable the development of compelling applications that use
those features. As an inevitable side effect, APIs may become obsolete
and need to be replaced by more feature-rich versions.

To mitigate the effect of the API deprecations, the Tizen team has
decided to support deprecated APIs for 2 releases. You are encouraged to
use the best API set that meets your needs at the time of development.
If the application needs a specific API version, you can indicate it in
the packaging information for Web, native, and hybrid application
packages.

<a name="versioning"></a>
## API Versioning


The version format used to identify the APIs of the Tizen platform is
**X.Y.Z** (Major.Minor.Micro). All changes, including any kind of
version update, maintain the application binary interface (ABI)
compatibility excepting only critical security reasons.

<a name="policy"></a>
## Deprecation Policy and Schedule

API deprecation is used to inform you that some APIs are no longer
recommended for use in your applications. The Tizen team is trying to
keep the API as stable as possible, but sometimes APIs must be
deprecated due to, for example, critical security issues, or new and
better alternatives.

Based on a careful analysis, the following deprecation policy has been
adopted in Tizen:

-   This policy comes into effect beginning with Tizen 2.4.

- The functionality of the deprecated API is available for 2 releases,
    as indicated in the following table.

  **Table: Deprecation schedule**

|      | V1 (Tizen 2.4/2.3.1/2.3.2)<br>Deprecation notice | V2 (Tizen 3.0)<br>Deprecated since V1 | V3 (Tizen 3.x)<br>Deprecated since V1 |
|---------------------|----------------------------------------|---------------------------------|---------------------------------|
| **API functionality**  | Available | Available  | **Not available**     |
| **API symbol** | Available   |Available                        | **Not available**   |
| **API Reference<br>API Guides<br>Samples** |Available  |Available      | **Not available**       |
| **TCT**  | Available   | Available    | **Not available**  |

- Deprecated APIs are removed after 2 version releases (including the
    notice version).

    During the 2 version releases, the functionality of the deprecated
    API may also be removed immediately for security reasons or as an
    unavoidable part of the platform evolution.

- Alternatives must be described within the reference of the
    deprecated API, if possible.

- All version changes are considered 1 release for purposes of the
    deprecation policy.


<a name="identify"></a>
## Identifying a Deprecated API


The Tizen Studio continues to provide deprecation warnings. From the API
reference, you can find a highlighted tag starting with **Deprecated**.
If there is an alternative for the deprecated API, it is specified
within that tag.

The following examples illustrate how the deprecation info is shown in
the API reference:

-   Deprecated API in the Native API:

    ```
    int app_context_get_package(app_context_h app_context, char ** package)

    Gets the package with the given application context.

    Deprecated:
        Deprecated since 2.3.1. Use app_context_get_app_id() instead.
    Since:
        2.3
    ```

- Deprecated API in the Web API:

    ```
    addAppInfoEventListener
    Adds a listener for receiving notifications for changes
    in the list of installed applications on a device.
    Deprecated. It is deprecated since Tizen 2.4. Instead, set a listener for getting notified
    of the application changes (add/remove/update) on a device using tizen.package.setPackageInfoEventListener().

    long addAppInfoEventListener(ApplicationInformationEventCallback eventCallback);

    Since: 2.0
    ```

- Deprecated enumeration in the Native API:

    ```
    enum telephony_call_state_e
    Enumeration for the call state.
    Deprecated:
        Deprecated Since 2.4. Use telephony_call_status_e instead.
    Since:
        2.3
    ```

- Deprecated type definition in the Native API:

    ```
    typedef void* bt_gatt_attribute_h
    The attribute handle of GATT (Generic Attribute Profile)
    Deprecated:
        Deprecated since 2.3.1. Use bt_gatt_h instead.
    Since:
        2.3
    ```

You can also see the API deprecation warning in log messages:

-   In a log message:

    ```
    DEPRECATION WARNING: app_context_get_package() is deprecated and
    will be removed from next release. Use app_context_get_app_id() instead.
    ```

- In a build log message:

    ```
    [2/3] Building src/basicuiwithedc.o
    ../src/basicuiwithedc.c:26:19: warning: 'app_get_resource_path' is deprecated [-Wdeprecated-declarations]
        char *res_path = app_get_resource_path();
    ```


<a name="compatibility"></a>
## API Backward Compatibility


With the best efforts, the Tizen platform tries to provide a backward
compatibility of public APIs documented in the API reference. Therefore, you must use the listed APIs in the API reference to make the applications compatible.
