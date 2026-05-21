### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UIObject Class

```csharp
public class UIObject : Searchable, IDisposable
```

### Constructors

<a name='TizenX.Aurum.UIObject..ctor'></a>

## UIObject()

```csharp
public UIObject()
```
<a name='TizenX.Aurum.UIObject..ctor.TizenX.Aurum.UIObject.'></a>

## UIObject(UIObject)

```csharp
public UIObject(UIObject src)
```
#### Parameters

`src` UIObject

### Methods

<a name='TizenX.Aurum.UIObject.Click'></a>

## Click()

```csharp
public void Click()
```
<a name='TizenX.Aurum.UIObject.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected override void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.UIObject.DoAtspiActivate'></a>

## DoAtspiActivate()

```csharp
public bool DoAtspiActivate()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.FindObject.TizenX.Aurum.UISelector.'></a>

## FindObject(UISelector)

```csharp
public override UIObject FindObject(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.FindObjects.TizenX.Aurum.UISelector.'></a>

## FindObjects(UISelector)

```csharp
public override UIObjectVector FindObjects(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIObject.First'></a>

## First()

```csharp
public UIObject First()
```
#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.GetApplicationPackage'></a>

## GetApplicationPackage()

```csharp
public string GetApplicationPackage()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetAutomationId'></a>

## GetAutomationId()

```csharp
public string GetAutomationId()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetChildAt.System.Int32.'></a>

## GetChildAt(int)

```csharp
public UIObject GetChildAt(int index)
```
#### Parameters

`index` int

#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.GetChildCount'></a>

## GetChildCount()

```csharp
public int GetChildCount()
```
#### Returns

int

<a name='TizenX.Aurum.UIObject.GetChildren'></a>

## GetChildren()

```csharp
public UIObjectVector GetChildren()
```
#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIObject.GetDescendant'></a>

## GetDescendant()

```csharp
public Node GetDescendant()
```
#### Returns

Node

<a name='TizenX.Aurum.UIObject.GetDescription'></a>

## GetDescription()

```csharp
public string GetDescription()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetElementStyle'></a>

## GetElementStyle()

```csharp
public string GetElementStyle()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetId'></a>

## GetId()

```csharp
public string GetId()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetImgSrc'></a>

## GetImgSrc()

```csharp
public string GetImgSrc()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetIncludeHidden'></a>

## GetIncludeHidden()

```csharp
public bool GetIncludeHidden()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.GetIncrement'></a>

## GetIncrement()

```csharp
public double GetIncrement()
```
#### Returns

double

<a name='TizenX.Aurum.UIObject.GetInterface'></a>

## GetInterface()

```csharp
public string GetInterface()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetMatches.TizenX.Aurum.UISelector.System.Boolean.'></a>

## GetMatches(UISelector, bool)

```csharp
public override UIObjectVector GetMatches(UISelector selector, bool earlyReturn)
```
#### Parameters

`selector` UISelector

`earlyReturn` bool

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIObject.GetMatchesInMatches.TizenX.Aurum.UISelector.TizenX.Aurum.UISelector.System.Boolean.'></a>

## GetMatchesInMatches(UISelector, UISelector, bool)

```csharp
public override UIObjectVector GetMatchesInMatches(UISelector firstSelector, UISelector secondSelector, bool earlyReturn)
```
#### Parameters

`firstSelector` UISelector

`secondSelector` UISelector

`earlyReturn` bool

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIObject.GetMaxValue'></a>

## GetMaxValue()

```csharp
public double GetMaxValue()
```
#### Returns

double

<a name='TizenX.Aurum.UIObject.GetMinValue'></a>

## GetMinValue()

```csharp
public double GetMinValue()
```
#### Returns

double

<a name='TizenX.Aurum.UIObject.GetOcrText'></a>

## GetOcrText()

```csharp
public string GetOcrText()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetParent'></a>

## GetParent()

```csharp
public UIObject GetParent()
```
#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.GetPid'></a>

## GetPid()

```csharp
public int GetPid()
```
#### Returns

int

<a name='TizenX.Aurum.UIObject.GetRole'></a>

## GetRole()

```csharp
public string GetRole()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetScreenBoundingBox'></a>

## GetScreenBoundingBox()

```csharp
public Rect GetScreenBoundingBox()
```
#### Returns

Rect

<a name='TizenX.Aurum.UIObject.GetSelector'></a>

## GetSelector()

```csharp
public UISelector GetSelector()
```
#### Returns

UISelector

<a name='TizenX.Aurum.UIObject.GetTargetAngle'></a>

## GetTargetAngle()

```csharp
public int GetTargetAngle()
```
#### Returns

int

<a name='TizenX.Aurum.UIObject.GetText'></a>

## GetText()

```csharp
public string GetText()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetTextMinBoundingRect'></a>

## GetTextMinBoundingRect()

```csharp
public Rect GetTextMinBoundingRect()
```
#### Returns

Rect

<a name='TizenX.Aurum.UIObject.GetToolkitName'></a>

## GetToolkitName()

```csharp
public string GetToolkitName()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetType'></a>

## GetType()

```csharp
public string GetType()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.GetValue'></a>

## GetValue()

```csharp
public double GetValue()
```
#### Returns

double

<a name='TizenX.Aurum.UIObject.GetWindowAngle'></a>

## GetWindowAngle()

```csharp
public int GetWindowAngle()
```
#### Returns

int

<a name='TizenX.Aurum.UIObject.GetWindowBoundingBox'></a>

## GetWindowBoundingBox()

```csharp
public Rect GetWindowBoundingBox()
```
#### Returns

Rect

<a name='TizenX.Aurum.UIObject.GetXPath'></a>

## GetXPath()

```csharp
public string GetXPath()
```
#### Returns

string

<a name='TizenX.Aurum.UIObject.HasObject.TizenX.Aurum.UISelector.'></a>

## HasObject(UISelector)

```csharp
public override bool HasObject(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsActive'></a>

## IsActive()

```csharp
public bool IsActive()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsCheckable'></a>

## IsCheckable()

```csharp
public bool IsCheckable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsChecked'></a>

## IsChecked()

```csharp
public bool IsChecked()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsClickable'></a>

## IsClickable()

```csharp
public bool IsClickable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsEnabled'></a>

## IsEnabled()

```csharp
public bool IsEnabled()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsFocusable'></a>

## IsFocusable()

```csharp
public bool IsFocusable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsFocused'></a>

## IsFocused()

```csharp
public bool IsFocused()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsHighlightable'></a>

## IsHighlightable()

```csharp
public bool IsHighlightable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsHighlighted'></a>

## IsHighlighted()

```csharp
public bool IsHighlighted()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsLongClickable'></a>

## IsLongClickable()

```csharp
public bool IsLongClickable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsScrollable'></a>

## IsScrollable()

```csharp
public bool IsScrollable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsSelectable'></a>

## IsSelectable()

```csharp
public bool IsSelectable()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsSelected'></a>

## IsSelected()

```csharp
public bool IsSelected()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsShowing'></a>

## IsShowing()

```csharp
public bool IsShowing()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsValid'></a>

## IsValid()

```csharp
public bool IsValid()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.IsVisible'></a>

## IsVisible()

```csharp
public bool IsVisible()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.Last'></a>

## Last()

```csharp
public UIObject Last()
```
#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.LongClick'></a>

## LongClick()

```csharp
public void LongClick()
```
<a name='TizenX.Aurum.UIObject.LongClick.System.UInt32.'></a>

## LongClick(uint)

```csharp
public void LongClick(uint durationMs)
```
#### Parameters

`durationMs` uint

<a name='TizenX.Aurum.UIObject.MoveTo'></a>

## MoveTo()

```csharp
public bool MoveTo()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.Next'></a>

## Next()

```csharp
public UIObject Next()
```
#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.Prev'></a>

## Prev()

```csharp
public UIObject Prev()
```
#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.Refresh'></a>

## Refresh()

```csharp
public void Refresh()
```
<a name='TizenX.Aurum.UIObject.SetFocus'></a>

## SetFocus()

```csharp
public bool SetFocus()
```
#### Returns

bool

<a name='TizenX.Aurum.UIObject.SetIncludeHidden.System.Boolean.'></a>

## SetIncludeHidden(bool)

```csharp
public void SetIncludeHidden(bool enabled)
```
#### Parameters

`enabled` bool

<a name='TizenX.Aurum.UIObject.SetLocalization.System.Boolean.'></a>

## SetLocalization(bool)

```csharp
public bool SetLocalization(bool enabled)
```
#### Parameters

`enabled` bool

#### Returns

bool

<a name='TizenX.Aurum.UIObject.SetOcrText.System.String.'></a>

## SetOcrText(string)

```csharp
public void SetOcrText(string text)
```
#### Parameters

`text` string

<a name='TizenX.Aurum.UIObject.SetText.System.String.'></a>

## SetText(string)

```csharp
public bool SetText(string text)
```
#### Parameters

`text` string

#### Returns

bool

<a name='TizenX.Aurum.UIObject.SetValue.System.Double.'></a>

## SetValue(double)

```csharp
public bool SetValue(double value)
```
#### Parameters

`value` double

#### Returns

bool

<a name='TizenX.Aurum.UIObject.UpdateApplication'></a>

## UpdateApplication()

```csharp
public void UpdateApplication()
```
<a name='TizenX.Aurum.UIObject.UpdateAttributes'></a>

## UpdateAttributes()

```csharp
public void UpdateAttributes()
```
<a name='TizenX.Aurum.UIObject.UpdateExtents'></a>

## UpdateExtents()

```csharp
public void UpdateExtents()
```
<a name='TizenX.Aurum.UIObject.UpdateInterface'></a>

## UpdateInterface()

```csharp
public void UpdateInterface()
```
<a name='TizenX.Aurum.UIObject.UpdateName'></a>

## UpdateName()

```csharp
public void UpdateName()
```
<a name='TizenX.Aurum.UIObject.UpdatePid'></a>

## UpdatePid()

```csharp
public void UpdatePid()
```
<a name='TizenX.Aurum.UIObject.UpdateRoleName'></a>

## UpdateRoleName()

```csharp
public void UpdateRoleName()
```
<a name='TizenX.Aurum.UIObject.UpdateStates'></a>

## UpdateStates()

```csharp
public void UpdateStates()
```
<a name='TizenX.Aurum.UIObject.UpdateTextMinBoundingRect'></a>

## UpdateTextMinBoundingRect()

```csharp
public void UpdateTextMinBoundingRect()
```
<a name='TizenX.Aurum.UIObject.UpdateToolkitName'></a>

## UpdateToolkitName()

```csharp
public void UpdateToolkitName()
```
<a name='TizenX.Aurum.UIObject.UpdateUniqueId'></a>

## UpdateUniqueId()

```csharp
public void UpdateUniqueId()
```
<a name='TizenX.Aurum.UIObject.UpdateValue'></a>

## UpdateValue()

```csharp
public void UpdateValue()
```
<a name='TizenX.Aurum.UIObject.UpdateXPath'></a>

## UpdateXPath()

```csharp
public void UpdateXPath()
```
<a name='TizenX.Aurum.UIObject.WaitFor.TizenX.Aurum.CheckableFunction.'></a>

## WaitFor(CheckableFunction)

```csharp
public bool WaitFor(CheckableFunction condition)
```
#### Parameters

`condition` CheckableFunction

#### Returns

bool

<a name='TizenX.Aurum.UIObject.WaitFor.TizenX.Aurum.FindObjectFunction.'></a>

## WaitFor(FindObjectFunction)

```csharp
public UIObject WaitFor(FindObjectFunction condition)
```
#### Parameters

`condition` FindObjectFunction

#### Returns

UIObject

<a name='TizenX.Aurum.UIObject.WaitFor.TizenX.Aurum.HasObjectFunction.'></a>

## WaitFor(HasObjectFunction)

```csharp
public bool WaitFor(HasObjectFunction condition)
```
#### Parameters

`condition` HasObjectFunction

#### Returns

bool

