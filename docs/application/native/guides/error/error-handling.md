# Error Handling


How to query error codes for a certain API function is determined by how the function returns error codes. In this sense, there are 2 kinds of native APIs in Tizen:

- APIs directly returning error codes

  All API functions which return error codes have the following section in their description:

  ```
  Returns:
      0 on success, otherwise a negative error value
  ```

  To see all of the available error values, see the Return values section in each API function description.

  For example:

  ```
  Return values:
      MESSAGES_ERROR_NONE /* Successful */
      MESSAGES_ERROR_INVALID_PARAMETER /* Invalid parameter */
      MESSAGES_ERROR_SERVER_NOT_READY /* Server is not ready */
      MESSAGES_ERROR_COMMUNICATION_WITH_SERVER_FAILED /* Server communication failed */
  ```

- APIs returning values (indirectly returning error codes)

  All API functions that return values have the following section in their description:

  ```
  Remarks:
  The specific error code can be obtained using the get_last_result() function. Error codes are described in Exception section.
  To see all of the available error values, please refer to the Exceptions section in each API function description.
  For example:

  Exceptions:
  BUNDLE_ERROR_NONE /* Success */
  BUNDLE_ERROR_OUT_OF_MEMORY /* Out of memory */
  ```

To obtain the error message for a specific error code, use the `get_error_message()` function to query the meaning of each error code. The pointer returned is a static variable; you must not free it.

For example:

```
char* errMsg;
location_manager_h location_handle;
int result = location_manager_create(LOCATION_METHOD_GPS, location_handle);

if (LOCATIONS_ERROR_NONE != result) {
    errMsg = get_error_message(result);
    dlog_print(DLOG_INFO, "MyTag", "%s", errMsg);
}
```

The `get_error_message()` function takes an error code as an input and returns its corresponding error messages, such as "Location service is not available".

Every error code in the Tizen native API is represented as an integer value.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
