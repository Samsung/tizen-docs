### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Template&lt;T> Class

A generic template class that provides a way to create and setup instances of a specified type.

```csharp
public class Template&lt;T>
    where T : class
```
#### Type parameters

<a name='Tizen.UI.Template_T_.T'></a>

`T`

The type of the object to create and setup.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Template&lt;T>

Derived  
&#8627; [ViewTemplate](Tizen.UI.ViewTemplate.md 'Tizen.UI.ViewTemplate')
### Constructors

<a name='Tizen.UI.Template_T_.Template(System.Func_T_)'></a>

## Template(Func&lt;T>) Constructor

Initializes a new instance of the Template class using a specified load template function.

```csharp
public Template(System.Func&lt;T> loadTemplate);
```
#### Parameters

<a name='Tizen.UI.Template_T_.Template(System.Func_T_).loadTemplate'></a>

`loadTemplate` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[T](Tizen.UI.Template_T_.md#Tizen.UI.Template_T_.T 'Tizen.UI.Template&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The function to load the template.

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if loadTemplate is null.

<a name='Tizen.UI.Template_T_.Template(System.Type)'></a>

## Template(Type) Constructor

Initializes a new instance of the Template class using a specified type.

```csharp
public Template(System.Type type);
```
#### Parameters

<a name='Tizen.UI.Template_T_.Template(System.Type).type'></a>

`type` [System.Type](https://docs.microsoft.com/en-us/dotnet/api/System.Type 'System.Type')

The type to instantiate.

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if type is null.
### Properties

<a name='Tizen.UI.Template_T_.LoadTemplate'></a>

## Template&lt;T>.LoadTemplate Property

Gets the [LoadTemplate](Tizen.UI.Template_T_.md#Tizen.UI.Template_T_.LoadTemplate 'Tizen.UI.Template&lt;T>.LoadTemplate') function used to create the obejct from the template.

```csharp
public System.Func&lt;T> LoadTemplate { get; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[T](Tizen.UI.Template_T_.md#Tizen.UI.Template_T_.T 'Tizen.UI.Template&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')
### Methods

<a name='Tizen.UI.Template_T_.CreateContent()'></a>

## Template&lt;T>.CreateContent() Method

Creates an instance of the object from the template and sets it up.

```csharp
public T CreateContent();
```

#### Returns
[T](Tizen.UI.Template_T_.md#Tizen.UI.Template_T_.T 'Tizen.UI.Template&lt;T>.T')  
The created instance.




