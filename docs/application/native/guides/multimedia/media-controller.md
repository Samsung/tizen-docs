# Media Controller


You can establish communication between a media controller server and a media controller client. You can send commands from the client to the server, and the client can request updated metadata and playback information from the server.

The main features of the Media Controller API include:

- Updating and retrieving information

  You can [update the metadata and playback information](#get_media) on the server side, and then retrieve the metadata and playback information on the client side.

  The media controller server provides current information about the registered application that you can send to the client.

  When the client requests the information, the media controller server updates the state information of an active application before transferring the data. If the application is not running when the client request arrives, the media controller server transfers the latest information.

- Sending and processing commands

  You can [send a command](#send_media) to the server from the client side, and then process the command on the server side.

  The client can request [server state](#serverstate) or [server metadata](#servermetadata) information from the server, and receive it through a callback.

## Prerequisites

To enable your application to use the media controller functionality:

- To use the media controller server:

  1. To use the functions and data types of the Media Controller Server API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CONTROLLER__SERVER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CONTROLLER__SERVER__MODULE.html) applications), include the `<media_controller_server.h>` header file in your application:

     ```
     #include <media_controller_server.h>
     ```

  2. To work with the Media Controller Server API, define a handle variable for the media controller server:

     ```
     static mc_server_h g_server_h = NULL;
     ```

     The server updates the metadata and playback information, and processes the requests and commands sent by the client.

     This guide uses a global variable for the handle.

- To use the media controller client:

  1. To use the functions and data types of the Media Controller Client API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CONTROLLER__CLIENT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CONTROLLER__CLIENT__MODULE.html) applications), include the `<media_controller_client.h>` header file in your application:

     ```
     #include <media_controller_client.h>
     ```

  2. To work with the Media Controller Client API, define a handle variable for the media controller client:

     ```
     static mc_client_h g_client_h = NULL;
     ```

     The client requests metadata and playback information from the server, and sends playback commands to server.

     This guide uses a global variable for the handle.

<a name="get_media"></a>
## Updating and Retrieving Information

To update the metadata and playback information on the server side:

1. Create the media controller server handle using the `mc_server_create()` function:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Set the metadata or playback information to be updated using the corresponding `mc_server_set_XXX()` function, and then update the metadata or playback information using the corresponding `mc_server_update_XXX()` function.

   For example, to update the playback state information, set the information to be updated using the `mc_server_set_playback_state()` function, and then update the information using the `mc_server_update_playback_info()` function:

   ```
   ret = mc_server_set_playback_state(g_mc_server, MC_PLAYBACK_STATE_PLAYING);

   ret = mc_server_update_playback_info(g_mc_server);
   ```

3. When no longer needed, destroy the media controller server handle using the `mc_server_destroy()` function:

   ```
   mc_server_destroy(g_server_h);
   ```

To retrieve the metadata and playback information on the client side:

1. Create the media controller client handle using the `mc_client_create()` function:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using the `mc_client_get_latest_server_info()` function:

   ```
   char *server_name = NULL;
   mc_server_state_e server_state;

   ret = mc_client_get_latest_server_info(g_mc_client, &server_name, &server_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Server state: %d\n", server_name, server_state);
   ```

3. Retrieve the metadata or playback information from the server using the corresponding `mc_client_get_server_XXX()` function. Use the server name retrieved in the previous step to identify the server.

   For example, to retrieve the playback information from the server, use the `mc_client_get_server_playback_info()` function:

   ```
   mc_playback_h playback = NULL;
   mc_playback_states_e playback_state;

   ret = mc_client_get_server_playback_info(g_client_h, server_name, &playback);

   ret = mc_client_get_playback_state(playback, &playback_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Playback State: %d\n", playback_state);
   ```

   The `mc_client_get_playback_state()` function retrieves the playback state from the playback information returned by the `mc_client_get_server_playback_info()` function.

4. When no longer needed, destroy the media controller client handle using the `mc_client_destroy()` function:

   ```
   mc_client_destroy(g_client_h);
   ```
<a name="send_media"></a>
## Sending and Processing Commands

To send a command to the server from the client side:

1. Create the media controller client handle using the `mc_client_create()` function:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using the `mc_client_get_latest_server_info()` function:

   ```
   char *server_name = NULL;
   mc_server_state_e server_state;

   ret = mc_client_get_latest_server_info(g_mc_client, &server_name, &server_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Server state: %d\n", server_name, server_state);
   ```

3. Send the command to the server using the corresponding `mc_client_send_XXX()` function. Use the server name retrieved in the previous step to identify the server.

   For example, to send a playback state change command to the server, use the `mc_client_send_playback_state_command()` function with the new state defined in the third parameter:

   ```
   mc_playback_h playback = NULL;
   mc_playback_states_e playback_state = MC_PLAYBACK_STATE_PLAYING;

   ret = mc_client_send_playback_state_command(g_client_h, server_name, playback_state);
   ```

   If you want to define your own commands to send to the server, use the `mc_client_send_custom_command()` function.

4. When no longer needed, destroy the media controller client handle using the `mc_client_destroy()` function:

   ```
   mc_client_destroy(g_client_h);
   ```

To process the received command on the server side:

1. Create the media controller server handle using the `mc_server_create()` function:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Define the callback that is invoked when the server receives the command.

   For example, to define a callback for playback state change commands:

   ```
   void
   command_received_cb(const char* client_name, mc_playback_states_e state, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Playback state: %d\n", client_name, state);
   }
   ```

3. Register the callback:

   - To register a callback for playback state change commands, use the `mc_server_set_playback_state_command_received_cb()` function.
   - To register a callback for a custom command, use the `mc_server_set_custom_command_received_cb()` function.

   For example, to register a callback for playback state change commands:

   ```
   ret = mc_server_set_playback_state_command_received_cb(g_mc_server, command_received_cb, NULL);
   ```

4. When no longer needed, destroy the media controller server handle using the `mc_server_destroy()` function:

   ```
   mc_server_destroy(g_server_h);
   ```
<a name="serverstate"></a>
## Media Controller Server State Attributes

The following table lists all the server state attributes the client can receive.

**Table: Media controller server state attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Server states**                |                                          |
| `MC_SERVER_ACTIVATE`             | Requested media controller server is active |
| `MC_SERVER_DEACTIVATE`           | Requested media controller server is not active |
| **Playback states**              |                                          |
| `MC_PLAYBACK_STATE_NONE`         | No history of media playback             |
| `MC_PLAYBACK_STATE_PLAYING`      | Playback state of playing                |
| `MC_PLAYBACK_STATE_PAUSED`       | Playback state of paused                 |
| `MC_PLAYBACK_STATE_STOPPED`      | Playback state of stopped                |
| `MC_PLAYBACK_STATE_NEXT_FILE`    | Playback state of next file              |
| `MC_PLAYBACK_STATE_PREV_FILE`    | Playback state of previous file          |
| `MC_PLAYBACK_STATE_FAST_FORWARD` | Playback state of fast forward           |
| `MC_PLAYBACK_STATE_REWIND`       | Playback state of rewind                 |
| **Shuffle mode states**          |                                          |
| `MC_SHUFFLE_MODE_ON`             | Shuffle mode is on                       |
| `MC_SHUFFLE_MODE_OFF`            | Shuffle mode is off                      |
| **Repeat mode states**           |                                          |
| `MC_REPEAT_MODE_ON`              | Repeat mode is on                        |
| `MC_REPEAT_MODE_OFF`             | Repeat mode is off                       |

<a name="servermetadata"></a>
## Media Controller Server Metadata Attributes

The following table lists all the server metadata attributes the client can receive.

**Table: Media controller server metadata attributes**

| Attribute                   | Description                              |
|-----------------------------|------------------------------------------|
| `MC_META_MEDIA_TITLE`       | Title of the latest content in the media controller server |
| `MC_META_MEDIA_ARTIST`      | Artist of the latest content in the media controller server |
| `MC_META_MEDIA_ALBUM`       | Album name of the latest content in the media controller server |
| `MC_META_MEDIA_AUTHOR`      | Author of the latest content in the media controller server |
| `MC_META_MEDIA_GENRE`       | Genre of the latest content in the media controller server |
| `MC_META_MEDIA_DURATION`    | Duration of the latest content in the media controller server |
| `MC_META_MEDIA_DATE`        | Date of the latest content in the media controller server |
| `MC_META_MEDIA_COPYRIGHT`   | Copyright of the latest content in the media controller server |
| `MC_META_MEDIA_DESCRIPTION` | Description of the latest content in the media controller server |
| `MC_META_MEDIA_TRACK_NUM`   | Track number of the latest content in the media controller server |
| `MC_META_MEDIA_PICTURE`     | Album art of the latest content in the media controller server |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
