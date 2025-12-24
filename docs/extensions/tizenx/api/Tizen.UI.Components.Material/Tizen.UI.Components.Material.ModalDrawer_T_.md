### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ModalDrawer&lt;T> Class

Canonical layout container that provides selectable items area in left side and content area in right side.  
The items area can be hidden.

```csharp
public class ModalDrawer&lt;T> : Tizen.UI.Components.Material.Drawer&lt;T>
    where T : Tizen.UI.ContentView, Tizen.UI.Components.IGroupSelectable
```
#### Type parameters

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Material.Drawer&lt;](Tizen.UI.Components.Material.Drawer_T_.md 'Tizen.UI.Components.Material.Drawer&lt;T>')[T](Tizen.UI.Components.Material.ModalDrawer_T_.md#Tizen.UI.Components.Material.ModalDrawer_T_.T 'Tizen.UI.Components.Material.ModalDrawer&lt;T>.T')[&gt;](Tizen.UI.Components.Material.Drawer_T_.md 'Tizen.UI.Components.Material.Drawer&lt;T>') &#129106; ModalDrawer&lt;T>

Derived  
&#8627; [ModalDrawer](Tizen.UI.Components.Material.ModalDrawer.md 'Tizen.UI.Components.Material.ModalDrawer')
### Constructors

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.ModalDrawer()'></a>

## ModalDrawer() Constructor

Initializes a new instance of the Drawer class with default settings.

```csharp
public ModalDrawer();
```

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.ModalDrawer(Tizen.UI.Components.Material.ModalDrawerVariables)'></a>

## ModalDrawer(ModalDrawerVariables) Constructor

Initializes a new instance of the Drawer class with specified variables.

```csharp
public ModalDrawer(Tizen.UI.Components.Material.ModalDrawerVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.ModalDrawer(Tizen.UI.Components.Material.ModalDrawerVariables).variables'></a>

`variables` [ModalDrawerVariables](Tizen.UI.Components.Material.ModalDrawerVariables.md 'Tizen.UI.Components.Material.ModalDrawerVariables')

The DrawerVariables object containing configuration for the drawer.
### Properties

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.Content'></a>

## ModalDrawer&lt;T>.Content Property

Gets or sets the content of the Drawer.

```csharp
public override Tizen.UI.View Content { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.Close()'></a>

## ModalDrawer&lt;T>.Close() Method

Closes the drawer if it is open and is not of the static type.

```csharp
public void Close();
```

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.Open()'></a>

## ModalDrawer&lt;T>.Open() Method

Opens the drawer if it is not already open and is not of the static type.

```csharp
public void Open();
```

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.Toggle(Tizen.UI.KeyDeviceClass)'></a>

## ModalDrawer&lt;T>.Toggle(KeyDeviceClass) Method

Toggles the state of the drawer between open and closed.

```csharp
public void Toggle(Tizen.UI.KeyDeviceClass device=Tizen.UI.KeyDeviceClass.None);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ModalDrawer_T_.Toggle(Tizen.UI.KeyDeviceClass).device'></a>

`device` [Tizen.UI.KeyDeviceClass](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.KeyDeviceClass 'Tizen.UI.KeyDeviceClass')













































