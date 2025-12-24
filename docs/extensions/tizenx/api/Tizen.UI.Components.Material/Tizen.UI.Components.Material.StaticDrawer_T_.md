### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## StaticDrawer&lt;T> Class

Canonical layout container that provides selectable items area in left side and content area in right side.

```csharp
public class StaticDrawer&lt;T> : Tizen.UI.Components.Material.Drawer&lt;T>
    where T : Tizen.UI.View, Tizen.UI.Components.IGroupSelectable
```
#### Type parameters

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Material.Drawer&lt;](Tizen.UI.Components.Material.Drawer_T_.md 'Tizen.UI.Components.Material.Drawer&lt;T>')[T](Tizen.UI.Components.Material.StaticDrawer_T_.md#Tizen.UI.Components.Material.StaticDrawer_T_.T 'Tizen.UI.Components.Material.StaticDrawer&lt;T>.T')[&gt;](Tizen.UI.Components.Material.Drawer_T_.md 'Tizen.UI.Components.Material.Drawer&lt;T>') &#129106; StaticDrawer&lt;T>

Derived  
&#8627; [StaticDrawer](Tizen.UI.Components.Material.StaticDrawer.md 'Tizen.UI.Components.Material.StaticDrawer')
### Constructors

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.StaticDrawer()'></a>

## StaticDrawer() Constructor

Initializes a new instance of the Drawer class with default settings.

```csharp
public StaticDrawer();
```

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.StaticDrawer(Tizen.UI.Components.Material.StaticDrawerVariables)'></a>

## StaticDrawer(StaticDrawerVariables) Constructor

Initializes a new instance of the Drawer class with specified variables.

```csharp
public StaticDrawer(Tizen.UI.Components.Material.StaticDrawerVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.StaticDrawer(Tizen.UI.Components.Material.StaticDrawerVariables).variables'></a>

`variables` [StaticDrawerVariables](Tizen.UI.Components.Material.StaticDrawerVariables.md 'Tizen.UI.Components.Material.StaticDrawerVariables')

The DrawerVariables object containing configuration for the drawer.
### Properties

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.Content'></a>

## StaticDrawer&lt;T>.Content Property

Gets or sets the content of the Drawer.

```csharp
public override Tizen.UI.View Content { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.Measure(float,float)'></a>

## StaticDrawer&lt;T>.Measure(float, float) Method

Measures the size requirements of the view for the given constraints.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size requirements of the view.

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.SwapContent(Tizen.UI.View)'></a>

## StaticDrawer&lt;T>.SwapContent(View) Method

Sets a content to be shown with the content swap animation.  
If current content is null, it will not show the content swap animation.

```csharp
public System.Threading.Tasks.Task SwapContent(Tizen.UI.View newContent);
```
#### Parameters

<a name='Tizen.UI.Components.Material.StaticDrawer_T_.SwapContent(Tizen.UI.View).newContent'></a>

`newContent` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

### Remarks
For the continuation task, please specify [System.Threading.Tasks.TaskScheduler](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.TaskScheduler 'System.Threading.Tasks.TaskScheduler') as the current synchronization context to ensure that the continuation runs on the UI thread.  
For example,  
  
```csharp  
staticDrawer.SwapContent(newContent).ContinueWith(finishedCallback, TaskScheduler.FromCurrentSynchronizationContext());  
```













































