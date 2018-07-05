# Stored Content Management

You can search for content (such as images, videos, and music) located in the local device storage. You can also perform content management tasks, such as viewing and updating content attributes.

The Content API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of Content API include:

- Content retrieval   

  You can [browse and search for content directories and content items](#browsing-content).

- Content management   

  You can [view and edit content item details](#managing-content). The details are common file information and metadata attributes of the media file.

- Content change notifications   

  You can keep the content in your application synchronized with an external content manager by [receiving notifications](#receiving-notifications-on-content-changes) in your application when the content changes.

- Playlist management   

  Using the `Playlist` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#Playlist), [wearable](../../api/latest/device_api/wearable/tizen/content.html#Playlist), and [TV](../../api/latest/device_api/tv/tizen/content.html#Playlist) applications), you can:

  - Create playlists

    You can [create a new playlist](#creating-a-playlist) and add items to it. You can also create a new playlist by copying the content of an existing playlist.

  - Manage playlists

    You can [retrieve playlists and delete them](#managing-playlists).

  - Manage playlist items

    You can [manage playlist items](#managing-playlist-items) by adding and retrieving items, and changing the position of a single item or the order of all items.

The Content API uses the same `ContentManager` interface instance (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications) for all content-related functionalities. The instance provides higher efficiency by performing batch operations on content items.

> **Note**  
> The batch mode does not provide progress information about operations. To ensure that you can view the progress, break the batch operation down into multiple smaller batch operations. For example, break down a batch of 100 update requests into 10 batch operations that update 10 records at a time. Breaking down a batch operation also helps you avoid blocking other database operations, such as add or remove.

## Prerequisites

To use the Content API (in [mobile](../../api/latest/device_api/mobile/tizen/content.html), [wearable](../../api/latest/device_api/wearable/tizen/content.html), and [TV](../../api/latest/device_api/tv/tizen/content.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/content.read"/>
<tizen:privilege name="http://tizen.org/privilege/content.write"/>
```

## Browsing Content

You can browse and search for content directories and content using the `getDirectories()` and `find()` methods of the `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications). When searching for content items, you can create [attribute filters](./data-filter.md#creating-attribute-filters), [attribute range filters](./data-filter.md#creating-attribute-range-filters), and [composite filters](./data-filter.md#creating-composite-filters) based on [specific filter attributes](./data-filter.md#content-filter-attributes) of the `ContentManager` interface. You can also [sort the search results](./data-filter.md#using-sorting-modes).

To browse and search for content directories and content items in directories:

1. Retrieve the `ContentManager` interface instance using the `tizen` global object:

   ```
   var manager = tizen.content;
   ```

2. To search for content directories on the local device, use the `getDirectories()` method of the `ContentManager` interface. The method returns an array of `ContentDirectory` objects (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentDirectory), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentDirectory), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentDirectory) applications).

   ```
   function onDirectoryArraySuccess(directories) {
       for (var i = 0; i < directories.length; i++) {
           /* Retrieve folder-specific information */
       }
   }

   manager.getDirectories(onDirectoryArraySuccess);
   ```

3. To search for the content items in all directories, use the `find()` method of the `ContentManager` interface. The method returns an array of `Content` objects (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#Content), [wearable](../../api/latest/device_api/wearable/tizen/content.html#Content), and [TV](../../api/latest/device_api/tv/tizen/content.html#Content) applications).

   ```
   function onContentItemArraySuccess(contents) {
       for (var i = 0; i < contents.length; i++) {
           console.log(i + ':' + contents[i].type + ':' + contents[i].title + ':' + contents[i].mimeType);
       }
   }

   var contentType = 'VIDEO';
   var filter = new tizen.AttributeFilter('type', 'EXACTLY', contentType);
   manager.find(onContentItemArraySuccess, null, null, filter);
   ```

   In the `find()` method in the above example, the directory ID parameter is set to `null` (which means that all directories are searched), the filter retrieves all content items whose type is `VIDEO`, and no sorting order is defined (which means that the default sorting order is used).

## Managing Content

You can manage content in many ways:

- You can view content item details with the `find()` method.
- You can update some attributes of a content item, for example its rating, with the `update()` method.  
   For more information on the content attributes, see the Content Full WebIDL Reference (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#full-webidl), [wearable](../../api/latest/device_api/wearable/tizen/content.html#full-webidl), and [TV](../../api/latest/device_api/tv/tizen/content.html#full-webidl) applications).
- If a content item is copied or moved, you cannot find it because a scan is not performed automatically. You can retrieve a copied or moved item with the `find()` method after calling the `scanFile()` method.
- You can create a thumbnail for a content item using the `createThumbnail()` method.

> **Note**  
> You can only view (and not update) the read-only attributes.

To view and update content details:

1. Retrieve the `ContentManager` interface instance (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications) using the `tizen` global object, and search for the item whose details you want to update.

   In the following example, the item whose title is `image7.jpg` is retrieved.

   ```
   var manager = tizen.content;

   var filter = new tizen.AttributeFilter('title', 'EXACTLY', 'image7.jpg');
   manager.find(onMediaItemArraySuccess, null, null, filter);
   ```

2. In the success event handler of the `find()` method, view the content item details by displaying them in the console log:

   ```
   function onMediaItemArraySuccess(item) {
       if (items.length > 0) {
           console.log(items[0].type + ': ' + items[0].title + ': ' + items[0].mimeType);
           console.log('geolocation-latitude: ' + items[0].geolocation.latitude +
                       ' longitude:' + items[0].geolocation.longitude);
           update(items[0]);
       }
   }
   ```

3. To update the editable attributes of the content item, use the `update()` method. In the following example, the rating of the content item is increased.

   ```
   function update(item) {
       /* Checks whether the attribute is editable */
       if (item.editableAttributes.indexOf('rating') >= 0) {
           /* Changes an attribute */
           item.rating = 1;

           /* Updates the item */
           manager.update(item);
       }
   }
   ```

4. To scan for the content item file, use the `scanFile()` method. Because scanning is not performed automatically when the content file is copied or moved, call the `scanFile()` method to find the file.

   ```
   /* Assume the images/photo.jpg is copied to the device */
   function onScanSuccessCallback(path) {
       console.log('Scanning completed:' + path);
   }

   tizen.filesystem.resolve('images/photo.jpg', function(file) {
       tizen.content.scanFile(file.toURI(), onScanSuccessCallback);
   });
   ```

5. To create a thumbnail for a content item, use the `createThumbnail()` method:

   ```
   function createCB(path) {
       console.log('A path of a just created thumbnail is ' + path);
   }

   function findCB(contents) {
       if (contents.length > 0) {
           tizen.content.createThumbnail(contents[0], createCB);
       }
   }

   tizen.content.find(findCB);
   ```

## Receiving Notifications on Content Changes

You can receive notifications when a content item is added, updated, or deleted. The `addChangeListener()` method of the `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications) registers a change listener. You can use the `ContentChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentChangeCallback), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentChangeCallback), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentChangeCallback) applications) to define listener event handlers for receiving the notifications.

To receive notifications when content items are added, updated, or removed:

1. Define the event handlers for different notifications using the `ContentChangeCallback` listener instance (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentChangeCallback), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentChangeCallback), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentChangeCallback) applications):

   ```
   var listener = {
       /* When new items are added */
       oncontentadded: function(content) {
           console.log(content.contentURI + ' content was added');
       },

       /* When items are updated */
       oncontentupdated: function(content) {
           console.log(content.contentURI + ' content was updated');
       },

       /* When items are deleted */
       oncontentremoved: function(id) {
           console.log(id + ' was removed');
       }
   };
   ```

2. Register the listener to use the defined event handlers:

   ```
   var listenerId = tizen.content.addChangeListener(listener);
   ```

3. To stop the notifications, use the `removeChangeListener()` method:

   ```
   tizen.content.removeChangeListener(listenerId);
   ```

## Creating a Playlist

Learning how to create a new playlist enables adding a playlist from your application:

- To create a new empty playlist, use the `createPlaylist()` method of the `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications):

  ```
  function createSuccess(playlist) {
      console.log('create SUCCESS');
  }

  tizen.content.createPlaylist('My new playlist', createSuccess);
  ```

- To create a new playlist based on an existing one (basically copy the existing playlist content to a new playlist), use the `createPlaylist()` method, passing the source playlist as a parameter:

  ```
  function createSuccess(playlist) {
      console.log('create SUCCESS');
  }

  tizen.content.getPlaylists(function(playlists) {
      var existingPlaylist = playlists[0];
      tizen.content.createPlaylist('My new playlist', createSuccess, null, existingPlaylist);
  });
  ```

## Managing Playlists

Learning how to retrieve and remove playlists is a basic playlist management skill:

- To retrieve a list of all playlists, use the `getPlaylists()` method of the `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications):

  ```
  function getPlaylistsSuccess(playlists) {
      for (var i = 0; i < playlists.length; i++) {
          var cur = playlists[i];
          console.log('[' + i + '] name:' + cur.name + ' number of tracks:' + cur.numberOfTracks);
      }
  }
  tizen.content.getPlaylists(getPlaylistsSuccess);
  ```

- To remove a playlist, use the `removePlaylist()` method providing the ID of the playlist:

  ```
  function removePlaylistSuccess() {
      console.log('removePlaylist() is successfully done.');
  }

  tizen.content.getPlaylists(function(playlists) {
      var myPlaylist = playlists[0];
      tizen.content.removePlaylist(myPlaylist.id, removePlaylistSuccess);
  });
  ```

## Managing Playlist Items

Learning how to manage list items is a basic playlist management skill:

- To add items to a playlist:

  1. Retrieve the multimedia content using the `find()` method of the `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications):

     ```
     var myPlaylist;

     tizen.content.getPlaylists(function(playlists) {
         myPlaylist = playlists[0];
         tizen.content.find(findSuccess, null, null, new tizen.AttributeFilter('type', 'EXACTLY', 'AUDIO'));
     });
     ```

  2. To add multiple items to the retrieved playlist, use the `addBatch()` method of the `Playlist` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#Playlist), [wearable](../../api/latest/device_api/wearable/tizen/content.html#Playlist), and [TV](../../api/latest/device_api/tv/tizen/content.html#Playlist) applications):

     ```
     function findSuccess(contents) {
         if (contents.length >= 3) {
             myPlaylist.addBatch([contents[0], contents[1], contents[2]]);
         } else {
             console.log('Not enough items. Need at least 3');
         }
     }
     ```

  3. To add a single item to the retrieved playlist, use the `add()` method of the `Playlist` interface:

     ```
     function findSuccess(contents) {
         if (contents.length > 0) {
             myPlaylist.add(contents[0]);
         }
     }
     ```

- To retrieve items from a playlist, use the `get()` method of the `Playlist` interface:

  ```
  function getSuccess(items) {
      console.log('Playlist items:');
      for (var i = 0; i < items.length; ++i) {
          console.log('[' + i + ']: name:' + items[i].name);
      }
  }

  tizen.content.getPlaylists(function(playlists) {
      var myPlaylist = playlists[0];
      myPlaylist.get(getSuccess);
  });
  ```

- To change the position of a single playlist item (track), use the `move()` method of the `Playlist` interface. The second parameter indicates how much and in which direction the item is moved.  
   Note that before moving the item, first you must retrieve it using the `get()` method.

  ```
  var myItem; /* Assume that it was retrieved using the get() method */
  function moveSuccess() {
      console.log('move item SUCCESS');
  }

  tizen.content.getPlaylists(function(playlists) {
      var myPlaylist = playlists[0];
      myPlaylist.move(myItem, -2, moveSuccess);
  });
  ```

  The example above moves the track 2 positions up on the playlist. The second parameter of the `move()` method can be a negative value, which means moving the track up, or a positive value, which means moving the track down. If the value is greater than number of tracks above or below, the item is moved accordingly to the beginning or end of the playlist.

- To change the order of all items in the playlist, use the `setOrder()` method. This feature is useful when sorting the playlist.  
   Following example reverses the order of the playlist items. For the `setOrder()` method to work, you must pass all items from the playlist. If an item is missing or an item from a different playlist is included, the `InvalidValuesError` exception is returned in the error callback.

  1. Get all tracks using the `get()` method.

  2. Within the success callback of the `setOrder()` method, create an array with the new order:

     ```
     var items; /* Assume that it was retrieved using the get() method */
     var newOrder = items.slice(0);
     newOrder.reverse();
     ```

  3. Execute the `setOrder()` method:

     ```
     function setOrderSuccess() {
         console.log('Set items order SUCCESS');
     }

     myPlaylist.setOrder(newOrder, setOrderSuccess);
     ```


## Related Information
* Dependencies     
     - Tizen 2.4 and Higher for Mobile
     - Tizen 2.3.1 and Higher for Wearable
     - Tizen 3.0 and Higher for TV
