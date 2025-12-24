### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## MoreButton Class

MoreVertical button is a button that pops up a contextual menu within a given navigator when clicked.  
If no navigator is specified it will use default navigator.

```csharp
public class MoreButton : Tizen.UI.Components.Material.IconButton,
Tizen.UI.Components.Material.IAppBarContent
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Pressable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Pressable 'Tizen.UI.Components.Pressable') &#129106; [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') &#129106; [IconButton](Tizen.UI.Components.Material.IconButton.md 'Tizen.UI.Components.Material.IconButton') &#129106; MoreButton

Implements [IAppBarContent](Tizen.UI.Components.Material.IAppBarContent.md 'Tizen.UI.Components.Material.IAppBarContent')
### Constructors

<a name='Tizen.UI.Components.Material.MoreButton.MoreButton()'></a>

## MoreButton() Constructor

Constructs a button with icon resource url.

```csharp
public MoreButton();
```

<a name='Tizen.UI.Components.Material.MoreButton.MoreButton(Tizen.UI.Components.Material.IconButtonVariables)'></a>

## MoreButton(IconButtonVariables) Constructor

Constructs a button with icon resource url.

```csharp
public MoreButton(Tizen.UI.Components.Material.IconButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.MoreButton.MoreButton(Tizen.UI.Components.Material.IconButtonVariables).variables'></a>

`variables` [IconButtonVariables](Tizen.UI.Components.Material.IconButtonVariables.md 'Tizen.UI.Components.Material.IconButtonVariables')
### Properties

<a name='Tizen.UI.Components.Material.MoreButton.ModalContent'></a>

## MoreButton.ModalContent Property

Gets or sets the modal content to be shown when clicked.

```csharp
public Tizen.UI.Components.IAnchoredModal ModalContent { get; set; }
```

#### Property Value
[Tizen.UI.Components.IAnchoredModal](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IAnchoredModal 'Tizen.UI.Components.IAnchoredModal')
### Methods

<a name='Tizen.UI.Components.Material.MoreButton.ApplyUnifiedContentColor(Tizen.UI.Color)'></a>

## MoreButton.ApplyUnifiedContentColor(Color) Method

Apply app bar unified content color.

```csharp
public void ApplyUnifiedContentColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.MoreButton.ApplyUnifiedContentColor(Tizen.UI.Color).color'></a>

`color` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

Implements [ApplyUnifiedContentColor(Color)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.ApplyUnifiedContentColor(Tizen.UI.Color) 'Tizen.UI.Components.Material.IAppBarContent.ApplyUnifiedContentColor(Tizen.UI.Color)')

<a name='Tizen.UI.Components.Material.MoreButton.OnAttached(Tizen.UI.Components.Material.AppBar)'></a>

## MoreButton.OnAttached(AppBar) Method

Called when the content is attached to AppBar.

```csharp
public virtual void OnAttached(Tizen.UI.Components.Material.AppBar appBar);
```
#### Parameters

<a name='Tizen.UI.Components.Material.MoreButton.OnAttached(Tizen.UI.Components.Material.AppBar).appBar'></a>

`appBar` [AppBar](Tizen.UI.Components.Material.AppBar.md 'Tizen.UI.Components.Material.AppBar')

Implements [OnAttached(AppBar)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.OnAttached(Tizen.UI.Components.Material.AppBar) 'Tizen.UI.Components.Material.IAppBarContent.OnAttached(Tizen.UI.Components.Material.AppBar)')

<a name='Tizen.UI.Components.Material.MoreButton.OnDetached(Tizen.UI.Components.Material.AppBar)'></a>

## MoreButton.OnDetached(AppBar) Method

Called when the content is detected from AppBar.

```csharp
public virtual void OnDetached(Tizen.UI.Components.Material.AppBar appBar);
```
#### Parameters

<a name='Tizen.UI.Components.Material.MoreButton.OnDetached(Tizen.UI.Components.Material.AppBar).appBar'></a>

`appBar` [AppBar](Tizen.UI.Components.Material.AppBar.md 'Tizen.UI.Components.Material.AppBar')

Implements [OnDetached(AppBar)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.OnDetached(Tizen.UI.Components.Material.AppBar) 'Tizen.UI.Components.Material.IAppBarContent.OnDetached(Tizen.UI.Components.Material.AppBar)')













































