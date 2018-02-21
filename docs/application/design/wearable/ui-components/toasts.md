# Toasts

Toasts display information and disappear automatically after 2 seconds. They're useful when you want to show simple and short bites of information. For more important messages, use a pop-up that requires confirmation. Using a graphic toast can help users understand information more easily.

## Usage

You can use toasts to show the result of non-critical actions and provide simple information on the app's current status.

## Behavior

-   **Automatic expiration**

    Toasts do not require user confirmation. They automatically expire after a 2-second timeout. Users can tap the screen to close a toast before it disappears automatically.

-   **No scrolling**

    Toasts don't allow scrolling. If you have long text that doesn't fit on one screen, use a confirmation pop-up instead.

## Types

-   **Graphic toasts**

  A graphic toast displays an icon or an icon with short text. You can provide up to 2 lines of text below the icon. Keep this text as short and simple as possible, for example Photo deleted, Message sent, or Update shared. You can use a [common set](http://developer.samsung.com/gear/design/resource/basic-ui) to minimize fragmentation, or use your own customized icon to express your app's identity.

|**Graphic toast pop-up**|  |
|-------------|-------------|
|    **Native**|Pop-up > toast/circle<br>(+ Displayed with an icon)|
|    **Web** |    -        |

  ![](media/ui_components_10.4.3_1-850x174.png)  
  *A graphic toast indicates a success/failure of an operation with a corresponding icon (V/X).*

-   **Text toasts**

    A text toast is useful when it's difficult to convey a message with an image. The text can be up to 3 lines long.

|**Text toast pop-up** in developer's guides|         |
|---------------------|---------|
|    **Native**     |  Pop-up > toast/circle|
|    **Web**        |  Pop-up > toast|

  ![](media/ui_components_10.4.3_2-850x174.png)  
  *A text toast communicates simple information that is hard to express with an image.*
