### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## INavigateBackHandler Interface

The INavigateBackHandler interface defines methods to handle navigating back.

```csharp
public interface INavigateBackHandler
```

Derived  
&#8627; [Navigator](Tizen.UI.Components.Navigator.md 'Tizen.UI.Components.Navigator')
### Methods

<a name='Tizen.UI.Components.INavigateBackHandler.HandleNavigateBack()'></a>

## INavigateBackHandler.HandleNavigateBack() Method

Handles navigating back.  
If navigating back is not consumed, then the Navigation object of this object will handle navigating back instead.

```csharp
bool HandleNavigateBack();
```

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if navigating back is consumed. False otherwise.


























































