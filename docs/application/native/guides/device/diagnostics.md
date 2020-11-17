# Diagnostics

Diagnostics API is used to collect data from applications and services. This API also allows you to read crash reports if a process in the system crashes.

**Figure: Diagnostics overall architecture**

![Diagnostics overall architecture](media/diag-arch.png)

## Prerequisites

To enable your application to use Diagnostics API:

1. To use Diagnostics API to collect diagnostics data, the application must be signed with a platform level distributor certificate.

   To sign application with a platform level certificate:

   1. In Tizen Studio, select **Tools > Certificate Manager**.
   2. To add a new certificate profile, click **+** in the Certificate Manager window.

      ![Add a new profile](media/diag-add-new-profile.png)

   3. Enter the profile name and click **Next**.

      ![Enter the profile name](media/diag-set-profile-name.png)

   4. Select **Select an existing author certificate** and click **Next**.

      ![Select **Select an existing author certificate**](media/diag-select-author-cert.png)

   5. Select an author certificate from the disk using **Browse**. Enter the password if needed and click **Next**.

      ![Choose the author certificate](media/diag-choose-tizen-author-cert.png)

   6. Select **Select a distributor certificate for an another app store** and click **Next**.

      ![Select **Select a distributor certificate for an another app store**](media/diag-select-distributor-cert.png)

   7. Click **Browse** and select the distributor certificate. Enter the password and click **Finish**.

      ![Choose the distributor certificate](media/diag-choose-tizen-distributor-cert.png)

      This newly added profile appears in the profile list.

   8. Click **Close**.

      ![Newly added profile](media/diag-finish.png)

2. To use functions and data types of Diagnostics API, include the `<diagnostics.h>` header file in your application:

   ```cpp
   #include <diagnostics.h>
   ```

## Crash reports

Diagnostics allows you to read the crash reports in case the process in the system fails. To do so, you must register the callback that will be called when the crash report is created:

```cpp
void crash_callback(diagnostics_ctx_h ctx, void *user_data)
{
    ...
}

int register_callback(void *user_data)
{
    return diagnostics_set_notification_cb(crash_callback, user_data);
}
```

To deregister the callback, use `diagnostics_unset_notification_cb()`.

In case a new crash report is created, callback is called. To read the content of the crash report use `diagnostics_get_data()`:

```cpp
void crash_callback(diagnostics_ctx_h ctx, void *user_data)
{
    diagnostics_data_h data;
    const char *params[] = {"cs_info_json"};

    int ret = diagnostics_get_data(ctx, params, 1, &data);
    if (ret != DIAGNOSTICS_ERROR_NONE)
        return;

    ...
}
```

Use the `params` argument to specify which data to read from the crash report. Currently, the proper values are:

-   `"cs_info_json"`: JSON report is returned, which contains information about crashed process such as callstack, mapped memory regions, and so on.
-   `"cs_full"`: Full crash report ZIP archive is collected.

The obtained data is associated with the `data` Diagnostics handler. To read the data content, use `diagnostics_data_read()`:

```cpp
void crash_callback(diagnostics_ctx_h ctx, void *user_data)
{
    diagnostics_data_h data;
    const char *params[] = {"cs_info_json"};

    int ret = diagnostics_get_data(ctx, params, 1, &data);
    if (ret != DIAGNOSTICS_ERROR_NONE)
        return;

    char buff[0x1000];
    int timeout_ms = 0;
    size_t bytes_read;

    for (;;) {
        ret = diagnostics_data_read(data, buff, sizeof(buff), timeout_ms, &bytes_read);
        if (ret == DIAGNOSTICS_ERROR_TRY_AGAIN)
            continue;

        if (ret != DIAGNOSTICS_ERROR_NONE)
            break; // error occured

        if (bytes_read == 0)
            break; // no more data to read

        fwrite(buff, 1, bytes_read, stdout); // write received data to the STDOUT
    }
}
```

## Diagnostic data request

Diagnostics API also can request data from other application or service, especially the diagnostic data that for various reasons cannot or must not be saved in the logs, such as binary or in custom format data, large volume data, reports that are time-consuming to create, and so on.

To do so, call `diagnostics_request_client_data()`. The `client_id` variable must be the id of the process that supports Diagnostics API requests:

```cpp
void request_data()
{
    const char *client_id = "org.tizen.some_service";
    diagnostics_data_h data;
    const char *params[] = {"custom_parameter"};

    int ret = diagnostics_request_client_data(client_id, params, 1, &data);
    if (ret != DIAGNOSTICS_ERROR_NONE)
        return;

    char buff[0x1000];
    int timeout_ms = 0;
    size_t bytes_read;

    for (;;) {
        ret = diagnostics_data_read(data, buff, sizeof(buff), timeout_ms, &bytes_read);
        if (ret == DIAGNOSTICS_ERROR_TRY_AGAIN)
            continue;

        if (ret != DIAGNOSTICS_ERROR_NONE)
            break; // error occured

        if (bytes_read == 0)
            break; // no more data to read

        fwrite(buff, 1, bytes_read, stdout); // write received data to the STDOUT
    }
}
```

If `diagnostics_request_client_data()` returns successfully, the obtained data can be read by `diagnostics_data_read()`.

## Related information
- Dependencies
  - Tizen 6.0 and Higher for Mobile
  - Tizen 6.0 and Higher for Wearable
