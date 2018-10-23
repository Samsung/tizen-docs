
# Sharing through NFC

The basic tasks involved in sharing content through Near Field
Communication (NFC) are to ensure that the device supports NFC,
initialize the NFC feature, and exchange NDEF messages through the NFC
P2P connection. The following sections provide you with the fundamental
building blocks for sharing data with other devices.


## Initializing NFC

NFC is an international standard (ISO/IEC 18092) that specifies an
interface and a protocol for simple wireless interconnection of closely
coupled devices.

To initialize NFC:

1.  To use the functions and data types of the NFC API (in
    [mobile](../../api/mobile/latest/group__CAPI__NETWORK__NFC__MODULE.html)
    and
    [wearable](../../api/wearable/latest/group__CAPI__NETWORK__NFC__MODULE.html)
    applications), include the `<nfc.h>` header file in your
    application:

    ```cpp
    #include <nfc.h>
    ```

2. Add the `http://tizen.org/privilege/nfc` privilege to the
    application manifest file.
3. Check whether the device supports NFC by calling the
    `nfc_manager_is_supported()` function. It takes no parameters and
    returns `true` if NFC is supported on the device.

    ```cpp
    void
    Network_NFC_startup(void)
    {
        gmainloop = g_main_loop_new(NULL, FALSE);
        bool is_nfc_supported = nfc_manager_is_supported();
        if (!is_nfc_supported)
            dlog_print(DLOG_INFO, LOG_TAG, "is_nfc_supported NOT SUPPORTED");
    }
    ```

    The `gmainloop` created above is used to wait for the results of
    calling asynchronous functions.

4. Call the `nfc_manager_initialize()` function to start the
    initialization:

    ```cpp
    int error_code = NFC_ERROR_NONE;

    error_code = nfc_manager_initialize();
    if (error_code != NFC_ERROR_NONE)
        /* Error handling */

    g_timeout_add(1000, timeout_func, gmainloop);
    g_main_loop_run(gmainloop);
    ```

    Run `gmainloop` to wait for the initialization result. It is closed
    when the time set in the `g_timeout_add()` function elapses. The
    time is defined in milliseconds, so in the above example the
    `timeout_func` is called after 1 second.


## Sending and Receiving Messages through NFC P2P

The NFC Data Exchange Format (NDEF) is a packet message format used in
the reader/writer and peer-to-peer (P2P) modes. In the following
example, the NDEF message contains a business card of the device owner
(name, phone number, and email address).

To exchange a simple NDEF message through NFC P2P connection:

1.  Prepare the NDEF message:  
    1.  To create an NDEF message consisting of text records, use the
        `nfc_ndef_record_create_text()` function. The following example
        creates 3 records for a name, phone number, and email address:

        ```cpp
        nfc_ndef_record_h ndef_name_record = NULL;
        nfc_ndef_record_h ndef_phone_record = NULL;
        nfc_ndef_record_h ndef_email_record = NULL;

        const char *name = "John Doe";
        const char *phone = "+82556666888";
        const char *email = "john.doe@tizen.org";

        nfc_ndef_record_create_text(&ndef_name_record, name, "en-US", NFC_ENCODE_UTF_8);
        nfc_ndef_record_create_text(&ndef_phone_record, phone, "en-US", NFC_ENCODE_UTF_8);
        nfc_ndef_record_create_text(&ndef_email_record, email, "en-US", NFC_ENCODE_UTF_8);
        ```

    2. Create an NDEF message and append the records to the message:

        ```cpp
        nfc_ndef_message_h ndef_message = NULL;
        nfc_ndef_message_create(&ndef_message);

        nfc_ndef_message_append_record(ndef_message, ndef_name_record);
        nfc_ndef_message_append_record(ndef_message, ndef_phone_record);
        nfc_ndef_message_append_record(ndef_message, ndef_email_record);
        ```

2. Register callbacks to receive notifications about discovered P2P
    targets and the received data:

    -   To exchange messages using P2P, register a callback for
        receiving notifications about discovered P2P targets. When the
        P2P target is discovered, the callback provides a handle to that
        device and information on whether it is attached or detached.
    -   Register a callback for receiving notifications about received
        data using the `nfc_p2p_set_data_received_cb()` function. Place
        the registration code in the callback called after the P2P
        device is discovered.

    ```cpp
    nfc_manager_set_p2p_target_discovered_cb(on_target_discovered, NULL);

    nfc_p2p_set_data_received_cb(target, on_p2p_data_received, NULL);
    ```

3. Exchange messages:
    -   Send a message to another device.

        When the other P2P device is attached, send the prepared message
        to it. You can use the `nfc_p2p_send()` function, if you do not
        want to check permissions.

        ```cpp
        nfc_p2p_send(target, ndef_message, NULL, NULL);
        ```

    - Receive a message from another device.

        The callback about receiving data is invoked when the device
        receives a message. The callback provides a handle to the
        received message and a handle to the message source.

        To get a specified record from the message, use the
        `nfc_ndef_message_get_record()` function with the parameters for
        a message handle, a record index, and a handle to store the
        obtained record. When the record is obtained, get the stored
        text using the `nfc_ndef_record_get_text()` function.

        ```cpp
        nfc_ndef_record_h ndef_record;

        char *name = NULL;
        nfc_ndef_message_get_record(message, 0, &ndef_record);
        nfc_ndef_record_get_text(ndef_record, &name);

        char *phone = NULL;
        nfc_ndef_message_get_record(message, 1, &ndef_record);
        nfc_ndef_record_get_text(ndef_record, &phone);

        char *email = NULL;
        nfc_ndef_message_get_record(message, 2, &ndef_record);
        nfc_ndef_record_get_text(ndef_record, &email);
        ```
