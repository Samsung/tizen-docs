### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## SelectableLottieImage Class

A selectable lottie image view that can be selected and deselected with animation.

```csharp
public class SelectableLottieImage : Tizen.UI.Components.Material.LottieImage
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ImageView &#129106; [Image](Tizen.UI.Components.Material.Image.md 'Tizen.UI.Components.Material.Image') &#129106; [LottieImage](Tizen.UI.Components.Material.LottieImage.md 'Tizen.UI.Components.Material.LottieImage') &#129106; SelectableLottieImage
### Constructors

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SelectableLottieImage(string,Tizen.UI.Components.ClosedRange_int_,Tizen.UI.Components.ClosedRange_int_)'></a>

## SelectableLottieImage(string, ClosedRange&lt;int>, ClosedRange&lt;int>) Constructor

Constructs a new selectable lottie image.

```csharp
public SelectableLottieImage(string resourceUrl, Tizen.UI.Components.ClosedRange&lt;int> selectionFrames, Tizen.UI.Components.ClosedRange&lt;int> deselectionFrames);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SelectableLottieImage(string,Tizen.UI.Components.ClosedRange_int_,Tizen.UI.Components.ClosedRange_int_).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SelectableLottieImage(string,Tizen.UI.Components.ClosedRange_int_,Tizen.UI.Components.ClosedRange_int_).selectionFrames'></a>

`selectionFrames` Tizen.UI.Components.ClosedRange&lt;[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')&gt;

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SelectableLottieImage(string,Tizen.UI.Components.ClosedRange_int_,Tizen.UI.Components.ClosedRange_int_).deselectionFrames'></a>

`deselectionFrames` Tizen.UI.Components.ClosedRange&lt;[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')&gt;
### Methods

<a name='Tizen.UI.Components.Material.SelectableLottieImage.Refresh()'></a>

## SelectableLottieImage.Refresh() Method

Redraw current frame.

```csharp
public void Refresh();
```

<a name='Tizen.UI.Components.Material.SelectableLottieImage.RefreshWhenThemeChanged()'></a>

## SelectableLottieImage.RefreshWhenThemeChanged() Method

Redraw when theme changed

```csharp
public void RefreshWhenThemeChanged();
```

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SetSelection(bool,bool)'></a>

## SelectableLottieImage.SetSelection(bool, bool) Method

Sets the selection.

```csharp
public void SetSelection(bool isSelected, bool animate);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SetSelection(bool,bool).isSelected'></a>

`isSelected` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.SelectableLottieImage.SetSelection(bool,bool).animate'></a>

`animate` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')














































