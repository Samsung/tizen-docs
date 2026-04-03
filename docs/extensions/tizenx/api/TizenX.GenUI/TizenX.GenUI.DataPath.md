### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## DataPath Class

```csharp
public sealed class DataPath
```

### Constructors

<a name='TizenX.GenUI.DataPath..ctor.System.String.'></a>

## DataPath(string)

```csharp
public DataPath(string path)
```
#### Parameters

`path` string

### Properties

<a name='TizenX.GenUI.DataPath.BaseName'></a>

## BaseName

```csharp
public string BaseName { get; }
```
#### Property Value

string

<a name='TizenX.GenUI.DataPath.Dirname'></a>

## Dirname

```csharp
public DataPath Dirname { get; }
```
#### Property Value

DataPath

<a name='TizenX.GenUI.DataPath.IsAbsolute'></a>

## IsAbsolute

```csharp
public bool IsAbsolute { get; }
```
#### Property Value

bool

<a name='TizenX.GenUI.DataPath.Segments'></a>

## Segments

```csharp
public List<string> Segments { get; }
```
#### Property Value

List<string>

### Fields

<a name='TizenX.GenUI.DataPath.Root'></a>

## Root

```csharp
public static readonly DataPath Root
```
#### Field Value

DataPath

### Methods

<a name='TizenX.GenUI.DataPath.Equals.System.Object.'></a>

## Equals(object)

Determines whether the specified object is equal to the current object.

```csharp
public override bool Equals(object obj)
```
#### Parameters

`obj` object

The object to compare with the current object.

#### Returns

bool

true if the specified object  is equal to the current object; otherwise, false.

<a name='TizenX.GenUI.DataPath.GetHashCode'></a>

## GetHashCode()

Serves as the default hash function.

```csharp
public override int GetHashCode()
```
#### Returns

int

A hash code for the current object.

<a name='TizenX.GenUI.DataPath.Join.TizenX.GenUI.DataPath.'></a>

## Join(DataPath)

```csharp
public DataPath Join(DataPath other)
```
#### Parameters

`other` DataPath

#### Returns

DataPath

<a name='TizenX.GenUI.DataPath.StartsWith.TizenX.GenUI.DataPath.'></a>

## StartsWith(DataPath)

```csharp
public bool StartsWith(DataPath other)
```
#### Parameters

`other` DataPath

#### Returns

bool

<a name='TizenX.GenUI.DataPath.ToString'></a>

## ToString()

Returns a string that represents the current object.

```csharp
public override string ToString()
```
#### Returns

string

A string that represents the current object.

