# Layer

A layer is a transparent sheet upon which shapes are placed. It supports sub layers within layers to any desired depth.
Layers provide a mechanism for overlaying groups of views on top of each other.
Layers can also clip their contents, to exclude any content outside a user defined area.

Layers can be two-dimensional or three-dimensional, defined by their _behavior_ property.

 ![ ](./media/layers.png)

When a layer is added to the Window, it assigns a unique depth value. By default, the stage has a root layer with a depth value of 0.

Layers provide a mechanism for overlaying groups of actors on top of each other. Layers are drawn in order to determined the **depth** value of the layer.


```
// C# example of adding an ImageView to the layer
//Import necessary namespaces
using Tizen.NUI;
using Tizen.NUI.BaseComponents;

// Gets the default (root) layer
Window window = Window.Instance;

// Create Layer 1
Layer layer1 = new Layer();
window.AddLayer(layer1);

//Create Layer 2
Layer layer2 = new Layer();
window.AddLayer(layer2)

// Add a child view to layer 1
ImageView imageView1 = new ImageView();
layer1.Add(imageView1);

// Add a child view to layer 2
ImageView imageView2 = new ImageView();
layer2.Add(imageView2);
```

## Layer Specific Properties

 - `Behavior`: Specifies the behavior of the layer. The value can be `LayerUI` (default) or `Layer3D`.
 - `ChildCount`: To get the number of children the layer holds.
 - `Depth`: To query the depth of the layer.
 - `Name`: To set or get the name of the layer.
 - `Opacity`: To retrieve and set the opacity of the layer.
 - `Viewport`: To set the viewport(in window coordinate) of the layer.
 - `Visibility`: To retrieve and set the visibility of the layer.

### Re-ordering layers

By default root layer obtained from the Window instance has a *Depth* field value equal to 0, the same as a newly created layer. Only adding a layer to the window using api *window.AddLayer()* set *Depth* value as it is shown on code example below

```
Window window = Window.Instance;
//window.GetDefaultLayer().Depth = 0;

Layer ly0 = new Layer();
//ly0.Depth = 0
window.AddLayer(ly0);
//ly0.Depth = 1;

Layer ly1 = new Layer();
//ly1.Depth = 0;
window.AddLayer(ly1);
//ly1.Depth = 2;
```

Renderer draws layers and its content from the layers with lowest depth at the beginning. In result a layer and its content with higher depth value will be drawn at the top of the stack.

To reorder layers a set of API listed below can be used: 
 - Lower(): decrements *Depth* parameter
 - LowerToBottom(): sets *Depth* parameter to 0. It reorders other layers, and increments root layer *Depth*
 - MoveAbove(Layer l): moves a layer *Depth* directly above the giver layer
 - MoveBelow(Layer l): similar to *MoveAbove()* 
 - Raise(): increments a layer *Depth*
 - RaiseToTop(): move layer to the top of the layers stack. 

### Examples 
- Floating buttons above of the other application content. 
- Custom popups or floating views. 
- Custom menus

### LayerUI

#### Background
 - Graphics are drawn using renderers
 - Views can have zero or many renderers
 - Renderers can be shared by views
 - Renderers have a depth index property

With `LayerUI`, the draw order of the renderers is defined by both:
 - Renderer depth index
 - Position of view in the layer tree

### Layer3D

When you set the behavior of the layer to `Layer3D`, the opaque renderers are drawn first and written to the depth buffer.

Transparent renderers are drawn in order of distance from the camera ( painter's algorithm ).

 ![ ](./media/transSort.png)

## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
