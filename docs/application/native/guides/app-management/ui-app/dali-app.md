# DALi Applications


You can use the Dynamic Animation Library (DALi) 3D UI toolkit to create a high-performance, rich UI application. For 2D-based Tizen native applications, use the [Enlightenment Foundation Libraries (EFL) UI toolkit](../../ui/efl/index.md).

Dynamic Animation Library (DALi) internally defines a virtual 3D world (space) and maintains hierarchical objects in the 3D world. The hierarchical object tree is known as the [scene graph](http://en.wikipedia.org/wiki/Scene_graph).

A node in the scene graph can have several children but often only a single parent, with the effect of a parent applied to all its child nodes; an operation performed on a group automatically propagates its effect to all of its members. There are various types of nodes, such as image, text, and buttons.

## Basic Fundamentals

Before you start UI programming with DALi, you must familiarize yourself with the basic DALi fundamentals. DALi consists of the following modules:

- **DALi Core**

  This module provides core functionalities, such as scene graph-based rendering, animation, and event handling. It is a base module and forms the biggest part of DALi.

- **DALi Adaptor**

  This module is a platform adaptation layer. It initializes and sets up DALi appropriately and provides many platform-related services with its internal module, platform abstraction. Several signals can be connected to it to keep you informed when certain platform-related activities occur.

- **DALi Toolkit**

  This module provides UI components and various effects on top of the DALi core.

For more information on how to implement a 3D world using DALi, see [DALi Overview](../../ui/dali/index.md). It helps you to understand how to use DALi easily, while providing a Hello World example of constructing a virtual 3D world.

## Application Types

With the DALi UI, you can create the following application types:

- [Basic UI application](dali-basic-app.md)

  A basic UI application provides a DALi-based user interface which allows the user to interact with the application.

  The basic UI application is available for both mobile and wearable devices.

- [Watch application](dali-watch-app.md) **in wearable applications only**

  A watch application provides a watch face with the current time (updated every second) as its user interface. You can take advantage of various DALi features to create the watch face.

  The watch application is available for wearable devices only, and it is shown on the idle screen of the device. For low-powered wearable devices, the watch application supports a special ambient mode. The ambient mode reduces power consumption by showing a limited UI and updating the time on the screen only once per minute.


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
