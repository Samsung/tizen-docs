### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## ScaffoldBase Class

A base class of scaffold which need to be root view of application.  
Application can have a scaffold in a window to layout content properly  
with some spefical UI layout and behavior.

```csharp
public abstract class ScaffoldBase : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; ScaffoldBase
### Constructors

<a name='Tizen.UI.Components.ScaffoldBase.ScaffoldBase()'></a>

## ScaffoldBase() Constructor

Constructs an empty Scaffoldbase.

```csharp
public ScaffoldBase();
```
### Properties

<a name='Tizen.UI.Components.ScaffoldBase.FloatingActionButton'></a>

## ScaffoldBase.FloatingActionButton Property

Gets or sets a floating action button.  
This button will be placed at the bottom right corner of the scaffold above the content.

```csharp
public Tizen.UI.View FloatingActionButton { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

### Remarks
There are predefined contents such as [FloatingActionButton](Tizen.UI.Components.ScaffoldBase.md#Tizen.UI.Components.ScaffoldBase.FloatingActionButton 'Tizen.UI.Components.ScaffoldBase.FloatingActionButton').

<a name='Tizen.UI.Components.ScaffoldBase.FloatingOffset'></a>

## ScaffoldBase.FloatingOffset Property

The relative offset of the floating action button from the bottom edge of the scaffold.

```csharp
public Tizen.UI.Point FloatingOffset { get; set; }
```

#### Property Value
[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

<a name='Tizen.UI.Components.ScaffoldBase.FloatingOrigin'></a>

## ScaffoldBase.FloatingOrigin Property

Gets or sets a origin type of floating action button regarding positioning.  
This may change position and pivot properties of the floating action button.

```csharp
public Tizen.UI.Components.FloatingOrigin FloatingOrigin { get; set; }
```

#### Property Value
[FloatingOrigin](Tizen.UI.Components.FloatingOrigin.md 'Tizen.UI.Components.FloatingOrigin')

<a name='Tizen.UI.Components.ScaffoldBase.HasIndicatorArea'></a>

## ScaffoldBase.HasIndicatorArea Property

Boolean flag whether system indicator area is included or not.  
If it is true, indicator height will be placed on the scaffold.

```csharp
public bool HasIndicatorArea { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.ScaffoldBase.HasNavigationBarArea'></a>

## ScaffoldBase.HasNavigationBarArea Property

Boolean flag whether system navigation bar area is included or not.  
If it is true, navigation bar height will be placed on the scaffold.

```csharp
public bool HasNavigationBarArea { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.ScaffoldBase.IndicatorAreaColor'></a>

## ScaffoldBase.IndicatorAreaColor Property

Gets or sets the color of indicator area.  
If this property is set, the color of indicator area will be set to this color regardless of other properties.  
If this property is set to `Color.Default` the color of indicator area will be set to the color provided from the [IndicatorAreaColorProvider](Tizen.UI.Components.ScaffoldBase.md#Tizen.UI.Components.ScaffoldBase.IndicatorAreaColorProvider 'Tizen.UI.Components.ScaffoldBase.IndicatorAreaColorProvider').  
If  [IndicatorAreaColorProvider](Tizen.UI.Components.ScaffoldBase.md#Tizen.UI.Components.ScaffoldBase.IndicatorAreaColorProvider 'Tizen.UI.Components.ScaffoldBase.IndicatorAreaColorProvider') not set, the color of indicator area will be transparent.

```csharp
public Tizen.UI.Color IndicatorAreaColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.ScaffoldBase.IndicatorAreaColorProvider'></a>

## ScaffoldBase.IndicatorAreaColorProvider Property

Gets or sets a color provider to the scaffold.

```csharp
public Tizen.UI.Components.IColorProvider IndicatorAreaColorProvider { get; set; }
```

#### Property Value
[IColorProvider](Tizen.UI.Components.IColorProvider.md 'Tizen.UI.Components.IColorProvider')
### Methods

<a name='Tizen.UI.Components.ScaffoldBase.SetExtraFloatingOffsetY(float)'></a>

## ScaffoldBase.SetExtraFloatingOffsetY(float) Method

Sets an additional vertical offset for floating components.  
Adjusts the Y position of the scaffold's floating action button by applying the specified offset.

```csharp
public void SetExtraFloatingOffsetY(float extra);
```
#### Parameters

<a name='Tizen.UI.Components.ScaffoldBase.SetExtraFloatingOffsetY(float).extra'></a>

`extra` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')


























































