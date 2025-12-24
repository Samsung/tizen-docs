### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## UIApplication Class

Represents a lite application tha has an UI screen.

```csharp
public class UIApplication
```

Inheritance [Tizen.Applications.CoreApplication](https://docs.microsoft.com/en-us/dotnet/api/Tizen.Applications.CoreApplication 'Tizen.Applications.CoreApplication') &#129106; UIApplication
### Constructors

<a name='Tizen.UI.UIApplication.UIApplication()'></a>

## UIApplication() Constructor

Initializes a new instance of the [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') class with the default window mode.

```csharp
public UIApplication();
```

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.Rect)'></a>

## UIApplication(Rect) Constructor

Initializes a new instance of the [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') class with the specified window bounds.

```csharp
public UIApplication(Tizen.UI.Rect windowBounds);
```
#### Parameters

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.Rect).windowBounds'></a>

`windowBounds` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The window bounds.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode)'></a>

## UIApplication(WindowMode) Constructor

Initializes a new instance of the [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') class with the specified window mode.

```csharp
public UIApplication(Tizen.UI.WindowMode mode);
```
#### Parameters

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode).mode'></a>

`mode` [WindowMode](Tizen.UI.WindowMode.md 'Tizen.UI.WindowMode')

The window mode.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,CoreTask)'></a>

## UIApplication(WindowMode, CoreTask) Constructor

Initializes a new instance of the [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') class with the specified window mode and core task.

```csharp
public UIApplication(Tizen.UI.WindowMode mode, CoreTask coreTask);
```
#### Parameters

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,CoreTask).mode'></a>

`mode` [WindowMode](Tizen.UI.WindowMode.md 'Tizen.UI.WindowMode')

The window mode of the application.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,CoreTask).coreTask'></a>

`coreTask` [Tizen.Applications.CoreTask](https://docs.microsoft.com/en-us/dotnet/api/Tizen.Applications.CoreTask 'Tizen.Applications.CoreTask')

The core task of the application.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect)'></a>

## UIApplication(WindowMode, Rect) Constructor

Initializes a new instance of the [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') class with the specified window mode and bounds.

```csharp
public UIApplication(Tizen.UI.WindowMode mode, Tizen.UI.Rect windowBounds);
```
#### Parameters

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect).mode'></a>

`mode` [WindowMode](Tizen.UI.WindowMode.md 'Tizen.UI.WindowMode')

The window mode.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect).windowBounds'></a>

`windowBounds` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The window bounds.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect,CoreTask)'></a>

## UIApplication(WindowMode, Rect, CoreTask) Constructor

Initializes a new instance of the [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') class with the specified window mode, bounds and core task.

```csharp
public UIApplication(Tizen.UI.WindowMode mode, Tizen.UI.Rect windowBounds, CoreTask coreTask);
```
#### Parameters

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect,CoreTask).mode'></a>

`mode` [WindowMode](Tizen.UI.WindowMode.md 'Tizen.UI.WindowMode')

The window mode of the application.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect,CoreTask).windowBounds'></a>

`windowBounds` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The window bounds of the application.

<a name='Tizen.UI.UIApplication.UIApplication(Tizen.UI.WindowMode,Tizen.UI.Rect,CoreTask).coreTask'></a>

`coreTask` [Tizen.Applications.CoreTask](https://docs.microsoft.com/en-us/dotnet/api/Tizen.Applications.CoreTask 'Tizen.Applications.CoreTask')

The core task of the application.
### Properties

<a name='Tizen.UI.UIApplication.Current'></a>

## UIApplication.Current Property

Gets the current instance of the LiteApplication class.

```csharp
public static Tizen.UI.UIApplication Current { get; set; }
```

#### Property Value
[UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication')

<a name='Tizen.UI.UIApplication.IsUIThread'></a>

## UIApplication.IsUIThread Property

Gets a value indicating whether the current thread is the UI thread.

```csharp
public bool IsUIThread { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.UIApplication.Windows'></a>

## UIApplication.Windows Property

Gets the list of created windows

```csharp
public static System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.Window> Windows { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Window](Tizen.UI.Window.md 'Tizen.UI.Window')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')
### Methods

<a name='Tizen.UI.UIApplication.PostToUI(System.Action)'></a>

## UIApplication.PostToUI(Action) Method

Posts the specified action to the UI thread.

```csharp
public void PostToUI(System.Action action);
```
#### Parameters

<a name='Tizen.UI.UIApplication.PostToUI(System.Action).action'></a>

`action` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The action to be executed on the UI thread.

<a name='Tizen.UI.UIApplication.Run(string[])'></a>

## UIApplication.Run(string[]) Method

Runs the UI application's main loop.

```csharp
public override void Run(string[] args);
```
#### Parameters

<a name='Tizen.UI.UIApplication.Run(string[]).args'></a>

`args` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

Arguments from the commandline.
### Events

<a name='Tizen.UI.UIApplication.Paused'></a>

## UIApplication.Paused Event

Occurs whenever the application is paused.

```csharp
public event EventHandler Paused;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.UIApplication.Resumed'></a>

## UIApplication.Resumed Event

Occurs whenever the application is resumed.

```csharp
public event EventHandler Resumed;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')




