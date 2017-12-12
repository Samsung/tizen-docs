# Web View Settings

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 3.0 and Higher for Wearable

You can set Web view properties.

This feature is supported in mobile and TV applications only.

The main features of the Web Setting API include:

- Setting user agents

  You can [set a custom user agent string](./device/web-view-w.md#set) for the running Web application.

- Deleting cookies

  You can [delete all cookies](./device/web-view-w.md#delete) set for the running Web application.

## Setting a User Agent for a Running Application

Use the `setUserAgentString()` method to set a Web view user agent string:

```
function successCallback() {
    console.log('The requested user agent string has just been set successfully.' + navigator.userAgent);
}

/* Set a user agent string */
var userAgent = 'CUSTOM_USER_AGENT_STRING';
tizen.websetting.setUserAgentString(userAgent, successCallback);
```

## Deleting Web View Cookies

Use the `removeAllCookies()` method to delete all the Web view cookies:

```
function CookiesRemovedSuccessCallback() {
    console.log('The cookies saved for your application have just been removed.');
}

tizen.websetting.removeAllCookies(CookiesRemovedSuccessCallback);
```