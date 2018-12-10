# Media Controller


You can establish communication between a media controller server and a media controller client. You can send commands from the client to the server, and the client can request updated metadata and playback information from the server.

The main features of the Media Controller API include:

- Updating and retrieving information

  You can [update the metadata and playback information](#updating-and-retrieving-information) on the server side, and then retrieve the metadata and playback information on the client side.

  The media controller server provides current information about the registered application that you can send to the client.

  When the client requests the information, the media controller server updates the state information of an active application before transferring the data. If the application is not running when the client request arrives, the media controller server transfers the latest information.

- Updating and retrieving playlist

  You can [update the playlist information](#updating-and-retrieving-playlist) on the server side, and then retrieve the playlist information on the client side.

  The media controller server provides current information about the registered application that you can send to the client.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Sending and processing commands to receive replies

  You can [send a command](#sending-and-processing-commands-to-receive-replies) to the server from the client side, and then process the command on the server side.

  You can [send a reply of the command](#send_command_reply) to the client from the server side, and then receive the reply on the client side.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Sending and processing a custom event

  You can [send a custom event](#sending-and-processing-a-custom-event) to the client from the server side and then process the event on the client side.

  You can [send a reply of the custom event](#send_event_reply) to the server from the client side and then receive the reply on the server side.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Sending and processing a search command

  You can [send a search command](#sending-and-processing-a-search-command) to the server from the client side, and then process the command on the server side.

  > **Note**
  >
  > This feature supports Tizen 5.0 and Higher for Mobile and Wearable.

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


## Updating and Retrieving Information

To update the metadata and playback information on the server side:

1. Create the media controller server handle using the `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Set the metadata or playback information to be updated using the corresponding `mc_server_set_XXX()` and then update the metadata or playback information using the corresponding `mc_server_update_XXX()`.

   For example, to update the playback state information, set the information to be updated using the `mc_server_set_playback_state()` and then update the information using the `mc_server_update_playback_info()`:

   ```
   ret = mc_server_set_playback_state(g_mc_server, MC_PLAYBACK_STATE_PLAYING);

   ret = mc_server_update_playback_info(g_mc_server);
   ```

3. Destroy the media controller server handle using the `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   mc_server_destroy(g_server_h);
   ```

To retrieve the metadata and playback information on the client side:

1. Create the media controller client handle using the `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using the `mc_client_get_latest_server_info()`:

   ```
   char *server_name = NULL;
   mc_server_state_e server_state;

   ret = mc_client_get_latest_server_info(g_mc_client, &server_name, &server_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Server state: %d\n", server_name, server_state);
   ```

3. Retrieve the metadata or playback information from the server using the corresponding `mc_client_get_server_XXX()`. Use the server name retrieved in the previous step to identify the server.

   For example, to retrieve the playback information from the server, use the `mc_client_get_server_playback_info()`:

   ```
   mc_playback_h playback = NULL;
   mc_playback_states_e playback_state;

   ret = mc_client_get_server_playback_info(g_client_h, server_name, &playback);

   ret = mc_client_get_playback_state(playback, &playback_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Playback State: %d\n", playback_state);
   ```

   The `mc_client_get_playback_state()` retrieves the playback state from the playback information returned by the `mc_client_get_server_playback_info()`.

4. Destroy the media controller client handle using the `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```


## Updating and Retrieving Playlist

To update the playlist and metadata information on the server side:

1. Create the media controller server handle using the `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```
2. Create the playlist handle using the `mc_server_create_playlist()`:

   ```
   mc_playlist_h playlist_h = NULL;

   ret = mc_server_create_playlist(g_server_h, "playlist", &playlist_h);
   ```
3. Set the metadata information in the playlist handle to be updated using the corresponding `mc_server_add_item_to_playlist()` and then update the playlist using the corresponding `mc_server_update_playlist_done()`:

   ```
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_TITLE, "title_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_ARTIST, "artist_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_ALBUM, "album_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_AUTHOR, "author_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_GENRE, "genre_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_DURATION, "duration_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_DATE, "date_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_COPYRIGHT, "copyright_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_DESCRIPTION, "desc_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_TRACK_NUM, "tracknum_1");
   mc_server_add_item_to_playlist(g_server_h, playlist_h, "1", MC_META_MEDIA_PICTURE, "picture_1");

   ret = mc_server_update_playlist_done(g_server_h, playlist_h);
   ```
4. When no longer needed, destroy the playlist handle using the `mc_playlist_destroy()`:

   ```
   mc_playlist_destroy(playlist_h);
   ```
5. Destroy the media controller server handle using the `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   mc_server_destroy(g_server_h);
   ```

To retrieve the playlist and metadata information on the client side:

1. Create the media controller client handle using the `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```
2. Define the callback that is invoked when the client receives the playlist:

   ```
   void
   playlist_updated_cb(const char *server_name, mc_playlist_update_mode_e mode, const char *playlist_name, mc_playlist_h playlist, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Playlist Update Mode: %d, Playlist Name: %s\n", server_name, mode, playlist_name);
   }
   ```

   If you want to use playlist handle outside, make a copy using `mc_playlist_clone()`.

3. Register the callback using the `mc_client_set_playlist_updated_cb()`:

   ```
   ret = mc_client_set_playlist_updated_cb(g_client_h, playlist_updated_cb, NULL);
   ```
4. Define the callback that retrieve the item from the playlist handle:

   ```
   bool
   playlist_item_cb(const char *index, mc_metadata_h metadata, void *user_data)
   {
     dlog_print(DLOG_DEBUG, LOG_TAG, "Index: %s\n", index);
   }
   ```

   If you want to use metadata handle outside, make a copy using `mc_metadata_clone()`.

5. Register the callback using the `mc_playlist_foreach_item()`:

   ```
   ret = mc_playlist_foreach_item(playlist_h, playlist_item_cb, NULL);
   ```

6. Retrieve the metadata information from the metadata handle using the `mc_metadata_get()`:

   ```
   char *title = NULL;
   ret = mc_metadata_get(metadata_h, MC_META_MEDIA_TITLE, &title);
   ```

7. When no longer needed, destroy the playlist handle using the `mc_playlist_destroy()`:

   ```
   mc_playlist_destroy(playlist_h);
   ```

8. Destroy the media controller client handle using the `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

> **Note**
>
> This feature supports Tizen 4.0 and Higher for Mobile.


## Sending and Processing Commands to Receive Replies

To send a command to the server from the client side:

1. Create the media controller client handle using the `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using the `mc_client_get_latest_server_info()`:

   ```
   char *server_name = NULL;
   mc_server_state_e server_state;

   ret = mc_client_get_latest_server_info(g_mc_client, &server_name, &server_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Server state: %d\n", server_name, server_state);
   ```

3. Send the command to the server using the corresponding `mc_client_send_XXX_cmd()`. Use the server name retrieved in the previous step to identify the server.

   For example, to send a playback action change command to the server, use the `mc_client_send_playback_action_cmd()` with the new action defined in the third parameter:

   ```
   mc_playback_action_e playback_action = MC_PLAYBACK_ACTION_PLAY;
   char *request_id = NULL;

   ret = mc_client_send_playback_action_cmd(g_client_h, server_name, playback_action, &request_id);
   ```

   If you want to define your own commands to send to the server, use the `mc_client_send_custom_cmd()`.
   The request_id will be passed to the `mc_client_cmd_reply_recieved_cb()`.

4. Destroy the media controller client handle using the `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

To process the received command on the server side:

1. Create the media controller server handle using the `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Define the callback that is invoked when the server receives the command.

   For example, to define a callback for playback state change commands:

   ```
   void
   playback_action_cmd_received_cb(const char* client_name, const char *request_id, mc_playback_action_e action, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Request Id: %s, Playback action: %d\n", client_name, request_id, action);
   }
   ```

3. Register the callback:

   - To register a callback for playback state change commands, use the `mc_server_set_playback_action_cmd_received_cb()`.
   - To register a callback for playback position change commands, use the `mc_server_set_playback_position_cmd_received_cb()`.
   - To register a callback for shuffle mode change commands, use the `mc_server_set_shuffle_mode_cmd_received_cb()`.
   - To register a callback for repeat mode change commands, use the `mc_server_set_repeat_mode_cmd_received_cb()`.
   - To register a callback for played item, playback state and playback position change commands in playlist, use the `mc_server_set_playlist_cmd_received_cb()`.
   - To register a callback for a custom command, use the `mc_server_set_custom_cmd_received_cb()`.

   For example, to register a callback for playback state change commands:

   ```
   ret = mc_server_set_playback_action_cmd_received_cb(g_mc_server, playback_action_cmd_received_cb, NULL);
   ```

4. Destroy the media controller server handle using the `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   mc_server_destroy(g_server_h);
   ```

To send the reply of completed command on the server side:

1. Send the reply of completed command using the `mc_server_send_cmd_reply()` with the request id of the command in the third parameter and the result of the command in fourth parameter:

   ```
   int result_code = 0;

   ret = mc_server_send_cmd_reply(g_server_h, client_name, request_id, result_code, NULL);
   ```

<a name="send_command_reply"></a>
To receive the reply of completed command on the client side:

1. Define the callback that is invoked when the client receives the reply:

   ```
   void
   cmd_reply_received_cb(const char *server_name, const char *request_id, int result_code, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Request Id: %s, Result Code: %d\n", server_name, request_id, result_code);
   }
   ```

2. Register the callback:

   ```
   ret = mc_client_set_cmd_reply_received_cb(g_client_h, cmd_reply_received_cb, NULL);
   ```

> **Note**
>
> This feature supports Tizen 4.0 and Higher for Mobile.


## Sending and Processing a Custom Event

To send a custom event to the client from the server side:

1. Create the media controller server handle using the `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Retrieve the client name using the `mc_server_foreach_client()`:

   ```
   bool
   activated_client_cb(const char *client_name, void *user_data)
   {
     GList **client_list = (GList **)user_data;

     if (!client_list || !client_name) return FALSE;
     *client_list = g_list_append(*client_list, g_strdup(client_name));

     return TRUE;
   }

   GList *client_list = NULL;

   ret = mc_server_foreach_client(g_mc_server, activated_client_cb, &client_list);
   ```

3. Send the event to the client using the corresponding `mc_server_send_custom_event()`. Use the client name retrieved in the previous step to identify the client.

   For example, to send a your own event to the client, use the `mc_server_send_custom_event()` with the event in the third parameter:

   ```
   char *request_id = NULL;

   ret = mc_server_send_custom_event(g_server_h, client_name, "evnet1", NULL, &request_id);
   ```

4. Destroy the media controller server handle using the `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   mc_server_destroy(g_server_h);
   ```

To process the received event on the client side:

1. Create the media controller client handle using the `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Define the callback that is invoked when the client receives the event.

   For example, to define a callback for a custom event:

   ```
   void
   event_received_cb(const char* server_name, const char *request_id, const char *event, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Request id: %s, Event: %s\n", server_name, request_id, event);
   }
   ```

3. Register the callback:

   - To register a callback for a custom events, use the `mc_client_set_custom_event_received_cb()`.

      For example, to register a callback for a custom event:

      ```
      ret = mc_client_set_custom_event_received_cb(g_client_h, event_received_cb, NULL);
      ```

4. Destroy the media controller client handle using the `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```


<a name="send_event_reply"></a>
To send the reply of completed custom event on the client side:

1. Send the reply of completed custom event using the `mc_client_send_event_reply()` with the request id of the custom event in the third parameter and the result of the custom event in fourth parameter:

   ```
   int result_code = 0;

   ret = mc_client_send_event_reply(g_server_h, server_name, request_id, result_code, NULL);
   ```

To receive the reply of processing command on the server side:

1. Define the callback that is invoked when the server receives the reply:

   ```
   void
   event_reply_received_cb(const char *client_name, const char *request_id, int result_code, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Request Id: %s, Result Code: %d\n", client_name, request_id, result_code);
   }
   ```

2. Register the callback:

   ```
   ret = mc_server_set_event_reply_received_cb(g_server_h, event_reply_received_cb, NULL);
   ```

> **Note**
>
> This feature supports Tizen 4.0 and Higher for Mobile.


## Sending and Processing a Search Command

To send a search command to the server from the client side:

1. Create the media controller client handle using the `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using the `mc_client_foreach_server()`:

   ```
   bool
   activated_server_cb(const char *server_name, void *user_data)
   {
     GList **server_list = (GList **)user_data;

     if (!server_list || !server_name) return FALSE;
     *server_list = g_list_append(*client_list, g_strdup(server_name));

     return TRUE;
   }

   GList *server_list = NULL;

   ret = mc_client_foreach_server(g_client_h, activated_server_cb, &server_list);
   ```

3. Create the search handle using the `mc_search_create()`:

   ```
   ret = mc_search_create(&g_search_h);
   ```

4. Set the condition with a [content type](#media-controller-content-type-attributes), a [search category](#media-controller-search-category-attributes) and a search keyword using the `mc_search_set_condition()`:

   ```
   ret = mc_search_set_condition(g_search_h, MC_CONTENT_TYPE_MUSIC, MC_SEARCH_TITLE, "keyword", NULL);
   ```

5. Send the search command to the server using the corresponding `mc_client_send_search_cmd()`. Use the server name retrieved in the previous step to identify the server.
For example, to send the search command to the server, use the `mc_client_send_search_cmd()` with the search handle in the third parameter:

   ```
   char *request_id = NULL;

   ret = mc_client_send_search_cmd(g_client_h, server_name, g_search_h, &request_id);
   ```

6. Destroy the search handle using the `mc_search_destroy()`, when search handle is no longer needed:

   ```
   mc_search_destroy(g_search_h);
   ```

7. Destroy the media controller client handle using the `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

To process the received search command on the server side:

1. Create the media controller server handle using the `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Define the callback that is invoked when the server receives the search command.

   For example, to define a callback for a search command:

   ```
   void
   search_command_received_cb(const char* client_name, const char *request_id, mc_search_h search, void *user_data)
   {
      mc_search_h *get_search = mc_search_h *(user_data);
      dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Request id: %s\n", client_name, request_id);
      ret = mc_search_clone(search, get_search);
   }
   ```

3. Register the callback:

   - To register a callback for a search command, use the `mc_server_set_search_cmd_received_cb()`.

      For example, to register a callback for a search command:

      ```
      mc_search_h g_search_h = NULL;
      ret = mc_server_set_search_cmd_received_cb(g_server_h, search_command_received_cb, &g_search);
      ```

4. Retrieve the search condition using the `mc_search_foreach_condition()`:

   ```
   bool
   search_condition_cb(mc_content_type_e content_type, mc_search_category_e category, const char *search_keyword, bundle *data, void *user_data)
   {
      dlog_print(DLOG_DEBUG, LOG_TAG, "Content Type: %d, Search Category: %d, Search Keyword: %s\n", content_type, category, search_keyword);

      return TRUE;
   }

   ret = mc_search_foreach_condition(g_search_h, search_condition_cb, NULL);
   ```

5. Destroy the search handle using the `mc_search_destroy()`, when search handle is no longer needed:

   ```
   mc_search_destroy(g_search_h);
   ```

6. Destroy the media controller server handle using the `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   mc_server_destroy(g_server_h);
   ```

> **Note**
>
> This feature supports Tizen 5.0 and Higher for Mobile and Wearable.


## Media Controller Server State Attributes

The following table lists all the server state attributes the client can receive:

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
| `MC_PLAYBACK_STATE_MOVING_TO_NEXT` | Playback state of moving to next media (Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable) |
| `MC_PLAYBACK_STATE_MOVING_TO_PREVIOUS` | Playback state of moving to previous media (Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable) |
| `MC_PLAYBACK_STATE_FAST_FORWARDING` | Playback state of fast forwarding (Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable) |
| `MC_PLAYBACK_STATE_REWINDING`       | Playback state of rewinding (Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable) |


## Media Controller Playback Action Attributes

The following table lists all the playback action attributes the client can send command and the server can receive:

**Table: Media controller playback action attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Playback actions**             |                                          |
| `MC_PLAYBACK_ACTION_PLAY`        | Playback action of play                  |
| `MC_PLAYBACK_ACTION_PAUSED`      | Playback action of pause                 |
| `MC_PLAYBACK_ACTION_STOPPED`     | Playback action of stop                  |
| `MC_PLAYBACK_ACTION_NEXT`        | Playback action of moving to next media  |
| `MC_PLAYBACK_ACTION_PREV`        | Playback action of moving to previous media |
| `MC_PLAYBACK_ACTION_FAST_FORWARD` | Playback action of fast forward         |
| `MC_PLAYBACK_ACTION_REWIND`      | Playback action of rewind                |
| `MC_PLAYBACK_ACTION_TOGGLE_PLAY_PAUSE` | Playback action of toggle between play and pause |

> **Note**
>
> This Attributes support Tizen 4.0 and Higher for Mobile.


## Media Controller Shuffle Mode Attributes

The following table lists all the shuffle mode attributes the client can receive and send command:

**Table: Media controller shuffle mode attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Shuffle modes**                |                                          |
| `MC_SHUFFLE_MODE_ON`             | Shuffle mode is on                       |
| `MC_SHUFFLE_MODE_OFF`            | Shuffle mode is off                      |


## Media Controller Repeat Mode Attributes

The following table lists all the repeat mode attributes the client can receive and send command:

**Table: Media controller repeat mode attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Repeat mode states**           |                                          |
| `MC_REPEAT_MODE_ON`              | Repeat mode is on                        |
| `MC_REPEAT_MODE_OFF`             | Repeat mode is off                       |
| `MC_REPEAT_MODE_ONE_MEDIA`       | Repeat mode is on for one media (Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable) |


## Media Controller Server Metadata Attributes

The following table lists all the server metadata attributes the client can receive:

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


## Media Controller Playlist Update Mode Attributes

The following table lists all the playlist update mode attributes the client can receive:

**Table: Media controller playlist update mode attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Playlist update modes**        |                                          |
| `MC_PLAYLIST_UPDATED`            | Create or updated playlist               |
| `MC_PLAYBACK_REMOVED`            | Remove playlist                          |

> **Note**
>
> This Attributes support Tizen 4.0 and Higher for Mobile.

## Media Controller Content Type Attributes

The following table lists all the content type attributes the server can receive:

**Table: Media controller content type attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Content types**        |                                          |
| `MC_CONTENT_TYPE_IMAGE`          | Image content type                       |
| `MC_CONTENT_TYPE_VIDEO`          | Video content type                       |
| `MC_CONTENT_TYPE_MUSIC`          | Music content type                       |
| `MC_CONTENT_TYPE_OTHER`          | Other content type                       |
| `MC_CONTENT_TYPE_UNDECIDED`      | Content type is not decided              |

> **Note**
>
> This Attributes support Tizen 5.0 and Higher for Mobile and Wearable.

## Media Controller Search Category Attributes

The following table lists all the search category attributes the server can receive:

**Table: Media controller search category attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Search categories**        |                                          |
| `MC_SEARCH_NO_CATEGORY`          | No search category                       |
| `MC_SEARCH_TITLE`                | Search by content title                  |
| `MC_SEARCH_ARTIST`               | Search by content artist                 |
| `MC_SEARCH_ALBUM`                | Search by content album                  |
| `MC_SEARCH_GENRE`                | Search by content genre                  |
| `MC_SEARCH_TPO`                  | Search by Time Place Occasion            |

> **Note**
>
> This Attributes support Tizen 5.0 and Higher for Mobile and Wearable.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
