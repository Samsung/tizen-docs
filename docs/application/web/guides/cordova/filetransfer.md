# File Transfers

You can transfer files using HTTP requests, and download and upload files. You can also track a transfer's progress and abort it as needed. The default HTTP method is `POST`, but `PUT` is also supported.

The File Transfer API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the File Transfer API include:

- Download

  You can [download a file](#downloading-files) from a remote server.

- Upload

  You can [upload a file](#uploading-files) to a remote server.

- Abort

  You can [terminate an on-going transfer](#aborting-transfers).

- Progress tracking

  You can [track the progress](#tracking-transfer-progress) of a file transfer.

All file operations are accessible by the `FileTransfer` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/filetransfer.html#FileTransfer), [wearable](../../api/latest/device_api/wearable/tizen/cordova/filetransfer.html#FileTransfer), and [TV](../../api/latest/device_api/tv/tizen/cordova/filetransfer.html#FileTransfer) applications).

## Prerequisites

To enable your application to use the file transfer functionality:

1. To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

   ```
   document.addEventListener('deviceready', onDeviceReady, false);

   function onDeviceReady() {
       console.log('Cordova features now available');
   }
   ```

2. To use the File Transfer API (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/filetransfer.html), [wearable](../../api/latest/device_api/wearable/tizen/cordova/filetransfer.html), and [TV](../../api/latest/device_api/tv/tizen/cordova/filetransfer.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

   ```
   <!--To download files-->
   <tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
   <tizen:privilege name="http://tizen.org/privilege/filesystem.write"/>

   <!--To upload files-->
   <tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
   <tizen:privilege name="http://tizen.org/privilege/internet"/>

   <!--To abort a transfer-->
   <tizen:privilege name="http://tizen.org/privilege/internet"/>
   ```

## Downloading Files

To download a file from a server, you must create a `FileTransfer` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/filetransfer.html#FileTransfer), [wearable](../../api/latest/device_api/wearable/tizen/cordova/filetransfer.html#FileTransfer), and [TV](../../api/latest/device_api/tv/tizen/cordova/filetransfer.html#FileTransfer) applications) and call its `download()` method with callbacks:

- The method is asynchronous, so you must provide a callback function which is invoked when the operation is successful.

  The callback parameter contains the downloaded `FileEntry` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#FileEntry), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#FileEntry), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#FileEntry) applications).

- If you need to track errors, you can provide an optional error callback as a parameter of the `download()` method.

To download a file from a remote server:

```
/* Valid URL needed, such as cdvfile://localhost/persistent/path/to/file.txt */
/* File does not need to exist before the operation */
var destinationURL;

var fileTransfer = new FileTransfer();
var uri = encodeURI('http://some.server.com/download.php');

fileTransfer.download(uri, destinationURL, function(entry) {
    console.log('download complete: ' + entry.toURL());
}, function(error) {
    console.log('download error source ' + error.source);
    console.log('download error target ' + error.target);
    console.log('upload error code' + error.code);
}, false, {
    headers: {
        'Authorization': 'Basic dGVzdHVzZXJuYW1lOnRlc3RwYXNzd29yZA=='
    }
});
```

The following output is shown in the system log:

```
download complete: file:///home/owner/apps_rw/Gk6hf8hjk/tmp/file.txt
```

## Uploading Files

The upload operation is very similar to download. To upload a file to a server, you must create a `FileTransfer` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/filetransfer.html#FileTransfer), [wearable](../../api/latest/device_api/wearable/tizen/cordova/filetransfer.html#FileTransfer), and [TV](../../api/latest/device_api/tv/tizen/cordova/filetransfer.html#FileTransfer) applications) and call its `upload()` method providing as parameters the URL of the uploaded file, server location, and a success callback function, which is invoked when the upload is finished successfully. You can also provide an optional error callback.

To upload a file to a remote server:

```
/* Valid URL needed, such as cdvfile://localhost/persistent/path/to/file.txt */
/* File must exist before the operation */
var fileURL;

var win = function(r) {
    console.log('Code = ' + r.responseCode);
    console.log('Response = ' + r.response);
    console.log('Sent = ' + r.bytesSent);
};

var fail = function(error) {
    alert('An error has occurred: Code = ' + error.code);
    console.log('upload error source ' + error.source);
    console.log('upload error target ' + error.target);
};

var ft = new FileTransfer();
ft.upload(fileURL, encodeURI('http://some.server.com/upload.php'), win, fail);
```

The following output is shown in the system log:

```
Code = 200
Response = OK
Sent = 1024
```

## Aborting Transfers

To abort an in-progress transfer, you must create the `FileTransfer` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/filetransfer.html#FileTransfer), [wearable](../../api/latest/device_api/wearable/tizen/cordova/filetransfer.html#FileTransfer), and [TV](../../api/latest/device_api/tv/tizen/cordova/filetransfer.html#FileTransfer) applications), start the download or upload transfer operation (as described above), and call the `abort()` method.  The method stops the transfer and sends the `FileTransferError.ABORT_ERR` error to the error callback (if provided).

To terminate a transfer:

```
/* Valid URL needed, such as cdvfile://localhost/persistent/path/to/file.txt */
var fileURL;

var win = function(r) {
    console.log('Should not be called.');
};

var fail = function(error) {
    /* error.code == FileTransferError.ABORT_ERR */
    alert('An error has occurred: Code = ' + error.code);
    console.log('upload error source ' + error.source);
    console.log('upload error target ' + error.target);
};

var ft = new FileTransfer();
ft.upload(fileURL, encodeURI('http://some.server.com/upload.php'), win, fail);
ft.abort();
```

The following output is shown in the system log:

```
An error has occurred: Code = 4
upload error source file:///home/owner/apps_rw/Gk6hf8hjk/tmp/file.txt
upload error target http://some.server.com/file.txt
```

## Tracking Transfer Progress

To track the progress of a file transfer, the `FileTransfer` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/filetransfer.html#FileTransfer), [wearable](../../api/latest/device_api/wearable/tizen/cordova/filetransfer.html#FileTransfer), and [TV](../../api/latest/device_api/tv/tizen/cordova/filetransfer.html#FileTransfer) applications) has the `onprogress` property, which is used to set up a method invoked each time a chunk of data is transferred. As a parameter, the method gets a `ProgressEvent` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#ProgressEvent), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#ProgressEvent), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#ProgressEvent) applications).

To track the progress of a transfer:

```
/* Valid URL needed, such as cdvfile://localhost/persistent/path/to/file.txt */
var fileURL;

var win = function(r) {
    console.log('Success. File uploaded.');
};

var fail = function(error) {
    /* error.code == FileTransferError.ABORT_ERR */
    alert('An error has occurred: Code = ' + error.code);
    console.log('upload error source ' + error.source);
    console.log('upload error target ' + error.target);
};

var ft = new FileTransfer();

ft.onprogress = function(event) {
    console.log('uploaded: ' + event.loaded);
};

ft.upload(fileURL, encodeURI('http://some.server.com/upload.php'), win, fail);
```

The following output is shown in the system log:

```
uploaded: 512
uploaded: 1024
Success.  File uploaded.
```

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
