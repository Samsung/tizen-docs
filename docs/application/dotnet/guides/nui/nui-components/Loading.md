# Loading

Loading is a common component that is used to give information about the ongoing operations.  
Loading indicators display the Loading status of the content or screen. You can use this component if it is not possible to measure the time or progress status.  

Following are the instances where Loading is used:

- When users cannot interact with any other components or content on the current screen while it is Loading, you have to dim the UI or the content. In this case, you can display the Loading indicator in the center of the screen.
- When the content cannot be displayed or the completion time is unpredictable while it is Loading, you can display the Loading indicator over the entire content area.
- When Loading an app, you can display the Loading indicator with the app logo.

![Loading](./media/loading.png)

## Add namespace
To implement loading, include `Tizen.NUI.Components` namespace in your application:

```cs
using Tizen.NUI;
using Tizen.NUI.Components;
```

## Create with property

To create a Loading using property, follow these steps:

1. Create Loading using the default constructor:

    ```cs
    utilityBasicLoading = new Loading();
    ```

2. Set the Loading property:

    ```cs
    string[] imageArray = new string[36];
    for (int i=0; i<36; i++)
    {
        imageArray[i] = "loading_" + i.ToString("00") + ".png";
    }
    utilityBasicLoading.ImageArray = imageArray;
    root.Add(utilityBasicLoading);
    ```

Following output is generated when the Loading is created using property:

![Loading](./media/loading.gif)

## Create with style

To create a Loading using style, follow these steps:

1. Create a style for Loading:

    ```cs
    string[] imageArray = new string[36];
    for (int i=0; i<36; i++)
    {
        imageArray[i] = "loading_" + i.ToString("00") + ".png";
    }
    LoadingStyle style = new LoadingStyle
    {
        ImageArray = imageArray
    };
    ```

2. Use the style to create a Loading and add it to parent:

    ```cs
    utilityBasicLoading = new Loading(style);
    utilityBasicLoading.Position2D = new Position2D(100, 350);
    utilityBasicLoading.Size2D = new Size2D(100, 100);
    root.Add(utilityBasicLoading);
    ```

Following output is generated when the Loading is created using style:

![Loading](./media/loading.gif)

## Create with defined styles

You can define a style based on the user experience (UX) and then use this style to create a Loading.

1. Define a custom style:

    ```cs
    internal class CustomLoadingStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            string[] imageArray = new string[36];
            for (int i=0; i<36; i++)
            {
                imageArray[i] = "loading_" + i.ToString("00") + ".png";
            }
            LoadingStyle style = new LoadingStyle { ImageArray = imageArray };
            return style;
        }
    }
    ```

2. Register your custom style:

    ```cs
    StyleManager.Instance.RegisterStyle("CustomLoading", null, typeof(YourNameSpace.CustomLoadingStyle));
    ```

3. Use your custom style to create a Loading instance:

    ```cs
    utilityBasicLoading = new Loading("CustomLoading");
    utilityBasicLoading.Position2D = new Position2D(100, 350);
    utilityBasicLoading.Size2D = new Size2D(100, 100);
    root.Add(utilityBasicLoading);
    ```

Following output is generated when the Loading is created using the defined style:

![Loading](./media/loading.gif)

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher
