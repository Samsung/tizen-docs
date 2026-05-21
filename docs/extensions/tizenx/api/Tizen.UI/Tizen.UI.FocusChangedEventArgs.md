### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## FocusChangedEventArgs Class

Provides data for the [FocusChanged](Tizen.UI.FocusManager.md#Tizen.UI.FocusManager.FocusChanged 'Tizen.UI.FocusManager.FocusChanged') event.

```csharp
public class FocusChangedEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; FocusChangedEventArgs
### Properties

<a name='Tizen.UI.FocusChangedEventArgs.FocusedView'></a>

## FocusChangedEventArgs.FocusedView Property

Gets or sets the view that currently has focus.

```csharp
public Tizen.UI.View FocusedView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.FocusChangedEventArgs.PreviousFocusedView'></a>

## FocusChangedEventArgs.PreviousFocusedView Property

Gets or sets the view that previously had focus.

```csharp
public Tizen.UI.View PreviousFocusedView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')






