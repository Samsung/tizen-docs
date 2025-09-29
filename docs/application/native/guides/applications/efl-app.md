# EFL Applications

You can use the Enlightenment Foundation Libraries (EFL) to create a 2D-based Tizen native application. However, EFL supports 2.5D, 3D effects, and 3D objects as well.

EFL is a collection of libraries that are independent or can build on top of each other. It provides useful features that complement an existing OS environment, rather than wrapping or abstracting it. This means that EFL expects you to use other system libraries and APIs in conjunction with EFL libraries to provide a complete working application or library - using EFL as a set of convenient pre-made libraries to accomplish a whole host of complex or tedious tasks.

## Basic Fundamentals

Before you start UI programming with EFL, you must familiarize yourself with the basic EFL fundamentals. EFL consists of the following main libraries:

- **Elementary**

  Elementary provides all the functions you need to create a window, create simple and complex layouts, manage the life-cycle of a view, and add UI components.

- **Edje**

  Edje provides a powerful theme library for your application. You can also use Edje to create your own objects and use them in your application, or even extend the default theme.

- **Ecore**

  Ecore manages the main loop of your application. The main loop is where events are handled, and where you interact with the user through the callback mechanism.

- **Evas**

  Evas is the canvas engine responsible for managing the drawing of your content. All graphical objects that you create are Evas objects.

- **Eina**

  Eina is a toolbox that implements an API for data types in an efficient way. It contains all the functions needed to create lists and hashes, manage shared strings, open shared libraries, and manage errors and memory pools.

For more information on how to get started with EFL programming, see [Getting Started with EFL UI Programming](../ui/efl/getting-started.md). It helps you to understand how EFL works, and how you can create a simple EFL application with basic features.

## Application Types

With the EFL UI, you can create the following application types:

- [Basic UI application](efl-ui-app.md)

  A basic UI application provides an EFL-based user interface that allows the user to interact with the application.

  The basic UI application is available for both mobile and wearable devices.

- [Widget application](widget-app.md)

  A widget application (or widget) is a specialized application that provides the user a quick view of specific information from the parent application. In addition, the widget allows the user to access certain features without launching the parent application. Combined with the parent application, your widget can have various features to increase the usability of your application.

  The widget application is available for both mobile and wearable devices.

## Related Information
- Dependencies
  - Since Tizen 2.4
- API References
  - [UI Applications](../../api/common/latest/group__EFL.html)
  - [EFL](../../api/common/latest/group__EFL.html)
