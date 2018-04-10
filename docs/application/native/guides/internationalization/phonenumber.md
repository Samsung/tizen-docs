# Phone Number Management


Tizen enables you to parse and format phone numbers. The Phonenumber utils APIs are implemented with the libphonenumber open source library.

The main features of the Phonenumber utils API include:

- Retrieving the location information

  You can [get the location](#get) based on the phone number, region, and language using the `phone_number_get_location_from_number()` function. If the function cannot provide the location with the passed language, it uses English.

- Formatting the phone number

  You can [format the phone number string](#format) based on the region using the dash ("-") and space (" ") characters using the `phone_number_get_formatted_number()` function.

- Normalizing the phone number

  You can [normalize the phone number](#normalise) using the `phone_number_get_normalized_number()` function.

## Prerequisites

To enable your application to use the phonenumber utils functionality:

1. To use the functions and data types of the Phonenumber utils API (in [mobile](../../api/mobile/latest/group__CAPI__TELEPHONY__PHONE__NUMBER__UTILS__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__TELEPHONY__PHONE__NUMBER__UTILS__MODULE.html) applications), include the `<phone_number.h>` header file in your application:

   ```
   #include <phone_number.h>
   ```

   To ensure that a Phonenumber utils function has been executed properly, make sure that the return is equal to `PHONE_NUMBER_ERROR_NONE`.

2. To connect to the phonenumber utils service to access the service features, use the `phone_number_connect()` function:

   ```
   int error_code;
   error_code = phone_number_connect();
   ```

   When the service is no longer needed, disconnect from it using the `phone_number_disconnect()` function:

   ```
   error_code = phone_number_disconnect();
   ```
<a name="get"></a>
## Getting the Location

To get the location from the phone number, use the `phone_number_get_location_from_number()` function:

```
int ret;
char *location = NULL;

ret = phone_number_get_location_from_number("0222550114", PHONE_NUMBER_REGION_REPUBLIC_OF_KOREA,
                                            PHONE_NUMBER_LANG_ENGLISH, &location);
if (PHONE_NUMBER_ERROR_NONE == ret) {
    /* Use location */
    /* location – "Seoul" */
    dlog_print(DLOG_DEBUG, LOG_TAG, "location=%s", location);
}
free(location);
```

<a name="format"></a>
## Formatting the Number

To format the phone number to use region-specific separators, use the `phone_number_get_formatted_number()` function:

```
int ret;
char *formatted_number = NULL;

ret = phone_number_get_formatted_number("0222550114", PHONE_NUMBER_REGION_REPUBLIC_OF_KOREA,
                                        &formatted_number);
if (PHONE_NUMBER_ERROR_NONE == ret) {
    /* Use formatted_number */
    /* formatted_number - "02-2255-0114" */
    dlog_print(DLOG_DEBUG, LOG_TAG, "formatted_number=%s", formatted_number);
}
free(formatted_number);
```

<a name="normalise"></a>
## Normalizing the Number

To normalize the phone number, use the `phone_number_get_normalized_number()` function:

```
int ret;
char *normalized_number = NULL;

ret = phone_number_get_normalized_number("0222550114", normalized_number);
if (PHONE_NUMBER_ERROR_NONE == ret) {
    /* Use normalized_number */
    /* normalized_number - "+821022550114" */
    dlog_print(DLOG_DEBUG, LOG_TAG, "normalized_number=%s", normalized_number);
}
free(normalized_number);
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
