# Synchronization Management


Tizen provides notifications for a service application to maintain data consistency between a server and the device.

You can manage the synchronization schedule for applications by using a UI application to request for sync jobs through the Sync Manager, and a service application to listen for the requests through the [Sync Adapter](#adapter). The service and UI applications must have the same package name.

The main features of the Sync Manager API include:

- Adding on-demand sync job schedules

  You can [add an on-demand sync job for a one-time operation](#on_demand_sync).

- Adding periodic sync job schedules

  You can [add a periodic sync job with a recurring cycle](#periodic_sync).

- Adding data change sync job schedules

  You can [add a data change sync job](#data_change_sync) for receiving notifications whenever a specific database change occurs.

- Removing registered sync job schedules

- Iterating registered sync job schedules

  You can [iterate all the registered sync jobs](#foreach_sync) for managing them more efficiently.

Use the [sync manager variables](#variables) with the sync job functions. The sync manager operates the sync jobs based on the rules defined in the following table.

**Table: Sync job scheduling rules**

| Rule                       | Description                              |
|----------------------------|------------------------------------------|
| Data changes on the server | A server sends a push message to the account provider service and service applications. When the data is changed on the server, a push message is sent from the server. Then, the device which receives the push message can trigger an on-demand sync job. |
| Data changes on the device | A subscribed callback function is invoked whenever a database change occurs for a registered capability. The data change listener notices the changes by using the Calendar (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CALENDAR__SVC__MODULE.html) applications), Contacts (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) applications), and Media Content (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CONTENT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CONTENT__MODULE.html) applications) APIs. If there are any changes in the corresponding data, the sync manager notices the changes and schedules a sync job.<br>Changing data in the Calendar database includes adding, updating, and deleting books, events, and todos. Changing data in the Contacts database includes adding, removing, and modifying contacts. The Media Content API provides notifications for changes in media types, such as image, music, sound, and video. |
| Network availability       | When a status change in the Wi-Fi or data network is detected, the behavior of the sync operation changes. |
| On demand sync             | The on-demand sync means that you can schedule a sync job once. You can use this feature with the `sync_manager_on_demand_sync_job()` function. |
| Periodic sync              | The periodic sync means that you can schedule a sync job to be performed regularly. You can use this feature with the `sync_manager_add_periodic_sync_job()` function. You can also use the sync intervals through various enumerators provided through the Sync Manager API.<br> When using the Sync Manager API, you can set an alarm indirectly. |

<a name="adapter"></a>
## Sync Adapter

> **Note**
>
> The Sync Adapter API (in [mobile](../../api/mobile/latest/group__CAPI__SYNC__ADAPTER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYNC__ADAPTER__MODULE.html) applications) operations must be carried out by a service application (which operates data synchronization) before using the Sync Manager API.
>
> The number of service applications that can set callbacks is restricted to only 1 per package.

The Sync Adapter API allows you to:

- [Register callbacks](#set_callback) for receiving notifications about the sync job start and cancellation.

- Start a sync operation with an app control, so that the application's daemon needs not to stay awake.

  The Sync Adapter API allows you to use this mechanism without using the App Control API (in [mobile](../../api/mobile/latest/group__CAPI__APP__CONTROL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__APP__CONTROL__MODULE.html) applications) separately. In other words, when using the Sync Adapter API, you can use the App Control API indirectly.

## Prerequisites

To enable your application to use the synchronization management functionality:

1. To use the Sync Manager API (in [mobile](../../api/mobile/latest/group__CAPI__SYNC__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYNC__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <!--To set an alarm-->
       <privilege>http://tizen.org/privilege/alarm.set</privilege>
       <!--To use the calendar capability-->
       <privilege>http://tizen.org/privilege/calendar.read</privilege>
       <!--To use the contact capability-->
       <privilege>http://tizen.org/privilege/contact.read</privilege>
    </privileges>
    ```

2. Before using the Sync Manager API, check whether the device supports the synchronization management feature with the `system_info_get_platform_bool()` function. If the device supports the Sync Manager API, the function returns `true` in the second parameter.

    ```
    bool sync_support;

    system_info_get_platform_bool("http://tizen.org/feature/account.sync", &sync_support);
    ```

3. [Set the sync adapter callbacks](#set_callback) in the service application:

    ```
    #include <sync_adapter.h>

    int result;
    result = sync_adapter_set_callbacks(on_start_cb, on_cancel_cb);
    ```

	A UI application cannot initialize and set callbacks through the Sync Adapter API (in [mobile](../../api/mobile/latest/group__CAPI__SYNC__ADAPTER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYNC__ADAPTER__MODULE.html) applications). Instead, the UI application must call the Sync Manager API to request sync operations.

4. To use the functions and data types of the Sync Manager API, include the `<sync_manager.h>` header file in the UI application:

    ```
    #include <sync_manager.h>
    ```

5. To use the functions and data types of the Sync Adapter API, include the `<sync_adapter.h>` header file in the service application:

    ```
    #include <sync_adapter.h>
    ```

<a name=""></a>
## Defining an On-demand Sync Job

To inform a service application of the time to operate a one-time sync job:

1. If you want to use an account, create the account and obtain the parameters that are used to call the `sync_manager_on_demand_sync_job()` function.

    For more information, see [Creating and Managing an Account](account.md#add) and [Managing and Using the Bundle Content](../app-management/data-bundles.md#manage).

    ```
    account_h account = NULL;
    int account_id = -1;

    account_create(&account);
    account_set_user_name(account, "test_name");
    account_set_email_address(account, "test_email@samsung.com");
    account_set_package_name(account, "data-sync-module");
    account_set_sync_support(account, ACCOUNT_SUPPORTS_SYNC);
    account_insert_to_db(account, &account_id);

    const char *sync_job_name = "on_demand_sync_job";

    bundle *sync_job_user_data = NULL;
    sync_job_user_data = bundle_create();
    bundle_add_str(sync_job_user_data, "str", "String sync_job_user_data sample.");

    int sync_job_id = -1;
    ```

2. Add an on-demand sync job:

   ```
   result = sync_manager_on_demand_sync_job(account, sync_job_name, SYNC_OPTION_NONE,
                                            sync_job_user_data, &sync_job_id);
   ```

   This function can be used with various options, as shown in the following example. The `SYNC_OPTION_NO_RETRY` option means the sync job is not performed again when it fails. The `SYNC_OPTION_EXPEDITED` option means the other sync job is operated as soon as possible. The call with the OR structure lets the other sync job operate just once with priority.

   ```
   result = sync_manager_on_demand_sync_job(account, sync_job_name2, SYNC_OPTION_NO_RETRY,
                                            sync_job_user_data, &sync_job_id2);
   result = sync_manager_on_demand_sync_job(account, sync_job_name3, SYNC_OPTION_EXPEDITED,
                                            sync_job_user_data, &sync_job_id3);
   result = sync_manager_on_demand_sync_job(account, sync_job_name4,
                                            (SYNC_OPTION_NO_RETRY | SYNC_OPTION_EXPEDITED),
                                            sync_job_user_data, &sync_job_id4);
   ```

   This function can also be called like in the following example, because the account handle and user data are not mandatory:

   ```
   result = sync_manager_on_demand_sync_job(NULL, sync_job_name, SYNC_OPTION_NONE,
                                            sync_job_user_data, &sync_job_id);
   result = sync_manager_on_demand_sync_job(account, sync_job_name2, SYNC_OPTION_NO_RETRY,
                                            NULL, &sync_job_id2);
   result = sync_manager_on_demand_sync_job(NULL, sync_job_name3, SYNC_OPTION_EXPEDITED,
                                            NULL, &sync_job_id3);
   ```

   If the on-demand sync job addition process succeeds, the `SYNC_ERROR_NONE` value is returned.

3. When the on-demand sync is no longer needed, remove it with the `sync_manager_remove_sync_job()` function with its `sync_job_id`. If you want to stop using the account too, clean up the account handle.

    At the end, unset the sync callbacks and release the resources with the `sync_adapter_unset_callbacks()` function.

    ```
    result = sync_manager_remove_sync_job(sync_job_id);

    account_delete_from_db_by_package_name("data-sync-module");
    account_destroy(account);

    sync_adapter_unset_callbacks();
    ```

	If no account is used:

    ```
    result = sync_manager_remove_sync_job(sync_job_id);

    sync_adapter_unset_callbacks();
    ```

<a name="periodic_sync"></a>
## Defining a Periodic Sync Job

To inform a service application of the time interval at which to operate a sync job:

1. If you want to use an account, create the account and obtain the parameters that are used to call the `sync_manager_add_periodic_sync_job()` function.

    For more information, see [Creating and Managing an Account](account.md#add) and [Managing and Using the Bundle Content](../app-management/data-bundles.md#manage).

    ```
    account_h account = NULL;
    int account_id = -1;
    account_create(&account);
    account_set_user_name(account, "test_name");
    account_set_email_address(account, "test_email@samsung.com");
    account_set_package_name(account, "data-sync-module");
    account_set_sync_support(account, ACCOUNT_SUPPORTS_SYNC);
    account_insert_to_db(account, &account_id);

    const char *sync_job_name = "periodic_sync_job";

    sync_period_e sync_period = SYNC_PERIOD_INTERVAL_30MIN;
    sync_period_e sync_period2 = SYNC_PERIOD_INTERVAL_1H;
    sync_period_e sync_period3 = SYNC_PERIOD_INTERVAL_3H;
    sync_period_e sync_period4 = SYNC_PERIOD_INTERVAL_6H;

    bundle *sync_job_user_data = NULL;
    sync_job_user_data = bundle_create();
    bundle_add_str(sync_job_user_data, "str", "String sync_job_user_data sample.");

    int sync_job_id = -1;
    ```

2. Add a periodic sync job with an interval as 30 minutes.

   This function operates the sync job with the given period interval.

   ```
   result = sync_manager_add_periodic_sync_job(account, sync_job_name, sync_period,
                                               SYNC_OPTION_NONE, sync_job_user_data,
                                               &sync_job_id);
   ```

   This function can be used with various options, as shown in the following example. The `SYNC_OPTION_NO_RETRY` option means a sync job is not performed again when it fails. The `SYNC_OPTION_EXPEDITED` option means another sync job is operated as soon as possible. The call with the OR structure lets the other sync job operate just once with priority.

   ```
   result = sync_manager_add_periodic_sync_job(account, sync_job_name2, sync_period2,
                                               SYNC_OPTION_NO_RETRY, sync_job_user_data,
                                               &sync_job_id2);
   result = sync_manager_add_periodic_sync_job(account, sync_job_name3, sync_period3,
                                               SYNC_OPTION_EXPEDITED, sync_job_user_data,
                                               &sync_job_id3);
   result = sync_manager_add_periodic_sync_job(account, sync_job_name4, sync_period4,
                                               (SYNC_OPTION_NO_RETRY | SYNC_OPTION_EXPEDITED),
                                               sync_job_user_data, &sync_job_id4);
   ```

   This function can also be called like in the following example, because the account handle and user data are not mandatory:

   ```
   result = sync_manager_add_periodic_sync_job(NULL, sync_job_name, sync_period,
                                               SYNC_OPTION_NONE, sync_job_user_data,
                                               &sync_job_id);
   result = sync_manager_add_periodic_sync_job(account, sync_job_name2, sync_period2,
                                               SYNC_OPTION_NO_RETRY, NULL,
                                               &sync_job_id2);
   result = sync_manager_add_periodic_sync_job(NULL, sync_job_name3, sync_period3,
                                               SYNC_OPTION_EXPEDITED, NULL,
                                               &sync_job_id3);
   ```

   If the periodic sync job addition process succeeds, the `SYNC_ERROR_NONE` value is returned.

3. The `sync_manager_add_periodic_sync_job()` function can renew a registered periodic sync job by using the same `sync_job_name` as before:

    ```
    result = sync_manager_add_periodic_sync_job(account, sync_job_name, sync_period,
                                                SYNC_OPTION_NONE, sync_job_user_data,
                                                &sync_job_id);
    result = sync_manager_add_periodic_sync_job(account, sync_job_name, sync_period2,
                                                SYNC_OPTION_EXPEDITED, sync_job_user_data2,
                                                &sync_job_id);
    ```

	All the function parameters can be reset except `sync_job_name` and `sync_job_id`, which are used to manage a specific sync job.

4. When the periodic sync is no longer needed, remove it with the `sync_manager_remove_sync_job()` function with its `sync_job_id`. If you want to stop using the account too, clean up the account handle.

    At the end, unset the sync callbacks and release the resources with the `sync_adapter_unset_callbacks()` function.

    ```
    result = sync_manager_remove_sync_job(sync_job_id);

    account_delete_from_db_by_package_name("data-sync-module");
    account_destroy(account);

    sync_adapter_unset_callbacks();
    ```

    If no account is used:
    ```
    result = sync_manager_remove_sync_job(sync_job_id);

    sync_adapter_unset_callbacks();
    ```

<a name="data_change_sync"></a>
## Defining a Data Change Sync Job

To inform a service application of the time to operate a sync job whenever a corresponding database change occurs:

1. If you want to use an account, create the account and obtain the parameters that are used to call the `sync_manager_add_data_change_sync_job()` function.

    For more information, see [Creating and Managing an Account](account.md#add) and [Managing and Using the Bundle Content](../app-management/data-bundles.md#manage).

    ```
    account_h account = NULL;
    int account_id = -1;
    account_create(&account);
    account_set_user_name(account, "test_name");
    account_set_email_address(account, "test_email@samsung.com");
    account_set_package_name(account, "data-sync-module");
    account_set_sync_support(account, ACCOUNT_SUPPORTS_SYNC);
    account_insert_to_db(account, &account_id);

    const char *sync_capability_calendar = SYNC_SUPPORTS_CAPABILITY_CALENDAR;
    const char *sync_capability_contact = SYNC_SUPPORTS_CAPABILITY_CONTACT;
    const char *sync_capability_image = SYNC_SUPPORTS_CAPABILITY_IMAGE;
    const char *sync_capability_music = SYNC_SUPPORTS_CAPABILITY_MUSIC;
    const char *sync_capability_sound = SYNC_SUPPORTS_CAPABILITY_SOUND;
    const char *sync_capability_video = SYNC_SUPPORTS_CAPABILITY_VIDEO;

    bundle *sync_job_user_data = NULL;
    sync_job_user_data = bundle_create();
    bundle_add_str(sync_job_user_data, "str", "String sync_job_user_data sample.");

    int sync_job_id = -1;
    ```

2. Add a data change sync job for the calendar capability.

   The `sync_manager_add_data_change_sync_job()` function operates a sync job only for a registered capability.

   ```
   result = sync_manager_add_data_change_sync_job(account, sync_capability_calendar,
                                                  SYNC_OPTION_NONE, sync_job_user_data,
                                                  &sync_job_id);
   ```

   This function can be used with various options, as shown in the following example. The `SYNC_OPTION_NO_RETRY` option means a sync job is not performed again when it fails. The `SYNC_OPTION_EXPEDITED` option means another sync job is operated as soon as possible. The call with the OR structure lets the other sync job operate just once with priority.

   ```
   result = sync_manager_add_data_change_sync_job(account, sync_capability_calendar,
                                                  SYNC_OPTION_NO_RETRY, sync_job_user_data,
                                                  &sync_job_id2);
   result = sync_manager_add_data_change_sync_job(account, sync_capability_contact,
                                                  SYNC_OPTION_EXPEDITED, sync_job_user_data,
                                                  &sync_job_id3);
   result = sync_manager_add_data_change_sync_job(account, sync_capability_image,
                                                  (SYNC_OPTION_NO_RETRY | SYNC_OPTION_EXPEDITED),
                                                  sync_job_user_data, &sync_job_id4);
   ```

   This function can also be called like in the following example, because the account handle and user data are not mandatory:

   ```
   result = sync_manager_add_data_change_sync_job(NULL, sync_capability_music,
                                                  SYNC_OPTION_NONE, sync_job_user_data,
                                                  &sync_job_id);
   result = sync_manager_add_data_change_sync_job(account, sync_capability_sound,
                                                  SYNC_OPTION_NO_RETRY, NULL,
                                                  &sync_job_id2);
   result = sync_manager_add_data_change_sync_job(NULL, sync_capability_video,
                                                  SYNC_OPTION_EXPEDITED, NULL,
                                                  &sync_job_id3);
   ```

   If the data change sync job addition process succeeds, the `SYNC_ERROR_NONE` value is returned.

3. The `sync_manager_add_data_change_sync_job()` function can renew a registered data change sync job by using the same `sync_capability` as before:

    ```
    result = sync_manager_add_data_change_sync_job(account, sync_capability_calendar,
                                                   SYNC_OPTION_NONE, sync_job_user_data,
                                                   &sync_job_id);
    result = sync_manager_add_data_change_sync_job(account, sync_capability_calendar,
                                                   SYNC_OPTION_EXPEDITED, sync_job_user_data2,
                                                   &sync_job_id);
    ```

	All the function parameters can be reset except `sync_capability` and `sync_job_id`, which are used to manage a specific sync job.

4. When the data change sync is no longer needed, remove it with the `sync_manager_remove_sync_job()` function with its `sync_job_id`. If you want to stop using the account too, clean up the account handle.

    At the end, unset the sync callbacks and release the resources with the `sync_adapter_unset_callbacks()` function.

    ```
    result = sync_manager_remove_sync_job(sync_job_id);

    account_delete_from_db_by_package_name("data-sync-module");
    account_destroy(account);

    sync_adapter_unset_callbacks();
    ```

	If no account is used:

    ```
    result = sync_manager_remove_sync_job(sync_job_id);

    sync_adapter_unset_callbacks();
    ```

<a name="foreach_sync"></a>
## Defining a ForEach Sync Job

To iterate all registered sync jobs to manage them more efficiently:

1. Set the callback to be invoked and call the iterate function at the same time:

   ```
   int result;
   result = sync_manager_foreach_sync_job(sync_job_cb, NULL);
   ```

2. Define the `sync_job_cb()` callback, which is invoked separately for every registered sync job. In the callback, the sync jobs are verified with a corresponding data.

    ```
    bool
    sync_job_cb(account_h account, const char *sync_job_name, const char *sync_capability,
                int sync_job_id, bundle *sync_job_user_data, void *user_data)
    {
        /* Verify the registered sync jobs */
    }
    ```

<a name="set_callback"></a>
## Setting the Callback Functions

To set callbacks in the service application to receive notifications about sync operations:

1. Subscribe to the callback functions to receive notifications for the sync operation when a specific event or condition is detected on the device:

   ```
   int result;
   result = sync_adapter_set_callbacks(on_start_cb, on_cancel_cb);
   ```

   When a specific event is detected or a sync job is requested, the applicable callback is invoked.

2. When the `on_start_cb()` callback is invoked, the predefined data sync process is performed inside the callback function. The `on_cancel_cb()` callback works in a similar way and cancels the data sync process.

    ```
    bool
    on_start_cb(account_h account, const char *sync_job_name,
                const char *sync_capability, bundle *sync_job_user_data)
    {
        /* Start the data sync process */
    }

    void
    on_cancel_cb(account_h account, const char *sync_job_name,
                 const char *sync_capability, bundle *sync_job_user_data)
    {
        /* Cancel the data sync process */
    }
    ```

3. When the sync operation notifications are no longer needed, unset the callbacks to free the sync adapter instance:

   ```
   result = sync_adapter_unset_callbacks();
   ```

<a name="variables"></a>
## Sync Manager Variables

The following table lists the variables used with the sync manager.

**Table: Sync manager variables**
<table border="1">
	<thead>
		<tr>
			<th>Variable</th>
			<th>Data type</th>
			<th>Mandatory</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Account handle</td>
			<td><code>account_s*</code></td>
			<td>No</td>
			<td>Handle of the account module for managing account-related data.</td>
		</tr>
		<tr>
			<td>Sync job name</td>
			<td><code>const char*</code></td>
			<td>Yes</td>
			<td>Sync job name for managing sync jobs.
			<p>The on-demand and periodic sync jobs can be managed by a user-defined name. If the <code>sync_manager_add_periodic_sync_job()</code> function is called again with same sync job name (where all details except the name and sync job ID are changed), the function does not add a new sync job but updates the existing job. This is mainly used to reset the periodic interval.</p>
			</td>
		</tr>
		<tr>
			<td>Sync capability</td>
			<td><code>const char*</code></td>
			<td>Yes</td>
			<td>Capability for adding data change sync jobs.
			<p>A data change sync job can provide a notification whenever a corresponding data change occurs. If the <code>sync_manager_add_data_change_sync_job()</code> function is used with a capability, it is operated for the related capability only.</p>
			<p>The following capabilities are available:</p>
			<pre><code>
#define SYNC_SUPPORTS_CAPABILITY_CALENDAR "http://tizen.org/sync/capability/calendar"
#define SYNC_SUPPORTS_CAPABILITY_CONTACT "http://tizen.org/sync/capability/contact"
#define SYNC_SUPPORTS_CAPABILITY_IMAGE "http://tizen.org/sync/capability/image"
#define SYNC_SUPPORTS_CAPABILITY_MUSIC "http://tizen.org/sync/capability/music"
#define SYNC_SUPPORTS_CAPABILITY_SOUND "http://tizen.org/sync/capability/sound"
#define SYNC_SUPPORTS_CAPABILITY_VIDEO "http://tizen.org/sync/capability/video"
</code></pre>
			</td>
		</tr>
		<tr>
			<td>Sync period</td>
			<td><code>sync_period_e</code></td>
			<td>Yes</td>
			<td>Interval for adding a periodic sync job.
			<p>If the interval is provided, the sync job is performed periodically. If you set the periodic interval to 30 minutes, a time interval is set as a power of 2 less than 30. This means that a time interval set to 16 minutes operates the sync job every 16 minutes while skipping the first notification (so the first is in 32 minutes). The same logic applies to other cases.</p>
			<p>This variable provides a periodic sync job with an inexact time. Coupling various periodic sync jobs with an interval as a power of 2 prevents the device from waking up the service application too many times.</p>
			<p>The <code>sync_period_e</code> enumerator (in <a href="../../api/mobile/latest/group__CAPI__SYNC__MANAGER__MODULE.html#gad6f301bc84c4e758aee1636b0122dd7e">mobile</a> and <a href="../../api/wearable/latest/group__CAPI__SYNC__MANAGER__MODULE.html#gad6f301bc84c4e758aee1636b0122dd7e">wearable</a> applications) defines the available period intervals.</p>
			</td>
		</tr>
		<tr>
			<td>Sync option</td>
			<td><code>sync_option_e</code></td>
			<td>Yes</td>
			<td>Option for deciding the sync job behavior.
			<p>The behavior options can be used as an OR value. For example, the <code>(SYNC_OPTION_EXPEDITED | SYNC_OPTION_NO_RETRY)</code> expression is available, and means that the "Sync job is operated just once with priority".</p>
			<p>The following options are available:</p>
			<ul>
				<li><code>SYNC_OPTION_NONE</code>: Sync job is operated normally</li>
				<li><code>SYNC_OPTION_EXPEDITED</code>: Sync job is operated as soon as possible</li>
				<li><code>SYNC_OPTION_NO_RETRY</code>: Sync job is not performed again when it fails</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Sync job ID</td>
			<td><code>int*</code></td>
			<td>Yes</td>
			<td>Unique ID for managing sync jobs.
			<p>The ID is generated when a sync job is added. It is required to remove the sync job. The number of ID that can be generated is restricted to a hundred per package.</p>
			</td>
		</tr>
		<tr>
			<td>Sync job user data</td>
			<td><code>bundle*</code></td>
			<td>No</td>
			<td>User data for sync jobs.
			<p>The data can contain additional information related to the registered sync jobs.</p>
			</td>
		</tr>
		<tr>
			<td>User data</td>
			<td><code>void*</code></td>
			<td>No</td>
			<td>User data for the <code>sync_manager_for_each_sync_job()</code> function.
			<p>The data can contain additional information related to the foreach jobs.</p>
			</td>
		</tr>
	</tbody>
</table>

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
