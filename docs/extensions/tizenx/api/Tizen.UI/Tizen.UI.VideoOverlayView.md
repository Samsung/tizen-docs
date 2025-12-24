### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## VideoOverlayView Class

VideoOverlayView is a class that displays video content on the screen.

```csharp
public class VideoOverlayView : Tizen.UI.View,
Tizen.UI.Internal.IResourceReadySignalHandler
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; VideoOverlayView

Implements [Tizen.UI.Internal.IResourceReadySignalHandler](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.IResourceReadySignalHandler 'Tizen.UI.Internal.IResourceReadySignalHandler')
### Constructors

<a name='Tizen.UI.VideoOverlayView.VideoOverlayView()'></a>

## VideoOverlayView() Constructor

Constructor of VideoOverlayView.

```csharp
public VideoOverlayView();
```
### Properties

<a name='Tizen.UI.VideoOverlayView.DisplayArea'></a>

## VideoOverlayView.DisplayArea Property

Gets the display area of the video.

```csharp
public Tizen.UI.Rect DisplayArea { get; }
```

#### Property Value
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')
### Methods

<a name='Tizen.UI.VideoOverlayView.SetPlayer(Player)'></a>

## VideoOverlayView.SetPlayer(Player) Method

Sets the player instance to be used to display media by the VideoOverlayView.

```csharp
public void SetPlayer(Player player);
```
#### Parameters

<a name='Tizen.UI.VideoOverlayView.SetPlayer(Player).player'></a>

`player` [Tizen.Multimedia.Player](https://docs.microsoft.com/en-us/dotnet/api/Tizen.Multimedia.Player 'Tizen.Multimedia.Player')

The player instance to be used.




