### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## SystemFontSizeManager Class

Provides a system-wide font size manager.

```csharp
public static class SystemFontSizeManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; SystemFontSizeManager
### Properties

<a name='Tizen.UI.SystemFontSizeManager.CurrentFontScale'></a>

## SystemFontSizeManager.CurrentFontScale Property

Gets the current font scale.

```csharp
public static float CurrentFontScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.SystemFontSizeManager.IsSupportSystemFontSize'></a>

## SystemFontSizeManager.IsSupportSystemFontSize Property

Gets a value indicating whether the system supports changing the font size.

```csharp
public static bool IsSupportSystemFontSize { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.SystemFontSizeManager.SystemFontSize'></a>

## SystemFontSizeManager.SystemFontSize Property

Provides a static property to get the current system font size.

```csharp
public static SystemSettingsFontSize SystemFontSize { get; }
```

#### Property Value
Tizen.System.SystemSettingsFontSize
### Methods

<a name='Tizen.UI.SystemFontSizeManager.GetScale(SystemSettingsFontSize)'></a>

## SystemFontSizeManager.GetScale(SystemSettingsFontSize) Method

Gets the font scale for the specified system settings font size.

```csharp
public static float GetScale(SystemSettingsFontSize settingSize);
```
#### Parameters

<a name='Tizen.UI.SystemFontSizeManager.GetScale(SystemSettingsFontSize).settingSize'></a>

`settingSize` Tizen.System.SystemSettingsFontSize

The system settings font size.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The font scale for the specified system settings font size.

<a name='Tizen.UI.SystemFontSizeManager.UpdateScaleTable(System.Collections.Generic.IDictionary_SystemSettingsFontSize,float_)'></a>

## SystemFontSizeManager.UpdateScaleTable(IDictionary&lt;SystemSettingsFontSize,float>) Method

Updates the scale table with the specified values.

```csharp
public static void UpdateScaleTable(System.Collections.Generic.IDictionary&lt;SystemSettingsFontSize,float> table);
```
#### Parameters

<a name='Tizen.UI.SystemFontSizeManager.UpdateScaleTable(System.Collections.Generic.IDictionary_SystemSettingsFontSize,float_).table'></a>

`table` [System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')Tizen.System.SystemSettingsFontSize[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

The dictionary containing the new scale values.
### Events

<a name='Tizen.UI.SystemFontSizeManager.FontScaleChanged'></a>

## SystemFontSizeManager.FontScaleChanged Event

Occurs when the system font size changes.

```csharp
public static event EventHandler FontScaleChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')





