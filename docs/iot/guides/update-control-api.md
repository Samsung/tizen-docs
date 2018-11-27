# Tizen Update Control Native API

You can control the system software version of IoT device using Update Control API.
The control of system software version includes:
- Checking the latest version
- Downloading and updating to the latest version
- Making a reservation for update

The update procedure and the server might be different according to the platform developer.
Therefore, this API just offers general functions for update, and platform developers must develop the application using Update Control API properly.

> **Note**
>
> As a default, the update agent works with [SmartThings Device Manager](https://console.smartthingsdm.com/) is available.

## Prerequisites

To enable your application to use the update control functionality:

1. To use the Update Control API, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:
    ```xml
       <privileges>
          <privilege>http://tizen.org/privilege/updatecontrol.admin</privilege>
       </privileges>
    ```

2. To use the functions and data types of the Update Control API, include the `<update_control.h>` header file in your application:
    ```cpp
    #include <update_control.h>
    ```

## Connecting to Server

The new version of platform is usually uploaded at the server and each device must connect to server to get the new version.
In some cases, connecting to server might require the procedure for getting the account information. The account information is obtained using `update_control_initialize()` or at the each update operations such as checking or downloading and updating the latest version.

**Example: Initializing update control**
```cpp
int error_code;

error_code = update_control_initialize();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```
> **Note**
>
> If some operation of deinitialization corresponding to initialization is required, the `update_control_deinitialize()` can be used.

## Checking the Latest Version

The device can query the latest version of current platform to the server. It can be implemented as the following:

```cpp
int error_code;

error_code = update_control_check_new_version();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```

If the newer version of platform is available, the correct value and type for `UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE` that depends on the platform developer will be set. The application can get the this value through the `update_control_get_property()` function:
```cpp
int error_code;
bool is_available;

error_code = update_control_get_property(UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE, (void **)&is_available);
if (error_code == UPDATE_CONTROL_ERROR_NONE) {
  if (is_available)
    // New version platform is available
    ...
}
```

## Downloading and Updating to New Version

If the newer version is available, you can download and update the system software to the latest available version.
The functions `update_control_download_package()` and `update_control_do_update()` are offered and their usage is similar to `update_control_get_property()`:
```cpp
int error_code;

error_code = update_control_download_package();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;

error_code = update_control_do_update();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```
Usually, downloading and updating are processed sequentially but the application also can call each function separately for intending operation.

## Making an Update Reservation

The availability of the IoT device might be critical for its operation. Because updating procedure might include unavailable time (For example, rebooting), it needs to schedule software update at specific time.
In this case, the application can use `update_control_make_reservation()` function:
```cpp
int error_code;
struct tm time;

// Set the "time" to trigger the update
error_code = update_control_make_reservation(&time);
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```
The reserved update task also can be canceled by `update_control_cancel_reservation()`.
```cpp
int error_code;

error_code = update_control_cancel_reservation();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```

> **Note**
>
> It assumes only one update reservation can be set. If the platform supports multiple reservations, then they must properly manage cancel request.

## Update Properties

Besides `UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE` mentioned in the code, there are several information about update.
You can get them through `update_control_get_property()` function and each key, which includes the following:

| Key                                   |  Description                                  | Type (example) |
| --------------------------------------| --------------------------------------------- |----------------|
| `UPDATE_CONTROL_PROPERTY_NEW_VERSION` | The value of new version (For example, string, and number). | string         |
| `UPDATE_CONTROL_PROPERTY_PACKAGE_URI` | URI of update package is uploaded.             | string         |
| `UPDATE_CONTROL_PROPERTY_RESULT`      | The result of recent update procedure.         | int            |
| `UPDATE_CONTROL_PROPERTY_PACKAGE_SIZE`| The size of update package to be downloaded.   | unsigned int   |
| `UPDATE_CONTROL_PROPERTY_DESCRIPTION` | The description about found version.           | string         |
| `UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE`| The flag of update availability.           | bool           |

Because their actual types depend on platform developer, the value that will be returned for each key must be known to the application.
