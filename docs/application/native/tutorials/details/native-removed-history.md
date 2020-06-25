# Removed functions and enumerations of Tizen Native API

This page describes the functions and enumerations that were removed since Tizen 3.0.

If you want to know the lifecycle of Tizen Native API, you need to read the contents of [API Versioning and Deprecation Policy of the Tizen Platform](deprecation-policy.md) first.

The following table provides detailed information regarding removed functions and enumerations:

| Module | Items(s) | Profile | Deprecated | Removed | Reason | Alternatives |
| ------ | -------- | ------- | ---------- | ------- | ------ | ------------ |
| Security - OpenSSL | SSLv2_method(), SSLv2_client_method(), SSLv2_server_method() | Mobile, Wearable | - | 3.0 | Security | - |
| Base - Utils - i18n | i18n_timezone_in_daylight_time(), i18n_usearch_create(), i18n_ustring_to_title() | Mobile, Wearable | Since 2.3.1 | 4.0 | No longer available | - | 
| Web - WebView | ewk_context_preferred_languages_set(), ewk_settings_private_browsing_enabled_set(), ewk_settings_private_browsing_enabled_get() | Mobile | Since 2.4 | 4.0 | No longer available | - |
| Base - Glib | Gdbus APIs (g_bus_\*(), g_dbus_\*(), and g_test_dbus_\*())| Mobile, Wearable | Since 2.3.2 | 5.0 | Security | - |
| Content - Media Content | audio_meta_get_played_count(), audio_meta_get_played_time(), audio_meta_get_played_position(), audio_meta_set_played_count(), audio_meta_set_played_time(), audio_meta_set_played_position(), media_content_set_db_updated_cb(), video_meta_get_played_time(), video_meta_get_played_position(), video_meta_set_played_count(), video_meta_set_played_time(), video_meta_set_played_position()|Mobile, Wearable | Since 2.4 | 5.0 | No longer available | - | 
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_TYPE_INSTALL of package_manager_event_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_TYPE_INSTALL |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_TYPE_UNINSTALL of package_manager_event_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_TYPE_UNINSTALL |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_TYPE_UPDATE of package_manager_event_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_TYPE_UPDATE |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_STARTED of package_manager_event_state_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_STARTED |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_PROCESSING of package_manager_event_state_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_PROCESSING |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_COMPLETED of package_manager_event_state_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_COMPLETED |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_FAILED of package_manager_event_state_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_FAILED |
| Application Framework - Package Manager | PACAKGE_MANAGER_REQUEST_MOVE_TO_INTERNAL of package_manager_move_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_REQUEST_MOVE_TO_INTERNAL |
| Application Framework - Package Manager | PACAKGE_MANAGER_REQUEST_MOVE_TO_EXTERNAL of package_manager_move_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_REQUEST_MOVE_TO_EXTERNAL |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_MATCH of package_manager_compare_result_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_MATCH |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_MISMATCH of package_manager_compare_result_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_MISMATCH |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_LHS_NO_CERT of package_manager_compare_result_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_LHS_NO_CERT |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_RHS_NO_CERT of package_manager_compare_result_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_RHS_NO_CERT |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_BOTH_NO_CERT of package_manager_compare_result_type_e | Mobile, Wearable | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_BOTH_NO_CERT |
| Multimedia - Image Util | image_util_decode_jpeg() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() | 
| Multimedia - Image Util | image_util_decode_jpeg_from_memory() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() |
| Multimedia - Image Util | image_util_decode_jpeg_with_downscale() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() |
| Multimedia - Image Util | image_util_decode_jpeg_from_memory_with_downscale() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() |
| Multimedia - Image Util | image_util_encode_jpeg() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | image_util_encode_create() |
| Multimedia - Image Util | image_util_encode_jpeg_to_memory() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | image_util_encode_create() |
| Multimedia - Sound Manager | sound_manager_set_current_sound_type() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Sound Manager | sound_manager_unset_current_sound_type() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Sound Manager | sound_manager_set_volume_changed_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_add_volume_changed_cb() |
| Multimedia - Sound Manager | sound_manager_unset_volume_changed_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_remove_volume_changed_cb() |
| Multimedia - Sound Manager | sound_manager_set_session_type() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_session_type() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Sound Manager | sound_manager_set_media_session_option() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_media_session_option() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_set_media_session_resumption_option() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_media_session_resumption_option() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_set_voip_session_mode() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_voip_session_mode() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_set_session_interrupted_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_unset_session_interrupted_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_current_device_list() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_get_device_list() |
| Multimedia - Sound Manager | sound_manager_set_device_connected_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_add_device_connection_changed_cb() |
| Multimedia - Sound Manager | sound_manager_unset_device_connected_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_remove_device_connection_changed_cb() |
| Multimedia - Sound Manager | sound_manager_set_device_information_changed_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_add_device_state_changed_cb() |
| Multimedia - Sound Manager | sound_manager_unset_device_information_changed_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_remove_device_connection_changed_cb() |
| Multimedia - WAV Player | wav_player_start() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | wav_player_start_new() |
| Multimedia - Tone Player | tone_player_start() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | tone_player_start_new() |
| Multimedia - Audio I/O | audio_in_set_interrupted_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Audio I/O | audio_in_unset_interrupted_cb() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_in_ignore_session() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_in_create_loopback() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Audio I/O | audio_out_set_interrupted_cb() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Audio I/O | audio_out_unset_interrupted_cb() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_out_ignore_session() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_out_create() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | audio_out_create_new() |
| Multimedia - Radio | RADIO_INTERRUPTED_COMPLETED, RADIO_INTERRUPTED_BY_MEDIA, RADIO_INTERRUPTED_BY_CALL, RADIO_INTERRUPTED_BY_EARJACK_UNPLUG, RADIO_INTERRUPTED_BY_ALARM, RADIO_INTERRUPTED_BY_EMERGENCY, RADIO_INTERRUPTED_BY_RESUMABLE_MEDIA, RADIO_INTERRUPTED_BY_NOTIFICATION of radio_interrupted_code_e | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Player | player_set_sound_type() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | player_set_sound_stream_info() |
| Network - Bluetooth | bt_adapter_le_start_device_discovery() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_stop_device_discovery() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_set_device_discovery_state_changed_cb() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_unset_device_discovery_state_changed_cb() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_add_advertising_data() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_remove_advertising_data() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_start_advertising() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_foreach_primary_services() | Mobile | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_client_foreach_services or bt_gatt_client_get_service() |
| Network - Bluetooth | bt_gatt_get_service_uuid() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_foreach_included_services() | Mobile | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_service_foreach_included_services() or bt_gatt_service_get_included_service() |
| Network - Bluetooth | bt_gatt_set_characteristic_changed_cb() | Mobile | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_set_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_unset_characteristic_changed_cb() | Mobile | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_unset_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_watch_characteristic_changes() | Mobile | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_set_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_unwatch_characteristic_changes() | Mobile | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_unset_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_get_characteristic_declaration() | Mobile | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_get_value() or bt_gatt_get_uuid() after bt_gatt_client_read_value() |
| Network - Bluetooth | bt_gatt_set_characteristic_value() | Mobile | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_set_value() and bt_gatt_client_write_value() |
| Network - Bluetooth | bt_gatt_read_characteristic_value() | Mobile | Since 2.3.1 | 5.0 | Better alternative | gatt_client_read_value() |
| Network - Bluetooth | bt_gatt_set_characteristic_value_request() | Mobile | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_set_value() and bt_gatt_client_write_value() |
| Network - Bluetooth | bt_gatt_clone_attribute_handle() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_destroy_attribute_handle() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_discover_characteristics() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_discover_characteristic_descriptor() | Mobile | Since 2.3.1 | 5.0 | No longer available | - |
| Social - Service Adaptor | All functions of this module | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Telephony - Telephony Information | telephony_call_get_voice_call_state(), telephony_call_get_video_call_state() | Mobile, Wearable | Since 3.0 | 5.0 | Better alternative | telephony_call_get_status() |
| UI - EFL - Eldbus | All functions of this module | Mobile, Wearable | Since 4.0 | 5.0 | Security | - |
| Multimedia - Recorder | RECORDER_ERROR_SOUND_POLICY, RECORDER_ERROR_SOUND_POLICY_BY_CALL, RECORDER_ERROR_SOUND_POLICY_BY_ALARM of recorder_error_e | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Recorder | RECORDER_POLICY_SOUND, RECORDER_POLICY_SOUND_BY_CALL, RECORDER_POLICY_SOUND_BY_ALARM of recorder_policy_e | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Camera | CAMERA_ERROR_SOUND_POLICY, CAMERA_ERROR_SOUND_POLICY_BY_CALL, CAMERA_ERROR_SOUND_POLICY_BY_ALARM of camera_error_e | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Camera | CAMERA_POLICY_SOUND, CAMERA_POLICY_SOUND_BY_CALL, CAMERA_POLICY_SOUND_BY_ALARM of camera_policy_e | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| UI - EFL UTIL | efl_util_notification_window_level_error_cb(), efl_util_set_notification_window_level_error_cb(), efl_util_unset_notification_window_level_error_cb(), efl_util_window_screen_mode_error_cb(), efl_util_set_window_screen_mode_error_cb(), efl_util_unset_window_screen_mode_error_cb() | Mobile, Wearable | Since 3.0 | 5.0 | No longer available | - |
| Content - Media Content - Media Information | audio_meta_update_to_db() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | image_meta_get_burst_id(), image_meta_is_burst_shot(), image_meta_set_orientation(), image_meta_update_to_db() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Folder | media_folder_get_parent_folder_id(), media_folder_get_modified_time(), media_folder_get_order(), media_folder_set_name(), media_folder_set_order(), media_folder_update_to_db() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_insert_burst_shot_to_db(), media_info_delete_batch_from_db(), media_info_get_weather(), media_info_get_author(), media_info_get_provider(), media_info_get_content_name(), media_info_get_category(), media_info_get_location_tag() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_get_age_rating(), media_info_get_keyword(), media_info_get_played_count(), media_info_get_played_time(), media_info_increase_played_count(), media_info_set_played_time(), media_info_set_display_name(), media_info_set_description() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_set_longitude(), media_info_set_latitude(), media_info_set_altitude(), media_info_set_weather(), media_info_set_rating(), media_info_set_author(), media_info_set_provider(), media_info_set_content_name(), media_info_set_category() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_set_location_tag(), media_info_set_age_rating(), media_info_set_keyword(), media_info_refresh_metadata_to_db(), media_info_set_added_time(), media_info_create(), media_info_insert_to_db_with_data(), media_info_set_title() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_set_album(), media_info_set_artist(), media_info_set_genre(), media_info_set_recorded_date() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Storage | media_storage_get_name() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | video_meta_update_to_db() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_cancel_all() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Media Controller Client | mc_client_set_server_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_set_server_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_server_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_unset_server_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_playback_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_set_playback_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_playback_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_unset_playback_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_metadata_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_set_metadata_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_metadata_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_unset_metadata_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_shuffle_mode_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_set_shuffle_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_shuffle_mode_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_unset_shuffle_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_repeat_mode_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_set_repeat_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_repeat_mode_update_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_unset_repeat_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_get_metadata() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_metadata_get() |
| Multimedia - Media Controller Client | mc_client_destroy_metadata() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_metadata_destroy() |
| Multimedia - Media Controller Client | mc_client_send_playback_state_command() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_send_playback_action_cmd() |
| Multimedia - Media Controller Client | mc_client_send_custom_command() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_client_send_custom_cmd() |
| Multimedia - Media Controller Client | mc_server_set_playback_state_command_received_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_server_set_playback_action_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_unset_playback_state_command_received_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_server_unset_playback_action_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_set_custom_command_received_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_server_set_custom_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_unset_custom_command_received_cb() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_server_unset_custom_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_send_command_reply() | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | mc_server_send_cmd_reply() |
| Multimedia - Player | player_set_progressive_download_path(), player_get_progressive_download_status(), player_set_progressive_download_message_cb(), player_unset_progressive_download_message_cb() | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Metadata Extractor | METADATA_AUTHOR of metadata_extractor_attr_e | Mobile, Wearable | Since 4.0 | 5.5 | Better alternative | METADATA_COMPOSER of metadata_extractor_attr_e |
| UI - DALi | Dali::Actor::GetPositionInheritanceMode() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Actor::IsPositionInherited() |
| UI - DALi | Dali::Actor::SetPositionInheritanceMode() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Actor::SetInheritPosition() |
| UI - DALi | Dali::Actor::Property::POSITION_INHERITANCE | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Actor::Property::INHERIT_POSITION |
| UI - DALi | Dali::PositionInheritanceMode enum | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Actor::SetInheritPosition() |
| UI - DALi | Dali::CustomActorImpl::ActorFlags::ACTOR_BEHAVIOUR_NONE | Mobile, Wearable | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::DrawMode::Type::STENCIL | Mobile, Wearable | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Layer::Behavior::LAYER_2D | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Layer::Behavior::LAYER_UI |
| UI - DALi | Dali::ViewMode::STEREO_INTERLACED | Mobile, Wearable | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::TextField::Property::SHADOW_OFFSET | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextField::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextField::Property::SHADOW_COLOR | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextField::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextLabel::Property::SHADOW_OFFSET | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextLabel::Property::SHADOW_COLOR | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextLabel::Property::UNDERLINE_ENABLED | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::UNDERLINE |
| UI - DALi | Dali::Toolkit::TextLabel::Property::UNDERLINE_COLOR | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::UNDERLINE |
| UI - DALi | Dali::Toolkit::TextLabel::Property::UNDERLINE_HEIGHT | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::UNDERLINE |
| System - Runtime information | RUNTIME_INFO_KEY_LOCATION_SERVICE_ENABLED, RUNTIME_INFO_KEY_LOCATION_NETWORK_POSITION_ENABLED of runtime_info_key_e | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Player | PLAYER_DISPLAY_TYPE_OBSOLETE_EVAS_WNONE, PLAYER_DISPLAY_TYPE_OBSOLETE_NONE_WEVAS of player_display_type_e | Mobile, Wearable | Since 4.0 | 5.5 | No longer available | - |
| UI - EFL | elm_ctxpopup_direction_available_get(), elm_win_profiles_set() | Mobile, Wearable | Since 2.4 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::Button::Property::UNSELECTED_STATE_IMAGE | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::SELECTED_STATE_IMAGE | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::DISABLED_STATE_IMAGE | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::SELECTED_COLOR | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::UNSELECTED_COLOR | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::LABEL_TEXT | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::SetDisabled(bool disabled) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED |
| UI - DALi | Dali::Toolkit::Button::IsDisabled() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED |
| UI - DALi | Dali::Toolkit::Button::SetAutoRepeating(bool autoRepeating) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::AUTO_REPEATING |
| UI - DALi | Dali::Toolkit::Button::IsAutoRepeating() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::AUTO_REPEATING |
| UI - DALi | Dali::Toolkit::Button::SetInitialAutoRepeatingDelay(float initialAutoRepeatingDelay) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::INITIAL_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::GetInitialAutoRepeatingDelay() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::INITIAL_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::SetNextAutoRepeatingDelay(float nextAutoRepeatingDelay) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::NEXT_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::GetNextAutoRepeatingDelay() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::NEXT_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::SetTogglableButton(bool togglable) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::TOGGLABLE |
| UI - DALi | Dali::Toolkit::Button::IsTogglableButton() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::TOGGLABLE |
| UI - DALi | Dali::Toolkit::Button::SetSelected(bool selected) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED |
| UI - DALi | Dali::Toolkit::Button::IsSelected() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED |
| UI - DALi | Dali::Toolkit::Button::SetAnimationTime(float animationTime) | Mobile, Wearable | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::Button::GetAnimationTime() const | Mobile, Wearable | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::Button::SetLabelText(const std::string& label) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::GetLabelText() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::SetUnselectedImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetBackgroundImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetSelectedImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetSelectedBackgroundImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetDisabledBackgroundImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetDisabledImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetDisabledSelectedImage(const std::string& filename) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetLabel(Actor label) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::SetButtonImage(Image image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetSelectedImage(Image image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::GetButtonImage() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::GetSelectedImage() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetButtonImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetBackgroundImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetSelectedImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetSelectedBackgroundImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetDisabledBackgroundImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetDisabledImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetDisabledSelectedImage(Actor image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Internal::Control::GetBackgroundColor() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Internal::Control::SetBackgroundImage(Image image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::Property::BACKGROUND_COLOR | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::Property::BACKGROUND_IMAGE | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::GetBackgroundColor() const | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::SetBackgroundImage(Image image) | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::ImageView::Property::RESOURCE_URL | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::ImageView::Property::IMAGE |
| Network - Wi-Fi | wifi_initialize() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_initialize() |
| Network - Wi-Fi | wifi_deinitialize() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_deinitialize() |
| Network - Wi-Fi | wifi_activate() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_activate() |
| Network - Wi-Fi | wifi_activate_with_wifi_picker_tested() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_activate_with_wifi_picker_tested() |
| Network - Wi-Fi | wifi_deactivate() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_deactivate() |
| Network - Wi-Fi | wifi_is_activated() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_is_activated() |
| Network - Wi-Fi | wifi_get_mac_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_mac_address() |
| Network - Wi-Fi | wifi_get_network_interface_name() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_network_interface_name() |
| Network - Wi-Fi | wifi_scan() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_scan() |
| Network - Wi-Fi | wifi_scan_specific_ap() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_scan_specific_ap() |
| Network - Wi-Fi | wifi_get_connected_ap() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_connected_ap() |
| Network - Wi-Fi | wifi_foreach_found_aps() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_foreach_found_ap() |
| Network - Wi-Fi | wifi_foreach_found_specific_aps() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_foreach_found_specific_ap() |
| Network - Wi-Fi | wifi_connect() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_connect() |
| Network - Wi-Fi | wifi_disconnect() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_disconnect() |
| Network - Wi-Fi | wifi_connect_by_wps_pbc() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_connect_by_wps_pbc() |
| Network - Wi-Fi | wifi_connect_by_wps_pin() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_connect_by_wps_pin() |
| Network - Wi-Fi | wifi_forget_ap() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_forget_ap() |
| Network - Wi-Fi | wifi_get_connection_state() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_connection_state() |
| Network - Wi-Fi | wifi_set_device_state_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_device_state_changed_cb() |
| Network - Wi-Fi | wifi_unset_device_state_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_device_state_changed_cb() |
| Network - Wi-Fi | wifi_set_background_scan_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_background_scan_cb() |
| Network - Wi-Fi | wifi_unset_background_scan_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_background_scan_cb() |
| Network - Wi-Fi | wifi_set_connection_state_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_connection_state_changed_cb() |
| Network - Wi-Fi | wifi_unset_connection_state_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_connection_state_changed_cb() |
| Network - Wi-Fi | wifi_set_rssi_level_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_rssi_level_changed_cb() |
| Network - Wi-Fi | wifi_unset_rssi_level_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_rssi_level_changed_cb() |
| Network - Wi-Fi | wifi_ap_create() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_create() |
| Network - Wi-Fi | wifi_ap_hidden_create() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_hidden_create() |
| Network - Wi-Fi | wifi_ap_destroy() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_destroy() |
| Network - Wi-Fi | wifi_ap_clone() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_clone() |
| Network - Wi-Fi | wifi_ap_refresh() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_refresh() |
| Network - Wi-Fi | wifi_ap_get_essid() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_essid() |
| Network - Wi-Fi | wifi_ap_get_bssid() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_bssid() |
| Network - Wi-Fi | wifi_ap_get_rssi() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_rssi() |
| Network - Wi-Fi | wifi_ap_get_frequency() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_frequency() |
| Network - Wi-Fi | wifi_ap_get_max_speed() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_max_speed() |
| Network - Wi-Fi | wifi_ap_is_favorite() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_favorite() |
| Network - Wi-Fi | wifi_ap_is_passpoint() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_passpoint() |
| Network - Wi-Fi | wifi_ap_get_connection_state() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_connection_state() |
| Network - Wi-Fi | wifi_ap_get_ip_config_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_ip_config_type() |
| Network - Wi-Fi | wifi_ap_set_ip_config_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_ip_config_type() |
| Network - Wi-Fi | wifi_ap_get_ip_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_ip_address() |
| Network - Wi-Fi | wifi_ap_set_ip_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_ip_address() |
| Network - Wi-Fi | wifi_ap_get_subnet_mask() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_subnet_mask() |
| Network - Wi-Fi | wifi_ap_set_subnet_mask() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_subnet_mask() |
| Network - Wi-Fi | wifi_ap_get_gateway_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_gateway_address() |
| Network - Wi-Fi | wifi_ap_set_gateway_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_gateway_address() |
| Network - Wi-Fi | wifi_ap_get_proxy_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_proxy_address() |
| Network - Wi-Fi | wifi_ap_set_proxy_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_proxy_address() |
| Network - Wi-Fi | wifi_ap_get_proxy_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_proxy_type() |
| Network - Wi-Fi | wifi_ap_set_proxy_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_proxy_type() |
| Network - Wi-Fi | wifi_ap_get_dns_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_dns_address() |
| Network - Wi-Fi | wifi_ap_set_dns_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_dns_address() |
| Network - Wi-Fi | wifi_ap_get_security_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_security_type() |
| Network - Wi-Fi | wifi_ap_set_security_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_security_type() |
| Network - Wi-Fi | wifi_ap_get_encryption_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_encryption_type() |
| Network - Wi-Fi | wifi_ap_set_encryption_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_encryption_type() |
| Network - Wi-Fi | wifi_ap_is_passphrase_required() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_passphrase_required() |
| Network - Wi-Fi | wifi_ap_set_passphrase() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_passphrase() |
| Network - Wi-Fi | wifi_ap_is_wps_supported() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_wps_supported() |
| Network - Wi-Fi | wifi_ap_set_eap_passphrase() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_passphrase() |
| Network - Wi-Fi | wifi_ap_get_eap_passphrase() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_passphrase() |
| Network - Wi-Fi | wifi_ap_get_eap_ca_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_ap_set_eap_ca_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_ap_get_eap_client_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_client_cert_file() |
| Network - Wi-Fi | wifi_ap_set_eap_client_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_client_cert_file() |
| Network - Wi-Fi | wifi_ap_get_eap_private_key_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_private_key_file() |
| Network - Wi-Fi | wifi_ap_set_eap_private_key_info() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_private_key_info() |
| Network - Wi-Fi | wifi_ap_get_eap_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_type() |
| Network - Wi-Fi | wifi_ap_set_eap_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_type() |
| Network - Wi-Fi | wifi_ap_get_eap_auth_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_auth_type() |
| Network - Wi-Fi | wifi_ap_set_eap_auth_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_auth_type() |
| Network - Wi-Fi | wifi_config_create() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_create() |
| Network - Wi-Fi | wifi_config_clone() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_clone() |
| Network - Wi-Fi | wifi_config_destroy() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_destroy() |
| Network - Wi-Fi | wifi_config_save_configuration() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_save() |
| Network - Wi-Fi | wifi_config_remove() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_remove() |
| Network - Wi-Fi | wifi_config_foreach_configuration() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_foreach_configuration() |
| Network - Wi-Fi | wifi_config_get_name() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_name() |
| Network - Wi-Fi | wifi_config_get_security_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_security_type() |
| Network - Wi-Fi | wifi_config_set_proxy_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_proxy_address() |
| Network - Wi-Fi | wifi_config_get_proxy_address() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_proxy_address() |
| Network - Wi-Fi | wifi_config_set_hidden_ap_property() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_hidden_ap_property() |
| Network - Wi-Fi | wifi_config_get_hidden_ap_property() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_hidden_ap_property() |
| Network - Wi-Fi | wifi_config_get_eap_anonymous_identity() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_anonymous_identity() |
| Network - Wi-Fi | wifi_config_set_eap_anonymous_identity() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_anonymous_identity() |
| Network - Wi-Fi | wifi_config_get_eap_ca_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_config_set_eap_ca_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_config_get_eap_client_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_client_cert_file() |
| Network - Wi-Fi | wifi_config_set_eap_client_cert_file() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_client_cert_file() |
| Network - Wi-Fi | wifi_config_get_eap_identity() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_identity() |
| Network - Wi-Fi | wifi_config_set_eap_identity() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_identity() |
| Network - Wi-Fi | wifi_config_get_eap_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_type() |
| Network - Wi-Fi | wifi_config_set_eap_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_type() |
| Network - Wi-Fi | wifi_config_get_eap_auth_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_auth_type() |
| Network - Wi-Fi | wifi_config_set_eap_auth_type() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_auth_type() |
| Network - Wi-Fi | wifi_config_get_eap_subject_match() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_subject_match() |
| Network - Wi-Fi | wifi_config_set_eap_subject_match() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_subject_match() |
| Network - Wi-Fi | wifi_tdls_disconnect() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_disconnect() |
| Network - Wi-Fi | wifi_tdls_get_connected_peer() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_get_connected_peer() |
| Network - Wi-Fi | wifi_tdls_set_state_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_set_state_changed_cb() |
| Network - Wi-Fi | wifi_tdls_unset_state_changed_cb() | Mobile, Wearable | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_unset_state_changed_cb() |
| Security - Privilege Info | privilege_info_get_privacy_privilege_status() | Mobile, Wearable | Since 5.0 | 6.0 | Better alternative | ppm_check_permission() |

## Related information

- [Tizen Native API Reference](../../api/overview.md)
