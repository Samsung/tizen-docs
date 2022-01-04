# Overview

VectorGraphics APIs are features for vector primitives drawing provided by NUI.
VectorGraphics namespace provides [CanvasView](./CanvasView.md) component and `Shape`, `DrawableGroup`, and `Picture` classes that inherit `Drawable` class.


The following lists the available feature using VectorGraphics:


## VectorGraphics Classes and Features

- [CanvasView](./CanvasView.md)
  - A component that uses the canvas area represented by `viewBox`.


- [Shape & Stroke](./ShapeAndStroke.md)
  - `Shape` is a set of path commands. it can set color, gradient and stroke property.


- [Grouping](./Grouping.md)
  - Groups the classes inherited by Drawable.


- [Transformation & Composition](./TransformationAndComposition.md)
  - Objects added to `CanvasView` support two-dimensional affine transformation. These also support composition of each other.


- [Picture](./Picture.md)
  - Draws a rasterized image (SVG, PNG, JPG and TVG format) in CanvasView.


## Related Information
- Dependencies
  -   Tizen 6.5 and Higher

