# Console Logging

You can write messages to the system console for debugging purposes.

The Console API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Console API include:

- Writing log messages and errors

  You can [write simple log and error messages](#writing-log-messages-and-errors) to the system console.

- Formatting objects

  You can [print a JavaScript representation of a specified object](#formatting-objects).

- Timing

  You can [measure the time elapsed during an operation](#measuring-timing).

> **Note**  
> To see the message writing results, use the system console in the Tizen Studio or use the `sdb dlog` command.

The global `console` object contains some additional features defined by Cordova.

## Prerequisites

To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova features now available');
    console.log('Connection type: ' + navigator.connection.type);
}
```

The `console` global object is available earlier, but it points to a default system console.

## Writing Log Messages and Errors

To write simple log and error messages to the system console, use the `log()` and `error()` methods:

```
console.log('console.log works well');
console.error('console.error works well');
```

> **Note**  
> To see the writing results, use the system console available in your Tizen Studio or use the `sdb dlog` command.

## Formatting Objects

To print a JavaScript representation of a specified object:

- To print without formatting:

  ```
  var john = {name: 'John', surname: 'Doe'};
  console.dir(john.name);
  ```

- To print with formatting, use `%o`:

  ```
  var john = {name: 'John', surname: 'Doe'};
  console.dir('my object %o', john);
  ```

## Measuring Timing

To measure the time elapsed during an operation:

1. Start the timer and give it a label (a string), which is used to identify the timer:

   ```
   console.time('Big array initialization');
   ```

2. Perform some operation:

   ```
   var array = new Array(1000000);
   for (var i = array.length - 1; i >= 0; i -= 1) {
       array[i] = new Object();
   }
   ```

3. Stop the timer by passing the same label to the `timeEnd()` method:
   ```
   console.timeEnd('Big array initialization');
   ```
   The following output is shown in the system console:
   ```
   Big array initialization: 176ms
   ```


## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
