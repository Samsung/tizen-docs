### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## MotionData Class

The MotionData is an abstract class that provides a base for model motion definition.

```csharp
public abstract class MotionData :
Tizen.UI.Scene3D.IMotionData
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; MotionData

Derived  
&#8627; [MotionData&lt;T&gt;](Tizen.UI.Scene3D.MotionData_T_.md 'Tizen.UI.Scene3D.MotionData&lt;T>')  
&#8627; [MotionDataSet](Tizen.UI.Scene3D.MotionDataSet.md 'Tizen.UI.Scene3D.MotionDataSet')

Implements [IMotionData](Tizen.UI.Scene3D.IMotionData.md 'Tizen.UI.Scene3D.IMotionData')
### Properties

<a name='Tizen.UI.Scene3D.MotionData.Duration'></a>

## MotionData.Duration Property

Get or set the duration of this motion data in milliseconds.

```csharp
public int Duration { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.Scene3D.MotionData.CreateNativeHandle()'></a>

## MotionData.CreateNativeHandle() Method

Creates a native handle of motion data.

```csharp
public Tizen.UI.Scene3D.NativeHandle.MotionDataHandle CreateNativeHandle();
```

Implements [CreateNativeHandle()](Tizen.UI.Scene3D.IMotionData.md#Tizen.UI.Scene3D.IMotionData.CreateNativeHandle() 'Tizen.UI.Scene3D.IMotionData.CreateNativeHandle()')

#### Returns
[MotionDataHandle](Tizen.UI.Scene3D.NativeHandle.MotionDataHandle.md 'Tizen.UI.Scene3D.NativeHandle.MotionDataHandle')  
The native handle of motion data.





































