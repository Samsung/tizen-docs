## Selection and other events

To create pagination using property, follow these steps:

1. Create an instance of a `Pagination` class using the default constructor:
    ```xaml
    <comp:Pagination x:Name="_pagination"/>
    ```

2. Set the pagination properties:
   ```xaml
   <comp:Pagination x:Name="_pagination" Size="500,150"
      Name="Pagination1" ParentOrigin="Center" PositionUsesPivotPoint="True" PivotPoint="BottomCenter"
      IndicatorSize="40,40" IndicatorSpacing="60" IndicatorCount="5" "SelectedIndex="1"
      BackgroundColor="0.4f, 0.56f, 1.0f, 0.7f"/>
   ```

    ```csharp
   // Path to the images
   string _imageUrl = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "images/";
   // Specific properties of the pagination
   var _indicatorImageUrlStyle = new PaginationStyle()
   {
      IndicatorImageUrl = new Selector<string>
      {
         Normal = _imageUrl + "circle_unselected.png",
         Selected = _imageUrl + "circle_selected.png"
      }
   };
   _pagination.ApplyStyle(_indicatorImageUrlStyle);
   ```

   To set the absolute path of the images that are used, the `Tizen.Applications.Application.Current.DirectoryInfo.Resource` path is used. For more information, see [Class Application](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Application.html) and [Class DirectoryInfo](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.DirectoryInfo.html).

   You can also set a solid color for the indicators, instead of using images:
   ```xaml
   IndicatorColor="1.0f, 1.0f, 1.0f, 0.5f"
   SelectedIndicatorColor="Black"
   ```

The following output is generated when the pagination is created using the property:

| Indicators with images                               | Solid color indicators                               |
|------------------------------------------------------|------------------------------------------------------|
|![Pagination1a](./media/PaginationExample_Images.png) | ![Pagination1b](./media/PaginationExample_Color.png) |

## Create with style

To create pagination using style, follow these steps:

1. Create a style for pagination:
    ```csharp
   string _imageUrl = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "images/";

    PaginationStyle _style = new PaginationStyle()
    {
        IndicatorSize = new Size(100, 100),
        IndicatorSpacing = 30,
        IndicatorImageUrl = new Selector<string>
        {
            Normal = _imageUrl + "shots.jpg",
            Selected = _imageUrl + "shots.gif"
        },
        Name = "Pagination2",
        Size = new Size(600, 200),
        BackgroundColor = new Color(0.0f, 0.0f, 0.0f, 1.0f)
    };
    ```

2. Use the style to create a new instance of a `Pagination` class:
    ```csharp
    _pagination.ApplyStyle(_indicatorImageUrlStyle);
    _pagination.IndicatorCount = 3;
    _pagination.SelectedIndex = 2;
    ```

The following output is generated when the pagination is created using style:

![Pagination2](./media/PaginationExample_Animated.gif)

## Create with custom styles

You can define a style based on the user experience (UX), and then use the style to create pagination.

1. Define a custom style inside the namespace:
    ```csharp
    internal class CustomPaginationStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            PaginationStyle _style = new PaginationStyle
            {
                IndicatorSize = new Size(100, 100),
                IndicatorSpacing = 50,
                IndicatorImageUrl = new Selector<string>
                {
                    Normal = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "images/gray.png",
                    Selected = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "images/blue.png"
                },
                Name = "Pagination3",
                Size = new Size(500, 200),
                BackgroundColor = new Color(1.0f, 1.0f, 1.0f, 1.0f),
            };
            return _style;
        }
    }
    ```

2. Register your custom style within your namespace:
    ```csharp
    Tizen.NUI.Components.StyleManager.Instance.RegisterStyle("CustomPagination", null, typeof(<YOUR_NAME_SPACE>.CustomPaginationStyle));
    ```

3. Use your custom style to create a new `Pagination` instance:
    ```csharp
    _pagination.ApplyStyle(_indicatorImageUrlStyle);
    _pagination.IndicatorCount = 3;
    _pagination.SelectedIndex = 1;
    ```
The following output is generated when the pagination is created using the defined style:

![Pagination2](./media/PaginationExample_Square.png)

## Respond to window key event

A [Window KeyEvent](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.Window.html#Tizen_NUI_Window_KeyEvent) is associated with the pagination by a method that handles the `Window_KeyEvent` as shown in the following code:
```csharp
Window window = NUIApplication.GetDefaultWindow();
window.KeyEvent += Window_KeyEvent;
```

The method supports pressing the `Left` or `Right` keys, which switches the pagination indicator in the appropriate direction:
```csharp
private void Window_KeyEvent(object sender, Window.KeyEventArgs e)
{
    if (e.Key.State == Key.StateType.Down)
    {
        if (e.Key.KeyPressedName == "Left")
        {
            if (_pagination.SelectedIndex > 0)
            {
                _pagination.SelectedIndex = _pagination.SelectedIndex - 1;
                // Add some additional actions associated with the Left key
            }
        }
        else if (e.Key.KeyPressedName == "Right")
        {
            if (_pagination.SelectedIndex < _pagination.IndicatorCount - 1)
            {
                _pagination.SelectedIndex = _pagination.SelectedIndex + 1;
                // Add some additional actions associated with the Right key
            }
        }
    }
}
```

<!-- uncomment after the review of the sample
[Here](https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/NUI_Pagination) one can find a working example using the above code.
-->
