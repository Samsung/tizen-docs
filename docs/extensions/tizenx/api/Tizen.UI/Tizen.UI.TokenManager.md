### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TokenManager Class

The manager for the token. It provides a way to set and get the token table.

```csharp
public static class TokenManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TokenManager
### Properties

<a name='Tizen.UI.TokenManager.ColorTable'></a>

## TokenManager.ColorTable Property

Gets the color token table. If the table is not set, it returns an empty table.

```csharp
public static Tizen.UI.ITokenTable&lt;Tizen.UI.Color> ColorTable { get; }
```

#### Property Value
[Tizen.UI.ITokenTable&lt;](Tizen.UI.ITokenTable_T_.md 'Tizen.UI.ITokenTable&lt;T>')[Color](Tizen.UI.Color.md 'Tizen.UI.Color')[&gt;](Tizen.UI.ITokenTable_T_.md 'Tizen.UI.ITokenTable&lt;T>')
### Methods

<a name='Tizen.UI.TokenManager.SetTable_T_(Tizen.UI.TokenType,Tizen.UI.ITokenTable_T_)'></a>

## TokenManager.SetTable&lt;T>(TokenType, ITokenTable&lt;T>) Method

Sets the token table. If the type is not supported, it will be ignored.

```csharp
public static void SetTable&lt;T>(Tizen.UI.TokenType type, Tizen.UI.ITokenTable&lt;T> table);
```
#### Type parameters

<a name='Tizen.UI.TokenManager.SetTable_T_(Tizen.UI.TokenType,Tizen.UI.ITokenTable_T_).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.TokenManager.SetTable_T_(Tizen.UI.TokenType,Tizen.UI.ITokenTable_T_).type'></a>

`type` [TokenType](Tizen.UI.TokenType.md 'Tizen.UI.TokenType')

<a name='Tizen.UI.TokenManager.SetTable_T_(Tizen.UI.TokenType,Tizen.UI.ITokenTable_T_).table'></a>

`table` [Tizen.UI.ITokenTable&lt;](Tizen.UI.ITokenTable_T_.md 'Tizen.UI.ITokenTable&lt;T>')[T](Tizen.UI.TokenManager.md#Tizen.UI.TokenManager.SetTable_T_(Tizen.UI.TokenType,Tizen.UI.ITokenTable_T_).T 'Tizen.UI.TokenManager.SetTable&lt;T>(Tizen.UI.TokenType, Tizen.UI.ITokenTable&lt;T>).T')[&gt;](Tizen.UI.ITokenTable_T_.md 'Tizen.UI.ITokenTable&lt;T>')






