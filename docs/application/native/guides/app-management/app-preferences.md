# Application Preferences


You can manage application preferences by setting and getting them. You can also share stored preference data among applications in the same package.

## Prerequisites

To use the functions and data types of the Preference API (in [mobile](../../api/mobile/latest/group__CAPI__PREFERENCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__PREFERENCE__MODULE.html) applications), include the `<app_preference.h>` header file in your application:

```
#include <app_preference.h>
```

## Managing Application Preferences

To manage preferences:

- To store and retrieve simple type variables:

  To store a variable, you must create a key-value pair. Use the following functions to create a key-value pair for a specific simple type:

  - `preference_set_int()`
  - `preference_set_double()`
  - `preference_set_boolean()`

  Before storing or retrieving a variable, check whether it exists using the `preference_is_existing()` function.

  Use the following functions to retrieve a stored variable of a given simple type:

  - `preference_get_int()`
  - `preference_get_double()`
  - `preference_get_boolean()`

  ```
  const char *integer_key = "integer_key";
  int integer_value = 1;
  int integer_output;

  preference_set_int(integer_key, integer_value);

  preference_is_existing(integer_key, &existing);

  preference_get_int(integer_key, &integer_output);
  ```

- To store and retrieve string variables, use the following functions:

  - `preference_set_string()`
  - `preference_get_string()`

  Release the value returned by the get function using the `free()` function.

  ```
  const char *string_key = "string_key";
  const char *string_value = "Sample content";
  char *string_output;
  bool existing;

  preference_set_string(string_key, string_value);

  preference_is_existing(string_key, &existing);

  preference_get_string(string_key, &string_output);

  free(string_output);
  ```

- To track variables:

  You can set a different callback function to each variable. The callback function is invoked each time the variable is changed.

  ```
  int previous_value;

  preference_set_changed_cb(integer_key, preference_changed_cb_impl, &previous_value);
  ```

  Pass custom parameters to the callback function in the `user_data` field.

  ```
  void
  preference_changed_cb_impl(const char *key, void *user_data)
  {
      int ret = 0;
      int integer_output = 0;

      dlog_print(DLOG_DEBUG, LOG_TAG, "[preference_changed_cb_impl]\n");
      preference_get_int(key, &integer_output);

      dlog_print(DLOG_DEBUG, LOG_TAG, "Key: %s has changed its value to %d \n",
                 key, integer_output);
  }
  ```

  When no longer needed, unset the callback function based on a variable key:

  ```
  preference_unset_changed_cb(const char *key);
  ```

- To list all records, use the foreach function. The function calls a specific callback function for each key-value pair in the database. You can pass additional data to the function in the `user_data` field.

  If the callback function returns `false`, or if all the records have been opened, the foreach function ends.

   ```
   bool
   preference_foreach_item_cb(const char *key, void *user_data)
   {
       dlog_print(DLOG_DEBUG, LOG_TAG, "[preference_foreach_item_cb]\n");
       dlog_print(DLOG_DEBUG, LOG_TAG, "Key found: %s\n", key);

       return true;
   }

   preference_foreach_item(preference_foreach_item_cb, NULL);
   ```

- To delete records one by one, use a unique key. You can also delete all records for an application using the preference_remove_all() function.

  ```
  preference_remove(key);
  ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
