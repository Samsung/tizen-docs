# STC


STC means Smart Traffic Control. It provides extensible packet-level control services, including per-app data usage, total data quota, and background app's data saving. STC Library provides APIs fulfilling below mentioned features for application development.

This feature is supported in mobile, tv and wearable profile.

The main features of the STC API include:

- Retrieve Data Usage For System

  You can [retrieve network data consumed by system](#retrieve-data-usage-for-system).

- Retrieve Data Usage For Applications

  You can [retrieve network data consumed by applications](#retrieve-data-usage-for-applications).


> **Note**  
> You can test the STC functionality on a target device only. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the STC API:

1. To use the [STC](../../api/mobile/latest/group__CAPI__NETWORK__STC__MODULE.html) API, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
   </privileges>
   ```

2. To use the functions and data types of the STC API, include the <stc.h> header file in your application:

   ```
   #include <stc.h>
   ```

3. Call the `stc_initialize()` function to initialize library:

    ```
    stc_initialize();
    ```

4. Call the `stc_deinitialize()` function to deinitialize library before quiting:

   ```
   stc_deinitialize();
   ```

## Retrieve Data Usage For System

To retrieve statistics about total network data consumed by system:

1. Define a callback function for processing data usage results

   ```
   stc_callback_ret_e __process_total_stats_cb(stc_error_e result,
                                            stc_stats_info_h info,
                                            void *user_data)
   {
      if (result != STC_ERROR_NONE) {
        printf("Error[%d] received in total stats info\n", result);
        return STC_CALLBACK_CANCEL;
      }

      /* Do the processing on received data (stc_stats_info_h info) */

      return STC_CALLBACK_CONTINUE;
   }
   ```

2. Create rule for retrieveing data usage:

   This rule will be passed as a function parameter in `stc_get_total_stats()` API call.

   ```
   int __create_stats_rule(stc_h stc, stc_stats_rule_h *rule)
   {
     int ret = STC_ERROR_NONE;

     ret = stc_stats_rule_create(stc, rule)
     if (ret != STC_ERROR_NONE) {
         printf("Failed to create stats rule\n");
         return ret;
     }

     /* Set stats rule using stc_stats_rule_set_* APIs */
     ret = stc_stats_rule_set_iface_type(rule, iface_type);
     if (ret != STC_ERROR_NONE)
         printf("Failed to set rule for time period\n");

     return ret;
   }
   ```

3. Call `stc_get_total_stats()` API.

   ```
   int get_total_stats(void)
   {
     int ret = STC_ERROR_NONE;
     stc_h stc;
     stc_stats_rule_h stats_rule_h;

     /* initialize library */
     ret = stc_initialize(&stc);
     if (ret != STC_ERROR_NONE) {
         printf("Initialization failed\n");
         return ret;
     }

     /* create stats rule handle */
     if (__create_stats_rule(stc, &stats_rule) != STC_ERROR_NONE) {
         stc_deinitialize(stc);
         printf("stats rule creation failed\n");
         return ret;
     }

     /* retrieve total stats */
     ret = stc_get_total_stats(stc, stats_rule, __process_total_stats_cb, NULL);
     if (ret == STC_ERROR_NONE)
         printf("Success to request stats total info\n");
     else
         printf("Fail to request stats total info [%d]\n", ret);

     /* destroy stats rule handle */
     ret = stc_stats_rule_destroy(stats_rule);
     if (ret != STC_ERROR_NONE) {
         stc_deinitialize(stc);
         printf("Failed to destroy stats rule.\n");
         return ret;
     }

      return ret;
   }
   ```

## Retrieve Data Usage For Applications

To retrieve statistics about total network data consumed by applications:

1. Define a callback function for processing foreach data usage results:

   ```
   stc_callback_ret_e __process_foreach_stats_cb(stc_error_e result,
                                              stc_stats_info_h info,
                                              void *user_data)
   {
     if (result != STC_ERROR_NONE) {
         printf("Error[%d] received in total stats info\n", result);
         return STC_CALLBACK_CANCEL;
     }

     /* Do the processing on received data (stc_stats_info_h info) */

     return STC_CALLBACK_CONTINUE;
   }
   ```

2. Create rule for retrieveing data usage for applications:

   This rule will be passed as a function parameter in `stc_foreach_stats()` API call.

   ```
   int __create_stats_rule(stc_h stc, stc_stats_rule_h *rule)
   {
     int ret = STC_ERROR_NONE;

     ret = stc_stats_rule_create(stc, rule)
     if (ret != STC_ERROR_NONE) {
         printf("Failed to create stats rule\n");
         return ret;
     }

     /* Set stats rule using stc_stats_rule_set_* APIs */
     ret = stc_stats_rule_set_app_id(rule, app_id);
     if (ret != STC_ERROR_NONE)
         printf("Failed to set rule for app_id [%s]\n", app_id);

     return ret;
   }
   ```

3. Call `stc_foreach_stats()` API.

   ```
   int get_foreach_stats(void)
   {
     int ret = STC_ERROR_NONE;
     stc_h stc;
     stc_stats_rule_h stats_rule_h;

     /* initialize library */
     ret = stc_initialize(&stc);
     if (ret != STC_ERROR_NONE) {
         printf("Initialization failed\n");
         return ret;
     }

     /* create stats rule handle */
     if (__create_stats_rule(stc, stats_rule) != STC_ERROR_NONE) {
         stc_deinitialize(stc);
         printf("stats rule creation failed\n");
         return ret;
      }

     /* retrieve foreach stats */
     ret = stc_foreach_stats(stc, stats_rule, __process_total_stats_cb, NULL);
     if (ret == STC_ERROR_NONE)
         printf("Success to request stats total info\n");
     else
         printf("Fail to request stats total info [%d]\n", ret);

     /* destroy stats rule handle */
     ret = stc_stats_rule_destroy(stats_rule);
     if (ret != STC_ERROR_NONE) {
         stc_deinitialize(stc);
         printf("Failed to destroy stats rule.\n");
         return ret;
     }

     return ret;
   }
   ```

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
