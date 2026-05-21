### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ScopedResourceManager Class

Provides a scoped mechanism for managing effective resource managers.  
This class implements IDisposable to automatically handle pushing and popping  
resource managers based on scope boundaries.

```csharp
public sealed class ScopedResourceManager :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ScopedResourceManager

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')

### Remarks
This class is designed to work with ResourceLocalizer's effective resource manager stack,  
allowing you to temporarily set a resource manager that will be automatically  
reverted when the scope ends (typically when leaving a using block).  
  
Example usage:  
  
```csharp  
{  
    using var scope = ScopedResourceManager.Scoped(myResourceManager);  
    // myResourceManager is now the effective resource manager  
    // ... localization operations ...  
} // myResourceManager is automatically popped when scope is disposed  
```
### Constructors

<a name='Tizen.UI.ScopedResourceManager.ScopedResourceManager(System.Resources.ResourceManager)'></a>

## ScopedResourceManager(ResourceManager) Constructor

Initializes a new instance of the ScopedResourceManager class,  
pushing the specified resource manager onto the effective resource manager stack.

```csharp
public ScopedResourceManager(System.Resources.ResourceManager manager);
```
#### Parameters

<a name='Tizen.UI.ScopedResourceManager.ScopedResourceManager(System.Resources.ResourceManager).manager'></a>

`manager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to make effective for this scope
### Methods

<a name='Tizen.UI.ScopedResourceManager.Dispose()'></a>

## ScopedResourceManager.Dispose() Method

Pops the resource manager from the effective resource manager stack,  
restoring the previous resource manager (if any).

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

### Remarks
This method is automatically called when the scope ends (in Dispose pattern).  
It ensures proper cleanup of the resource manager stack even if exceptions occur.

<a name='Tizen.UI.ScopedResourceManager.Scoped(System.Resources.ResourceManager)'></a>

## ScopedResourceManager.Scoped(ResourceManager) Method

Creates a new scoped resource manager instance.

```csharp
public static Tizen.UI.ScopedResourceManager Scoped(System.Resources.ResourceManager resourceManager);
```
#### Parameters

<a name='Tizen.UI.ScopedResourceManager.Scoped(System.Resources.ResourceManager).resourceManager'></a>

`resourceManager` [System.Resources.ResourceManager](https://docs.microsoft.com/en-us/dotnet/api/System.Resources.ResourceManager 'System.Resources.ResourceManager')

The resource manager to push onto the stack

#### Returns
[ScopedResourceManager](Tizen.UI.ScopedResourceManager.md 'Tizen.UI.ScopedResourceManager')  
A new ScopedResourceManager instance

### Remarks
This factory method provides a more fluent way to create scoped resource managers.  
The created instance will push the specified resource manager onto the effective  
resource manager stack and automatically pop it when disposed.






