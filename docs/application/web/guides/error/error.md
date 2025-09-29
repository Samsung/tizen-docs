# Error Handling

You can handle generic error situations in your application.

The Tizen API is mandatory for Tizen TV and IoT profiles, which means that it is supported on all TV and IoT devices. All mandatory APIs are supported on the Tizen emulators.

The main error handling features of the Tizen API include the following:

- Exception handling

  You can enable the Tizen APIs to throw errors synchronously with the `WebAPIException` interface (in [TV](../../api/latest/device_api/tv/tizen/tizen.html#WebAPIException) applications), or return errors in the error event handlers of asynchronous methods with the `WebAPIError` interface (in [TV](../../api/latest/device_api/tv/tizen/tizen.html#WebAPIError) applications).

   > [!NOTE]
   > Do not use the `code` attribute of the `WebAPIException` interface to distinguish errors, because the code of the exception object is set to `0` for new error types that are not defined in [DOMException](https://heycam.github.io/webidl/#idl-DOMException){:target="_blank"}.

- Generic event handling  

  You can [handle the results of asynchronous operations](#using-the-generic-event-handlers) with generic events. The operations can implemented using the `SuccessCallback` (in [TV](../../api/latest/device_api/tv/tizen/tizen.html#SuccessCallback) applications) and `ErrorCallback` (in [TV](../../api/latest/device_api/tv/tizen/tizen.html#ErrorCallback) applications) event handlers of the Tizen API.

## Use the generic Event Handlers

Learning how to use generic, predefined event handlers allows you handle application operations and errors efficiently, follow these steps:

1. The generic `onSuccess()` event handler of the `SuccessCallBack` interface (in [TV](../../api/latest/device_api/tv/tizen/tizen.html#SuccessCallback) applications) can be used with methods that do not require a return value when successful.

   In this example, the event handler is used to stop a running application with the `kill()` method of the `Application` interface (in [TV](../../api/latest/device_api/tv/tizen/application.html#Application) applications):

   ```
   function onSuccess() {
       console.log('Application terminated successfully');
   }

   tizen.application.kill(ctxIDToKill, onSuccess);
   ```

2.  The generic `onError()` event handler of the `ErrorCallBack` interface (in [TV](../../api/latest/device_api/tv/tizen/tizen.html#ErrorCallback) applications) can be used with methods that only require an error as an input parameter in the error callback.

    In this example, the event handler is used to handle possible errors with the `getCalendars()` method of the `CalendarManager` interface:

    ```
    function errorCallback(error) {
        console.log('The following error occurred: ' + error.name);
    }

    tizen.calendar.getCalendars('EVENT', calendarListCallback, errorCallback);
    ```

## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for TV
* API References
  - [TV](../../api/latest/device_api/tv/tizen/tizen.html)
