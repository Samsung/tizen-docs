Phone Number Management
=======================

## Dependencies

- Tizen 4.0 and Higher

You can parse, format, and normalize phone numbers. The
Tizen.PhonenumberUtils namespace is implemented with the libphonenumber
open source library.

The main features of the Tizen.PhonenumberUtils namespace include:

-   Retrieving location information

    You can [get the location](#getting) based on the phone number,
    region, and language.

- Formatting phone numbers

    You can [format the phone number string based on the
    region](#formatting)using the dash ("-") and space (" ") characters.

- Normalizing phone numbers

    You can [normalize the phone number](#normalizing).


Prerequisites
-------------

To enable your application to use the phone number management
functionality:

1.  To use the `GetNormalizedNumber()` method of the
    [Tizen.PhonenumberUtils.PhonenumberUtils](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1PhonenumberUtils_1_1PhonenumberUtils.html)
    class, the application has to request permission by adding the
    following privilege to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <privilege>http://tizen.org/privilege/telephony</privilege>
    </privileges>
    ```

2. To use the methods and properties of the
    [Tizen.PhonenumberUtils](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1PhonenumberUtils.html)
    namespace, include it in your application:

    ``` {.prettyprint}
    using Tizen.PhonenumberUtils;
    ```


Retrieving Location Information <a id="getting"></a>
-------------------------------

To retrieve the location from a phone number, use the
`GetLocationFromNumber()` method of the
[Tizen.PhonenumberUtils.PhonenumberUtils](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1PhonenumberUtils_1_1PhonenumberUtils.html)
class. Provide the region of the phone number and the language of the
returned location string as parameters, using the values defined in the
[Tizen.PhonenumberUtils.Region](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1PhonenumberUtils.html#acfcfcabb066feb7d4a2ab2da337e745b)
and
[Tizen.PhonenumberUtils.Language](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1PhonenumberUtils.html#ab159dc3447ec930e04ed1016cf6e80a6)
enumerations, respectively.

``` {.prettyprint}
var utils = new PhonenumberUtils();
var location = utils.GetLocationFromNumber("0222550114", Region.Korea, Language.English);
/// Method returns the location string "Seoul"
```


Formatting Phone Numbers <a id="formatting"></a>
------------------------

To format a phone number to use region-specific separators, use the
`GetFormattedNumber()` method of the
[Tizen.PhonenumberUtils.PhonenumberUtils](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1PhonenumberUtils_1_1PhonenumberUtils.html)
class, which takes the region parameter as a value of the
[Tizen.PhonenumberUtils.Region](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1PhonenumberUtils.html#acfcfcabb066feb7d4a2ab2da337e745b)
enumeration:

``` {.prettyprint}
var utils = new PhonenumberUtils();
var formattedNumber = utils.GetFormattedNumber("0222550114", Region.Korea);
/// Method returns the formatted number string "02-2255-0114"
```


Normalizing Phone Numbers <a id="normalizing"></a>
-------------------------

To retrieve a phone number in a normalized format, use the
`GetNormalizedNumber()` method of the
[Tizen.PhonenumberUtils.PhonenumberUtils](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1PhonenumberUtils_1_1PhonenumberUtils.html)
class:

``` {.prettyprint}
var utils = new PhonenumberUtils();
var normalizedNumber = utils.GetNormalizedNumber("0222550114");
/// Method returns the normalized number string "+821022550114"
```
