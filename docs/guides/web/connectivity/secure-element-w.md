# Secure Element Access

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

Tizen enables you to access secure elements in a device. You can access various secure elements, such as UICC and SIM cards, embedded secure elements, and secure SD cards.

This feature is supported in mobile and wearable applications only.

The main features of the Secure Element API include:

- Managing secure elements   

  You can [manage secure elements](./connectivity/secure-element-w.md#Managing_Secure_Element) by retrieving all the available secure element readers and receiving notifications of reader changes using the `SEService` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#SEService) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#SEService) applications). You can also shut down secure elements.

- Opening sessions and channels   

  You can [open a session](./connectivity/secure-element-w.md#Opening_Sessions) to connect to a secure element reader. Within a session, you can open basic or logical channels.

- Transmitting APDUs to the applet	

  You can [transmit application protocol data units (APDU)](./connectivity/secure-element-w.md#Transmitting_APDU) to a secure element using a channel.

- Closing sessions and channels	

  When the channel or session is no longer needed, you can [close them](./connectivity/secure-element-w.md#Closing_Sessions).

## Prerequisites

To use the Secure Element API (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/secureelement"/>
```

## Managing Secure Elements

To use secure elements in your application, you must learn to retrieve them and track changes in them:

1. To retrieve all the available secure element readers, use the `getReaders()` method of the `SEService` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#SEService) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#SEService) applications). The method registers the `ReaderArraySuccessCallback` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#ReaderArraySuccessCallback) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#ReaderArraySuccessCallback) applications), which is invoked when the list of available secure element readers has been successfully retrieved.

   ```
   function success(readers) {
       for (var i = 0; i < readers.length; i++) {
           if (readers[i].isPresent)
               console.log('Reader Name: ' + readers[i].getName());
       }
   }
   tizen.seService.getReaders(success, function(err) {
       /* Error handling */
   });
   ```

2. To receive reader change notifications, use the `registerSEListener()` method of the `SEService` interface:

   1. Define a listener using the `SEChangeListener` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#SEChangeListener) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#SEChangeListener) applications):

      ```
      var setSEChange = {
          onSEReady: function(reader) {
              console.log(reader.getName() + ' is ready.');
          },
          onSENotReady: function(reader) {
              console.log(reader.getName() + ' is not ready.');
          },
      }
      ```

   2. Register the listener:

      ```
      var seListener = tizen.seService.registerSEListener(setSEChange);
      ```

3. To stop listening to the reader changes, use the `unregisterSEListener()` method:

   ```
   tizen.seService.unregisterSEListener(seListener);
   ```

## Opening Sessions and Channels

To use secure elements in your application, you must learn to open sessions and channels:

1. To open a session, use the `openSession()` method of the `Reader` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Reader) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Reader) applications). The method registers the `SessionSuccessCallback` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#SessionSuccessCallback) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#SessionSuccessCallback) applications), which is invoked when a session on a specific reader is opened.

   ```
   function successCB(session) {
       console.log('A session is open successfully');
   }

   function errorCB(err) {
       /* Error handling */
   }
   reader.openSession(successCB, errorCB);
   ```

2. To open a channel within a session:

   1. Open a basic channel with the `openBasicChannel()` method of the `Session` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Session) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Session) applications). The method registers the `ChannelSuccessCallback` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#ChannelSuccessCallback) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#ChannelSuccessCallback) applications), which is invoked when a channel is opened to communicate with a specific applet.

      ```
      function successCB(channel) {
          if (channel.isBasicChannel)
              console.log('A basic channel is opened successfully');
          else
              console.log('A logical channel is opened successfully');
      }

      function errorCB(err) {
          /* Error handling */
      }

      /* This aid is for testing purposes for your applet */
      session.openBasicChannel([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe], successCB, errorCB);
      ```

   2. Open a logical channel with the `openLogicalChannel()` method of the `Session` interface. As with a basic channel, the method registers the `ChannelSuccessCallback` interface.

      ```
      session.openLogicalChannel([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe], successCB, errorCB);
      ```

## Transmitting APDUs to Secure Elements

To use secure elements in your application, you must learn to transmit application protocol data units (APDU) to secure elements:

1. To transmit an APDU command to a secure element, use the `transmit()` method of the `Channel` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Channel) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Channel) applications).

   ```
   /* APDU command is defined in ISO7816-4 */
   channel.transmit(command, successCB, errorCB);
   ```

2. The `transmit()` method registers the `TransmitSuccessCallback` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#TransmitSuccessCallback) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#TransmitSuccessCallback) applications), which is invoked when a command has been successfully transmitted:

   ```
   function successCB(response) {
       console.log('An APDU is transmitted successfully. The response is ' + response);
   }
   function errorCB(err) {
       /* Error handling */
   }
   ```

## Closing Sessions and Channels

To use secure elements in your application, you must learn to close sessions and channels:

1. To close a specific channel, use the `close()` method of the `Channel` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Channel) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Channel) applications):

   ```
   channel.close();
   ```

2. To close all channels within a specific session, use the `closeChannels()` method of the `Session` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Session) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Session) applications):

   ```
   session.closeChannels();
   ```

3. To close a specific session, use the `close()` method of the `Session` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Session) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Session) applications):

   ```
   session.close();
   ```

4. To close all session for a specific reader, use the `closeSessions()` method of the `Reader` interface (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/se.html#Reader) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/se.html#Reader) applications):

   ```
   reader.closeSessions();
   ```