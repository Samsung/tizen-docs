# Data Control

Data control allows you to read and modify data stored and provided by another application, and monitor changes in that data. The application storing and controlling the data is called a DataControl provider application. The application using the data is called a DataControl consumer application. A single DataControl provider can serve multiple DataControl consumers.

The Data Control API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main data control features are:

- Data storage as key-value pairs   

  You can [get, add, update, and remove values assigned to a key](#managing-data-in-key-value-pairs) using the `MappedDataControlConsumer` interface (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#MappedDataControlConsumer), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#MappedDataControlConsumer), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#MappedDataControlConsumer) applications).

- Complex data storage using a SQL-type database and queries   

  You can [select, insert, update, and remove data](#managing-sql-type-data) using the `SQLDataControlConsumer` interface (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#SQLDataControlConsumer), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#SQLDataControlConsumer), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#SQLDataControlConsumer) applications).

- Provider data change monitoring   

  You can [receive notifications](#monitoring-provider-data-changes) about changes in DataControl provider applications.

## Prerequisites

To use the Data Control API (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/datacontrol.consumer"/>

<!--To receive DataControl provider data change notifications-->
<tizen:privilege name="http://tizen.org/privilege/datasharing"/>
<tizen:privilege name="http://tizen.org/privilege/appmanager.launch"/>
```

## Managing Data in Key-value Pairs

Learning how to manage map-type data allows you to use key-value pairs exposed by a DataControl provider:

1. Retrieve the `MappedDataControlConsumer` object (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#MappedDataControlConsumer), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#MappedDataControlConsumer), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#MappedDataControlConsumer) applications) using the `getDataControlConsumer()` method of the `DataControlManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#DataControlManager), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#DataControlManager), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#DataControlManager) applications). This object allows accessing the key-value data stored by the DataControl provider.

   You need a running DataControl provider application, which uses the `"http://tizen.org/datacontrol/provider/DictionaryDataControlProvider"` provider ID.

   ```
   /* Get the map-type DataControlConsumerObject */
   try {
       var globalMappedConsumer = tizen.datacontrol.getDataControlConsumer('http://tizen.org/datacontrol/provider/DictionaryDataControlProvider', 'Dictionary', 'MAP');
   }
   ```

2. To meet the API requirement of using unique request identifiers, define a global variable, which is incremented every time a new request ID is needed. When the Data Control API responds to a request, it provides the request ID, which allows connecting the response with the specific request.

   ```
   var globalReqId = new Date().getTime() % 2e9;
   ```

3. Define a common success and error callback:

   ```
   function onRequestSuccess(id) {
       console.log('Request ' + id + ' - done');
   }

   function onRequestError(id, error) {
       console.log('error in request ' + id + ', message: ' + error.message);
   }
   ```

4. To manage key-value pairs:

   - To add a key-value pair, use the `addValue()` method of the `MappedDataControlConsumer`:

     ```
     try {
         /* Increase globalReqId for uniqueness */
         globalReqId++;
         globalMappedConsumer.addValue(globalReqId, 'tizen', 'Foo', onRequestSuccess, onRequestError);
     }
     ```

   - To retrieve values assigned to a key, use the `getValue()` method of the `MappedDataControlConsumer`:

     ```
     function onGetValueSuccess(values, id) {
         console.log('Values retrieved in request ' + id + ': ' + values.toString());
     }

     try {
         globalReqId++;
         globalMappedConsumer.getValue(globalReqId, 'tizen', onGetValueSuccess, onRequestError);
     }
     ```

   - To update a value assigned to a key, use the `updateValue()` method of the `MappedDataControlConsumer` interface:

     ```
     try {
         globalReqId++;
         globalMappedConsumer.updateValue(globalReqId, 'tizen', 'Foo', 'Bar', onRequestSuccess, onRequestError);
     }
     ```

   - To remove a key-value pair, use the `removeValue()` method of the `MappedDataControlConsumer` interface:

     ```
     try {
         globalReqId++;
         globalMappedConsumer.removeValue(globalReqId, 'tizen', 'Bar', onRequestSuccess, onRequestError);
     }
     ```

## Managing SQL-type Data

Learning how to manage SQL-type data allows you to use databases exposed by a DataControl provider:

1. To retrieve a `SQLDataControlConsumer` object (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#SQLDataControlConsumer), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#SQLDataControlConsumer), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#SQLDataControlConsumer) applications), use the `getDataControlConsumer()` method of the `DataControlManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#DataControlManager), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#DataControlManager), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#DataControlManager) applications). This object allows accessing the data stored by the DataControl provider.

   You need a running DataControl provider application, which uses the `"http://tizen.org/datacontrol/provider/DictionaryDataControlProvider"` provider ID.

   ```
   /* Get the SQL type DataControlConsumerObject */
   try {
       var globalSQLConsumer = tizen.datacontrol.getDataControlConsumer('http://tizen.org/datacontrol/provider/DictionaryDataControlProvider', 'Dictionary', 'SQL');
   }
   ```

2. To meet the API requirement of using unique request identifiers, define a global variable, which is incremented every time new request ID is needed. When the Data Control API responds to a request, it provides the request ID, which allows connecting the response with the specific request.

   ```
   var globalReqId = new Date().getTime() % 2e9;
   ```

3. Define a common success and error callback:

   ```
   function onRequestSuccess(id) {
       console.log('Request ' + id + ' - done');
   }

   function onRequestError(id, error) {
       console.log('error in request ' + id + ', message: ' + error.message);
   }
   ```

4. To manage the data:

   - To insert data, use the `insert()` method of the `SQLDataControlConsumer` interface:

     ```
     function onInsertSuccess(reqId, rowId) {
         console.log('request: ' + reqId + ' succeed - inserted row id:' + rowId);
     }

     try {
         var rowData = {
             columns: ['WORD', 'WORD_DESC'],
             values: ['\'tizen1\'', '\'tizen2\'']
         };
         /* Increases globalReqId for uniqueness */
         globalReqId++;
         globalSQLConsumer.insert(globalReqId, rowData, onInsertSuccess, onRequestError);
     }
     ```

   - To select data, use the `select()` method of the `SQLDataControlConsumer` interface:

     ```
     function onSelectSuccess(result, id) {
         var length = result.length, i, j;
         for (i = 0; i < length; i++) {
             console.log('==== Row ', i, ':');
             for (j = 0; j < result[i].columns.length; j++) {
                 console.log('column: ' + result[i].columns[j] + ', value: ' + result[i].values[j]);
             }
         }
     }

     try {
         var columns = ['WORD', 'WORD_DESC'];
         var order = 'WORD ASC';
         var page = null;
         var maxNumberPerPage = null;

         globalReqId++;
         globalSQLConsumer.select(globalReqId, columns, 'WORD=\'tizen1\'', onSelectSuccess,
                                  onRequestError, page, maxNumberPerPage, order);
     }
     ```

   - To update data, use the `update()` method of the `SQLDataControlConsumer` interface:

     ```
     try {
         var rowData = {
             columns: ['WORD', 'WORD_DESC'],
             values: ['\'tizen1\'', '\'Web apps platform!\'']
         };
         globalReqId++;
         globalSQLConsumer.update(globalReqId, rowData, 'WORD=\'tizen1\'', onRequestSuccess, onRequestError);
     }
     ```

   - To remove data, use the `remove()` method of the `SQLDataControlConsumer` interface:

     ```
     try {
         globalReqId++;
         globalSQLConsumer.remove(globalReqId, 'WORD=\'tizen1\'', onRequestSuccess, onRequestError);
     }
     ```

## Monitoring Provider Data Changes

Learning how to add a listener allows you to receive notifications about DataControl provider data changes:

1. To monitor changes in the DataControl provider data, you must retrieve a `SQLDataControlConsumer` object (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#SQLDataControlConsumer), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#SQLDataControlConsumer), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#SQLDataControlConsumer) applications) or a `MappedDataControlConsumer` object (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#MappedDataControlConsumer), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#MappedDataControlConsumer), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#MappedDataControlConsumer) applications). Retrieve the required object using the `getDataControlConsumer()` method of the `DataControlManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/datacontrol.html#DataControlManager), [wearable](../../api/latest/device_api/wearable/tizen/datacontrol.html#DataControlManager), and [TV](../../api/latest/device_api/tv/tizen/datacontrol.html#DataControlManager) applications).

   You need a running DataControl provider application, which uses the `"http://tizen.org/datacontrol/provider/DictionaryDataControlProvider"` provider ID.

   ```
   /* Get the map-type DataControlConsumerObject */
   try {
       var globalMappedConsumer = tizen.datacontrol.getDataControlConsumer('http://tizen.org/datacontrol/provider/DictionaryDataControlProvider', 'Dictionary', 'MAP');
   } catch (error) {
       console.log("The following error occurred: " +  error.name);
   }

   /* Get the SQL-type DataControlConsumerObject */
   try {
       var globalSQLConsumer = tizen.datacontrol.getDataControlConsumer('http://tizen.org/datacontrol/provider/DictionaryDataControlProvider', 'Dictionary', 'SQL');
   } catch (error) {
       console.log("The following error occurred: " +  error.name);
   }
   ```

2. Define a change callback, error callback, and needed variables:

   ```
   var SqlWatcherId = 0, MapWatcherId = 0;

   function dataChangeSuccessCallback(eventType, rowData) {
       console.log("Operation " + eventType + " was performed");
       console.log("Data changed:");
       for (var i = 0; i < rowData.columns.length; i++) {
           console.log("column " + rowData.columns[i] + " value " + rowData.values[i]);
       }
   }

   function errorCallback(error) {
       console.log("The following error occurred: " +  error.name);
   }
   ```

3. Register the listeners that trigger the change callback when the provider data changes:

   ```
   try {
       SqlWatcherId = globalSQLConsumer.addChangeListener(dataChangeSuccessCallback, errorCallback);
       console.log("SQL change listener has been added with watchId = " + SqlWatcherId);
   } catch (error) {
       console.log("The following error occurred: " +  error.name);
   }

   try {
       MapWatcherId = globalMappedConsumer.addChangeListener(dataChangeSuccessCallback, errorCallback);
       console.log("MAP change listener has been added with watchId = " + MapWatcherId);
   } catch (error) {
       console.log("The following error occurred: " +  error.name);
   }
   ```

4. When the notifications are no longer needed, stop them with the `removeChangeListener()` method:

   ```
   try {
       globalSQLConsumer.removeChangeListener(SqlWatcherId);
   } catch (error) {
       console.log("The following error occurred: " +  error.name);
   }

   try {
       globalMappedConsumer.removeChangeListener(MapWatcherId);
   } catch (error) {
       console.log("The following error occurred: " +  error.name);
   }
   ```

> **Note**  
> To monitor DataControl provider data changes, it is not enough to implement a listener in the DataControl consumer. You also need to implement the data change sending functionality in the DataControl provider.  
> The data sending implementation determines the actual change data returned to the DataControl consumer. For more information on the DataControl provider implementation, see [Monitoring Data Changes](../../../native/guides/app-management/data-control.md#monitoring-data-changes).

## Related information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.2 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
