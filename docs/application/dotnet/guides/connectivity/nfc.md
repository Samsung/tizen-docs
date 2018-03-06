# Near Field Communication (NFC)


Tizen enables you to use Near Field Communication (NFC) functionalities, such as reading and writing tags, and emulating a smartcard. NFC is an international standard (ISO/IEC 18092) that specifies an interface and a protocol for simple wireless interconnection of closely coupled devices. For more information, see the [NFC Forum](http://nfc-forum.org/).

The main features of the Tizen.Network.Nfc namespace include:

-   NFC management

    You can [activate or deactivate NFC](#manager_activating_nfc_device), [monitor NFC events](#manager_events), and [retrieve adapters for various NFC modes](#manager_get_adapters).

-   NDEF support

    The NFC Data Exchange Format (NDEF) is a packet message format used in the reader/writer and peer-to-peer modes.

    You can [create NDEF records and messages](#ndef_record).

-   Tag mode

    You can [manage tag events](#tag_get_tag_event) and [read and write NDEF messages](#tag_read_ndef) from and to an NFC tag.

-   Peer-to-peer mode

    You can [manage peer-to-peer (P2P) events](#p2p_get_p2p_event) and [send and receive NDEF messages](#p2p_receive) between peer devices.

-   Card emulation mode

    The [card emulation](#card_emulation) mode allows an NFC device to function as a smart card.

    You can [enable and disable the card emulation mode](#ce_enable), [register an AID value](#ce_register_aid), [manage secure element events](#ce_ohce_status), [manage HCE events from the NFC reader](#ce_hce_event), and [send HCE responses to the NFC reader](#ce_hce_send_response).


<a name="card_emulation"></a>
## Card Emulation
The card emulation mode can be broadly divided into 2 categories:

-   Traditional card emulation

    In traditional card emulation, the NFC controller in the device routes data from the NFC reader directly to the secure element (SE), and an applet handles all of the data in the SE. The user does not participate in the operation at all.

    Tizen supports eSE and UICC as SEs.

    **Figure: Traditional card emulation**

    ![Traditional card emulation](./media/nfc_card_emulation.png)

-   Host-based card emulation (HCE)

    HCE is an on-device technology that permits a phone to perform card emulation on an NFC-enabled device without relying on access to a secure element (SE). The data is routed to the user space on which Tizen applications reside, instead of routing the data to a secure element.

    **Figure: Card emulation with HCE**

    ![Card emulation with HCE](./media/nfc_card_emulation_hce.png)

    HCE allows you to create your own card emulation system and bypass the SE. This approach brings 2 advantages:

    -   For UICC-type SE, the mobile service provider is involved in the card emulation behavior. With HCE, you are independent of the service provider.
    -   You do not need SE hardware chips within the device.

    To understand HCE behavior, mainly how data is internally routed to the correct application, consider how Tizen handles NFC routing:

    1.  Assume that the user has an HCE application or installs one.

        The application has an "AID" value, which is stored in the NFC routing table (blue arrow in the following figure).

    2.  When the NFC reader attempts card emulation, the NFC controller checks the routing table to find the application to which the data is sent for emulation (red arrows in the following figure).
    3.  When the application is uninstalled, the AID value is deleted from the routing table.

    **Figure: HCE routing**

    ![HCE routing](./media/nfc_hce_routing.png)

## Prerequisites

To enable your application to use the NFC functionality:

1.  To use the [Tizen.Network.Nfc](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/nfc</privilege>
       <privilege>http://tizen.org/privilege/nfc.cardemulation</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the `Tizen.Network.Nfc` namespace, include it in your application:

    ```
    using Tizen.Network.Nfc;
    ```

<a name="manager_activating_nfc_device"></a>
## Activating and Deactivating NFC

To activate and deactivate NFC:

1.  To use the following NFC activation method, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/nfc.admin</privilege>
    </privileges>
    ```

    > **Note**   
	> To be able to use this privilege, your application must be signed with a partner-level certificate.

2.  To activate NFC, use the `SetActivationAsync()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class with the `true` parameter:

    ```
    NfcManager.SetActivationAsync(true);
    ```

3.  To deactivate NFC, use the `SetActivationAsync()` method with the `false` parameter:

    ```
    NfcManager.SetActivationAsync(false);
    ```

<a name="manager_events"></a>
## Monitoring NFC State Changes

To monitor NFC state changes using event handlers:

1.  Define an event handler to be triggered when the NFC activation state changes:

    ```
    public static void ActivationStatusChanged(object sender, ActivationChangedEventArgs e)
    {
        isActivated = e.Activated;
        flagStateChanged = true;
    }
    ```

2.  Register the event handler for the `ActivationChanged` event of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class:

    ```
    NfcManager.ActivationChanged += ActivationStatusChanged;
    ```

3.  When it is no longer needed, deregister the event handler:

    ```
    NfcManager.ActivationChanged -= ActivationStatusChanged;
    ```

<a name="manager_get_adapters"></a>
## Retrieving the Connection Adapter

Before any NFC operations, retrieve the appropriate connection adapter with the corresponding `GetXXXAdapter()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class.

For example, to retrieve the NFC tag mode adapter, use the `GetTagAdapter()` method:

```
public static void GetTagAdapter_RETURN_VALUE()
{
    try
    {
        /// Test code
        Assert.IsInstanceOf<NfcTagAdapter>(NfcManager.GetTagAdapter(), "GetTagAdapter return value is not of the type NfcTagAdapter");
    }
    catch (NotSupportedException)
    {
        Assert.IsTrue(isNfcSupported == false || isTagSupported == false, "GetTagAdapter throws the NotSupportedException, but Tizen supports the NFC Tag operation");
    }
}
```
<a name="ndef_record"></a>
## Creating NDEF Records and Messages
To create an NDEF record and attach it to an NDEF message:

1.  To create an NDEF record, create a new instance of the [Tizen.Network.Nfc.NfcNdefRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcNdefRecord.html) class and give it the required values.

    In the following example, a record is created with 3 bytes of binary data as a payload.

    ```
    public static void AppendRecord_RETURN_VALUE()
    {
        /// Test code
        try
        {
            byte[] type = new byte[1]{0x02};
            byte[] id = new byte[1]{0x01};
            byte[] payload = new byte[3]{0x04, 0x05, 0x06};

            NfcNdefRecord record = new NfcNdefRecord(NfcRecordTypeNameFormat.WellKnown, type, id, payload, 3);
    ```

    You can also create NDEF records to store different kinds of data, such as text or images, by using different parameters when creating the `Tizen.Network.Nfc.NfcNdefRecord` instance.

2.  Create the NDEF message as a new instance of the [Tizen.Network.Nfc.NfcNdefMessage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcNdefMessage.html) class and add the record to it using the `AppendRecord()` method:

    ```
            NfcNdefMessage msg = new NfcNdefMessage();

            int previousMsgRecordCount = msg.RecordCount;

            bool success = msg.AppendRecord(record);
            Assert.IsTrue(success, "Failed to append record to NdefMessage");

            int currentMsgRecordCount = msg.RecordCount;
            Assert.IsTrue(previousMsgRecordCount + 1 == currentMsgRecordCount, "currentMsgRecordCount should be greater than previousMsgRecordCount");
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(isSupported == false, "Method throws the NotSupportedException, but Tizen supports the NFC operation");
        }
    }
    ```

<a name="tag_get_tag_event"></a>
## Managing Tag Events

To keep track of NFC tag events through event handlers:

1.  Define an event handler to trigger whenever a new NFC tag is found:

    ```
    public static void TagDiscoveredCallback(object sender, TagDiscoveredEventArgs e)
    {
        _eventArgs = e;
    }
    ```

2.  Register the event handler for the `TagDiscovered` event of the [Tizen.Network.Nfc.NfcTagAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcTagAdapter.html) class:

    ```
    public static async Task TagDiscovered_EVENT_LISTEN()
    {
        try
        {
            /// Precondition
            /// 1. Retrieve the tag adapter
            /// 2. Register the event handler

            _tagAdapter = NfcManager.GetTagAdapter();
            _tagAdapter.TagDiscovered += TagDiscoveredCallback;

            ///  Test code
            await WaitTagDiscovered();
    ```

3.  When it is no longer needed, deregister the event handler.

    ```
            Assert.IsNotNull(_eventArgs, "_eventArgs should not be null");
            Assert.IsNotNull(_eventArgs.Tag, "Tag should not be null");

            /// Postcondition
            /// 1. Unregister the event handler
            /// 2. Reset variables

            Assert.IsNotNull(_tagAdapter, "_tagAdapter should not be null");
            _tagAdapter.TagDiscovered -= TagDiscoveredCallback;

            _tagAdapter = null;
            _eventArgs = null;
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(_nfcFeature == false || _tagFeature == false,
                          "Method throws the NotSupportedException, but Tizen supports the NFC Tag operation");
        }
    }
    ```

<a name="tag_read_ndef"></a>
## Reading and Writing NDEF Messages

To read NDEF messages from an NFC tag and write them to a tag:

-   To read an NDEF message:
    1.  Retrieve the NFC tag adapter and register a `TagDiscovered` event handler for it:

        ```
        public static async Task ReadNdefMessageAsync_METHOD_RETURN()
        {
            try
            {
                /// Precondition
                /// 1. Retrieve the tag adapter
                /// 2. Register the event handler

                _tagAdapter = NfcManager.GetTagAdapter();
                _tagAdapter.TagDiscovered += TagDiscoveredCallback;
        ```

    2.  Once the tag is discovered, read the message with the `ReadNdefMessageAsync()` method of the [Tizen.Network.Nfc.NfcTag](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcTag.html) class:

        ```
                /// Test code
                await WaitTagDiscovered();

                Assert.IsNotNull(_eventArgs, "_eventArgs should not be null");
                Assert.IsNotNull(_eventArgs.Tag, "Tag should not be null");

                NfcNdefMessage ndefMessage = await _eventArgs.Tag.ReadNdefMessageAsync();

                Assert.IsTrue(ndefMessage.RecordCount > 0, "RecordCount should be greater than 0");

                /// Postcondition
                /// 1. Unregister the event handler
                /// 2. Reset variables

                Assert.IsNotNull(_tagAdapter, "_tagAdapter should not be null");
                _tagAdapter.TagDiscovered -= TagDiscoveredCallback;

                _tagAdapter = null;
                _eventArgs = null;
            }
            catch (NotSupportedException)
            {
                Assert.IsTrue(_nfcFeature == false || _tagFeature == false,
                              "Method throws the NotSupportedException, but Tizen supports the NFC Tag operation");
            }
        }
        ```

-   To write an NDEF message:
    1.  Retrieve the NFC tag adapter and register a `TagDiscovered` event handler for it:

        ```
        public static async Task WriteNdefMessageAsync_METHOD_RETURN()
        {
            try
            {
                /// Precondition
                /// 1. Retrieve the tag adapter
                /// 2. Register the event handler

                _tagAdapter = NfcManager.GetTagAdapter();
                _tagAdapter.TagDiscovered += TagDiscoveredCallback;
        ```

    2.  Once the tag is discovered, create a new NDEF message as an instance of the [Tizen.Network.Nfc.NfcNdefMessage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcNdefMessage.html) class and a new NDEF record as an instance of the [Tizen.Network.Nfc.NfcNdefRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcNdefRecord.html) class. Then append the record into the message with the `AppendRecord()` method of the `Tizen.Network.Nfc.NfcNdefMessage` class:

        ```
                /// Test code
                await WaitTagDiscovered();

                Assert.IsNotNull(_eventArgs, "_eventArgs should not be null");
                Assert.IsNotNull(_eventArgs.Tag, "Tag should not be null");

                NfcNdefMessage ndefMessage = new NfcNdefMessage();
                NfcNdefRecord ndefRecord = new NfcNdefRecord("123", "KR", NfcEncodeType.Utf8);
                ndefMessage.AppendRecord(ndefRecord);
        ```

    3.  Write the message to the NFC tag with the `WriteNdefMessageAsync()` method of the `Tizen.Network.Nfc.NfcTag` class:

        ```
                NfcError nfcError = await _eventArgs.Tag.WriteNdefMessageAsync(ndefMessage);

                Assert.IsTrue(nfcError == NfcError.None, "nfcError should be no error");

                /// Postcondition
                /// 1. Unregister the event handler
                /// 2. Reset variables

                Assert.IsNotNull(_tagAdapter, "_tagAdapter should not be null");
                _tagAdapter.TagDiscovered -= TagDiscoveredCallback;

                _tagAdapter = null;
                _eventArgs = null;
            }
            catch (NotSupportedException)
            {
                Assert.IsTrue(_nfcFeature == false || _tagFeature == false,
                              "Method throws the NotSupportedException, but Tizen supports the NFC Tag operation");
            }
        }
        ```

<a name="p2p_get_p2p_event"></a>
## Managing P2P Events

To keep track of P2P events through event handlers:

1.  Define an event handler to trigger whenever a new P2P target has been found:

    ```
    public static void P2pTargetDiscoveredCallback(object sender, P2pTargetDiscoveredEventArgs e)
    {
        _p2pTargetDiscoveredEventArgs = e;
    }
    ```

2.  Register the event handler for the `P2pTargetDiscovered` event of the [Tizen.Network.Nfc.NfcP2pAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcP2pAdapter.html) class:

    ```
    public static async Task P2pTargetDiscovered_EVENT_LISTEN()
    {
        try
        {
            /// Precondition
            /// 1. Retrieve the P2P adapter
            /// 2. Register the event handler

            _p2pAdapter = NfcManager.GetP2pAdapter();
            _p2pAdapter.P2pTargetDiscovered += P2pTargetDiscoveredCallback;

            /// Test code
            await WaitTargetDiscovered();
    ```

3.  When it is no longer needed, deregister the event handler:

    ```
            Assert.IsNotNull(_p2pTargetDiscoveredEventArgs, "P2pTargetDiscoveredEventArgs should not be null");

            /// Postcondition
            /// 1. Unregister event handler
            /// 2. Reset variables

            Assert.IsNotNull(_p2pAdapter, "_tagAdapter should not be null");
            _p2pAdapter.P2pTargetDiscovered -= P2pTargetDiscoveredCallback;

            _p2pAdapter = null;
            _p2pTargetDiscoveredEventArgs = null;
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(_nfcFeature == false || _p2pFeature == false,
                          "Method throws the NotSupportedException, but Tizen supports the NFC P2P operation");
        }
    }
    ```

<a name="p2p_receive"></a>
## Sending and Receiving NDEF Messages Between Peer Devices

You can both send and receive NDEF devices between peer devices in P2P mode.

-   To send an NDEF message to a peer device:
    1.  Retrieve the P2P adapter and register a `P2pTargetDiscovered` event handler for it:

        ```
        public static async Task SendNdefMessageAsync_METHOD_RETURN()
        {
            try
            {
                /// Precondition
                /// 1. Retrieve the P2P adapter
                /// 2. Register the event handler

                _p2pAdapter = NfcManager.GetP2pAdapter();
                _p2pAdapter.P2pTargetDiscovered += P2pTargetDiscoveredCallback;
        ```

    2.  Create a new NDEF message as an instance of the [Tizen.Network.Nfc.NfcNdefMessage](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcNdefMessage.html) class and a new NDEF record as an instance of the [Tizen.Network.Nfc.NfcNdefRecord](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcNdefRecord.html) class. Then append the record into the message with the `AppendRecord()` method of the `Tizen.Network.Nfc.NfcNdefMessage` class.

        ```
                /// Test code
                await WaitTargetDiscovered();

                Assert.IsNotNull(_p2pTargetDiscoveredEventArgs, "P2pTargetDiscoveredEventArgs should not be null");

                NfcP2p currentP2p = _p2pAdapter.GetConnectedTarget();

                Assert.IsNotNull(currentP2p, "currentP2p should not be null");

                NfcNdefMessage ndefMessage = new NfcNdefMessage();
                NfcNdefRecord ndefRecord = new NfcNdefRecord("123", "KR", NfcEncodeType.Utf8);
                ndefMessage.AppendRecord(ndefRecord);
        ```

    3.  Send the NDEF message with the `SendNdefMessageAsync()` method of the [Tizen.Network.Nfc.NfcP2p](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcP2p.html) class:

        ```
                NfcError nfcError = await currentP2p.SendNdefMessageAsync(ndefMessage);

                Assert.IsTrue(nfcError == NfcError.None, "nfcError should be no error");

                /// Postcondition
                /// 1. Unregister the event handler
                /// 2. Reset variables

                Assert.IsNotNull(_p2pAdapter, "_tagAdapter should not be null");
                _p2pAdapter.P2pTargetDiscovered -= P2pTargetDiscoveredCallback;

                _p2pAdapter = null;
                _p2pTargetDiscoveredEventArgs = null;
            }
            catch (NotSupportedException)
            {
                Assert.IsTrue(_nfcFeature == false || _p2pFeature == false,
                              "Method throws the NotSupportedException, but Tizen supports the NFC P2P operation");
            }
        }
        ```

-   To receive an NDEF message from a peer device:
    1.  Define an event handler to trigger whenever P2P data is received:

        ```
        public static void P2pDataReceivedCallback(object sender, P2pDataReceivedEventArgs e)
        {
            _p2pDataReceivedEventArgs = e;
        }
        ```

    2.  Once a P2P connection has been made, retrieve the connected P2P target with the `GetConnectedTarget()` method of the [Tizen.Network.Nfc.NfcP2pAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcP2pAdapter.html) class, and add the new event handler for the `P2pDataReceived` event of the newly-created instance of the [Tizen.Network.Nfc.NfcP2p](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcP2p.html) class:

        ```
        public static async Task NdefMessage_READ_ONLY()
        {
            try
            {
                /// Precondition
                /// 1. Retrieve the P2P adapter
                /// 2. Register the event handler

                _p2pAdapter = NfcManager.GetP2pAdapter();
                _p2pAdapter.P2pTargetDiscovered += P2pTargetDiscoveredCallback;

                /// Test code
                await WaitTargetDiscovered();

                Assert.IsNotNull(_p2pTargetDiscoveredEventArgs, "P2pTargetDiscoveredEventArgs should not be null");
                NfcP2p p2pTarget = _p2pAdapter.GetConnectedTarget();
                p2pTarget.P2pDataReceived += P2pDataReceivedCallback;
        ```

    3.  The received NDEF message can be read through the newly-created instance of the [Tizen.Network.Nfc.P2pDataReceivedEventArgs](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.P2pDataReceivedEventArgs.html) class:

        ```
                await WaitDataReceived();

                Assert.IsNotNull(_p2pDataReceivedEventArgs, "P2pDataReceivedEventArgs should not be null");

                Assert.IsInstanceOf<NfcNdefMessage>(_p2pDataReceivedEventArgs.NdefMessage, "NdefMessage value is not of the type NfcNdefMessage");

                /// Postcondition
                /// 1. Unregister event handlers
                /// 2. Reset variables

                Assert.IsNotNull(p2pTarget, "p2pTarget should not be null");
                p2pTarget.P2pDataReceived -= P2pDataReceivedCallback;
                Assert.IsNotNull(_p2pAdapter, "_p2pAdapter should not be null");
                _p2pAdapter.P2pTargetDiscovered -= P2pTargetDiscoveredCallback;

                _p2pAdapter = null;
                _p2pTargetDiscoveredEventArgs = null;
                _p2pDataReceivedEventArgs = null;
            }
            catch (NotSupportedException)
            {
                Assert.IsTrue(_nfcFeature == false || _p2pFeature == false,
                              "Method throws the NotSupportedException, but Tizen supports the Nfc P2P operation");
            }
        }
        ```

<a name="ce_enable"></a>
## Enabling and Disabling the Card Emulation Mode

To enable and disable the smart card emulation mode:

1.  Retrieve the card emulation adapter with the `GetCardEmulationAdapter()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class:

    ```
    public static void EnableCardEmulation_CHECK_CARD_EMULATION_STATUS()
    {
        try
        {
            NfcCardEmulationAdapter ceAdapter = NfcManager.GetCardEmulationAdapter();
    ```

2.  Enable and disable the card emulation mode with the `EnableCardEmulation()` and `DisableCardEmulation()` methods of the [Tizen.Network.Nfc.NfcCardEmulationAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcCardEmulationAdapter.html) class:

    ```
            ceAdapter.DisableCardEmulation();

            ceAdapter.EnableCardEmulation();

            NfcSecureElementCardEmulationMode ceMode = ceAdapter.GetCardEmulationMode();
            Assert.IsTrue(ceMode == NfcSecureElementCardEmulationMode.On, "The card emulation mode should be true.");
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(isNfcSupported == false || isCeSupported == false, "Method throws the NotSupportedException, but Tizen supports the NFC operation");
        }
    }
    ```

<a name="ce_register_aid"></a>
## Registering AID

To register an AID value:

1.  Retrieve the card emulation adapter with the `GetCardEmulationAdapter()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class:

    ```
    public static void RegisterAid_METHOD_CALL_WITH_HCE_PAYMENT()
    {
        try
        {
            NfcCardEmulationAdapter ceAdapter = NfcManager.GetCardEmulationAdapter();
    ```

2.  Register the AID with the `RegisterAid()` method of the [Tizen.Network.Nfc.NfcCardEmulationAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcCardEmulationAdapter.html) class:

    ```
            ceAdapter.RegisterAid(NfcSecureElementType.Hce, NfcCardEmulationCategoryType.Payment, "325041592E5359532E4444463031");
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(isNfcSupported == false || isHceSupported == false, "Method throws the NotSupportedException, but Tizen supports the NFC operation");
        }
    }
    ```

<a name="ce_ohce_status"></a>
## Managing Secure Element Events

To manage secure element (SE) events:

1.  Define an event handler to be triggered when an SE event occurs:

    ```
    public static void SecureElementCallback(object sender, SecureElementEventArgs e)
    {
        _seEventArgs = e;
    }
    ```

2.  Retrieve the card emulation adapter with the `GetCardEmulationAdapter()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class, and register the SE event handler for its `SecureElementEvent` event:

    ```
    public static async Task SecureElementEvent()
    {
        try
        {
            /// Precondition
            /// 1. Retrieve the card emulation adapter
            /// 2. Register the SE event handler

            _cardEmulationAdapter = NfcManager.GetCardEmulationAdapter();
            _cardEmulationAdapter.SecureElementEvent += SecureElementCallback;

            /// Test code
            await WaitSeEvent();

            Assert.IsNotNull(_seEventArgs, "The _seEventArgs should not be null when HCE event callback is called");
            Assert.IsTrue(_checkFlag == true, "isChecked should be true");
    ```

3.  When it is no longer needed, deregister the event handler:

    ```
            /// Postcondition
            /// 1. Unregister the SE event handler
            /// 2. Reset variables

            Assert.IsNotNull(_cardEmulationAdapter, "_cardEmulationAdapter should not be null");
            _cardEmulationAdapter.SecureElementEvent -= SecureElementCallback;

            _cardEmulationAdapter = null;
            _seEventArgs = null;
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(_nfcFeature == false || _ceFeature == false || _hceFeature == false,
                          "Method throws the NotSupportedException, but Tizen supports the NFC card emulation operation");
        }
    }
    ```

<a name="ce_hce_event"></a>
## Managing HCE Events from the NFC Reader

To manage HCE events from the NFC reader:

1.  Define an event handler to be triggered when an HCE event occurs:

    ```
    public static void HostCardEmulationCallback(object sender, HostCardEmulationEventArgs e)
    {
        _hceEventArgs = e;
    }
    ```

2.  Retrieve the card emulation adapter with the `GetCardEmulationAdapter()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class, and register the HCE event handler for its `HostCardEmulationEvent` event:

    ```
    public static async Task HostCardEmulationEvent_HOST_CARD_EMULATION_EVENT_LISTEN_TYPE_ACTIVATED()
    {
        try
        {
            /// Precondition
            /// 1. Retrieve the card emulation adapter
            /// 2. Register the HCE event handler

            _cardEmulationAdapter = NfcManager.GetCardEmulationAdapter();
            _cardEmulationAdapter.HostCardEmulationEvent += HostCardEmulationCallback;

            /// Test code
            await WaitHceEventActivated();

            Assert.IsNotNull(_hceEventArgs, "The _hceEventArgs should not be null when HCE event callback is called");
            Assert.IsTrue(_checkFlag == true, "isChecked should be true");
    ```

3.  When it is no longer needed, deregister the event handler:

    ```
            /// Postcondition
            /// 1. Unregister the HCE event handler
            /// 2. Reset variables

            Assert.IsNotNull(_cardEmulationAdapter, "_cardEmulationAdapter should not be null");
            _cardEmulationAdapter.HostCardEmulationEvent -= HostCardEmulationCallback;

            _cardEmulationAdapter = null;
            _hceEventArgs = null;
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(_nfcFeature == false || _ceFeature == false || _hceFeature == false,
                          "Method throws the NotSupportedException, but Tizen supports the NFC host card emulation operation");
        }
    }
    ```

<a name="ce_hce_send_response"></a>
## Sending HCE Responses to the NFC Reader

To send HCE responses to the NFC reader:

1.  Retrieve the card emulation adapter with the `GetCardEmulationAdapter()` method of the [Tizen.Network.Nfc.NfcManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcManager.html) class, and register the HCE event handler for its `HostCardEmulationEvent` event:

    ```
    public static async Task HceSendApduResponse_METHOD_RETURN()
    {
        try
        {
            /// Precondition
            /// 1. Retrieve the card emulation adapter
            /// 2. Register the HCE event handler

            _cardEmulationAdapter = NfcManager.GetCardEmulationAdapter();
            _cardEmulationAdapter.HostCardEmulationEvent += HostCardEmulationCallback;
    ```

2.  Once the HCE event triggers, send the response with the `HceSendApduResponse()` method of the [Tizen.Network.Nfc.NfcSecureElement](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Nfc.NfcSecureElement.html) class:

    ```
            /// Test code
            byte[] responseBuffer = {0x90, 0x00};

            await WaitHceEvent();

            Assert.IsNotNull(_eventArgs, "The _eventArgs should not be null when HCE event callback is called");
            Assert.IsNotNull(_eventArgs.SecureElement, "The SecureElement property of _eventArgs should not be null when HCE event callback is called");
            Assert.IsInstanceOf<NfcSecureElement>(_eventArgs.SecureElement, "SecureElement value is not of the type NfcSecureElement");

            _eventArgs.SecureElement.HceSendApduResponse(responseBuffer, 2);

            /// Postcondition
            /// 1. Unregister the HCE event handler
            /// 2. Reset variables

            _cardEmulationAdapter.HostCardEmulationEvent -= HostCardEmulationCallback;

            _cardEmulationAdapter = null;
            _eventArgs = null;
        }
        catch (NotSupportedException)
        {
            Assert.IsTrue(_nfcFeature == false || _ceFeature == false || _hceFeature == false,
                          "Method throws the NotSupportedException, but Tizen supports the NFC host card emulation operation");
        }
    }
    ```



## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
