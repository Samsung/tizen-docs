### [Tizen.UI.Visuals](Tizen.UI.Visuals.md 'Tizen.UI.Visuals')

## ViewExtensions Class

Extension methods for managing visual objects

```csharp
public static class ViewExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ViewExtensions
### Methods

<a name='Tizen.UI.Visuals.ViewExtensions.Add_T_(thisT,Tizen.UI.Visuals.VisualObject)'></a>

## ViewExtensions.Add&lt;T>(this T, VisualObject) Method

Adds a visual to the view.

```csharp
public static T Add&lt;T>(this T view, Tizen.UI.Visuals.VisualObject visual)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Visuals.ViewExtensions.Add_T_(thisT,Tizen.UI.Visuals.VisualObject).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.Visuals.ViewExtensions.Add_T_(thisT,Tizen.UI.Visuals.VisualObject).view'></a>

`view` [T](Tizen.UI.Visuals.ViewExtensions.md#Tizen.UI.Visuals.ViewExtensions.Add_T_(thisT,Tizen.UI.Visuals.VisualObject).T 'Tizen.UI.Visuals.ViewExtensions.Add&lt;T>(this T, Tizen.UI.Visuals.VisualObject).T')

The view to which the visual is added.

<a name='Tizen.UI.Visuals.ViewExtensions.Add_T_(thisT,Tizen.UI.Visuals.VisualObject).visual'></a>

`visual` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual to be added to the view.

#### Returns
[T](Tizen.UI.Visuals.ViewExtensions.md#Tizen.UI.Visuals.ViewExtensions.Add_T_(thisT,Tizen.UI.Visuals.VisualObject).T 'Tizen.UI.Visuals.ViewExtensions.Add&lt;T>(this T, Tizen.UI.Visuals.VisualObject).T')  
The view with the added visual.

<a name='Tizen.UI.Visuals.ViewExtensions.Remove(thisTizen.UI.View,Tizen.UI.Visuals.VisualObject)'></a>

## ViewExtensions.Remove(this View, VisualObject) Method

Removes the specified visual from the view.

```csharp
public static void Remove(this Tizen.UI.View view, Tizen.UI.Visuals.VisualObject visual);
```
#### Parameters

<a name='Tizen.UI.Visuals.ViewExtensions.Remove(thisTizen.UI.View,Tizen.UI.Visuals.VisualObject).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to remove the visual from.

<a name='Tizen.UI.Visuals.ViewExtensions.Remove(thisTizen.UI.View,Tizen.UI.Visuals.VisualObject).visual'></a>

`visual` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual to remove.

<a name='Tizen.UI.Visuals.ViewExtensions.Visuals(thisTizen.UI.View)'></a>

## ViewExtensions.Visuals(this View) Method

This method returns the VisualManager object associated with the given View.

```csharp
public static Tizen.UI.Visuals.VisualManager Visuals(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Visuals.ViewExtensions.Visuals(thisTizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The View object to retrieve the VisualManager from.

#### Returns
[VisualManager](Tizen.UI.Visuals.VisualManager.md 'Tizen.UI.Visuals.VisualManager')  
The VisualManager object associated with the given View.

























