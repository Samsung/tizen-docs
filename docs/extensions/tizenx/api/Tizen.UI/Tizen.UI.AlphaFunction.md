### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## AlphaFunction Class

The AlphaFunction class provides a way to define custom interpolation for animations.

```csharp
public sealed class AlphaFunction :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AlphaFunction

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Constructors

<a name='Tizen.UI.AlphaFunction.AlphaFunction(System.Func_float,float_)'></a>

## AlphaFunction(Func&lt;float,float>) Constructor

Creates an AlphaFunction object with a user-defined function.

```csharp
public AlphaFunction(System.Func&lt;float,float> userAlpha);
```
#### Parameters

<a name='Tizen.UI.AlphaFunction.AlphaFunction(System.Func_float,float_).userAlpha'></a>

`userAlpha` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

The user-defined function to use.

<a name='Tizen.UI.AlphaFunction.AlphaFunction(Tizen.UI.BuiltinAlphaFunctions)'></a>

## AlphaFunction(BuiltinAlphaFunctions) Constructor

Creates an AlphaFunction object with a built-in function.

```csharp
public AlphaFunction(Tizen.UI.BuiltinAlphaFunctions builtin);
```
#### Parameters

<a name='Tizen.UI.AlphaFunction.AlphaFunction(Tizen.UI.BuiltinAlphaFunctions).builtin'></a>

`builtin` [BuiltinAlphaFunctions](Tizen.UI.BuiltinAlphaFunctions.md 'Tizen.UI.BuiltinAlphaFunctions')

The built-in function to use.

<a name='Tizen.UI.AlphaFunction.AlphaFunction(Tizen.UI.Point,Tizen.UI.Point)'></a>

## AlphaFunction(Point, Point) Constructor

Creates a bezier curve alpha function with two control points.

```csharp
public AlphaFunction(Tizen.UI.Point point1, Tizen.UI.Point point2);
```
#### Parameters

<a name='Tizen.UI.AlphaFunction.AlphaFunction(Tizen.UI.Point,Tizen.UI.Point).point1'></a>

`point1` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The first control point.

<a name='Tizen.UI.AlphaFunction.AlphaFunction(Tizen.UI.Point,Tizen.UI.Point).point2'></a>

`point2` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The second control point.
### Properties

<a name='Tizen.UI.AlphaFunction.Handle'></a>

## AlphaFunction.Handle Property

Gets the handle of the AlphaFunction object.

```csharp
public System.IntPtr Handle { get; }
```

#### Property Value
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')
### Methods

<a name='Tizen.UI.AlphaFunction.Dispose()'></a>

## AlphaFunction.Dispose() Method

Disposes of this object and releases all resources.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')






