# Smart Traffic Control


Smart Traffic Control (STC) provides extensible packet-level control services, including per-app data usage, total data quota, and background app's data saving.

The main features of the Tizen.Network.Stc namespace include:

- Retrieve Data Usage for System

  You can [retrieve the network data consumed by the system](#retrieve-data-usage-for-system).

- Retrieve Data Usage for Applications

  You can [retrieve the network data consumed by the applications](#retrieve-data-usage-for-applications).


> **Note**  
>
> You can test the STC functionality on a target device only. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the STC functionality:

1.  To use the [Tizen.Network.Stc](/application/dotnet/api/TizenFX/latest/api/Tizen.Network.Stc.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <privilege>http://tizen.org/privilege/network.get</privilege>      
    </privileges>
    ```

2. To use the methods and properties of the `Tizen.Network.Stc` namespace, include it in your application:

    ```csharp
    using Tizen.Network.Stc;
    ```

## Retrieve Data Usage for System

To retrieve the statistics about total network data consumed by the system:

1. Create a filter for retrieving data usage:

    This filter will be passed as a method parameter in `GetStatisticsAsync()` call.
    
   ```csharp
   public static StatisticsFilter MakeFilter()
   {
      Tizen.Log.Info(Globals.LogTag, "StcSetup.MakeFilter");

      StatisticsFilter _filter = new StatisticsFilter
      {
         AppId = null,
         From = DateTime.Now.AddMonths(-1),
         To = DateTime.Now,
         InterfaceType = NetworkInterface.All,
         TimePeriod = TimePeriodType.Week
      };
     
      return _filter;
   }
   ```
   
2. Call the `GetStatisticsAsync()` method.

   ```csharp
   try
   {
      StatisticsFilter _filter = StcSetup.MakeFilter();
      Task<IEnumerable<NetworkStatistics>> _task = StcManager.GetStatisticsAsync(_filter);
      var _stats = await _task;
      await Task.Delay(1000);
      using (IEnumerator<NetworkStatistics> _iter = _stats.GetEnumerator())
      {
          _iter.MoveNext();
          
          /* Do the processing on received data */       
      }
   }
   catch (NotSupportedException)
   {
      Assert.IsTrue(s_isStcSupported == false, "Invalid NotSupportedException");
   }
   catch (TypeInitializationException e)
   {
      Assert.IsTrue(s_isStcSupported == false && e.InnerException.GetType() == typeof(NotSupportedException), "Invalid NotSupportedException or TypeInitializationException");
   }
   catch (NullReferenceException)
   {
      Log.Info(Globals.LogTag, "Inside NullReferenceException: 'stats' is null");
      Assert.True(true, "Inside NullReferenceException: 'stats' is null");
   }
   catch (Exception ex)
   {
      Assert.True(false, "Exception occurs. Msg : " + ex.ToString());
   }
   Log.Info(Globals.LogTag, "Successfully done");
    
   ```
   
## Retrieve Data Usage for Applications

To retrieve the statistics about total network data consumed by the applications:

1. Create a filter for retrieving the application data usage:

   This filter will be passed as a method parameter in `GetStatisticsAsync()` call.

   ```csharp
   public static StatisticsFilter MakeFilter()
   {
      Tizen.Log.Info(Globals.LogTag, "StcSetup.MakeFilter");

      StatisticsFilter _filter = new StatisticsFilter
      {
         AppId = "TOTAL_IPV4",
         From = DateTime.Now.AddMonths(-1),
         To = DateTime.Now,
         InterfaceType = NetworkInterface.All,
         TimePeriod = TimePeriodType.Week
      };
     
      return _filter;
   }
   ``` 
   
2. Call the `GetStatisticsAsync()` method.

   ```csharp
   try
   {
      StatisticsFilter _filter = StcSetup.MakeFilter();
      Task<IEnumerable<NetworkStatistics>> _task = StcManager.GetStatisticsAsync(_filter);
      var _stats = await _task;
      await Task.Delay(1000);
      using (IEnumerator<NetworkStatistics> _iter = _stats.GetEnumerator())
      {
          _iter.MoveNext();
          
          /* Do the processing on received data */       
      }
   }
   catch (NotSupportedException)
   {
      Assert.IsTrue(s_isStcSupported == false, "Invalid NotSupportedException");
   }
   catch (TypeInitializationException e)
   {
      Assert.IsTrue(s_isStcSupported == false && e.InnerException.GetType() == typeof(NotSupportedException), "Invalid NotSupportedException or TypeInitializationException");
   }
   catch (NullReferenceException)
   {
      Log.Info(Globals.LogTag, "Inside NullReferenceException: 'stats' is null");
      Assert.True(true, "Inside NullReferenceException: 'stats' is null");
   }
   catch (Exception ex)
   {
      Assert.True(false, "Exception occurs. Msg : " + ex.ToString());
   }
   Log.Info(Globals.LogTag, "Successfully done");
    
   ```
 
 ## Related Information
- Dependencies
  -   Tizen 5.5 and Higher
