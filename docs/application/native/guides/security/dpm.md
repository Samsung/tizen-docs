# Device Policy Management


The Device Policy Management (DPM) framework supports enterprise applications by providing IT administrators means to create security-aware applications. They are useful in situations where IT administrators require rich control over employee devices.

DPM consists of a device policy client library and a device policy manager. The device policy manager manages all device policies and provides interfaces for the device policy client library. The device policy client library contains the device administration functions the client application can call. Internally, the device policy client library communicates with the device policy manager using a built-in remote method invocation engine.

The main features of the Device Policy Manager API include:

- Managing policies

  You can [track the state between the device admin client and the device policy manager](#client_application) with a device policy manager handle, provided by the Policy Manager Interface API (in [mobile](../../api/mobile/latest/group__CAPI__DPM__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__DPM__MANAGER__MODULE.html) applications).


- Checking restrictions

  You can [check the restriction states of the device](#client_application), such as camera, microphone, Wi-Fi, Bluetooth, and USB, using the getter functions of the Restriction policy group API (in [mobile](../../api/mobile/latest/group__CAPI__DPM__RESTRICTION__POLICY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__DPM__RESTRICTION__POLICY__MODULE.html) applications).

  You can also check the external and internal storage encryption state using the Security policy group API (in [mobile](../../api/mobile/latest/group__CAPI__DPM__SECURITY__POLICY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__DPM__SECURITY__POLICY__MODULE.html) applications) and get the name of the created zone and the zone state using the Zone policy group API (in [mobile](../../api/mobile/latest/group__CAPI__DPM__ZONE__POLICY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__DPM__ZONE__POLICY__MODULE.html) applications).

The following figure illustrates the DPM framework process.

**Figure: DPM framework process**

![DPM framework process](./media/dpm-framework.png)

## Prerequisites

To use the functions and data types of the Device Policy Manager API (in [mobile](../../api/mobile/latest/group__CAPI__SECURITY__DPM__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SECURITY__DPM__MODULE.html) applications), include the `<dpm/device-policy-manager.h>` header file in your application:

```
#include <dpm/device-policy-manager.h>
```

<a name="client_application"></a>
## Managing Device Policies

To manage device policies:

1. Create a DPM handle:

   ```
   device_policy_manager_h dpm;

   /* Create a DPM handle */
   dpm = dpm_manager_create();
   ```

2. Add a policy change callback to the device policy manager:

   ```
   int callback_id;

   /* Create the policy change callback function */
   void
   on_policy_changed(const char* name, const char* value, void* data)
   {
       int state = strcmp(value, "allowed") ? 0 : 1;

       if (strcmp(name, "camera") == 0) {
           if (state)
               /* Using the camera is allowed */
           else
               /* Using the camera is not allowed */
       }
   }

   /* Add the policy change callback to the device policy manager */
   int
   dpm_init()
   {
       int ret = dpm_add_policy_changed_cb(dpm, "camera", on_policy_changed, user_data, &callback_id);
       if (ret < 0)
           /* Error handling */
   }
   ```

3. Check the device restriction state:

   ```
   #include <dpm/restriction.h>

   int state;

   /* Check the restriction state of the camera */
   if (dpm_restriction_get_camera_state(dpm, &state) == DPM_ERROR_NONE) {
       /* state: 0: using the camera is not allowed */
       /* state: 1: using the camera is allowed */
   }
   ```

4. When no longer needed, remove the policy change callback from the device policy manager and destroy the DPM handle:

   ```
   void
   dpm_finalize()
   {
       /* Remove the policy change callback from the device policy manager */
       dpm_remove_policy_changed_cb(dpm, callback_id);
       /* Destroy the DPM handle */
       dpm_manager_destroy(dpm);
   }
   ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
