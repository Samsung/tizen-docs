# Vibration

To provide tactile feedback to the user or to interact with the user even when the device volume is low, you can [make a Tizen device vibrate](#managing-vibrations). The vibration can provide a better user experience and improve the perception of your application.

This feature is supported in mobile and wearable applications only.

The vibration interface is implemented by all `Navigator` instances. With the `vibrate()` method parameters, you can define different vibration types:

- Continuous vibration for a given length of time

  The `time` parameter defines the vibration time in milliseconds.

- Vibration in a given pattern

  The `pattern` parameter defines a vibration pattern as a list of time entries. Odd entries represent the vibration time in milliseconds, and even entries represent still periods in milliseconds between the vibrations.

## Managing Vibrations

To enhance the user interaction with the device, learn to manage vibrations:

1. To launch a vibration for a given length of time, call the `vibrate()` method, which is implemented by all `Navigator` instances:

   ```
   <!DOCTYPE html>
   <html>
      <head>
         <meta charset="utf-8"/>
         <meta name="viewport"
               content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
         <title>Tizen Vibration API Example code</title>

         <script>
   ```
   ```
             function singleVibration() {
                 /* Vibrate for 2 seconds */
                 navigator.vibrate(2000);
             }
   ```

2. To launch a vibration that uses a pattern of vibration and still periods, define the pattern as the `vibrate()` method parameter:

   ```
             function patternVibration() {
                 /* Vibrate in a given pattern: 1 sec on, 1 sec off, 2 sec on, 2 sec off */
                 navigator.vibrate([1000, 1000, 2000, 2000, 1000]);
             }
   ```

3. To stop the vibration before it ends naturally, use the `vibrate()` method with `0` or `[]` as a parameter. The method call cancels all existing vibrations.

   ```
             function stopVibration() {
                 navigator.vibrate(0);
             }
   ```

4. Create the buttons used to manage the vibrations:

   ```
         </script>
      </head>

      <body>
         <header style="width: 100%; text-align: center;">
            <h1>Vibration API Example</h1>
         </header>

         <nav style="width: 100%; text-align: center;">
            <!--Button click calls singleVibration()-->
            <button onclick="singleVibration();"
                    style="width: 200px; height: 50px; margin-bottom: 10px">
               Single vibration
            </button>

            <!--Button click calls patternVibration()-->
            <button onclick="patternVibration();"
                    style="width: 200px; height: 50px; margin-bottom: 10px">
               Pattern vibration
            </button>

            <!--Button click calls stopVibration()-->
            <button onclick="stopVibration();"
                    style="width: 200px; height: 50px">
               Stop vibration
            </button>
         </nav>
      </body>
   </html>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [vibration_tutorial.html](http://download.tizen.org/misc/examples/w3c_html5/device/vibration_api)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
