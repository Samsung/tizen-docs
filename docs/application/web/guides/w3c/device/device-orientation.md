# DeviceOrientation Event Specification

You can detect device motion and provide interaction between the user and device based on the motion.

This feature is supported in mobile and wearable applications only.

The main orientation event features include:

- Detecting rotation

  You can use the [deviceorientation](http://www.w3.org/TR/2011/WD-orientation-event-20111201/#deviceorientation) event to [detect rotation data](#detecting-device-rotation) in order to rotate game characters or elements.

- Detecting acceleration

  You can [use rotation speed (acceleration of the device) information](#detecting-device-acceleration), including gravity, with the [devicemotion](http://www.w3.org/TR/2011/WD-orientation-event-20111201/#devicemotion) event. You can move game characters or elements, and capture acceleration values to add certain events.

## Detecting Device Rotation

Learning how to detect device rotation is a basic device motion handling skill:

1. Display the device rotation details on the screen:

   ```
   <h1>Device orientation tutorial</h1>
   <div>
      <p id="alpha"></p>
      <p id="beta"></p>
      <p id="gamma"></p>
   </div>

   <script>
   ```

   ```
       var alphaElem = document.getElementById('alpha');
       var betaElem = document.getElementById('beta');
       var gammaElem = document.getElementById('gamma');
   ```

2. To track changes in device rotation, subscribe to the [deviceorientation](http://www.w3.org/TR/2011/WD-orientation-event-20111201/#deviceorientation) event:

   ```
       window.addEventListener('deviceorientation', function(e) {
           alphaElem.innerHTML ='alpha value ' + Math.round(e.alpha);
           betaElem.innerHTML = 'beta value ' + Math.round(e.beta);
           gammaElem.innerHTML = 'gamma value ' + Math.round(e.gamma);
       }, true);
   ```

   ```
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [device_orientation.html](http://download.tizen.org/misc/examples/w3c_html5/device/device_orientation_event_specification)

## Detecting Device Acceleration

Learning how to detect device acceleration is a basic device motion handling skill:

1. Display the device acceleration details on the screen:

   ```
   <h1>device orientation tutorial</h1>
   <div>
      <p id="firElem"></p>
      <p id="secElem"></p>
      <p id="thirElem"></p>
   </div>

   <script>
   ```

   ```
       var firElem = document.getElementById('firElem');
       var secElem = document.getElementById('secElem');
       var thirElem = document.getElementById('thirElem');
   ```

2. To track changes in device acceleration, subscribe to the [devicemotion](http://www.w3.org/TR/2011/WD-orientation-event-20111201/#devicemotion) event:

   ```
       window.addEventListener('devicemotion', function(e) {
           /* Data for acceleration */
           firElem.innerHTML = 'acceleration value<br/><br/> ' +
                               '[ x value: ' + Math.round(e.acceleration.x) + ' ]<br/>' +
                               '[ y value: ' + Math.round(e.acceleration.y) + ' ]<br/>' +
                               '[ z value: ' + Math.round(e.acceleration.z) + ']';

           /* Data for acceleration, including gravity */
           secElem.innerHTML = 'accelerationIncludingGravity value<br/><br/> ' +
                               '[ x value: ' + Math.round(e.accelerationIncludingGravity.x) + ' ]<br/>' +
                               '[ y value: ' + Math.round(e.accelerationIncludingGravity.y) + ' ]<br/>' +
                               '[ z value: ' + Math.round(e.accelerationIncludingGravity.z) + ']';

           /* Data for rotation rate */
           thirElem.innerHTML = 'rotationRate value<br/><br/> ' +
                                '[ alpha value: ' + Math.round(e.rotationRate.alpha) + ' degree ]<br/>' +
                                '[ beta value: ' + Math.round(e.rotationRate.beta) + ' degree ]<br/>' +
                                '[ gamma value: ' + Math.round(e.rotationRate.gamma) + ' degree ]';
       }, true);
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [device_motion.html](http://download.tizen.org/misc/examples/w3c_html5/device/device_orientation_event_specification)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
