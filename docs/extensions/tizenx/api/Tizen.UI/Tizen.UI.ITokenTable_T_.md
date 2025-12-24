### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ITokenTable&lt;T> Interface

The interface for a token table.

```csharp
public interface ITokenTable&lt;T>
```
#### Type parameters

<a name='Tizen.UI.ITokenTable_T_.T'></a>

`T`
### Methods

<a name='Tizen.UI.ITokenTable_T_.Bind(Tizen.UI.View,string,System.Action_object,T_,Tizen.UI.IToken)'></a>

## ITokenTable&lt;T>.Bind(View, string, Action&lt;object,T>, IToken) Method

The method to bind target with token.  
When table is updated, binded view will be updated.

```csharp
void Bind(Tizen.UI.View target, string name, System.Action&lt;object,T> setter, Tizen.UI.IToken token);
```
#### Parameters

<a name='Tizen.UI.ITokenTable_T_.Bind(Tizen.UI.View,string,System.Action_object,T_,Tizen.UI.IToken).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.ITokenTable_T_.Bind(Tizen.UI.View,string,System.Action_object,T_,Tizen.UI.IToken).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ITokenTable_T_.Bind(Tizen.UI.View,string,System.Action_object,T_,Tizen.UI.IToken).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.ITokenTable_T_.md#Tizen.UI.ITokenTable_T_.T 'Tizen.UI.ITokenTable&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.ITokenTable_T_.Bind(Tizen.UI.View,string,System.Action_object,T_,Tizen.UI.IToken).token'></a>

`token` [IToken](Tizen.UI.IToken.md 'Tizen.UI.IToken')

<a name='Tizen.UI.ITokenTable_T_.TryGetToken(Tizen.UI.View,string,Tizen.UI.IToken)'></a>

## ITokenTable&lt;T>.TryGetToken(View, string, IToken) Method

The method to get binded token to the view.

```csharp
bool TryGetToken(Tizen.UI.View target, string propertyName, out Tizen.UI.IToken token);
```
#### Parameters

<a name='Tizen.UI.ITokenTable_T_.TryGetToken(Tizen.UI.View,string,Tizen.UI.IToken).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

The target view.

<a name='Tizen.UI.ITokenTable_T_.TryGetToken(Tizen.UI.View,string,Tizen.UI.IToken).propertyName'></a>

`propertyName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The property name of the target view.

<a name='Tizen.UI.ITokenTable_T_.TryGetToken(Tizen.UI.View,string,Tizen.UI.IToken).token'></a>

`token` [IToken](Tizen.UI.IToken.md 'Tizen.UI.IToken')

The binded token.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the token is found, otherwise false.

<a name='Tizen.UI.ITokenTable_T_.TryGetValue(string,T)'></a>

## ITokenTable&lt;T>.TryGetValue(string, T) Method

The method to get the value from the resource table.

```csharp
bool TryGetValue(string id, out T result);
```
#### Parameters

<a name='Tizen.UI.ITokenTable_T_.TryGetValue(string,T).id'></a>

`id` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ITokenTable_T_.TryGetValue(string,T).result'></a>

`result` [T](Tizen.UI.ITokenTable_T_.md#Tizen.UI.ITokenTable_T_.T 'Tizen.UI.ITokenTable&lt;T>.T')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ITokenTable_T_.Unbind(Tizen.UI.View,string)'></a>

## ITokenTable&lt;T>.Unbind(View, string) Method

The method to unbind the binded token from the target.

```csharp
void Unbind(Tizen.UI.View target, string name);
```
#### Parameters

<a name='Tizen.UI.ITokenTable_T_.Unbind(Tizen.UI.View,string).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.ITokenTable_T_.Unbind(Tizen.UI.View,string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ITokenTable_T_.Update(System.Collections.Generic.IDictionary_string,T_)'></a>

## ITokenTable&lt;T>.Update(IDictionary&lt;string,T>) Method

The method to update the resource table.

```csharp
void Update(System.Collections.Generic.IDictionary&lt;string,T> table);
```
#### Parameters

<a name='Tizen.UI.ITokenTable_T_.Update(System.Collections.Generic.IDictionary_string,T_).table'></a>

`table` [System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[T](Tizen.UI.ITokenTable_T_.md#Tizen.UI.ITokenTable_T_.T 'Tizen.UI.ITokenTable&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')
### Events

<a name='Tizen.UI.ITokenTable_T_.Updated'></a>

## ITokenTable&lt;T>.Updated Event

The event which is invoked when the resource table is updated.

```csharp
event EventHandler Updated;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






