# Synchronization Management


You can manage a synchronization schedule for applications by using a UI application to request for sync jobs through the Sync Manager, and a service application to listen for the requests through the Sync Adapter. The service and UI applications must have the same package name.

The main features of the Tizen.Account.SyncManager namespace are:

-   Sync Adapter
    -   Setting Sync Adapter callbacks

        You can [set the callback methods](#set_callback) in your Sync Adapter service application that your client application can call to set up a sync operation.

-   Sync Manager
    -   Defining a sync job

        You can [create a new sync job](#set_parameters) and add user data into it as either an account information instance or a data bundle.

    -   Requesting an on-demand sync job

        You can [add an on-demand sync job](#on_demand_sync) for a one-time operation.

    -   Requesting a periodic sync job

        You can [add a periodic sync job](#periodic_sync) with a recurring cycle.

    -   Requesting a data change sync job

        You can [add a data change sync job](#data_change_sync) for receiving a notification whenever a specific database changes.

    -   Retrieving all registered sync jobs

        You can [get a list of all registered sync jobs](#foreach_sync).

    -   Removing sync jobs

        You can [remove registered sync jobs](#remove_sync) when they are no longer needed.

## Prerequisites


To enable your application to use the synchronization management functionality:

1.  To use the [Tizen.Account.SyncManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/account.read</privilege>
       <privilege>http://tizen.org/privilege/account.write</privilege>
       <privilege>http://tizen.org/privilege/alarm.set</privilege>
       <privilege>http://tizen.org/privilege/calendar.read</privilege>
       <privilege>http://tizen.org/privilege/contact.read</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Account.SyncManager namespace, include it in your application:

    ```
    using Tizen.Account.SyncManager;
    ```

> **Note**   
> To use the features of the [Tizen.Account.SyncManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.html) namespace, the service application must first [set the callbacks](#set_callback). A UI application cannot initialize or set callback methods through the [Tizen.Account.SyncManager.SyncAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncAdapter.html) class. Instead, the UI application must call the methods of the [Tizen.Account.SyncManager.SyncClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncClient.html) class to request sync operations from the service application.

<a name="set_callback"></a>
## Setting Sync Adapter Callbacks

To set callbacks in your Sync Adapter service application that your UI application can call to request sync operations:

1.  Set up event handlers for starting and stopping data synchronization. When the `StartSyncCallback()` callback of the [Tizen.Account.SyncManager.SyncAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncAdapter.html) class is invoked, the predefined data sync process is performed inside the callback method. The `CancelSyncCallback()` callback works in a similar way and cancels the data sync process.

    ```
    static bool StartSyncCallback(SyncJobData data)
    {
        /// Code for starting data synchronization

        return true;
    }

    static void CancelSyncCallback(SyncJobData data)
    {
        /// Code for cancelling data synchronization
    }
    ```

2.  Register the event callbacks with the `SetSyncEventCallbacks()` method of the `Tizen.Account.SyncManager.SyncAdapter` class to receive notifications regarding the sync operation.

    When a specific event is detected or a sync job is requested, the `StartSyncCallback()` or `CancelSyncCallback()` callbacks are invoked.

    ```
    SyncAdapter obj = new SyncAdapter();
    obj.SetSyncEventCallbacks(StartSyncCallback, CancelSyncCallback);
    ```

3.  When the sync operations are no longer needed, unset the callbacks to free the `Tizen.Account.SyncManager.SyncAdapter` instance:

    ```
    obj.UnsetSyncEventCallbacks();
    ```

<a name="set_parameters"></a>
## Defining a Sync Job

To define a sync job, create a new [Tizen.Account.SyncManager.SyncJobData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncJobData.html) instance:

```
SyncJobData request = new SyncJobData();
request.SyncJobName = "PeriodicSyncJob";
```

You can add user data to a sync job as an account information instance or as a data bundle:

-   To add account information to a sync job, create a new instance of the [Tizen.Account.AccountManager.Account](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.Account.html) class, add your account information into it, and then add it into the sync job as the `Account` property of the `Tizen.Account.SyncManager.SyncJobData` instance. For more information about creating accounts, see [Creating and Managing an Account](account.md#add).

    ```
    using Tizen.Account.AccountManager;

    AccountManager.Account account = AccountManager.Account.CreateAccount();
    account.UserName = "Kim";
    account.SyncState = AccountSyncState.Idle;
    AccountService.AddAccount(account);

    SyncJobData request = new SyncJobData();
    request.Account = account;
    ```

-   To add a data bundle to a sync job, create a new instance of the [Tizen.Applications.Bundle](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Bundle.html) class, add your data into it, and add it as the `UserData` property of the `Tizen.Account.SyncManager.SyncJobData` instance.

    ```
    using Tizen.Applications;

    Applications.Bundle bundle = new Applications.Bundle();
    bundle.AddItem("key", "value");

    SyncJobData request = new SyncJobData();
    request.UserData = bundle;
    ```

<a name="on_demand_sync"></a>
## Requesting an On-demand Sync Job

To request a one-time sync job from the Sync Adapter service application, use the `RequestOnDemandSyncJob()` method of the [Tizen.Account.SyncManager.SyncClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncClient.html) class:

```
SyncJobData request = new SyncJobData();
request.SyncJobName = "OnDemandSyncJob";
int id = SyncClient.RequestOnDemandSyncJob(request, SyncOption.NoRetry);
```

<a name="periodic_sync"></a>
## Requesting a Periodic Sync Job

To register a periodically-recurring sync operation with the Sync Adapter service application:

-   To set up a periodic sync job with a regular sync interval, use the `AddPeriodicSyncJob()` method of the [Tizen.Account.SyncManager.SyncClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncClient.html) class, and give the sync interval as a value of the [Tizen.Account.SyncManager.SyncPeriod](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncPeriod.html) enumeration. In the following example, the sync interval is set to 30 minutes:

    ```
    SyncJobData request = new SyncJobData();
    request.SyncJobName = "PeriodicSyncJob";
    int id = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.ThirtyMin, SyncOption.None);
    ```

    You can also add additional parameters to the sync job using values of the [Tizen.Account.SyncManager.SyncOption](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncOption.html) enumeration. The value `NoRetry` means that the application does not retry the sync job if it fails, and `Expedited` means that the sync job is handled as soon as possible.

    ```
    id = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.OneHour, SyncOption.NoRetry);
    id = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.OneDay, SyncOption.Expedited);
    ```

-   You can renew a previously registered periodic sync job with the `AddPeriodicSyncJob()` method by using the same [Tizen.Account.SyncManager.SyncJobData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncJobData.html) instance with new parameters:

    ```
    SyncJobData request = new SyncJobData();
    request.SyncJobName = "PeriodicSyncJob";
    int id = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.ThirtyMin, SyncOption.None);
    id = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.TwoHours, SyncOption.Expedited);
    ```

<a name="data_change_sync"></a>
## Defining a Data Change Sync Job

To register a data change sync job with the Sync Adapter service application, to occur whenever corresponding data changes:

-   Add a data change sync job with the `AddDataChangeSyncJob()` method of the [Tizen.Account.SyncManager.SyncClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncClient.html) class. This method adds the sync job only for the capability given as the value of the `SyncJobName` property of the [Tizen.Account.SyncManager.SyncJobData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncJobData.html) instance. For example, to add a data change sync job for the calendar:

    ```
    SyncJobData request = new SyncJobData();
    request.SyncJobName = SyncJobData.CalendarCapability;
    int id = SyncClient.AddDataChangeSyncJob(request, SyncOption.None);
    ```

    You can also add additional parameters to the sync job using values of the [Tizen.Account.SyncManager.SyncOption](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncOption.html) enumeration. The value `NoRetry` means that the application does not retry the sync job if it fails, and `Expedited` means that another sync job is handled as soon as possible.

    ```
    SyncJobData request2 = new SyncJobData();
    request2.SyncJobName = SyncJobData.ContactCapability;
    SyncJobData request3 = new SyncJobData();
    request3.SyncJobName = SyncJobData.ImageCapability;
    int id2 = SyncClient.AddDataChangeSyncJob(request2, SyncOption.NoRetry);
    int id3 = SyncClient.AddDataChangeSyncJob(request3, SyncOption.Expedited);
    ```

-   You can renew a previously registered data change sync job with the `AddDataChangeSyncJob()` method by using the same `Tizen.Account.SyncManager.SyncJobData` instance with new parameters:

    ```
    SyncJobData request = new SyncJobData();
    request.SyncJobName = SyncJobData.ContactCapability;
    int id = SyncClient.AddDataChangeSyncJob(request, SyncOption.Expedited);
    id = SyncClient.AddDataChangeSyncJob(request, SyncOption.None);
    ```

<a name="foreach_sync"></a>
## Retrieving All Registered Sync Jobs

To retrieve a list of all registered sync jobs, use the `GetAllSyncJobs()` method of the [Tizen.Account.SyncManager.SyncClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncClient.html) class:

```
SyncJobData request = new SyncJobData()
{
    SyncJobName = "PeriodicSyncJob"
};
int periodicId = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.ThreeHours, SyncOption.None);

SyncJobData request2 = new SyncJobData()
{
    SyncJobName = SyncJobData.MusicCapability
};
int dataChangeId = SyncClient.AddDataChangeSyncJob(request2, SyncOption.None);

IEnumerable<KeyValuePair<int, SyncJobData>> syncJobs = SyncClient.GetAllSyncJobs();
foreach (KeyValuePair<int, SyncJobData> item in syncJobs)
{
    if (item.Key == periodicId)
    {
        Console.WriteLine(item.Value.SyncJobName.ToString());
    }
    if (item.Key == datachangeId)
    {
        Console.WriteLine(item.Value.SyncJobName.ToString());
    }
}
```

<a name="remove_sync"></a>
## Removing Sync Jobs

To remove registered sync jobs, use the `RemoveSyncJob()` method of the [Tizen.Account.SyncManager.SyncClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.SyncManager.SyncClient.html) class, using the `id` property of the job to be removed:

```
SyncJobData request = new SyncJobData();
request.SyncJobName = "PeriodicSyncJob";

SyncJobData request2 = new SyncJobData();
request2.SyncJobName = SyncJobData.ImageCapability;

int id = SyncClient.AddPeriodicSyncJob(request, SyncPeriod.OneHour, SyncOption.Expedited);
int id2 = SyncClient.AddDataChangeSyncJob(request2, SyncOption.None);

SyncClient.RemoveSyncJob(id);
SyncClient.RemoveSyncJob(id2);
```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
