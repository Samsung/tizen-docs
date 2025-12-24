### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## ILayout Interface

Defines the contract for a class that can provide layout functionality for its children using a LayoutManager.

```csharp
public interface ILayout
```

Derived  
&#8627; [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox')  
&#8627; [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid')  
&#8627; [IFlexBox](Tizen.UI.Layouts.IFlexBox.md 'Tizen.UI.Layouts.IFlexBox')  
&#8627; [IGridLayout](Tizen.UI.Layouts.IGridLayout.md 'Tizen.UI.Layouts.IGridLayout')  
&#8627; [IStackLayout](Tizen.UI.Layouts.IStackLayout.md 'Tizen.UI.Layouts.IStackLayout')  
&#8627; [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout')  
&#8627; [StackBase](Tizen.UI.Layouts.StackBase.md 'Tizen.UI.Layouts.StackBase')
### Properties

<a name='Tizen.UI.Layouts.ILayout.Children'></a>

## ILayout.Children Property

Gets the children of the layout.

```csharp
System.Collections.Generic.IList&lt;Tizen.UI.View> Children { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Layouts.ILayout.DesiredHeight'></a>

## ILayout.DesiredHeight Property

Gets the desired height of the layout.

```csharp
float DesiredHeight { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.ILayout.DesiredWidth'></a>

## ILayout.DesiredWidth Property

Gets the desired width of the layout.

```csharp
float DesiredWidth { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.ILayout.LayoutDirection'></a>

## ILayout.LayoutDirection Property

Gets the layout direction of the layout.

```csharp
Tizen.UI.LayoutDirection LayoutDirection { get; }
```

#### Property Value
[Tizen.UI.LayoutDirection](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.LayoutDirection 'Tizen.UI.LayoutDirection')

<a name='Tizen.UI.Layouts.ILayout.LayoutParam'></a>

## ILayout.LayoutParam Property

Gets the attached LayoutParam for the layout.

```csharp
Tizen.UI.Layouts.LayoutParam LayoutParam { get; }
```

#### Property Value
[LayoutParam](Tizen.UI.Layouts.LayoutParam.md 'Tizen.UI.Layouts.LayoutParam')

<a name='Tizen.UI.Layouts.ILayout.Padding'></a>

## ILayout.Padding Property

Gets the padding of the layout.

```csharp
Tizen.UI.Thickness Padding { get; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')






























































