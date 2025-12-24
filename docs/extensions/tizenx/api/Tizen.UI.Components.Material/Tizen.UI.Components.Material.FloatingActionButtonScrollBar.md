### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## FloatingActionButtonScrollBar Class

A class representing a scroll bar with a floating icon.

```csharp
public class FloatingActionButtonScrollBar : Tizen.UI.Components.Material.ScrollBar
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; [Tizen.UI.Components.ScrollBarBase](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ScrollBarBase 'Tizen.UI.Components.ScrollBarBase') &#129106; [ScrollBar](Tizen.UI.Components.Material.ScrollBar.md 'Tizen.UI.Components.Material.ScrollBar') &#129106; FloatingActionButtonScrollBar

Derived  
&#8627; [GoToTopScrollBar](Tizen.UI.Components.Material.GoToTopScrollBar.md 'Tizen.UI.Components.Material.GoToTopScrollBar')
### Constructors

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButtonScrollBar()'></a>

## FloatingActionButtonScrollBar() Constructor

Initializes a new instance of the [GoToTopScrollBar](Tizen.UI.Components.Material.GoToTopScrollBar.md 'Tizen.UI.Components.Material.GoToTopScrollBar') class.

```csharp
public FloatingActionButtonScrollBar();
```

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables)'></a>

## FloatingActionButtonScrollBar(ScrollBarVariables) Constructor

Initializes a new instance of the [GoToTopScrollBar](Tizen.UI.Components.Material.GoToTopScrollBar.md 'Tizen.UI.Components.Material.GoToTopScrollBar') class.

```csharp
public FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables varables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables).varables'></a>

`varables` [ScrollBarVariables](Tizen.UI.Components.Material.ScrollBarVariables.md 'Tizen.UI.Components.Material.ScrollBarVariables')

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables,Tizen.UI.Components.Material.IconButtonVariables)'></a>

## FloatingActionButtonScrollBar(ScrollBarVariables, IconButtonVariables) Constructor

Initializes a new instance of the [GoToTopScrollBar](Tizen.UI.Components.Material.GoToTopScrollBar.md 'Tizen.UI.Components.Material.GoToTopScrollBar') class with variables.

```csharp
public FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables variables, Tizen.UI.Components.Material.IconButtonVariables iconVariables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables,Tizen.UI.Components.Material.IconButtonVariables).variables'></a>

`variables` [ScrollBarVariables](Tizen.UI.Components.Material.ScrollBarVariables.md 'Tizen.UI.Components.Material.ScrollBarVariables')

The variables for the scroll bar.

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButtonScrollBar(Tizen.UI.Components.Material.ScrollBarVariables,Tizen.UI.Components.Material.IconButtonVariables).iconVariables'></a>

`iconVariables` [IconButtonVariables](Tizen.UI.Components.Material.IconButtonVariables.md 'Tizen.UI.Components.Material.IconButtonVariables')

The variables for the go to top icon.
### Properties

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButton'></a>

## FloatingActionButtonScrollBar.FloatingActionButton Property

Gets or sets a floating action button.  
This button will be placed at the bottom right corner of the scaffold above the content.

```csharp
public Tizen.UI.Components.Material.IconButton FloatingActionButton { get; set; }
```

#### Property Value
[IconButton](Tizen.UI.Components.Material.IconButton.md 'Tizen.UI.Components.Material.IconButton')

### Remarks
There are predefined contents such as [FloatingActionButton](Tizen.UI.Components.Material.FloatingActionButtonScrollBar.md#Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButton 'Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingActionButton').

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingIcon'></a>

## FloatingActionButtonScrollBar.FloatingIcon Property

Clickable Go-To-Top icon.

```csharp
public Tizen.UI.Components.Material.IconButton FloatingIcon { get; }
```

#### Property Value
[IconButton](Tizen.UI.Components.Material.IconButton.md 'Tizen.UI.Components.Material.IconButton')

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingOffset'></a>

## FloatingActionButtonScrollBar.FloatingOffset Property

The relative offset of the floating action button from the bottom edge of the scaffold.

```csharp
public Tizen.UI.Point FloatingOffset { get; set; }
```

#### Property Value
[Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.FloatingOrigin'></a>

## FloatingActionButtonScrollBar.FloatingOrigin Property

Gets or sets a origin type of floating action button regarding positioning.  
This may change position and pivot properties of the floating action button.

```csharp
public Tizen.UI.Components.FloatingOrigin FloatingOrigin { get; set; }
```

#### Property Value
[Tizen.UI.Components.FloatingOrigin](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.FloatingOrigin 'Tizen.UI.Components.FloatingOrigin')
### Methods

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.SetExtraFloatingOffsetY(float)'></a>

## FloatingActionButtonScrollBar.SetExtraFloatingOffsetY(float) Method

Sets an additional vertical offset for floating components.  
Adjusts the Y position of the scaffold's floating action button by applying the specified offset.

```csharp
public void SetExtraFloatingOffsetY(float extra);
```
#### Parameters

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.SetExtraFloatingOffsetY(float).extra'></a>

`extra` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.UpdateScrollPosition(Tizen.UI.Point)'></a>

## FloatingActionButtonScrollBar.UpdateScrollPosition(Point) Method

Updates the scroll position of the target view.

```csharp
public override void UpdateScrollPosition(Tizen.UI.Point position);
```
#### Parameters

<a name='Tizen.UI.Components.Material.FloatingActionButtonScrollBar.UpdateScrollPosition(Tizen.UI.Point).position'></a>

`position` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The new scroll position.

Implements [UpdateScrollPosition(Point)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IScrollBar.UpdateScrollPosition#Tizen_UI_IScrollBar_UpdateScrollPosition_Tizen_UI_Point_ 'Tizen.UI.IScrollBar.UpdateScrollPosition(Tizen.UI.Point)')













































