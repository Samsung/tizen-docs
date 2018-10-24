# DALi Overview


Dynamic Animation Library (DALi) internally defines a virtual 3D world (space) and maintains hierarchical objects in the 3D world. The hierarchical object tree is known as the [scene graph](http://en.wikipedia.org/wiki/Scene_graph). A node in the scene graph can have several children but often only a single parent, with the effect of a parent applied to all its child nodes; an operation performed on a group automatically propagates its effect to all of its members.

There are various types of nodes, such as image, text, and buttons.

## DALi Fundamentals

Before starting UI programming with DALi, familiarize yourself with the basic concepts.

### Actor and Stage

Actor is the primary object with which DALi applications interact. Actors are effective nodes that receive input (such as touch events), and act as a container for drawable elements (which are also nodes) and other actors.
A DALi application uses a hierarchy of actor objects to position visible content. An actor inherits a position relative to its parent, and can be moved relative to this point. UI components can be built by combining multiple actors.

Stage is a top-level node of the scene graph used for displaying a tree of actors. An actor must be added to the stage to display its contents.

The following example shows how to connect a new actor to the stage:
   ```
   Actor actor = Actor::New();
   Stage::GetCurrent().Add( actor );
   ```

### Signal and Slot

In DALi applications, a [signal and slot](https://en.wikipedia.org/wiki/Signals_and_slots) mechanism is used for communication between objects. This means that, in the DALi event system, objects can send signals containing event information, which can be received by other objects using special functions known as slots.

Signal events are emitted when a certain action or event occurs. The application can connect to these signals. Standard C-style functions can be used to connect to these signals if no local data needs to be accessed, otherwise a class function can also be connected.

Applications can manually disconnect from signals when required. However, DALi also provides safe signal disconnection. This means that when the connecting object is deleted, the signal is automatically disconnected.

### Coordinate System

DALi uses a left-handed coordinate system with the origin at the top-left corner, with positive X to right, positive Y going downwards, and positive Z going outside the screen with the default camera. This is convenient when creating 2D views.

The stage has a 2D size that matches the size of the application window. The default unit 1 is 1 pixel with the default camera.

**Figure: DALi coordinate system**

![DALi coordinate system](./media/actor_coordinates.png)

### Camera

DALi has a concept of a camera to display its virtual 3D world to a 2D screen. There are 2 ways of using the camera in DALi:

- For **2D** applications, you do not need to care about the camera at all. The default camera is already best suited for 2D applications (configured to have the origin of the coordinate system at the top-left corner of the screen, and unit 1 as 1 pixel of the screen). This is a typical way.
- For **3D** applications, you can change the view by manipulating the camera. You can translate or rotate the camera in this case. Note that the top-left corner of the screen and unit 1 no longer are (0,0,0) and 1 pixel after manipulating the camera.

### DALi Modules

DALi consists of the following modules:

- **DALi Core**

  This module provides core functionalities, such as scene graph-based rendering, animation, and event handling. It is a base module and forms the biggest part of DALi.

- **DALi Adaptor**

  This module is a platform adaptation layer. It initializes and sets up DALi appropriately and provides many platform-related services with its internal module, platform abstraction. Several signals can be connected to it to keep you informed when certain platform-related activities occur.

- **DALi Toolkit**

  This module provides UI components and various effects on top of the DALi core.

**Figure: Layer diagram for DALi modules**

![Layer diagram for DALi modules](./media/dali_modules.png)

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
