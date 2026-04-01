### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## Sel Class

Provides static methods for creating UISelector instances with specific criteria.
This class serves as a factory for UISelector objects, allowing fluent selector creation.

```csharp
public class Sel : IDisposable
```

### Constructors

<a name='TizenX.Aurum.Sel..ctor'></a>

## Sel()

```csharp
public Sel()
```
### Fields

<a name='TizenX.Aurum.Sel.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.Sel.Depth.System.Int32.'></a>

## Depth(int)

```csharp
public static UISelector Depth(int depth)
```
#### Parameters

`depth` int

#### Returns

UISelector

<a name='TizenX.Aurum.Sel.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.Sel.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.Sel.Finalize'></a>

## ~Sel()

```csharp
protected ~Sel()
```
<a name='TizenX.Aurum.Sel.Style.System.String.'></a>

## Style(string)

```csharp
public static UISelector Style(string style)
```
#### Parameters

`style` string

#### Returns

UISelector

<a name='TizenX.Aurum.Sel.Text.System.String.'></a>

## Text(string)

Creates a UISelector that matches UI elements with the specified text content.

```csharp
public static UISelector Text(string text)
```
#### Parameters

`text` string

The text content to match.

#### Returns

UISelector

A new UISelector instance configured for text matching.

<a name='TizenX.Aurum.Sel.Type.System.String.'></a>

## Type(string)

```csharp
public static UISelector Type(string type)
```
#### Parameters

`type` string

#### Returns

UISelector

