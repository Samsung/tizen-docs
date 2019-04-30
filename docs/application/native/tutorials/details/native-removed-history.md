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

## Related information

- [Tizen Native API Reference](../../api/overview.md)
