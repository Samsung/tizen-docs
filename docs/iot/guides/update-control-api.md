# Tizen Update Control Native API

- [Privilege & Feature](#privilege-feature)
- [Prerequisites](#prerequisites)
- [Connecting to Server](#connecting-to-server)
- [Checking the Latest Version](#checking-the-latest-version)
- [Downloading and Updating to New Version](#downloading-and-updating-to-new-version)
- [Making an Update Reservation](#making-an-update-reservation)
- [Update Properties](#update-properties)

You can control the system software version of IoT device using update control API.
The control of system software version includes:
- Checking the latest version
- Downloading and updating to the latest version
- Making a reservation for update

The update procedure and the server may be different according to the platform developer.
Therefore this API just offers general functions for update, and platform developers should develop the application using update control API properly.

>As a default, the update agent works with [SmartThings Device Manager](https://console.smartthingsdm.com/) is available.

## Privilege & Feature

The update control API requires special privilege and feature to use it.

| Privilege                                | Level    | Privacy      | Since | Description                              |
|----------------------------------------|-------|------------|-----|----------------------------------------|
| `http://tizen.org/privilege/updatecontrol.admin` | platform   | -      | 5.0   |  The application can control the firmware update procedure.       |

| Feature key                              | Description                              | Since |
|----------------------------------------|----------------------------------------|-----|
| `http://tizen.org/feature/device_update`       | Specify this key, if the application requires Device Update API to control the system software update of the device. | 5.0   |

More details about the privilege and feature, refer to [Security and API Privileges](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/security-and-api-privileges) and [Application Filtering](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/application-filtering).

## Prerequisites

To enable your application to use the update control functionality:

1. To use the update control API at applications, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

```xml
   <privileges>
      <privilege>http://tizen.org/privilege/updatecontrol.admin</privilege>
   </privileges>
```

2. To use the functions and data types of the update control API, include the `<update_control.h>` header file in your application

3. If some initialization is required to use update control functions, you can use `update_control_initialize()`

```cpp
int error_code;

error_code = update_control_initialize();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```
Likewise, there is a function `update_control_deinitialize()` for deinitialization.

## Connecting to Server

The new version of platform is usually uploaded at the server and each device should connect to server to get the new version.
In some cases, the procedure about the account may be required for connection. It can be done by `update_control_initialize()` or some of following procedures.

## Checking the Latest Version

The device can query the latest version of current platform to server. It can be implemented simply by:
```cpp
int error_code;

error_code = update_control_check_new_version();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```

If the newer version of platform is available, the value of `UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE` will be set properly
(It's type and value are depend on platform developer).
The application can get the result through the `update_control_get_property()` function:
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

If the newer version is available, the application can download it and update to the found one.
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

The device especially IoT may be critical at it's operation time. Because updating procedure may include unavailable time (ex. rebooting), it needs to schedule software update at specific time.
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

> **Note**
>
> It assumes only one update reservation can be set. If the platform supports multiple reservations, they should be managed properly about cancel request.

## Update Properties

Besides `UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE` mentioned at above, there are several information about update.
They can be got through `update_control_get_property()` function and each key:

| Key                                   |  Description                                  | Type (example) |
| --------------------------------------| --------------------------------------------- |----------------|
| `UPDATE_CONTROL_PROPERTY_NEW_VERSION` | The value of new version (ex. string, number) | string         |
| `UPDATE_CONTROL_PROPERTY_PACKAGE_URI` | URI of update package is uploaded             | string         |
| `UPDATE_CONTROL_PROPERTY_RESULT`      | The result of recent update procedure         | int            |
| `UPDATE_CONTROL_PROPERTY_PACKAGE_SIZE`| The size of update package to be downloaded   | unsigned int   |
| `UPDATE_CONTROL_PROPERTY_DESCRIPTION` | The description about found version           | string         |
| `UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE`| The flag of update availability           | bool           |

Because their actual types are depend on platform developer, the value that will be returned for each key should be known to the application.
