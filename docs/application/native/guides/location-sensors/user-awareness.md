# User Awareness
The user awareness API provides functions to detect user presence and location based on multiple sensors.

The main features of the user awareness include:
- Location detection
  
  Check who owns the detected device. Location detection basically find the user location and distance.
- Presence/absence detection
  
  Mainly, the PRESENCE / ABSENCE is divided into a technique for detecting a device, a technique for detecting the presence of a user, and a technique for distinguishing whether a specific user exists.
  
  ## Prerequisites
  To use the functions and data types of the user awareness API, include the <user-awareness.h> header file in your application:
  
  ```#include <user-awareness.h>```
  
  ## Start presence detection
  
  To start the presence detection:
  1. Create a user presence/absence monitor handle using the ```ua_monitor_create()``` API before you use the user awareness features.

  ```
  ua_monitor_h g_ua_mon_h;
  ua_monitor_create(&ua_mon_h);
  ```
  > The user awareness framework is not thread-safe and depends on the main loop. Implement the presence detection within the main loop, and do not use it in a thread.
  2. Starts the user presence detection using the ```ua_monitor_start_presence_detection()``` API. This call is asynchronous and only initiates the process of starting the user presence detection. Once the presence detection is started, the registered callbacks are invoked when their corresponding events take place. To know when the user presence is detected, use the ```ua_presence_detected_cb()``` function.
  ```
  ua_monitor_start_presence_detection()
  ``` 
