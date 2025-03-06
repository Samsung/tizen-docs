# UI Applications


UI applications are Tizen native applications with a graphical user interface that run on the foreground. Since they have a UI, they allow the user to easily interact with them.

A Tizen native UI application is similar to a conventional Linux application, with some additional features optimized for mobile and wearable devices. The additional features have constraints, such as a relatively small screen size and lack of system resources compared to a larger system. For example, for power management reasons, the application can take actions to reduce usage when it finds out that it has its display window covered over by another application window. State change events are delivered to make it possible to detect these situations.

When creating a native UI application, you can use EFL UI frameworks:

- EFL

  The EFL application is based on the Enlightenment Foundation Library. With EFL and streamlined graphic core libraries, you can create powerful 2D-based Tizen native applications. EFL needs relatively low memory but provides high performance, and supports a retained mode graphics system and user-centric features, such as themes, 2D/3D effects, and accessibility. In addition, EFL supports various resolutions with the same layout, fast and small file systems, a variety of programming language bindings, and a separate UI and logic.

  For more information on the available application types with EFL, see [EFL Applications](efl-app.md).


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
- API Reference
  - [UI Applications](../../api/common/latest/group__CAPI__APPLICATION__MODULE.html)
