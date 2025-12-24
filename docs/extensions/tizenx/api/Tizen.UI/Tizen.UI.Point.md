### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Point Struct

Struct defining a 2-D point as a pair of floats.

```csharp
public struct Point
```
### Constructors

<a name='Tizen.UI.Point.Point(float,float)'></a>

## Point(float, float) Constructor

Creates a new Point object that represents the point (x,y).

```csharp
public Point(float x, float y);
```
#### Parameters

<a name='Tizen.UI.Point.Point(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal coordinate.

<a name='Tizen.UI.Point.Point(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical coordinate.

<a name='Tizen.UI.Point.Point(Tizen.UI.Size)'></a>

## Point(Size) Constructor

Creates a new Point object that has coordinates that are specified by the width and height of sz, in that order.

```csharp
public Point(Tizen.UI.Size sz);
```
#### Parameters

<a name='Tizen.UI.Point.Point(Tizen.UI.Size).sz'></a>

`sz` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

Size that specifies a Point that has the coordinates (Width, Height).
### Fields

<a name='Tizen.UI.Point.Zero'></a>

## Point.Zero Field

The Point at {0,0}.

```csharp
public static Point Zero;
```

#### Field Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')
### Properties

<a name='Tizen.UI.Point.IsEmpty'></a>

## Point.IsEmpty Property

Whether both X and Y are 0.

```csharp
public bool IsEmpty { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if both X and Y are 0.0.

<a name='Tizen.UI.Point.X'></a>

## Point.X Property

Location along the horizontal axis.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Point.Y'></a>

## Point.Y Property

Location along the vertical axis.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Point.Deconstruct(float,float)'></a>

## Point.Deconstruct(float, float) Method

Deconstructs the Point object into its individual components (X and Y).

```csharp
public void Deconstruct(out float x, out float y);
```
#### Parameters

<a name='Tizen.UI.Point.Deconstruct(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X component of the Point.

<a name='Tizen.UI.Point.Deconstruct(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y component of the Point.

<a name='Tizen.UI.Point.Distance(Tizen.UI.Point)'></a>

## Point.Distance(Point) Method

Calculates the distance between two points.

```csharp
public double Distance(Tizen.UI.Point other);
```
#### Parameters

<a name='Tizen.UI.Point.Distance(Tizen.UI.Point).other'></a>

`other` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The Point to which the distance is calculated.

#### Returns
[System.Double](https://docs.microsoft.com/en-us/dotnet/api/System.Double 'System.Double')  
The distance between this and the other.

<a name='Tizen.UI.Point.Equals(object)'></a>

## Point.Equals(object) Method

Returns true if the X and Y values of this are exactly equal to those in the argument.

```csharp
public override bool Equals(object o);
```
#### Parameters

<a name='Tizen.UI.Point.Equals(object).o'></a>

`o` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

Another Point.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if the X and Y values are equal to those in o. Returns false if o is not a Point.

<a name='Tizen.UI.Point.GetHashCode()'></a>

## Point.GetHashCode() Method

Returns a hash value for the Point.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A value intended for efficient insertion and lookup in hashtable-based data structures.

<a name='Tizen.UI.Point.Offset(float,float)'></a>

## Point.Offset(float, float) Method

Returns a new Point that translates the current Point by dx and dy.

```csharp
public Tizen.UI.Point Offset(float dx, float dy);
```
#### Parameters

<a name='Tizen.UI.Point.Offset(float,float).dx'></a>

`dx` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount to add along the X axis.

<a name='Tizen.UI.Point.Offset(float,float).dy'></a>

`dy` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount to add along the Y axis.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A new Point at [this.X + dx, this.Y + dy].

<a name='Tizen.UI.Point.Round()'></a>

## Point.Round() Method

Returns a new Point whose X and Y have been rounded to the nearest integral value.

```csharp
public Tizen.UI.Point Round();
```

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A new Point whose X and Y have been rounded to the nearest integral value, per the behavior of Math.Round(Double).

<a name='Tizen.UI.Point.ToString()'></a>

## Point.ToString() Method

Returns a string that represents the current [Point](Tizen.UI.Point.md 'Tizen.UI.Point') structure.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
A string that represents the current [Point](Tizen.UI.Point.md 'Tizen.UI.Point') structure.
### Operators

<a name='Tizen.UI.Point.op_Addition(Tizen.UI.Point,Tizen.UI.Point)'></a>

## Point.operator +(Point, Point) Operator

Adds two Points.

```csharp
public static Tizen.UI.Point operator +(Tizen.UI.Point p1, Tizen.UI.Point p2);
```
#### Parameters

<a name='Tizen.UI.Point.op_Addition(Tizen.UI.Point,Tizen.UI.Point).p1'></a>

`p1` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The first point value.

<a name='Tizen.UI.Point.op_Addition(Tizen.UI.Point,Tizen.UI.Point).p2'></a>

`p2` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The second point value.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
The sum of `p1` and `p2`.

<a name='Tizen.UI.Point.op_Addition(Tizen.UI.Point,Tizen.UI.Size)'></a>

## Point.operator +(Point, Size) Operator

Returns a new Point by adding a Size to a Point.

```csharp
public static Tizen.UI.Point operator +(Tizen.UI.Point pt, Tizen.UI.Size sz);
```
#### Parameters

<a name='Tizen.UI.Point.op_Addition(Tizen.UI.Point,Tizen.UI.Size).pt'></a>

`pt` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The Point to which sz is being added.

<a name='Tizen.UI.Point.op_Addition(Tizen.UI.Point,Tizen.UI.Size).sz'></a>

`sz` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The values to add to pt.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A new Point at [pt.X + sz.Width, pt.Y + sz.Height].

<a name='Tizen.UI.Point.op_ExplicitTizen.UI.Size(Tizen.UI.Point)'></a>

## Point.explicit operator Size(Point) Operator

Returns a new Size whose Width and Height and equivalent to the pt's X and Y properties.

```csharp
public static Tizen.UI.Size explicit operator Size(Tizen.UI.Point pt);
```
#### Parameters

<a name='Tizen.UI.Point.op_ExplicitTizen.UI.Size(Tizen.UI.Point).pt'></a>

`pt` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The Point to be translated as a Size.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
A new Size based on the pt.

<a name='Tizen.UI.Point.op_Inequality(Tizen.UI.Point,Tizen.UI.Point)'></a>

## Point.operator !=(Point, Point) Operator

Compares two points to determine if they are not equal.

```csharp
public static bool operator !=(Tizen.UI.Point ptA, Tizen.UI.Point ptB);
```
#### Parameters

<a name='Tizen.UI.Point.op_Inequality(Tizen.UI.Point,Tizen.UI.Point).ptA'></a>

`ptA` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The first point to compare.

<a name='Tizen.UI.Point.op_Inequality(Tizen.UI.Point,Tizen.UI.Point).ptB'></a>

`ptB` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The second point to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the points are not equal, false otherwise.

<a name='Tizen.UI.Point.op_Subtraction(Tizen.UI.Point,Tizen.UI.Point)'></a>

## Point.operator -(Point, Point) Operator

Subtracts one from another.

```csharp
public static Tizen.UI.Point operator -(Tizen.UI.Point p1, Tizen.UI.Point p2);
```
#### Parameters

<a name='Tizen.UI.Point.op_Subtraction(Tizen.UI.Point,Tizen.UI.Point).p1'></a>

`p1` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The point from which `p2` is substracted.

<a name='Tizen.UI.Point.op_Subtraction(Tizen.UI.Point,Tizen.UI.Point).p2'></a>

`p2` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The point to substract from `p1`.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
The difference between them.

<a name='Tizen.UI.Point.op_Subtraction(Tizen.UI.Point,Tizen.UI.Size)'></a>

## Point.operator -(Point, Size) Operator

Returns a new Point by subtracting a Size from a Point.

```csharp
public static Tizen.UI.Point operator -(Tizen.UI.Point pt, Tizen.UI.Size sz);
```
#### Parameters

<a name='Tizen.UI.Point.op_Subtraction(Tizen.UI.Point,Tizen.UI.Size).pt'></a>

`pt` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The Point from which sz is to be subtracted.

<a name='Tizen.UI.Point.op_Subtraction(Tizen.UI.Point,Tizen.UI.Size).sz'></a>

`sz` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The Size whose Width and Height will be subtracted from pt's X and Y.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A new Point at [pt.X - sz.Width, pt.Y - sz.Height].






