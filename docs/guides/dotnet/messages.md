Messages
========

## Dependencies

- Tizen 4.0 and Higher

You can access the device messaging capabilities, including sending SMS
and MMS messages.

The main features of the Tizen.Messaging.Messages namespace include:

-   Text messaging (SMS)

    You can [create and send SMS messages](#sending). You can also
    receive incoming messages, and [search for messages within a message
    list](#fetching).

- Multimedia messaging (MMS)

    You can [create and send MMS messages](#sending). An image, audio,
    video, vCard, vCalendar, or a combination of them is supported as an
    attachment type in MMS messages. An image or audio attachment cannot
    be combined with video attachments.

- Message notifications

    You can [register event handlers](#managing_events) to be notified
    when an incoming message has been received.

The sent status of the SMS and MMS messages can be checked
asynchronously. You receive a separate status report for each SMS
recipient, and one status report for each MMS message regardless of the
number of recipients.



**Note** You can test sending MMS messages on a target device only. The
emulator does not support this feature.


Prerequisites
-------------

To enable your application to use the messaging functionality:

1.  To use the
    [Tizen.Messaging.Messages](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Messaging_1_1Messages.html)
    namespace, the application has to request permission by adding the
    following privileges to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <privilege>http://tizen.org/privilege/message.read</privilege>
       <privilege>http://tizen.org/privilege/message.write</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Messaging.Messages
    namespace, include it in your application:

    ``` {.prettyprint}
    using Tizen.Messaging.Messages;
    ```


Managing Events <a id="managing_events"></a>
---------------

To manage events related to messages:

1.  Define the `EventHandlerMessageReceived()` event handler, which is
    triggered when receiving a message:

    ``` {.prettyprint}
    public static void EventHandlerMessageReceived(object sender, MessageReceivedEventArgs e)
    {
        Console.WriteLine("Text of received message: " + e.ReceivedMessage.Text);
    }
    ```

2. Register the event handler for the `MessageReceived` event of the
    [Tizen.Messaging.Messages.MessagesManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MessagesManager.html)
    class:

    ``` {.prettyprint}
    MessagesManager.MessageReceived += EventHandlerMessageReceived;
    ```

3. When it is no longer needed, deregister the event handler:

    ``` {.prettyprint}
    MessagesManager.MessageReceived -= EventHandlerMessageReceived;
    ```


Sending SMS or MMS Messages <a id="sending"></a>
---------------------------

You can send SMS (Short Message Service) messages and MMS (Multimedia
Message Service) messages with attachments (image or video files).

To send a message:

1.  Create a message by creating an instance of the
    [Tizen.Messaging.Messages.SmsMessage](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1SmsMessage.html)
    or
    [Tizen.Messaging.Messages.MmsMessage](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MmsMessage.html) class.

    The following example creates an MMS message:

    ``` {.prettyprint}
    var msg = new MmsMessage();
    ```

2. Define the recipient, as a new instance of the
    [Tizen.Messaging.Messages.MessagesAddress](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MessagesAddress.html)
    class, and add the message body and SIM slot ID into the
    `Tizen.Messaging.Messages.MmsMessage` instance:

    ``` {.prettyprint}
    var address = new MessagesAddress("1234567890");
    msg.To.Add(address);
    msg.Text = "Tizen C# test mms message";
    msg.SimId = SimSlotId.Sim1;
    ```

3. Set a subject and add an attachment for the MMS message:
    -   Set a message subject:

        ``` {.prettyprint}
        msg.Subject = "Tizen C# test subject";
        ```

    - Add attachments using their absolute path in the device
        file system. Before adding an attachment, create it as a new
        instance of the
        [Tizen.Messaging.Messages.MessagesAttachment](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MessagesAttachment.html)
        class and give it the appropriate attachment type by using
        values of the
        [Tizen.Messaging.Messages.MediaType](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Messaging_1_1Messages.html#a0408c916cbaeda8c0cddc17b655efcb8) enumeration.

        ``` {.prettyprint}
        var attachment = new MessagesAttachment(MediaType.Image, "/path/to/image/file");
        msg.Attachments.Add(attachment);
        ```

4. Send the message with the `SendMessageAsync()` method of the
    [Tizen.Messaging.Messages.MessagesManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MessagesManager.html)
    class:

    ``` {.prettyprint}
    var result = await MessagesManager.SendMessageAsync(msg, false);
    ```


Fetching Messages from a Specified Message Box <a id="fetching"></a>
----------------------------------------------

To fetch messages from a message box, use the `SearchMessageAsync()`
method of the
[Tizen.Messaging.Messages.MessagesManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MessagesManager.html)
class with an appropriate filter:

1.  Create a new filter as an instance of the
    [Tizen.Messaging.Messages.MessagesSearchFilter](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Messaging_1_1Messages_1_1MessagesSearchFilter.html)
    class:

    ``` {.prettyprint}
    var filter = new MessagesSearchFilter();
    ```

2. Set filter properties.

    A message filter allows you to limit your search results to a subset
    of all available messages based on any or all of the following:

    -   Message box type (inbox, outbox, sent items, drafts, or all
        of them)
    -   Message type (such as SMS or MMS)
    -   Keyword (for search based on text and subject)
    -   Address (message recipient address)

    The following example shows how to define a filter that limits the
    search results to SMS messages in the inbox, containing “Tizen” in
    the text or subject and “1234” in the recipient address:

    ``` {.prettyprint}
    filter.MessageBoxType = MessageBoxType.Inbox;
    filter.MessageType = MessageType.Sms;
    filter.TextKeyword = "Tizen";
    filter.AddressKeyword = "1234";
    ```

3. Perform the search:

    ``` {.prettyprint}
    var resultMessages = await MessagesManager.SearchMessageAsync(filter);
    ```
