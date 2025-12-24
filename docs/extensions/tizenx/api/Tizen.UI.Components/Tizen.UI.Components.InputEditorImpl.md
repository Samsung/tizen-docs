### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## InputEditorImpl Class

Wrapper class of DALi text editor.

```csharp
public class InputEditorImpl : Tizen.UI.Components.InputTextBaseImpl
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [TextBaseImpl](Tizen.UI.Components.TextBaseImpl.md 'Tizen.UI.Components.TextBaseImpl') &#129106; [InputTextBaseImpl](Tizen.UI.Components.InputTextBaseImpl.md 'Tizen.UI.Components.InputTextBaseImpl') &#129106; InputEditorImpl
### Properties

<a name='Tizen.UI.Components.InputEditorImpl.IsAbsoluteLineHeight'></a>

## InputEditorImpl.IsAbsoluteLineHeight Property

Gets or sets the line height policy. This value will determine how the line height is calculated.  
If the value is false, the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is false with value 1.0f.

```csharp
public bool IsAbsoluteLineHeight { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InputEditorImpl.LineBreakMode'></a>

## InputEditorImpl.LineBreakMode Property

Gets or sets the line break mode of the text.

```csharp
public Tizen.UI.LineBreakMode LineBreakMode { get; set; }
```

#### Property Value
[Tizen.UI.LineBreakMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.LineBreakMode 'Tizen.UI.LineBreakMode')

<a name='Tizen.UI.Components.InputEditorImpl.LineCount'></a>

## InputEditorImpl.LineCount Property

Gets the number of lines of text.

```csharp
public int LineCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.InputEditorImpl.LineHeight'></a>

## InputEditorImpl.LineHeight Property

Gets or sets the minimum line height. If the value is smaller than the natural line height, the natural line height will be used instead.

```csharp
public float LineHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
This property is treated differently by the [LineHeightPolicy](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy 'LineHeightPolicy'). If the value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative'), the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative') with value 1.0f.


























































