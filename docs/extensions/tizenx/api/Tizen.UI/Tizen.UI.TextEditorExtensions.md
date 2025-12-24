### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TextEditorExtensions Class

Provides a set of extension methods for the [TextEditor](Tizen.UI.TextEditor.md 'Tizen.UI.TextEditor') class.

```csharp
public static class TextEditorExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TextEditorExtensions
### Methods

<a name='Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool)'></a>

## TextEditorExtensions.IsAbsoluteLineHeight&lt;TView>(this TView, bool) Method

Sets whether the line height is absolute or relative.

```csharp
public static TView IsAbsoluteLineHeight&lt;TView>(this TView view, bool isAbsoluteLineHeight)
    where TView : Tizen.UI.TextEditor;
```
#### Type parameters

<a name='Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.TextEditorExtensions.md#Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).TView 'Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight&lt;TView>(this TView, bool).TView')

The TextEditor instance.

<a name='Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).isAbsoluteLineHeight'></a>

`isAbsoluteLineHeight` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the value of line height is absolute value, false otherwise.

#### Returns
[TView](Tizen.UI.TextEditorExtensions.md#Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).TView 'Tizen.UI.TextEditorExtensions.IsAbsoluteLineHeight&lt;TView>(this TView, bool).TView')  
The TextEditor instance.

<a name='Tizen.UI.TextEditorExtensions.LineHeight_TView_(thisTView,float)'></a>

## TextEditorExtensions.LineHeight&lt;TView>(this TView, float) Method

Sets the line height of the TextEditor.

```csharp
public static TView LineHeight&lt;TView>(this TView view, float height)
    where TView : Tizen.UI.TextEditor;
```
#### Type parameters

<a name='Tizen.UI.TextEditorExtensions.LineHeight_TView_(thisTView,float).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextEditorExtensions.LineHeight_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.TextEditorExtensions.md#Tizen.UI.TextEditorExtensions.LineHeight_TView_(thisTView,float).TView 'Tizen.UI.TextEditorExtensions.LineHeight&lt;TView>(this TView, float).TView')

The TextEditor instance.

<a name='Tizen.UI.TextEditorExtensions.LineHeight_TView_(thisTView,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative line height.

#### Returns
[TView](Tizen.UI.TextEditorExtensions.md#Tizen.UI.TextEditorExtensions.LineHeight_TView_(thisTView,float).TView 'Tizen.UI.TextEditorExtensions.LineHeight&lt;TView>(this TView, float).TView')  
The TextEditor instance with the specified relative line height.





