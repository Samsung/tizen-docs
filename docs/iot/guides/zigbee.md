# Zigbee


Zigbee is a low-cost, low-power, wireless mesh network standard targeted at battery-powered devices in wireless control and monitoring applications. Zigbee delivers low-latency communication. Zigbee framework for Tizen provides hardware abstraction for application developer. Using Zigbee API set you can create, destroy, and manage Zigbee network.

Following are the main features of Zigbee API:

- [Create or Destroy Zigbee Service Handle](#create-or-destroy-zigbee-service-handle)
- [Enable or Disable Zigbee Device](#enable-or-disable-zigbee-device)
- [Form or Disable Zigbee Network Coordinator](#form-or-disable-zigbee-network-coordinator)
- [Permit Join](#permit-join)

Following is the list of supported hardware and chipset combinations:

- ARTIK 5 (inbuilt module)
- ARTIK 7 (inbuilt module)
- ARTIK 10 (inbuilt module)
- CEL's MeshConnect™ EM357 (external USB stick)

> **Note**
> - This feature is supported in the Tizen IoT.
> - You can test the Zigbee functionality only on a target device. The [Emulator](../../application/tizen-studio/common-tools/emulator.md) does not support this feature.
> - All callbacks in this module are called in the main loop context.

## Prerequisites

1. To make your application visible in the Tizen Store only for devices that support the Zigbee feature, the application must specify the following feature in the `tizen-manifest.xml` file:

   ```
    <feature name="http://tizen.org/feature/network.zigbee">true</feature>
   ```

2. To enable and disable Zigbee, the application must request permission by adding the following platform level privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/zigbee.admin</privilege>
   </privileges>
   ```

3. To do operations other than enabling and disabling Zigbee, the application must request permission by adding the following public level privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/zigbee</privilege>
   </privileges>
   ```

4. To use the functions and data types of the Zigbee API, include the following header file in your application:

   ```
   #include <zigbee.h>
   ```

## Create or Destroy Zigbee Service Handle

1. Call `zb_create()` to create a Zigbee service handle:

   ```
   int zb_create(zb_zigbee_h *handle);
   ```

2. Call `zb_destroy()` to destroy a Zigbee service handle:

   ```
   int zb_destroy(zb_zigbee_h handle);
   ```

## Enable or Disable Zigbee Device

1. To enable Zigbee, you must call `zb_enable()` API and wait for Zigbee state changed event `ZB_ZDP_ENABLE_EVENT`:

   ```
   static void _zb_event_cb(zb_nwk_addr addr16, zb_ieee_addr addr64, zb_event_e e,
                            zb_event_data_h ev, void* user_data)
   {
       // Handle e for ZB_ZDP_ENABLE_EVENT
   }

   zb_zigbee_h enable_zigbee_device(void)
   {
       zb_zigbee_h handle;
       int ret = ZIGBEE_ERROR_NONE;

       ret = zb_create(&handle);
       if (ZIGBEE_ERROR_NONE != ret) {
           printf("zb_create() - FAILED!!!");
           return NULL;
       }

       ret = zb_set_event_cb(handle, _zb_event_cb);
       if (ZIGBEE_ERROR_NONE != ret) {
           printf("zb_set_event_cb() - FAILED!!!");
           return NULL;
       }

       ret = zb_enable(handle);
       if (ZIGBEE_ERROR_NONE != ret) {
           printf("zb_enable() - FAILED!!!");
           return NULL;
       }

       return handle;
   }
   ```

2. To disable Zigbee, you must call `zb_disable()` API and wait for Zigbee state changed event `ZB_ZDP_ENABLE_EVENT`:

   ```
   static void _zb_event_cb(zb_nwk_addr addr16, zb_ieee_addr addr64, zb_event_e e,
                            zb_event_data_h ev, void* user_data)
   {
       // Handle e for ZB_ZDP_ENABLE_EVENT
   }

   int disable_zigbee_device(zb_zigbee_h handle)
   {
       int ret = ZIGBEE_ERROR_NONE;

       /*
        * It is expected that user has already registered zb_set_event_cb(handle, _zb_event_cb),
        * because the actual result proving that zigbee device has been disabled
        * will come in _zb_event_cb().
        */

       ret = zb_disable(handle);
       if (ZIGBEE_ERROR_NONE != ret) {
           printf("zb_disable() - FAILED!!!");
           return FALSE;
       }

       return TRUE;
   }
   ```

## Form or Disable Zigbee Network Coordinator

1. To form a zigbee network coordinator, you must call `zb_form_network()` API and wait for result in `zb_form_network_cb` callback:

   ```
   static void _zb_form_network_done_cb(zb_nwk_addr panid, void *user_data)
   {
       printf("form_network_done received PANID = 0x%04X\n", panid);
   }

   int run_form_network(zb_zigbee_h handle)
   {
       int ret = ZIGBEE_ERROR_NONE;

       ret = zb_form_network(handle, _zb_form_network_done_cb, NULL);
       if (ZIGBEE_ERROR_NONE != ret) {
               msg("zb_form_network() - FAILED!!!");
               return FALSE;
       }

       return TRUE;
   }
   ```

2. To disable a zigbee network coordinator, you must call `zb_disable_network()` API and wait for result in `zb_disable_network_cb` callback:

   ```
   static void _zb_disable_network_done_cb(unsigned char ret, void *user_data)
   {
       printf("disable_network result received = 0x%02X\n", ret);
   }

   int run_disable_network(zb_zigbee_h handle)
   {
       int ret = ZIGBEE_ERROR_NONE;

       ret = zb_disable_network(handle, _zb_disable_network_done_cb, NULL);
       if (ZIGBEE_ERROR_NONE != ret) {
               msg("zb_disable_network() - FAILED!!!");
               return FALSE;
       }

       return TRUE;
   }
   ```

## Permit Join

Zigbee framework for Tizen on ARTIK works as a Zigbee coordinator, therefore, permission is required to communicate with a new Zigbee device. Zigbee is enabled when a network is created or when a network is re-created. In both the scenarios, you need to make the coordinator to permit joining state.

   ```
   int permit_join(zb_zigbee_h handle)
   {
       int ret = ZIGBEE_ERROR_NONE;
       unsigned char timeout = 90;

       ret = zb_permit_join(handle, timeout);
       if (ZIGBEE_ERROR_NONE != ret) {
               msg("zb_permit_join() - FAILED!!!");
               return FALSE;
       }

       return TRUE;
   }
   ```

> **Note**
>
> After permit setting, enable Zigbee thing search mode using the Zigbee thing device. For more information, see the Zigbee thing's device manual.
>
> If the device is joined, you can see `ZB_ZDP_JOIN_EVENT` in callback registered using `zb_set_event_cb()` API.

## Related Information
- Dependencies
  - Tizen 5.0 and Higher for Tizen IoT

- Related Info
  - http://www.zigbee.org/
  - http://www.zigbee.org/download/standards-zigbee-specification/
  - http://www.zigbee.org/zigbee-for-developers/applicationstandards/zigbeehomeautomation/
  - https://wiki.tizen.org/Tizen_ZigbeeFW_On_ARTIK
