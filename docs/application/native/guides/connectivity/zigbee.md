# Zigbee


Zigbee is a low-cost, low-power, wireless mesh network standard targeted at battery-powered devices in wireless control and monitoring applications. Zigbee delivers low-latency communication. Tizen's Zigbee framework provides hardware abstraction for application developer. Using Zigbee API set you can create, destroy and manage Zigbee network.

Following are the main features of Zigbee API:

- [Creating or Destroying Zigbee Service Handle](#creating-or-destroying-zigbee-service-handle)
- [Enable or Disable Zigbee Device](#enable-or-disable-zigbee-device)
- [Form or Disable Zigbee Network Coordinator](#form-or-disable-zigbee-network-coordinator)
- [Permit Join](#permit-join)
- [Select Target Device](#select-target-device)

Following is the list of supported hardware and chipset combinations:

- Artik 5 (Inbuilt module)
- Artik 7 (Inbuilt module)
- Artik 10 (Inbuilt module)
- CEL EM357 (External USB stick)

> **Note**
> - This feature is supported in the Tizen IoT.
> - You can test the Zigbee functionality only on a target device. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.
> - All callbacks in this module are called in the main loop context.

## Prerequisites

Below are the prerequisites for Zigbee API:

1. To make your application visible in the Tizen Store only for devices that support the Zigbee feature, the application must specify the following feature in the `tizen-manifest.xml` file:

   ```
    <feature name="http://tizen.org/feature/network.zigbee">true</feature>
   ```

2. To enable and disable Zigbee, the application has to request permission by adding the following platform level privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/zigbee.admin</privilege>
   </privileges>
   ```

3. To do operations other than enabling and disabling Zigbee, the application has to request permission by adding the following public level privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/zigbee</privilege>
   </privileges>
   ```

4. To use the functions and data types of the Zigbee API, include the following header file in your application:

   ```
   #include <zigbee.h>
   ```

## Creating or Destroying Zigbee Service Handle

1. Call the `zb_create()` function to create zigbee service handle:

   ```
   int zb_create(zb_zigbee_h *handle);
   ```

2. Call the `zb_destroy()` function to destroy zigbee service handle:

   ```
   int zb_destroy(zb_zigbee_h handle);
   ```

## Enable or Disable Zigbee Device

1. To enable Zigbee, you must call `zb_enable()` API and wait for Zigbee state changed event `ZB_ZDP_ENABLE_EVENT`.

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

2. To disable Zigbee, you must call `zb_disable()` API and wait for Zigbee state changed event `ZB_ZDP_ENABLE_EVENT`.

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

1. To form a zigbee network coordinator, you must call `zb_form_network()` API and wait for result in `zb_form_network_cb` callback.

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

2. To disable a zigbee network coordinator, you must call `zb_disable_network()` API and wait for result in `zb_disable_network_cb` callback.

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

Tizen Zigbee Framework on ARTIK works as a Zigbee coordinator, therefore, permission is required to communicate with a new Zigbee device. Zigbee is enabled when a network is created or when a network is re-created. In both the scenarios, you need to make the coordinator to permit joining state.

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
> After permit setting, enable Zigbee thing search mode using the Zigbee thing device. For more information, see the device manual.
>
> If the device is joined, you can see `ZB_ZDP_JOIN_EVENT` in callback registered using `zb_set_event_cb()` API.

## Select Target Device
To communicate specific Zigbee thing in network, you need to select the target device. If target device is selected, you can communicate and send data to it.

   ```
    static int run_choose_end_device_list(MManager *mm, struct menu_data *menu)
    {
            int ret = ZIGBEE_ERROR_NONE;
            int i, j;
            zb_nwk_addr addr16;
            zb_ieee_addr addr64;
            unsigned char num_of_ep;
            zb_end_point *ep_list = NULL;

            if (NULL != target_list)
                    zb_end_dev_info_list_free(target_list);

            ret = zb_end_dev_get_end_dev_info_list(handle, &target_list_count, &target_list);

            printf(" - zb_end_dev_get_end_dev_info_list() ret: [0x%X] [%s]",
                    ret, zigbee_error_to_string(ret));
            printf("");

            for (i = 0; i < target_list_count && target_list; i++) {
                    zb_end_dev_info_get_network_address(target_list[i], &addr16);
                    zb_end_dev_info_get_ieee_address((target_list)[i], addr64);

                    printf("[# %02d] End device", (i+1));
                    if (!strncmp((char *)sj_addr64, (char *)addr64, sizeof(addr64))) {
                            sj_addr16 = addr16;
                            printf("   Found [Samjin Power Outlet] !!");
                    }
                    if (!strncmp((char *)st_addr64, (char *)addr64, sizeof(addr64))) {
                            st_addr16 = addr16;
                            printf("   Found [ST Open/Close Sensor] !!");
                    }
                    printf("   network address = 0x%02X", addr16);
                    printf("      IEEE address = %02X:%02X:%02X:%02X:%02X:%02X:%02X:%02X",
                            addr64[0], addr64[1], addr64[2], addr64[3],
                            addr64[4], addr64[5], addr64[6], addr64[7]);

                    zb_end_dev_info_get_num_of_ep((target_list)[i], &num_of_ep);
                    printf("   number of end-points = 0x%04X", num_of_ep);

                    zb_end_dev_info_get_ep_list((target_list)[i], &ep_list);
                    printf("      ");

                    if (ep_list) {
                            for (j = 0; j < num_of_ep; j++)
                                    printf("%04x ", ep_list[j]);
                            printf("\n");

                            free(ep_list);
                            ep_list = NULL;
                    }
            }

            return ret;
    }

    static int run_select_device(MManager *mm, struct menu_data *menu)
    {
            int i;
            int selected = (int)strtol(data_choose_target, NULL, 10);
            zb_nwk_addr addr16;

            /* Apply manual address first */
            if (strlen(data_dest_addr16) > 0) {
                    dest_addr16 = (unsigned short)strtol(data_dest_addr16, NULL, 16);
                    printf("  network addr [0x%04X] selected.", dest_addr16);
                    memset(data_dest_addr16, '\0', MENU_DATA_SIZE + 1);
                    return RET_SUCCESS;
            }

            if (NULL == target_list) {
                    printf("Please select device list first !");
                    return RET_FAILURE;
            }

            if (selected <= 0) {
                    printf("Please input valid device index !");
                    return RET_FAILURE;
            }

            for (i = 0; i < target_list_count && target_list; i++) {
                    if (selected == (i+1)) {
                            zb_end_dev_info_get_network_address(target_list[i], &addr16);
                            zb_end_dev_info_get_ieee_address((target_list)[i], dest_addr64);
                            dest_addr16 = addr16;
                            printf("  network addr [0x%04X] selected.", dest_addr16);
                            printf("  ieee address = %02X:%02X:%02X:%02X:%02X:%02X:%02X:%02X",
                                    dest_addr64[0], dest_addr64[1], dest_addr64[2], dest_addr64[3],
                                    dest_addr64[4], dest_addr64[5], dest_addr64[6], dest_addr64[7]);
                            return RET_SUCCESS;
                    }
            }

            printf("  Index [%d] was not found from end device list", selected);

            return RET_FAILURE;
    }
   ```

## Related Information
- Dependencies
  - Tizen 5.0 and Higher for Tizen IoT

- Related Info
  - http://www.zigbee.org/
  - http://www.zigbee.org/download/standards-zigbee-specification/
  - http://www.zigbee.org/zigbee-for-developers/applicationstandards/zigbeehomeautomation/
  - https://wiki.tizen.org/Tizen_ZigbeeFW_On_ARTIK
