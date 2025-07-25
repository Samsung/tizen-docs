# User Interface

The user interface features introduce how you can create a visual outlook for the UI application to ensure the best possible user experience.

The UI framework is a universal, reusable software environment that provides the essential building blocks as part of the Tizen platform to facilitate the development of Tizen native applications. The framework provides the window, UI components, and scene-based graphic rendering architecture needed to manage your application user interface.

In addition, the framework provides animations and effects needed to make your application more fresh and vivid. With event handling and using the main loop to interact with the user and system, it provides various other features, such as scalability and font setting. The Tizen platform provides the EFL UI toolkit frameworks and the Tizen window system shell for creating immersive user interfaces.

You can use the following user interface features in your native applications:

- [Enlightenment Foundation Libraries (EFL)](efl/index.md)

  You can use the EFL UI toolkit if you are creating a 2D-based Tizen native application. However, EFL supports 2.5D and 3D effects and 3D objects as well. EFL provides streamlined graphic core libraries you need to create powerful applications. EFL needs relatively low memory but provides high performance, and supports a retained mode graphics system and user-centric features, such as themes, 2D/3D effects, and accessibility. In addition, EFL supports various resolutions with the same layout, fast and small file systems, a variety of programming language bindings, and a separate UI and logic.

- [Tizen Window System Shell (TZSH)](tizen-ws-shell/index.md)

  You can use the TZSH to manipulate the windows of the system graphical user interfaces (GUI) services such as the quickpanel. It allows you to control the windows of system GUI services and get notifications about the state changes of each window within an application. Not all applications require to use the TZSH's functionalities. However, in some cases, certain applications may require to perform manipulation of system GUI service's window.

## Related Information
- Dependencies
  - Since Tizen 2.4
- API References
  - [UI](../../api/common/latest/group__CAPI__UI__FRAMEWORK.html)
