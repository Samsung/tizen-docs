# Hardware Input Handling

EFL does not depend on any specific hardware input methods, such as hardware keys, to generate back and home events, or rotary component parts to generate rotary events. Instead, these hardware input events are tightly related to the Tizen UX. As a result, EFL has created the EFL Extension library to support these common UX behaviors between the applications and hardware events.

EFL provides the following hardware event management features:

- [Managing Menu and Back Key Events](./key-events.md) **in mobile applications only**

  The Tizen platform offers the **Menu**, **Back**, and **Home** keys as physical hardware keys for mobile devices.  

  When the user presses the **Menu** or **Back** key, the key generates a signal with its key property. The Ecore library receives the signal and propagates it to the application layers as an event. The EFL Extension library consumes the events and handles the views of the application according to key properties.

- [Managing Rotary Events](./rotary-events.md) **in wearable applications only**

  The Tizen platform supports rotary events for user interaction on a wearable rotary device or sensor. The rotary device can rotate clockwise or counter-clockwise, and dispatch an event for each movement. EFL Extension manages the rotary events, which are generated from rotary components on wearable devices and delivered to application layers by defining an event callback or a handler function, and registering it.

- [Grabbing Hardware Key Events](./key-grab.md)

  Normally, the hardware keys do only what they are designed to do, such as increase the volume or return to the previous screen. In some applications, you can assign special actions to hardware keys. For example, the volume key can be used to increase and decrease the size of the text. This is called key grabbing.

## Related Information
- Dependencies  
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
