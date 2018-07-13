# Natural User Interface

Natural User Interface (NUI) is a C\# toolkit on top of the DALi (Dynamic Animation Library) graphics library, which is written in C++.

NUI is a rich GUI library used for creating two-dimensional or three-dimensional applications. These applications are run on a range of Tizen devices, such as mobile devices, TVs, and wearables. NUI is built on a multi-threaded architecture, enabling realistic smooth animations. In addition, a range of optimization techniques are utilized to obtain low CPU and GPU usage, further increasing graphics performance.

After you have set up the NUI development environment, you can quickly create rich UI applications with realistic effects and animations, such as:  

-   Image and video galleries
-   Music players
-   Home screens and launch pads
-   Advanced watch faces for wearable devices

NUI offers the following main features:

-   UI consisting of hierarchical scene graph nodes
-   Image and text creation
-   Layers to aid in two-dimensional UI layouting
-   Automatic background loading of resources
-   Easy-to-use [animation framework](animation.md) which hides the complexity of the underlying three-dimensional math
-   Keyboard, touch, and mouse handling

<a name="concepts"></a>
## Key Concepts

To be able to use NUI in your applications, you must become familiar with the following NUI key concepts:

-   **Scene graph**: Tree data structure, consisting of a collection of nodes.
-   **Window**: Top level of the scene graph, used for displaying a tree of layers and views.
-   **View**: Primary object for interaction. Views are effectively nodes that receive input (such as touch events), and act as a container for drawable elements and other views. Views can display content, such as color shapes, images, and text.

    A NUI application uses a hierarchy of view objects to position the visible content.

-   **Layer**: Layers allow you to overlay groups of views on top of each other.

To get started with NUI development, [study a "Hello World" sample application](hello-world.md).

## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
