# Tizen Update Control Native API

Update Control API allows to control the system software version of the IoT device.
System software version control includes:
- Checking for the latest version
- Downloading and updating to the latest version in a synchronous or an asynchronous manner
- Making a time reservation for the update.

The update procedure and the server may vary depending on the platform developer.
Therefore, this API only offers general update functions, and platform developers must develop the application using Update Control API properly.

## Prerequisites

Steps to enable your application to use the update control functionality:

1. To use the Update Control API, the application must request permissions by adding the following privileges to the `tizen-manifest.xml` file:
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

The new version of the platform is usually uploaded at the server and each device must connect to server to get the new version.
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
bool* is_available;

error_code = update_control_get_property(UPDATE_CONTROL_PROPERTY_UPDATE_AVAILABLE, (void **)(&is_available));
if (error_code == UPDATE_CONTROL_ERROR_NONE) {
  if (*is_available)
    // New version platform is available
    ...

  free(is_available);
}
```

## Downloading and Updating to New Version - basic usage

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
Usually, downloading and updating are processed sequentially but the application also can call each function separately to perform the intended operation.

## Updating to New Version - advanced usage

There are 3 types of update routines: `update_control_do_update()` is the basic way to trigger an upgrade. The other two
functions: `update_control_do_ro_update_async()` and `update_control_do_finish_update_async()` allow to hook up callbacks
which will be triggered when the upgrade operation is completed.

`update_control_do_update()` - triggers the upgrade script and tells it to execute both the RO upgrade and the RW upgrade
operations (full upgrade process). This function only runs the upgrade script in the background and returns quickly.
It doesn't check the return value of the upgrade script. It only allows to check if the RO and RW upgrade have been
triggered successfully which doesn't guarantee successful completion).

`update_control_do_ro_update_async` - triggers the upgrade script and tells it to execute RO upgrade only. This function
does not perform the RW upgrade. Once the operation has completed, the callback set by the `update_control_set_ro_update_cb()`
will be triggered.

`update_control_do_finish_update_async` - triggers the upgrade script and tells it to reboot and execute only the RW upgrade
after reboot. This function does not perform the RO upgrade. To trigger the RO upgrade use `update_control_do_ro_update_async()`.
Once the operation has finished, the callback set by `update_control_set_finish_update_cb()` will be triggered on failure.
In case of success the callback may not be called, because the system will restart. The main purpose of this callback is to
handle an error - inform the user that the upgrade was unsuccessful.

`update_control_set_ro_update_cb()` - sets a callback to trigger once RO upgrade operation has completed (either successfully or erroneously).

`update_control_unset_ro_update_cb()` - unsets the callback set by `udpate_control_set_ro_update_cb()`.

`update_control_set_finish_update_cb()` - sets a callback to trigger once RW upgrade operation has completed (successfully or erroneously).

`update_control_unset_finish_update_cb()` - unsets the callback set by `udpate_control_set_finish_update_cb()`.

## Making an Update Reservation

The availability of the IoT device might be critical for its operation. Because updating procedure might include
unavailable time (for example, rebooting), it needs to schedule software update at a specific time.
In this case, the application can use the `update_control_make_reservation()` function:
```cpp
int error_code;
struct tm time;

// Set the "time" to trigger the update
error_code = update_control_make_reservation(&time);
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```
The reserved update task can also be canceled by `update_control_cancel_reservation()`.
```cpp
int error_code;

error_code = update_control_cancel_reservation();
if (error_code != UPDATE_CONTROL_ERROR_NONE)
  return;
```

> **Note**
>
> It assumes only one update reservation can be set. If the platform supports multiple reservations, then they must properly manage cancel request.

## Example

The following example initializes the update-control API, downloads the update package, hooks up an RO upgrade callback,
and triggers the RO upgrade with the asynchronous `update_control_do_ro_update_async` API function. Practically, the callback
will be triggered only when the upgrade fails at some stage. It won't be called on success, as the system restarts before it
performs an RO upgrade.

```cpp
#include <gio/gio.h>
#include <stdio.h>
#include <update_control.h>

static GMainLoop *main_loop = NULL;

void ro_update_control_cb(const update_control_error_e result, const void *user_data)
{
  if (result != UPDATE_CONTROL_ERROR_NONE) {
    fprintf(stderr, "RO upgrade failed, error code: %d\n", result);
  }
  else {
    fprintf(stderr, "RO upgrade succeeded\n");
  }
  g_main_loop_quit(main_loop);
  g_main_loop_unref(main_loop);
}

int main(int argc, char **argv)
{
  int error_code;

  error_code = update_control_initialize();
  if (error_code != UPDATE_CONTROL_ERROR_NONE) {
    fprintf(stderr, "Cannot initialize update control, error code: %d\n", error_code);
    return 1;
  }

  error_code = update_control_download_package();
  if (error_code != UPDATE_CONTROL_ERROR_NONE) {
    fprintf(stderr, "Failed to download update package, error code: %d\n", error_code);
    return 1;
  }

  main_loop = g_main_loop_new(NULL, FALSE);

  error_code = update_control_set_ro_update_cb(ro_update_control_cb, NULL);
  if (error_code != UPDATE_CONTROL_ERROR_NONE) {
    fprintf(stderr, "Failed to set callback for RO upgrade, error code: %d\n", error_code);
    return 1;
  }

  error_code = update_control_do_ro_update_async();
  if (error_code != UPDATE_CONTROL_ERROR_NONE) {
    fprintf(stderr, "Failed to trigger RO upgrade, error code: %d\n", error_code);
    return 1;
  }

  g_main_loop_run(main_loop);

  error_code = update_control_deinitialize();
  if (error_code != UPDATE_CONTROL_ERROR_NONE) {
    fprintf(stderr, "Failed to deinitialize update control, error code:: %d\n", error_code);
    return 1;

  return 0;
}
```

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

## Error Codes

The following error codes may occur while working with the update-control API functions:

| Error constant                                |  Error description         |
| ----------------------------------------------| -------------------------- |
| `UPDATE_CONTROL_ERROR_CONNECTION_REFUSED`     | Connection refused         |
| `UPDATE_CONTROL_ERROR_PROTOCOL_NOT_SUPPORTED` | Protocol not supported     |
| `UPDATE_CONTROL_ERROR_TIMED_OUT`              | Operation timed out        |
| `UPDATE_CONTROL_ERROR_RESOURCE_BUSY`          | Device or resource busy    |
| `UPDATE_CONTROL_ERROR_INVALID_OPERATION`      | Function not implemented   |
| `UPDATE_CONTROL_ERROR_INVALID_PACKAGE`        | Invalid package            |
| `UPDATE_CONTROL_ERROR_INVALID_URI`            | Invalid URI                |
| `UPDATE_CONTROL_ERROR_PACKAGE_NOT_SUPPORTED`  | Package type not supported |
| `UPDATE_CONTROL_ERROR_SYSTEM_ERROR`           | System error               |
| `UPDATE_CONTROL_ERROR_RO_UPDATE_IN_PROGRESS`  | RO update is in progress   |

