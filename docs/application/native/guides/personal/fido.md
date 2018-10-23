# FIDO Universal Authentication Framework


The FIDO (Fast IDentity Online) Alliance is a organization formed to address the lack of interoperability among strong authentication devices as well as the problems users face with creating and remembering multiple usernames and passwords.

FIDO covers both password-less authentications (through [FIDO UAF components](#fido_uaf_components)), such as fingerprint, iris, voice, and multi-factor authentication, such as OTP and USB dongle. Tizen currently does not support multi-factor authentication.

FIDO Alliance provides certification for FIDO-compliant products through FIDO Ready™.

<a name="fido_uaf_components"></a>
## FIDO UAF Components

UAF (Universal Authentication Framework) authenticators can be connected to a user device using various physical interfaces, such as SPI, USB, and Bluetooth. The UAF Authenticator-Specific Module (ASM) is a software interface on top of UAF authenticators, which gives a standardized way for the FIDO UAF clients to [detect and access the functionality of UAF authenticators](#find_auth), and hides the internal communication complexity from the clients.

The ASM is a platform-specific software component offering an API to FIDO UAF clients, enabling them to discover and communicate with 1 or more available authenticators. A single ASM can report on behalf of multiple authenticators.

The FIDO UAF protocol and its various operations are described in the [FIDO UAF Protocol Specification](https://fidoalliance.org/specs/fido-uaf-v1.0-ps-20141208/fido-uaf-protocol-v1.0-ps-20141208.html). The following figure shows a simplified architecture diagram of the interactions and actors.

**Figure: UAF high level architecture**

![UAF High Level Architecture](./media/fido_uaf_high_level_architecture.png)

The FIDO UAF consists of the following basic components:

- **FIDO UAF client**

  The FIDO UAF client implements the client side of the FIDO UAF protocols, and is responsible for interacting with specific FIDO UAF authenticators using the FIDO UAF authenticator abstraction layer through the FIDO UAF Authenticator API (in [mobile](../../api/mobile/latest/group__CAPI__FIDO__AUTHENTICATOR__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__FIDO__AUTHENTICATOR__MODULE.html) applications). Before you use the authenticators, [check whether the device can process the UAF protocol messages](#check_uaf_msg_supported).

- **FIDO UAF server**

  The FIDO UAF server implements the server side of the FIDO UAF protocols and is responsible for:

  - Interacting with the relying party Web server to [communicate FIDO UAF protocol messages to a FIDO UAF client](#set_server_result) using a device user agent.
  - Validating FIDO UAF authenticator attestations against the configured authenticator metadata to ensure only trusted authenticators are registered for use.
  - Managing the association of registered FIDO UAF authenticators to user accounts at the relying party.
  - Evaluating user authentication and transaction confirmation responses to determine their validity.

- **FIDO UAF protocols**

  The FIDO UAF protocols carry FIDO UAF messages between user devices and relying parties. [Use the protocol messages to register, authenticate, and deregister the authentication](#protocol_conversation):

  - Authenticator registration:

    The FIDO UAF registration protocol enables relying parties to discover the FIDO UAF authenticators available on a user's system or device. Discovery conveys the FIDO UAF authenticator attributes to the relying party, thus enabling policy decisions and enforcement to take place.

    **Figure: FIDO UAF registration**

    ![Components](./media/fido_reg_flow.png)

  - User authentication:

    Authentication is typically based on cryptographic challenge-response authentication protocols and facilitates the user choice regarding which FIDO UAF authenticators are employed in an authentication event.

    **Figure: FIDO UAF authentication**

    ![Components](./media/fido_auth_flow.png)

  - Authenticator deregistration:

    Deregistration is typically required when the user account is removed at the relying party. The relying party can trigger the deregistration by requesting the authenticator to delete the UAF credential associated with the user account.

    **Figure: FIDO UAF deregistration**

    ![Components](./media/fido_dereg_flow.png)

- **FIDO UAF authenticator abstraction layer**

  The FIDO UAF authenticator abstraction layer provides a uniform API to FIDO clients enabling the use of authenticator-based cryptographic services for FIDO-supported operations. It provides a uniform lower-layer "authenticator plugin" API facilitating the deployment of multi-vendor FIDO UAF authenticators and their requisite drivers.

- **FIDO UAF authenticator**

  The FIDO UAF authenticator is a secure entity, connected to or housed within the FIDO user devices, that can create key material associated with a relying party. The key can then be used to participate in FIDO UAF strong authentication protocols.

- **FIDO UAF authenticator metadata validation**

  In the FIDO UAF context, attestation is how authenticators make claims to a relying party during registration. They claim that the keys they generate, and certain measurements they report, originate from genuine devices with certified characteristics. An attestation signature, carried in a FIDO UAF registration protocol message, is validated by the FIDO UAF server.

## Prerequisites

To use the FIDO Client API (in [mobile](../../api/mobile/latest/group__CAPI__FIDO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__FIDO__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

```
<privileges>
   <privilege>http://tizen.org/privilege/fido.client</privilege>
</privileges>
```

<a name="find_auth"></a>
## Finding the FIDO Authenticator

To obtain the list of all available authenticators, use the `fido_foreach_authenticator()` function:

```
void
start_discover(void *data, Evas_Object *obj, void *event_info)
{
    int ret = fido_foreach_authenticator(auth_list_cb, data);
}

static void
auth_list_cb(const fido_authenticator_h auth, void *user_data)
{
    appdata_s *ad = user_data;
    __print_authinfo(auth, ad);
}

static void
__print_authinfo(fido_authenticator_h auth, appdata_s *ad)
{
    char *title = NULL;
    fido_authenticator_get_title(auth, &title);

    char *aaid = NULL;
    fido_authenticator_get_aaid(auth, &aaid);
}
```

<a name="check_uaf_msg_supported"></a>
## Checking the UAF Message Support

To check whether the given UAF protocol message can be processed by the device, use the `fido_uaf_is_supported()` function:

```
void
start_check_policy(void *data, Evas_Object *obj, void *event_info)
{
    bool is_supported = false;
    int ret = fido_uaf_is_supported(json_reg, &is_supported);

    char str[2048] = {0,};
    str[0] = '\0';

    strcpy(str, "CHECK POLICY RESPONSE | ");
    if (is_supported == true)
        sprintf(str, "TRUE");
    else
        sprintf(str, "FALSE");

    create_popup(str, (appdata_s *)user_data);
    free(error_string);
}
```

<a name="protocol_conversation"></a>
## Managing the Protocol Conversation

The core UAF protocol consists of conceptual conversations between the FIDO UAF client and the FIDO server.

To manage the conversations:

1. Register an authenticator.

   UAF allows the relying party to register a FIDO authenticator with the user account at the relying party. The relying party can specify a policy for supporting various FIDO authenticator types. A FIDO UAF client only registers existing authenticators that conform to that policy.

   ```
   void
   start_registration(void *data, Evas_Object *obj, void *event_info)
   {
       int ret = fido_uaf_get_response_message(json_reg, NULL, _process_cb, data);
   }

   static void
   _process_cb(fido_error_e tizen_error_code, const char *uaf_response, void *user_data)
   {
       char str[2048] = {0,};
       if (tizen_error_code == 0 && uaf_response != NULL) {
           const int max_popup_str_len = strlen(uaf_response) + 500;
           char *popup_str = calloc(1, max_popup_str_len);
           snprintf(popup_str, max_popup_str_len - 1, "UAF Response =%s", uaf_response);
           create_popup(popup_str, (appdata_s *)user_data);
           free(popup_str);
       }
   }
   ```

2. Authenticate a user.

   UAF allows the relying party to prompt the end user to authenticate using a previously registered FIDO authenticator. This authentication can be invoked any time, at the relying party's discretion.

   ```
   void
   start_auth(void *data, Evas_Object *obj, void *event_info)
   {
       int ret = fido_uaf_get_response_message(json_auth, NULL, _process_cb, data);
   }
   ```

3. Deregister an authentication key.

   The relying party can trigger the deletion of the account-related authentication key material.

   ```
   void
   start_de_registration(void *data, Evas_Object *obj, void *event_info)
   {
       int ret = fido_uaf_get_response_message(json_dereg, NULL, _process_dereg_cb, data);
   }

   static void
   _process_dereg_cb(int tizen_error_code, char *uaf_response, void *user_data)
   {
       char *error_string = get_error_code(tizen_error_code);
       create_popup(error_string, (appdata_s *)user_data);
       free(error_string);
   }
   ```

<a name="set_server_result"></a>
## Setting the Server Result

The server result is used to indicate the status code resulting from a FIDO UAF message delivered to the remote server.

To set the server result:

- Set the server result with success:

  ```
  void
  start_notify_pos(void *data, Evas_Object *obj, void *event_info)
  {
      if (json_reg != NULL)
          int ret = fido_uaf_get_response_message(json_reg, NULL, _process_cb_for_notify_pos, data);
  }

  static void
  _process_cb_for_notify_pos(fido_error_e tizen_error_code, const char *uaf_response, void *user_data)
  {
      int ret = fido_uaf_set_server_result(FIDO_SERVER_STATUS_CODE_OK, uaf_response);

      char *error_string = get_error_code(tizen_error_code);
      create_popup(error_string, (appdata_s *)user_data);
      free(error_string);
  }
  ```

- Set the server result with failure:

  ```
  void
  start_notify_neg(void *data, Evas_Object *obj, void *event_info)
  {
      int ret = fido_uaf_get_response_message(json_reg, NULL, _process_cb_for_notify_neg, data);
  }

  static void
  _process_cb_for_notify_neg(fido_error_e tizen_error_code, const char *uaf_response, void *user_data)
  {
      int ret = fido_uaf_set_server_result(0, uaf_response);

      char *error_string = get_error_code(tizen_error_code);
      create_popup(error_string, (appdata_s *)user_data);
      free(error_string);
  }
  ```

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
