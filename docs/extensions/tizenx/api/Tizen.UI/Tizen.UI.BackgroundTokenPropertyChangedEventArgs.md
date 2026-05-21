### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## BackgroundTokenPropertyChangedEventArgs Class

Provides data for background token property changed events.

```csharp
public class BackgroundTokenPropertyChangedEventArgs : Tizen.UI.TokenPropertyChangedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs') &#129106; BackgroundTokenPropertyChangedEventArgs

### Remarks
Extends [TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs') with background information.  
Uses singleton pattern for event argument instances.
### Properties

<a name='Tizen.UI.BackgroundTokenPropertyChangedEventArgs.Background'></a>

## BackgroundTokenPropertyChangedEventArgs.Background Property

Gets or sets the background value of the changed property.

```csharp
public Tizen.UI.Background Background { get; set; }
```

#### Property Value
[Background](Tizen.UI.Background.md 'Tizen.UI.Background')  
The new background value.
### Methods

<a name='Tizen.UI.BackgroundTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Background)'></a>

## BackgroundTokenPropertyChangedEventArgs.Create(View, string, Background) Method

Creates a new instance of [BackgroundTokenPropertyChangedEventArgs](Tizen.UI.BackgroundTokenPropertyChangedEventArgs.md 'Tizen.UI.BackgroundTokenPropertyChangedEventArgs').

```csharp
public static Tizen.UI.BackgroundTokenPropertyChangedEventArgs Create(Tizen.UI.View view, string name, Tizen.UI.Background background);
```
#### Parameters

<a name='Tizen.UI.BackgroundTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Background).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view associated with the property change.

<a name='Tizen.UI.BackgroundTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Background).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the changed property.

<a name='Tizen.UI.BackgroundTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Background).background'></a>

`background` [Background](Tizen.UI.Background.md 'Tizen.UI.Background')

The new background value.

#### Returns
[BackgroundTokenPropertyChangedEventArgs](Tizen.UI.BackgroundTokenPropertyChangedEventArgs.md 'Tizen.UI.BackgroundTokenPropertyChangedEventArgs')  
An initialized [BackgroundTokenPropertyChangedEventArgs](Tizen.UI.BackgroundTokenPropertyChangedEventArgs.md 'Tizen.UI.BackgroundTokenPropertyChangedEventArgs') instance.






