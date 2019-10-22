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

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher
