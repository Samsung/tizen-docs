# Loading

Loading is a common component that is used to give information about the ongoing operations.  
Loading indicators display the loading status of the content or screen. You can use this component if it is not possible to measure the time or progress status.  

Following are the instances where loading is used:

- When users cannot interact with any other components or content on the current screen while it is loading, you have to dim the UI or the content. In this case, you can display the loading indicator in the center of the screen.
- When the content cannot be displayed or the completion time is unpredictable while it is loading, you can display the loading indicator over the entire content area.
- When loading an app, you can display the loading indicator with the app logo.

![Loading](./media/loading.png)

## Create with Property

To create a loading using property, follow these steps:

1. Create loading using the default constructor:

    ```cs
    utilityBasicLoading = new Loading();
    ```

2. Set the loading property:

    ```cs
    string[] imageArray = new string[36];
    for (int i=0; i<36; i++)
    {
        imageArray[i] = "loading_" + i.ToString("00") + ".png";
    }
    utilityBasicLoading.ImageArray = imageArray;
    root.Add(utilityBasicLoading);
    ```

Following output is generated when the loading is created using property:

![Loading](./media/loading.gif)

## Create with style

To create a loading using style, follow these steps:

1. Create loading style

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

2. Use the style to create a loading and add it to parent

    ```cs
    utilityBasicLoading = new Loading(style);
    utilityBasicLoading.Position2D = new Position2D(100, 350);
    utilityBasicLoading.Size2D = new Size2D(100, 100);
    root.Add(utilityBasicLoading);
    ```

Following output is generated when the loading is created using style:

![Loading](./media/loading.gif)

## Create with defined styles

You can define a style according to the UX, then you can use the this style to ceate a loading.

1. User define a custom style as the whole view.

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

2. Register your custom style.

    ```cs
    StyleManager.Instance.RegisterStyle("CustomLoading", null, typeof(YourNameSpace.CustomLoadingStyle));
    ```

3. Use your custom style to create a loading instance

    ```cs
    utilityBasicLoading = new Loading("CustomLoading");
    utilityBasicLoading.Position2D = new Position2D(100, 350);
    utilityBasicLoading.Size2D = new Size2D(100, 100);
    root.Add(utilityBasicLoading);
    ```

Following output is generated when the loading is created using defined style:

![Loading](./media/loading.gif)

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher
