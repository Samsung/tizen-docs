### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ActionButton Class

A button that can be used in an AppBar.

```csharp
public class ActionButton : Tizen.UI.Components.Material.IconButton,
Tizen.UI.Components.Material.IAppBarContent
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; Tizen.UI.Components.Pressable &#129106; Tizen.UI.Components.Clickable &#129106; [IconButton](Tizen.UI.Components.Material.IconButton.md 'Tizen.UI.Components.Material.IconButton') &#129106; ActionButton

Implements [IAppBarContent](Tizen.UI.Components.Material.IAppBarContent.md 'Tizen.UI.Components.Material.IAppBarContent')
### Constructors

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton()'></a>

## ActionButton() Constructor

Constructs a button.

```csharp
public ActionButton();
```

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(string)'></a>

## ActionButton(string) Constructor

Constructs a button.

```csharp
public ActionButton(string iconResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(string).iconResourceUrl'></a>

`iconResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(string,Tizen.UI.Components.Material.IconButtonVariables)'></a>

## ActionButton(string, IconButtonVariables) Constructor

Constructs a button.

```csharp
public ActionButton(string iconResourceUrl, Tizen.UI.Components.Material.IconButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(string,Tizen.UI.Components.Material.IconButtonVariables).iconResourceUrl'></a>

`iconResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The resource url of the icon.

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(string,Tizen.UI.Components.Material.IconButtonVariables).variables'></a>

`variables` [IconButtonVariables](Tizen.UI.Components.Material.IconButtonVariables.md 'Tizen.UI.Components.Material.IconButtonVariables')

The variables to apply to the button.

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(Tizen.UI.Components.Material.IconButtonVariables)'></a>

## ActionButton(IconButtonVariables) Constructor

Constructs a button.

```csharp
public ActionButton(Tizen.UI.Components.Material.IconButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ActionButton.ActionButton(Tizen.UI.Components.Material.IconButtonVariables).variables'></a>

`variables` [IconButtonVariables](Tizen.UI.Components.Material.IconButtonVariables.md 'Tizen.UI.Components.Material.IconButtonVariables')

The variables to apply to the button.
### Methods

<a name='Tizen.UI.Components.Material.ActionButton.ApplyUnifiedContentColor(Tizen.UI.Color)'></a>

## ActionButton.ApplyUnifiedContentColor(Color) Method

Apply app bar unified content color.

```csharp
public void ApplyUnifiedContentColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ActionButton.ApplyUnifiedContentColor(Tizen.UI.Color).color'></a>

`color` Tizen.UI.Color

Implements [ApplyUnifiedContentColor(Color)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.ApplyUnifiedContentColor(Tizen.UI.Color) 'Tizen.UI.Components.Material.IAppBarContent.ApplyUnifiedContentColor(Tizen.UI.Color)')

<a name='Tizen.UI.Components.Material.ActionButton.OnAttached(Tizen.UI.Components.Material.AppBar)'></a>

## ActionButton.OnAttached(AppBar) Method

Called when the content is attached to AppBar.

```csharp
public virtual void OnAttached(Tizen.UI.Components.Material.AppBar appBar);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ActionButton.OnAttached(Tizen.UI.Components.Material.AppBar).appBar'></a>

`appBar` [AppBar](Tizen.UI.Components.Material.AppBar.md 'Tizen.UI.Components.Material.AppBar')

Implements [OnAttached(AppBar)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.OnAttached(Tizen.UI.Components.Material.AppBar) 'Tizen.UI.Components.Material.IAppBarContent.OnAttached(Tizen.UI.Components.Material.AppBar)')

<a name='Tizen.UI.Components.Material.ActionButton.OnDetached(Tizen.UI.Components.Material.AppBar)'></a>

## ActionButton.OnDetached(AppBar) Method

Called when the content is detected from AppBar.

```csharp
public virtual void OnDetached(Tizen.UI.Components.Material.AppBar appBar);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ActionButton.OnDetached(Tizen.UI.Components.Material.AppBar).appBar'></a>

`appBar` [AppBar](Tizen.UI.Components.Material.AppBar.md 'Tizen.UI.Components.Material.AppBar')

Implements [OnDetached(AppBar)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.OnDetached(Tizen.UI.Components.Material.AppBar) 'Tizen.UI.Components.Material.IAppBarContent.OnDetached(Tizen.UI.Components.Material.AppBar)')














































