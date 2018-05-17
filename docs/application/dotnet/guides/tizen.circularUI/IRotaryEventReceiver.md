---
uid: Tizen.Wearable.CircularUI.doc.IRotaryEventReceiver
summary: IRotaryEventReceiver guide
---

# IRotaryEventReceiver
`IRotaryEventReceiver` is a receiver interface to take a rotary event. `IRotaryEventReceiver` has `Rotate(RotaryEventArgs)` method that is called when rotary event is occurred. You can simply handle of rotary event using this interface. Such as below sample, you can easily rotate image according to bezel rotation.

## Adding IRotaryEventReceiver
Add `IRotaryEventReceiver` interface to `CirclePage` or `Page` having [CircleSurfaceEffectBehavior](xref:Tizen.Wearable.CircularUI.doc.CircleSurfaceEffectBehavior). Implement `Rotate()` method to control a rotary event. `RotaryEventArgs` is event argument for the Rotary Event.
`RotaryEventArgs.IsClockwise` gets the direction of bezel rotation. If the device has rotated in the clockwise direction, `IsClockwise` is `true`.
Below sample receives rotary event at `Rotate()` method and add angle of the image following to rotary event direction. And then rotate the image.

_This guide's code example uses WearableUIGallery's TCIRotaryEventReceiver code at the test\WearableUIGallery\WearableUIGallery\TC\TCIRotaryEventReceiver.xaml_

For more information. Please refer to [IRotaryEventReceiver API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.IRotaryEventReceiver.html)

**C# file**
```cs
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class TCIRotaryEventReceiver : CirclePage, IRotaryEventReceiver
    {
        bool _rotating;
        double _angle;
        public TCIRotaryEventReceiver ()
        {
            InitializeComponent ();
            _angle = 0;
        }

        public void Rotate(RotaryEventArgs args)
        {
            if (_rotating) return;

            _rotating = true;
            _angle += args.IsClockwise ? 30 : -30;
            Cat.RotateTo(_angle).ContinueWith(
                (b) =>
                {
                    _rotating = false;
                    if (_angle == 360)
                    {
                        Cat.Rotation = 0;
                        _angle = 0;
                    }
                });
        }
    }
```

**XAML file**
```xml
    <w:CirclePage.Content>
        <Image x:Name="Cat" Source="image/cat360.png" />
    </w:CirclePage.Content>
```