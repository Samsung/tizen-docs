# Application Usage History Data


You can retrieve the user's application usage patterns, such as information about frequently used applications.

The main features of the Tizen.Context.AppHistory namespace are:

-   Retrieving application usage statistics

    You can [retrieve application launch history](#retrieve_usage_stats), such as frequently used applications and recently used applications, using the [Tizen.Context.AppHistory.UsageStatistics](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.UsageStatisticsData.html) class.

-   Retrieving battery usage statistics

    You can [retrieve battery usage statistics](#retrieve_battery_stats), using the [Tizen.Context.AppHistory.BatteryStatistics](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.BatteryStatistics.html) class.

## Prerequisites


To enable your application to use the application usage history data functionality:

1.  To use the [Tizen.Context.AppHistory](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/apphistory.read</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Context.AppHistory namespace, include it in your application:

    ```
    using Tizen.Context.AppHistory;
    ```

<a name="retrieve_usage_stats"></a>
## Retrieving Application Usage Statistics

To retrieve application usage statistics for a given time period, and check detailed statistics information, such as duration, launch count, and last launch time of the used applications:

1.  To retrieve the application launch history, create a usage statistics instance:
    -   To use the default `LaunchCountMost` sort order, create a new instance of the [Tizen.Context.AppHistory.UsageStatistics](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.UsageStatistics.html) class without specifying the `sortOrder` parameter:

        ```
        UsageStatistics frequentlyUsedApp = new UsageStatistics();
        ```

    -   To use another sort order for your usage statistics instance, add the `sortOrder` parameter to the `Tizen.Context.AppHistory.UsageStatistics` class constructor, using values of the [Tizen.Context.AppHistory.UsageStatistics.SortOrderType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.UsageStatistics.SortOrderType.html) enumeration:

        ```
        UsageStatistics recentlyUsedApp = new UsageStatistics(UsageStatistics.SortOrderType.LastLaunchTimeNewest);
        ```

2.  To get information about the most frequently used applications for a given time period, use the `Query()` method of the `Tizen.Context.AppHistory.UsageStatistics` class:
    -   To retrieve a list of frequently used applications for a given time period, specify the `startTime` and the `endTime` parameters to determine the time period.

        For example, to retrieve a list of the most frequently used applications for the last 2 weeks:

        ```
        IReadOnlyList<UsageStatisticsData> frequentlyUsedAppList = frequentlyUsedApp.Query(DateTime.Now.AddDays(-14), DateTime.Now);
        ```

    -   By default, the query returns a maximum of 10 results. You can change the number of returned results by setting the `resultSize` parameter.

        For example, to retrieve a list of 5 most frequently used applications for the last 2 weeks:

        ```
        IReadOnlyList<UsageStatisticsData> frequentlyUsedAppList = frequentlyUsedApp.Query(DateTime.Now.AddDays(-14), DateTime.Now, 5);
        ```

    -   The query returns a sorted list of [Tizen.Context.AppHistory.UsageStatisticsData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.UsageStatisticsData.html) class instances. To enumerate the list:

        ```
        foreach(var record in frequentlyUsedAppList)
        {
            Log.Info(LOGTAG, "AppId: " + record.AppId);
            Log.Info(LOGTAG, "Duration: " + record.Duration);
            Log.Info(LOGTAG, "LaunchCount: " + record.LaunchCount);
            Log.Info(LOGTAG, "LastLaunchTime: " + record.LastLaunchTime);
        }
        ```

<a name="retrieve_battery_stats"></a>		
## Retrieving Battery Usage Statistics

To retrieve battery usage statistics for a given time period, and check detailed statistics information, such as the battery consumption of the used applications:

1.  To retrieve the battery consumption per application, create an instance of the [Tizen.Context.AppHistory.BatteryStatistics](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.BatteryStatistics.html) class:

    ```
    BatteryStatistics batteryConsumedApp = new BatteryStatistics(BatteryStatistics.SortOrderType.ConsumptionMost);
    ```

2.  To get the information about the application battery consumption, use the `Query()` method of the `Tizen.Context.AppHistory.BatteryStatistics` class.

    For example, to retrieve battery consumption history since the device was last fully charged, use a `DateTime` instance returned by the `GetLastFullyChargedTime()` method as the `startTime` parameter of the `Query()` method:

    ```
    DateTime time = BatteryStatistics.GetLastFullyChargedTime();
    IReadOnlyList<BatteryStatisticsData> batteryConsumedAppList = batteryConsumedApp.Query(time, DateTime.Now, 5);
    ```

3.  The `Query()` method returns a sorted list of [Tizen.Context.AppHistory.BatteryStatisticsData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Context.AppHistory.BatteryStatisticsData.html) class instances. To enumerate the list:

    ```
    foreach(var record in batteryConsumedAppList)
    {
        Log.Info(LOGTAG, "AppId: " + record.AppId);
        Log.Info(LOGTAG, "Consumption: " + record.Consumption);
    }
    ```

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
