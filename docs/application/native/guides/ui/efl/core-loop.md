# Core Loop and OS Interfacing

The Ecore library provides convenience functions, which allow you to manage the application processing mechanisms through:

- [Main loop](main-loop.md)

  Tizen applications developed with EFL use the EDA (Event-driven Architecture) pattern. In EDA, applications reiterate a sequence that checks input events, processes the events, and then displays the outputs. This sequence is handled by the main loop, which is the heart of any UI based on EDA.  

  Most applications start and end the main loop, which is used in special situations, such as propagation of events to UI components for handling and updating the application appearance and state. That guarantees the delivery of all events received from low-level input devices, and provides an accurate and speedy render event loop for synchronizing the application UI with events.  

  The Ecore library provides main loop abstraction with a clean and tiny event loop library. Applications mainly deal with file descriptor handling, event handling, and timer handling from the beginning of the main loop. In addition, Ecore provides several modules related to, for example, Audio, Cocoa, Connection, Drm, FrameBuffer, Input, IPC, Wayland, Win32, and X11 with convenient methods to communicate with underlying operating systems, such as Ubuntu, Windows&reg;, or macOS.

- [Threads](threads.md)

  The Ecore library provides concurrent processing mechanisms through Ecore threads. An Ecore thread is not a simple wrapper for standard POSIX threads, and it is not meant to be used to run parallel tasks throughout the entire duration of the application, especially when these tasks are performance-critical. Ecore manages tasks using a pool of threads based on system configuration, such as the number of processors the system has, and the maximum amount of concurrent threads set for the application.  

  There are 2 types of threads in Tizen applications:  
   - Main thread that contains the main loop
   - Worker threads that support concurrent processing. In parallel processing, applications must keep the UI updated while processing the data related to the UI.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
