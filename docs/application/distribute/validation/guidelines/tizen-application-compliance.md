# Tizen Application Compliance


1. Namespace
   1. Application should include a namespace, such as: <company>; <application>.
   2. Application must not overwrite the Tizen API namespaces.
   
   
2. Application packaging and SDK use
   1. Application that is not packaged using Tizen SDK will be rejected.
   2. Application that does not use the Tizen SDK will be rejected
   
   
3. Privileges
   1. Application that uses a method of privilege that is not specified in the manifest file will be rejected.
   2. Application that uses system privilege level without permission will be rejected.
   3. Application that uses programming interface embedded in the official SDK but not specified as official Tizen API's shall be rejected.
   4. Application that does not use any method of privilege defined in the manifest file will be rejected.
   
   
4. Interrupt Handling, Messaging and Calls
   1. Application that sends and/or receives SMS or MMS messages should send the messages successfully.
   2. Users should be able to accept an incoming phone call while the application is running. Furthermore, it should resume from the same point, or at a reasonable re-starting point, when the call is ended.
   3. Application should not block the user from making emergency calls on a cellular network.
   4. Application should not crash or cause malfunctions due to system performance while the application is running (e.g. alarm, SMS/MMS, email, receiving a call).
   
   
5. Network Usage
   1. Application should not excessively use network capacity or bandwidth.
   2. Application should handle the network connection being invalid/unusable (e.g. data connection/APN not properly set up or invalid for current carrier) or the device being switched into offline/flight mode.
   3. Users should be notified by a message if network delays or connection errors occur.
   
   
6. Security
   1. Application that contains viruses, spyware, Trojan, malicious or harmful code which could damage, destroy, or adversely affect other software, firmware, hardware, data, systems, services or networks will be rejected.
   2. Application that uses advertising networks that promote malware will be rejected.