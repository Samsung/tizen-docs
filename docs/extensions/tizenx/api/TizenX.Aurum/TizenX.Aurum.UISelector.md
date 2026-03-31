### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UISelector Class

Provides a fluent interface for building UI element selection criteria.
This class allows chaining multiple selection conditions to precisely target UI elements
based on their properties such as text, type, style, state, and hierarchy.

```csharp
public class UISelector : IDisposable
```

### Constructors

<a name='TizenX.Aurum.UISelector..ctor'></a>

## UISelector()

```csharp
public UISelector()
```
### Methods

<a name='TizenX.Aurum.UISelector.Automationid.System.String.'></a>

## Automationid(string)

```csharp
public UISelector Automationid(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Depth.System.Int32.'></a>

## Depth(int)

```csharp
public UISelector Depth(int depth)
```
#### Parameters

`depth` int

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Depth.System.Int32.System.Int32.'></a>

## Depth(int, int)

```csharp
public UISelector Depth(int minDepth, int maxDepth)
```
#### Parameters

`minDepth` int

`maxDepth` int

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Description'></a>

## Description()

```csharp
public string Description()
```
#### Returns

string

<a name='TizenX.Aurum.UISelector.Description.System.String.'></a>

## Description(string)

```csharp
public UISelector Description(string description)
```
#### Parameters

`description` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.UISelector.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.UISelector.Finalize'></a>

## ~UISelector()

```csharp
protected ~UISelector()
```
<a name='TizenX.Aurum.UISelector.FromParent.TizenX.Aurum.UISelector.'></a>

## FromParent(UISelector)

```csharp
public UISelector FromParent(UISelector parent)
```
#### Parameters

`parent` UISelector

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Geometry.TizenX.Aurum.Rect.System.Boolean.'></a>

## Geometry(Rect, bool)

```csharp
public UISelector Geometry(Rect geometry, bool isEqual)
```
#### Parameters

`geometry` Rect

`isEqual` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.HasChild.TizenX.Aurum.UISelector.'></a>

## HasChild(UISelector)

```csharp
public UISelector HasChild(UISelector child)
```
#### Parameters

`child` UISelector

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Id.System.String.'></a>

## Id(string)

```csharp
public UISelector Id(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.ImgSrc.System.String.'></a>

## ImgSrc(string)

```csharp
public UISelector ImgSrc(string imgSrc)
```
#### Parameters

`imgSrc` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsActive.System.Boolean.'></a>

## IsActive(bool)

```csharp
public UISelector IsActive(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsCheckable.System.Boolean.'></a>

## IsCheckable(bool)

```csharp
public UISelector IsCheckable(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsChecked.System.Boolean.'></a>

## IsChecked(bool)

```csharp
public UISelector IsChecked(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsClickable.System.Boolean.'></a>

## IsClickable(bool)

```csharp
public UISelector IsClickable(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsEnabled.System.Boolean.'></a>

## IsEnabled(bool)

```csharp
public UISelector IsEnabled(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsFocusable.System.Boolean.'></a>

## IsFocusable(bool)

```csharp
public UISelector IsFocusable(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsFocused.System.Boolean.'></a>

## IsFocused(bool)

```csharp
public UISelector IsFocused(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsHighlightable.System.Boolean.'></a>

## IsHighlightable(bool)

```csharp
public UISelector IsHighlightable(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsHighlighted.System.Boolean.'></a>

## IsHighlighted(bool)

```csharp
public UISelector IsHighlighted(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsScrollable.System.Boolean.'></a>

## IsScrollable(bool)

```csharp
public UISelector IsScrollable(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsSelectable.System.Boolean.'></a>

## IsSelectable(bool)

```csharp
public UISelector IsSelectable(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsSelected.System.Boolean.'></a>

## IsSelected(bool)

```csharp
public UISelector IsSelected(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsShowing.System.Boolean.'></a>

## IsShowing(bool)

```csharp
public UISelector IsShowing(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.IsVisible.System.Boolean.'></a>

## IsVisible(bool)

```csharp
public UISelector IsVisible(bool condition)
```
#### Parameters

`condition` bool

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.MaxDepth.System.Int32.'></a>

## MaxDepth(int)

```csharp
public UISelector MaxDepth(int depth)
```
#### Parameters

`depth` int

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.MinDepth.System.Int32.'></a>

## MinDepth(int)

```csharp
public UISelector MinDepth(int depth)
```
#### Parameters

`depth` int

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Pkg.System.String.'></a>

## Pkg(string)

```csharp
public UISelector Pkg(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Role.System.String.'></a>

## Role(string)

```csharp
public UISelector Role(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Style.System.String.'></a>

## Style(string)

```csharp
public UISelector Style(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Text.System.String.'></a>

## Text(string)

```csharp
public UISelector Text(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.TextPartialMatch.System.String.'></a>

## TextPartialMatch(string)

```csharp
public UISelector TextPartialMatch(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Type.System.String.'></a>

## Type(string)

```csharp
public UISelector Type(string text)
```
#### Parameters

`text` string

#### Returns

UISelector

<a name='TizenX.Aurum.UISelector.Xpath.System.String.'></a>

## Xpath(string)

```csharp
public UISelector Xpath(string xpath)
```
#### Parameters

`xpath` string

#### Returns

UISelector

