# Push Server


You can push events from an application server to your application on a Tizen device. If the message sending fails for any reason, an error code identifying the failure reason is returned. You can use the [error code](#error_codes) to determine how to handle the failure.

The main features of the Tizen.Messaging.Push namespace for server developers include:

-   Sending push notifications

    You can [send push notifications](#send_server) from the application server to an application.

<a name="send_server"></a>
## Sending Push Notifications

You can send notifications to your applications installed on Tizen devices. The basics of sending push notifications are covered in the [Push](push.md#send) guide. This use case covers more advanced information, such as sending multiple notifications in one request and sending multicast notifications.

To send push notifications:

1.  Determine the RQM server.

    The request manager (RQM) servers collect your push notifications before sending them to the applications. The RQM server must be chosen based on the first 2 digits of the registration ID.

    **Table: Push RQM server URLs**

    | Prefix of the `regId` | Region                 | URL                                      |
    |---------------------|----------------------|----------------------------------------|
    | 00                    | US East                | `https://useast.push.samsungosp.com:8090/spp/pns/api/push` |
    | 02                    | Asia Pacific Southeast | `https://apsoutheast.push.samsungosp.com:8090/spp/pns/api/push` |
    | 03                    | EU West                | `https://euwest.push.samsungosp.com:8090/spp/pns/api/push` |
    | 04                    | Asia Pacific Northeast | `https://apnortheast.push.samsungosp.com:8090/spp/pns/api/push` |
    | 05                    | Korea                  | `https://apkorea.push.samsungosp.com:8090/spp/pns/api/push` |
    | 06                    | China                  | `https://apchina.push.samsungosp.com.cn:8090/spp/pns/api/push` |
    | 50                    | US East                | `https://useast.gateway.push.samsungosp.com:8090/spp/pns/api/push` |
    | 52                    | Asia Pacific Southeast | `https://apsoutheast.gateway.push.samsungosp.com:8090/spp/pns/api/push` |
    | 53                    | EU West                | `https://euwest.gateway.push.samsungosp.com:8090/spp/pns/api/push` |
    | 54                    | Asia Pacific Northeast | `https://apnortheast.gateway.push.samsungosp.com:8090/spp/pns/api/push` |
    | 55                    | Korea                  | `https://apkorea.gateway.push.samsungosp.com:8090/spp/pns/api/push` |
    | 56                    | China                  | `https://apchina.gateway.push.samsungosp.com.cn:8090/spp/pns/api/push` |

    For example, if the registration ID of the application that you want to send a notification to begins with 04, the URL of the RQM server must be `https://apnortheast.push.samsungosp.com:8090/spp/pns/api/push`.

2. Determine the type of push notification.

    You can determine the notification type. You can send a notification either to notify a user about urgent information or to deliver data to the application for update:

    -   If you have an urgent message or data for the user, fill the message field with a proper action value:

        ```
        {
            "messages":
            [{
                /* Other content */
                "message": "action=ALERT&badgeOption=INCREASE&badgeNumber=1&alertMessage=Hi",
                "appData": "{id:asdf&passwd:1234}",
                /* Other content */
            ]}
        }
        ```

    - If you have data to send to the application but no need to notify the user, use the action field on the same level as the message field, instead of within the message field, and do not include the message field itself. In this case, the notification is delivered with the best effort.

        ```
        {
            "action": "backgroundLaunch",
            "messages":
            [{
                /* Other content */
                "appData": "{id:asdf&passwd:1234}",
                /* Other content */
            ]}
        }
        ```

3. Create the notification message.

    A message is one of the fields that constitute a notification. The message field contains not only the message to show in the quick panel on the device, but also the behaviors that the device must take when receiving the notification. The message field is a string that consists of key-value pairs. The available pair options are given in the following table.

    **Table: Message field key-value pairs**

    | Key            | Value                                    | Description                              |
    |--------------|----------------------------------------|----------------------------------------|
    | `action`       | `ALERT`: Store the message and alert the user.<br>`SILENT`: Store the message without alerting the user.<br>`DISCARD`: Discard the message, if the application is not up and running.<br>`LAUNCH`: Forcibly launch the application and deliver the notification.<br>`BACKGROUNDLAUNCH`: Launch the application in the background and deliver the notification. | Action to be performed if the application is not running. If no action is defined, the default behavior is `SILENT`. |
    | `alertMessage` | Up to 127 bytes                          | Alert message shown to the user in the quick panel. If the action is not set as `ALERT`, this value is meaningless. |
    | `badgeOption`  | `INCREASE`: Increase the badge number by the given value.<br>`DECREASE`: Decrease the badge number by the given value.<br>`SET`: Set badge number to the given value. | Option for updating the icon badge number. If the action is set as `DISCARD`, the `badgeOption` is ignored. If the badge option is not included, the icon badge number remains unchanged. |
    | `badgeNumber`  | 0-999                                    | -                                        |

    For example, to show a "Hi" message in the quick panel and increase the badge count by 1 when the notification arrives at the device, the message field of the notification must be the following:

    ```
    "badgeOption=INCREASE&badgeNumber=1&action=ALERT&alertMessage=Hi"
    ```

    The message field takes effect only when the application is not running (more precisely, when the application is not connected to the push service). If a notification with the above message field arrives at the device where the application is running, the push service delivers the notification directly to the application. It does not show the "Hi" message in the quick panel or increase the badge count.

    When you send a notification to the device with the `BACKGROUNDLAUNCH` action value, the push service launches the application in the background (if it is not already running), and delivers the appData field to the application. The user cannot see that a notification is received, but they find out when they use the application the next time.

4. Use the Rest APIs for sending push notifications.
    -   Single request

        With the created message field, you can construct a notification using a JSON query and send it to the RQM server using the POST method. The following list contains the details:

        -   URI: URI of the RQM server chosen based on the first 2 digits of the registration ID

        - Method: POST

        - Data: JSON

        - Description: Request a notification push from the push server to the push service

        - Note: The total request message body must be less than the system default value, 200 kb. If not, "3035 – error of too long chunked message data" is returned. The system default value can be changed as needed.

        - Header

            There are 2 required fields: `appID` and `appSecret`.

            The fields are given when you register the application, and they are used for application authentication. If either is missing, the push server rejects the request and returns "3045 – error of application authentication" error. Put these 2 parameters on the request header.

        - Arguments

            **Table: Arguments**

            | Key              | Description                              | Additional information                   |
            |----------------|----------------------------------------|----------------------------------------|
            | `encoding`       | Encoding defines how the `regId` is encoded.<br>For most cases, the push server issues the `regId` as a hex string by default, but if third-party providers state that they use the base64 encoding for the `regId` at the application registration time, the `regId` is base64-encoded.<br>If the `regId` is base64-encoded, use the `"base64"` value for this field. Otherwise, leave this field blank to allow the push server to handle the `regId` as a hex string. | Optional<br>Type: string<br>Default: `NULL`      |
            | `regID`          | Distinguish a recipient from other recipients by assigning a unique registration ID to each recipient.<br>The registration ID is assigned when the application is installed on a device and marked to use an application service.<br>The current registration ID passing policy is as follows (it can change in the future):<br>a. The preloaded push service connects to the push server and registers the application.<br>b. The push server returns the registration ID to the push service.<br>c. The push service passes the ID to the application.<br>d. The push server passes the registration ID to an application server.<br>In other applications, the application passes the registration ID to the application server. | Required<br>Type: string                     |
            | `requestID`      | An application server needs to assign a request ID to each request. It enables you to distinguish one request from the others. | Required<br>Type: string                     |
            | `sender`         | Information on the user who sends the notification. | Optional<br>Type: string<br>Default: `NULL`      |
            | `action`         | This message is delivered along with another urgent message, when the action value is `"backgroundLaunch"` and message field is `NULL`. | Optional<br>Type: string<br>Default: `NULL`      |
            | `message`        | The message the sender wants to deliver. It can be a multibyte character.<br>The message goes from an application server through the push server and push service to the application, which can handle the message.<br>Maximum message length must be less than 2 kb. Make sure that if there is no message and `appData`, the push server rejects the message and returns an error. | Conditionally mandatory (if `appData` is `NULL`, this field is required)<br>Type: string<br>Default: `NULL` |
            | `appData`        | Applications can use this field to carry their own data. The handling of this data depends on the type defined with the `type` key.<br>Make sure that if there is no message and no `appData`, the push server rejects the message and returns an error. | Conditionally mandatory (if message is `NULL`, this field is required)<br>Type: string<br>Default: `NULL` |
            | `reliableOption` | The push server guarantees reliable message delivery if the `reliableOption` is set. The possible options are:<br><br>`NoReliable`: Do not send any acknowledgment back to an application server and do not store the notification in the push server if the push service did not receive the notification.<br>`Transport`: Send an acknowledgment back to the application server when the push service receives the notification.<br><br>This is an optional field, and if it does not exist, the server applies its default value (`Transport`). An acknowledgment at this point does not mean a response to the notification request, but an acknowledgment that the push service has received the notification. When the push service receives the notification, the push server sends this acknowledgment to the application server in a JSON format through HTTP. | Optional<br>Type: string<br>Default: transport   |
            | `sessionInfo`    | Connection information for an application. Third-party applications can define this field by themselves. | Optional<br>Type: string<br>Default: `NULL`      |
            | `timeStamp`      | Server time in milliseconds when a notification request has been made. | OptionalType: longDefault: `NULL`        |
            | `expiryDate`     | Time period, in minutes, for storing the request in the push server if the delivery fails:<br><br>- If the value set to 0, the push server stores the request for 1440 minutes (24 hours).<br>- If the value is 1 - 2800, the push server stores the request for that number of minutes.If the push server default setting is less than the defined value, the push server stores the request according to its own setting.<br>- If the value is greater than 2880, the push server stores the request for 2880 minutes (48 hours).<br><br>This is an optional field, and if it does not exist, the server applies its default value (0). If `reliableOption` is set at `NoReliable`, this field is meaningless. | Optional<br>Type: int<br>Default: 0              |

        The following examples illustrate the notification:

        -   Example header:

            ```
            appID: 1234567890987654
            appSecret: dYo/o/m11gmWmjs7+5f+2zLNVOc=
            ```

        - Example request:

            ```
            {
                "encoding": "base64" /* Optional */
                "regID": "ab123456",
                "requestID": "0000001",
                "sender": "oscal", /* Optional */
                "type": 0 /* Optional */
                "message": "badgeOption=INCREASE&badgeNumber=1&action=ALERT&alertMessage=Hi", /* Optional */
                "appData": "{id:asdf&passwd:1234}", /* Optional, (Opaque) */
                "sessionInfo": "002002", /* Optional */
                "timeStamp": 1234567890, /* Optional */
            }
            ```

        - Example response:

            If the push server receives a notification request, the server returns a JSON string that contains the `regID`, `requestID`, status code, and status message. If the request contains a malformed JSON format, requests are not processed and are returned without the `regID` and `requestID` values. If the request is of the JSON format but has invalid data, no requests are processed and are considered as an error.

            The response message only shows whether receiving the notification request was successful. The response message does not deal with whether the push service receives the notification. The order of the response message is the same as the request message order.

            -   The following example shows a response message when the request is successful:

                ```
                {
                    "results":
                    [{
                        "regID": "ab123456",
                        "requestID": "0000001",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }]
                }
                ```

            - The following example shows a response message when the request fails due to malformation:

                ```
                {
                    "results":
                    [{
                        "regID": "",
                        "requestID": "",
                        "statusCode": 3023,
                        "statusMsg": "error of json mapping exception"
                    }]
                }
                ```

            - The following example shows a response message when the request fails due to abnormal data:

                ```
                {
                    "results":
                    [{
                        "regID": "ab123456",
                        "requestID": "0000001",
                        "statusCode": 3008,
                        "statusMsg": "error of not registered regID"
                    }]
                }
                ```

                > **Note**   
				> In the above example, the 3008 error code means that the `regID` does not exist in the push server. It happens when your application of that particular `regID` was uninstalled or disabled by the user, and consequently the `regID` must be removed from your application server. When the application is reinstalled or enabled, it must repeat the [registration process](push.md#registration) and send a new `regID` to your application server.

	-  Multiple request

		You can construct a multiple request in a Rest API call. Currently, this feature is not supported for the registration IDs starting with 5.

        The following list contains the details:

        -   URI: URI of the RQM server chosen based on the first 2 digits of the registration ID
        -   Method: POST
        -   Data: JSON
        -   Description: Request a notification push from the push server to the push service
        -   Argument: See the [single request](#single_req)
        -   Note: The total request message body must be less than the system default value, 200 kb. If not, "3035 – error of too long chunked message data" is returned. The system default value can be changed as needed.
        -   Example header:

            ```
            appID: 1234567890987654
            appSecret: dYo/o/m11gmWmjs7+5f+2zLNVOc=
            ```

        -   Example request:

            ```
            {
                "messages":
                [{
                    "encoding": "base64" /* Optional */
                    "regID": "ab123456",
                    "requestID": "0000001",
                    "sender": "oscal", /* Optional */
                    "type": 0 /* Optional */
                    "message": "example", /* Optional */
                    "appData": "{id:asdf&passwd:1234}", /* Optional, (Opaque) */
                    "reliableOption": "Transport", /* Optional */
                    "sessionInfo": "192.168.0.1-8080-12345567", /* Optional */
                    "timeStamp": 1234567890, /* Optional */
                }
                {
                    "encoding": "base64" /* Optional */
                    "regID": "ab234567",
                    "requestID": "0000002",
                    "sender": "oscal", /* Optional */
                    "type": 0 /* Optional */
                    "message": "example", /* Optional */
                    "appData": "{id:asdf&passwd:1234}", /* Optional, (Opaque) */
                    "reliableOption": "Transport", /* Optional */
                    "sessionInfo": "192.168.0.1-8080-12345567", /* Optional */
                    "timeStamp": 1234567890, /* Optional */
                ]}
            }
            ```

        -   Example response:
            -   The following example shows a response message when the request is successful:

                ```
                {
                    "results":
                    [{
                        "regID": "ab123456",
                        "requestID": "0000001",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }
                    {
                        "regID": "ab234567",
                        "requestID": "0000002",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }]
                }
                ```

            -   The following example shows a response message when the request fails due to malformation:

                ```
                {
                    "results":
                    [{
                        "regID": "",
                        "requestID": "",
                        "statusCode": 3023,
                        "statusMsg": "error of json mapping exception"
                    }]
                }
                ```

            -   The following example shows a response message when some parts of the multiple request have failed and the others have not:

                ```
                {
                    "results":
                    [{
                        "regID": "ab123456",
                        "requestID": "0000001",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }
                    {
                        "regID": "ab234567",
                        "requestID": "0000002",
                        "statusCode": 3008,
                        "statusMsg": "error of not registered regID"
                    }]
                }
                ```

    -   Multicast

        You can construct a multicast to send a push notification to multiple applications. Currently, this feature is not supported for the registration IDs starting with 5.

        The following list contains the details:

        -   URI: URI of the RQM server chosen based on the first 2 digits of the registration ID
        -   Method: POST
        -   Data: JSON
        -   Description: Request a notification push from the push server to the push service
        -   Argument: See the [single request](#single_req)
        -   Note: The total request message body must be less than the system default value, 200 kb. If not, "3035 – error of too long chunked message data" is returned. The system default value can be changed as needed.
        -   Example header:

            ```
            appID: 1234567890987654
            appSecret: dYo/o/m11gmWmjs7+5f+2zLNVOc=
            ```

        -   Example request:

            ```
            {
                "messages":
                [{
                    "encoding": "base64" /* Optional */
                    "regID": ["ab123456", "ab234567", "ab345678"]
                    "requestID": "0000001",
                    "sender": "oscal", /* Optional */
                    "type": 0 /* Optional */
                    "message": "example", /* Optional */
                    "appData": "{id:asdf&passwd:1234}", /* Optional */
                    "sessionInfo": "192.168.0.1-8080-12345567", /* Optional */
                    "timeStamp": 1234567890, /* Optional */
                ]}
            }
            ```

        -   Example response:
            -   The following example shows a response message when the request is successful:

                ```
                {
                    "results":
                    [{
                        "regID": "ab123456",
                        "requestID": "0000001",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }
                    {
                        "regID": "ab234567",
                        "requestID": "0000002",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }
                    {
                        "regID": "ab345678",
                        "requestID": "0000002",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }]
                }
                ```

            -   The following example shows a response message when the request fails due to malformation:

                ```
                {
                    "results":
                    [{
                        "regID": "",
                        "requestID": "",
                        "statusCode": 3023,
                        "statusMsg": "error of json mapping exception"
                    }]
                }
                ```

            -   The following example shows a response message when some parts of the multicast request have failed and the others have not:

                ```
                {
                    "results":
                    [{
                        "regID": "ab123456",
                        "requestID": "0000001",
                        "statusCode": 1000,
                        "statusMsg": "Success"
                    }
                    {
                        "regID": "ab234567",
                        "requestID": "0000001",
                        "statusCode": 3008,
                        "statusMsg": "error of not registered regID"
                    }
                    {
                        "regID": "ab345678",
                        "requestID": "0000001",
                        "statusCode": 3013,
                        "statusMsg": "error of impossible to enqueue"
                    }]
                }
                ```


<a name="error_codes"></a>				
## Error Codes

If sending a push notification request fails for some reason, the response message contains an error code.

The following table lists all possible error codes for push notifications, helping you to identify the reason for the failure and take appropriate action.

**Table: Push notification error codes**

| Status code | Basic status message                     |
|-----------|----------------------------------------|
| 1000        | Success                                  |
| 1001        | Failed                                   |
| 1002        | Expired                                  |
| 3001        | Error of unknown reason                  |
| 3002        | Internal server error                    |
| 3003        | Error of no appId field                  |
| 3004        | Error of no deviceToken field            |
| 3005        | Error of no regID field                  |
| 3006        | Error of no requestID field              |
| 3007        | Error of at least either message or appData is needed |
| 3008        | Error of not registered regID            |
| 3009        | Error of not registered appID            |
| 3010        | Error of malformed notification request data |
| 3011        | Error of fatal problems with mapping of content |
| 3012        | Error of insufficient field              |
| 3013        | Error of impossible enqueue              |
| 3014        | Error of notification to cancel is not in queue or already sent |
| 3015        | Error of I/O produced by failed, interrupted I/O operation or unknown reason |
| 3016        | Error of not supporting requested URI    |
| 3017        | Error of not supporting requested method |
| 3018        | Error of notification data contains unreadable data or `NULL` |
| 3019        | Error of containing abnormal data        |
| 3020        | Error of not supported reliability option |
| 3021        | Error of bad padding exception           |
| 3022        | Error of json parse exception            |
| 3023        | Error of json mapping                    |
| 3024        | Error of illegal blocksize               |
| 3025        | Error occurred while decoding regID      |
| 3026        | Error of no secret key field             |
| 3027        | Error of not authenticated application   |
| 3028        | Error of unsupported encoding type       |
| 3029        | Error of unparseable request type        |
| 3030        | Error of message length excess. message length is allowed up to 2kb |
| 3031        | Error of unsupported connectionTerm      |
| 3032        | Error of not supporting chunked request body |
| 3033        | Error of illegal expiry date             |
| 3034        | Error of illegal delay date              |
| 3035        | Error of too long chunked message data    |
| 3036        | Error of empty multiple request          |
| 3037        | Error of notification key generation     |
| 3038        | Error of create application              |
| 3039        | Error of delete application              |
| 3040        | Error of read application                |
| 3041        | Error of update application              |
| 3042        | Error of invalid timeStamp               |
| 3043        | Error of invalid type                    |
| 3044        | Error of not registered application      |
| 3045        | Error of application authentication failed |
| 3046        | Error of not allowed to use Push Server  |


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
