### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## ModelPrimitive Class

Class for Model Primitives for 3D Geometry and Material.

```csharp
public class ModelPrimitive : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; ModelPrimitive
### Constructors

<a name='Tizen.UI.Scene3D.ModelPrimitive.ModelPrimitive()'></a>

## ModelPrimitive() Constructor

Create an initialized ModelPrimitive.

```csharp
public ModelPrimitive();
```
### Properties

<a name='Tizen.UI.Scene3D.ModelPrimitive.Geometry'></a>

## ModelPrimitive.Geometry Property

The Geometry object of the ModelNode object.

```csharp
public Tizen.UI.Internal.Geometry Geometry { get; set; }
```

#### Property Value
Tizen.UI.Internal.Geometry

<a name='Tizen.UI.Scene3D.ModelPrimitive.Material'></a>

## ModelPrimitive.Material Property

The Material object of the ModelNode object.

```csharp
public Tizen.UI.Scene3D.Material Material { get; set; }
```

#### Property Value
[Material](Tizen.UI.Scene3D.Material.md 'Tizen.UI.Scene3D.Material')

### Remarks
This Material object is for setting Material properties of 3D models. Also, Material can be shared with multiple ModelPrimitives and if the value is modified, the rendering results of all ModelPrimitives using this Material will be changed.






































