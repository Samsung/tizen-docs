# Secure Element Access

You can access secure elements in a device. You can access various secure elements, such as UICC and SIM cards, embedded secure elements, and secure SD cards.

This feature is optional.

The main features of the Secure Element API include the following:

- Managing secure elements   

  You can [manage secure elements](#managing-secure-elements) by retrieving all the available secure element readers and receiving notifications of reader changes using the `SEService` interface. You can also shut down secure elements.

- Opening sessions and channels   

  You can [open a session](#opening-sessions-and-channels) to connect to a secure element reader. Within a session, you can open basic or logical channels.

- Transmitting APDUs to the applet

  You can [transmit application protocol data units (APDU)](#transmitting-apdus-to-secure-elements) to a secure element using a channel.

- Closing sessions and channels

  When the channel or session is no longer needed, you can [close them](#closing-sessions-and-channels).

## Prerequisites

To use the Secure Element API, the application has to request permission by adding the following privilege to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/secureelement"/>
```

## Manage secure elements

To use secure elements in your application, you must learn to retrieve them and track changes in them:

1. To retrieve all the available secure element readers, use the `getReaders()` method of the `SEService` interface. The method registers the `ReaderArraySuccessCallback` interface, which is invoked when the list of available secure element readers has been successfully retrieved:

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

   1. Define a listener using the `SEChangeListener` interface:

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

3. To stop listening for the reader changes, use the `unregisterSEListener()` method:

   ```
   tizen.seService.unregisterSEListener(seListener);
   ```

## Opening Sessions and Channels

To use secure elements in your application, you must learn to open sessions and channels:

1. To open a session, use the `openSession()` method of the `Reader` interface. The method registers the `SessionSuccessCallback` interface, which is invoked when a session on a specific reader is opened:

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

   1. Open a basic channel with the `openBasicChannel()` method of the `Session` interface. The method registers the `ChannelSuccessCallback` interface, which is invoked when a channel is opened to communicate with a specific applet:

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

   2. Open a logical channel with the `openLogicalChannel()` method of the `Session` interface. As with a basic channel, the method registers the `ChannelSuccessCallback` interface:

      ```
      session.openLogicalChannel([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe], successCB, errorCB);
      ```

## Transmit APDUs to secure elements

To use secure elements in your application, you must learn to transmit application protocol data units (APDU) to secure elements:

1. To transmit an APDU command to a secure element, use the `transmit()` method of the `Channel` interface:

   ```
   /* APDU command is defined in ISO7816-4 */
   channel.transmit(command, successCB, errorCB);
   ```

2. The `transmit()` method registers the `TransmitSuccessCallback` interface, which is invoked when a command has been successfully transmitted:

   ```
   function successCB(response) {
       console.log('An APDU is transmitted successfully. The response is ' + response);
   }
   function errorCB(err) {
       /* Error handling */
   }
   ```

## Closing sessions and channels

To use secure elements in your application, you must learn to close sessions and channels:

1. To close a specific channel, use the `close()` method of the `Channel` interface:

   ```
   channel.close();
   ```

2. To close all channels within a specific session, use the `closeChannels()` method of the `Session` interface:

   ```
   session.closeChannels();
   ```

3. To close a specific session, use the `close()` method of the `Session` interface:

   ```
   session.close();
   ```

4. To close all session for a specific reader, use the `closeSessions()` method of the `Reader` interface:

   ```
   reader.closeSessions();
   ```


## Related information
* Dependencies   
  - Tizen 2.4 and Higher
