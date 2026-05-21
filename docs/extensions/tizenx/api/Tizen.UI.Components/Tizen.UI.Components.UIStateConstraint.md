### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIStateConstraint Struct

Represents a constraint for a state that will be given when calling [Match(UIStateChangedEventArgs)](Tizen.UI.Components.UIStateConstraint.md#Tizen.UI.Components.UIStateConstraint.Match(Tizen.UI.Components.UIStateChangedEventArgs) 'Tizen.UI.Components.UIStateConstraint.Match(Tizen.UI.Components.UIStateChangedEventArgs)').

```csharp
public readonly struct UIStateConstraint :
System.IEquatable&lt;Tizen.UI.Components.UIStateConstraint>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Constructors

<a name='Tizen.UI.Components.UIStateConstraint.UIStateConstraint()'></a>

## UIStateConstraint() Constructor

Create a new value of the UIStateConstraint.

```csharp
public UIStateConstraint();
```

<a name='Tizen.UI.Components.UIStateConstraint.UIStateConstraint(Tizen.UI.Components.UIState,System.Func_Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateChangedEventArgs,bool_)'></a>

## UIStateConstraint(UIState, Func&lt;UIState,UIStateChangedEventArgs,bool>) Constructor

Create a new value of the UIStateConstraint.

```csharp
public UIStateConstraint(Tizen.UI.Components.UIState state, System.Func&lt;Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateChangedEventArgs,bool> constraint);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConstraint.UIStateConstraint(Tizen.UI.Components.UIState,System.Func_Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateChangedEventArgs,bool_).state'></a>

`state` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIStateConstraint.UIStateConstraint(Tizen.UI.Components.UIState,System.Func_Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateChangedEventArgs,bool_).constraint'></a>

`constraint` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[UIStateChangedEventArgs](Tizen.UI.Components.UIStateChangedEventArgs.md 'Tizen.UI.Components.UIStateChangedEventArgs')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')
### Fields

<a name='Tizen.UI.Components.UIStateConstraint.True'></a>

## UIStateConstraint.True Field

No constraint.

```csharp
public static UIStateConstraint True;
```

#### Field Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')
### Methods

<a name='Tizen.UI.Components.UIStateConstraint.Equals(object)'></a>

## UIStateConstraint.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object other);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConstraint.Equals(object).other'></a>

`other` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if obj and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Components.UIStateConstraint.GetHashCode()'></a>

## UIStateConstraint.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Components.UIStateConstraint.Match(Tizen.UI.Components.UIStateChangedEventArgs)'></a>

## UIStateConstraint.Match(UIStateChangedEventArgs) Method

Determine if a specified state satisfies the constraint.

```csharp
public bool Match(Tizen.UI.Components.UIStateChangedEventArgs e);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConstraint.Match(Tizen.UI.Components.UIStateChangedEventArgs).e'></a>

`e` [UIStateChangedEventArgs](Tizen.UI.Components.UIStateChangedEventArgs.md 'Tizen.UI.Components.UIStateChangedEventArgs')

The state changed event args to test if it satisfies the constraints.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the constraint is met, otherwise false.
### Operators

<a name='Tizen.UI.Components.UIStateConstraint.op_Equality(Tizen.UI.Components.UIStateConstraint,Tizen.UI.Components.UIStateConstraint)'></a>

## UIStateConstraint.operator ==(UIStateConstraint, UIStateConstraint) Operator

Compares two UIStateConstraint for equality.

```csharp
public static bool operator ==(Tizen.UI.Components.UIStateConstraint operand1, Tizen.UI.Components.UIStateConstraint operand2);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConstraint.op_Equality(Tizen.UI.Components.UIStateConstraint,Tizen.UI.Components.UIStateConstraint).operand1'></a>

`operand1` [UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

The first operand object.

<a name='Tizen.UI.Components.UIStateConstraint.op_Equality(Tizen.UI.Components.UIStateConstraint,Tizen.UI.Components.UIStateConstraint).operand2'></a>

`operand2` [UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

The second operand object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if both are equal, otherwise false.

<a name='Tizen.UI.Components.UIStateConstraint.op_ImplicitTizen.UI.Components.UIStateConstraint(Tizen.UI.Components.UIState)'></a>

## UIStateConstraint.implicit operator UIStateConstraint(UIState) Operator

Provides an implicit conversion between [UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint') and [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState').

```csharp
public static Tizen.UI.Components.UIStateConstraint implicit operator UIStateConstraint(Tizen.UI.Components.UIState state);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConstraint.op_ImplicitTizen.UI.Components.UIStateConstraint(Tizen.UI.Components.UIState).state'></a>

`state` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

The [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') to convert.

#### Returns
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')  
The corresponding [Included](Tizen.UI.Components.UIState.md#Tizen.UI.Components.UIState.Included 'Tizen.UI.Components.UIState.Included') constraint.

<a name='Tizen.UI.Components.UIStateConstraint.op_Inequality(Tizen.UI.Components.UIStateConstraint,Tizen.UI.Components.UIStateConstraint)'></a>

## UIStateConstraint.operator !=(UIStateConstraint, UIStateConstraint) Operator

Compares two UIStateConstraint for inequality.

```csharp
public static bool operator !=(Tizen.UI.Components.UIStateConstraint operand1, Tizen.UI.Components.UIStateConstraint operand2);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConstraint.op_Inequality(Tizen.UI.Components.UIStateConstraint,Tizen.UI.Components.UIStateConstraint).operand1'></a>

`operand1` [UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

The first operand object.

<a name='Tizen.UI.Components.UIStateConstraint.op_Inequality(Tizen.UI.Components.UIStateConstraint,Tizen.UI.Components.UIStateConstraint).operand2'></a>

`operand2` [UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

The second operand object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if both are not equal, otherwise false.


























































