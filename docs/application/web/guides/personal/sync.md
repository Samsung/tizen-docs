# Data Synchronization

You can synchronize device data, such as contacts and calendar events, with the OMA DS server using the [OMA](http://openmobilealliance.org/) DS (Data Synchronization) 1.2 protocol.

This feature is supported in mobile applications only.

The main features of the Data Synchronization API include:

- Creating a sync profile   

  You can [create a profile](#creating-a-sync-profile), define the profile name, and provide other profile and operation information using the applicable interfaces.

  Tizen sets a limitation on the number of supported OMA DS profiles on the device. Before creating a new profile, you must check whether sync profile slots are available.

- Retrieving synchronization process information   

  After starting the synchronization process, you can [monitor the progress](#starting-and-monitoring-data-synchronization) of the operation.

> **Note**  
> As a prerequisite to synchronizing your device data with the server, you must create an OMA DS server account.

## Prerequisites

To use the [Data Synchronization](../../api/latest/device_api/mobile/tizen/datasync.html) API, the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/datasync"/>
```

## Creating a Sync Profile

To create a sync profile:

1. Check whether there are available profile slots on the device using the `getProfilesNum()` and `getMaxProfilesNum()` methods of the [DataSynchronizationManager](../../api/latest/device_api/mobile/tizen/datasync.html#DataSynchronizationManager) interface:

   ```
   var numMaxProfiles = tizen.datasync.getMaxProfilesNum();
   var numProfiles = tizen.datasync.getProfilesNum();
   ```

2. Create a sync profile. Use the [SyncInfo](../../api/latest/device_api/mobile/tizen/datasync.html#SyncInfo), [SyncServiceInfo](../../api/latest/device_api/mobile/tizen/datasync.html#SyncServiceInfo), and [SyncProfileInfo](../../api/latest/device_api/mobile/tizen/datasync.html#SyncProfileInfo) interfaces to provide sync profile and operation information:

   ```
   if ((numMaxProfiles <= 0) || (numProfiles < numMaxProfiles)) {
       var syncInfo = new tizen.SyncInfo('http://example.com/sync', 'myId', 'myPassword', 'MANUAL', 'TWO_WAY');
       var contactInfo = new tizen.SyncServiceInfo(true, 'CONTACT', 'serverContact');
       var eventInfo = new tizen.SyncServiceInfo(true, 'EVENT', 'serverEvent');
       var serviceInfo = [contactInfo, eventInfo];
       var profile = new tizen.SyncProfileInfo('MyProfile', syncInfo, serviceInfo);
   ```

3. To be able to use the created profile, add it to your device using the `add()` method of the [DataSynchronizationManager](../../api/latest/device_api/mobile/tizen/datasync.html#DataSynchronizationManager) interface:

   ```
       tizen.datasync.add(profile);
       var profileId = profile.profileId;
   }
   ```

## Starting and Monitoring Data Synchronization

After starting the synchronization process using the `startSync()` method of the `DataSynchronizationManager` interface, you can monitor the progress of the operation. Use the [SyncProgressCallback](../../api/latest/device_api/mobile/tizen/datasync.html#SyncProgressCallback) interface to define listeners for receiving notifications. After the synchronization is completed, you can retrieve statistics using the `getLastSyncStatistics()` method.

To start and monitor the data synchronization process:

1. Define the event handlers for the notifications using the `SyncProgressCallback` listener interface:

   ```
   var syncCallback = {
       onprogress: function(profileId, serviceType, isFromServer, totalPerType, syncedPerType) {
           console.log('Total: ' + totalPerType + ', synced: ' + syncedPerType + ' for the sync type: ' + serviceType);
       },
       onfailed: function(profileId, error) {
           console.log('Failed with id: ' + profileId + ', error name: ' + error.name);
       }
   };
   ```

2. Start the sync operation using the `startSync()` method, with the corresponding listener as a parameter:

   ```
   tizen.datasync.startSync(profileId, syncCallback);
   ```

## Related Information
* Dependencies   
  - Tizen 2.4 and Higher for Mobile
