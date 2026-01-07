### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## BindingExtensions Class

Provides extension methods for binding properties of a view model to a view.

```csharp
public static class BindingExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; BindingExtensions
### Methods

<a name='Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string)'></a>

## BindingExtensions.Bind&lt;TView,TProperty>(this TView, BindingProperty&lt;TView,TProperty>, string) Method

Binds the specified property of the view to the specified path in the view model.

```csharp
public static TView Bind&lt;TView,TProperty>(this TView view, Tizen.UI.BindingProperty&lt;TView,TProperty> property, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).TProperty'></a>

`TProperty`

The type of the property.
#### Parameters

<a name='Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.Bind&lt;TView,TProperty>(this TView, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).property'></a>

`property` [Tizen.UI.BindingProperty&lt;](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.Bind&lt;TView,TProperty>(this TView, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TView')[,](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')[TProperty](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).TProperty 'Tizen.UI.BindingExtensions.Bind&lt;TView,TProperty>(this TView, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TProperty')[&gt;](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')

The property to bind.

<a name='Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.Bind_TView,TProperty_(thisTView,Tizen.UI.BindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.Bind&lt;TView,TProperty>(this TView, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TView')  
The view with the property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindBackgroundColor_TView_(thisTView,string)'></a>

## BindingExtensions.BindBackgroundColor&lt;TView>(this TView, string) Method

Binds the [BackgroundColor](Tizen.UI.View.md#Tizen.UI.View.BackgroundColor 'Tizen.UI.View.BackgroundColor') property of the view to the specified path in the view model.

```csharp
public static TView BindBackgroundColor&lt;TView>(this TView view, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindBackgroundColor_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindBackgroundColor_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindBackgroundColor_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindBackgroundColor&lt;TView>(this TView, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindBackgroundColor_TView_(thisTView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindBackgroundColor_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindBackgroundColor&lt;TView>(this TView, string).TView')  
The view with the background color property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindFontSize_TText_(thisTText,string)'></a>

## BindingExtensions.BindFontSize&lt;TText>(this TText, string) Method

Binds the [FontSize](Tizen.UI.IText.md#Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize') property of the view to the specified path in the view model.

```csharp
public static TText BindFontSize&lt;TText>(this TText view, string path)
    where TText : Tizen.UI.View, Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindFontSize_TText_(thisTText,string).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindFontSize_TText_(thisTText,string).view'></a>

`view` [TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindFontSize_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindFontSize&lt;TText>(this TText, string).TText')

The text view to set the font size for.

<a name='Tizen.UI.BindingExtensions.BindFontSize_TText_(thisTText,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the font size property in the data context.

#### Returns
[TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindFontSize_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindFontSize&lt;TText>(this TText, string).TText')  
The text view with the font size property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindHeight_TView_(thisTView,string)'></a>

## BindingExtensions.BindHeight&lt;TView>(this TView, string) Method

Binds the [Height](Tizen.UI.View.md#Tizen.UI.View.Height 'Tizen.UI.View.Height') property of the view to the specified path in the view model.

```csharp
public static TView BindHeight&lt;TView>(this TView view, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindHeight_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindHeight_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindHeight_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindHeight&lt;TView>(this TView, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindHeight_TView_(thisTView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindHeight_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindHeight&lt;TView>(this TView, string).TView')  
The view with the height property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_)'></a>

## BindingExtensions.BindingSession&lt;T,TViewModel>(this T, BindingSession&lt;TViewModel>) Method

Sets the binding session for the specified view.

```csharp
public static T BindingSession&lt;T,TViewModel>(this T view, Tizen.UI.BindingSession&lt;TViewModel> session)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).T'></a>

`T`

The type of the view model.

<a name='Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).TViewModel'></a>

`TViewModel`
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).view'></a>

`view` [T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).T 'Tizen.UI.BindingExtensions.BindingSession&lt;T,TViewModel>(this T, Tizen.UI.BindingSession&lt;TViewModel>).T')

The view.

<a name='Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).session'></a>

`session` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[TViewModel](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).TViewModel 'Tizen.UI.BindingExtensions.BindingSession&lt;T,TViewModel>(this T, Tizen.UI.BindingSession&lt;TViewModel>).TViewModel')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The binding session.

#### Returns
[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindingSession_T,TViewModel_(thisT,Tizen.UI.BindingSession_TViewModel_).T 'Tizen.UI.BindingExtensions.BindingSession&lt;T,TViewModel>(this T, Tizen.UI.BindingSession&lt;TViewModel>).T')  
The view.

<a name='Tizen.UI.BindingExtensions.BindingSession_TViewModel_(thisTizen.UI.View)'></a>

## BindingExtensions.BindingSession&lt;TViewModel>(this View) Method

Gets the binding session for the specified view.

```csharp
public static Tizen.UI.BindingSession&lt;TViewModel> BindingSession&lt;TViewModel>(this Tizen.UI.View view);
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindingSession_TViewModel_(thisTizen.UI.View).TViewModel'></a>

`TViewModel`

The type of the view model.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindingSession_TViewModel_(thisTizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view.

#### Returns
[Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[TViewModel](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindingSession_TViewModel_(thisTizen.UI.View).TViewModel 'Tizen.UI.BindingExtensions.BindingSession&lt;TViewModel>(this Tizen.UI.View).TViewModel')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')  
The binding session.

<a name='Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string)'></a>

## BindingExtensions.BindLocalizedResource&lt;T>(this T, Action&lt;T,string>, string) Method

Binds the localized resource of the given view to the specified path.

```csharp
public static T BindLocalizedResource&lt;T>(this T view, System.Action&lt;T,string> setter, string path)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).view'></a>

`view` [T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).T 'Tizen.UI.BindingExtensions.BindLocalizedResource&lt;T>(this T, System.Action&lt;T,string>, string).T')

The view to bind.

<a name='Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).T 'Tizen.UI.BindingExtensions.BindLocalizedResource&lt;T>(this T, System.Action&lt;T,string>, string).T')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The setter method to set the localized resource.

<a name='Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the localized resource.

#### Returns
[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedResource_T_(thisT,System.Action_T,string_,string).T 'Tizen.UI.BindingExtensions.BindLocalizedResource&lt;T>(this T, System.Action&lt;T,string>, string).T')  
The view itself.

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager)'></a>

## BindingExtensions.BindLocalizedText&lt;T>(this T, Action&lt;T,string>, string, ResourceManager) Method

Binds the localized text of the given view to the specified key.

```csharp
public static T BindLocalizedText&lt;T>(this T view, System.Action&lt;T,string> setter, string key, System.Resources.ResourceManager resourceManager=null)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).view'></a>

`view` [T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).T 'Tizen.UI.BindingExtensions.BindLocalizedText&lt;T>(this T, System.Action&lt;T,string>, string, System.Resources.ResourceManager).T')

The view to bind.

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).T 'Tizen.UI.BindingExtensions.BindLocalizedText&lt;T>(this T, System.Action&lt;T,string>, string, System.Resources.ResourceManager).T')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The setter method to set the localized text.

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized text.

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized text.

#### Returns
[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedText_T_(thisT,System.Action_T,string_,string,System.Resources.ResourceManager).T 'Tizen.UI.BindingExtensions.BindLocalizedText&lt;T>(this T, System.Action&lt;T,string>, string, System.Resources.ResourceManager).T')  
The view itself.

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager)'></a>

## BindingExtensions.BindLocalizedText&lt;TText>(this TText, string, ResourceManager) Method

Binds the localized text of the given [IText](Tizen.UI.IText.md 'Tizen.UI.IText') to the specified key.

```csharp
public static TText BindLocalizedText&lt;TText>(this TText view, string key, System.Resources.ResourceManager resourceManager=null)
    where TText : class, Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager).view'></a>

`view` [TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.BindingExtensions.BindLocalizedText&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized text.

<a name='Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized text.

#### Returns
[TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindLocalizedText_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.BindingExtensions.BindLocalizedText&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')  
The text view itself.

<a name='Tizen.UI.BindingExtensions.BindMultipliedColor_TImageView_(thisTImageView,string)'></a>

## BindingExtensions.BindMultipliedColor&lt;TImageView>(this TImageView, string) Method

Binds the multiplied color of the given [ImageView](Tizen.UI.ImageView.md 'Tizen.UI.ImageView') to the specified path.

```csharp
public static TImageView BindMultipliedColor&lt;TImageView>(this TImageView imageView, string path)
    where TImageView : Tizen.UI.ImageView;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindMultipliedColor_TImageView_(thisTImageView,string).TImageView'></a>

`TImageView`

The type of the image view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindMultipliedColor_TImageView_(thisTImageView,string).imageView'></a>

`imageView` [TImageView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindMultipliedColor_TImageView_(thisTImageView,string).TImageView 'Tizen.UI.BindingExtensions.BindMultipliedColor&lt;TImageView>(this TImageView, string).TImageView')

The image view to bind.

<a name='Tizen.UI.BindingExtensions.BindMultipliedColor_TImageView_(thisTImageView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the resource.

#### Returns
[TImageView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindMultipliedColor_TImageView_(thisTImageView,string).TImageView 'Tizen.UI.BindingExtensions.BindMultipliedColor&lt;TImageView>(this TImageView, string).TImageView')  
The image view with the resource url property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindResourceUrl_TImageView_(thisTImageView,string)'></a>

## BindingExtensions.BindResourceUrl&lt;TImageView>(this TImageView, string) Method

Binds the resource URL of the given [ImageView](Tizen.UI.ImageView.md 'Tizen.UI.ImageView') to the specified path.

```csharp
public static TImageView BindResourceUrl&lt;TImageView>(this TImageView imageView, string path)
    where TImageView : Tizen.UI.ImageView;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindResourceUrl_TImageView_(thisTImageView,string).TImageView'></a>

`TImageView`

The type of the image view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindResourceUrl_TImageView_(thisTImageView,string).imageView'></a>

`imageView` [TImageView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindResourceUrl_TImageView_(thisTImageView,string).TImageView 'Tizen.UI.BindingExtensions.BindResourceUrl&lt;TImageView>(this TImageView, string).TImageView')

The image view to bind.

<a name='Tizen.UI.BindingExtensions.BindResourceUrl_TImageView_(thisTImageView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the resource.

#### Returns
[TImageView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindResourceUrl_TImageView_(thisTImageView,string).TImageView 'Tizen.UI.BindingExtensions.BindResourceUrl&lt;TImageView>(this TImageView, string).TImageView')  
The image view with the resource url property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindText_TText_(thisTText,string)'></a>

## BindingExtensions.BindText&lt;TText>(this TText, string) Method

Binds the [Text](Tizen.UI.IText.md#Tizen.UI.IText.Text 'Tizen.UI.IText.Text') property of the view to the specified path in the view model.

```csharp
public static TText BindText&lt;TText>(this TText view, string path)
    where TText : Tizen.UI.View, Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindText_TText_(thisTText,string).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindText_TText_(thisTText,string).view'></a>

`view` [TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindText_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindText&lt;TText>(this TText, string).TText')

The text view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindText_TText_(thisTText,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindText_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindText&lt;TText>(this TText, string).TText')  
The text view with the text property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindTextColor_TText_(thisTText,string)'></a>

## BindingExtensions.BindTextColor&lt;TText>(this TText, string) Method

Binds the [TextColor](Tizen.UI.IText.md#Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor') property of the view to the specified path in the view model.

```csharp
public static TText BindTextColor&lt;TText>(this TText view, string path)
    where TText : Tizen.UI.View, Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindTextColor_TText_(thisTText,string).TText'></a>

`TText`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindTextColor_TText_(thisTText,string).view'></a>

`view` [TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindTextColor_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindTextColor&lt;TText>(this TText, string).TText')

The view whose text color property is to be set.

<a name='Tizen.UI.BindingExtensions.BindTextColor_TText_(thisTText,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the source property.

#### Returns
[TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindTextColor_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindTextColor&lt;TText>(this TText, string).TText')  
The text view with the text color property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindTextTwoWay_TText_(thisTText,string)'></a>

## BindingExtensions.BindTextTwoWay&lt;TText>(this TText, string) Method

Binds the [Text](Tizen.UI.IText.md#Tizen.UI.IText.Text 'Tizen.UI.IText.Text') property of the view to the specified path in the view model on two-way with  [TextChanged](Tizen.UI.ITextEditable.md#Tizen.UI.ITextEditable.TextChanged 'Tizen.UI.ITextEditable.TextChanged') event.

```csharp
public static TText BindTextTwoWay&lt;TText>(this TText view, string path)
    where TText : Tizen.UI.View, Tizen.UI.IText, Tizen.UI.ITextEditable;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindTextTwoWay_TText_(thisTText,string).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindTextTwoWay_TText_(thisTText,string).view'></a>

`view` [TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindTextTwoWay_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindTextTwoWay&lt;TText>(this TText, string).TText')

The text view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindTextTwoWay_TText_(thisTText,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TText](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindTextTwoWay_TText_(thisTText,string).TText 'Tizen.UI.BindingExtensions.BindTextTwoWay&lt;TText>(this TText, string).TText')  
The text view with the text property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindWidth_TView_(thisTView,string)'></a>

## BindingExtensions.BindWidth&lt;TView>(this TView, string) Method

Binds the [Width](Tizen.UI.View.md#Tizen.UI.View.Width 'Tizen.UI.View.Width') property of the view to the specified path in the view model.

```csharp
public static TView BindWidth&lt;TView>(this TView view, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindWidth_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindWidth_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindWidth_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindWidth&lt;TView>(this TView, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindWidth_TView_(thisTView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindWidth_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindWidth&lt;TView>(this TView, string).TView')  
The view with the width property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindX_TView_(thisTView,string)'></a>

## BindingExtensions.BindX&lt;TView>(this TView, string) Method

Binds the [X](Tizen.UI.View.md#Tizen.UI.View.X 'Tizen.UI.View.X') property of the view to the specified path in the view model.

```csharp
public static TView BindX&lt;TView>(this TView view, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindX_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindX_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindX_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindX&lt;TView>(this TView, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindX_TView_(thisTView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindX_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindX&lt;TView>(this TView, string).TView')  
The view with the X position property bound to the view model.

<a name='Tizen.UI.BindingExtensions.BindY_TView_(thisTView,string)'></a>

## BindingExtensions.BindY&lt;TView>(this TView, string) Method

Binds the [Y](Tizen.UI.View.md#Tizen.UI.View.Y 'Tizen.UI.View.Y') property of the view to the specified path in the view model.

```csharp
public static TView BindY&lt;TView>(this TView view, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.BindY_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.BindY_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindY_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindY&lt;TView>(this TView, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.BindY_TView_(thisTView,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.BindY_TView_(thisTView,string).TView 'Tizen.UI.BindingExtensions.BindY&lt;TView>(this TView, string).TView')  
The view with the Y position property bound to the view model.

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string)'></a>

## BindingExtensions.SetBinding&lt;T,TView>(this TView, BindingSession&lt;T>, Action&lt;T,TView>, string) Method

Sets the binding for the specified view model property.

```csharp
public static TView SetBinding&lt;T,TView>(this TView view, Tizen.UI.BindingSession&lt;T> vm, System.Action&lt;T,TView> set, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).T'></a>

`T`

The type of the view model.

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).TView 'Tizen.UI.BindingExtensions.SetBinding&lt;T,TView>(this TView, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T,TView>, string).TView')

The view to bind to.

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).vm'></a>

`vm` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).T 'Tizen.UI.BindingExtensions.SetBinding&lt;T,TView>(this TView, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T,TView>, string).T')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The view model to bind from.

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).set'></a>

`set` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).T 'Tizen.UI.BindingExtensions.SetBinding&lt;T,TView>(this TView, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T,TView>, string).T')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).TView 'Tizen.UI.BindingExtensions.SetBinding&lt;T,TView>(this TView, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T,TView>, string).TView')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The action to set the view property.

<a name='Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view model property.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T,TView_(thisTView,Tizen.UI.BindingSession_T_,System.Action_T,TView_,string).TView 'Tizen.UI.BindingExtensions.SetBinding&lt;T,TView>(this TView, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T,TView>, string).TView')  
The view.

<a name='Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string)'></a>

## BindingExtensions.SetBinding&lt;T>(this View, BindingSession&lt;T>, Action&lt;T>, string) Method

Sets the binding for the specified view model property.

```csharp
public static Tizen.UI.View SetBinding&lt;T>(this Tizen.UI.View view, Tizen.UI.BindingSession&lt;T> vm, System.Action&lt;T> set, string path);
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).T'></a>

`T`

The type of the view model.
#### Parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to bind to.

<a name='Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).vm'></a>

`vm` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).T 'Tizen.UI.BindingExtensions.SetBinding&lt;T>(this Tizen.UI.View, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T>, string).T')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The view model to bind from.

<a name='Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).set'></a>

`set` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[T](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).T 'Tizen.UI.BindingExtensions.SetBinding&lt;T>(this Tizen.UI.View, Tizen.UI.BindingSession&lt;T>, System.Action&lt;T>, string).T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The action to set the view property.

<a name='Tizen.UI.BindingExtensions.SetBinding_T_(thisTizen.UI.View,Tizen.UI.BindingSession_T_,System.Action_T_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view model property.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The view.

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string)'></a>

## BindingExtensions.SetBinding&lt;TView,TViewModel,TProperty>(this TView, BindingSession&lt;TViewModel>, BindingProperty&lt;TView,TProperty>, string) Method

Sets the binding for the specified view model property.

```csharp
public static TView SetBinding&lt;TView,TViewModel,TProperty>(this TView view, Tizen.UI.BindingSession&lt;TViewModel> session, Tizen.UI.BindingProperty&lt;TView,TProperty> property, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TViewModel'></a>

`TViewModel`

The type of the view model.

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TProperty'></a>

`TProperty`

The type of the view property.
#### Parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.SetBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TView')

The view to bind to.

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).session'></a>

`session` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[TViewModel](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TViewModel 'Tizen.UI.BindingExtensions.SetBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TViewModel')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The binding session.

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).property'></a>

`property` [Tizen.UI.BindingProperty&lt;](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.SetBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TView')[,](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')[TProperty](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TProperty 'Tizen.UI.BindingExtensions.SetBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TProperty')[&gt;](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')

The view property.

<a name='Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view model property.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.BindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.SetBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.BindingProperty&lt;TView,TProperty>, string).TView')  
The view.

<a name='Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string)'></a>

## BindingExtensions.SetBinding&lt;TViewModel>(this View, BindingSession&lt;TViewModel>, string, string) Method

Sets the binding for the specified view model property.

```csharp
public static Tizen.UI.View SetBinding&lt;TViewModel>(this Tizen.UI.View view, Tizen.UI.BindingSession&lt;TViewModel> session, string targetPath, string srcPath);
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string).TViewModel'></a>

`TViewModel`

The type of the view model.
#### Parameters

<a name='Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to bind to.

<a name='Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string).session'></a>

`session` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[TViewModel](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string).TViewModel 'Tizen.UI.BindingExtensions.SetBinding&lt;TViewModel>(this Tizen.UI.View, Tizen.UI.BindingSession&lt;TViewModel>, string, string).TViewModel')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The binding session.

<a name='Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string).targetPath'></a>

`targetPath` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view property.

<a name='Tizen.UI.BindingExtensions.SetBinding_TViewModel_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,string,string).srcPath'></a>

`srcPath` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view model property.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The view.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string)'></a>

## BindingExtensions.SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView, BindingSession&lt;TViewModel>, TwoWayBindingProperty&lt;TView,TProperty>, string) Method

Sets the two-way binding for the specified view model property.

```csharp
public static TView SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView view, Tizen.UI.BindingSession&lt;TViewModel> session, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty> property, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TViewModel'></a>

`TViewModel`

The type of the view model.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TProperty'></a>

`TProperty`

The type of the view property.
#### Parameters

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TView')

The to.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).session'></a>

`session` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[TViewModel](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TViewModel 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TViewModel')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The binding session.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).property'></a>

`property` [Tizen.UI.TwoWayBindingProperty&lt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TView')[,](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[TProperty](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TProperty 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TProperty')[&gt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')

The view property.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view model property.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TView,TViewModel,TProperty_(thisTView,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TView,TViewModel,TProperty>(this TView, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TView')  
The view.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string)'></a>

## BindingExtensions.SetTwoWayBinding&lt;TViewModel,TProperty>(this View, BindingSession&lt;TViewModel>, TwoWayBindingProperty&lt;View,TProperty>, string) Method

Sets the two-way binding for the specified view model property.

```csharp
public static Tizen.UI.View SetTwoWayBinding&lt;TViewModel,TProperty>(this Tizen.UI.View view, Tizen.UI.BindingSession&lt;TViewModel> session, Tizen.UI.TwoWayBindingProperty&lt;Tizen.UI.View,TProperty> property, string path);
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).TViewModel'></a>

`TViewModel`

The type of the view model.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).TProperty'></a>

`TProperty`

The type of the view property.
#### Parameters

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to bind to.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).session'></a>

`session` [Tizen.UI.BindingSession&lt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')[TViewModel](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).TViewModel 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TViewModel,TProperty>(this Tizen.UI.View, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;Tizen.UI.View,TProperty>, string).TViewModel')[&gt;](Tizen.UI.BindingSession_TViewModel_.md 'Tizen.UI.BindingSession&lt;TViewModel>')

The binding session.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).property'></a>

`property` [Tizen.UI.TwoWayBindingProperty&lt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[View](Tizen.UI.View.md 'Tizen.UI.View')[,](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[TProperty](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).TProperty 'Tizen.UI.BindingExtensions.SetTwoWayBinding&lt;TViewModel,TProperty>(this Tizen.UI.View, Tizen.UI.BindingSession&lt;TViewModel>, Tizen.UI.TwoWayBindingProperty&lt;Tizen.UI.View,TProperty>, string).TProperty')[&gt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')

The view property.

<a name='Tizen.UI.BindingExtensions.SetTwoWayBinding_TViewModel,TProperty_(thisTizen.UI.View,Tizen.UI.BindingSession_TViewModel_,Tizen.UI.TwoWayBindingProperty_Tizen.UI.View,TProperty_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the view model property.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The view.

<a name='Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string)'></a>

## BindingExtensions.TwoWayBind&lt;TView,TProperty>(this TView, TwoWayBindingProperty&lt;TView,TProperty>, string) Method

Binds the specified two-way property of the view to the specified path in the view model.

```csharp
public static TView TwoWayBind&lt;TView,TProperty>(this TView view, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty> property, string path)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TProperty'></a>

`TProperty`

The type of the property.
#### Parameters

<a name='Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.TwoWayBind&lt;TView,TProperty>(this TView, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TView')

The view to bind the property to.

<a name='Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).property'></a>

`property` [Tizen.UI.TwoWayBindingProperty&lt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.TwoWayBind&lt;TView,TProperty>(this TView, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TView')[,](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[TProperty](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TProperty 'Tizen.UI.BindingExtensions.TwoWayBind&lt;TView,TProperty>(this TView, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TProperty')[&gt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')

The property to bind.

<a name='Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the property in the view model.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.TwoWayBind_TView,TProperty_(thisTView,Tizen.UI.TwoWayBindingProperty_TView,TProperty_,string).TView 'Tizen.UI.BindingExtensions.TwoWayBind&lt;TView,TProperty>(this TView, Tizen.UI.TwoWayBindingProperty&lt;TView,TProperty>, string).TView')  
The view with the property bound to the view model.

<a name='Tizen.UI.BindingExtensions.ViewModel_TView_(thisTView,object)'></a>

## BindingExtensions.ViewModel&lt;TView>(this TView, object) Method

Sets the view model for the specified view.

```csharp
public static TView ViewModel&lt;TView>(this TView view, object viewModel)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.BindingExtensions.ViewModel_TView_(thisTView,object).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.BindingExtensions.ViewModel_TView_(thisTView,object).view'></a>

`view` [TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.ViewModel_TView_(thisTView,object).TView 'Tizen.UI.BindingExtensions.ViewModel&lt;TView>(this TView, object).TView')

The view to set the view model for.

<a name='Tizen.UI.BindingExtensions.ViewModel_TView_(thisTView,object).viewModel'></a>

`viewModel` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The view model to set.

#### Returns
[TView](Tizen.UI.BindingExtensions.md#Tizen.UI.BindingExtensions.ViewModel_TView_(thisTView,object).TView 'Tizen.UI.BindingExtensions.ViewModel&lt;TView>(this TView, object).TView')  
The view with the view model set.






