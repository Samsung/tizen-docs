### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## CircleButton Class

A [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') component containing single icon.  
The main difference from an [IconButton](Tizen.UI.Components.Material.IconButton.md 'Tizen.UI.Components.Material.IconButton') is that it can have a [Tizen.UI.Components.UIState.Progressing](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.UIState.Progressing 'Tizen.UI.Components.UIState.Progressing') like [Button](Tizen.UI.Components.Material.Button.md 'Tizen.UI.Components.Material.Button').

```csharp
public class CircleButton : Tizen.UI.Components.Clickable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Pressable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Pressable 'Tizen.UI.Components.Pressable') &#129106; [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') &#129106; CircleButton
### Constructors

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton()'></a>

## CircleButton() Constructor

Constructs an empty button.

```csharp
public CircleButton();
```

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(string)'></a>

## CircleButton(string) Constructor

Constructs a button with icon resource url.

```csharp
public CircleButton(string iconResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(string).iconResourceUrl'></a>

`iconResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(string,Tizen.UI.Components.Material.CircleButtonVariables)'></a>

## CircleButton(string, CircleButtonVariables) Constructor

Constructs a button with icon resource url.

```csharp
public CircleButton(string iconResourceUrl, Tizen.UI.Components.Material.CircleButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(string,Tizen.UI.Components.Material.CircleButtonVariables).iconResourceUrl'></a>

`iconResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(string,Tizen.UI.Components.Material.CircleButtonVariables).variables'></a>

`variables` [CircleButtonVariables](Tizen.UI.Components.Material.CircleButtonVariables.md 'Tizen.UI.Components.Material.CircleButtonVariables')

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(Tizen.UI.Components.Material.CircleButtonVariables)'></a>

## CircleButton(CircleButtonVariables) Constructor

Constructs an empty button.

```csharp
public CircleButton(Tizen.UI.Components.Material.CircleButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.CircleButton.CircleButton(Tizen.UI.Components.Material.CircleButtonVariables).variables'></a>

`variables` [CircleButtonVariables](Tizen.UI.Components.Material.CircleButtonVariables.md 'Tizen.UI.Components.Material.CircleButtonVariables')
### Properties

<a name='Tizen.UI.Components.Material.CircleButton.IsProgressing'></a>

## CircleButton.IsProgressing Property

Gets or sets whether the progress mode is enabled.

```csharp
public bool IsProgressing { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.CircleButton.Padding'></a>

## CircleButton.Padding Property

Gets or sets the padding of button.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')
### Methods

<a name='Tizen.UI.Components.Material.CircleButton.GetTouchEffectTarget()'></a>

## CircleButton.GetTouchEffectTarget() Method

Get the target view to apply feedback.

```csharp
public override Tizen.UI.View GetTouchEffectTarget();
```

Implements [GetTouchEffectTarget()](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget')

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')













































