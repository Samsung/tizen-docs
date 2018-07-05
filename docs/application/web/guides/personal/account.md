# Account Management

You can access user accounts and account providers. After getting a specific account, you can manage it, retrieve account information, and monitor changes in it. You can use existing configured on-line accounts and providers, and create new accounts of known types.

This feature is supported in mobile and wearable applications only.

The main features of the Account API include:

- Accessing accounts

  You can [get a specific account or all available accounts](#retrieving-accounts).

- Accessing account providers

  You can [get a specific provider or all available providers](#retrieving-providers).

- Managing accounts

  You can [add, update, and remove accounts](#managing-accounts).

- Monitoring account changes

  You can [register a listener](#receiving-notifications-on-account-changes) and track changes in the account database.

- Managing extended data

  You can [set and get extended data](#managing-extended-account-data) for an account. The extended data is defined as key-value pairs.

To understand account management, you must be familiar with the following basic concepts:

- Provider

  An on-line service provider entity, such as Google, Vodafone, or Facebook. A service provider is identified by its application ID. The account provider is registered while the application is installed. The information is used in the **Add account** screen in the device settings.

- Account

  An entity that collects all the data (such as user name, credentials, settings) needed for connecting to services. An account is always bound to a single provider and has a list of service instances bound to the account. The services can be individually enabled and disabled on the given account. For instance, "`Laccount1@gmail.com`" can identify a Google account, giving access to services, such as Gmail, Picasa, and Youtube, with each service having a separate service instance bound to the account.

## Prerequisites

To enable your application to use the account functionality:

1. To make your application visible in the Tizen Store only for devices that support the account feature, the application must specify the following feature in the `config.xml` file:

   ```
   <widget>
      <tizen:feature name="http://tizen.org/feature/account"/>
   </widget>
   ```

   Additionally, to double-check the Account API support (in [mobile](../../api/latest/device_api/mobile/tizen/account.html) and [wearable](../../api/latest/device_api/wearable/tizen/account.html) applications) while the application is running, use the `tizen.systeminfo.getCapability()` method and enable or disable the code that needs the API, as needed.

2. To use the Account API, the application has to request permission by adding the following privileges to the `config.xml` file:

   ```
   <tizen:privilege name="http://tizen.org/privilege/account.read"/>
   <tizen:privilege name="http://tizen.org/privilege/account.write"/>
   ```

3. Some of the account management features can be invoked only in account provider applications. If you are creating an account provider application, pay attention to the following requirements:

   - Account provider applications must have a specially prepared `config.xml` file with an account provider section:

     ```
     <tizen:account multiple-account-support="true">
        <tizen:icon section="Account">icon.png</tizen:icon> <!--In mobile applications only-->
        <tizen:icon section="AccountSmall">icon.png</tizen:icon> <!--In mobile applications only-->
        <tizen:display-name xml:lang="en-gb">Test</tizen:display-name>
        <tizen:capability>http://tizen.org/account/capability/contact</tizen:capability>
     </tizen:account>
     ```

   - If the application is registered as a provider, it is launched to authenticate the account. You must implement an application control to allow the account provider to be launched through the application control request.

   - The following methods are available only in an account provider application: `add()`, `remove()`, and `update()`.

   - The account provider application declares the account capabilities. The capability name is decided by the author of the account provider application, and must have an IRI form. For example:

     - `http://tizen.org/account/capability/contact` is used when the account is related to contacts.
     - `http://tizen.org/account/capability/calendar` is used when the account is related to the calendar.

## Retrieving Accounts

Learning how to retrieve account information enables you to include account support into your applications:

- To retrieve information about all available accounts, use the `getAccounts()` method of the `AccountManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#AccountManager) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#AccountManager) applications):

  ```
  function getAccountsSuccess(accounts) {
      for (var i = 0; i < accounts.length; i++) {
          /* Use the retrieved accounts */
      }
  }
  function getAccountsError(error) {
      console.log('Error: ' + error.message);
  }
  tizen.account.getAccounts(getAccountsSuccess, getAccountsError);
  ```

- If you already know the ID of the account, you can get the `Account` object (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#Account) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#Account) applications) using the `getAccount()` method of the `AccountManager` interface:

  ```
  var account = tizen.account.getAccount(my_account_id);
  ```

## Retrieving Providers

To create accounts, you must learn how to get access to account providers:

- Get a specific account provider with the given application ID using the `getProviders()` method of the `ApplicationManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationManager) and [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationManager) applications).  
  If the current application is an account provider application (meaning that it contains the `<tizen:account>` element, in [mobile](../../../tizen-studio/web-tools/config-editor.md#mw_account) and [wearable](../../../tizen-studio/web-tools/config-editor.md#ww_account) applications, in its `config.xml` file), you can use the current application ID.  Otherwise, get the ID of the current application using the `getCurrentApplication()` method of the `ApplicationManager` interface:

  ```
  var appId = tizen.application.getCurrentApplication().appInfo.id;
  var provider = tizen.account.getProvider(appId);
  ```

- To get information about all available account providers, use the `getProviders()` method of the `AccountManager` interface:

  ```
  function getProvidersSuccess(providers) {
      /* Providers is an array whose members are providers with contact capability */
  }
  function getProvidersError(error) {
      console.log('Error: ' + error.message);
  }

  tizen.account.getProviders(getProvidersSuccess, getProvidersError, 'http://tizen.org/account/capability/contact');
  ```

## Managing Accounts

Creating, adding, updating, and deleting accounts is a basic account management skill:

> **Note**  
> To perform these operations, your application must be the account provider.

1. To create an account, first get an account provider. If your application is an account provider application (meaning that it contains the `<tizen:account>` element, in [mobile](../../../tizen-studio/web-tools/config-editor.md#mw_account) and [wearable](../../../tizen-studio/web-tools/config-editor.md#mw_account) applications, in its `config.xml` file), use the `getProvider()` method:

   ```
   var appId = tizen.application.getCurrentApplication().appInfo.id;
   var accountProvider = tizen.account.getProvider(appId);
   ```

2. Create an instance of the `Account` interface (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#Account) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#Account) applications):

   ```
   var account = new tizen.Account(accountProvider, {userName: 'admin', iconUri: 'path/to/icon.jpg'});
   ```

3. Add the account to the account database:

   ```
   tizen.account.add(account);
   ```

4. To update the account information, change the attributes of the `Account` object for the relevant account:

   ```
   account.userName = 'new username';
   ```

5. To save the changed values, use the `update()` method of the `AccountManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#AccountManager) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#AccountManager) applications):

   ```
   tizen.account.update(account);
   ```

6. To remove the account from the system, use the `remove()` method of  the `AccountManager` interface, providing the account ID:

   ```
   tizen.account.remove(account.id);
   ```

## Receiving Notifications on Account Changes

Learning how to register change listeners enables you to synchronize the view of your application with the changes in the account database:

1. Define a listener implementing the `AccountChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#AccountChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#AccountChangeCallback) applications):

   ```
   var accountChangeListener = {
       onadded: function(account) {
           /* Called when an account is added */
       },
       onremoved: function(accountId) {
           /* Called when an account is removed */
       },
       onupdated: function(account) {
           /* Called when a registered account is changed */
       }
   };
   ```

2. Register the account listener using the `addAccountListener()` method of the `AccountManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#AccountManager) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#AccountManager) applications) to start receiving notifications about changes:

   ```
   var watchId = tizen.account.addAccountListener(accountChangeListener);
   ```

3. When notifications are no longer required, deregister the listener using the `removeAccountListener()` method of the `AccountManager` interface:

   ```
   tizen.account.removeAccountListener(watchId);
   ```

## Managing Extended Account Data

Learning how to manage extended data for an account enables you to include account support into your applications:

1. [Retrieve the account object](#retrieving-accounts).

2. Manage the extended data for the retrieved account:

   - To set extended data:

     Set the additional information with the `setExtendedData()` method:

     ```
     var key = 'nickname';
     var value = 'nickname of anonymous user';
     account.setExtendedData(key, value);
     ```

     To overwrite the previous data value, set a new value with the same key:

     ```
     account.setExtendedData(key, 'nickname updated');
     ```

   - To get extended data:

     - To retrieve extended data value for a specific key, use the `getExtendedData()` method:
       ```
       var key = 'accessToken';
       var value = account.getExtendedData(key);
       ```

     - To retrieve all extended data for an account, use the asynchronous version of the `getExtendedData()` method. The success callback contains an array of the extended data key-value pairs.

       ```
       account.getExtendedData(function(extendedData) {
           for (var i = 0; i < extendedData.length; i++) {
               var key = extendedData.key;
               var value = extendedData.value;
               console.log(key + ': ' + value);
           }
       }, function(e) {
           console.log('Error: ' + e.message);
       });
       ```

## Related Information
* Dependencies       
  - Tizen 2.4 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
