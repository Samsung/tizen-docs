# Application Preferences

Preference management allows you to store and retrieve the application preferences. You can create, store, and retrieve all custom preferences needed by your application. Each preference has its own key and value, where the value can be a string, number, or a boolean value.

This feature is supported in mobile and wearable applications only.

> **Note**  
> The Preference API is a different feature than the [`preferences` attribute of the `config.xml` file](../../tutorials/process/setting-properties.md#preferences), which is used to set and retrieve name-value pairs using the Widget Interface API (in [mobile](../../api/latest/w3c_api/w3c_api_m.html#widget) and [wearable](../../api/latest/w3c_api/w3c_api_w.html#widget) applications).

The main preference features are:

- Setting up a preference

  You can [set up a preference](#setting-up-a-preference) with the `setValue()` method.  If the preference exists before setting up, its value is set. If the preference does not exist, it is created.

- Getting a preference value

  You can [retrieve a value of a single preference or values of all preferences](#getting-preference-values) using the `getValue()` or `getAll()` method. You can also [check whether a preference exists](#checking-whether-a-preference-exists) using the `exists()` method.

- Removing a preference

  You can [remove a preference](#removing-preferences) with the `remove()` and `removeAll()` functions. The first removes only 1 preference while the second removes them all.

- Monitoring preference value changes

  You can provide a listener method which is called every time a given preference's value changes. [Register the listener](#monitoring-preference-value-changes) with the `setChangeListener()` method. The provided listener is called with a preference key and its new value. If you want to remove the listener, use the `unsetChangeListener()` method.

## Setting up a Preference

To create a preference with a given key or to change a value of an existing one, use the `setValue()` method:

```
tizen.preference.setValue('key1', 'New value');
```

If the preference with the given key does not exist, it is created with the given value.  If the preference exists, only its new value is assigned.

## Getting Preference Values

To retrieve preference values:

- To get the value of a preference with a given key, use the `getValue()` method:

   ```
   var currentValue = tizen.preference.getValue('key1');   
   console.log('The current value of the preference key1 is: ' + currentValue);
   ```

  The value returned by the method can be a string, number, or boolean. If the preference with the given key does not exist, an exception is thrown.  

- To get all preferences, use the asynchronous `getAll()` method. Its callback gets an array of all preferences, where each row of the array consists of a field key and value.

  ```
  var successCB = function(preferences) {
      var i;
      for (i = 0; i < preferences.length; i++) {
          console.log('The preference - key: ' + preferences[i].key + ' value: ' + preferences[i].value);
      }
  };

  tizen.preference.getAll(successCB);
  ```

## Checking Whether a Preference Exists

To determine whether a preference with a given key exists, use the `exists()` method:

```
if (tizen.preference.exists('key1')) {
    console.log('Preference with the key key1 exists');
} else {
    console.log('Preference with the key key1 doesn't exist');
}
```

The method returns `true` if the preference exists and `false` if it does not.

## Removing Preferences

To remove preferences:

- To remove a single preference with the given key, use the `remove()` method:
   ```
   tizen.preference.remove('key1');
   ```
   If the preference with the given key does not exist, an exception is thrown.
- To remove all existing preferences, use the `removeAll()` method:
   ```
   tizen.preference.removeAll();
   ```

## Monitoring Preference Value Changes

To start and stop listening for value changes in a preference with a given key:

- To start listening, use the `setChangeListener()` method:

  ```
  var listener = function(data) {
      console.log('Preference with the key: ' + data.key + ' has a new value: ' + data.value);
  };

  tizen.preference.setChangeListener('key1', listener);
  ```

  The listener callback is called every time the value of the given preference changes. The callback parameter is an object that consists of the `key` and `value` fields.

- To stop listening, use the `unsetChangeListener()` method:

  ```
  var listener = function(data) {
      tizen.preference.unsetChangeListener(data.key);
  };

  tizen.preference.setChangeListener('key1', listener);
  ```


## Related Information
* Dependencies  
  - Tizen 3.0 and Higher for Mobile
  - Tizen 2.3.2 and Higher for Wearable
