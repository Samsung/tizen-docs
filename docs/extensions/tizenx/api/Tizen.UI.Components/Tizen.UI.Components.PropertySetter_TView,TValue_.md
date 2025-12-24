### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## PropertySetter&lt;TView,TValue> Class

Describes a property setter.

```csharp
public class PropertySetter&lt;TView,TValue> :
Tizen.UI.Components.IPropertySetter&lt;TValue>
```
#### Type parameters

<a name='Tizen.UI.Components.PropertySetter_TView,TValue_.TView'></a>

`TView`

<a name='Tizen.UI.Components.PropertySetter_TView,TValue_.TValue'></a>

`TValue`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; PropertySetter&lt;TView,TValue>

Implements [Tizen.UI.Components.IPropertySetter&lt;](Tizen.UI.Components.IPropertySetter_TValue_.md 'Tizen.UI.Components.IPropertySetter&lt;TValue>')[TValue](Tizen.UI.Components.PropertySetter_TView,TValue_.md#Tizen.UI.Components.PropertySetter_TView,TValue_.TValue 'Tizen.UI.Components.PropertySetter&lt;TView,TValue>.TValue')[&gt;](Tizen.UI.Components.IPropertySetter_TValue_.md 'Tizen.UI.Components.IPropertySetter&lt;TValue>')
### Constructors

<a name='Tizen.UI.Components.PropertySetter_TView,TValue_.PropertySetter(string,System.Action_TView,TValue_)'></a>

## PropertySetter(string, Action&lt;TView,TValue>) Constructor

Creates an instance of the PropertySetter class.

```csharp
public PropertySetter(string name, System.Action&lt;TView,TValue> setter);
```
#### Parameters

<a name='Tizen.UI.Components.PropertySetter_TView,TValue_.PropertySetter(string,System.Action_TView,TValue_).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property.

<a name='Tizen.UI.Components.PropertySetter_TView,TValue_.PropertySetter(string,System.Action_TView,TValue_).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.Components.PropertySetter_TView,TValue_.md#Tizen.UI.Components.PropertySetter_TView,TValue_.TView 'Tizen.UI.Components.PropertySetter&lt;TView,TValue>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TValue](Tizen.UI.Components.PropertySetter_TView,TValue_.md#Tizen.UI.Components.PropertySetter_TView,TValue_.TValue 'Tizen.UI.Components.PropertySetter&lt;TView,TValue>.TValue')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The action to set the property.
### Properties

<a name='Tizen.UI.Components.PropertySetter_TView,TValue_.Name'></a>

## PropertySetter&lt;TView,TValue>.Name Property

The name of the property.

```csharp
public string Name { get; }
```

Implements [Name](Tizen.UI.Components.IPropertySetter_TValue_.md#Tizen.UI.Components.IPropertySetter_TValue_.Name 'Tizen.UI.Components.IPropertySetter&lt;TValue>.Name')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')


























































