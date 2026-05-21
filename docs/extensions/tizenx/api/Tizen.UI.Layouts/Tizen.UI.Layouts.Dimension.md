### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## Dimension Class

Provides a set of static methods for working with dimensions.

```csharp
public static class Dimension
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Dimension
### Fields

<a name='Tizen.UI.Layouts.Dimension.Maximum'></a>

## Dimension.Maximum Field

The constant representing the maximum dimension value.

```csharp
public const float Maximum = ∞;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.Dimension.Minimum'></a>

## Dimension.Minimum Field

The constant representing the minimum dimension value.

```csharp
public const float Minimum = 0;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.Dimension.Unset'></a>

## Dimension.Unset Field

The constant representing the unset dimension value.

```csharp
public const float Unset = NaN;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Layouts.Dimension.IsExplicitSet(float)'></a>

## Dimension.IsExplicitSet(float) Method

Checks if the given float value is explicitly set.

```csharp
public static bool IsExplicitSet(float value);
```
#### Parameters

<a name='Tizen.UI.Layouts.Dimension.IsExplicitSet(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The float value to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the value is explicitly set, false otherwise.

<a name='Tizen.UI.Layouts.Dimension.IsMaximumSet(float)'></a>

## Dimension.IsMaximumSet(float) Method

Checks if the given value has been set to its maximum value.

```csharp
public static bool IsMaximumSet(float value);
```
#### Parameters

<a name='Tizen.UI.Layouts.Dimension.IsMaximumSet(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the value has been set to its maximum value, false otherwise.

<a name='Tizen.UI.Layouts.Dimension.IsMinimumSet(float)'></a>

## Dimension.IsMinimumSet(float) Method

Checks if the given value is set to its minimum value.

```csharp
public static bool IsMinimumSet(float value);
```
#### Parameters

<a name='Tizen.UI.Layouts.Dimension.IsMinimumSet(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the value is set to its minimum value, false otherwise.

<a name='Tizen.UI.Layouts.Dimension.ResolveMinimum(float)'></a>

## Dimension.ResolveMinimum(float) Method

Resolves the minimum dimension value.

```csharp
public static float ResolveMinimum(float value);
```
#### Parameters

<a name='Tizen.UI.Layouts.Dimension.ResolveMinimum(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The dimension value to resolve.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The resolved dimension value.






























































