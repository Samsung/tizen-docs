# Globalization

You can get information about the user's locale, language, and time zone. You can also convert strings, numbers, and dates according to the user locale.

The Globalization API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Globalization API include:

- Obtaining locale information

  You can obtain the following locale information:

  - [Get the user's current language](#retrieving-the-current-language) as the BCP 47 identifier (such as en-US).
  - [Get the user's current locale](#retrieving-the-current-locale) as the BCP 47 identifier (such as en-US).
  - [Get the pattern string to format and parse currency](#retrieving-the-currency-details) and the ISO 4217 currency code.
  - [Get the names of months and names of the days of the week](#retrieving-the-names-of-the-months-and-days-of-the-week).
  - [Get the pattern string to format and parse dates](#retrieving-the-date-format-details).
  - [Get the first day of the week](#retrieving-the-first-day-of-the-week).
  - [Get the pattern string to format and parse numbers](#retrieving-the-number-format-details).
  - [Determine whether the Daylight Saving Time is in effect](#retrieving-the-daylight-saving-time-status) for a given date.

- Converting data

  You can [convert strings, numbers, and dates](#performing-conversions) according to the user locale.

All Globalization functions are accessible by the `navigator.globalization` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/globalization.html#GlobalizationManager), [wearable](../../api/latest/device_api/wearable/tizen/cordova/globalization.html#GlobalizationManager), and [TV](../../api/latest/device_api/tv/tizen/cordova/globalization.html#GlobalizationManager) applications).

## Prerequisites

To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova features now available');
}
```

## Retrieving the Current Language

To get the current BCP 47 language identifier:

```
navigator.globalization.getPreferredLanguage(function(language) {
    console.log('Language: ' + language.value);
}, function() {
    console.log('Error getting language.');
});
```

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language,
   this outputs a similar text as below
*/

Language: en-US
```

## Retrieving the Current Locale

To get the current BCP 47 locale identifier:

```
navigator.globalization.getLocaleName(function(locale) {
    console.log('Locale: ' + locale.value);
}, function() {
    console.log('Error getting locale.');
});
```

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language,
   this outputs a similar text as below
*/

Locale: en-US
```

## Retrieving the Currency Details

To obtain the following information about the currency:

- Currency pattern to format and parse the currency values

  The patterns follow the Unicode Technical Standard #35.

- ISO 4217 currency code

- Number of fractional digits

- Rounding increment

- Decimal symbol

- Grouping symbol

```
navigator.globalization.getCurrencyPattern('USD', function(pattern) {
    console.log('pattern: ' + pattern.pattern);
    console.log('code: ' + pattern.code);
    console.log('fraction: ' + pattern.fraction);
    console.log('rounding: ' + pattern.rounding);
    console.log('decimal: ' + pattern.decimal);
    console.log('grouping: ' + pattern.grouping);
}, function() {
    console.log('Error getting pattern.');
});
```

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language and
   the selected currency is United States Dollars,
   this outputs a similar text as below
*/

pattern: $#,##0.##;($#,##0.##)
code: USD
fraction: 2
rounding: 0
decimal: .
grouping: ,
```

## Retrieving the Names of the Months and Days of the Week

To obtain the names of months:

```
navigator.globalization.getDateNames(function(names) {
    for (var i = 0; i < names.value.length; i++) {
        console.log('month: ' + names.value[i]);
    }
}, function() {
    console.log('Error getting names.');
}, {type: 'wide', item: 'months'});
```

In the above example, the third parameter is `{type: 'wide', item: 'months'}`, and the names of months are obtained. To obtain the names of weekdays, pass `{type: 'wide', item: 'days'}` as the third parameter.

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language,
   this outputs a similar text as below
*/

month: January
month: February
month: March
month: April
month: May
month: June
month: July
month: August
month: September
month: October
month: November
month: December
```

## Retrieving the Date Format Details

To get the following information about the date format:

- Date and time pattern that follows Unicode Technical Standard #35
- Abbreviated name of the time zone
- Current difference in seconds between the user's time zone and coordinated universal time
- Current daylight saving time offset in seconds between the user's non-daylight saving time zone and the user's daylight saving time zone.

```
function checkDatePattern() {
    navigator.globalization.getDatePattern(function(date) {
        console.log('Date pattern: ' + date.pattern);
    }, function() {
        console.log('Error getting pattern');
    }, {formatLength: 'short', selector: 'date and time'});
}

checkDatePattern();
```

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language and
   the selected currency is United States Dollars,
   this outputs a similar text as below
*/

Date pattern: M/d/yyyy h:mm a
```

## Retrieving the First Day of the Week

To obtain information on which day is the first day of the week (1 means Sunday):

```
navigator.globalization.getFirstDayOfWeek(function(day) {
    console.log('day: ' + day.value);
}, function() {
    console.log('Error getting first day of week.');
});
```

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language and
   the selected currency is United States Dollars,
   this outputs a similar text as below
*/

day: 1
```

## Retrieving the Number Format Details

To obtain the following information about the number format:

- Number pattern that follows Unicode Technical Standard #35

- Symbol to use when formatting and parsing, such as percent or currency symbol  

  It depends on the third parameter of the `getNumberPattern()` method, which can be `'decimal'`, `'percent'`, or `'currency'`.

- Number of fractional digits

- Rounding increment

- Symbol to use for positive numbers

- Symbol to use for negative numbers

- Decimal symbol

- Grouping symbol

```
navigator.globalization.getNumberPattern(function(pattern) {
    console.log('pattern: ' + pattern.pattern);
    console.log('symbol: ' + pattern.symbol);
    console.log('fraction: ' + pattern.fraction);
    console.log('rounding: ' + pattern.rounding);
    console.log('positive: ' + pattern.positive);
    console.log('negative: ' + pattern.negative);
    console.log('decimal: ' + pattern.decimal);
    console.log('grouping: ' + pattern.grouping);
}, function() {
    console.log('An error occurred.');
}, {type: 'decimal'});
```

The following output is shown in the system log:

```
/*
   When the browser is set to the en-US language and
   the selected currency is United States Dollars,
   this outputs a similar text as below
*/

pattern: #,##0.###
symbol: .
fraction: 0
rounding: 0
positive:
negative: -
decimal: .
grouping: ,
```

## Retrieving the Daylight Saving Time Status

To obtain information on whether the daylight saving time is in effect for a given date using the current time zone:

```
navigator.globalization.isDayLightSavingsTime(new Date(), function(date) {
    console.log('dst: ' + date.dst);
}, function() {
    console.log('Error getting the DST state.');
});
```

The following output is shown in the system log:

```
/*
   When the browser is set DST-enabled time zone and
   it is summer,
   this outputs a similar text as below
*/

dst: true
```

## Performing Conversions

To make conversions between strings, numbers, and dates according to the current locale:

- Date to string  

  To convert a date to a string according to the user's locale and time zone:

  ```
  /* This example uses the default conversion options */

  navigator.globalization.dateToString(new Date(), function(date) {
      console.log('Date: ' + date.value);
  }, function() {
      console.log('Error getting dateString.');
  }, {formatLength: 'short', selector: 'date and time'});
  ```

  The following output is shown in the system log:

  ```
  /*
     When the browser is set to the en-US language and
     the selected currency is United States Dollars,
     this outputs a similar text as below
  */

  Date: 9/25/2012 4:21PM
  ```

- String to date  

  To convert a date formatted as a DOMString according to the user's locale and time zone:

  ```
  navigator.globalization.stringToDate('9/25/2012', function(date) {
      console.log('month: ' + date.month + ', day: ' + date.day +
                  ', year: ' + date.year)
  }, function() {
      console.log('Error getting date.');
  }, {selector: 'date'});
  ```

  The following output is shown in the system log:

  ```
  /*
     When the browser is set to the en-US language and
     the selected currency is United States Dollars,
     this outputs a similar text as below
     Note that the month integer is 1 less than the string,
     as the month integer represents an array index
  */

  month: 8, day: 25, year: 2012
  ```

- Number to string  

  To return a number formatted as a string according to the user's preferences:

  ```
  navigator.globalization.numberToString(3.1415926, function(number) {
      console.log('decimal number: ' + number.value);
  }, function() {
      console.log('Error getting number.');
  }, {type: 'decimal'});

  navigator.globalization.numberToString(1000003, function(number) {
      console.log('big decimal number: ' + number.value);
  }, function() {
      console.log('Error getting number.');
  }, {type: 'decimal'});

  navigator.globalization.numberToString(0.3183099, function(number) {
      console.log('percentile: ' + number.value);
  }, function() {
      console.log('Error getting number.');
  }, {type: 'percent'});

  navigator.globalization.numberToString(1099.95, function(number) {
      console.log('currency: ' + number.value);
  }, function() {
      console.log('Error getting number');
  }, {type: 'currency'});
  ```

  The following output is shown in the system log:

  ```
  /*
     When the browser is set to the en-US language and
     the selected currency is United States Dollars,
     this outputs a similar text as below
  */

  decimal number: 3.142
  big decimal number: 1,000,003
  percentile: 32%
  currency: $1,099.95
  ```

- String to number  

  To parse a number formatted as a string according to the user's preferences and return the corresponding number:

  ```
  navigator.globalization.stringToNumber('1234.56', function(number) {
      console.log('number: ' + number.value);
  }, function() {
      console.log('Error getting number.');
  }, {type: 'decimal'});
  ```

  The following output is shown in the system log:

  ```
  /*
     When the browser is set to the en-US language and
     the selected currency is United States Dollars,
     this outputs a similar text as below
  */

  number: 1234.56
  ```

## Related Information
* Dependencies  
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
