### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ResourceLocalizer Class

Provides a mechanism for localizing strings and resources.

```csharp
public static class ResourceLocalizer
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ResourceLocalizer
### Properties

<a name='Tizen.UI.ResourceLocalizer.EffectiveResourceManager'></a>

## ResourceLocalizer.EffectiveResourceManager Property

Gets the currently effective resource manager for localization.  
This returns the most recently pushed resource manager from the stack,  
or falls back to the default ResourceManager if the stack is empty.

```csharp
public static System.Resources.ResourceManager EffectiveResourceManager { get; }
```

#### Property Value
[System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

### Remarks
This property is used to determine which ResourceManager should be used  
for localization in the current context. When multiple ResourceManagers  
are pushed onto the stack (using PushEffectiveResourceManager), this will  
return the most recent one. If no ResourceManagers have been pushed,  
it returns the default ResourceManager.

<a name='Tizen.UI.ResourceLocalizer.ResourceManager'></a>

## ResourceLocalizer.ResourceManager Property

Gets or sets the [ResourceManager](Tizen.UI.ResourceLocalizer.md#Tizen.UI.ResourceLocalizer.ResourceManager 'Tizen.UI.ResourceLocalizer.ResourceManager') used for localization.

```csharp
public static System.Resources.ResourceManager ResourceManager { get; set; }
```

#### Property Value
[System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')
### Methods

<a name='Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager)'></a>

## ResourceLocalizer.BindingLocalized&lt;T>(T, Action&lt;T,string>, string, ResourceManager) Method

Binds the specified tag to the specified property on the target object.

```csharp
public static void BindingLocalized&lt;T>(T target, System.Action&lt;T,string> setter, string tag, System.Resources.ResourceManager resourceManager=null)
    where T : class;
```
#### Type parameters

<a name='Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).T'></a>

`T`

The type of the target object.
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).target'></a>

`target` [T](Tizen.UI.ResourceLocalizer.md#Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).T 'Tizen.UI.ResourceLocalizer.BindingLocalized&lt;T>(T, System.Action&lt;T,string>, string, System.Resources.ResourceManager).T')

The target object.

<a name='Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.ResourceLocalizer.md#Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).T 'Tizen.UI.ResourceLocalizer.BindingLocalized&lt;T>(T, System.Action&lt;T,string>, string, System.Resources.ResourceManager).T')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The setter method for the property to bind to.

<a name='Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag to bind to.

<a name='Tizen.UI.ResourceLocalizer.BindingLocalized_T_(T,System.Action_T,string_,string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

<a name='Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string)'></a>

## ResourceLocalizer.BindingLocalizedResource&lt;T>(T, Action&lt;T,string>, string) Method

Binds the specified tag to the specified property on the target object, using localized resources.

```csharp
public static void BindingLocalizedResource&lt;T>(T target, System.Action&lt;T,string> setter, string tag)
    where T : class;
```
#### Type parameters

<a name='Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string).T'></a>

`T`

The type of the target object.
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string).target'></a>

`target` [T](Tizen.UI.ResourceLocalizer.md#Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string).T 'Tizen.UI.ResourceLocalizer.BindingLocalizedResource&lt;T>(T, System.Action&lt;T,string>, string).T')

The target object.

<a name='Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.ResourceLocalizer.md#Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string).T 'Tizen.UI.ResourceLocalizer.BindingLocalizedResource&lt;T>(T, System.Action&lt;T,string>, string).T')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The setter method for the property to bind to.

<a name='Tizen.UI.ResourceLocalizer.BindingLocalizedResource_T_(T,System.Action_T,string_,string).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag to bind to.

<a name='Tizen.UI.ResourceLocalizer.ClearBinding(Tizen.UI.View)'></a>

## ResourceLocalizer.ClearBinding(View) Method

Clears the binding for the specified target object.

```csharp
public static void ClearBinding(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.ClearBinding(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The target object.

<a name='Tizen.UI.ResourceLocalizer.LoadResourceManager(string,System.Reflection.Assembly)'></a>

## ResourceLocalizer.LoadResourceManager(string, Assembly) Method

Loads the specified resource manager for localization.

```csharp
public static void LoadResourceManager(string baseName, System.Reflection.Assembly assembly);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.LoadResourceManager(string,System.Reflection.Assembly).baseName'></a>

`baseName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The base name of the resource to load.

<a name='Tizen.UI.ResourceLocalizer.LoadResourceManager(string,System.Reflection.Assembly).assembly'></a>

`assembly` [System.Reflection.Assembly](https://docs.microsoft.com/en-us/dotnet/api/System.Reflection.Assembly 'System.Reflection.Assembly')

The assembly containing the resource.

<a name='Tizen.UI.ResourceLocalizer.LocalizedResource(string)'></a>

## ResourceLocalizer.LocalizedResource(string) Method

Returns the localized resource for the specified path.

```csharp
public static string LocalizedResource(string path);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.LocalizedResource(string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path for the localized resource.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The localized resource, or `null` if not found.

<a name='Tizen.UI.ResourceLocalizer.LocalizedString(string)'></a>

## ResourceLocalizer.LocalizedString(string) Method

Returns the localized string for the specified key.

```csharp
public static string LocalizedString(string key);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.LocalizedString(string).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key for the localized string.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The localized string, or `null` if not found.

<a name='Tizen.UI.ResourceLocalizer.LocalizedString(string,System.Resources.ResourceManager)'></a>

## ResourceLocalizer.LocalizedString(string, ResourceManager) Method

Returns the localized string for the specified key.

```csharp
public static string LocalizedString(string key, System.Resources.ResourceManager resourceManager);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.LocalizedString(string,System.Resources.ResourceManager).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key for the localized string.

<a name='Tizen.UI.ResourceLocalizer.LocalizedString(string,System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager for the localized string.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The localized string, or `null` if not found.

<a name='Tizen.UI.ResourceLocalizer.PopEffectiveResourceManager()'></a>

## ResourceLocalizer.PopEffectiveResourceManager() Method

Pops the current effective resource manager from the stack,  
restoring the previous resource manager (if any).

```csharp
public static void PopEffectiveResourceManager();
```

### Remarks
This should be called to undo a previous PushEffectiveResourceManager call,  
typically when leaving a scope where a specific resource manager was needed.  
If no resource managers have been pushed, this will throw an exception.

<a name='Tizen.UI.ResourceLocalizer.PushEffectiveResourceManager(System.Resources.ResourceManager)'></a>

## ResourceLocalizer.PushEffectiveResourceManager(ResourceManager) Method

Pushes a new resource manager onto the effective resource manager stack,  
making it the current effective resource manager for localization.

```csharp
public static void PushEffectiveResourceManager(System.Resources.ResourceManager manager);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.PushEffectiveResourceManager(System.Resources.ResourceManager).manager'></a>

`manager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The ResourceManager to push onto the stack

### Remarks
Use this method when you need to temporarily override the resource manager  
for a specific scope or context. The pushed manager will be used for all  
subsequent localization operations until it is popped from the stack.  
Remember to call PopEffectiveResourceManager when done to restore the  
previous resource manager.

<a name='Tizen.UI.ResourceLocalizer.SetDefaultCulture(System.Globalization.CultureInfo)'></a>

## ResourceLocalizer.SetDefaultCulture(CultureInfo) Method

Sets the default culture for the application and updates all resource bindings to use the new culture.

```csharp
public static void SetDefaultCulture(System.Globalization.CultureInfo culture);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.SetDefaultCulture(System.Globalization.CultureInfo).culture'></a>

`culture` [System.Globalization.CultureInfo](https://docs.microsoft.com/en-us/dotnet/api/System.Globalization.CultureInfo 'System.Globalization.CultureInfo')

The [System.Globalization.CultureInfo](https://docs.microsoft.com/en-us/dotnet/api/System.Globalization.CultureInfo 'System.Globalization.CultureInfo') object representing the culture to set as default. If null, CultureInfo.CurrentUICulture is used

<a name='Tizen.UI.ResourceLocalizer.SetLocalizeBypass(bool)'></a>

## ResourceLocalizer.SetLocalizeBypass(bool) Method

Sets the LocalizeBypass mode state.

```csharp
public static void SetLocalizeBypass(bool value);
```
#### Parameters

<a name='Tizen.UI.ResourceLocalizer.SetLocalizeBypass(bool).value'></a>

`value` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

true to enable LocalizeBypass mode, false to disable

### Remarks
When enabled, LocalizeBypass mode skips localization processing and passes resource IDs through without translation, primarily for test automation.






