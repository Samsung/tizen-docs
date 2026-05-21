### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Rect Struct

Represents a rectangular area by defining its position and size.

```csharp
public struct Rect
```
### Constructors

<a name='Tizen.UI.Rect.Rect(float,float,float,float)'></a>

## Rect(float, float, float, float) Constructor

Initializes a new instance of the [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') struct.

```csharp
public Rect(float x, float y, float width, float height);
```
#### Parameters

<a name='Tizen.UI.Rect.Rect(float,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the upper-left corner of the rectangle.

<a name='Tizen.UI.Rect.Rect(float,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the upper-left corner of the rectangle.

<a name='Tizen.UI.Rect.Rect(float,float,float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the rectangle.

<a name='Tizen.UI.Rect.Rect(float,float,float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the rectangle.

<a name='Tizen.UI.Rect.Rect(Tizen.UI.Point,Tizen.UI.Size)'></a>

## Rect(Point, Size) Constructor

Initializes a new instance of the [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') struct.

```csharp
public Rect(Tizen.UI.Point loc, Tizen.UI.Size sz);
```
#### Parameters

<a name='Tizen.UI.Rect.Rect(Tizen.UI.Point,Tizen.UI.Size).loc'></a>

`loc` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The location of the upper-left corner of the rectangle.

<a name='Tizen.UI.Rect.Rect(Tizen.UI.Point,Tizen.UI.Size).sz'></a>

`sz` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size of the rectangle.
### Fields

<a name='Tizen.UI.Rect.Zero'></a>

## Rect.Zero Field

Gets a [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure with all coordinates and sizes set to zero.

```csharp
public static Rect Zero;
```

#### Field Value
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')
### Properties

<a name='Tizen.UI.Rect.Bottom'></a>

## Rect.Bottom Property

Gets the y-coordinate of the bottom edge of the rectangle.

```csharp
public float Bottom { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.Center'></a>

## Rect.Center Property

Gets the center point of the rectangle.

```csharp
public Tizen.UI.Point Center { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.Rect.Height'></a>

## Rect.Height Property

Gets or sets the height of the rectangle.

```csharp
public float Height { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.IsEmpty'></a>

## Rect.IsEmpty Property

Gets a value indicating whether this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') is empty.

```csharp
public bool IsEmpty { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Rect.Left'></a>

## Rect.Left Property

Gets the x-coordinate of the left edge of the rectangle.

```csharp
public float Left { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.Location'></a>

## Rect.Location Property

Gets or sets the location of the upper-left corner of the rectangle.

```csharp
public Tizen.UI.Point Location { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.Rect.Right'></a>

## Rect.Right Property

Gets the x-coordinate of the right edge of the rectangle.

```csharp
public float Right { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.Size'></a>

## Rect.Size Property

Gets or sets the size of the rectangle.

```csharp
public Tizen.UI.Size Size { get; set; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.Rect.Top'></a>

## Rect.Top Property

Gets the y-coordinate of the top edge of the rectangle.

```csharp
public float Top { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.Width'></a>

## Rect.Width Property

Gets or sets the width of the rectangle.

```csharp
public float Width { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.X'></a>

## Rect.X Property

Gets or sets the x-coordinate of the upper-left corner of the rectangle.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Rect.Y'></a>

## Rect.Y Property

Gets or sets the y-coordinate of the upper-left corner of the rectangle.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Rect.Contains(float,float)'></a>

## Rect.Contains(float, float) Method

Indicates whether the specified point is contained within the rectangular region defined by this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure.

```csharp
public bool Contains(float x, float y);
```
#### Parameters

<a name='Tizen.UI.Rect.Contains(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the point to test.

<a name='Tizen.UI.Rect.Contains(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the point to test.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [x](Tizen.UI.Rect.md#Tizen.UI.Rect.Contains(float,float).x 'Tizen.UI.Rect.Contains(float, float).x') and [y](Tizen.UI.Rect.md#Tizen.UI.Rect.Contains(float,float).y 'Tizen.UI.Rect.Contains(float, float).y') are contained within the rectangular region defined by this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure; otherwise, false.

<a name='Tizen.UI.Rect.Contains(Tizen.UI.Point)'></a>

## Rect.Contains(Point) Method

Indicates whether the specified point is contained within the rectangular region defined by this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure.

```csharp
public bool Contains(Tizen.UI.Point pt);
```
#### Parameters

<a name='Tizen.UI.Rect.Contains(Tizen.UI.Point).pt'></a>

`pt` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The point to test.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [pt](Tizen.UI.Rect.md#Tizen.UI.Rect.Contains(Tizen.UI.Point).pt 'Tizen.UI.Rect.Contains(Tizen.UI.Point).pt') is contained within the rectangular region defined by this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure; otherwise, false.

<a name='Tizen.UI.Rect.Contains(Tizen.UI.Rect)'></a>

## Rect.Contains(Rect) Method

Checks if the specified rectangle is completely inside this rectangle.

```csharp
public bool Contains(Tizen.UI.Rect rect);
```
#### Parameters

<a name='Tizen.UI.Rect.Contains(Tizen.UI.Rect).rect'></a>

`rect` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The rectangle to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the specified rectangle is completely inside this rectangle, otherwise false.

<a name='Tizen.UI.Rect.Deconstruct(float,float,float,float)'></a>

## Rect.Deconstruct(float, float, float, float) Method

Deconstructs the Rect object into its individual components (X, Y, Width, Height).

```csharp
public void Deconstruct(out float x, out float y, out float width, out float height);
```
#### Parameters

<a name='Tizen.UI.Rect.Deconstruct(float,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X coordinate of the rectangle.

<a name='Tizen.UI.Rect.Deconstruct(float,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y coordinate of the rectangle.

<a name='Tizen.UI.Rect.Deconstruct(float,float,float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the rectangle.

<a name='Tizen.UI.Rect.Deconstruct(float,float,float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the rectangle.

<a name='Tizen.UI.Rect.Equals(object)'></a>

## Rect.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Rect.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [obj](Tizen.UI.Rect.md#Tizen.UI.Rect.Equals(object).obj 'Tizen.UI.Rect.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, false.

<a name='Tizen.UI.Rect.Equals(Tizen.UI.Rect)'></a>

## Rect.Equals(Rect) Method

Indicates whether this instance and another specified [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure are equal.

```csharp
public bool Equals(Tizen.UI.Rect other);
```
#### Parameters

<a name='Tizen.UI.Rect.Equals(Tizen.UI.Rect).other'></a>

`other` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [other](Tizen.UI.Rect.md#Tizen.UI.Rect.Equals(Tizen.UI.Rect).other 'Tizen.UI.Rect.Equals(Tizen.UI.Rect).other') and this instance are equal; otherwise, false.

<a name='Tizen.UI.Rect.FromLTRB(float,float,float,float)'></a>

## Rect.FromLTRB(float, float, float, float) Method

Creates a new [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure with the specified values.

```csharp
public static Tizen.UI.Rect FromLTRB(float left, float top, float right, float bottom);
```
#### Parameters

<a name='Tizen.UI.Rect.FromLTRB(float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the upper-left corner of the rectangle.

<a name='Tizen.UI.Rect.FromLTRB(float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the upper-left corner of the rectangle.

<a name='Tizen.UI.Rect.FromLTRB(float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the lower-right corner of the rectangle.

<a name='Tizen.UI.Rect.FromLTRB(float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the lower-right corner of the rectangle.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure with the specified values.

<a name='Tizen.UI.Rect.GetHashCode()'></a>

## Rect.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Rect.Inflate(float,float)'></a>

## Rect.Inflate(float, float) Method

Inflates the current rectangle by the specified width and height.

```csharp
public Tizen.UI.Rect Inflate(float width, float height);
```
#### Parameters

<a name='Tizen.UI.Rect.Inflate(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount to inflate the rectangle horizontally.

<a name='Tizen.UI.Rect.Inflate(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount to inflate the rectangle vertically.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new rectangle that represents the inflated version of the current rectangle.

<a name='Tizen.UI.Rect.Inflate(Tizen.UI.Size)'></a>

## Rect.Inflate(Size) Method

Returns a new [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure that has been inflated by the specified amount.

```csharp
public Tizen.UI.Rect Inflate(Tizen.UI.Size sz);
```
#### Parameters

<a name='Tizen.UI.Rect.Inflate(Tizen.UI.Size).sz'></a>

`sz` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size of the inflation.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure that represents the inflated rectangle.

<a name='Tizen.UI.Rect.Intersect(Tizen.UI.Rect)'></a>

## Rect.Intersect(Rect) Method

Returns a new rectangle that represents the intersection of the current rectangle and the specified rectangle.

```csharp
public Tizen.UI.Rect Intersect(Tizen.UI.Rect r);
```
#### Parameters

<a name='Tizen.UI.Rect.Intersect(Tizen.UI.Rect).r'></a>

`r` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The rectangle to intersect with the current rectangle.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new rectangle that represents the intersection of the current rectangle specified rectangle.

<a name='Tizen.UI.Rect.Intersect(Tizen.UI.Rect,Tizen.UI.Rect)'></a>

## Rect.Intersect(Rect, Rect) Method

Returns a new rectangle that represents the intersection of two given rectangles.

```csharp
public static Tizen.UI.Rect Intersect(Tizen.UI.Rect r1, Tizen.UI.Rect r2);
```
#### Parameters

<a name='Tizen.UI.Rect.Intersect(Tizen.UI.Rect,Tizen.UI.Rect).r1'></a>

`r1` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The first rectangle.

<a name='Tizen.UI.Rect.Intersect(Tizen.UI.Rect,Tizen.UI.Rect).r2'></a>

`r2` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The second rectangle.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new rectangle representing the intersection of the two given rectangles.

<a name='Tizen.UI.Rect.IntersectsWith(Tizen.UI.Rect)'></a>

## Rect.IntersectsWith(Rect) Method

Indicates whether the rectangular region represented by this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') intersects with the rectangular region represented by the specified [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure.

```csharp
public bool IntersectsWith(Tizen.UI.Rect r);
```
#### Parameters

<a name='Tizen.UI.Rect.IntersectsWith(Tizen.UI.Rect).r'></a>

`r` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure to test for intersection.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if the rectangular region represented by this [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') intersects with the rectangular region represented by [r](Tizen.UI.Rect.md#Tizen.UI.Rect.IntersectsWith(Tizen.UI.Rect).r 'Tizen.UI.Rect.IntersectsWith(Tizen.UI.Rect).r'); otherwise, false.

<a name='Tizen.UI.Rect.Offset(float,float)'></a>

## Rect.Offset(float, float) Method

Returns a new rectangle that is offset by the specified amount.

```csharp
public Tizen.UI.Rect Offset(float dx, float dy);
```
#### Parameters

<a name='Tizen.UI.Rect.Offset(float,float).dx'></a>

`dx` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal offset.

<a name='Tizen.UI.Rect.Offset(float,float).dy'></a>

`dy` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical offset.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new rectangle with the offset applied.

<a name='Tizen.UI.Rect.Offset(Tizen.UI.Point)'></a>

## Rect.Offset(Point) Method

Returns a new Rect that has been offset by the specified distance.

```csharp
public Tizen.UI.Rect Offset(Tizen.UI.Point dr);
```
#### Parameters

<a name='Tizen.UI.Rect.Offset(Tizen.UI.Point).dr'></a>

`dr` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The distance to offset the Rect.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new Rect that has been offset by the specified distance.

<a name='Tizen.UI.Rect.Round()'></a>

## Rect.Round() Method

Rounds the values of the X, Y, Width, and Height properties of the current Rect object to the nearest whole number.

```csharp
public Tizen.UI.Rect Round();
```

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new Rect object with the rounded values.

<a name='Tizen.UI.Rect.ToString()'></a>

## Rect.ToString() Method

Returns a string that represents the current object.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
A string that represents the current object.

<a name='Tizen.UI.Rect.Union(Tizen.UI.Rect)'></a>

## Rect.Union(Rect) Method

Returns a rectangle that represents the union of the current rectangle and the specified rectangle.

```csharp
public Tizen.UI.Rect Union(Tizen.UI.Rect r);
```
#### Parameters

<a name='Tizen.UI.Rect.Union(Tizen.UI.Rect).r'></a>

`r` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The rectangle to combine with the current rectangle.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new rectangle that represents the union of the current rectangle and the specified rectangle.

<a name='Tizen.UI.Rect.Union(Tizen.UI.Rect,Tizen.UI.Rect)'></a>

## Rect.Union(Rect, Rect) Method

Returns a rectangle that represents the union of the two given rectangles.

```csharp
public static Tizen.UI.Rect Union(Tizen.UI.Rect r1, Tizen.UI.Rect r2);
```
#### Parameters

<a name='Tizen.UI.Rect.Union(Tizen.UI.Rect,Tizen.UI.Rect).r1'></a>

`r1` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The first rectangle.

<a name='Tizen.UI.Rect.Union(Tizen.UI.Rect,Tizen.UI.Rect).r2'></a>

`r2` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The second rectangle.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new rectangle that represents the union of the two given rectangles.
### Operators

<a name='Tizen.UI.Rect.op_Equality(Tizen.UI.Rect,Tizen.UI.Rect)'></a>

## Rect.operator ==(Rect, Rect) Operator

Compares two [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structures for equality.

```csharp
public static bool operator ==(Tizen.UI.Rect r1, Tizen.UI.Rect r2);
```
#### Parameters

<a name='Tizen.UI.Rect.op_Equality(Tizen.UI.Rect,Tizen.UI.Rect).r1'></a>

`r1` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The first [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure to compare.

<a name='Tizen.UI.Rect.op_Equality(Tizen.UI.Rect,Tizen.UI.Rect).r2'></a>

`r2` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The second [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [r1](Tizen.UI.Rect.md#Tizen.UI.Rect.op_Equality(Tizen.UI.Rect,Tizen.UI.Rect).r1 'Tizen.UI.Rect.op_Equality(Tizen.UI.Rect, Tizen.UI.Rect).r1') and [r2](Tizen.UI.Rect.md#Tizen.UI.Rect.op_Equality(Tizen.UI.Rect,Tizen.UI.Rect).r2 'Tizen.UI.Rect.op_Equality(Tizen.UI.Rect, Tizen.UI.Rect).r2') are equal; otherwise, false.

<a name='Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect,Tizen.UI.Rect)'></a>

## Rect.operator !=(Rect, Rect) Operator

Compares two [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structures for inequality.

```csharp
public static bool operator !=(Tizen.UI.Rect r1, Tizen.UI.Rect r2);
```
#### Parameters

<a name='Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect,Tizen.UI.Rect).r1'></a>

`r1` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The first [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure to compare.

<a name='Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect,Tizen.UI.Rect).r2'></a>

`r2` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The second [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') structure to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [r1](Tizen.UI.Rect.md#Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect,Tizen.UI.Rect).r1 'Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect, Tizen.UI.Rect).r1') and [r2](Tizen.UI.Rect.md#Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect,Tizen.UI.Rect).r2 'Tizen.UI.Rect.op_Inequality(Tizen.UI.Rect, Tizen.UI.Rect).r2') are not equal; otherwise, false.






