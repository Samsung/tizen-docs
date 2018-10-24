# Account Management


An account is a collection of information representing the user of a specific provider. You can manage accounts and their details in your application.

The main features of the Tizen.Account.AccountManager namespace include:

-   Creating and managing accounts

    You can [create an account](#add), set its properties, and insert it to the database.

    You can also [manage the account secrecy level](#secret) and [remove accounts](#remove).

- Retrieving account information

    You can [retrieve information for each existing account](#get) and implement an event handler.

    You can also get accounts based on a [specific account provider package name](#retrieve), or account providers based on a [specific capability](#capability).

- Receiving account change notifications
- Modifying account properties

    You can [query the account details](#queries) with database queries, [retrieve the account type](#type), and [update the account information](#update). For a list of modifiable account properties, see [Account and Account Provider Properties](#account_and_provider_properties).

> **Note**
>
> Account providers, such as Google and Facebook, represent specific service provider-related information or protocol that provides the user accounts. To add, update, or remove an account, you must register a specific account provider for all your applications belonging to the same package.  
>
> To register an account provider, define the [account provider information](#provider_prop) in the `Account` tab of the manifest editor, and implement the account application control.
>
> If the application has defined the account provider information and implements the [appcontrol for the account provider](#appcontrol), the account provider is automatically registered when the application is installed.

<a name="appcontrol"></a>
## Account Application Control

The account application control, which allows the user to add and configure accounts, must be implemented in all applications that define an account provider. You are not required to define the application control information in the **Application Control** tab of the manifest editor to add the application on the Account screen.

This application control supports the `http://tizen.org/appcontrol/operation/account/add` and `http://tizen.org/appcontrol/operation/account/configure` operations.

<a name="signin"></a>
### ACCOUNT OPERATION SIGNIN Operation

The `http://tizen.org/appcontrol/operation/account/add` operation enables the user to add a new account for a specific account provider.

With the operation, the login page for the specific account provider can be displayed. In **Settings &gt; Accounts**, if the account provider is clicked for adding a new account, this operation is launched.

**Table: ACCOUNT OPERATION SIGNIN operation**

| Operation                                | Description                      |
|----------------------------------------|--------------------------------|
| `http://tizen.org/appcontrol/operation/account/add` | Account ID of the added account. |

  <a name="CONFIG"></a>
### ACCOUNT OPERATION VIEW Operation

The `http://tizen.org/appcontrol/operation/account/configure` operation enables the user to set account information, such as synchronization settings. The delete button must be included for removing accounts.

In **Settings &gt; Accounts**, if the specific account is clicked for setting the account information, this operation is launched.

**Table: ACCOUNT OPERATION VIEW operation**

| Operation                                | Description                              |
|----------------------------------------|----------------------------------------|
| `http://tizen.org/appcontrol/operation/account/configure` | Account ID for setting account information. |

## Prerequisites


To enable your application to use the account management functionality:

1.  To use the [Tizen.Account.AccountManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/account.read</privilege>
       <privilege>http://tizen.org/privilege/account.write</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Account.AccountManager namespace, include it in your application:

    ```
    using Tizen.Account.AccountManager;
    ```

    <a name="add"></a>
## Creating and Managing an Account

To create an account, set its properties, and add it to the account database:

1.  Create an account using the `CreateAccount()` method of the [Tizen.Account.AccountManager.Account](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.Account.html) class:

    ```
    Account account = Account.CreateAccount();
    ```

2. When the account is created, you can set account properties, such as name, display name, domain name, and email ID:

    ```
    string userName = "Marcus";
    string displayName = "Marcus_display";
    string domainName = "Marcus_domain";
    string emailId = "marcus@example.com";
    string iconPath = "image_path";

    account.UserName = userName;
    account.DisplayName = displayName;
    account.DomainName = domainName;
    account.EmailId = emailId
    account.IconPath = iconPath;
    ```

3. When the account properties are set, use the `AddAccount()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class to insert the account into the account database:

    ```
    int account_id = AccountService.AddAccount(account);
    ```

    The method returns the account ID (`account_id`) of the newly inserted account.

    <a name="get"></a>
## Getting Account Information

To get account information, such as user name, display name, domain name, and email ID:

1.  Use the `GetAccountsCount()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class to get the total number of records in the account database.

    To get individual records, use the `GetAccountsAsync()` method, which iterates through all the records and invokes an event handler for each account.

    ```
    int total_count = AccountService.GetAccountsCount();
    IEnumerable<Account> accounts = AccountService.GetAccountsAsync();
    ```

2. To get more details, use the `AccountId`, `UserName`, `DisplayName`, and `IconPath` properties of the [Tizen.Account.AccountManager.Account](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.Account.html) class instance returned in the event handler:

    ```
    Account account = Account.CreateAccount();

    /// Get the account ID
    var id = account.AccountId;
    Console.WriteLine("Account ID: {0}", id);

    /// Get the user name
    string userName = account.UserName;
    Console.WriteLine("User Name: {0}", userName);

    /// Get the display name
    string display = account.DisplayName;
    Console.WriteLine("Display Name: {0}", display);

    /// Get the icon path
    string iconPath = account.IconPath;
    Console.WriteLine("Icon Path: {0}", iconPath);
    ```

<a name="retrieve"></a>
## Retrieving Accounts by Package Name

To retrieve accounts by a specific account provider, use the `GetAccountsByPackageName()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class with the package name of the account provider:

```
IEnumerable<Account> accounts = null;
string packageName = "packageName";
accounts = AccountService.GetAccountsByPackageName(packageName);
```

<a name="capability"></a>
## Retrieving Account Providers by Capability

To retrieve account providers by a specific capability, use the `GetAccountProvidersByFeature()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class:

```
string capability = "http://tizen.org/account/capability/contact";
IEnumerable<AccountProvider> providers = AccountService.GetAccountProvidersByFeature(capability);
```

<a name="remove"></a>
## Removing an Account

Accounts to be removed can be identified by the account ID, user name, package name.

To remove an account, use the `DeleteAccount()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class:

-   Remove an account using an account ID:

    ```
    Account account = Account.CreateAccount();
    var id = account.AccountId;
    AccountService.DeleteAccount(account);
    ```

- Remove an account using a user name:

    ```
    string userName = "user_name";
    string packageName = "packageName";
    AccountService.DeleteAccount(userName, packageName);
    ```

- Remove an account using a package name:

    ```
    string packageName = "packageName";
    AccountService.DeleteAccount(packageName);
    ```

<a name="queries"></a>
## Performing Database Queries

To perform database queries:

1.  Prepare sample content.

    To perform queries, you need existing content in the database. To access an existing account, obtain it from the database. This can be done using a few different methods, depending on the user requirements.

    To create new content and add it to the database:

    1.  The `Create_Account()` method takes a new [Tizen.Account.AccountManager.Account](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.Account.html) instance and gives it some account details (name, display name, domain, email):

        ```
        void Create_Account(Account account, string userName, string displayName, string domainName, string emailId)
        {
            account.UserName = userName;
            account.DisplayName = displayName;
            account.domainName = domainName;
            account.EmailId = emailId;
        }
        ```

        3 capabilities are added to the account to demonstrate some of the query functions. The capabilities as well as user custom types can be predefined.

        After the account is created, it is added to the database.

        ```
        Account account = Account.CreateAccount();

        Create_Account(account, "Person", "DisplayPerson", "Person Domain", "someone1@somewho.com");

        account.SetCapability("Custom", CapabilityState.Enabled);
        account.SetCapability("Next", CapabilityState.Enabled);
        account.SetCapability("Another", CapabilityState.Disabled);

        AccountService.AddAccount(account);
        ```

    2. Add 2 more accounts to the database:

        ```
        Create_Account(account, "Human", "Humanity", "Everyone", "someone3@somewho.com");
        AccountService.AddAccount(account);

        Create_Account(account, "LastOne", "LastDisplay", "Last Domain", "someone4@somewho.com");
        AccountService.AddAccount(account);
        ```

2. Get the accounts:

    Get all accounts to verify the database insertion:

    ```
    IEnumerable<Account> accounts = AccountService.GetAccountsAsync();
    ```

3. Query the account by various attributes:
    -   Query by the ID:

        ```
        IEnumerable<Account> accounts = null;
        List<int> values = new List<int>();
        foreach (int i in values)
        {
            accounts = AccountService.GetAccountById(i);
        }
        ```

    - Query by user name.

        Querying data by user name requires a valid user name.

        ```
        IEnumerable<Account> accounts = null;
        string userName = "Human";
        accounts = AccountService.GetAccountsByUserName(userName);
        ```

    - Query by package name.

        By default, the accounts created in the application context have a package name set to the application name. Change it using the `PackageName` property of the [Tizen.Account.AccountManager.Account](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.Account.html) instance. To list accounts by package name, the user can provide a name by themselves or obtain it through the `PackageName` property.

        ```
        IEnumerable<Account> accounts = null;
        Account account = Account.CreateAccount();
        string packageName = account.PackageName;
        accounts = AccountService.GetAccountsByPackageName(packageName);
        ```

    - Query by capability.

        The `GetAccountsByCapabilityType()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class allows the user to find all accounts with a specified capability type.

        ```
        IEnumerable<Account> accounts = null;
        accounts = AccountService.GetAccountsByCapabilityType("Custom");
        ```

    - Query capability by account ID.

        The `GetCapabilitiesById()` method is different from the previous methods. It returns all capabilities from an account with a specified ID.

        ```
        Dictionary<string, CapabilityState> newcapabilities = AccountService.GetCapabilitiesById(account.AccountId);
        ```

4. Destroy all account instances when they are no longer needed:

    ```
    account.Dispose();
    ```

    <a name="secret"></a>
## Managing Account Secrecy

To manage account secrecy:

1.  The secrecy state of an account is set and fetched using the `SecrecyState` property of the [Tizen.Account.AccountManager.Account](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.Account.html) class, which uses values from the [Tizen.Account.AccountManager.AccountSecrecyState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountSecrecyState.html) enumeration:

    ```
    int account1_id = 0, account2_id = 0, account3_id = 0;
    Account account = Account.CreateAccount();

    /// Account 1
    Create_Account(account, "Security 1", "Invalid", "NOBODY", "anony@mous.not");
    account.SecrecyState = AccountSecrecyState.InvalidState;
    id = AccountService.AddAccount(account);

    /// Account 2
    Create_Account(account, "Security 2", "Invisible", " NOBODY", "anony1@mous.not");
    account.SecrecyState = AccountSecrecyState.Invisible;
    id = AccountService.AddAccount(account);

    /// Account 3
    Create_Account(account, "Secret 3", "Visible", " NOBODY", "anony2@mous.not");
    account.SecrecyState = AccountSecrecyState.Visible;
    id = AccountService.AddAccount(account);

    List_Accounts(NULL);
    ```

    Secrecy is only linked with the visibility on the account settings screen. The account is still visible and can be accessed using a query or a `foreach` method.

    ```
    /// List_Account() console output
    My ID: 12
    My Name: Security 1
    My Disp.: Invalid
    -------------------
    My ID: 13
    My Name: Security 2
    My Disp.: Invisible
    -------------------
    My ID: 14
    My Name: Secret 3
    My Disp.: Visible
    ```

    <a name="update"></a>
## Updating Accounts

To update and track account data:

1.  Create the account event handler.

    If an event handler is registered and any action takes place on any account, the event handler provides in its parameters the event type as a string and the ID of the account associated with the actual change.

    ```
    handler = (object sender, AccountSubscriberEventArgs args) =>
    {
        Console.WriteLine("Callback Event Type: {0}, Account ID: {1}", args.EventType, args.accountId);
    };
    ```

    Register the event handler for the `AccountUpdated` event of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class:

    ```
    AccountService.AccountUpdated += handler;
    ```

2. Create an account:

    ```
    Account account = Account.CreateAccount();
    Create_Account(account, "Updater", "Updated?", "ToUpdate", "not.up@to.date");
    AccountService.AddAccount(account);
    ```

3. Update the account:

    1.  Get the account from the database based on its ID.
    2.  Make the necessary changes.
    3.  Update the account using the valid ID.

    ```
    Account account = AccountService.GetAccountById(id);
    account.DisplayName = "Updated!";
    AccountService.UpdateAccount(account);
    ```

4. Show the account to verify the updates:

    ```
    Account account = AccountService.GetAccountById(accountId);
    Show_Account(account);
    ```

5. When it is no longer needed, deregister the event handler:

    ```
    AccountService.AccountUpdated -= handler;
    ```

    <a name="type"></a>
## Retrieving Account Types

To retrieve account types:

-   Get the type information.

    If the account type with a specified ID exists, you can get it from the database with the `GetAccountProviderByAppId()` method of the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Account.AccountManager.AccountService.html) class.

    It is possible to set, for example:

    -   ID
    -   Labels
    -   Features
    -   Multiple account support (this is only a flag)

    To get the account types by the application ID, use the `GetAccountProviderByAppId()` method:

    ```
    string appId = "com.tizen.example"; /// App ID for retrieving account types
    AccountProvider provider = AccountService.GetAccountProviderByAppId(appId);

    if (provider.IsAppSupported(appId))
    {
        multipleAccountSupport = provider.MultipleAccountSupport;
        iconPath = provider.IconPath;
        features = AccountProvider.GetFeaturesByAppId(appId);
    }
    ```

- List the account types or all the labels from a specified type:

    ```
    IEnumerable<AccountProvider> accountProviders = AccountService.GetAccountProviders();
    Dictionary<string, string> labels = AccountProvider.GetLabelsByAppId(appId);
    ```

<a name="account_and_provider_properties"></a>
## Account and Account Provider Properties

The following table lists the account properties that can be modified.

**Table: Account properties**

| Account property    | Data type                          | Mandatory | Description                              |
|-------------------|----------------------------------|---------|----------------------------------------|
| User name           | String                           | Yes       | Identity of an account.<br>If the display name and email ID are not set for an account, the user name is shown for the account on the Accounts screen in the Setting application. |
| Display name        | String                           | No        | Display name of an account.<br>Display name is shown for the account on the Accounts screen in the Setting application. |
| Email ID            | String                           | No        | Email ID of an account.<br>If the display name is not set for an account, the email ID is shown for the account on the Accounts screen in the Setting application. |
| Package name        | String                           | No        | One of an account package IDs, like the app ID.<br>If the package name is not set for an account, the app ID is used as a package name. |
| Icon path           | String                           | No        | Icon path of an account.<br>The icon is shown through the registered icon path as an account icon on the Accounts screen in the Setting application. |
| Domain name         | String                           | No        | Domain name of an account.               |
| Access token        | String                           | No        | Access token of an account.              |
| Auth type           | Integer                          | No        | Authentication type, such as oauth or xauth. |
| Capability          | Key-value string-integer pairs | No        | Capability of an account.                |
| Secret              | Integer                          | No        | The secret value is used to decide whether the account is shown on the Accounts screen in the Setting application. |
| Sync support        | Integer                          | No        | Current synchronization status.          |
| Source              | String                           | No        | Source of an account.                    |
| User text           | String                           | No        | String array, which you can use freely.  |
| User int            | Integer                          | No        | Integer array, which you can use freely. |
| Custom              | Key-value string pairs           | No        | Key-value pairs, which you can use freely. |
| Safe account handle | SafeAccountHandle                | No        | Read-only account handle of an account.  |

The following table lists the properties that can be defined for each account provider.

<a name="provider_prop"></a>
**Table: Account provider properties**

| Account property          | Data type | Mandatory | Description                              |
|-------------------------|---------|---------|----------------------------------------|
| Multiple accounts support | bool    | Yes       | Indicates whether multiple accounts are supported. |
| Icon                      | String  | Yes       | File path of the account provider icon.  <br>    The icon size is:<br> - 72 x 72 for Xhigh (HD) <br> - 48 x 48 for High (WVGA) <br> Since the icon is used in **Settings > Accounts**, place the icon in a shared directory. |
| Small icon                | String  | Yes       | File path of the account provider icon.    <br>  The icon size is:<br> - 45 x 45 for Xhigh (HD)<br> - 30 x 30 for High (WVGA)<br> Since the small icon is used in other applications, place the icon in a shared directory. |
| Display name              | String  | Yes       | Display name of the account provider.    |
| Capabilities              | String  | No        | Capability of the account provider.<br>       Capability can be a liaison between an account application and another application. If an account application registers a capability in the manifest file, other applications know that the account application has the capability. And if an account application gives an account a capability, other applications know that the account has the capability.<br> Several service-specific capabilities are defined for the [Tizen.Account.AccountManager.AccountService](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Account_1_1AccountManager_1_1AccountService.html) class:<br>- Contact capability:<br>    `ContactCapability` or `"http://tizen.org/account/capability/contact"`<br>If you register this capability in the manifest file, the user using the contact application can see a list of accounts with the account of your service in the contact application. <br>-Calendar capability:<br>	    `CalendarCapability` or `"http://tizen.org/account/capability/calendar"`<br>If you register this capability in the manifest file, the user using the calendar application can see a list of accounts with the account of your service in the calendar application.<br>-Email capability:<br>	    `EmailCapability` or `"http://tizen.org/account/capability/email"`<br>-Photo capability:<br>	    `PhotoCapability` or `"http://tizen.org/account/capability/photo"`<br>-Video capability:<br>	    `VideoCapability` or `"http://tizen.org/account/capability/video"`<br>-Music capability:<br>	    `MusicCapability` or `"http://tizen.org/account/capability/music" ` <br>-Document capability:<br>	    `DocumentCapability` or `"http://tizen.org/account/capability/document"` <br>-Message capability:<br>	    `MessageCapability` or `"http://tizen.org/account/capability/message"` <br>-Game capability:<br>	    `GameCapability` or `"http://tizen.org/account/capability/game"` |



## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
