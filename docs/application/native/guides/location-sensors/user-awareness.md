# User Awareness
The user awareness API provides functions to detect user presence and location based on multiple sensors.

The main features of the user awareness include:
- Location detection
  
  Check who owns the detected device. Location detection basically find the user location (distance and direction).
- Presence/absence detection
  
  Mainly, the PRESENCE / ABSENCE is divided into a technique for detecting a device, a technique for detecting the presence of a user, and a technique for distinguishing whether a specific user exists.
  
 ## Prerequisites
  To use the functions and data types of the user awareness API, include the <user-awareness.h> header file in your application:
  
  ```#include <user-awareness.h>```
  
 ## Initialization of user awareness
  
  To start initialization of user awareness:
  1. The user awareness framework must be initialized using the ```ua_initialize()``` API before application use the user awareness features.
  ```
  ua_initialize();
  ```
  2. Create a user monitor handle using the ```ua_monitor_create()``` API.

  ```
  ua_monitor_h g_ua_mon_h;
  ua_monitor_create(&g_ua_mon_h);
  ```
  
  3. Add available sensors in the monitor handle using the ```ua_monitor_add_sensor()``` API and load sensor plugins.

  ```
  ua_monitor_add_sensor(g_ua_mon_h,BLE);
  ua_monitor_add_sensor(g_ua_mon_h,WIFI);
  ua_monitor_add_sensor(g_ua_mon_h,LIGHT);
  ua_monitor_add_sensor(g_ua_mon_h,MOTION);
  ua_monitor_add_sensor(g_ua_mon_h,UA_SENSOR_UWB);
  ua_monitor_add_sensor(g_ua_mon_h,UA_SENSOR_WIFI_LOCATION);
  ```
  
  
  > The user awareness framework is not thread-safe and depends on the main loop. Implement the detection logics within the main loop, and do not use it in a thread.
 ## Registration of service, user and device
 
 1. Create a service handle using the ```ua_service_create()``` API.
  ```
  char g_service_str[MENU_DATA_SIZE + 1] = { "ua.service.default" };
  ua_service_h g_service_h;
  
  ua_service_create(g_service_str, &g_service_h);
  ```
  2. Create a user handle using the ```ua_user_create()``` API and add in service.
  ```
  char user_account_str[] = {"default@default.com"};
  ua_user_h user_h;
  
  ua_user_create(user_account_str, &user_h);
  
  ua_user_h g_user_h;
  ua_service_add_user(g_service_h, g_user_h);
  ```
  3. Create a device handle using the ```ua_device_create()``` API and add in user.
  ```
  unsigned char device_type; 
  char *device_id_str;
  char *mac_addr_str;
  ua_device_h device_h;
  
  ua_device_create(device_type, mac_addr_str,device_id_str, &device_h);
  
  ua_device_h g_device_h; 
  ua_user_add_device(g_user_h, g_device_h, __device_added_cb, NULL);

  ```
 ## Starting the presence detection
  
  To start the presence detection:
  
  1. Starts the user presence detection using the ```ua_monitor_start_presence_detection()``` API. This call is asynchronous and only initiates the process of starting the user presence detection. Once the presence detection is started, the registered callbacks are invoked when their corresponding events take place. To know when the user presence is detected, use the ```ua_presence_detected_cb()``` function.
  ```
  ua_monitor_start_presence_detection(g_ua_mon_h, NULL, detection_mode, __presence_detected_cb, NULL);
  ```
  The ```__presence_detected_cb()``` function is a callback, which is called when the user presence is detected.
  
  2. Using the user presence detection consumes the system resources, so if the service is not used, stop the user presence detection using the ```ua_monitor_stop_presence_detection()``` API. Call the ```ua_monitor_start_presence_detection()``` API again if user presence detection is needed.
  ```
  ua_monitor_stop_presence_detection(g_ua_mon_h);
  ```
  3. At the end of application, destroy all used resources, such as the user monitor handle using the ```ua_monitor_destroy()``` API.
  ```
  ua_monitor_destroy(g_ua_mon_h);
  ```
## Starting the absence detection

To start the absence detection:
  
   1. Starts the user presence detection using the ```ua_monitor_start_absence_detection()``` API. This call is asynchronous and only initiates the process of starting the user absence detection. Once the absence detection is started, the registered callbacks are invoked when their corresponding events take place. To know when the user absence is detected, use the ```ua_absence_detected_cb()``` function.
  ```
  ua_monitor_start_absence_detection(g_ua_mon_h, NULL, detection_mode, __absence_detected_cb, NULL);
  ```
  The ```__absence_detected_cb()``` function is a callback, which is called when the user absence is detected.
  
   2. Using the user absence detection consumes the system resources, so if the service is not used, stop the user absence detection using the ```ua_monitor_stop_absence_detection()``` API. Call the ```ua_monitor_start_absence_detection()``` API again if user presence detection is needed.
  ```
  ua_monitor_stop_absence_detection(g_ua_mon_h);
  ```
  3. At the end of application, destroy all used resources, such as the user monitor handle using the ```ua_monitor_destroy()``` API.
  ```
  ua_monitor_destroy(g_ua_mon_h);
  ```
  
## Starting the location detection

To start the location detection:
## Related Information
- Dependencies
  - Tizen 6.5 and higher 
