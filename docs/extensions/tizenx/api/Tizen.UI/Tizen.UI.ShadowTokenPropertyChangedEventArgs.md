### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ShadowTokenPropertyChangedEventArgs Class

Provides data for shadow token property changed events.

```csharp
public class ShadowTokenPropertyChangedEventArgs : Tizen.UI.ColorTokenPropertyChangedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs') &#129106; [ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs') &#129106; ShadowTokenPropertyChangedEventArgs

### Remarks
Extends [ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs') with shadow information.  
Uses singleton pattern for event argument instances.
### Properties

<a name='Tizen.UI.ShadowTokenPropertyChangedEventArgs.Shadow'></a>

## ShadowTokenPropertyChangedEventArgs.Shadow Property

Gets or sets the shadow value of the changed property.

```csharp
public Tizen.UI.Shadow Shadow { get; set; }
```

#### Property Value
[Shadow](Tizen.UI.Shadow.md 'Tizen.UI.Shadow')  
The new shadow value.
### Methods

<a name='Tizen.UI.ShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Shadow)'></a>

## ShadowTokenPropertyChangedEventArgs.Create(View, string, Shadow) Method

Creates a new instance of [ShadowTokenPropertyChangedEventArgs](Tizen.UI.ShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.ShadowTokenPropertyChangedEventArgs').

```csharp
public static Tizen.UI.ShadowTokenPropertyChangedEventArgs Create(Tizen.UI.View view, string name, Tizen.UI.Shadow shadow);
```
#### Parameters

<a name='Tizen.UI.ShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Shadow).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view associated with the property change.

<a name='Tizen.UI.ShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Shadow).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the changed property.

<a name='Tizen.UI.ShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Shadow).shadow'></a>

`shadow` [Shadow](Tizen.UI.Shadow.md 'Tizen.UI.Shadow')

The new shadow value.

#### Returns
[ShadowTokenPropertyChangedEventArgs](Tizen.UI.ShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.ShadowTokenPropertyChangedEventArgs')  
An initialized [ShadowTokenPropertyChangedEventArgs](Tizen.UI.ShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.ShadowTokenPropertyChangedEventArgs') instance.






