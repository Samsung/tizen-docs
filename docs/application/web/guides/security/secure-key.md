# Secure Key Management

The key manager allows you to [control data access](#data-access-control) by securely storing in a central secure repository keys, certificates, and sensitive data related to users and their password-protected applications. Additionally, the key manager provides secure cryptographic operations for non-exportable keys without revealing the key values to clients. The central secure repository is protected by a password.

The Key Manager API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Key Manager API include:

- Saving data		

  You can [save data](#saving-data) to a repository, and define which applications are allowed to access and remove it.

- Getting data		

  You can [retrieve data](#getting-data) from a repository. You can access both data that you have added yourself, and data that another application has added and granted you permissions to access.

- Removing data		

  You can [remove data](#removing-data) from a repository. You can remove both data that you have added yourself, and data that another application has added and granted you permissions to remove.

## Data Access Control

With the key manager, you can control various security aspects of your application:

- Data store policy

  A client can specify simple access rules when storing data in the key manager:

  - Extractable or non-extractable    
    - Only for data tagged as extractable, the key manager returns the raw value of the data.
    - If data is tagged as non-extractable, the key manager does not return its raw value. In that case, the key manager provides secure cryptographic operations for non-exportable keys without revealing the key values to the clients.
  - Per key password    
    - All data in the key manager is protected by a user password.
    - A client can encrypt its data using their own password additionally.
    - If a client provides a password when storing data, the data is encrypted with the password. This password must be provided when getting the data from the key manager.

- Data access control

  By default, only the data owner can access the data. If the owner grants access to other applications, those applications can read or delete the data from the key manager database.

  When an application is deleted, the data and access control information granted by the application are also removed.

**Figure: Key manager process**

![Key manager process](./media/key_manager.png)

## Saving Data

To save data in a repository:

1. Save the data using the `saveData()` method:

   ```
   var data_name = 'data1', raw_data = 'my data';

   tizen.keymanager.saveData(data_name, raw_data, null, onSave);
   ```

2. To grant an application permission to remove the data, use the `setPermission()` method in the data saving callback.

    In this example, permission is granted for an application with the 9PdoiICQ4c ID:

   ```
   function onPermissionSet() {
       console.log('Successfully set permission');
   }

   function onSave() {
       /*
          Dictionary does not require a package ID because an
          application can only set permission for data which it saved
       */
       tizen.keymanager.setPermission({'name': data_name}, '9PdoiICQ4c',
                                      'READ_REMOVE', onPermissionSet);
   }
   ```

## Getting Data

To retrieve data from a repository:

- Retrieve data which your application has added:

  ```
  var data_name = 'data1', raw_data = 'my data';

  function onSave() {
      /*
         Dictionary does not require a package ID because the
         application calling getData() saved 'data1'
      */
      var app_data = tizen.keymanager.getData({'name': data_name});
      console.log('App data: ' + app_data + ' was retrieved');
  }

  tizen.keymanager.saveData(data_name, raw_data, null, onSave);
  ```

- Retrieve data which another application has saved, and granted permission for you to access.

  The following example assumes that the application that created `aliases[0]` also gave your application permission to read it:

  ```
  var aliases = tizen.keymanager.getDataAliasList();

  if (aliases.length != 0) {
      /*
         Assuming that the application calling getData()
         has permission to read aliases[0]
      */
      var app_data = tizen.keymanager.getData(aliases[0]);
      console.log('App data: ' + app_data + ' was retrieved');
  }
  ```

## Removing Data

To remove data from a repository:

1. Remove data which your application has added:

   ```
   var data_name = 'data1', raw_data = 'my data';

   function onSave() {
       /* Do something */

       /*
          Dictionary does not require a package ID because the
          application calling removeData() saved 'data1'
       */
       tizen.keymanager.removeData({'name': data_name});
   }

   tizen.keymanager.saveData(data_name, raw_data, null, onSave);
   ```

2. Remove data which another application has saved, and granted permission for you to remove.

   The following example assumes that the application that created `aliases[0]` also gave your application permission to remove it:

   ```
   var aliases = tizen.keymanager.getDataAliasList();

   if (aliases.length != 0) {
       /*
          Assuming that the application calling removeData()
          has permission to remove aliases[0]
       */
       var app_data = tizen.keymanager.removeData(aliases[0]);
   }
   ```

## Related Information
* Dependencies   
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
