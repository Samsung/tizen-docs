# Web View Settings

You can set Web view properties.

This feature is optional.

The main features of the Web Setting API include the following:

- Setting user agents

  You can [set a custom user agent string](#set-a-user-agent-for-a-running-application) for the running Web application.

- Deleting cookies

  You can [delete all cookies](#delete-web-view-cookies) set for the running Web application.

## Set a user agent for a running application

Use the `setUserAgentString()` method to set a Web view user agent string:

```
function successCallback() {
    console.log('The requested user agent string has just been set successfully.' + navigator.userAgent);
}

/* Set a user agent string */
var userAgent = 'CUSTOM_USER_AGENT_STRING';
tizen.websetting.setUserAgentString(userAgent, successCallback);
```

## Delete Web view cookies

Use the `removeAllCookies()` method to delete all the Web view cookies:

```
function CookiesRemovedSuccessCallback() {
    console.log('The cookies saved for your application have just been removed.');
}

tizen.websetting.removeAllCookies(CookiesRemovedSuccessCallback);
```

## Related information
* Dependencies
  - Tizen 2.4 and Higher
