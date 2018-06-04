# Content Downloads

You can download files from the Internet and monitor the progress and status of ongoing downloads.

The Download API is mandatory for the Tizen mobile profile, but optional for wearable and TV profiles. This means that it is supported on all mobile devices, but may not be supported on all wearable and TV devices. The Download API is supported on all Tizen Emulators.

The main features of the Download API include:

- Managing downloads

  You can [start, pause, resume, and cancel a download](#managing-downloads) of content using the `DownloadManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadManager), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadManager), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadManager) applications).

- Checking the download state and information

  You can [access the current download state and retrieve the download information](#checking-the-download-state-and-information) using the `DownloadManager` interface. The states are defined in the `DownloadState` enumerator (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadState), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadState), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadState) applications).

## Prerequisites

To use the Download API (in [mobile](../../api/latest/device_api/mobile/tizen/download.html), [wearable](../../api/latest/device_api/wearable/tizen/download.html), and [TV](../../api/latest/device_api/tv/tizen/download.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name=" http://tizen.org/privilege/download"/>
```

## Managing Downloads

To provide the user access to Internet resources, you must learn how to manage download operations:

1. Create an instance of the `DownloadRequest` interface (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadRequest), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadRequest), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadRequest) applications) that defines the URL of the file to be downloaded:

   ```
   var downloadRequest = new tizen.DownloadRequest('http://download.tizen.org/tools/README.txt', 'downloads');
   ```

   The final parameter (`downloads`) defines the folder where the downloaded content is stored. The parameter uses a relative folder location defined in the Filesystem API (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html) applications). The folder is not an absolute folder location, but instead uses a [virtual root location](../data/file-system.md#roots) (`downloads` is the default download location in the virtual root).

2. It is not possible to download anything when the device is not connected to a network. To check whether any connection is available, use the `getPropertyValue()` method of the `SystemInfo` interface (in [mobile](../../api/latest/device_api/mobile/tizen/systeminfo.html#SystemInfo), [wearable](../../api/latest/device_api/wearable/tizen/systeminfo.html#SystemInfo), and [TV](../../api/latest/device_api/tv/tizen/systeminfo.html#SystemInfo) applications):

   ```
   tizen.systeminfo.getPropertyValue('NETWORK', function(networkInfo) {
       if (networkInfo.networkType === 'NONE') {
           console.log('Network connection is not available.
                        Download is not possible.');
           downloadRequest = null;
       }
   });
   ```

3. Define the event handlers for different download process notifications using the `DownloadCallback` listener interface (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadCallback), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadCallback), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadCallback) applications):

   ```
   var listener = {
       /* When the download progresses (interval is platform-dependent) */
       onprogress: function(id, receivedSize, totalSize) {
           console.log('Received with id: ' + id + ', ' + receivedSize + '/' + totalSize);
       },

       /* When the user pauses the download */
       onpaused: function(id) {
           console.log('Paused with id: ' + id);
       },

       /* When the user cancels the download */
       oncanceled: function(id) {
           console.log('Canceled with id: ' + id);
       },

       /* When the download is completed */
       oncompleted: function(id, fullPath) {
           console.log('Completed with id: ' + id + ', full path: ' + fullPath);
       },

       /* When the download fails */
       onfailed: function(id, error) {
           console.log('Failed with id: ' + id + ', error name: ' + error.name);
       }
   };
   ```

4. To start downloading the file from the Internet, use the `start()` method of the `DownloadManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadManager), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadManager), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadManager) applications):

   ```
   downloadId = tizen.download.start(downloadRequest, listener);
   ```

   The `start()` method returns a unique identifier for the download operation.

5. During the download:

   1. To pause the download, use the `pause()` method with the download ID:

      ```
      tizen.download.pause(downloadId);
      ```

   2. To resume the download, use the `resume()` method with the download ID:

      ```
      tizen.download.resume(downloadId);
      ```

   3. To cancel the download, use the `cancel()` method with the download ID:

      ```
      tizen.download.cancel(downloadId);
      ```

## Checking the Download State and Information

To provide the user access to Internet resources, you must learn how to check the state of a download operation and retrieve relevant information:

1. To be able to monitor the download state, you need the download ID, which is the return value of the `start()` method of the `DownloadManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadManager), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadManager), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadManager) applications):

   ```
   downloadId = tizen.download.start(downloadRequest, listener);
   ```

2.  Use the `getState()` method with the download ID as a parameter to get the current state:

    ```
    var state = tizen.download.getState(downloadId);
    ```

    The method returns a `DownloadState` enumerator value (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadState), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadState), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadState) applications).

3. Use the `getDownloadRequest()` method with the download ID as a parameter to get the download request details that the user has previously set:

   ```
   var downloadRequest = tizen.download.getDownloadRequest(downloadId);
   ```

   The method returns the `DownloadRequest` information (in [mobile](../../api/latest/device_api/mobile/tizen/download.html#DownloadRequest), [wearable](../../api/latest/device_api/wearable/tizen/download.html#DownloadRequest), and [TV](../../api/latest/device_api/tv/tizen/download.html#DownloadRequest) applications) which is used as the parameter when starting the download.

4. Use the `getMIMEType()` method with the download ID as a parameter to get the MIME type of the file that you have started downloading:

   ```
   var MIMEType = tizen.download.getMIMEType(downloadId);
   ```

## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
