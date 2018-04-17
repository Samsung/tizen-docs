# Bookmarks

You can manage the Tizen Web browser bookmarks by retrieving the current bookmark list. You can create or delete both bookmark folders and items.

This feature is supported in mobile applications only.

The main features of the Bookmark API include:

- Creating bookmarks

  You can [create bookmark folders and items](#creating-bookmark-folders-and-items) using the [BookmarkManager](../../api/latest/device_api/mobile/tizen/bookmark.html#BookmarkManager) interface.

- Deleting bookmarks

  You can [delete bookmark folders and items](#deleting-bookmarks) using the `BookmarkManager` interface.

- Retrieving bookmarks

  You can [retrieve a list of current bookmarks](#retrieving-the-bookmark-list) of the Tizen Web browser using the `BookmarkManager` interface.

## Prerequisites

To use the [Bookmark](../../api/latest/device_api/mobile/tizen/bookmark.html) API, the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/bookmark.read"/>
<tizen:privilege name="http://tizen.org/privilege/bookmark.write"/>
```

## Creating Bookmark Folders and Items

To create engaging applications with bookmark-related features, you must learn how to add bookmark folders and items to the root bookmark folder and subfolders:

- To add a folder and a bookmark to the root bookmark folder:    

  1. Create an instance of the [BookmarkFolder](../../api/latest/device_api/mobile/tizen/bookmark.html#BookmarkFolder) interface by specifying the bookmark folder name:

     ```
     var folder1 = new tizen.BookmarkFolder('folder1');
     ```

  2. Create an instance of the [BookmarkItem](../../api/latest/device_api/mobile/tizen/bookmark.html#BookmarkItem) interface by specifying the bookmark item name and URL:

     ```
     var tizen = new tizen.BookmarkItem('tizen', 'https://www.tizen.org');
     ```

  3. Use the `add()` method of the [BookmarkManager](../../api/latest/device_api/mobile/tizen/bookmark.html#BookmarkManager) interface to add both a bookmark folder and a bookmark to the root bookmark folder:

     ```
     tizen.bookmark.add(folder1);
     tizen.bookmark.add(tizen);
     ```

- To add a folder and a bookmark to a subfolder:    

  1. Create an instance of the `BookmarkFolder` and `BookmarkItem` interface:

     ```
     var folder2 = new tizen.BookmarkFolder('folder2');
     var developerTizen = new tizen.BookmarkItem('developerTizen', 'https://developer.tizen.org');
     ```

  2. Use the `add()` method to add a folder and a bookmark to a bookmark subfolder by specifying the parent bookmark folder name:

     ```
     tizen.bookmark.add(folder2, folder1);
     tizen.bookmark.add(developerTizen, folder1);
     ```

     As a result of the code snippet above, the `folder1` folder contains the `developerTizen` bookmark and the `folder2` subfolder.

## Deleting Bookmarks

To create engaging applications with bookmark-related features, you must learn how to delete bookmarks:

- To remove a bookmark item, use the `remove()` method of the [BookmarkManager](../../api/latest/device_api/mobile/tizen/bookmark.html#BookmarkManager) interface and specify the bookmark item:

  ```
  tizen.bookmark.remove(tizen);
  ```

- To remove a bookmark folder, use the `remove()` method and specify the bookmark folder:

  ```
  tizen.bookmark.remove(folder2);
  ```

- To remove all the bookmark folders and items from the bookmarks list, use the `remove()` method without specifying a parameter:

  ```
  tizen.bookmark.remove();
  ```

## Retrieving the Bookmark List

To create engaging applications with bookmark-related features, you must learn how to retrieve the bookmarks:

- To retrieve bookmarks only from the root bookmark folder, use the `get()` method of the [BookmarkManager](../../api/latest/device_api/mobile/tizen/bookmark.html#BookmarkManager) interface without specifying any parameter:

  ```
  tizen.bookmark.get();
  ```

- To retrieve bookmarks from the root bookmark folder and subfolders, use the `get()` method and set the `recursive` parameter as `true`:

  ```
  tizen.bookmark.get(null, true);
  ```

- To retrieve bookmarks only from a specific bookmark folder excluding its subfolders, use the `get()` method and specify the bookmark folder name:

  ```
  tizen.bookmark.get(folder1);
  ```

- To retrieve bookmarks from a specific bookmark folder and its subfolders, use the `get()` method, specifying the bookmark folder name and setting the `recursive` parameter as `true`:

  ```
  tizen.bookmark.get(folder1, true);
  ```

## Related Information
* Dependencies  
  - Tizen 2.4 and Higher for Mobile
