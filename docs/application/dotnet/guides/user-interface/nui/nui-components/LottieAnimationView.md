# LottieAnimationView
LottieAnimationView is a common component that is used to show a vector animation. It parses the Adobe After Effects® animations exported as JSON with Bodymovin and renders them.

![LottieAnimationView](./media/lottie.gif)

## Create with property

To create a LottieAnimationView using property, follow these steps:

1. Create LottieAnimationView using the default constructor:

    ```xaml
    <base:LottieAnimationView x:Name="lottie"/>
    ```

2. Set the properties:

    ```xaml
    <base:LottieAnimationView x:Name="lottie" 
	LoopCount="3" 
	WidthSpecification="100"
	HeightSpecification="108"
	URL="myLottie.json"
	StopBegavior="CurrentFrame"
	CurrentFrame="20"
	/>
    ```

## Control animation playback
After the view is created, you can control its playback:

```csharp
lottie.Play();
lottie.Pause();
lottie.Stop();
```

## Handle events
You can receive an event when the animation finishes:

```xaml
<base:LottieAnimationView x:Name="lottie" Finished="OnAnimationFinished"/>
```

```csharp
private void OnAnimationFinished(object sender, EventArgs e)
{
  // Do something
}
```

## Related information

- Dependencies
  -   Tizen 6.5 and Higher

- API References
  - [LottieAnimationView API](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.BaseComponents.LottieAnimationView.html)
