---
uid: Tizen.Wearable.CircularUI.doc.IRotaryEventReceiver
summary: IRotaryEventReceiver guide
---

# IRotaryEventReceiver
`IRotaryEventReceiver` is a receiver interface to receive [Rotary event](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/event-handling#rotary). When a rotary event occur, `IRotaryEventReceiver` calls `Rotate(RotaryEventArgs)` method. You can control the [Rotary event](https://developer.tizen.org/development/training/native-application/understanding-tizen-programming/event-handling#rotary) using this interface. If you read the following paragraphs, you can easily rotate image according to bezel rotation.

## Add IRotaryEventReceiver
Add `IRotaryEventReceiver` interface to `CirclePage` or `Page` having [CircleSurfaceEffectBehavior](xref:Tizen.Wearable.CircularUI.doc.CircleSurfaceEffectBehavior). Implement `Rotate()` method to control a rotary event. `RotaryEventArgs` is event argument for the Rotary Event.
`RotaryEventArgs.IsClockwise` gets the direction of bezel rotation. `IsClockwise` is `true`, when the device is rotated in the clockwise direction.
The following sample receives rotary event at `Rotate()` method and add angle of the image following to rotary event direction. And then rotate the image.

For more information, see [IRotaryEventReceiver API reference](https://samsung.github.io/Tizen.CircularUI/api/Tizen.Wearable.CircularUI.Forms.IRotaryEventReceiver.html).

_The code example of this guide uses TCIRotaryEventReceiver code of WearableUIGallery. The code is available in test\WearableUIGallery\WearableUIGallery\TC\TCIRotaryEventReceiver.xaml_

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