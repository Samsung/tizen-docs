
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
