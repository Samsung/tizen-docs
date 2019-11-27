# STC


STC means Smart Traffic Control. It provides extensible packet-level control services, including per-app data usage, total data quota, and background app's data saving. STC Library provides APIs fulfilling below mentioned features for application development.

This feature is supported in mobile, tv and wearable profile.

The main features of the STC API include:

- Retrieve Data Usage For System

  You can [retrieve network data consumed by system](#retrieve-data-usage-for-system).

- Retrieve Data Usage For Applications

  You can [retrieve network data consumed by applications](#retrieve-data-usage-for-applications).


> **Note**  
> You can test the STC functionality on a target device only. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the STC API:

1.  To use the [Tizen.Network.Stc](https://samsung.github.io/TizenFX/latest/api/Tizen.Network.Stc.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/network.get</privilege>
       <privilege>http://tizen.org/privilege/network.set</privilege>
       <privilege>http://tizen.org/privilege/network.profile</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Network.Stc namespace, include it in your application:

    ```
    using Tizen.Network.Stc;
    ```

## Retrieve Data Usage For System

To retrieve statistics about total network data consumed by system:

1. Create filter for retrieveing data usage:

    This filter will be passed as a function parameter in GetStatisticsAsync() API call.
    
   ```
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
   
2. Call `GetStatisticsAsync()` API.

   ```
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
      Assert.IsTrue(s_isStcSupported == false && e.InnerException.GetType() == typeof(NotSupportedException), "Invalid          NotSupportedException or TypeInitializationException");
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
   
## Retrieve Data Usage For Applications

To retrieve statistics about total network data consumed by applications:

1. Create filter for retrieveing data usage for applications:

   This filter will be passed as a function parameter in GetStatisticsAsync() API call.

   ```
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
   
2. Call `GetStatisticsAsync()` API.

   ```
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
      Assert.IsTrue(s_isStcSupported == false && e.InnerException.GetType() == typeof(NotSupportedException), "Invalid          NotSupportedException or TypeInitializationException");
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
* Dependencies
  -   Tizen 4.0 and Higher
