### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## InnerShadowTokenPropertyChangedEventArgs Class

Provides data for inner shadow token property changed events.

```csharp
public class InnerShadowTokenPropertyChangedEventArgs : Tizen.UI.ColorTokenPropertyChangedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs') &#129106; [ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs') &#129106; InnerShadowTokenPropertyChangedEventArgs

### Remarks
Extends [ColorTokenPropertyChangedEventArgs](Tizen.UI.ColorTokenPropertyChangedEventArgs.md 'Tizen.UI.ColorTokenPropertyChangedEventArgs') with inner shadow information.  
Uses singleton pattern for event argument instances.
### Properties

<a name='Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.Shadow'></a>

## InnerShadowTokenPropertyChangedEventArgs.Shadow Property

Gets or sets the inner shadow value of the changed property.

```csharp
public Tizen.UI.InnerShadow Shadow { get; set; }
```

#### Property Value
[InnerShadow](Tizen.UI.InnerShadow.md 'Tizen.UI.InnerShadow')  
The new inner shadow value.
### Methods

<a name='Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.InnerShadow)'></a>

## InnerShadowTokenPropertyChangedEventArgs.Create(View, string, InnerShadow) Method

Creates a new instance of [InnerShadowTokenPropertyChangedEventArgs](Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.InnerShadowTokenPropertyChangedEventArgs').

```csharp
public static Tizen.UI.InnerShadowTokenPropertyChangedEventArgs Create(Tizen.UI.View view, string name, Tizen.UI.InnerShadow shadow);
```
#### Parameters

<a name='Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.InnerShadow).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view associated with the property change.

<a name='Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.InnerShadow).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the changed property.

<a name='Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.Create(Tizen.UI.View,string,Tizen.UI.InnerShadow).shadow'></a>

`shadow` [InnerShadow](Tizen.UI.InnerShadow.md 'Tizen.UI.InnerShadow')

The new inner shadow value.

#### Returns
[InnerShadowTokenPropertyChangedEventArgs](Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.InnerShadowTokenPropertyChangedEventArgs')  
An initialized [InnerShadowTokenPropertyChangedEventArgs](Tizen.UI.InnerShadowTokenPropertyChangedEventArgs.md 'Tizen.UI.InnerShadowTokenPropertyChangedEventArgs') instance.






