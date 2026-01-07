### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ColorTokenPropertyChangedEventArgs Class

Provides data for color token property changed events.

```csharp
public class ColorTokenPropertyChangedEventArgs : Tizen.UI.TokenPropertyChangedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs') &#129106; ColorTokenPropertyChangedEventArgs

Derived  
&#8627; [InnerShadowTokenPropertyChangedEventArgs](Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.InnerShadowTokenPropertyChangedEventArgs')  
&#8627; [ShadowTokenPropertyChangedEventArgs](Tizen.UI.ShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.ShadowTokenPropertyChangedEventArgs')

### Remarks
Extends [TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs') with color information.  
Uses singleton pattern for event argument instances.
### Properties

<a name='Tizen.UI.ColorTokenPropertyChangedEventArgs.Color'></a>

## ColorTokenPropertyChangedEventArgs.Color Property

Gets or sets the color value of the changed property.

```csharp
public Tizen.UI.Color Color { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The new color value.
### Methods

<a name='Tizen.UI.ColorTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Color)'></a>

## ColorTokenPropertyChangedEventArgs.Create(View, string, Color) Method

Creates a new instance of [ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs').

```csharp
public static Tizen.UI.ColorTokenPropertyChangedEventArgs Create(Tizen.UI.View view, string name, Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.ColorTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Color).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view associated with the property change.

<a name='Tizen.UI.ColorTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Color).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the changed property.

<a name='Tizen.UI.ColorTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The new color value.

#### Returns
[ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs')  
An initialized [ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs') instance.






