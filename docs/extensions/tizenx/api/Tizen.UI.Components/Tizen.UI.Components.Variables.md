### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Variables Class

Variables used by UI components to construct inside.

```csharp
public abstract class Variables :
System.IEquatable&lt;Tizen.UI.Components.Variables>
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Variables

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[Variables](Tizen.UI.Components.Variables.md 'Tizen.UI.Components.Variables')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Constructors

<a name='Tizen.UI.Components.Variables.Variables()'></a>

## Variables() Constructor

Constructs a new instance.

```csharp
public Variables();
```
### Properties

<a name='Tizen.UI.Components.Variables.this[string]'></a>

## Variables.this[string] Property

```csharp
public object this[string name] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.Variables.this[string].name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

#### Property Value
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')
### Methods

<a name='Tizen.UI.Components.Variables.GetNullable_T_(string,T)'></a>

## Variables.GetNullable&lt;T>(string, T) Method

Gets the nullable item with given name.

```csharp
public T GetNullable&lt;T>(string name, T fallback);
```
#### Type parameters

<a name='Tizen.UI.Components.Variables.GetNullable_T_(string,T).T'></a>

`T`

The type of the nullable item.
#### Parameters

<a name='Tizen.UI.Components.Variables.GetNullable_T_(string,T).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the nullable item.

<a name='Tizen.UI.Components.Variables.GetNullable_T_(string,T).fallback'></a>

`fallback` [T](Tizen.UI.Components.Variables.md#Tizen.UI.Components.Variables.GetNullable_T_(string,T).T 'Tizen.UI.Components.Variables.GetNullable&lt;T>(string, T).T')

The fallback value if the nullable item does not exist.

#### Returns
[T](Tizen.UI.Components.Variables.md#Tizen.UI.Components.Variables.GetNullable_T_(string,T).T 'Tizen.UI.Components.Variables.GetNullable&lt;T>(string, T).T')  
The nullable item if it exists, otherwise throws an exception.

<a name='Tizen.UI.Components.Variables.HasNullable(string)'></a>

## Variables.HasNullable(string) Method

Gets whether the nullable item with given name exists or not.

```csharp
public bool HasNullable(string name);
```
#### Parameters

<a name='Tizen.UI.Components.Variables.HasNullable(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the nullable item.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the nullable item exists, otherwise false.

<a name='Tizen.UI.Components.Variables.TryGetNullable_T_(string,T)'></a>

## Variables.TryGetNullable&lt;T>(string, T) Method

Tries to get the nullable item with given name.

```csharp
public bool TryGetNullable&lt;T>(string name, out T value);
```
#### Type parameters

<a name='Tizen.UI.Components.Variables.TryGetNullable_T_(string,T).T'></a>

`T`

The type of the nullable item.
#### Parameters

<a name='Tizen.UI.Components.Variables.TryGetNullable_T_(string,T).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the nullable item.

<a name='Tizen.UI.Components.Variables.TryGetNullable_T_(string,T).value'></a>

`value` [T](Tizen.UI.Components.Variables.md#Tizen.UI.Components.Variables.TryGetNullable_T_(string,T).T 'Tizen.UI.Components.Variables.TryGetNullable&lt;T>(string, T).T')

The nullable item if it exists, otherwise default value.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the nullable item exists, otherwise false.


























































