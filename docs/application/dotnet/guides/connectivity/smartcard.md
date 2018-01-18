# Smart Card


You can use smart card functionalities, such as accessing a secure element (SE). Before using the Tizen.Network.Smartcard namespace, make sure you have an SE in the device. The smart card service allows you to open a session on an SE, open a channel to the applet in the SE, send a command to the channel, and finally receive a response to the command.

The main features of the Tizen.Network.Smartcard namespace include:

-   Smart card reader

    The [Tizen.Network.Smartcard.SmartcardManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardManager.html) class allows you to [get the available readers](#manager). Each reader functions as a connector to the SE framework system.

    The [Tizen.Network.Smartcard.SmartcardReader](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardReader.html) class allows you to access the SE connected with the selected reader. You can [get the reader name and open and close sessions](#reader).

-   Smart card session

    A session is an open connection between an application on the device and an SE.

    The [Tizen.Network.Smartcard.SmartcardSession](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardSession.html) class allows you to [open and close basic and logical channels](#session), and get ATR (answer to reset).

-   Smart card channel

    A channel is an open connection between an application on the device and an applet on the SE.

    The [Tizen.Network.Smartcard.SmartcardChannel](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardChannel.html) class allows you to [close channels and transmit application protocol data units](#channel) (APDU).

The following figure illustrates the smart card service architecture in Tizen. The Smartcard service sends and receives data through the terminal of each SE.

**Figure: Smart card service architecture**

![Smart card service architecture](./media/smartcard_architecture.png)

The Tizen.Network.Smartcard namespace is a reference implementation of the SIMalliance Open Mobile 3.0 API specification that enables Tizen applications to communicate with secure elements. For more information, see the [SimAlliance](http://simalliance.org/).

The Tizen implementation differs from the original, since only the transport layer is provided. There is no service layer support in Tizen.


## Prerequisites

To enable your application to use the smart card functionality:

1.  To use the [Tizen.Network.Smartcard](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/secureelement</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Network.Smartcard namespace, include it in your application:

    ```
    using Tizen.Network.Smartcard;
    ```

<a name="manager"></a>
## Retrieving Readers

To retrieve the available smart card readers, use the `GetReaders()` method of the [Tizen.Network.Smartcard.SmartcardManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardManager.html) class:

```
public static void GetReaders_RETURN_LIST_OF_READERS()
{
    try
    {
        var count = 0;
        readers = SmartcardManager.GetReaders();

        foreach (SmartcardReader reader in readers)
        {
            count++;
        }

        Assert.Greater(count, 0, "The reader count should be greater than 0");
    }
    catch (NotSupportedException)
    {
        Assert.IsTrue(isSupported == false, "Method throws the NotSupportedException, but Tizen supports the smart card operation");
    }
    catch (Exception ex)
    {
        Assert.True(false, "Exception occurs. Msg: " + ex.ToString());
    }
}
```

<a name="reader"></a>
## Managing the Reader

To manage a reader:

1.  Retrieve the name of the reader with the `Name` property of the [Tizen.Network.Smartcard.SmartcardReader](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardReader.html) class:

    ```
    public static void Name_READ_ONLY()
    {
        try
        {
            readers = SmartcardManager.GetReaders();

            foreach (SmartcardReader reader in readers)
            {
                Assert.IsInstanceOf<string>(reader.Name);
                Assert.IsNotNull(reader.Name, "Reader Name should be not null.");
    ```

2.  Before establishing a session, use the `IsSecureElementPresent` property of the `Tizen.Network.Smartcard.SmartcardReader` class to make sure that the SE is present in the reader:

    ```
                Assert.IsInstanceOf<bool>(reader.IsSecureElementPresent);
                Assert.True(reader.IsSecureElementPresent, "IsSecureElementPresent property should be true.");

                if (reader.IsSecureElementPresent == false)
                {
                    Assert.True(false, "SecureElement is not present on the reader with the name, " + reader.Name);

                    return;
                }
    ```

3.  Open a session to connect to the SE in the reader using the `OpenSession()` method of the `Tizen.Network.Smartcard.SmartcardReader` class.

    When you no longer need the reader, use the `CloseSessions()` method to close all sessions opened on the specific reader.

    ```
                SmartcardSession session = reader.OpenSession();
                Assert.IsNotNull(session, "Session should be not null");

                reader.CloseSessions();
            }
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(isSupported == false, "Method throws the NotSupportedException, but Tizen supports the smart card operation");
        }
        catch (Exception ex)
        {
            Assert.True(false, "Exception occurs. Msg: " + ex.ToString());
        }
    }
    ```

<a name="session"></a>
## Managing Sessions

You can manage a session using the [Tizen.Network.Smartcard.SmartcardSession](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardSession.html) instance that you have created when opening the session with a reader.

To manage sessions:

-   Retrieve the reader that provides the session:

    ```
    /// Open a session
    SmartcardSession session = reader.OpenSession();

    Assert.IsInstanceOf<SmartcardReader>(session.Reader);
    Assert.IsNotNull(session.Reader, "Session.Reader value should be not null.");
    Assert.True(session.Reader == reader, "Session.Reader value should be equal to reader");
    ```

-   Retrieve the answer to reset (ATR) value of the SE with the `Atr` property of the `Tizen.Network.Smartcard.SmartcardSession` class:

    ```
    /// Open a session
    SmartcardSession session = reader.OpenSession();

    Assert.IsInstanceOf<byte[]>(session.Atr);
    Assert.IsNotNull(session.Atr, "Session Atr should be not null.");
    ```

-   To open and close basic and logical channels:
    1.  A basic channel is defined in the ISO/IEC 7816-4 specification (the one that has number 0). To open a logical channel with the SE, you must select the applet represented by the given application ID (AID).

        To open a logical channel, use the `OpenLogicalChannel()` method of the `Tizen.Network.Smartcard.SmartcardSession` class:

        ```
        /// Open a session
        SmartcardSession session = reader.OpenSession();

        byte[] aid = new byte[3]{0x04, 0x05, 0x06};
        byte p2 = 0x00;

        session.OpenLogicalChannel(aid, p2);
        ```

    2.  To close all channels opened for a specific session, use the `CloseChannels()` method:

        ```
        session.CloseChannels();
        ```

-   Close a session and check that it is truly closed:

    ```
    /// Open a session
    SmartcardSession session = reader.OpenSession();

    Assert.IsInstanceOf<bool>(session.IsClosed);
    Assert.IsFalse(session.IsClosed, "session IsClosed should be not true.");
    ```

<a name="channel"></a>
## Managing Channels

You can manage a channel using the [Tizen.Network.Smartcard.SmartcardChannel](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Smartcard.SmartcardChannel.html) instance that you have created when opening the channel with a session.

To manage channels:

-   Retrieve the session that opened a specific channel by using the `Session` property of the `Tizen.Network.Smartcard.SmartcardChannel` class:

    ```
    /// Open a session and channel
    SmartcardSession session = reader.OpenSession();
    byte[] aid = new byte[3]{0x04, 0x05, 0x06};
    byte p2 = 0x00;

    SmartcardChannel channel = session.OpenLogicalChannel(aid, p2);

    /// Retrieve the channel session information
    Assert.IsTrue(session == channel.Session, "session should be equal to channel.Session");
    ```

-   To close the channel opened for a specific SE, use the `Close()` method of the `Tizen.Network.Smartcard.SmartcardChannel` class:

    ```
    /// Open a session and channel
    SmartcardSession session = reader.OpenSession();
    byte[] aid = new byte[3]{0x04, 0x05, 0x06};
    byte p2 = 0x00;

    SmartcardChannel channel = session.OpenLogicalChannel(aid, p2);
    Assert.IsTrue(channel.IsClosed == false, "channel.IsClosed should be false when channel is open");

    /// Close the channel
    channel.Close();
    Assert.IsTrue(channel.IsClosed == true, "channel.IsClosed should be true when channel is closed");
    ```

-   To transmit an APDU command (as per ISO/IEC 7816-4) to the SE, use the `Transmit()` method:

    ```
    /// Open a session and channel
    SmartcardSession session = reader.OpenSession();
    byte[] aid = new byte[3]{0x04, 0x05, 0x06};
    byte p2 = 0x00;

    SmartcardChannel channel = session.OpenLogicalChannel(aid, p2);
    byte[] selectCmd = new byte[8]{0x00, 0xA4, 0x04, 0x00, 0x03, 0x0A, 0x0B, 0x0C};

    /// Transmit the command
    channel.Transmit(selectCmd);
    ```

## Related Information
* Dependencies
    -   Tizen 4.0 and Higher
