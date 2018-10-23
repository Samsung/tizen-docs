# Error Handling

You can handle generic error situations in your application.

The Tizen API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main error handling features of the Tizen API include:

- Exception handling

  You can enable the Tizen APIs to throw errors synchronously with the `WebAPIException` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#WebAPIException), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#WebAPIException), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#WebAPIException) applications), or return errors in the error event handlers of asynchronous methods with the `WebAPIError` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#WebAPIError), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#WebAPIError), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#WebAPIError) applications).

   > **Note**  
   > Do not use the `code` attribute of the `WebAPIException` interface to distinguish errors, because the code of the exception object is set to `0` for new error types that are not defined in [DOMException](http://www.w3.org/TR/dom/#domexception).

- Generic event handling  

  You can [handle the results of asynchronous operations](#using-the-generic-event-handlers) with generic events. The operations can implemented using the `SuccessCallback` (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#SuccessCallback), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#SuccessCallback), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#SuccessCallback) applications) and `ErrorCallback` (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#ErrorCallback), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#ErrorCallback), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#ErrorCallback) applications) event handlers of the Tizen API.

## Using the Generic Event Handlers

Learning how to use generic, predefined event handlers allows you handle application operations and errors efficiently:

1. The generic `onSuccess()` event handler of the `SuccessCallBack` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#SuccessCallback), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#SuccessCallback), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#SuccessCallback) applications) can be used with methods that do not require a return value when successful.

   In this example, the event handler is used to stop a running application with the `kill()` method of the `Application` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#Application), [wearable](../../api/latest/device_api/wearable/tizen/application.html#Application), and [TV](../../api/latest/device_api/tv/tizen/application.html#Application) applications).

   ```
   function onSuccess() {
       console.log('Application terminated successfully');
   }

   tizen.application.kill(ctxIDToKill, onSuccess);
   ```

2.  The generic `onError()` event handler of the `ErrorCallBack` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#ErrorCallback), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#ErrorCallback), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#ErrorCallback) applications) can be used with methods that only require an error as an input parameter in the error callback.

    In this example, the event handler is used to handle possible errors with the `getCalendars()` method of the `CalendarManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#CalendarManager) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#CalendarManager) applications).

    ```
    function errorCallback(error) {
        console.log('The following error occurred: ' + error.name);
    }

    tizen.calendar.getCalendars('EVENT', calendarListCallback, errorCallback);
    ```

## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
