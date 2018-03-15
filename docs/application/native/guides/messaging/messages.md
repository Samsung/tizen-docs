# Messages


You can access the device messaging capabilities, including sending SMS and MMS messages.

The main messaging features include:

- Text messaging (SMS)

  You can [create a message, send it, and receive the sent status](#sending). You can also receive incoming messages, and [search for messages within a message list](#fetching).

- Multimedia messaging (MMS)

  You can [create and send MMS messages](#sending). An image, audio, video, vCard, vCalendar, or a combination of them is supported as an attachment type in MMS messages. An image or audio attachment cannot be combined with video attachments.

- Messaging notifications

  You can register and deregister callback functions to be notified when an outgoing message is successfully sent or an incoming message has been received.

The sent status of the SMS and MMS messages can be checked asynchronously. You receive a separate status report for each SMS recipient, and one status report for each MMS message regardless of the number of recipients.

## Prerequisites

To enable your application to use the messaging functionality:

1. To use the Messages API (in [mobile](../../api/mobile/latest/group__CAPI__MESSAGING__MESSAGES__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MESSAGING__MESSAGES__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/message.read</privilege>
      <privilege>http://tizen.org/privilege/message.write</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Messages API, include the `<messages.h>` header file in your application:

   ```
   #include <messages.h>
   ```

3. The Messages service works like a client-service architecture. In this architecture, a Tizen application is the client side and has to connect to the service before using the Messages API.

   Establish a connection using the `messages_open_service()` function:

   ```
   static messages_service_h service_handle = NULL;
   int error_code;

   error_code = messages_open_service(&service_handle);

   if (error_code != MESSAGES_ERROR_NONE)
       /* Error handling */
   ```

4. When a connection with the Messages service is no longer needed (or the application is exiting), call the `messages_close_service()` function for proper connection closing:

   ```
   messages_close_service(service_handle);
   service_handle = NULL;
   ```

<a name="fetching"></a>
## Fetching Messages from a Specified Message Box

To fetch messages from a message box, use the `messages_foreach_message()` function with the appropriate parameters. One of these parameters is the callback function called for each message matching the search criteria.

To fetch messages:

1. Define the message search callback function.

   1. Within the callback, to print the message content (or to show it to the user in any other way), extract the message text, address, and type:

      ```
      char *message = NULL;
      char *address = NULL;
      messages_recipient_type_e rtype;
      int error_code = MESSAGES_ERROR_NONE;

      error_code = messages_get_text(msg, &message);
      if (error_code != MESSAGES_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to get message content");

      error_code = messages_get_address(msg, 0, &address, &rtype);
      if (error_code != MESSAGES_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to get recipient address");

      messages_message_type_e mtype = MESSAGES_TYPE_UNKNOWN;
      messages_get_message_type(msg, &mtype);
      ```

   2. For MMS messages, the subject and attachments attributes exist and can be extracted from the found message:

      ```
      if (MESSAGES_TYPE_MMS == mtype) {
          char *subject = NULL;
          error_code = messages_mms_get_subject(msg, &subject);
          if (error_code != MESSAGES_ERROR_NONE)
              dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to get MMS subject");
          int atcount = 0;
          messages_mms_get_attachment_count(msg, &atcount);
      }
      ```

   3. The memory allocated for the message given to the callback function and for all string variables extracted from the message has to be explicitly released before leaving the applicable visibility scope:

      ```
      free(subject);
      free(message);
      free(address);
      ```

2. Perform the search.

   Call the `messages_foreach_message()` function to retrieve all existing messages stored in different mailboxes. With the function parameters, you can limit the search results to a subset of all available messages based on:

   - Message box type (inbox, outbox, sent items, drafts, or all of them)
   - Message type (such as SMS or MMS)
   - Keyword (for search by text or subject)
   - Address (message recipient address)

   The following example shows a simple search for all SMS messages in all message boxes with a callback function named `message_search_callback()`.

   ```
   int error_code;
   error_code = messages_open_service(&service_handle);
   if (error_code != MESSAGES_ERROR_NONE)
       dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to open connection");

   error_code = messages_foreach_message(service_handle, MESSAGES_MBOX_ALL,
                                         MESSAGES_TYPE_SMS, NULL, NULL, 0, 0,
                                         messages_search_callback, NULL);
   if (error_code != MESSAGES_ERROR_NONE)
       dlog_print(DLOG_DEBUG, LOG_TAG, "Messages searching failed");

   messages_close_service(service_handle);
   ```
<a name="sending"></a>
## Sending SMS or MMS Messages

You can send SMS (Short Message Service) messages and MMS (Multimedia Message Service) messages with attachments (image or video files).

To send a message:

1. Create a message.

   To create an SMS or an MMS message, use the `messages_create_message()` function. Specify the message type (`MESSAGES_TYPE_SMS` or `MESSAGES_TYPE_MMS`) when creating the message. The following example creates an SMS message.

   ```
   int error_code;
   messages_message_h msg_hndl = NULL;

   /* Create an SMS message handle */
   error_code = messages_create_message(MESSAGES_TYPE_SMS, &msg_hndl);
   if (error_code != MESSAGES_ERROR_NONE)
       dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to create message");
   ```

2. Define the recipients and message body.

   Functions for setting the recipient address and the message body (the message text) are the same for SMS and MMS.

   ```
   error_code = messages_add_address(msg_hndl, "123456789", MESSAGES_RECIPIENT_TO);
   if (error_code != MESSAGES_ERROR_NONE)
       dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to add recipient address");

   error_code = messages_set_text(msg_hndl, __PRETTY_FUNCTION__);
   if (error_code != MESSAGES_ERROR_NONE)
       dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to set message text");
   ```

3. Set a subject and add an attachment for an MMS message (note that MMS sending is not supported on the emulator).

   - Set a message subject:

     ```
     error_code = messages_mms_set_subject(msg_hndl, "MMS test");
     if (error_code != MESSAGES_ERROR_NONE)
         dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to set MMS subject");
     ```

   - Add attachments with their absolute path in the device file system. When adding the attachment, give the attachment type. Possible attachment types are image, audio, and video.

     ```
     error_code = messages_mms_add_attachment(g_message, MESSAGES_MEDIA_IMAGE,
                                              "/path/to/image/file");
     if (error_code != MESSAGES_ERROR_NONE)
         dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to add attachment to MMS");
     ```

4. Send the message.

   1. Define a callback for the `messages_send_message()` function. You can use the callback to let the messaging service inform you about the message sending status. Use the first parameter to determine whether the sending succeeded:

      ```
      static void
      sent_msg_cb(messages_sending_result_e result, void *user_data)
      {
          if (MESSAGES_SENDING_SUCCEEDED == result)
              dlog_print(DLOG_DEBUG, LOG_TAG, "Message sending succeeded");
          else
              dlog_print(DLOG_DEBUG, LOG_TAG, "Message sending failed");
      }
      ```

   2. If the connection to the messaging service is open (you have the `service_handle` handle) and the message itself (`msg_hndl`) is successfully created, send the message using the `messages_send_message()` function:

      ```
      error_code = messages_send_message(service_handle, msg_hndl, true,
                                         sent_msg_cb, NULL);
      if (error_code != MESSAGES_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Failed to send message");
      ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
