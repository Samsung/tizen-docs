### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## AccessibilityManager Class

Provides accessibility features for the application.

```csharp
public static class AccessibilityManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AccessibilityManager
### Properties

<a name='Tizen.UI.AccessibilityManager.IsAccessibilityEnabled'></a>

## AccessibilityManager.IsAccessibilityEnabled Property

Gets a value indicating whether accessibility is enabled.

```csharp
public static bool IsAccessibilityEnabled { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.AccessibilityManager.IsScreenReaderEnabled'></a>

## AccessibilityManager.IsScreenReaderEnabled Property

Gets a value indicating whether a screen reader is enabled.

```csharp
public static bool IsScreenReaderEnabled { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.AccessibilityManager.AnnounceAsync(string,bool)'></a>

## AccessibilityManager.AnnounceAsync(string, bool) Method

Announces the specified sentence.

```csharp
public static System.Threading.Tasks.Task&lt;Tizen.UI.AnnouncementState> AnnounceAsync(string sentence, bool discardable);
```
#### Parameters

<a name='Tizen.UI.AccessibilityManager.AnnounceAsync(string,bool).sentence'></a>

`sentence` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The sentence to announce.

<a name='Tizen.UI.AccessibilityManager.AnnounceAsync(string,bool).discardable'></a>

`discardable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the announcement can be discarded by the user.

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[AnnouncementState](Tizen.UI.AnnouncementState.md 'Tizen.UI.AnnouncementState')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
A task that represents the announcement operation.

<a name='Tizen.UI.AccessibilityManager.CancelAnnouncement()'></a>

## AccessibilityManager.CancelAnnouncement() Method

Cancels the current announcement.

```csharp
public static void CancelAnnouncement();
```

<a name='Tizen.UI.AccessibilityManager.GetHighlighted()'></a>

## AccessibilityManager.GetHighlighted() Method

Gets the currently highlighted view.

```csharp
public static Tizen.UI.View GetHighlighted();
```

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The currently highlighted view.

<a name='Tizen.UI.AccessibilityManager.SendChangedNameEvent(Tizen.UI.View)'></a>

## AccessibilityManager.SendChangedNameEvent(View) Method

Sends an accessibility event indicating that the name has changed.

```csharp
public static void SendChangedNameEvent(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.AccessibilityManager.SendChangedNameEvent(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The target view whose name change event will be sent.

### Remarks
This function notifies screen-readers that the accessible name of the specified view has been updated.

<a name='Tizen.UI.AccessibilityManager.SendShowingEvent(Tizen.UI.View,bool)'></a>

## AccessibilityManager.SendShowingEvent(View, bool) Method

Sends an accessibility event indicating that the showing state of the specified view.

```csharp
public static void SendShowingEvent(Tizen.UI.View view, bool isShowing);
```
#### Parameters

<a name='Tizen.UI.AccessibilityManager.SendShowingEvent(Tizen.UI.View,bool).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The target view whose showing state change will be reported.

<a name='Tizen.UI.AccessibilityManager.SendShowingEvent(Tizen.UI.View,bool).isShowing'></a>

`isShowing` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A boolean value indicating whether the view is now visible (`true`) or hidden(`false`).

### Remarks
This function notifies screen-readers whether the target view has become visible (`true`) or hidden(`false`).

<a name='Tizen.UI.AccessibilityManager.SetHighlight(Tizen.UI.View)'></a>

## AccessibilityManager.SetHighlight(View) Method

Sets the highlight to the specified view.

```csharp
public static bool SetHighlight(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.AccessibilityManager.SetHighlight(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to set the highlight indicator to. If it is null, the existing highlight will be cleared and return true.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the focus is set successfully, false otherwise.

<a name='Tizen.UI.AccessibilityManager.SetHighlightIndicator(Tizen.UI.View)'></a>

## AccessibilityManager.SetHighlightIndicator(View) Method

Sets the highlight indicator to the specified view.

```csharp
public static void SetHighlightIndicator(Tizen.UI.View indicator);
```
#### Parameters

<a name='Tizen.UI.AccessibilityManager.SetHighlightIndicator(Tizen.UI.View).indicator'></a>

`indicator` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to set the highlight indicator to.

<a name='Tizen.UI.AccessibilityManager.SetReadingInfo(Tizen.UI.View,Tizen.UI.AccessibilityReadingInfo)'></a>

## AccessibilityManager.SetReadingInfo(View, AccessibilityReadingInfo) Method

Sets the reading information type of the specified view to name.

```csharp
public static void SetReadingInfo(Tizen.UI.View view, Tizen.UI.AccessibilityReadingInfo readingInfo);
```
#### Parameters

<a name='Tizen.UI.AccessibilityManager.SetReadingInfo(Tizen.UI.View,Tizen.UI.AccessibilityReadingInfo).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The target view whose reading information type will be set to name

<a name='Tizen.UI.AccessibilityManager.SetReadingInfo(Tizen.UI.View,Tizen.UI.AccessibilityReadingInfo).readingInfo'></a>

`readingInfo` [AccessibilityReadingInfo](Tizen.UI.AccessibilityReadingInfo.md 'Tizen.UI.AccessibilityReadingInfo')

The reading information type will be set

### Remarks
This function configures the accessibility reading behavior so that   
screen readers announce the view's name when the view receives accessibility focus.
### Events

<a name='Tizen.UI.AccessibilityManager.AccessibilityStateChanged'></a>

## AccessibilityManager.AccessibilityStateChanged Event

Occurs when the accessibility state changes.

```csharp
public static event EventHandler AccessibilityStateChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.AccessibilityManager.ScreenReaderStateChanged'></a>

## AccessibilityManager.ScreenReaderStateChanged Event

Occurs when the screen reader state changes.

```csharp
public static event EventHandler ScreenReaderStateChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






