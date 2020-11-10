# LottieAnimationView
LottieAnimationView is a common component that is used to show a vector animation. It parses the Adobe After Effects® animations exported as JSON with Bodymovin and renders them.

![LottieAnimationView](./media/lottie.gif)

## Create with property

To create a LottieAnimationView using property, follow these steps:

1. Create LottieAnimationView using the default constructor:

    ```csharp
    lottieAnimationView = new LottieAnimationView();
    ```

2. Set the properties:

    ```csharp
    lottieAnimationView.Size = new Size(100, 108);
    lottieAnimationView.URL = "myLottie.json"
    lottieAnimationView.LoopCount = 3;
    lottieAnimationView.StopBehavior = StopBehaviorType.CurrentFrame;
    lottieAnimationView.CurrentFrame = 20;

    lottieAnimationView.SetMinMaxFrame(10, 30);

    parent.Add(lottieAnimationView);
    ```

## Control animation playback
After the view is created, you can control its playback:

```csharp
lottieAnimationView.Play();
lottieAnimationView.Pause();
lottieAnimationView.Stop();
```

## Event handling
You can receive an event when the animation finishes:

```csharp
lottieAnimationView.Finished += OnAnimationFinished;
```

```csharp
private void OnAnimationFinished(object sender)
{
  // Do something
}
```

## Related information
- Dependencies
  -   Tizen 5.5 and Higher
