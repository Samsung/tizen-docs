# Call History

You can access information about various telephony services for circuit-switched telephony and voice over IP (VoIP). You can browse the call history of a device, remove call history entries, and monitor changes.

This feature is supported in mobile applications only.

The main features of the Call History API include:

- Call history tracking   

  You can [search and store data about all incoming and outgoing calls](#searching-for-call-history-items) using the [CallHistory](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistory) interface. The retrieved data is displayed as a list using the [CallHistoryEntry](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistoryEntry) interface.

- Call history item deletion   

  You can manage the call history by [removing unnecessary call history items](#removing-call-history-items) using the `CallHistory` interface.

- Change monitoring   

  You can register event listeners to [monitor changes in the call history](#monitoring-the-call-history) using the [CallHistoryChangeCallback](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistoryChangeCallback) listener interface.

## Prerequisites

To use the [Call History](../../api/latest/device_api/mobile/tizen/callhistory.html) API, the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/callhistory.read"/>
<tizen:privilege name="http://tizen.org/privilege/callhistory.write"/>
```

## Searching for Call History Items

Learning how to retrieve call history items using different parameters allows you to view specific items in a specific order, making call history monitoring easy and convenient.

1. To retrieve call history items, use the `find(successCallback, errorCallback, filter, sortMode, limit, offset)` method of the [CallHistory](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistory) interface.  
  This method is asynchronous, and the result of the query is an array of [CallHistoryEntry](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistoryEntry) objects.

   ```
   tizen.callhistory.find(onSuccess, onError, ifilter, sortMode, 20, 10);
   ```

2. Use the `SuccessCallback` parameter of the `find()` method to define an event handler for the query result set.

   In the following code snippet, the found call history items are appended to the console log.

   ```
   function onSuccess(results) {
       console.log(results.length + ' call history item(s) found!');
       for (var i = 0; i < results.length; i++) {
           console.log(i + '. ' + results[i].toString());
           /* Process the CallHistoryEntry */
       }
   }
   ```

3. Use the `filter` parameter of the `find()` method to define a filter for the query result set. A filter with the `CallHistoryEntry` attributes is used to limit the results of the call history search.

   When searching for call history items, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#call-history-filter-attributes).

   You can define various filters:

   - The `AttributeFilter` type is used to search based on a single `CallHistoryEntry` attribute.

     For example, the following filters define that only cellular calls or calls where the remote party has the telephone number 123456789 are included in the query results:

     ```
     /* First filter example */
     var filter = new tizen.AttributeFilter('type', 'EXACTLY', 'TEL');

     /* Second filter example */
     var numberFilter = new tizen.AttributeFilter('remoteParties.remoteParty', 'EXACTLY', '123456789');
     ```

   - The `CompositeFilter` type represents a set of filters. The `UNION` type composite filter matches any object that is matched by any of its filters; the `INTERSECTION` type composite filter matches all objects that are matched by all its filters.

     For example, the following code snippet defines a set of filters that include in the query results only the video calls where the remote party has the telephone number 123456789 and the call has started during the year 2009 or 2011:

     ```
     /* Create the ranges for the time filter */
     var y2009Filter = new tizen.AttributeRangeFilter('startTime',
                                                      new Date(2009, 0, 1),
                                                      new Date(2010, 0, 1));
     var y2011Filter = new tizen.AttributeRangeFilter('startTime',
                                                      new Date(2011, 0, 1),
                                                      new Date(2012, 0, 1));

     /* Create a time filter */
     var dataFilter = new tizen.CompositeFilter('UNION',
                                                [y2009Filter, y2011Filter]);

     /* Create a video call filter */
     var tfilter = new tizen.AttributeFilter('features', 'EXACTLY', 'VIDEOCALL');

     /* Combine the filters into a set */
     var ifilter = new tizen.CompositeFilter('INTERSECTION', [numberFilter, dataFilter, tfilter]);
     ```

4. Use the `sortMode` parameter to [order the query result set](../data/data-filter.md#using-sorting-modes). If the parameter is undefined or set to `null`, the results are sorted by default in a descending order.

   In the following code snippet, the found call history items are sorted according to the start time, in descending order:

   ```
   var sortMode = new tizen.SortMode('startTime', 'DESC');
   ```

5. Use the `limit` and `offset` parameters of the `find()` method to specify the starting point and upper limit of the results that are returned.

   The `limit` parameter specifies the maximum number of matching results that are returned (the value 0 makes the limit infinite), while the `offset` parameter skips that many matching results that are to be returned (the value 0 means nothing is skipped).

   For example, if your search results consist of 100 matching results and you have specified an offset of 10 and a limit of 20, you get the objects from 10-29. The matching results from 0-9 are skipped due to the offset, and the 20 results starting from the first result after the offset are returned.

## Removing Call History Items

Learning how to remove call history items allows you to keep the call history list organized and save storage space on the device:

1.  Use the `remove()` method of the [CallHistory](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistory) interface to remove a specific item from the call history. First, search for the entry to be removed with the `find()` method, and then handle the removal in the event handler that is called when the `find()` method is successful.

    ```
    /* Remove the found call history item */
    function onSuccess(results) {
        if (results.length > 0)
            tizen.callhistory.remove(results[0]);
    }

    var numberFilter = new tizen.AttributeFilter('remoteParties.remoteParty',
                                                 'EXACTLY', '123456789');
    /* Search for the item to be removed */
    tizen.callhistory.find(onSuccess, onError, numberFilter, null, 1);
    ```

2.  To remove multiple call history items, use the `removeBatch()` method.

    The `removeBatch()` method functions similarly as the `remove()` method, except that it removes a list of call history items instead of a single item:

    ```
    /* Define success callback */
    function onSuccess(results) {
        tizen.callhistory.removeBatch(results);
    }

    var numberFilter = new tizen.AttributeFilter('remoteParties.remoteParty',
                                                 'EXACTLY', '123456789');
    tizen.callhistory.find(onSuccess, onError, numberFilter);
    ```

3.  To remove all call history items, use the `removeAll()` method:

    ```
    tizen.callhistory.removeAll();
    ```

## Monitoring the Call History

Learning how to register change listeners allows you to synchronize the view of your application to changes in the call history database.

1. Define the `onadded` event handler of the [CallHistoryChangeCallback](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistoryChangeCallback) listener interface, which tracks all new incoming and outgoing calls that are added to the call history.

   ```
   var onHistoryChange = {
       onadded: function(newItems) {
           for (var i in newItems) {
               console.log('Item ' + i + ' is newly added. Its startTime: ' + newItems[i].startTime);
           }
       },
   ```

2. Define the `onchanged` event handler, which tracks all changes in the call history.

   The event handler receives as an argument an array of [CallHistoryEntry](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistoryEntry) instances, which represent the changed items in the call history.

   ```
       onchanged: function(changedItems) {
           for (var i in changedItems) {
               console.log('Item ' + i + ' is updated. Its direction: ' + changedItems[i].direction);
           }
       },
   ```

3. Define the `onremoved` event handler, which tracks all items that are removed from the call history:

   ```
       onremoved: function(removedItems) {
           for (var i in removedItems) {
               console.log('Item ' + i + ' is removed. The removed item UID: ' + removedItems[i]);
           }
       }
   };
   ```

4. Use the `addChangeListener()` method of the [CallHistory](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistory) interface to register a listener for observing call history changes:

   ```
   var callHistoryListener = tizen.callhistory.addChangeListener(onHistoryChange);
   ```

5. Use the `removeChangeListener()` method to deregister a previously registered listener. Use the ID returned by the `addChangeListener()`:

   ```
   tizen.callhistory.removeChangeListener(callHistoryListener);
   ```

## Related Information
* Dependencies   
  - Tizen 2.4 and Higher for Mobile
