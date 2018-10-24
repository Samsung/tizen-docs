# Messages

You can use messaging functionalities, such as SMS, MMS, and email.

This feature is supported in mobile applications only.

The messaging process used in HTML5 involves Uniform Resource Identifiers (URIs), which form values of attributes, such as `tel`, `mailto`, and `sms`. These attributes invoke external services which then perform the messaging tasks. The Messaging API minimizes your coding efforts by providing one-step capabilities to perform all high-level messaging-related operations.

The main features of the Messaging API include:

- Message writing and sending   

  You can [create and send messages](#creating-and-sending-messages), and save message drafts.

  You can also retrieve information on available SIM cards and [select the SIM card with which to send a message](#selecting-the-sim-card-for-sending-messages).

- Message management   

  You can [find, update, and delete messages](#managing-messages) in the message storage.

- Finding folders   

  You can [find message folders](#finding-folders) belonging to a message service.

- Full message content retrieval from the email server   

  You can [load email messages and attachments](#synchronizing-with-the-server) from the email service and synchronize your email accounts.

- Message storage change notifications   

  You can [receive notifications](#receiving-notifications-on-message-storage-changes) when messages are added, updated, or deleted.

## Prerequisites

To use the [Messaging](../../api/latest/device_api/mobile/tizen/messaging.html) API, the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/messaging.read"/>
<tizen:privilege name="http://tizen.org/privilege/messaging.write"/>
```

## Creating and Sending Messages

You can create a message by using the [Message](../../api/latest/device_api/mobile/tizen/messaging.html#Message) object constructor, and you can set the message attributes and parameters using a [MessageInit](../../api/latest/device_api/mobile/tizen/messaging.html#MessageInit) object (for example, you can set the message service type - SMS, MMS or email - by using the `type` parameter).

> **Note**  
> The system assigns a unique read-only message ID to each message the first time it is processed, such as when sending it or creating a draft message for it.

To create and send messages:

1. Retrieve the messaging service using the `getMessageServices()` method. The first parameter specifies the type of the messaging service to retrieve. There are 3 possible types: "messaging.sms", "messaging.mms" and "messaging.email". In the following example, the SMS service is retrieved.

   ```
   function errorCallback(error) {
       console.log(error.name + ': ' + error.message);
   }

   tizen.messaging.getMessageServices('messaging.sms', serviceListCB, errorCallback);
   ```

2. In the success callback of the `getMessageServices()` method, use the `Message` interface to define the content and attributes of the message, and then send the message using the `sendMessage()` method of the [MessageService](../../api/latest/device_api/mobile/tizen/messaging.html#MessageService) interface. The `sendMessage()` method requires both success and error event handlers. Depending on the result of the sending operation, the message is moved to the device's Sent Items or Drafts folder, and additionally stored in the message storage database.

   If the message is not ready to be sent yet, save the message draft using the `addDraftMessage()` method of the [MessageStorage](../../api/latest/device_api/mobile/tizen/messaging.html#MessageStorage) interface.

   ```
   function onAddSuccess() {
       console.log('Successfully added');
   }

   function serviceListCB(services) {
       /* Define SMS message */
       var msg = new tizen.Message('messaging.sms', {
           plainBody: 'I will arrive in 10 minutes.',
           to: ['+34666666666', '+34888888888']
       });

       var msgReady = true;

       if (msgReady) {
           /* Send SMS message */
           services[0].sendMessage(msg, messageSent, errorCallback);
       } else {
           /* Save a draft */
           services[0].messageStorage.addDraftMessage(msg, onAddSuccess, errorCallback);
       }
   }
   ```

   If sending MMS or email messages with attachments, add the attachments as an array of [MessageAttachment](../../api/latest/device_api/mobile/tizen/messaging.html#MessageAttachment) objects with the file path and the MIME type (`image/png`, `text/pdf`, or `text/html`) defined for each object.

   Assign the array to the `attachments` attribute of the `Message` object.

   ```
   var msg = new tizen.Message('messaging.email');
   msg.attachments = [new tizen.MessageAttachment('images/myimage.png', 'image/png'),
                      new tizen.MessageAttachment('docs/mydoc.pdf', 'text/pdf')];
   ```

3. Define the message sending success callback that is called if the message is sent successfully. (For email, that means that the message is sent to the email delivery system, not to the final recipient of the message.)

   For messaging technologies, such as SMS, where the message is sent individually to every message recipient, the success callback must be invoked individually for each recipient.

   ```
   function messageSent(recipients) {
       for (var i = 0; i < recipients.length; i++) {
           console.log('The SMS has been sent to ' + recipients[i]);
       }
   }
   ```

   Defining a sending error callback allows you to handle all possible errors and exceptions that can occur causing the message delivery to fail.

## Selecting the SIM Card for Sending Messages

If there are multiple SIM cards in the device, by default the system determines which one is used to send a message. You can also specify the SIM card when sending an SMS.

To add the dual SIM feature to your messaging application, you must learn to retrieve information on available SIM cards and select the SIM card to send SMS and MMS messages:

1. To check how many SIM cards are available, call the `getCount()` method of the [SystemInfo](../../api/latest/device_api/mobile/tizen/systeminfo.html#SystemInfo) interface.

   ```
   var count = tizen.systeminfo.getCount('SIM');
   if (count > 1) {
       console.log('Dual SIM is supported');
   }
   ```

2. To retrieve additional information on the available SIM cards, use the `getPropertyValueArray()` method of the `SystemInfo` interface:

   ```
   function getPropertySuccess(sims) {
       for (var i = 0; i < sims.length; i++) {
           console.log('SIM' + (i+1) + ' - ' + sims[i].msisdn + ' (' + sims[i].operatorName + ') ' + sims[i].state);
       }
   }
   tizen.systeminfo.getPropertyValueArray('SIM', getPropertySuccess);
   ```

   The information can be presented to the user to let them select the SIM card they want.

3. To send the message using the second SIM card, call the `sendMessage()` method of the [MessageService](../../api/latest/device_api/mobile/tizen/messaging.html#MessageService) interface specifying the SIM index as `2`:

   ```
   function sendSuccess() {
       console.log('Message has been sent');
   }

   function serviceSuccess(messageService) {
       message = new Message(messageService.type, {
           to: ['0001'],
           plainBody: 'Surprise!'
       });
       /* SIM is selected (first SIM - 1, second SIM - 2) */
       messageService.sendMessage(message, sendSuccess, null, 2);
   }

   tizen.messaging.getMessageServices('messaging.sms', serviceSuccess);
   ```

## Managing Messages

You can find, update, and delete stored messages with methods provided by the [MessageStorage](../../api/latest/device_api/mobile/tizen/messaging.html#MessageStorage) interface: `findMessages()`, `updateMessages()`, and `removeMessages()`. The interface allows you to manage message storages.

To work with messages in the message store:

1. Retrieve messages whose sender is "me" from the message storage using the `findMessages()` method of the `MessageStorage` interface .

   When searching for messages, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#messaging-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes).

   ```
   var emailService;
   function serviceListCB(services) {
       emailService = services[0];
       /* Set the attribute filter */
       var filter = new tizen.AttributeFilter('from', 'CONTAINS', 'me');

       emailService.messageStorage.findMessages(filter, messageArrayCB);
   }
   tizen.messaging.getMessageServices('messaging.email', serviceListCB);
   ```

   The `findMessages()` method returns an array of [Message](../../api/latest/device_api/mobile/tizen/messaging.html#Message) objects as the search result.

   The search result does not contain the actual bodies of the messages. To [load a message body](#synchronizing-with-the-server), call the `loadMessageBody()` method of the [MessageService](../../api/latest/device_api/mobile/tizen/messaging.html#MessageService) interface.

2. To update a message in the message storage, use the `updateMessages()` method. The method uses an array of `Message` objects found previously by the `findMessages()` method as a parameter.

   In the following example, the `isRead` attribute of the first `Message` object in the given array is updated to `true`.

   ```
   function successCallback() {
       console.log('Success');
   }

   function messageArrayCB(messages) {
       messages[0].isRead = true;
       emailService.messageStorage.updateMessages(messages, successCallback);
   }
   ```

3. To delete a message from the message storage, use the `removeMessages()` method:

   ```
   function messageArrayCB(messages) {
       emailService.messagingStorage.removeMessages(messages, successCallback);
   }
   ```

## Finding Folders

To find message folders, use the `findFolders()` method of the [MessageStorage](../../api/latest/device_api/mobile/tizen/messaging.html#MessageStorage) interface:

1. To retrieve the messaging service, use the `getMessageServices()` method of the [Messaging](../../api/latest/device_api/mobile/tizen/messaging.html#Messaging) interface:

   ```
   var service;

   function serviceListCB(services) {
       console.log('Found ' + services.length + ' email services');
       service = services[0];
   }

   tizen.messaging.getMessageServices('messaging.email', serviceListCB);
   ```

2. Define a success handler implementing the [MessageFolderArraySuccessCallback](../../api/latest/device_api/mobile/tizen/messaging.html#MessageFolderArraySuccessCallback) interface, and optionally an error handler too:

   ```
   function onFindFolders(folders) {
       console.log(folders.length + ' folder(s) found.');

       for (var i = 0; i < folders.length; i++) {
           console.log('Folder ' + (i + 1) + ': ' + folders[i].name);
       }
   }

   function onFindFoldersFail(error) {
       console.log('Error occurred:  ' + error.name);
   }
   ```

3. Define a filter (for attributes supported by the message folder filter, see [Messaging Filter Attributes](../data/data-filter.md#messaging-filter-attributes)):

   ```
   var filter = new tizen.AttributeFilter('serviceId', 'EXACTLY', service.id);
   ```

4. To get all message folders, use the `findFolders()` method of the `MessageStorage` interface:

   ```
   service.messageStorage.findFolders(filter, onFindFolders, onFindFoldersFail);
   ```

## Synchronizing with the Server

To keep your email service accounts up-to-date, synchronize them with their respective external servers, such as Gmail and Microsoft Exchange, with the `sync()` method. You can also synchronize a single folder, such as the Inbox, with the `syncFolder()` method. You can specify the maximum number of messages that can be retrieved in each folder.

It is possible that an email message is accessible through the [Message](../../api/latest/device_api/mobile/tizen/messaging.html#Message) object, but its full body or attachment has not been downloaded yet. You can load email messages and attachments from the email service with the `loadMessageBody()` and `loadMessageAttachment()` methods of the [MessageService](../../api/latest/device_api/mobile/tizen/messaging.html#MessageService) interface.

To load email messages and attachments and synchronize email:

1. Retrieve the messaging service using the `getMessageServices()` method.

   ```
   tizen.messaging.getMessageServices('messaging.email', serviceListCB, errorCallback);
   ```

2. Search for all email messages with attachments using the `findMessages()` method of the [MessageStorage](../../api/latest/device_api/mobile/tizen/messaging.html#MessageStorage) interface:

   ```
   service.messageStorage.findMessages(new tizen.AttributeFilter('hasAttachment', 'EXACTLY', true),
                                       messageQueryCallback);
   ```

3. To load a message body, use the `loadMessageBody()` method of the `MessageService` interface:

   ```
   /* Success callback for the search operation */
   function messageQueryCallback(messages) {
       for (var i = 0; i < messages.length; i++) {
           var message = messages[i];
           if (!message.body.loaded) {
               tizen.messaging.loadMessageBody(message, successCallback, errorCallback);
   ```

4. To download the message attachments, use the `loadMessageAttachment()` method with an array of attachments (with valid file paths) as a parameter:

   ```
               tizen.messaging.loadMessageAttachment(message.attachments[0], successCallback,
                                                     errorCallback);
         }
      }
   }
   ```

5. To synchronize email with an external server:

   1. To synchronize all account folders, use the `sync()` method:

      ```
      /* Synchronize the folders in the success event handler */
      function servicesListSuccessCB(services) {
          services[0].sync(serviceSyncedCB, null, 30);
      }

      /* Get the email service */
      tizen.messaging.getMessageServices('messaging.email', servicesListSuccessCB);
      ```

   2. To synchronize a specific folder, use the `syncFolder()` method. In the following example, only folders containing "INBOX" in their name are synchronized.

      ```
      var emailService; /* Assume email service is initialized */
      function serviceCallback(services) {
          emailService = services[0];
      }

      /* Synchronize in the search success event handler */
      function folderQueryCallback(folders) {
          for (var i = 0; i < folders.length; i++) {
              if (folders[i].type === 'INBOX') {
                  emailService.syncFolder(folders[i], folderSyncedCB, null, 30);
              }
          }
      }

      /* Get the email service */
      tizen.messaging.getMessageServices('messaging.email', serviceCallback, errorCallback);

      /* Search for specific folders */
      var filter = new tizen.AttributeFilter('serviceId', 'EXISTS');
      emailService.messageStorage.findFolders(filter, folderQueryCallback));
      ```

## Receiving Notifications on Message Storage Changes

You can register event listeners to monitor changes in the message storage, a particular conversation, or a particular message folder.

The `addMessagesChangeListener()`, `addConversationsChangeListener()`, and `addFoldersChangeListener()` methods of the [MessageStorage](../../api/latest/device_api/mobile/tizen/messaging.html#MessageStorage) interface register an event listener, which starts asynchronously once the method returns the subscription identifier for the listener. You can use the [MessagesChangeCallback](../../api/latest/device_api/mobile/tizen/messaging.html#MessagesChangeCallback), [MessageConversationsChangeCallback](../../api/latest/device_api/mobile/tizen/messaging.html#MessageConversationsChangeCallback), and [MessageFoldersChangeCallback](../../api/latest/device_api/mobile/tizen/messaging.html#MessageFoldersChangeCallback) interfaces to define listener event handlers for receiving notifications about the changes.

To receive notifications when messages and message folders are added, updated, or removed:

1. Define the needed variable:

   ```
   /* Watch identifier */
   var watchId;
   ```

2. Define the event handlers for different notifications by implementing the [MessagesChangeCallback](../../api/latest/device_api/mobile/tizen/messaging.html#MessagesChangeCallback) listener interface:

   ```
   var messageChangeCallback = {
       /* When messages are updated */
       messagesupdated: function(messages) {
           console.log(messages.length + ' message(s) updated');
       },

       /* When messages are added */
       messagesadded: function(messages) {
           console.log(messages.length + ' message(s) added');
       },

       /* When messages are deleted */
       messagesremoved: function(messages) {
           console.log(messages.length + ' message(s) removed');
       }
   };
   ```

3. Register the listener to use the defined event handlers:

   ```
   watchId = msgService.messageStorage.addMessagesChangeListener(messageChangeCallback);
   ```

4. To stop receiving the notifications, use the `removeChangeListener()` method of the `MessageStorage` interface:

   ```
   msgService.messageStorage.removeChangeListener(watchId);
   ```

> **Note**  
> To provide notifications for changes in specific conversations or message folders, use the applicable methods and event handlers similarly as above.


## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
