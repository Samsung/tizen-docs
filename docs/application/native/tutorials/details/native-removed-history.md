# Removed Functions and Enumerations of Tizen Native API

This page describes the functions and enumerations that were removed since Tizen 3.0.

If you want to know the lifecycle of Tizen Native API, you need to read the contents of [API Versioning and Deprecation Policy of the Tizen Platform](deprecation-policy.md) first.

The following table provides detailed information regarding removed functions and enumerations:

| Module | Items(s) | Deprecated | Removed | Reason | Alternatives |
| ------ | -------- | ---------- | ------- | ------ | ------------ |
| Security - OpenSSL | SSLv2_method(), SSLv2_client_method(), SSLv2_server_method() | - | 3.0 | Security | - |
| Base - Utils - i18n | i18n_timezone_in_daylight_time(), i18n_usearch_create(), i18n_ustring_to_title() | Since 2.3.1 | 4.0 | No longer available | - | 
| Web - WebView | ewk_context_preferred_languages_set(), ewk_settings_private_browsing_enabled_set(), ewk_settings_private_browsing_enabled_get() | Since 2.4 | 4.0 | No longer available | - |
| Base - Glib | Gdbus APIs (g_bus_\*(), g_dbus_\*(), and g_test_dbus_\*())| Since 2.3.2 | 5.0 | Security | - |
| Content - Media Content | audio_meta_get_played_count(), audio_meta_get_played_time(), audio_meta_get_played_position(), audio_meta_set_played_count(), audio_meta_set_played_time(), audio_meta_set_played_position(), media_content_set_db_updated_cb(), video_meta_get_played_time(), video_meta_get_played_position(), video_meta_set_played_count(), video_meta_set_played_time(), video_meta_set_played_position()| Since 2.4 | 5.0 | No longer available | - | 
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_TYPE_INSTALL of package_manager_event_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_TYPE_INSTALL |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_TYPE_UNINSTALL of package_manager_event_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_TYPE_UNINSTALL |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_TYPE_UPDATE of package_manager_event_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_TYPE_UPDATE |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_STARTED of package_manager_event_state_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_STARTED |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_PROCESSING of package_manager_event_state_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_PROCESSING |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_COMPLETED of package_manager_event_state_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_COMPLETED |
| Application Framework - Package Manager | PACAKGE_MANAGER_EVENT_STATE_FAILED of package_manager_event_state_e | - | 5.0 | Typo | PACKAGE_MANAGER_EVENT_STATE_FAILED |
| Application Framework - Package Manager | PACAKGE_MANAGER_REQUEST_MOVE_TO_INTERNAL of package_manager_move_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_REQUEST_MOVE_TO_INTERNAL |
| Application Framework - Package Manager | PACAKGE_MANAGER_REQUEST_MOVE_TO_EXTERNAL of package_manager_move_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_REQUEST_MOVE_TO_EXTERNAL |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_MATCH of package_manager_compare_result_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_MATCH |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_MISMATCH of package_manager_compare_result_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_MISMATCH |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_LHS_NO_CERT of package_manager_compare_result_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_LHS_NO_CERT |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_RHS_NO_CERT of package_manager_compare_result_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_RHS_NO_CERT |
| Application Framework - Package Manager | PACAKGE_MANAGER_COMPARE_BOTH_NO_CERT of package_manager_compare_result_type_e | - | 5.0 | Typo | PACKAGE_MANAGER_COMPARE_BOTH_NO_CERT |
| Multimedia - Image Util | image_util_decode_jpeg() | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() | 
| Multimedia - Image Util | image_util_decode_jpeg_from_memory() | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() |
| Multimedia - Image Util | image_util_decode_jpeg_with_downscale() | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() |
| Multimedia - Image Util | image_util_decode_jpeg_from_memory_with_downscale() | Since 3.0 | 5.0 | Better alternative | image_util_decode_create() |
| Multimedia - Image Util | image_util_encode_jpeg() | Since 3.0 | 5.0 | Better alternative | image_util_encode_create() |
| Multimedia - Image Util | image_util_encode_jpeg_to_memory() | Since 3.0 | 5.0 | Better alternative | image_util_encode_create() |
| Multimedia - Sound Manager | sound_manager_set_current_sound_type() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Sound Manager | sound_manager_unset_current_sound_type() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Sound Manager | sound_manager_set_volume_changed_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_add_volume_changed_cb() |
| Multimedia - Sound Manager | sound_manager_unset_volume_changed_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_remove_volume_changed_cb() |
| Multimedia - Sound Manager | sound_manager_set_session_type() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_session_type() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Sound Manager | sound_manager_set_media_session_option() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_media_session_option() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_set_media_session_resumption_option() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_media_session_resumption_option() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_set_voip_session_mode() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_voip_session_mode() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_set_session_interrupted_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_unset_session_interrupted_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Sound Manager | sound_manager_get_current_device_list() | Since 3.0 | 5.0 | Better alternative | sound_manager_get_device_list() |
| Multimedia - Sound Manager | sound_manager_set_device_connected_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_add_device_connection_changed_cb() |
| Multimedia - Sound Manager | sound_manager_unset_device_connected_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_remove_device_connection_changed_cb() |
| Multimedia - Sound Manager | sound_manager_set_device_information_changed_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_add_device_state_changed_cb() |
| Multimedia - Sound Manager | sound_manager_unset_device_information_changed_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_remove_device_connection_changed_cb() |
| Multimedia - WAV Player | wav_player_start() | Since 3.0 | 5.0 | Better alternative | wav_player_start_new() |
| Multimedia - Tone Player | tone_player_start() | Since 3.0 | 5.0 | Better alternative | tone_player_start_new() |
| Multimedia - Audio I/O | audio_in_set_interrupted_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Audio I/O | audio_in_unset_interrupted_cb() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_in_ignore_session() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_in_create_loopback() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Audio I/O | audio_out_set_interrupted_cb() | Since 3.0 | 5.0 | Better alternative | sound_manager_create_stream_information() |
| Multimedia - Audio I/O | audio_out_unset_interrupted_cb() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_out_ignore_session() | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Audio I/O | audio_out_create() | Since 3.0 | 5.0 | Better alternative | audio_out_create_new() |
| Multimedia - Radio | RADIO_INTERRUPTED_COMPLETED, RADIO_INTERRUPTED_BY_MEDIA, RADIO_INTERRUPTED_BY_CALL, RADIO_INTERRUPTED_BY_EARJACK_UNPLUG, RADIO_INTERRUPTED_BY_ALARM, RADIO_INTERRUPTED_BY_EMERGENCY, RADIO_INTERRUPTED_BY_RESUMABLE_MEDIA, RADIO_INTERRUPTED_BY_NOTIFICATION of radio_interrupted_code_e | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Player | player_set_sound_type() | Since 3.0 | 5.0 | Better alternative | player_set_sound_stream_info() |
| Network - Bluetooth | bt_adapter_le_start_device_discovery() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_stop_device_discovery() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_set_device_discovery_state_changed_cb() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_unset_device_discovery_state_changed_cb() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_add_advertising_data() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_remove_advertising_data() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_adapter_le_start_advertising() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_foreach_primary_services() | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_client_foreach_services or bt_gatt_client_get_service() |
| Network - Bluetooth | bt_gatt_get_service_uuid() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_foreach_included_services() | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_service_foreach_included_services() or bt_gatt_service_get_included_service() |
| Network - Bluetooth | bt_gatt_set_characteristic_changed_cb() | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_set_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_unset_characteristic_changed_cb() | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_unset_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_watch_characteristic_changes() | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_set_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_unwatch_characteristic_changes() | Since 2.3.1 | 5.0 | Better alternative | bt_gatt_client_unset_characteristic_value_changed_cb() |
| Network - Bluetooth | bt_gatt_get_characteristic_declaration() | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_get_value() or bt_gatt_get_uuid() after bt_gatt_client_read_value() |
| Network - Bluetooth | bt_gatt_set_characteristic_value() | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_set_value() and bt_gatt_client_write_value() |
| Network - Bluetooth | bt_gatt_read_characteristic_value() | Since 2.3.1 | 5.0 | Better alternative | gatt_client_read_value() |
| Network - Bluetooth | bt_gatt_set_characteristic_value_request() | Since 2.3.1 | 5.0 | Better alternatives | bt_gatt_set_value() and bt_gatt_client_write_value() |
| Network - Bluetooth | bt_gatt_clone_attribute_handle() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_destroy_attribute_handle() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_discover_characteristics() | Since 2.3.1 | 5.0 | No longer available | - |
| Network - Bluetooth | bt_gatt_discover_characteristic_descriptor() | Since 2.3.1 | 5.0 | No longer available | - |
| Social - Service Adaptor | All functions of this module | Since 3.0 | 5.0 | No longer available | - |
| Telephony - Telephony Information | telephony_call_get_voice_call_state(), telephony_call_get_video_call_state() | Since 3.0 | 5.0 | Better alternative | telephony_call_get_status() |
| UI - EFL - Eldbus | All functions of this module | Since 4.0 | 5.0 | Security | - |
| Multimedia - Recorder | RECORDER_ERROR_SOUND_POLICY, RECORDER_ERROR_SOUND_POLICY_BY_CALL, RECORDER_ERROR_SOUND_POLICY_BY_ALARM of recorder_error_e | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Recorder | RECORDER_POLICY_SOUND, RECORDER_POLICY_SOUND_BY_CALL, RECORDER_POLICY_SOUND_BY_ALARM of recorder_policy_e | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Camera | CAMERA_ERROR_SOUND_POLICY, CAMERA_ERROR_SOUND_POLICY_BY_CALL, CAMERA_ERROR_SOUND_POLICY_BY_ALARM of camera_error_e | Since 3.0 | 5.0 | No longer available | - |
| Multimedia - Camera | CAMERA_POLICY_SOUND, CAMERA_POLICY_SOUND_BY_CALL, CAMERA_POLICY_SOUND_BY_ALARM of camera_policy_e | Since 3.0 | 5.0 | No longer available | - |
| UI - EFL UTIL | efl_util_notification_window_level_error_cb(), efl_util_set_notification_window_level_error_cb(), efl_util_unset_notification_window_level_error_cb(), efl_util_window_screen_mode_error_cb(), efl_util_set_window_screen_mode_error_cb(), efl_util_unset_window_screen_mode_error_cb() | Since 3.0 | 5.0 | No longer available | - |
| Content - Media Content - Media Information | audio_meta_update_to_db() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | image_meta_get_burst_id(), image_meta_is_burst_shot(), image_meta_set_orientation(), image_meta_update_to_db() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Folder | media_folder_get_parent_folder_id(), media_folder_get_modified_time(), media_folder_get_order(), media_folder_set_name(), media_folder_set_order(), media_folder_update_to_db() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_insert_burst_shot_to_db(), media_info_delete_batch_from_db(), media_info_get_weather(), media_info_get_author(), media_info_get_provider(), media_info_get_content_name(), media_info_get_category(), media_info_get_location_tag() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_get_age_rating(), media_info_get_keyword(), media_info_get_played_count(), media_info_get_played_time(), media_info_increase_played_count(), media_info_set_played_time(), media_info_set_display_name(), media_info_set_description() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_set_longitude(), media_info_set_latitude(), media_info_set_altitude(), media_info_set_weather(), media_info_set_rating(), media_info_set_author(), media_info_set_provider(), media_info_set_content_name(), media_info_set_category() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_set_location_tag(), media_info_set_age_rating(), media_info_set_keyword(), media_info_refresh_metadata_to_db(), media_info_set_added_time(), media_info_create(), media_info_insert_to_db_with_data(), media_info_set_title() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | media_info_set_album(), media_info_set_artist(), media_info_set_genre(), media_info_set_recorded_date() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Storage | media_storage_get_name() | Since 4.0 | 5.5 | No longer available | - |
| Content - Media Content - Media Information | video_meta_update_to_db() | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_cancel_all() | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Media Controller Client | mc_client_set_server_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_set_server_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_server_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_unset_server_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_playback_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_set_playback_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_playback_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_unset_playback_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_metadata_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_set_metadata_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_metadata_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_unset_metadata_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_shuffle_mode_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_set_shuffle_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_shuffle_mode_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_unset_shuffle_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_repeat_mode_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_set_repeat_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_repeat_mode_update_cb() | Since 4.0 | 5.5 | Better alternative | mc_client_unset_repeat_mode_updated_cb() |
| Multimedia - Media Controller Client | mc_client_get_metadata() | Since 4.0 | 5.5 | Better alternative | mc_metadata_get() |
| Multimedia - Media Controller Client | mc_client_destroy_metadata() | Since 4.0 | 5.5 | Better alternative | mc_metadata_destroy() |
| Multimedia - Media Controller Client | mc_client_send_playback_state_command() | Since 4.0 | 5.5 | Better alternative | mc_client_send_playback_action_cmd() |
| Multimedia - Media Controller Client | mc_client_send_custom_command() | Since 4.0 | 5.5 | Better alternative | mc_client_send_custom_cmd() |
| Multimedia - Media Controller Client | mc_server_set_playback_state_command_received_cb() | Since 4.0 | 5.5 | Better alternative | mc_server_set_playback_action_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_unset_playback_state_command_received_cb() | Since 4.0 | 5.5 | Better alternative | mc_server_unset_playback_action_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_set_custom_command_received_cb() | Since 4.0 | 5.5 | Better alternative | mc_server_set_custom_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_unset_custom_command_received_cb() | Since 4.0 | 5.5 | Better alternative | mc_server_unset_custom_cmd_received_cb() |
| Multimedia - Media Controller Client | mc_server_send_command_reply() | Since 4.0 | 5.5 | Better alternative | mc_server_send_cmd_reply() |
| Multimedia - Player | player_set_progressive_download_path(), player_get_progressive_download_status(), player_set_progressive_download_message_cb(), player_unset_progressive_download_message_cb() | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Metadata Extractor | METADATA_AUTHOR of metadata_extractor_attr_e | Since 4.0 | 5.5 | Better alternative | METADATA_COMPOSER of metadata_extractor_attr_e |
| UI - DALi | Dali::Actor::GetPositionInheritanceMode() | Since 3.0 | 5.5 | Better alternative | Dali::Actor::IsPositionInherited() |
| UI - DALi | Dali::Actor::SetPositionInheritanceMode() | Since 3.0 | 5.5 | Better alternative | Dali::Actor::SetInheritPosition() |
| UI - DALi | Dali::Actor::Property::POSITION_INHERITANCE | Since 3.0 | 5.5 | Better alternative | Dali::Actor::Property::INHERIT_POSITION |
| UI - DALi | Dali::PositionInheritanceMode enum | Since 3.0 | 5.5 | Better alternative | Dali::Actor::SetInheritPosition() |
| UI - DALi | Dali::CustomActorImpl::ActorFlags::ACTOR_BEHAVIOUR_NONE | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::DrawMode::Type::STENCIL | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Layer::Behavior::LAYER_2D | Since 3.0 | 5.5 | Better alternative | Dali::Layer::Behavior::LAYER_UI |
| UI - DALi | Dali::ViewMode::STEREO_INTERLACED | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::TextField::Property::SHADOW_OFFSET | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextField::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextField::Property::SHADOW_COLOR | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextField::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextLabel::Property::SHADOW_OFFSET | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextLabel::Property::SHADOW_COLOR | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::SHADOW |
| UI - DALi | Dali::Toolkit::TextLabel::Property::UNDERLINE_ENABLED | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::UNDERLINE |
| UI - DALi | Dali::Toolkit::TextLabel::Property::UNDERLINE_COLOR | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::UNDERLINE |
| UI - DALi | Dali::Toolkit::TextLabel::Property::UNDERLINE_HEIGHT | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::TextLabel::Property::UNDERLINE |
| System - Runtime information | RUNTIME_INFO_KEY_LOCATION_SERVICE_ENABLED, RUNTIME_INFO_KEY_LOCATION_NETWORK_POSITION_ENABLED of runtime_info_key_e | Since 4.0 | 5.5 | No longer available | - |
| Multimedia - Player | PLAYER_DISPLAY_TYPE_OBSOLETE_EVAS_WNONE, PLAYER_DISPLAY_TYPE_OBSOLETE_NONE_WEVAS of player_display_type_e | Since 4.0 | 5.5 | No longer available | - |
| UI - EFL | elm_ctxpopup_direction_available_get(), elm_win_profiles_set() | Since 2.4 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::Button::Property::UNSELECTED_STATE_IMAGE | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::SELECTED_STATE_IMAGE | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::DISABLED_STATE_IMAGE | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::SELECTED_COLOR | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::UNSELECTED_COLOR | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::Property::LABEL_TEXT | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::SetDisabled(bool disabled) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED |
| UI - DALi | Dali::Toolkit::Button::IsDisabled() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED |
| UI - DALi | Dali::Toolkit::Button::SetAutoRepeating(bool autoRepeating) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::AUTO_REPEATING |
| UI - DALi | Dali::Toolkit::Button::IsAutoRepeating() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::AUTO_REPEATING |
| UI - DALi | Dali::Toolkit::Button::SetInitialAutoRepeatingDelay(float initialAutoRepeatingDelay) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::INITIAL_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::GetInitialAutoRepeatingDelay() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::INITIAL_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::SetNextAutoRepeatingDelay(float nextAutoRepeatingDelay) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::NEXT_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::GetNextAutoRepeatingDelay() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::NEXT_AUTO_REPEATING_DELAY |
| UI - DALi | Dali::Toolkit::Button::SetTogglableButton(bool togglable) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::TOGGLABLE |
| UI - DALi | Dali::Toolkit::Button::IsTogglableButton() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::TOGGLABLE |
| UI - DALi | Dali::Toolkit::Button::SetSelected(bool selected) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED |
| UI - DALi | Dali::Toolkit::Button::IsSelected() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED |
| UI - DALi | Dali::Toolkit::Button::SetAnimationTime(float animationTime) | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::Button::GetAnimationTime() const | Since 3.0 | 5.5 | No longer available | - |
| UI - DALi | Dali::Toolkit::Button::SetLabelText(const std::string& label) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::GetLabelText() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::SetUnselectedImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetBackgroundImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetSelectedImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetSelectedBackgroundImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetDisabledBackgroundImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetDisabledImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetDisabledSelectedImage(const std::string& filename) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetLabel(Actor label) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::LABEL |
| UI - DALi | Dali::Toolkit::Button::SetButtonImage(Image image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::SetSelectedImage(Image image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::GetButtonImage() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Button::GetSelectedImage() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetButtonImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetBackgroundImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::UNSELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetSelectedImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetSelectedBackgroundImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetDisabledBackgroundImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_BACKGROUND_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetDisabledImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_UNSELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::PushButton::SetDisabledSelectedImage(Actor image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Button::Property::DISABLED_SELECTED_VISUAL |
| UI - DALi | Dali::Toolkit::Internal::Control::GetBackgroundColor() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Internal::Control::SetBackgroundImage(Image image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::Property::BACKGROUND_COLOR | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::Property::BACKGROUND_IMAGE | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::GetBackgroundColor() const | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::Control::SetBackgroundImage(Image image) | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::Control::Property::BACKGROUND |
| UI - DALi | Dali::Toolkit::ImageView::Property::RESOURCE_URL | Since 3.0 | 5.5 | Better alternative | Dali::Toolkit::ImageView::Property::IMAGE |
| Network - Wi-Fi | wifi_initialize() | Since 3.0 | 5.5 | Better alternative | wifi_manager_initialize() |
| Network - Wi-Fi | wifi_deinitialize() | Since 3.0 | 5.5 | Better alternative | wifi_manager_deinitialize() |
| Network - Wi-Fi | wifi_activate() | Since 3.0 | 5.5 | Better alternative | wifi_manager_activate() |
| Network - Wi-Fi | wifi_activate_with_wifi_picker_tested() | Since 3.0 | 5.5 | Better alternative | wifi_manager_activate_with_wifi_picker_tested() |
| Network - Wi-Fi | wifi_deactivate() | Since 3.0 | 5.5 | Better alternative | wifi_manager_deactivate() |
| Network - Wi-Fi | wifi_is_activated() | Since 3.0 | 5.5 | Better alternative | wifi_manager_is_activated() |
| Network - Wi-Fi | wifi_get_mac_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_mac_address() |
| Network - Wi-Fi | wifi_get_network_interface_name() | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_network_interface_name() |
| Network - Wi-Fi | wifi_scan() | Since 3.0 | 5.5 | Better alternative | wifi_manager_scan() |
| Network - Wi-Fi | wifi_scan_specific_ap() | Since 3.0 | 5.5 | Better alternative | wifi_manager_scan_specific_ap() |
| Network - Wi-Fi | wifi_get_connected_ap() | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_connected_ap() |
| Network - Wi-Fi | wifi_foreach_found_aps() | Since 3.0 | 5.5 | Better alternative | wifi_manager_foreach_found_ap() |
| Network - Wi-Fi | wifi_foreach_found_specific_aps() | Since 3.0 | 5.5 | Better alternative | wifi_manager_foreach_found_specific_ap() |
| Network - Wi-Fi | wifi_connect() | Since 3.0 | 5.5 | Better alternative | wifi_manager_connect() |
| Network - Wi-Fi | wifi_disconnect() | Since 3.0 | 5.5 | Better alternative | wifi_manager_disconnect() |
| Network - Wi-Fi | wifi_connect_by_wps_pbc() | Since 3.0 | 5.5 | Better alternative | wifi_manager_connect_by_wps_pbc() |
| Network - Wi-Fi | wifi_connect_by_wps_pin() | Since 3.0 | 5.5 | Better alternative | wifi_manager_connect_by_wps_pin() |
| Network - Wi-Fi | wifi_forget_ap() | Since 3.0 | 5.5 | Better alternative | wifi_manager_forget_ap() |
| Network - Wi-Fi | wifi_get_connection_state() | Since 3.0 | 5.5 | Better alternative | wifi_manager_get_connection_state() |
| Network - Wi-Fi | wifi_set_device_state_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_device_state_changed_cb() |
| Network - Wi-Fi | wifi_unset_device_state_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_device_state_changed_cb() |
| Network - Wi-Fi | wifi_set_background_scan_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_background_scan_cb() |
| Network - Wi-Fi | wifi_unset_background_scan_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_background_scan_cb() |
| Network - Wi-Fi | wifi_set_connection_state_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_connection_state_changed_cb() |
| Network - Wi-Fi | wifi_unset_connection_state_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_connection_state_changed_cb() |
| Network - Wi-Fi | wifi_set_rssi_level_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_set_rssi_level_changed_cb() |
| Network - Wi-Fi | wifi_unset_rssi_level_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_unset_rssi_level_changed_cb() |
| Network - Wi-Fi | wifi_ap_create() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_create() |
| Network - Wi-Fi | wifi_ap_hidden_create() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_hidden_create() |
| Network - Wi-Fi | wifi_ap_destroy() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_destroy() |
| Network - Wi-Fi | wifi_ap_clone() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_clone() |
| Network - Wi-Fi | wifi_ap_refresh() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_refresh() |
| Network - Wi-Fi | wifi_ap_get_essid() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_essid() |
| Network - Wi-Fi | wifi_ap_get_bssid() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_bssid() |
| Network - Wi-Fi | wifi_ap_get_rssi() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_rssi() |
| Network - Wi-Fi | wifi_ap_get_frequency() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_frequency() |
| Network - Wi-Fi | wifi_ap_get_max_speed() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_max_speed() |
| Network - Wi-Fi | wifi_ap_is_favorite() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_favorite() |
| Network - Wi-Fi | wifi_ap_is_passpoint() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_passpoint() |
| Network - Wi-Fi | wifi_ap_get_connection_state() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_connection_state() |
| Network - Wi-Fi | wifi_ap_get_ip_config_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_ip_config_type() |
| Network - Wi-Fi | wifi_ap_set_ip_config_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_ip_config_type() |
| Network - Wi-Fi | wifi_ap_get_ip_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_ip_address() |
| Network - Wi-Fi | wifi_ap_set_ip_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_ip_address() |
| Network - Wi-Fi | wifi_ap_get_subnet_mask() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_subnet_mask() |
| Network - Wi-Fi | wifi_ap_set_subnet_mask() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_subnet_mask() |
| Network - Wi-Fi | wifi_ap_get_gateway_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_gateway_address() |
| Network - Wi-Fi | wifi_ap_set_gateway_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_gateway_address() |
| Network - Wi-Fi | wifi_ap_get_proxy_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_proxy_address() |
| Network - Wi-Fi | wifi_ap_set_proxy_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_proxy_address() |
| Network - Wi-Fi | wifi_ap_get_proxy_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_proxy_type() |
| Network - Wi-Fi | wifi_ap_set_proxy_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_proxy_type() |
| Network - Wi-Fi | wifi_ap_get_dns_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_dns_address() |
| Network - Wi-Fi | wifi_ap_set_dns_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_dns_address() |
| Network - Wi-Fi | wifi_ap_get_security_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_security_type() |
| Network - Wi-Fi | wifi_ap_set_security_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_security_type() |
| Network - Wi-Fi | wifi_ap_get_encryption_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_encryption_type() |
| Network - Wi-Fi | wifi_ap_set_encryption_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_encryption_type() |
| Network - Wi-Fi | wifi_ap_is_passphrase_required() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_passphrase_required() |
| Network - Wi-Fi | wifi_ap_set_passphrase() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_passphrase() |
| Network - Wi-Fi | wifi_ap_is_wps_supported() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_is_wps_supported() |
| Network - Wi-Fi | wifi_ap_set_eap_passphrase() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_passphrase() |
| Network - Wi-Fi | wifi_ap_get_eap_passphrase() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_passphrase() |
| Network - Wi-Fi | wifi_ap_get_eap_ca_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_ap_set_eap_ca_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_ap_get_eap_client_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_client_cert_file() |
| Network - Wi-Fi | wifi_ap_set_eap_client_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_client_cert_file() |
| Network - Wi-Fi | wifi_ap_get_eap_private_key_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_private_key_file() |
| Network - Wi-Fi | wifi_ap_set_eap_private_key_info() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_private_key_info() |
| Network - Wi-Fi | wifi_ap_get_eap_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_type() |
| Network - Wi-Fi | wifi_ap_set_eap_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_type() |
| Network - Wi-Fi | wifi_ap_get_eap_auth_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_get_eap_auth_type() |
| Network - Wi-Fi | wifi_ap_set_eap_auth_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_ap_set_eap_auth_type() |
| Network - Wi-Fi | wifi_config_create() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_create() |
| Network - Wi-Fi | wifi_config_clone() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_clone() |
| Network - Wi-Fi | wifi_config_destroy() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_destroy() |
| Network - Wi-Fi | wifi_config_save_configuration() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_save() |
| Network - Wi-Fi | wifi_config_remove() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_remove() |
| Network - Wi-Fi | wifi_config_foreach_configuration() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_foreach_configuration() |
| Network - Wi-Fi | wifi_config_get_name() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_name() |
| Network - Wi-Fi | wifi_config_get_security_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_security_type() |
| Network - Wi-Fi | wifi_config_set_proxy_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_proxy_address() |
| Network - Wi-Fi | wifi_config_get_proxy_address() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_proxy_address() |
| Network - Wi-Fi | wifi_config_set_hidden_ap_property() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_hidden_ap_property() |
| Network - Wi-Fi | wifi_config_get_hidden_ap_property() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_hidden_ap_property() |
| Network - Wi-Fi | wifi_config_get_eap_anonymous_identity() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_anonymous_identity() |
| Network - Wi-Fi | wifi_config_set_eap_anonymous_identity() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_anonymous_identity() |
| Network - Wi-Fi | wifi_config_get_eap_ca_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_config_set_eap_ca_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_ca_cert_file() |
| Network - Wi-Fi | wifi_config_get_eap_client_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_client_cert_file() |
| Network - Wi-Fi | wifi_config_set_eap_client_cert_file() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_client_cert_file() |
| Network - Wi-Fi | wifi_config_get_eap_identity() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_identity() |
| Network - Wi-Fi | wifi_config_set_eap_identity() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_identity() |
| Network - Wi-Fi | wifi_config_get_eap_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_type() |
| Network - Wi-Fi | wifi_config_set_eap_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_type() |
| Network - Wi-Fi | wifi_config_get_eap_auth_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_auth_type() |
| Network - Wi-Fi | wifi_config_set_eap_auth_type() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_auth_type() |
| Network - Wi-Fi | wifi_config_get_eap_subject_match() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_get_eap_subject_match() |
| Network - Wi-Fi | wifi_config_set_eap_subject_match() | Since 3.0 | 5.5 | Better alternative | wifi_manager_config_set_eap_subject_match() |
| Network - Wi-Fi | wifi_tdls_disconnect() | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_disconnect() |
| Network - Wi-Fi | wifi_tdls_get_connected_peer() | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_get_connected_peer() |
| Network - Wi-Fi | wifi_tdls_set_state_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_set_state_changed_cb() |
| Network - Wi-Fi | wifi_tdls_unset_state_changed_cb() | Since 3.0 | 5.5 | Better alternative | wifi_manager_tdls_unset_state_changed_cb() |
| Security - Privilege Info | privilege_info_get_privacy_privilege_status() | Since 5.0 | 6.0 | Better alternative | ppm_check_permission() |
| Network - Curl | CURLE_SSL_CACERT | Since 5.0 | 5.5 | Security | CURLE_PEER_FAILED_VERIFICATION |
| Network - Curl | CURLOPT_DNS_USE_GLOBAL_CACHE | Since 5.0 | 5.5 | Security | CURLOPT_SHARE |
| Multimedia - Video Util | video_util_create() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_destroy() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_file_path() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_accurate_mode() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_video_codec() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_audio_codec() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_file_format() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_resolution() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_set_fps() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_start_transcoding() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_cancel_transcoding() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_get_progress_transcoding() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_foreach_supported_file_format() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_foreach_supported_video_codec() | Since 5.0 | 6.0 | No longer available | - |
| Multimedia - Video Util | video_util_foreach_supported_audio_codec() | Since 5.0 | 6.0 | No longer available | - |
| UI - UI View Manager | All functions of this module | Since 6.0 | 7.0 | No longer available | - |
| UI - DALi | All functions of this module | Since 6.0 | 7.0 | No longer available | - |
| Application Framework - Widget - Widget Viewer DALi | All functions of this module | Since 6.0 | 7.0 | No longer available | - |
| Context - Activity Recognition | All functions of this module | Since 6.0 | 7.0 | No longer available | - |
| Context - Gesture Recognition | All functions of this module | Since 6.0 | 7.0 | No longer available | - |
| Content - Media Content | media_filter_set_storage() | Since 5.0 | 8.0 | Better alternative | media_filter_set_condition() |
| Content - Media Content | media_filter_get_storage() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_folder_get_storage_type() | Since 5.0 | 8.0 | Better alternative | storage_get_type_dev() |
| Content - Media Content | media_folder_get_storage_id() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_info_delete_from_db() | Since 5.0 | 8.0 | Better alternative | media_content_scan_file() |
| Content - Media Content | media_info_create_thumbnail() | Since 5.0 | 8.0 | Better alternative | media_info_generate_thumbnail() |
| Content - Media Content | media_info_cancel_thumbnail() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_info_get_storage_id() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_info_get_storage_type() | Since 5.0 | 8.0 | Better alternative | storage_get_type_dev() |
| Content - Media Content | media_storage_get_storage_info_from_db() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_storage_get_storage_count_from_db() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_storage_foreach_storage_from_db() | Since 5.0 | 8.0 | Better alternative | System - Storage |
| Content - Media Content | media_storage_get_media_count_from_db() | Since 5.0 | 8.0 | Better alternative | media_info_get_media_count_from_db() |
| Content - Media Content | media_storage_foreach_media_from_db() | Since 5.0 | 8.0 | Better alternative | media_info_foreach_media_from_db() |
| Content - Media Content | media_storage_destroy() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_storage_clone() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_storage_get_id() | Since 5.0 | 8.0 | No longer available | - |
| Content - Media Content | media_storage_get_path() | Since 5.0 | 8.0 | Better alternative | System - Storage |
| Content - Media Content | media_storage_get_type() | Since 5.0 | 8.0 | Better alternative | storage_get_type_dev() |
| Content - Media Content | media_content_storage_e | Since 5.0 | 8.0 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_create() | Since 5.0 | 8.0 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_extract() | Since 5.0 | 8.0 | Better alternative | thumbnail_util_extract_to_file(), thumbnail_util_extract_to_buffer() |
| Multimedia - Thumbnail Util | thumbnail_util_set_path() | Since 5.0 | 8.0 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_set_size() | Since 5.0 | 8.0 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_cancel() | Since 5.0 | 8.0 | No longer available | - |
| Multimedia - Thumbnail Util | thumbnail_util_destroy() | Since 5.0 | 8.0 | No longer available | - |
| Multimedia - Media Vision | mv_inference_target_type_e | Since 5.5 | 8.0 | No longer available | - |
| Multimedia - Media Vision | MV_INFERENCE_TARGET_TYPE | Since 5.5 | 8.0 | No longer available | - |
| UI - Clipboard History Manager | All functions of this module | - | 8.0 | No longer available | - |
| UI - Gesture | All functions of this module | - | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_FILE_NAME_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_TITLE_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_ALBUM_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_ARTIST_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_ALBUM_ARTIST_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_GENRE_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | MEDIA_COMPOSER_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Filter | FOLDER_NAME_PINYIN | Since 7.0 | 9.0 | No longer available | - |
| Multimedia - Stream Recorder | All functions of this module | Since 7.0 | 9.0 | No longer available | - |
| Multimedia - Image Util | image_util_calculate_buffer_size() | Since 5.5 | 9.0 | No longer available | - |
| Multimedia - Image Util | image_util_transform_set_hardware_acceleration() | Since 5.0 | 9.0 | No longer available | - |
| Multimedia - Image Util | image_util_encode_set_resolution() | Since 5.5 | 9.0 | Better alternative | image_util_create_image() |
| Multimedia - Image Util | image_util_encode_set_colorspace() | Since 5.5 | 9.0 | Better alternative | image_util_create_image() |
| Multimedia - Image Util | image_util_encode_set_webp_lossless() | Since 7.0 | 9.0 | Better alternative | image_util_encode_set_lossless() |
| Multimedia - Image Util | image_util_encode_set_gif_frame_delay_time() | Since 5.5 | 9.0 | Better alternative | image_util_agif_encode_add_frame() |
| Multimedia - Image Util | image_util_encode_set_input_buffer() | Since 5.5 | 9.0 | Better alternative | image_util_create_image() |
| Multimedia - Image Util | image_util_encode_set_output_path() | Since 5.5 | 9.0 | Better alternative | image_util_encode_run_to_file() or image_util_encode_run_async_to_file() |
| Multimedia - Image Util | image_util_encode_set_output_buffer() | Since 5.5 | 9.0 | Better alternative | image_util_encode_run_to_buffer() or image_util_encode_run_async_to_buffer() |
| Multimedia - Image Util | image_util_encode_run() | Since 5.5 | 9.0 | Better alternative | image_util_encode_run_to_file() or image_util_encode_run_to_buffer() |
| Multimedia - Image Util | image_util_encode_run_async() | Since 5.5 | 9.0 | Better alternative | image_util_encode_run_async_to_file() or image_util_encode_run_async_to_buffer() |
| Multimedia - Image Util | image_util_decode_set_output_buffer() | Since 5.5 | 9.0 | No longer available | - |
| Multimedia - Image Util | image_util_decode_run() | Since 5.5 | 9.0 | Better alternative | image_util_decode_run2() |
| Multimedia - Image Util | image_util_decode_run_async() | Since 5.5 | 9.0 | Better alternative | image_util_decode_run_async2() |
| Multimedia - Media Controller Client | mc_client_set_shuffle_ability_updated_cb() | Since 5.5 | 9.0 | Better alternative | mc_client_set_ability_support_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_shuffle_ability_updated_cb() | Since 5.5 | 9.0 | Better alternative | mc_client_unset_ability_support_updated_cb() |
| Multimedia - Media Controller Client | mc_client_set_repeat_ability_updated_cb() | Since 5.5 | 9.0 | Better alternative | mc_client_set_ability_support_updated_cb() |
| Multimedia - Media Controller Client | mc_client_unset_repeat_ability_updated_cb() | Since 5.5 | 9.0 | Better alternative | mc_client_unset_ability_support_updated_cb() |
| Multimedia - Media Controller Client | mc_client_get_playlist_item_index() | Since 5.0 | 9.0 | Better alternative | mc_client_get_playlist_item_info() |
| Multimedia - Media Controller Client | mc_client_get_server_shuffle_ability_support() | Since 5.5 | 9.0 | Better alternative | mc_client_get_server_ability_support() |
| Multimedia - Media Controller Client | mc_client_get_server_repeat_ability_support() | Since 5.5 | 9.0 | Better alternative | mc_client_get_server_ability_support() |
| Multimedia - Media Controller Client | mc_client_foreach_server_playlist() | Since 5.5 | 9.0 | Better alternative | mc_playlist_foreach_playlist() |
| Multimedia - Media Controller Server | mc_server_set_playlist_item_index() | Since 5.0 | 9.0 | Better alternative | mc_server_set_playlist_item_info() |
| Multimedia - Media Controller Server | mc_server_foreach_playlist() | Since 5.5 | 9.0 | Better alternative | mc_playlist_foreach_playlist() |
| Multimedia - Media Controller Server | mc_server_set_shuffle_ability() | Since 5.5 | 9.0 | Better alternative | mc_server_set_ability_support() |
| Multimedia - Media Controller Server | mc_server_set_repeat_ability() | Since 5.5 | 9.0 | Better alternative | mc_server_set_ability_support() |
| Multimedia - Media Streamer | All functions of this module | Since 7.0 | 9.0 | No longer available | - |
| Content - Media Content - Media Face | All functions of this module | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information - Image Metadata | image_meta_get_exposure_time() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information - Image Metadata | image_meta_get_fnumber() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information - Image Metadata | image_meta_get_iso() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information - Image Metadata | image_meta_get_model() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information | media_info_get_face_count_from_db() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information | media_info_foreach_face_from_db() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information | media_info_start_face_detection() | Since 8.0 | 10.0 | No longer available | - |
| Content - Media Content - Media Information | media_info_cancel_face_detection() | Since 8.0 | 10.0 | No longer available | - |

## Related information

- [Tizen Native API Reference](../../api/overview.md)
