# Get HERE Maps Credentials


The HERE Maps plug-in for the Maps Service API is based on the HERE Maps services. It is provided as an example in the Tizen platform, and to use it on the HERE Maps, you need credentials for it.

You can select HERE plans depending on the number of request queries and the kind of supported features you need, and pay for them accordingly. The following instructions provide a summary of how to get new credentials. For more information, see [HERE developers](https://developer.here.com){:target="_blank"}.

To get credentials, follow these steps:

1.  Go to the [HERE Developers](https://developer.here.com){:target="_blank"} website and sign in.

    If you have no account, first register for the HERE Maps account.

2.  Select a plan for using the HERE Maps services, and register a new project.

    You can select between various [public or business plans](https://developer.here.com/plans){:target="_blank"}. Signing up for a plan automatically registers a new project.

    1.  Select the plan that meets your requirements for the number of transactions you need and click **Sign up**.
    2.  Provide your contact details and agree to the terms and conditions.

        > [!NOTE]
		> The registration does not support some regions and countries. If your contact details contain such a region or country, you cannot register a new application.


3.  Generate the credentials.

    To access the new project, select **Projects** in the drop-down menu next to your username in the upper-right corner of the screen, and click the project in the project list.

    To generate the credentials, click **Generate App ID and App Code**.

4.  Use the credentials in your application.

    You can use the credentials in your application with the [Tizen.Maps.MapService](/application/dotnet/api/TizenFX/latest/api/Tizen.Maps.MapService.html) class.

    The HERE Maps services provide 2 values as credentials: app ID and app code. If the app ID is `XXXX` and the app code is `YYYY`, concatenate them with the "/" separator:

    ```csharp
    var maps = new MapService("HERE", "XXXX/YYYY");
    ```

    > [!NOTE]
	> According to the HERE Maps:
    > -   The app ID uniquely identifies your application.
    > -   The app code is used in the authentication process to identify a session.


## Related information
* Dependencies
  -   Tizen 4.0 and Higher
