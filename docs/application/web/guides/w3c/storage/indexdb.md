# Indexed Database

In HTML5, an indexed database is a local storage used to store and manipulate key-value format data in a client. You can implement effective searches using an index, which is a specialized persistent key-value storage containing entries from the database based on specific property values.

The main features of the Indexed Database API include the following:

- Creating a database

  Use the `IndexedDB.open()` method to [create a database](#creating-a-database). In a database (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#database-concept){:target="_blank"}, [wearable](https://www.w3.org/TR/IndexedDB/#database-operations){:target="_blank"}, and [TV](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#database-concept){:target="_blank"} applications), at least 1 object store (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#object-store-concept){:target="_blank"}, [wearable](http://www.w3.org/TR/2013/WD-IndexedDB-20130516/#object-store-concept){:target="_blank"}, and [TV](https://www.w3.org/TR/IndexedDB/#object-store-construct){:target="_blank"} applications) must be present.

- Creating an object store

  Object store is the basic storage mechanism of indexed database storage data.

  You can [create an object store](#creating-an-object-store) using the `createObjectStore()` method. The object store contains a list of records for storing data, and a key-value list sorted according to the key in an ascending order.

- Managing data

  You can [save and access data](#managing-data) in the object store.

  The stored data creates a key, assigned to a `keypath`, which in turn creates a value as a JSON object.

  > [!NOTE]
  > Tizen supports the `READ_ONLY`, `READ_WRITE`, and `VERSION_CHANGE` transactions (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#transaction){:target="_blank"}, [wearable](https://www.w3.org/TR/IndexedDB/#transaction-construct){:target="_blank"}, and [TV](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#transaction){:target="_blank"} applications) with the `unsigned short` type.

- Creating an index

  In the object store, you can use the `createIndex()` method to [generate an index](#index). You can search for and retrieve records stored in the index (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#index-concept){:target="_blank"}, [wearable](https://www.w3.org/TR/IndexedDB/#index-construct){:target="_blank"}, and [TV](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#index-concept){:target="_blank"} applications) using other properties than the key, as the key is not always unique. You can also retrieve records containing arrays as keys.

## Create a database

Creating and deleting a database is a useful data management skill, follow these steps to create and delete a database:

1. Use the `window.webkitIndexedDB.open()` method to generate a database named `TizenIndexedDB` in order to create an object store for storage:

   ```
   <script>
       if (!window.webkitIndexedDB) {
           window.alert('Does not support IndexedDB');
       } else {
           var tizenDB = {};
           var request = window.webkitIndexedDB.open('TizenIndexedDB');

           request.onsuccess = function(e) {};
           request.onerror = function(e) {/* Error handling */};
       }
   </script>
   ```

   Check whether an indexed database is supported in the `window` object. If the database is generated properly, the `onsuccess` event handler is called.

   > [!NOTE]
   > The name of the database can be any string type, including an empty string. To change the version of the database, use the `VERSION_CHANGE` transaction.

2. Delete the generated database using the `window.webkitIndexedDB.deleteDatabase()` method:

   ```
   <script>
       window.webkitIndexedDB.deleteDatabase('TizenIndexedDB');
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [indexedDB_opening_database.html](http://download.tizen.org/misc/examples/w3c_html5/storage/indexed_database_api){:target="_blank"}

## Create an object store

An object store can derive keys from the following sources:

- Key generator (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#dfn-key-generator){:target="_blank"}, [wearable](https://www.w3.org/TR/IndexedDB/#key-generator-construct){:target="_blank"}, and [TV](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#dfn-key-generator){:target="_blank"} applications)

    Generates an increasing number every time a key is needed.
- Key path (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#key-path-construct){:target="_blank"}, [wearable](https://www.w3.org/TR/IndexedDB/#key-path-construct){:target="_blank"}, and [TV](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#key-path-construct){:target="_blank"} applications)

    Key is derived through a key path.

- Value (in [mobile](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#value-construct){:target="_blank"}, [wearable](https://www.w3.org/TR/IndexedDB/#value-construct){:target="_blank"}, and [TV](http://www.w3.org/TR/2015/REC-IndexedDB-20150108/#value-construct){:target="_blank"} applications)

    Key is specified when a value is stored in the object store.

Creating and deleting an object store is a useful data management skill:

1. To generate an object store for data storage, use the `createObjectStore()` method:

   ```
   <script>
       var tizenDB = {}
       var request = window.webkitIndexedDB.open('TizenIndexedDB');
       request.onupgradeneeded = function(e) {
           tizenDB.db = event.target.result;
           try {
               var objStore = tizenDB.db.createObjectStore('tizenStore', {keyPath: 'key'});
           }
       };
   </script>
   ```

   The name and key path of an independent object are defined in the object store. The `keyPath` property makes the object store unique and must contain the `key` attribute to store data in the object store.

2. To delete the object store, use the `deleteObjectStore()` method:

   ```
   <script>
       window.webkitIndexedDB.deleteObjectStore('tizenStore');
   </script>
   ```

### Source code

For the complete source code related to this use case, see the following file:

- [indexedDB_creating_objectStore.html](http://download.tizen.org/misc/examples/w3c_html5/storage/indexed_database_api){:target="_blank"}

## Manage data

Saving, accessing, and deleting data in an object store is a useful data management skill, follow these steps to save, access, and delete a data:

1. Access the object store using the `readwrite` transaction and save data using the `put()` method:

   ```
   <script>
       objStore.transaction.oncomplete = function(e) {
           var trans = tizenDB.db.transaction('tizenStore', 'readwrite');
           var tizenStore = trans.objectStore('tizenStore');
           var data = {
               'key': new Date().getTime(),
               'text': 'Tizen-' + Math.random()
           };

           var request = tizenStore.put(data);
           request.onsuccess = function(e) {
               tizenDB.db.objectStoreId = request.result;
               console.log(request.result);
           };
       };
   </script>
   ```

2. Request data in the `tizenStore` object store by calling data relevant to the key value in the storage with the `get()` method:

   ```
   <script>
       var request = tizenStore.put(data);
       request.onsuccess = function(e) {
           tizenDB.db.objectStoreId = request.result;
           var data = tizenStore.get(tizenDB.db.objectStoreId);
       };
   </script>
   ```

3. Delete the data in the object store using the `delete()` method:

   ```
   <script>
       var request = tizenStore.put(data);
       request.onsuccess = function(e) {
           tizenDB.db.objectStoreId = request.result;
           var data = tizenStore.delete(tizenDB.db.objectStoreId);
           data.onsuccess = function(e) {
               console.log(data);
           };
       };
   </script>
   ```

### Source code

For the complete source code related to this use case, see the following file:

- [indexedDB_saving_data.html](http://download.tizen.org/misc/examples/w3c_html5/storage/indexed_database_api){:target="_blank"}

<a name="index"> </a>
## Create an index

Creating, accessing, and deleting an index is a useful data management skill, follow these steps to create, access, and delete an index:

1. Create an index named `tizen01` to search for stored data in records based on its property (`text`):

   ```
   <script>
       var objStore = tizenDB.db.createObjectStore('tizenStore', {keyPath: 'key'});
       tizenDB.index = objStore.createIndex('tizen01', 'text');
   ```

2. Access the index using the `objStore.index()` method:

   ```
       var dbIndex = objStore.index('tizen01');
   ```

3. Delete the index using the `objStore.deleteIndex()` method:

   ```
       tizenDB.index = objStore.deleteIndex('tizen01');
   </script>
   ```

### Source code

For the complete source code related to this use case, see the following file:

- [indexedDB_creating_index.html](http://download.tizen.org/misc/examples/w3c_html5/storage/indexed_database_api){:target="_blank"}

## Related information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
