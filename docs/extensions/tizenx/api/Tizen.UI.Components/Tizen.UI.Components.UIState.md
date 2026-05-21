### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIState Struct

Defines a value type of view state.

```csharp
public readonly struct UIState :
System.IEquatable&lt;Tizen.UI.Components.UIState>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Fields

<a name='Tizen.UI.Components.UIState.All'></a>

## UIState.All Field

The All state is used in a selector class. It represents all states, so if this state is defined in a selector, the other states are ignored.

```csharp
public static readonly UIState All;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Disabled'></a>

## UIState.Disabled Field

Disabled State.

```csharp
public static readonly UIState Disabled;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.DisabledFocused'></a>

## UIState.DisabledFocused Field

DisabledFocused State.

```csharp
public static readonly UIState DisabledFocused;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.DisabledSelected'></a>

## UIState.DisabledSelected Field

DisabledSelected State.

```csharp
public static readonly UIState DisabledSelected;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Focused'></a>

## UIState.Focused Field

Focused State.

```csharp
public static readonly UIState Focused;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Normal'></a>

## UIState.Normal Field

Normal State.

```csharp
public static readonly UIState Normal;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Other'></a>

## UIState.Other Field

This is used in a selector class. It represents all other states except for states that are already defined in a selector.

```csharp
public static readonly UIState Other;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Paused'></a>

## UIState.Paused Field

Paused State. (It is for the component paused state. Not for animatable playback state)

```csharp
public static readonly UIState Paused;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Pressed'></a>

## UIState.Pressed Field

Pressed State.

```csharp
public static readonly UIState Pressed;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.PressedByKey'></a>

## UIState.PressedByKey Field

Pressed caused by key state.

```csharp
public static readonly UIState PressedByKey;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.PressedByTouch'></a>

## UIState.PressedByTouch Field

Pressed caused by touch state.

```csharp
public static readonly UIState PressedByTouch;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Progressing'></a>

## UIState.Progressing Field

Progressing State.

```csharp
public static readonly UIState Progressing;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Selected'></a>

## UIState.Selected Field

Selected State.

```csharp
public static readonly UIState Selected;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.SelectedFocused'></a>

## UIState.SelectedFocused Field

SelectedFocused State.

```csharp
public static readonly UIState SelectedFocused;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.SelectedPressed'></a>

## UIState.SelectedPressed Field

SelectedPressed State.

```csharp
public static readonly UIState SelectedPressed;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIState.Warning'></a>

## UIState.Warning Field

Warning State.

```csharp
public static readonly UIState Warning;
```

#### Field Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')
### Properties

<a name='Tizen.UI.Components.UIState.Added'></a>

## UIState.Added Property

Gets a constraint that a state is added compared with previous state.

```csharp
public Tizen.UI.Components.UIStateConstraint Added { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

<a name='Tizen.UI.Components.UIState.Changed'></a>

## UIState.Changed Property

Gets a constraint that a state is added or removed.

```csharp
public Tizen.UI.Components.UIStateConstraint Changed { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

<a name='Tizen.UI.Components.UIState.Excluded'></a>

## UIState.Excluded Property

Gets a constraint that a state must not include this state.

```csharp
public Tizen.UI.Components.UIStateConstraint Excluded { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

<a name='Tizen.UI.Components.UIState.Included'></a>

## UIState.Included Property

Gets a constraint that a state must include this state.

```csharp
public Tizen.UI.Components.UIStateConstraint Included { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

<a name='Tizen.UI.Components.UIState.Is'></a>

## UIState.Is Property

Gets a constraint that a state must be identical to this state.

```csharp
public Tizen.UI.Components.UIStateConstraint Is { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

<a name='Tizen.UI.Components.UIState.Not'></a>

## UIState.Not Property

Gets a constraint that a state must not be identical to this state.

```csharp
public Tizen.UI.Components.UIStateConstraint Not { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

<a name='Tizen.UI.Components.UIState.Removed'></a>

## UIState.Removed Property

Gets a constraint that a state is removed compared with previous state.

```csharp
public Tizen.UI.Components.UIStateConstraint Removed { get; }
```

#### Property Value
[UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')
### Methods

<a name='Tizen.UI.Components.UIState.Contains(Tizen.UI.Components.UIState)'></a>

## UIState.Contains(UIState) Method

Determines whether a state contains a specified state.

```csharp
public bool Contains(Tizen.UI.Components.UIState state);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.Contains(Tizen.UI.Components.UIState).state'></a>

`state` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

The state to search for

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if the state contain a specified state, otherwise, false.

<a name='Tizen.UI.Components.UIState.Create(string)'></a>

## UIState.Create(string) Method

Create an instance of the [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') with state name.

```csharp
public static Tizen.UI.Components.UIState Create(string name);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.Create(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The state name.

#### Returns
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')  
The [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') instance which has single state.

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown when the given name is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown when the given name is invalid.

<a name='Tizen.UI.Components.UIState.Equals(object)'></a>

## UIState.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.Components.UIState.md#Tizen.UI.Components.UIState.Equals(object).obj 'Tizen.UI.Components.UIState.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Components.UIState.Equals(Tizen.UI.Components.UIState)'></a>

## UIState.Equals(UIState) Method

Indicates whether this instance and another specified [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') structure are equal.

```csharp
public bool Equals(Tizen.UI.Components.UIState other);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.Equals(Tizen.UI.Components.UIState).other'></a>

`other` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

The [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') structure to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if [other](Tizen.UI.Components.UIState.md#Tizen.UI.Components.UIState.Equals(Tizen.UI.Components.UIState).other 'Tizen.UI.Components.UIState.Equals(Tizen.UI.Components.UIState).other') and this instance are equal; otherwise, false.

<a name='Tizen.UI.Components.UIState.GetHashCode()'></a>

## UIState.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Components.UIState.HasIntersectionWith(Tizen.UI.Components.UIState)'></a>

## UIState.HasIntersectionWith(UIState) Method

Checks if there is a intersection part between this and the other.

```csharp
public bool HasIntersectionWith(Tizen.UI.Components.UIState other);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.HasIntersectionWith(Tizen.UI.Components.UIState).other'></a>

`other` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

The other state to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if an intersection exists, otherwise false.

<a name='Tizen.UI.Components.UIState.ToString()'></a>

## UIState.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.
### Operators

<a name='Tizen.UI.Components.UIState.op_Addition(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState)'></a>

## UIState.operator +(UIState, UIState) Operator

The addition operator.

```csharp
public static Tizen.UI.Components.UIState operator +(Tizen.UI.Components.UIState lhs, Tizen.UI.Components.UIState rhs);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.op_Addition(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).lhs'></a>

`lhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the left hand side.

<a name='Tizen.UI.Components.UIState.op_Addition(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).rhs'></a>

`rhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the right hand side.

#### Returns
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')  
The [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') containing the result of the addition.

<a name='Tizen.UI.Components.UIState.op_Equality(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState)'></a>

## UIState.operator ==(UIState, UIState) Operator

Compares whether the two ControlStates are same or not.

```csharp
public static bool operator ==(Tizen.UI.Components.UIState lhs, Tizen.UI.Components.UIState rhs);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.op_Equality(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).lhs'></a>

`lhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the left hand side.

<a name='Tizen.UI.Components.UIState.op_Equality(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).rhs'></a>

`rhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the right hand side.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if the ControlStates are equal; otherwise, false.

<a name='Tizen.UI.Components.UIState.op_Inequality(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState)'></a>

## UIState.operator !=(UIState, UIState) Operator

Compares whether the two ControlStates are different or not.

```csharp
public static bool operator !=(Tizen.UI.Components.UIState lhs, Tizen.UI.Components.UIState rhs);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.op_Inequality(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).lhs'></a>

`lhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the left hand side.

<a name='Tizen.UI.Components.UIState.op_Inequality(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).rhs'></a>

`rhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the right hand side.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if the ControlStates are not equal; otherwise, false.

<a name='Tizen.UI.Components.UIState.op_OnesComplement(Tizen.UI.Components.UIState)'></a>

## UIState.operator ~(UIState) Operator

The substraction operator.

```csharp
public static Tizen.UI.Components.UIState operator ~(Tizen.UI.Components.UIState state);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.op_OnesComplement(Tizen.UI.Components.UIState).state'></a>

`state` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A target [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState').

#### Returns
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')  
The [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') containing the result of bitwise complement.

<a name='Tizen.UI.Components.UIState.op_Subtraction(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState)'></a>

## UIState.operator -(UIState, UIState) Operator

The substraction operator.

```csharp
public static Tizen.UI.Components.UIState operator -(Tizen.UI.Components.UIState lhs, Tizen.UI.Components.UIState rhs);
```
#### Parameters

<a name='Tizen.UI.Components.UIState.op_Subtraction(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).lhs'></a>

`lhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the left hand side.

<a name='Tizen.UI.Components.UIState.op_Subtraction(Tizen.UI.Components.UIState,Tizen.UI.Components.UIState).rhs'></a>

`rhs` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

A [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') on the right hand side.

#### Returns
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')  
The [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState') containing the result of the substraction.


























































