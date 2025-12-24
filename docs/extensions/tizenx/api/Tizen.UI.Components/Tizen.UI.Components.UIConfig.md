### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIConfig Class

The base class for UI configuration.  
It provides default values for UI components.  
The derived classes can override these values.

```csharp
public class UIConfig
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; UIConfig
### Constructors

<a name='Tizen.UI.Components.UIConfig.UIConfig()'></a>

## UIConfig() Constructor

Creates a new instance of UIConfig.

```csharp
public UIConfig();
```
### Properties

<a name='Tizen.UI.Components.UIConfig.BaselineDpi'></a>

## UIConfig.BaselineDpi Property

The baseline dpi.  
Default value is 160.

```csharp
public int BaselineDpi { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.UIConfig.IgnoreDpi'></a>

## UIConfig.IgnoreDpi Property

Indicates whether the dpi should be ignored or not.  
Default value is true.

```csharp
public bool IgnoreDpi { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

### Remarks
If it's true, the dp value will be treated as px.

<a name='Tizen.UI.Components.UIConfig.IsBackKey'></a>

## UIConfig.IsBackKey Property

Check if the key is for back.

```csharp
public System.Func&lt;string,bool> IsBackKey { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.UIConfig.IsDecreaseKey'></a>

## UIConfig.IsDecreaseKey Property

Check if the key is for decreasing.

```csharp
public System.Func&lt;string,bool> IsDecreaseKey { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.UIConfig.IsExecutionKey'></a>

## UIConfig.IsExecutionKey Property

Check if the key is for execution.

```csharp
public System.Func&lt;string,bool> IsExecutionKey { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.UIConfig.IsIncreaseKey'></a>

## UIConfig.IsIncreaseKey Property

Check if the key is for increasing.

```csharp
public System.Func&lt;string,bool> IsIncreaseKey { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.UIConfig.LongPressKeyCount'></a>

## UIConfig.LongPressKeyCount Property

The required key pressed count to recognize long press.

```csharp
public uint LongPressKeyCount { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.Components.UIConfig.ScalingFactor'></a>

## UIConfig.ScalingFactor Property

The scaling factor.  
Default value is 1.0f.

```csharp
public float ScalingFactor { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Components.UIConfig.CreateBorderTable()'></a>

## UIConfig.CreateBorderTable() Method

Creates borderline width tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,float> CreateBorderTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateColorTable()'></a>

## UIConfig.CreateColorTable() Method

Creates color tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,Tizen.UI.Color> CreateColorTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')Tizen.UI.Color[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateCornerTable()'></a>

## UIConfig.CreateCornerTable() Method

Creates corner tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,Tizen.UI.CornerRadius> CreateCornerTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')Tizen.UI.CornerRadius[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateEffectColorTable()'></a>

## UIConfig.CreateEffectColorTable() Method

Creates effect color tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,Tizen.UI.Color> CreateEffectColorTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')Tizen.UI.Color[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateFontFamilyLoader()'></a>

## UIConfig.CreateFontFamilyLoader() Method

Creates a font family loader.

```csharp
public virtual Tizen.UI.Components.IFontFamilyLoader CreateFontFamilyLoader();
```

#### Returns
[IFontFamilyLoader](Tizen.UI.Components.IFontFamilyLoader.md 'Tizen.UI.Components.IFontFamilyLoader')

<a name='Tizen.UI.Components.UIConfig.CreateFontScaleLoader()'></a>

## UIConfig.CreateFontScaleLoader() Method

Creates a font scale loader.

```csharp
public virtual Tizen.UI.Components.IFontScaleLoader CreateFontScaleLoader();
```

#### Returns
[IFontScaleLoader](Tizen.UI.Components.IFontScaleLoader.md 'Tizen.UI.Components.IFontScaleLoader')

<a name='Tizen.UI.Components.UIConfig.CreateFontSizeTable()'></a>

## UIConfig.CreateFontSizeTable() Method

Creates font family size tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,float> CreateFontSizeTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateFontTable()'></a>

## UIConfig.CreateFontTable() Method

Creates font family tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,string> CreateFontTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateSpacingTable()'></a>

## UIConfig.CreateSpacingTable() Method

Creates spacing tokens used in the application.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,float> CreateSpacingTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.UIConfig.CreateThemeLoader()'></a>

## UIConfig.CreateThemeLoader() Method

Creates a theme loader.

```csharp
public virtual Tizen.UI.Components.IThemeLoader CreateThemeLoader();
```

#### Returns
[IThemeLoader](Tizen.UI.Components.IThemeLoader.md 'Tizen.UI.Components.IThemeLoader')

<a name='Tizen.UI.Components.UIConfig.CreateVariables()'></a>

## UIConfig.CreateVariables() Method

Creates variables for UI components.

```csharp
public virtual Tizen.UI.Components.UIVariables CreateVariables();
```

#### Returns
[UIVariables](Tizen.UI.Components.UIVariables.md 'Tizen.UI.Components.UIVariables')



























































