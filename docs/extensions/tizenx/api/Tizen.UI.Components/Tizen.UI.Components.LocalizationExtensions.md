### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## LocalizationExtensions Class

Provides extension methods for the localization.

```csharp
public static class LocalizationExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; LocalizationExtensions
### Methods

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager)'></a>

## LocalizationExtensions.BindLocalizedAccessibilityDescription&lt;TView>(this TView, string, ResourceManager) Method

Binds the localized accessibility description of the given [TView](https://docs.microsoft.com/en-us/dotnet/api/TView 'TView') to the specified key.

```csharp
public static TView BindLocalizedAccessibilityDescription&lt;TView>(this TView view, string key, System.Resources.ResourceManager resourceManager=null)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager).view'></a>

`view` [TView](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager).TView 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription&lt;TView>(this TView, string, System.Resources.ResourceManager).TView')

The view to bind.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized accessibility description.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized accessibility description.

#### Returns
[TView](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription_TView_(thisTView,string,System.Resources.ResourceManager).TView 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityDescription&lt;TView>(this TView, string, System.Resources.ResourceManager).TView')  
The view itself.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager)'></a>

## LocalizationExtensions.BindLocalizedAccessibilityName&lt;TView>(this TView, string, ResourceManager) Method

Binds the localized accessibility name of the given [TView](https://docs.microsoft.com/en-us/dotnet/api/TView 'TView') to the specified key.

```csharp
public static TView BindLocalizedAccessibilityName&lt;TView>(this TView view, string key, System.Resources.ResourceManager resourceManager=null)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager).view'></a>

`view` [TView](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager).TView 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName&lt;TView>(this TView, string, System.Resources.ResourceManager).TView')

The view to bind.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized accessibility name.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized accessibility name.

#### Returns
[TView](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName_TView_(thisTView,string,System.Resources.ResourceManager).TView 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedAccessibilityName&lt;TView>(this TView, string, System.Resources.ResourceManager).TView')  
The view itself.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager)'></a>

## LocalizationExtensions.BindLocalizedPlaceholderText&lt;TText>(this TText, string, ResourceManager) Method

Binds the localized placeholder text of the given Tizen.UI.ITextEditable to the specified key.

```csharp
public static TText BindLocalizedPlaceholderText&lt;TText>(this TText view, string key, System.Resources.ResourceManager resourceManager=null)
    where TText : class, Tizen.UI.ITextEditable;
```
#### Type parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager).view'></a>

`view` [TText](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')

The text view to bind.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized text.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized text.

#### Returns
[TText](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedPlaceholderText&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')  
The text view itself.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager)'></a>

## LocalizationExtensions.BindLocalizedSubtitle&lt;TText>(this TText, string, ResourceManager) Method

Binds the localized subtitle text of the given [IDoubleTitle](Tizen.UI.Components.IDoubleTitle.md 'Tizen.UI.Components.IDoubleTitle') to the specified key.

```csharp
public static TText BindLocalizedSubtitle&lt;TText>(this TText view, string key, System.Resources.ResourceManager resourceManager=null)
    where TText : class, Tizen.UI.Components.IDoubleTitle;
```
#### Type parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager).view'></a>

`view` [TText](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')

The text view to bind.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized text.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized text.

#### Returns
[TText](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedSubtitle&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')  
The text view itself.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager)'></a>

## LocalizationExtensions.BindLocalizedTitle&lt;TText>(this TText, string, ResourceManager) Method

Binds the localized title text of the given [ITitle](Tizen.UI.Components.ITitle.md 'Tizen.UI.Components.ITitle') to the specified key.

```csharp
public static TText BindLocalizedTitle&lt;TText>(this TText view, string key, System.Resources.ResourceManager resourceManager=null)
    where TText : class, Tizen.UI.Components.ITitle;
```
#### Type parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager).TText'></a>

`TText`

The type of the text view.
#### Parameters

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager).view'></a>

`view` [TText](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')

The text view to bind.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key to the localized text.

<a name='Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to the localized text.

#### Returns
[TText](Tizen.UI.Components.LocalizationExtensions.md#Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle_TText_(thisTText,string,System.Resources.ResourceManager).TText 'Tizen.UI.Components.LocalizationExtensions.BindLocalizedTitle&lt;TText>(this TText, string, System.Resources.ResourceManager).TText')  
The text view itself.



























































