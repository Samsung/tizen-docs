### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## MotionData&lt;T> Class

Model motion definition.  
MotionData has a pair of [MotionIndex](Tizen.UI.Scene3D.MotionData_T_.md#Tizen.UI.Scene3D.MotionData_T_.MotionIndex 'Tizen.UI.Scene3D.MotionData&lt;T>.MotionIndex') and [MotionValue](Tizen.UI.Scene3D.MotionData_T_.md#Tizen.UI.Scene3D.MotionData_T_.MotionValue 'Tizen.UI.Scene3D.MotionData&lt;T>.MotionValue').  
MotionIndex specifies the target of motion.  
MotionValue is destination value of target for the motion.

```csharp
public class MotionData&lt;T> : Tizen.UI.Scene3D.MotionData
```
#### Type parameters

<a name='Tizen.UI.Scene3D.MotionData_T_.T'></a>

`T`

The type of the destination value.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [MotionData](Tizen.UI.Scene3D.MotionData.md 'Tizen.UI.Scene3D.MotionData') &#129106; MotionData&lt;T>
### Properties

<a name='Tizen.UI.Scene3D.MotionData_T_.MotionIndex'></a>

## MotionData&lt;T>.MotionIndex Property

Index of motion value. It will be used to specify the target of motion applied.

```csharp
public Tizen.UI.Scene3D.MotionIndex MotionIndex { get; set; }
```

#### Property Value
[MotionIndex](Tizen.UI.Scene3D.MotionIndex.md 'Tizen.UI.Scene3D.MotionIndex')

<a name='Tizen.UI.Scene3D.MotionData_T_.MotionValue'></a>

## MotionData&lt;T>.MotionValue Property

MotionValue is a pair of progress and a destination value.

```csharp
public System.Collections.Generic.IList&lt;(float progress,T value)> MotionValue { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[T](Tizen.UI.Scene3D.MotionData_T_.md#Tizen.UI.Scene3D.MotionData_T_.T 'Tizen.UI.Scene3D.MotionData&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')





































