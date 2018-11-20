# EFL Applications

You can use the Enlightenment Foundation Libraries (EFL) to create a 2D-based Tizen native application. However, EFL supports 2.5D and 3D effects and 3D objects as well. For 3D-based Tizen native applications, you can use the [Dynamic Animation Library (DALi) UI toolkit](../../ui/dali/index.md) as well.

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

For more information on how to get started with EFL programming, see [Getting Started with EFL UI Programming](../../ui/efl/getting-started.md). It helps you to understand how EFL works, and how you can create a simple EFL application with basic features.

## Application Types

With the EFL UI, you can create the following application types:

- [Basic UI application](efl-ui-app.md)

  A basic UI application provides a DALi-based user interface which allows the user to interact with the application.

  The basic UI application is available for both mobile and wearable devices.

- [Watch application](watch-app.md) **in wearable applications only**

  A watch application provides a watch face with the current time (updated every second) as its user interface. You can take advantage of various DALi features to create the watch face.

  The watch application is available for wearable devices only, and it is shown on the idle screen of the device. For low-powered wearable devices, the watch application supports a special ambient mode. The ambient mode reduces power consumption by showing a limited UI and updating the time on the screen only once per minute.

- [Widget application](widget-app.md)

  A widget application (or widget) is a specialized application that provides the user a quick view of specific information from the parent application. In addition, the widget allows the user to access certain features without launching the parent application. Combined with the parent application, your widget can have various features to increase the usability of your application.

  The widget application is available for both mobile and wearable devices.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
