# Media Content


You can get information about media content from the metadata in the content, such as an ID3 or MP4 tag. You can obtain or update data from the media database, which stores metadata for the media files (such as images, videos, and audio) on the device.

**Figure: Media content of the device**

![Media content of the device](./media/content.png)

The media files are updated by an application (by using the classes and methods of the [Tizen.Content.MediaContent](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.html) namespace) or a media scanner. When updating the files with the media scanner, the following limitations apply:

-   SD card insertion and removal: Media files are updated only in the SD card.
-   Rebooting the device: Media files are updated in the internal memory and SD card on the device.

You can only use the Tizen.Content.MediaContent classes to manage files located in specific paths.


> **Note**   
> To obtain information from the media database, you must first [connect to it](#prerequisites). When the connection is no longer needed, remember to disconnect from the media database.


The main features of the Tizen.Content.MediaContent namespace include:

-   Media content

    You can update database details due to file (or folder) creation or deletion. If the specified file (or folder) does not exist in the file system, it is removed from the database.

    You can also retrieve a list of media folders, retrieve a list of media items, and [monitor changes](#update) in the media database. You can [search for specific media folders](#find_folder) and [retrieve media folder content](#folder_content).

- Media information

    You can update the media database due to file creation, deletion, or update on the device. You can [retrieve media information](#info), add [media files and folders](#insert) to the database, and [scan for media folders](#scan).

    You can also retrieve [general information about the media and more specific information about the media type](#media_info).

- Media bookmarks

    You can [insert](#inserting), [search for](#finding), and [remove](#removing) bookmarks for video and audio files.

- Media filtering

    You can [create a filter](#filter) to find specific media items.

- Media playlists

    You can [add](#create_playlist) or [delete](#delete_playlist) a playlist of video and audio files, and add media files to a created playlist. In addition, you can also [search for playlists](#find_playlist).

- Media tags

    You can access the tag information for the media files in the database. You can, for example, [add media tags](#tag_add), [retrieve tag information](#tag_list), and [delete tags](#tag_delete).

- Media albums

    You can manage an album of audio files. You can, for example, [search for albums](#findingall) and [retrieve album content](#findinginfo).

- Media item groups

    You can manage a collection of media items as a group, when the items have the same value of a given property. You can, for example, [search for groups](#find_groups).

- Media storages

    You can [retrieve information about the media storages](#storage_list).


## Prerequisites

To enable your application to use the media content functionality:

1.  To use the [Tizen.Content.MediaContent](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <!--To insert content-->
       <privilege>http://tizen.org/privilege/content.write</privilege>
       <!--To access a storage to insert content-->
       <privilege>http://tizen.org/privilege/mediastorage</privilege>
    </privileges>
    ```

2. Connect to the database:

    ```
    var mediaDatabase = new MediaDatabase();

    mediaDatabase.Connect();
    ```

3. When you no longer use the database, disconnect from it:

    ```
    mediaDatabase.Disconnect();
    ```

<a name="update"></a>
## Receiving Update Notifications

1.  To receive notifications of database changes, define and register event handlers for the `MediaInfoUpdated` or `FolderUpdated` events of the [Tizen.Content.MediaContent.MediaDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaDatabase.html) class:

    ```
    void OnMediaInfoUpdated(object sender, MediaInfoUpdatedEventArgs args)
    {
        Tizen.Log.Info(LogTag, $"MediaInfo updated: Id = {args.Id}, Operation = {args.OperationType}");
    }

    void OnFolderUpdated(object sender, MediaInfoUpdatedEventArgs args)
    {
        Tizen.Log.Info(LogTag, $"Folder updated: Id = {args.Id}, Operation = {args.OperationType}");
    }

    MediaDatabase.MediInfoUpdated += OnMediaInfoUpdated;
    MediaDatabase.FolderUpdated += OnFolderUpdated;
    ```

2. When you no longer want to receive notifications, deregister the event handlers:

    ```
    MediDatabase.MediInfoUpdated -= OnMediaInfoUpdated;
    MediDatabase.FolderUpdated -= OnFolderUpdated;
    ```

<a name="findingall"></a>
## Finding Albums

To find the albums satisfying certain criteria, or modify the search results in a specific way, create a filter and set its properties.

The following example filters media albums so that only albums with the artist named "Tizen" are included in the result. The filter is case-insensitive, and the results are sorted in descending order by album name. For more information on the filter properties, see [Setting up a Filter](#filter).

```
var selectArguments = new SelectArguments()
{
    FilterExpression = $"{AlbumColumns.Artist} = 'Tizen' COLLATE NOCASE",
    SortOrder = $"{AlbumColumns.Name} DESC"
};

var albumCmd = new AlbumCommand(mediaDatabase);

using (var mediaDataReader = albumCmd.Select(selectArguments))
{
    while (mediaDataReader.Read())
    {
        var album = mediaDataReader.Current;

        Tizen.Log.Info(LogTag, $"Album - Id: {album.Id}, Name: {album.Name}, Artist: {album.Artist}");
```

Get the media item count in the album with the `CountMember()` method of the [Tizen.Content.MediaContent.AlbumCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.AlbumCommand.html) class:

```
        int count = albumCmd.CountMember(album.Id);

        Tizen.Log.Info(LogTag, $"Media count in this album: {count}");
    }
}
```

You can also get the number of albums available with the `Count()` method.

<a name="findinginfo"></a>
## Retrieving Album Content

To retrieve the media items in a given album:

```
Album album = ...

using (var mediaDataReader = albumCmd.SelectMember(album.Id))
{
    while (mediaDataReader.Read())
    {
        var mediaInfo = mediaDataReader.Current;

        Tizen.Log.Info(LogTag, $"MediaInfo - Title: {mediaInfo.Title}, MIME type: {mediaInfo.MimeType}, Size: {mediaInfo.Size}");
    }
}
```

<a name="inserting"></a>
## Inserting Bookmarks

To set a bookmark for a video file at a given timestamp, use the `Insert()` method of the [Tizen.Content.MediaContent.BookmarkCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.BookmarkCommand.html) class:

```
var bookmarkCmd = new BookmarkCommand(mediaDatabase);

var thumbnailPath = "path/to/image/file";

bookmarkCmd.Insert(mediaInfo.Id, offset, thumbnailPath);
```

The parameters are the media ID of the video file, the moment (time in milliseconds from the beginning) in the video to bookmark, and the image used as a thumbnail for the bookmark.

<a name="finding"></a>
## Finding Bookmarks

To retrieve bookmarks:

-   To find the bookmarks, use the `Select()` method of the [Tizen.Content.MediaContent.BookmarkCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.BookmarkCommand.html) class:

    ```
    using (var mediaDataReader = bookmarkCmd.Select())
    {
        while (mediaDataReader.Read())
        {
            var bookmark = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Bookmark ThumbnailPath={bookmark.ThumbnailPath}, Offset={bookmark.Offset}");
        }
    }
    ```

- To find the bookmarks set for a media item, use the `SelectBookmark()` method of the [Tizen.Content.MediaContent.MediaInfoCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoCommand.html) class:

    ```
    var mediaDataReader = mediaInfoCmd.SelectBookmark(mediaId);
    ```

<a name="removing"></a>
## Removing Bookmarks

To remove a bookmark, use the `Delete()` method of the [Tizen.Content.MediaContent.BookmarkCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.BookmarkCommand.html) class:

```
bookmarkCmd.Delete(bookmark.Id);
```

<a name="filter"></a>
## Setting up a Filter

The classes of the [Tizen.Content.MediaContent](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.html) namespace use the `SelectXXX()` and `CountXXX()` methods to search for items in the media database. You can filter or modify the output of these methods by using an instance of the [Tizen.Content.MediaContent.SelectArguments](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.SelectArguments.html) class as a parameter for the `SelectXXX()` methods or an instance of the [Tizen.Content.MediaContent.CountArguments](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.CountArguments.html) class as a parameter for the `CountXXX()` methods.

For example, to filter the results of the `SelectMedia()` method of the [Tizen.Content.MediaContent.MediaInfoCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoCommand.html) class:

1.  Create an instance of the `Tizen.Content.MediaContent.SelectArguments` class:

    ```
    var selectArguments = new SelectArguments();
    ```

2. Set a filter expression as the `FilterExpression` property of the instance.

    The following example sets a filter expression which finds albums with the artist named "Tizen" with a case-insensitive search:

    ```
    selectArguments.FilterExpression = $"{AlbumColumns.Artist}='Tizen' COLLATE NOCASE";
    ```

    The `FilterExpression` property used for filtering the search results is passed to an SQL database. It defines the `WHERE` clause of an SQL query and must match the following pattern:

    ```
    /* Basic pattern, COLLATE (optional) determines how the strings are compared */
    <column name> <relation> <value> [COLLATE NOCASE/RTRIM/LOCALIZED]

    /* If the relation is =, >, >=, <, or <=, the following is also valid */
    <value> <relation> <column name> [COLLATE NOCASE/RTRIM/LOCALIZED]
    ```

    The valid relations are:

    ```
    =, >, >=, <, <=, IN, NOT IN, LIKE
    ```

    Conditions can be joined by `OR` and `AND` to form more complex conditions.

    Column names are defined in the `*Columns` classes.

3. Set a sorting order using the `SortOrder` property.

    The following example sorts the results in ascending order by artist name. The sorting is case-insensitive.

    ```
    selectArguments.SortOrder = $"{AlbumColumns.Artist} COLLATE NOCASE ASC";
    ```

4. Set a limit to read using the `StartRowIndex` and `TotalRowCount` properties. This allows you to limit the results to a specific subset. For example, if you sort the items by size in an ascending order and set the `StartRowIndex` to 10, the 10 smallest items are not included in the results.

    The following example sets a `TotalRowCount` property that returns results starting from the beginning, and returns a maximum of 5 results:

    ```
    selectArguments.TotalRowCount = 5;
    ```

5. To use the filter, include it as a parameter of the `SelectMedia()` method of the `Tizen.Content.MediaContent.MediaInfoCommand` class:

    ```
    mediaInfoCmd.SelectMedia(selectArguments);
    ```

<a name="find_folder"></a>
## Finding Folders

To find media folders:

1.  To find media folders and filter the results, use the `Select()` method of the [Tizen.Content.MediaContent.FolderCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.FolderCommand.html) class.

    The following example filters media folders so that only folders named "Downloads" found in the internal storage are included in the result. For more information on the filter properties, see [Setting up a Filter](#filter).

    ```
    var folderCmd = new FolderCommand(mediaDatabase);

    var selectArguments = new SelectArguments()
    {
        FilterExpression = $"{FolderColumns.Name}='Downloads' AND {FolderColumns.StorageType}={(int)StorageType.Internal}"
    };

    using (var mediaDataReader = folderCmd.Select(selectArguments))
    {
        while (mediaDataReader.Read())
        {
            var folder = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Folder Id={folder.Id}, Path={folder.Path}");
    ```

2. Get the media item count in the folder with the `CountMedia()` method:

    ```
            int count = folderCmd.CountMedia(folder.Id);

            Tizen.Log.Info(LogTag, $"{count} media items in Path={folder.Path}");
        }
    }
    ```

<a name="folder_content"></a>
## Retrieving Folder Content

To retrieve media items in the folder with the given ID, use the `SelectMedia()` method of the [Tizen.Content.MediaContent.FolderCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.FolderCommand.html) class:

```
using (var mediaDataReader = folderCmd.SelectMedia(folder.Id))
{
    while (mediaDataReader.Read())
    {
        var mediaInfo = mediaDataReader.Current;

        Tizen.Log.Info(LogTag, $"MediaInfo Title={mediaInfo.Title}");
    }
}
```

<a name="info"></a>
## Retrieving Media Information

To access media item information:

1.  The following example filters media items so that only image and video items are included in the result. The filter is case-insensitive, and the results are sorted in descending order by item display name. For more information on the filter properties, see [Setting up a Filter](#filter).

    ```
    var selectArguments = new SelectArguments()
    {
        FilterExpression = $"{MediaInfoColumns.MediaType}={(int)Media​Type.Image} OR {MediaInfoColumns.MediaType}={(int)Media​Type.Video}",
        SortOrder = "{MediaInfoColumns.DisplayName} COLLATE NOCASE DESC"
    };
    ```

2. To find the media items, use the `SelectMedia()` method of the [Tizen.Content.MediaContent.MediaInfoCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoCommand.html) class.

    The available metadata varies depending on the media type, such as image, video, or audio.

    ```
    using (var mediaDataReader = mediaInfoCmd.SelectMedia(selectArguments))
    {
        while (mediaDataReader.Read())
        {
            var mediaInfo = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Id={mediaInfo.Id}, Name={mediaInfo.DisplayName}, Path={mediaInfo.Path}");

            switch (mediaInfo.MediaType)
            {
                case MediaType.Image:
                    ImageInfo imageInfo = mediaInfo as ImageInfo;

                    Tizen.Log.Info(LogTag, "This is an image");
                    Tizen.Log.Info(LogTag, $"Width: {imageInfo.Width}, Height: {imageInfo.Height}, Orientation: {imageInfo.Orientation}, Date taken: {imageInfo.DateTaken}");
                    break;

                case MediaType.Video:
                    VideoInfo videoInfo = mediaInfo as VideoInfo;

                    Tizen.Log.Info(LogTag, "This is a video");
                    Tizen.Log.Info(LogTag, $"Title: {videoInfo.Title}, Album: {videoInfo.Alarm}, Artist: {videoInfo.Artist}, Album artist: {videoInfo.AlbumArtist}, Duration: {videoInfo.Duration}");
            }
        }
    }
    ```

<a name="insert"></a>
## Inserting Media in the Database

To use newly created media files, insert them into the database. To add information in the database, use one of the following options:

-   The `Add()` method of the [Tizen.Content.MediaContent.MediaInfoCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoCommand.html) class:

    ```
    mediaInfoCmd.Add(imagePath);
    ```

- The `MediaDatabase.ScanFile()` method of the [Tizen.Content.MediaContent.MediaDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaDatabase.html) class:

    ```
    mediaDatabase.ScanFile(imagePath);
    ```

The difference between the 2 options is that the `Add()` method returns the [Tizen.Content.MediaContent.MediaInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfo.html) instance of the media file after inserting the file in the database, whereas the `ScanFile()` method only inserts the file.

<a name="scan"></a>
## Scanning a Media Folder

To update media items in a folder, and optionally its subfolders, use the `ScanFolderAsync()` method of the [Tizen.Content.MediaContent.MediaDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaDatabase.html) class.

If the second parameter is set to `true`, all subfolders are scanned too.

```
await mediaDatabase.ScanFolderAsync(folderPath, true);
```

<a name="create_playlist"></a>
## Creating Playlists

To create and insert a playlist to the database:

1.  Insert a playlist to the database as a record.

    Add a new playlist to the database using the `Insert()` method of the [Tizen.Content.MediaContent.PlaylistCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.PlaylistCommand.html) class:

    ```
    var playlistCmd = new PlaylistCommand(mediaDatabase);

    var playlist = playlistCmd.Insert("playlist_for_tutorial");
    ```

    You can modify the playlist name later using the `Update()` method.

2. To add media items to the playlist, use the `AddMember()` or `AddMembers()` methods:

    ```
    /// Add 1 item to the playlist
    playlistCmd.AddMember(playlist.Id, mediaInfo.Id);

    /// Add multiple items to the playlist
    string[] mediaInfoIds = new string[]{mediaInfo1.Id, mediaInfo2.Id};
    playlistCmd.AddMembers(playlist.Id, mediaInfoIds);
    ```

<a name="find_playlist"></a>
## Finding Playlists

To find playlists and their contents:

-   To find playlists and filter the results, use the `Select()` method of the [Tizen.Content.MediaContent.PlaylistCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.PlaylistCommand.html) class:

    ```
    using (var mediaDataReader = playlistCmd.Select())
    {
        while (mediaDataReader.Read())
        {
            var playlist = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Playlist Name={playlist.Name}");
        }
    }
    ```

    To find only playlists satisfying certain criteria, or modify the results in a specific way, use an instance of the [Tizen.Content.MediaContent.SelectArguments](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.SelectArguments.html) class as a parameter to the `Select()` method.

    For information on creating a filter, see [Setting up a Filter](#filter).

- To retrieve the media items in the playlist, use the `SelectMember()` method of the `Tizen.Content.MediaContent.PlaylistCommand` class:

    ```
    using (var mediaDataReader = playlistCmd.SelectMember(playlist.Id))
    {
        while (mediaDataReader.Read())
        {
            var mediaInfo = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Media info on the playlist: {mediaInfo.Id}");
        }
    }
    ```

<a name="delete_playlist"></a>
## Deleting Playlists

When you no longer need it, delete a playlist from the database with the `Delete()` method of the [Tizen.Content.MediaContent.PlaylistCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.PlaylistCommand.html) class to avoid creating useless records:

```
playlistCmd.Delete(playlist.Id);
```

<a name="tag_add"></a>
## Adding Tags

To add a tag to the database, and a file to the tag:

1.  Add the tag with the `Insert()` method of the [Tizen.Content.MediaContent.TagCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.TagCommand.html) class:

    ```
    var tagCmd = new TagCommand(mediaDatabase);

    var tag = tagCmd.Insert("Tag name");
    ```

2. Insert a media item into the tag with the `AddMedia()` method.

    To insert an item into the tag, you need to know the ID of the item:

    ```
    tagCmd.AddMedia(tag.Id, mediaInfo.Id);
    ```

<a name="tag_list"></a>
## Retrieving Tag Information

To retrieve tag information:

-   To find tags and filter the results, use the `Select()` method of the [Tizen.Content.MediaContent.TagCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.TagCommand.html) class:

    ```
    using (var mediaDataReader = tagCmd.Select())
    {
        while (mediaDataReader.Read())
        {
            var tag = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Tag Name={tag.Name}");
        }
    }
    ```

    To find only tags satisfying certain criteria, or modify the results in a specific way, use an instance of the [Tizen.Content.MediaContent.SelectArguments](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.SelectArguments.html) class as a parameter to the `Select()` method.

    For information on creating a filter, see [Setting up a Filter](#filter).

- To retrieve the media items added to the tag, use the `SelectMedia()` method of the `Tizen.Content.MediaContent.TagCommand` class:

    ```
    using (var mediaDataReader = tagCmd.SelectMedia(tag.Id))
    {
        while (mediaDataReader.Read())
        {
            var mediaInfo = mediaDataReader.Current;

            Tizen.Log.Info(LogTag, $"Media info added to the tag: {mediaInfo.Id}");
        }
    }
    ```

<a name="tag_delete"></a>
## Deleting Tags

To delete a tag, use the `Delete()` method of the [Tizen.Content.MediaContent.TagCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.TagCommand.html) class:

```
tagCmd.Delete(tag.Id);
```

<a name="storage_list"></a>
## Retrieving Storage Information

To find the media storages, use the `Select()` method of the [Tizen.Content.MediaContent.StorageCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.StorageCommand.html) class:

```
var storageCmd = new StorageCommand(mediaDatabase);

using (var mediaDataReader = storageCmd.Select())
{
    while (mediaDataReader.Read())
    {
        var storage = mediaDataReader.Current;

        Tizen.Log.Info(LogTag, storage.ToString());
    }
}
```

<a name="find_groups"></a>
## Finding Media Item Groups

A group is a collection of media items which have the same value of a given column. For example, if the column is the artist, there are as many groups as there are artists, and each group consists of items by the same artist. The possible groups are determined by the [Tizen.Content.MediaContent.MediaInfoColumnKey](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoColumnKey.html) enumeration values, such as `Artist` and `MimeType`.

To find media item groups and filter the results:

1.  To find the media items satisfying certain criteria, or modify the results in a specific way, create an instance of the [Tizen.Content.MediaContent.SelectArguments](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.SelectArguments.html) class.

    The following example filters media items so that only items whose display name ends with ".jpg" are included in the result (the '%' characters act as wildcards in the filter expression, and they must be escaped using another '%' character to avoid compiler warnings). For more information on the filter properties, see [Setting up a Filter](#filter).

    ```
    var selectArguments = new SelectArguments()
    {
        FilterExpression = $"{MediaInfoColumns.DisplayName} LIKE '%%.jpg'"
    };
    ```

2. To group media files by MIME type:
    1.  To find the number of MIME type-related groups, use the `CountGroupBy()` method of the [Tizen.Content.MediaContent.MediaInfoCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoCommand.html) class:

        ```
        int count = mediaInfoCmd.CountGroupBy(MediaInfoColumnKey.MimeType);

        Tizen.Log.Info(LogTag, $"Group count: {count}");
        ```

        Since the method is called without a `Tizen.Content.MediaContent.SelectArguments` instance as a parameter, no filtering is performed and all groups are counted.

    2. To find the media item groups, use the `MediaInfoCommand.SelectGroupBy()` method:

        ```
        using (var mediaDataReader = mediaInfoCmd.SelectGroupBy(MediaInfoColumnKey.MimeType, selectArguments))
        {
            while (mediaDataReader.Read())
            {
        ```

    3. The `MediaDataReader<string>` returned by the `SelectGroupBy()` method contains the group names, in this case, various MIME types, such as `image/png` and `audio/mpeg`.

        ```
                var groupName = mediaDataReader.Current;

                Tizen.Log.Info(LogTag, $"Group name: {groupName}");
        ```

    4. You can use the group name to get all items in the group by adding a condition as the `FilterExpression` property of an instance of the `Tizen.Content.MediaContent.SelectArguments` class, then using that instance as a parameter of the `SelectMedia()` method of the `Tizen.Content.MediaContent.MediaInfoCommand` class:

        ```
                var selectArguments = new SelectArguments()
                {
                    FilterExpression = $"{MediaInfoColumns.DisplayName} LIKE '%%.jpg' AND {MediaInfoColumns.MimeType}='{groupName}'"
                };

                using (var mediaInfoReader = mediaInfoCmd.SelectMedia(selectArguments))
                {
                    /// Read the items
                }
            }
        }
        ```

<a name="media_info"></a>
## Media Information

You can get the media data from the media database using various methods, such as the `SelectMedia()` method of the [Tizen.Content.MediaContent.MediaInfoCommand](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Content.MediaContent.MediaInfoCommand.html) class. After that, you can retrieve general information about the media and specific information for each media type.

The following tables list the available media file information.

**Table: General information**

| Metadata name    | Description                              |
|----------------|----------------------------------------|
| `Media ID`       | ID of the media content                  |
| `File path`      | Path of the media content                |
| `Display name`   | Display name of the media content        |
| `Media type`     | Media type of the media content          |
| `Mime type`      | MIME type of the media content           |
| `Size`           | File size of the media content           |
| `Added time`     | Time the media content was added to the database |
| `Modified time`  | Last modification time of the media content |
| `Timeline`       | Time the media content was created       |
| `Thumbnail path` | Path of the stored thumbnail image of the media content |
| `Description`    | Description of the media content         |
| `Longitude`      | Longitude of the media content           |
| `Latitude`       | Latitude of the media content            |
| `Altitude`       | Altitude of the media content            |
| `Rating`         | Rating of the media content              |
| `Favorite`       | Favorite status of the media content     |
| `Title`          | Title of the media content               |
| `Storage type`   | Storage type of the media content        |

**Table: Audio metadata (only for audio files)**

| Metadata name    | Description                              |
|----------------|----------------------------------------|
| `Album`          | Album information for the audio content  |
| `Artist`         | Artist of the audio content              |
| `Album Artist`   | Album artist of the audio content<br>The artist and album artist can be the same. |
| `Genre`          | Genre of the audio content               |
| `Composer`       | Composer of the audio content            |
| `Year`           | Year the audio content was recorded      |
| `Date recorded`  | Date the audio content was recorded      |
| `Copyright`      | Copyright information for the audio content |
| `Track number`   | Track number of the audio content        |
| `Bit rate`       | Bit rate of the audio content            |
| `Bit per sample` | Bit per sample of the audio content<br>The bit per sample is the same as the sample format. The sample format is the number of digits in the digital representation of each sample. |
| `Sample rate`    | Sample rate of the audio content         |
| `Channels`       | Channel information for the audio content |
| `Duration`       | Duration of the audio content            |

**Table: Image metadata (only for image files)**

| Metadata name   | Description                              |
|---------------|----------------------------------------|
| `Width`         | Width of the image                       |
| `Height`        | Height of the image                      |
| `Exposure time` | Exposure time of the image               |
| `F-number`      | F-number of the image                    |
| `ISO`           | ISO of the image                         |
| `Model`         | Model name of the camera that created the image |
| `Orientation`   | Orientation of the image                 |
| `Date taken`    | Time the image was created<br>You can get this information from the EXIF tag. If there is no EXIF tag for the image, set the created time in the file system. |

**Table: Video metadata (only for video files)**

| Metadata name   | Description                             |
|---------------|---------------------------------------|
| `Album`         | Album information for the video content |
| `Artist`        | Artist of the video content             |
| `Album artist`  | Album artist of the video content       |
| `Genre`         | Genre of the video content              |
| `Composer`      | Media composer of the video content     |
| `Year`          | Year the video content was recorded     |
| `Date recorded` | Date the video content was recorded     |
| `Copyright`     | Copyright of the video content          |
| `Track number`  | Track number of the video content       |
| `Bit rate`      | Bit rate of the video content           |
| `Duration`      | Duration of the video content           |
| `Width`         | Width of the video content              |
| `Height`        | Height of the video content             |



## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
