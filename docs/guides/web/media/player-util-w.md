# Audio Latency

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

Tizen enables you to control the audio latency mode of the W3C player.

This feature is supported in mobile and wearable applications only.

The main features of the Player Util API include:

- Getting the latency mode	

  You can [get the current latency mode of the player](./media/player-util-w.md#get) with the `getLatencyMode()` method.

- Setting the latency mode	

  You can [set the latency mode of the player](./media/player-util-w.md#set) with the `setLatencyMode()` method.

## Getting the Current Latency Mode

To get the current latency mode, use the `getLatencyMode()` method:

```
var latencyMode;
try {
    latencyMode = tizen.playerutil.getLatencyMode();
} catch (error) {
    console.log(error.name + ': ' + error.message);
}
```

## Setting the Latency Mode

To set a new latency mode, use one of the available modes defined in the `LatencyMode` enumerator (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/playerutil.html#LatencyMode) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/playerutil.html#LatencyMode) applications):

```
try {
    tizen.playerutil.setLatencyMode('HIGH');
} catch (error) {
    console.log(error.name + ': ' + error.message);
}
```