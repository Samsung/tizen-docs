### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## Drawable Class

The Drawable class is an abstract class that provides a base for all drawable objects.

```csharp
public abstract class Drawable : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Drawable

Derived  
&#8627; [DrawableGroup](Tizen.UI.Primitives2D.DrawableGroup.md 'Tizen.UI.Primitives2D.DrawableGroup')  
&#8627; [ImageDrawable](Tizen.UI.Primitives2D.ImageDrawable.md 'Tizen.UI.Primitives2D.ImageDrawable')  
&#8627; [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')
### Properties

<a name='Tizen.UI.Primitives2D.Drawable.BoundingBox'></a>

## Drawable.BoundingBox Property

Gets the bounding box of the drawable object.

```csharp
public Tizen.UI.Rect BoundingBox { get; }
```

#### Property Value
Tizen.UI.Rect
### Methods

<a name='Tizen.UI.Primitives2D.Drawable.ClipPath(Tizen.UI.Primitives2D.Drawable)'></a>

## Drawable.ClipPath(Drawable) Method

Sets the clip path for the drawable object.

```csharp
public void ClipPath(Tizen.UI.Primitives2D.Drawable clip);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Drawable.ClipPath(Tizen.UI.Primitives2D.Drawable).clip'></a>

`clip` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The clip path to set.

<a name='Tizen.UI.Primitives2D.Drawable.Rotate(float)'></a>

## Drawable.Rotate(float) Method

Rotates the position of the drawable object by the specified degree.

```csharp
public void Rotate(float degree);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Drawable.Rotate(float).degree'></a>

`degree` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The degree to rotate the position by.

<a name='Tizen.UI.Primitives2D.Drawable.Scale(float)'></a>

## Drawable.Scale(float) Method

Scales the size of the drawable object by the specified factor.

```csharp
public void Scale(float factor);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Drawable.Scale(float).factor'></a>

`factor` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The factor to scale the size by.

<a name='Tizen.UI.Primitives2D.Drawable.Transform(float[])'></a>

## Drawable.Transform(float[]) Method

Sets the transform matrix of the drawable object.

```csharp
public void Transform(float[] matrix);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Drawable.Transform(float[]).matrix'></a>

`matrix` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The transform matrix to set.

<a name='Tizen.UI.Primitives2D.Drawable.Translate(float,float)'></a>

## Drawable.Translate(float, float) Method

Translates the position of the drawable object by the specified amount.

```csharp
public void Translate(float x, float y);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Drawable.Translate(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount to translate on the x-axis.

<a name='Tizen.UI.Primitives2D.Drawable.Translate(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount to translate on the y-axis.



















































