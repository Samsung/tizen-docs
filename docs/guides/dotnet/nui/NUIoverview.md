# NUI Overview
## Dependencies
-   Tizen 4.0 and Higher

NUI (Natural User Interface) is a C\# toolkit on top of the DALi (Dynamic Animation Library) graphics library, which is written in C++.

NUI is a rich GUI library for creating 2D or 3D applications. These applications are run on a range of Tizen devices, such as TVs and wearables. NUI is built on a multi-threaded architecture enabling realistic smooth animations. In addition, a range of optimization techniques are utilized to obtain low CPU and GPU usage, further increasing graphics performance.

NUI enables you to quickly create rich UI applications with realistic effects and animations, such as:

-   Image and video galleries
-   Music players
-   Homescreens and launch pads
-   Advanced watch faces for wearable devices

NUI offers the following main features:

-   Provides a UI consisting of hierarchical scene graph nodes.
-   Creates images and text.
-   Provides layers to aid in 2D UI layouting.
-   Allows automatic background loading of resources.
-   Provides an easy-to-use animation framework which hides the complexity of the underlying 3D math.
-   Provides keyboard, touch, and mouse handling.

<a name="concepts"></a>
## Key Concepts

To be able to use NUI in your applications, you must become familiar with the following NUI key concepts:

-   **Scene graph**: Tree data structure, consisting of a collection of nodes.
-   **Window**: Top level of the scene graph, used for displaying a tree of layers and views.
-   **View**: Primary object for interaction. Views are effectively nodes that receive input (such as touch events), and act as a container for drawable elements and other views. Views can display content, such as color shapes, images, and text.

    A NUI application uses a hierarchy of view objects to position visible content.

-   **Layer**: Layers provide a mechanism for overlaying groups of views on top of each other.

<a name="started"></a>
## Getting Started 

To get started with NUI development:

-   [Set up the NUI development environment](setup-ubuntu.md).
-   [Study a "Hello World" sample application](hello-world.md).
-   Create various controls for your application views, such as:

    -   [Flex container](flexcontainer.md)
    -   [ImageView](imageview.md)
    -   [TextLabel](textlabel.md)
    -   [Button](button.md)

    You can also create [custom view controls](creating-custom-view-controls.md).

-   Add [visuals](visuals.md) and [animations](animation.md) to your controls.
-   [Style your controls](styling-controls-with-JSON.md) based on states and add transitions between states.
