### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## LottieImage Class

LottieImage is a control for displaying Lottie animations.

```csharp
public class LottieImage : Tizen.UI.Components.Material.Image,
Tizen.UI.Components.IAnimatedImage
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ImageView &#129106; [Image](Tizen.UI.Components.Material.Image.md 'Tizen.UI.Components.Material.Image') &#129106; LottieImage

Derived  
&#8627; [SelectableLottieImage](Tizen.UI.Components.Material.SelectableLottieImage.md 'Tizen.UI.Components.Material.SelectableLottieImage')

Implements Tizen.UI.Components.IAnimatedImage
### Constructors

<a name='Tizen.UI.Components.Material.LottieImage.LottieImage()'></a>

## LottieImage() Constructor

Creates a LottieAnimationView.

```csharp
public LottieImage();
```

<a name='Tizen.UI.Components.Material.LottieImage.LottieImage(string)'></a>

## LottieImage(string) Constructor

Creates a LottieAnimationView.

```csharp
public LottieImage(string resourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.LottieImage(string).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Properties

<a name='Tizen.UI.Components.Material.LottieImage.CurrentFrame'></a>

## LottieImage.CurrentFrame Property

Gets or sets the current frame of the animation.

```csharp
public int CurrentFrame { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.LottieImage.FrameSpeedFactor'></a>

## LottieImage.FrameSpeedFactor Property

Specifies a speed factor for the animated image frame.

```csharp
public float FrameSpeedFactor { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
The speed factor is a multiplier of the normal velocity of the animation. Values between [0,1] will  
slow down the animation and values above one will speed up the animation.  
The range of this value is clamped between [0.01f ~ 100.0f].  
The default is 1.0f.

<a name='Tizen.UI.Components.Material.LottieImage.IsLooping'></a>

## LottieImage.IsLooping Property

Gets or sets whether the animation should loop.

```csharp
public bool IsLooping { get; set; }
```

Implements IsLooping

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.LottieImage.PlayState'></a>

## LottieImage.PlayState Property

Gets the current play state of the animation.

```csharp
public Tizen.UI.AnimationState PlayState { get; }
```

#### Property Value
Tizen.UI.AnimationState

<a name='Tizen.UI.Components.Material.LottieImage.RedrawInScalingDown'></a>

## LottieImage.RedrawInScalingDown Property

Whether to redraw the image when the visual is scaled down.

```csharp
public bool RedrawInScalingDown { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

### Remarks
Inhouse API. The default is true.

<a name='Tizen.UI.Components.Material.LottieImage.RepeatCount'></a>

## LottieImage.RepeatCount Property

Gets or sets the number of times the animation should repeat.

```csharp
public int RepeatCount { get; set; }
```

Implements RepeatCount

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.LottieImage.RepeatMode'></a>

## LottieImage.RepeatMode Property

Gets or sets the mode of animation repetition.

```csharp
public Tizen.UI.AnimationRepeatMode RepeatMode { get; set; }
```

#### Property Value
Tizen.UI.AnimationRepeatMode

<a name='Tizen.UI.Components.Material.LottieImage.StopBehavior'></a>

## LottieImage.StopBehavior Property

Gets or sets the behavior of the animation when it stops.

```csharp
public Tizen.UI.AnimationStopBehavior StopBehavior { get; set; }
```

Implements StopBehavior

#### Property Value
Tizen.UI.AnimationStopBehavior

<a name='Tizen.UI.Components.Material.LottieImage.TotalFrame'></a>

## LottieImage.TotalFrame Property

Gets the total number of frames in the animation.

```csharp
public int TotalFrame { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.Components.Material.LottieImage.ClearDynamicProperties()'></a>

## LottieImage.ClearDynamicProperties() Method

Clear registered dynamic properties.

```csharp
public void ClearDynamicProperties();
```

<a name='Tizen.UI.Components.Material.LottieImage.GetContentInfo()'></a>

## LottieImage.GetContentInfo() Method

Gets the content information of the animation.

```csharp
public System.Collections.Generic.IList&lt;(string,int,int)> GetContentInfo();
```

#### Returns
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')  
of tuples containing the layer name, start frame index, and end frame index.

<a name='Tizen.UI.Components.Material.LottieImage.GetMarkerInfo()'></a>

## LottieImage.GetMarkerInfo() Method

Gets the marker information of the animation.

```csharp
public System.Collections.Generic.IList&lt;(string,int,int)> GetMarkerInfo();
```

#### Returns
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')  
of tuples containing the marker name, start frame index, and end frame index.

<a name='Tizen.UI.Components.Material.LottieImage.Pause()'></a>

## LottieImage.Pause() Method

Pauses the animation.

```csharp
public override void Pause();
```

Implements Pause()

<a name='Tizen.UI.Components.Material.LottieImage.Play()'></a>

## LottieImage.Play() Method

Plays the animation.

```csharp
public override void Play();
```

Implements Play()

<a name='Tizen.UI.Components.Material.LottieImage.Play(int)'></a>

## LottieImage.Play(int) Method

Plays the animation from the specified frame.

```csharp
public virtual void Play(int startFrame);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.Play(int).startFrame'></a>

`startFrame` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.LottieImage.Play(int,int)'></a>

## LottieImage.Play(int, int) Method

Plays the animation with range.

```csharp
public virtual void Play(int startFrame, int maxFrame);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.Play(int,int).startFrame'></a>

`startFrame` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.LottieImage.Play(int,int).maxFrame'></a>

`maxFrame` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.LottieImage.Play(string)'></a>

## LottieImage.Play(string) Method

Plays the animation based on the given marker.  
Animation will play between the start frame index and the end frame index of the specified marker.

```csharp
public virtual void Play(string marker);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.Play(string).marker'></a>

`marker` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.Play(string,string)'></a>

## LottieImage.Play(string, string) Method

Plays the animation based on the given markers.  
Animation will play between the start frame index of the startMarker and the end frame index of the endMarker.

```csharp
public virtual void Play(string startMarker, string endMarker);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.Play(string,string).startMarker'></a>

`startMarker` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.Play(string,string).endMarker'></a>

`endMarker` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicBackgroundColor(string,System.Func_int,Tizen.UI.Color_)'></a>

## LottieImage.RegisterDynamicBackgroundColor(string, Func&lt;int,Color>) Method

Register a dynamic fill color (R, G, B, A) property.

```csharp
public void RegisterDynamicBackgroundColor(string path, System.Func&lt;int,Tizen.UI.Color> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicBackgroundColor(string,System.Func_int,Tizen.UI.Color_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicBackgroundColor(string,System.Func_int,Tizen.UI.Color_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Color[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

### Remarks
This can overwrite or overwritten by RegisterDynamicFillOpacity.  
If you want to use both fill color and opacity, use only RegisterDynamicBackgroundColor with proper alpha value.

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicFillOpacity(string,System.Func_int,float_)'></a>

## LottieImage.RegisterDynamicFillOpacity(string, Func&lt;int,float>) Method

Register a dynamic fill opacity property.

```csharp
public void RegisterDynamicFillOpacity(string path, System.Func&lt;int,float> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicFillOpacity(string,System.Func_int,float_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicFillOpacity(string,System.Func_int,float_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

### Remarks
This can overwrite or overwritten by RegisterDynamicBackgroundColor.  
If you want to use both fill color and opacity, use only RegisterDynamicBackgroundColor with proper alpha value.

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeColor(string,System.Func_int,Tizen.UI.Color_)'></a>

## LottieImage.RegisterDynamicStrokeColor(string, Func&lt;int,Color>) Method

Register a dynamic stroke color (R, G, B, A) property.

```csharp
public void RegisterDynamicStrokeColor(string path, System.Func&lt;int,Tizen.UI.Color> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeColor(string,System.Func_int,Tizen.UI.Color_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeColor(string,System.Func_int,Tizen.UI.Color_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Color[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

### Remarks
This can overwrite or overwritten by RegisterDynamicStrokeOpacity.  
If you want to use both stroke color and opacity, use only RegisterDynamicStrokeColor with proper alpha value.

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeOpacity(string,System.Func_int,float_)'></a>

## LottieImage.RegisterDynamicStrokeOpacity(string, Func&lt;int,float>) Method

Register a dynamic stroke opacity property.

```csharp
public void RegisterDynamicStrokeOpacity(string path, System.Func&lt;int,float> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeOpacity(string,System.Func_int,float_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeOpacity(string,System.Func_int,float_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

### Remarks
This can overwrite or overwritten by RegisterDynamicStrokeColor.  
If you want to use both stroke color and opacity, use only RegisterDynamicStrokeColor with proper alpha value.

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeWidth(string,System.Func_int,float_)'></a>

## LottieImage.RegisterDynamicStrokeWidth(string, Func&lt;int,float>) Method

Register a dynamic stroke width property.

```csharp
public void RegisterDynamicStrokeWidth(string path, System.Func&lt;int,float> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeWidth(string,System.Func_int,float_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicStrokeWidth(string,System.Func_int,float_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformAnchor(string,System.Func_int,Tizen.UI.Point_)'></a>

## LottieImage.RegisterDynamicTransformAnchor(string, Func&lt;int,Point>) Method

Register a dynamic transform anchor property.

```csharp
public void RegisterDynamicTransformAnchor(string path, System.Func&lt;int,Tizen.UI.Point> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformAnchor(string,System.Func_int,Tizen.UI.Point_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformAnchor(string,System.Func_int,Tizen.UI.Point_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Point[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformOpacity(string,System.Func_int,float_)'></a>

## LottieImage.RegisterDynamicTransformOpacity(string, Func&lt;int,float>) Method

Register a dynamic transform opacity property.

```csharp
public void RegisterDynamicTransformOpacity(string path, System.Func&lt;int,float> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformOpacity(string,System.Func_int,float_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformOpacity(string,System.Func_int,float_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformPosition(string,System.Func_int,Tizen.UI.Point_)'></a>

## LottieImage.RegisterDynamicTransformPosition(string, Func&lt;int,Point>) Method

Register a dynamic transform position property.

```csharp
public void RegisterDynamicTransformPosition(string path, System.Func&lt;int,Tizen.UI.Point> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformPosition(string,System.Func_int,Tizen.UI.Point_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformPosition(string,System.Func_int,Tizen.UI.Point_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Point[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformRotation(string,System.Func_int,float_)'></a>

## LottieImage.RegisterDynamicTransformRotation(string, Func&lt;int,float>) Method

Register a dynamic transform rotation property.

```csharp
public void RegisterDynamicTransformRotation(string path, System.Func&lt;int,float> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformRotation(string,System.Func_int,float_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformRotation(string,System.Func_int,float_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformScale(string,System.Func_int,Tizen.UI.Point_)'></a>

## LottieImage.RegisterDynamicTransformScale(string, Func&lt;int,Point>) Method

Register a dynamic transform scale property.

```csharp
public void RegisterDynamicTransformScale(string path, System.Func&lt;int,Tizen.UI.Point> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformScale(string,System.Func_int,Tizen.UI.Point_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTransformScale(string,System.Func_int,Tizen.UI.Point_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Point[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTrimEnd(string,System.Func_int,Tizen.UI.Point_)'></a>

## LottieImage.RegisterDynamicTrimEnd(string, Func&lt;int,Point>) Method

Register a dynamic trim end property.

```csharp
public void RegisterDynamicTrimEnd(string path, System.Func&lt;int,Tizen.UI.Point> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTrimEnd(string,System.Func_int,Tizen.UI.Point_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTrimEnd(string,System.Func_int,Tizen.UI.Point_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')Tizen.UI.Point[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTrimStart(string,System.Func_int,float_)'></a>

## LottieImage.RegisterDynamicTrimStart(string, Func&lt;int,float>) Method

Register a dynamic trim start property.

```csharp
public void RegisterDynamicTrimStart(string path, System.Func&lt;int,float> valueProvider);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTrimStart(string,System.Func_int,float_).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImage.RegisterDynamicTrimStart(string,System.Func_int,float_).valueProvider'></a>

`valueProvider` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.LottieImage.Stop()'></a>

## LottieImage.Stop() Method

Stops the animation.

```csharp
public override void Stop();
```

Implements Stop()
### Events

<a name='Tizen.UI.Components.Material.LottieImage.Finished'></a>

## LottieImage.Finished Event

Event triggered when the animation finishes.

```csharp
public event EventHandler Finished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')














































