# Media Controller


You can establish communication between a media controller server and a media controller client. You can send commands from the client to the server, and the client can request updated metadata and playback information from the server.

The main features of the Media Controller API include:

- Retrieving application list

  You can [retrieve the server and the client application list](#retrieving-application-list) to communicate with
the applications you want.
  Additionally, the client can get the latest server information even though the application is not activated currently. The last server that changed the state to "MC_PLAYBACK_STATE_PLAYING" becomes the latest server.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Updating and retrieving playback

  You can [update the playback information](#updating-and-retrieving-playback) on the server side, and then retrieve the playback information on the client side.

  The media controller server provides current information about the registered application that you can send to the client.

  When the client requests the information, the media controller server updates the state information of an active application before transferring the data. If the application is not running when the client request arrives, the media controller server transfers the latest information.

- Updating and retrieving metadata

  You can [update the metadata](#updating-and-retrieving-metadata) on the server side, and then retrieve the metadata on the client side.
  
  The media controller server can provide metadata of current playing content.
  
  > **Note**
  >
  > Since Tizen 5.5, metadata for Season, Episode, and Resolution are supported.

- Updating and retrieving playlist

  You can [update the playlist information](#updating-and-retrieving-playlist) on the server side, and then retrieve the playlist information on the client side.

  The media controller server provides current information about the registered application that you can send to the client.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Sending and processing commands

  You can [send a command](#sending-and-processing-commands) to the server from the client side, and then process the command on the server side.

  You can [send a reply of the command](#send_command_reply) to the client from the server side, and then receive the reply on the client side.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Sending a custom event to the client

  You can [send a custom event](#sending-and-processing-a-custom-event) to the client from the server side, and then process the event on the client side.

  You can [send a reply of the custom event](#send_event_reply) to the server from the client side, and then receive the reply on the server side.

  > **Note**
  >
  > This feature supports Tizen 4.0 and Higher for Mobile and Tizen 5.0 and Higher for Wearable.

- Sending and processing a search command

  You can [send a search command](#sending-and-processing-a-search-command) to the server from the client side, and then process the command on the server side.

  > **Note**
  >
  > This feature supports Tizen 5.0 and Higher for Mobile and Wearable.

- Updating and retrieving abilities

  You can [update the abilities](#updating-and-retrieving-abilities) on the server side, and then retrieve the abilities on the client side.

  The media controller server provides current abilities about the registered application.
  
  When the server supports abilities, then the media controller clients can send commands to the server.
  
  > **Note**
  >
  > This feature supports Tizen 5.5 and Higher for Mobile and Wearable.
  
## Prerequisites

To enable your application to use the media controller functionality:

- To use the media controller server:

  1. To use the Media Controller Server API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CONTROLLER__SERVER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CONTROLLER__SERVER__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

     ```
     <privileges>
        <privilege>http://tizen.org/privilege/mediacontroller.server</privilege>
     </privileges>
     ```
  
  2. To use the functions and data types of the Media Controller Server API, include the `<media_controller_server.h>` header file in your application:

     ```
     #include <media_controller_server.h>
     ```

  3. To work with the Media Controller Server API, define a handle variable for the media controller server:

     ```
     static mc_server_h g_server_h = NULL;
     ```

     The server updates the metadata and playback information, and processes the requests and commands sent by the client.

     This guide uses a global variable for the handle.

- To use the media controller client:

  1. To use the Media Controller Client API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__CONTROLLER__CLIENT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__CONTROLLER__CLIENT__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:
  
     ```
     <privileges>
        <privilege>http://tizen.org/privilege/mediacontroller.client</privilege>
     </privileges>
     ```
  
  2. To use the functions and data types of the Media Controller Client API, include the `<media_controller_client.h>` header file in your application:
  
     ```
     #include <media_controller_client.h>
     ```

  3. To work with the Media Controller Client API, define a handle variable for the media controller client:

     ```
     static mc_client_h g_client_h = NULL;
     ```

     The client requests metadata and playback information from the server, and sends playback commands to server.

     This guide uses a global variable for the handle.


## Retrieving Application List

To retrieve the latest server information on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using `mc_client_get_latest_server_info()`:

   ```
   char *server_name = NULL;
   mc_server_state_e server_state;

   ret = mc_client_get_latest_server_info(g_mc_client, &server_name, &server_state);
   dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Server state: %d\n", server_name, server_state);
   ```
To retrieve the server list on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server list using `mc_client_foreach_server()`:

   ```
   bool
   activated_server_cb(const char *server_name, void *user_data)
   {
       GList **server_list = (GList **)user_data;

       if (!server_list || !server_name) return FALSE;
       *server_list = g_list_append(*server_list, g_strdup(server_name));

       return TRUE;
   }

   GList *server_list = NULL;

   ret = mc_client_foreach_server(g_client_h, activated_server_cb, &server_list);
   ```

To retrieve the client list on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```
2. Retrieve the client list using `mc_server_foreach_client()`:

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

   ret = mc_server_foreach_client(g_server_h, activated_client_cb, &client_list);
   ```


## Updating and Retrieving Playback

To update the playback information on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Set the playback information to be updated using the corresponding `mc_server_set_XXX()` function, and then update the playback information using `mc_server_update_playback_info()`.

   For example, to update the playback state information, set the information to be updated using `mc_server_set_playback_state()`, and then update the information using `mc_server_update_playback_info()`:

   ```
   /* The following APIs can be set at the same time */
   ret = mc_server_set_playback_state(g_mc_server, MC_PLAYBACK_STATE_PLAYING);
   ret = mc_server_set_playback_position(g_mc_server, 150);
   
   /* Only Tizen 4.0 for Mobile */ 
   ret = mc_server_set_playlist_item_index(g_mc_server, 10);
   
   /* Since Tizen 5.0, the following APIs are supported */ 
   ret = mc_server_set_playlist_item_info(g_mc_server, "my_favoriates", 10);
   ret = mc_server_set_playback_content_type(g_mc_server, MC_CONTENT_TYPE_MUSIC);
   ret = mc_server_set_content_age_rating(g_mc_server, MC_CONTENT_RATING_7_PLUS);

   ret = mc_server_update_playback_info(g_mc_server);
   ```

3. Destroy the media controller server handle using `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   ret = mc_server_destroy(g_server_h);
   ```

To retrieve the playback information on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the [server name.](#retrieving-application-list)

3. Retrieve the playback information from the server using the corresponding `mc_client_get_server_XXX()` function. Use the server name retrieved in the previous step to identify the server.

   To retrieve the playback information from the server, use `mc_client_get_server_playback_info()`:

   ```
   mc_playback_h playback = NULL;
   mc_playback_states_e playback_state;
   unsigned long long position = 0;
   char *playlist_name = NULL;
   char *index = NULL;
   mc_content_type_e content_type;
   mc_content_age_rating_e age_rating;

   ret = mc_client_get_server_playback_info(g_client_h, server_name, &playback);
   ret = mc_client_get_playback_state(playback, &playback_state);
   ret = mc_client_get_playback_position(playback, &position);

   /* Only Tizen 4.0 for Mobile */ 
   ret = mc_client_get_playlist_item_index(playback, &index);

   /* Since Tizen 5.0, the following APIs are supported */ 
   ret = mc_client_get_playlist_item_info(playback, &playlist_name, &index);
   ret = mc_client_get_playback_content_type(playback, &content_type);
   ret = mc_client_get_age_rating(playback, &age_rating);
   ```

4. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```


## Updating and Retrieving Metadata
  
To update the metadata on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Set the metadata to be updated using `mc_server_set_metadata()` and then update the metadata using `mc_server_update_metadata()`:

   ```
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_TITLE, "title_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_ARTIST, "artist_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_ALBUM, "album_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_AUTHOR, "author_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_GENRE, "genre_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_DURATION, "duration_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_DATE, "date_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_COPYRIGHT, "copyright_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_DESCRIPTION, "desc_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_TRACK_NUM, "tracknum_1");
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_PICTURE, "picture_1");
   
   ret = mc_server_update_metadata(g_server_h);
   ```
   
   You must encode the values for MC_META_MEDIA_SEASON, MC_META_MEDIA_EPISODE, and MC_META_MEDIA_RESOLUTION. 
   
   To set the proper information, encode the metadata values using the corresponding `mc_metadata_encode_XXX()` function:
   
   ```
   char *encoded_meta = NULL;
   
   /* set season */
   mc_metadata_encode_season(8, "season_8", &encoded_meta);
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_SEASON, encoded_meta);
   free(encoded_meta);
   
   /* set episode */
   mc_metadata_encode_episode(5, "episode_5", &encoded_meta);
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_EPISODE, encoded_meta);
   free(encoded_meta);
   
   /* set resolution */
   mc_metadata_encode_resolution(1920, 1280, &encoded_meta);
   mc_server_set_metadata(g_server_h, MC_META_MEDIA_RESOLUTION, encoded_meta);
   free(encoded_meta);
   ```

3. Destroy the media controller server handle using `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   ret = mc_server_destroy(g_server_h);
   ```
   
To retrieve the metadata on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the [server name.](#retrieving-application-list)

3. Retrieve the encoded metadata from the server using `mc_client_get_server_metadata()`. Use the server name retrieved in the previous step to identify the server:

   ```
   mc_metadata_h metadata_h = NULL;
   char *value = NULL;
   int i = 0;
   
   ret = mc_client_get_server_metadata(g_client_h, server_name, &metadata_h);
   
   for (i = MC_META_MEDIA_TITLE; i <=  MC_META_MEDIA_PICTURE; i++) {
       mc_metadata_get(metadata_h, i, &value);
       ...
       free(value);
   }
   ```

   To get the proper information, you must decode the metadata values using the corresponding `mc_metadata_decode_XXX()` function.

   You can get the encoded values for  MC_META_MEDIA_SEASON, MC_META_MEDIA_EPISODE and MC_META_MEDIA_RESOLUTION using the following code:
   
   ```
   mc_metadata_h metadata_h = NULL;
   char *value = NULL;
   int num = 0;
   char *title = NULL;
   unsigned int width = 0;
   unsigned int height = 0;
   
   ret = mc_client_get_server_metadata(g_client_h, server_name, &metadata_h);
   
   /* get season */
   ret = mc_metadata_get(metadata_h, MC_META_MEDIA_SEASON, &value);
   
   mc_metadata_decode_season(value, &num, &title);
   ...
   free(title);
   free(value);
   
   /* get episode */
   ret = mc_metadata_get(metadata_h, MC_META_MEDIA_EPISODE, &value);
   
   mc_metadata_decode_episode(value, &num, &title);
   ...
   free(title);
   free(value);
   
   /* get resolution */
   ret = mc_metadata_get(metadata_h, MC_META_MEDIA_RESOLUTION, &value);
   mc_metadata_decode_resolution(value, &width, &height);
   ...
   
   free(value);
   ```
  
4. Destroy the metadata handle using `mc_metadata_destroy()`, when metadata handle is no longer needed:

   ```
   mc_metadata_destroy(metadata_h);
   ```
5. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

  > **Note**
  >
  > The MC_META_MEDIA_SEASON, MC_META_MEDIA_EPISODE, and MC_META_MEDIA_RESOLUTION features support Tizen 5.5 and Higher.
  
## Updating and Retrieving Playlist

To update the playlist and item's metadata on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```
2. Create the playlist handle using `mc_server_create_playlist()`:

   ```
   mc_playlist_h playlist_h = NULL;

   ret = mc_server_create_playlist(g_server_h, "playlist", &playlist_h);
   ```
3. Set the metadata in the playlist handle to be updated using `mc_server_add_item_to_playlist()`, and then update the playlist using `mc_server_update_playlist_done()`:

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
4. Destroy the playlist handle using `mc_playlist_destroy()`, when playlist handle is no longer needed:

   ```
   mc_playlist_destroy(playlist_h);
   ```

5. Destroy the media controller server handle using `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   ret = mc_server_destroy(g_server_h);
   ```

To retrieve the playlist and metadata on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

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

3. Register a callback using `mc_client_set_playlist_updated_cb()`:

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

5. Register a callback using `mc_playlist_foreach_item()`:

   ```
   ret = mc_playlist_foreach_item(playlist_h, playlist_item_cb, NULL);
   ```

6. Retrieve the metadata from the metadata handle using `mc_metadata_get()`:

   ```
   char *title = NULL;
   ret = mc_metadata_get(metadata_h, MC_META_MEDIA_TITLE, &title);
   ```

7. When no longer needed, destroy the playlist handle using `mc_playlist_destroy()`:

   ```
   mc_playlist_destroy(playlist_h);
   ```

8. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

> **Note**
>
> This feature supports Tizen 4.0 and Higher for Mobile.


## Sending and Processing Commands

To send a command to the server from the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the [server name.](#retrieving-application-list)

3. Set the callback function if you want to get the result of your sent command from the server using `mc_client_set_cmd_reply_received_cb()`:

   ```
   mc_playback_action_e playback_action = MC_PLAYBACK_ACTION_PLAY;
   char *request_id = NULL;

   ret = mc_client_set_cmd_reply_received_cb(g_client_h, server_name, playback_action, &request_id);
   ```
   
4. Send the command to the server using the corresponding `mc_client_send_XXX_cmd()` function. Use the server name retrieved in the previous step to identify the server.

   For example, to send a playback action change command to the server, use `mc_client_send_playback_action_cmd()` with the new action defined as the third parameter:

   ```
   mc_playback_action_e playback_action = MC_PLAYBACK_ACTION_PLAY;
   char *request_id = NULL;

   /* If you want to receive reply */
   ret = mc_client_send_playback_action_cmd(g_client_h, server_name, playback_action, &request_id);
   
   /* If you don't want to receive reply */
   ret = mc_client_send_playback_action_cmd(g_client_h, server_name, playback_action, NULL);
   ```
 
   You can send various commands using the following APIs:
   ```
   char *request_id = NULL; /* If you want to receive reply, set this */
   
   mc_client_send_playback_position_cmd(g_client_h, server_name, 15000, NULL);
   mc_client_send_shuffle_mode_cmd(g_client_h, server_name, MC_SHUFFLE_MODE_ON, NULL);
   mc_client_send_repeat_mode_cmd(g_client_h, server_name, MC_REPEAT_MODE_OFF, NULL);
   mc_client_send_playlist_cmd(g_client_h, server_name, "my_favorite", "1", MC_PLAYBACK_ACTION_PLAY, 0, NULL);
   
   /* Since Tizen 5.5, the following APIs are supported */
   mc_client_send_subtitles_cmd(g_client_h, server_name, TRUE, NULL);
   mc_client_send_360_mode_cmd(g_client_h, server_name, FALSE, NULL);
   mc_client_send_display_mode_cmd(g_client_h, server_name, MC_DISPLAY_MODE_FULL_SCREEN, NULL);
   mc_client_send_display_rotation_cmd(g_client_h, server_name, MC_DISPLAY_ROTATION_180, NULL);
   ```
   
   If you want to define custom commands, that you can send to the server, use `mc_client_send_custom_cmd()`:
   ```
   bundle *bundle_data = NULL;
   
   bundle_data = bundle_create();
   bundle_add_str(bundle_data, "key", "val");
   
   mc_client_send_custom_cmd(g_client_h, server_name, "custom_key", bundle_data, NULL);
   bundle_free(bundle_data);
   ```

   You can also send a search command. For more information, see [Sending and Processing a Search Command](#sending-and-processing-a-search-command).
   
5. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

To process the received command on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Define and register the callback that is invoked when the server receives the command.

   For example, to define a callback for playback state change commands:

   ```
   void
   playback_action_cmd_received_cb(const char* client_name, const char *request_id, mc_playback_action_e action, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Request ID: %s, Playback action: %d\n", client_name, request_id, action);
   }
   
   ret = mc_server_set_playback_action_cmd_received_cb(g_mc_server, playback_action_cmd_received_cb, NULL);
   ```

   - `mc_server_set_playback_action_cmd_received_cb()`: To register a callback for playback state change commands.
   - `mc_server_set_playback_position_cmd_received_cb()`: To register a callback for playback position change commands.
   - `mc_server_set_shuffle_mode_cmd_received_cb()`: To register a callback for shuffle mode change commands.
   - `mc_server_set_repeat_mode_cmd_received_cb()`: To register a callback for repeat mode change commands.
   - `mc_server_set_playlist_cmd_received_cb()`: To register a callback for played item, playback state, and playback position change commands in playlist.
   - `mc_server_set_custom_cmd_received_cb()`: To register a callback for custom commands.
   
   Since Tizen 5.5, the following APIs are also supported:
   - `mc_server_set_subtitles_cmd_received_cb()`: To register a callback for subtitles change commands.
   - `mc_server_set_360_mode_cmd_received_cb()`: To register a callback for 360 mode change commands.
   - `mc_server_set_display_mode_cmd_received_cb()`: To register a callback for display mode change commands.
   - `mc_server_set_display_rotation_cmd_received_cb()`: To register a callback for display rotation change commands.
   
3. Destroy the media controller server handle using `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   ret = mc_server_destroy(g_server_h);
   ```

To send the reply of completed command on the server side, follow these steps:

1. Send the reply of completed command using `mc_server_send_cmd_reply()` with the request ID of the command as the third parameter, and the result of the command as the fourth parameter:

   ```
   int result_code = 0;

   ret = mc_server_send_cmd_reply(g_server_h, client_name, request_id, result_code, NULL);
   ```

<a name="send_command_reply"></a>
To receive the reply of completed command on the client side, follow these steps:

1. Define and register the callback that is invoked when the client receives the reply:

   ```
   void
   cmd_reply_received_cb(const char *server_name, const char *request_id, int result_code, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Request ID: %s, Result Code: %d\n", server_name, request_id, result_code);
   }
   
   ret = mc_client_set_cmd_reply_received_cb(g_client_h, cmd_reply_received_cb, NULL);
   ```

> **Note**
>
> This feature supports Tizen 4.0 and Higher for Mobile.


## Sending and Processing a Custom Event

To send a custom event to the client from the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```

2. Retrieve the client name using `mc_server_foreach_client()`:

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

3. Send the event to the client using `mc_server_send_custom_event()`. Use the client name retrieved in the previous step to identify the client.

   For example, to send a custom event to the client, use `mc_server_send_custom_event()` with the event as the third parameter:

   ```
   char *request_id = NULL;

   ret = mc_server_send_custom_event(g_server_h, client_name, "evnet1", NULL, &request_id);
   ```

4. Destroy the media controller server handle using `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   ret = mc_server_destroy(g_server_h);
   ```

To process the received event on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Define the callback that is invoked when the client receives the event.

   For example, to define a callback for a custom event:

   ```
   void
   event_received_cb(const char* server_name, const char *request_id, const char *event, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Server Name: %s, Request ID: %s, Event: %s\n", server_name, request_id, event);
   }
   ```

3. Register a callback for custom event, use `mc_client_set_custom_event_received_cb()`: 

   ```
   ret = mc_client_set_custom_event_received_cb(g_client_h, event_received_cb, NULL);
   ```

4. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```


<a name="send_event_reply"></a>
To send the reply of completed custom event on the client side, follow these steps:

1. Send the reply of completed custom event using `mc_client_send_event_reply()` with the request ID of the custom event as the third parameter and the result of the custom event as the fourth parameter:

   ```
   int result_code = 0;

   ret = mc_client_send_event_reply(g_server_h, server_name, request_id, result_code, NULL);
   ```

To receive the reply of processing command on the server side, follow these steps:

1. Define the callback that is invoked when the server receives the reply:

   ```
   void
   event_reply_received_cb(const char *client_name, const char *request_id, int result_code, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Request ID: %s, Result Code: %d\n", client_name, request_id, result_code);
   }
   ```

2. Register a callback:

   ```
   ret = mc_server_set_event_reply_received_cb(g_server_h, event_reply_received_cb, NULL);
   ```

> **Note**
>
> This feature supports Tizen 4.0 and Higher for Mobile.


## Sending and Processing a Search Command

To send a search command to the server from the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Retrieve the server name using `mc_client_foreach_server()`:

   ```
   bool
   activated_server_cb(const char *server_name, void *user_data)
   {
       GList **server_list = (GList **)user_data;

       if (!server_list || !server_name) return FALSE;
       *server_list = g_list_append(*server_list, g_strdup(server_name));

       return TRUE;
   }

   GList *server_list = NULL;

   ret = mc_client_foreach_server(g_client_h, activated_server_cb, &server_list);
   ```

3. Create the search handle using `mc_search_create()`:

   ```
   ret = mc_search_create(&g_search_h);
   ```

4. Set the condition with a [content type](#media-controller-content-type-attributes), a [search category](#media-controller-search-category-attributes), and a search keyword using `mc_search_set_condition()`:

   ```
   ret = mc_search_set_condition(g_search_h, MC_CONTENT_TYPE_MUSIC, MC_SEARCH_TITLE, "keyword", NULL);
   ```

5. Send the search command to the server using `mc_client_send_search_cmd()`. Use the server name retrieved in the previous step to identify the server.
For example, to send the search command to the server, use `mc_client_send_search_cmd()` with the search handle as the third parameter:

   ```
   char *request_id = NULL;

   ret = mc_client_send_search_cmd(g_client_h, server_name, g_search_h, &request_id);
   ```

6. Destroy the search handle using `mc_search_destroy()`, when search handle is no longer needed:

   ```
   mc_search_destroy(g_search_h);
   ```

7. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   mc_client_destroy(g_client_h);
   ```

To process the received search command on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

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
       dlog_print(DLOG_DEBUG, LOG_TAG, "Client Name: %s, Request ID: %s\n", client_name, request_id);
       ret = mc_search_clone(search, get_search);
   }
   ```

3. Register a callback for search command, use `mc_server_set_search_cmd_received_cb()`:

   ```
   mc_search_h g_search_h = NULL;
   ret = mc_server_set_search_cmd_received_cb(g_server_h, search_command_received_cb, &g_search);
   ```

4. Retrieve the search condition using `mc_search_foreach_condition()`:

   ```
   bool
   search_condition_cb(mc_content_type_e content_type, mc_search_category_e category, const char *search_keyword, bundle *data, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "Content Type: %d, Search Category: %d, Search Keyword: %s\n", content_type, category, search_keyword);

       return TRUE;
   }

   ret = mc_search_foreach_condition(g_search_h, search_condition_cb, NULL);
   ```

5. Destroy the search handle using `mc_search_destroy()`, when search handle is no longer needed:

   ```
   mc_search_destroy(g_search_h);
   ```

6. Destroy the media controller server handle using `mc_server_destroy()`, when media controller server handle is no longer needed:

   ```
   ret = mc_server_destroy(g_server_h);
   ```

> **Note**
>
> This feature supports Tizen 5.0 and Higher for Mobile and Wearable.


## Updating and Retrieving Abilities
To update the abilities on the server side, follow these steps:

1. Create the media controller server handle using `mc_server_create()`:

   ```
   ret = mc_server_create(&g_server_h);
   ```
   
2. Set the abilities using the corresponding `mc_server_set_XXX_ability()`, or `mc_server_set_ability_support()`.
   
   To update the playback ability, set the ability for each playback action using `mc_server_set_playback_ability()`, and then update the ability using `mc_server_update_playback_ability()`:
   ```
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_PLAY, MC_ABILITY_SUPPORTED_YES);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_PAUSE, MC_ABILITY_SUPPORTED_NO);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_STOP, MC_ABILITY_SUPPORTED_YES);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_NEXT, MC_ABILITY_SUPPORTED_NO);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_PREV, MC_ABILITY_SUPPORTED_YES);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_FAST_FORWARD, MC_ABILITY_SUPPORTED_NO);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_REWIND, MC_ABILITY_SUPPORTED_YES);
   ret = mc_server_set_playback_ability(g_mc_server, MC_PLAYBACK_ACTION_TOGGLE_PLAY_PAUSE, MC_ABILITY_SUPPORTED_NO);
   
   ret = mc_server_update_playback_ability(g_mc_server);
   ```
   
   To update the display mode ability, set the ability using `mc_server_set_display_mode_ability()`:
   ```
   ret = mc_server_set_display_mode_ability(g_mc_server, MC_DISPLAY_MODE_LETTER_BOX | MC_DISPLAY_MODE_ORIGIN_SIZE | MC_DISPLAY_MODE_FULL_SCREEN | MC_DISPLAY_MODE_CROPPED_FULL, MC_ABILITY_SUPPORTED_YES);
   ```
   
   To update the display rotation ability, set the ability using `mc_server_set_display_rotation_ability()`:
    ```
   ret = mc_server_set_display_rotation_ability(g_mc_server, MC_DISPLAY_ROTATION_NONE | MC_DISPLAY_ROTATION_90 | MC_DISPLAY_ROTATION_180 | MC_DISPLAY_ROTATION_270, MC_ABILITY_SUPPORTED_YES);
   ```
   
   In case of other abilities, set the ability using `mc_server_set_ability_support()`, to update it. For example, to update shuffle and repeat ability, set the ability using `mc_server_set_ability_support()`:
   ```
   ret = mc_server_set_ability_support(g_mc_server, MC_ABILITY_SHUFFLE, MC_ABILITY_SUPPORTED_YES);
   ret = mc_server_set_ability_support(g_mc_server, MC_ABILITY_REPEAT, MC_ABILITY_SUPPORTED_NO);
   ```

To retrieve the abilities on the client side, follow these steps:

1. Create the media controller client handle using `mc_client_create()`:

   ```
   ret = mc_client_create(&g_client_h);
   ```

2. Define the callback that gets invoked when the client receives the change in abilities.

   To define a callback for a playback ability:
   ```
   ret = mc_client_set_playback_ability_updated_cb(g_client_h, _mc_playback_ability_updated_cb, NULL);
   ```
   
   - `mc_client_set_playback_ability_updated_cb()`: To register a callback for changing the playback ability.
   - `mc_client_set_display_mode_ability_updated_cb()`: To register a callback for changing the display mode ability.
   - `mc_client_set_display_rotation_ability_updated_cb()`: To register a callback for changing the display rotation ability.
   - `mc_client_set_ability_support_updated_cb()`: To register a callback for changing other abilities.
   
3. The client can get the server ability directly. For example, to get server playback ability:
   ```
   mc_playback_ability_h ability = NULL;
   ret = mc_client_get_server_playback_ability(g_client_h, "server_name", &ability);
   ```

   - `mc_client_get_server_display_mode_ability()`: For display mode ability.
   - `mc_client_get_server_display_rotation_ability()`: For display rotation ability.
   - `mc_client_get_server_ability_support()`: For other abilities.
   
4. Destroy the media controller client handle using `mc_client_destroy()`, when media controller client handle is no longer needed:

   ```
   ret = mc_client_destroy(g_client_h);
   ```
   
> **Note**
>
> This feature supports Tizen 5.5 and Higher for Mobile and Wearable.

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
> These attributes support Tizen 4.0 and Higher for Mobile.


## Media Controller Shuffle Mode Attributes

The following table lists all the shuffle mode attributes that the client can receive and send the command to:

**Table: Media controller shuffle mode attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Shuffle modes**                |                                          |
| `MC_SHUFFLE_MODE_ON`             | Shuffle mode is on                       |
| `MC_SHUFFLE_MODE_OFF`            | Shuffle mode is off                      |


## Media Controller Repeat Mode Attributes

The following table lists all the repeat mode attributes that the client can receive and send the command to:

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
> These attributes support Tizen 4.0 and Higher for Mobile.

## Media Controller Content Type Attributes

The following table lists all the content type attributes that the server can receive:

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
> These attributes support Tizen 5.0 and Higher for Mobile and Wearable.

## Media Controller Search Category Attributes

The following table lists all the search category attributes that the server can receive:

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
> These attributes support Tizen 5.0 and Higher for Mobile and Wearable.

## Media Controller Display Mode Attributes

The following table lists all the display mode attributes that the client can receive and send the command to:

**Table: Media controller display mode attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Display modes**                |                                          |
| `MC_DISPLAY_MODE_LETTER_BOX`     | Display mode is letter box               |
| `MC_DISPLAY_MODE_ORIGIN_SIZE`    | Display mode is origin size              |
| `MC_DISPLAY_MODE_FULL_SCREEN`    | Display mode is fullscreen               |
| `MC_DISPLAY_MODE_CROPPED_FULL`   | Display mode is cropped fullscreen       |

> **Note**
>
> These attributes support Tizen 5.5 and Higher for Mobile and Wearable.

## Media Controller Display Rotation Attributes

The following table lists all the display rotation attributes that the client can receive and send the command to:

**Table: Media controller display rotation attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Display rotations**            |                                          |
| `MC_DISPLAY_ROTATION_NONE`       | Display is not rotated                   |
| `MC_DISPLAY_ROTATION_90`         | Display is rotated 90 degrees            |
| `MC_DISPLAY_ROTATION_180`        | Display is rotated 180 degrees           |
| `MC_DISPLAY_ROTATION_270`        | Display is rotated 270 degrees           |

> **Note**
>
> These attributes support Tizen 5.5 and Higher for Mobile and Wearable.

## Media Controller Ability Attributes

The following table lists all the search category attributes that the server can receive:

**Table: Media controller ability attributes**

| Attribute                        | Description                              |
|----------------------------------|------------------------------------------|
| **Ability**                      |                                          |
| `MC_ABILITY_SHUFFLE`             | Ability for shuffle                      |
| `MC_ABILITY_REPEAT`              | Ability for repeat                       |
| `MC_ABILITY_PLAYBACK_POSITION`   | Ability for playback position            |
| `MC_ABILITY_PLAYLIST`            | Ability for playlist                     |
| `MC_ABILITY_CLIENT_CUSTOM`       | Ability for custom event                 |
| `MC_ABILITY_SEARCH`              | Ability for search                       |

> **Note**
>
> These attributes support Tizen 5.5 and Higher for Mobile and Wearable.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
