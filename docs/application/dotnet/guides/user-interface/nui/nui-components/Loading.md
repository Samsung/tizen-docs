# Loading

Loading is a common component that is used to give information about ongoing operations.
Loading indicators display the loading status of the content on the screen. You can use this component if it is not possible to measure the time or progress status. 

The following are the instances where Loading is used:

- When users cannot interact with any other components or content on the current screen while it is loading, you have to dim the UI or the content. In this case, you can display the Loading indicator in the center of the screen.
- When the content cannot be displayed or the completion time is unpredictable while it is loading, you can display the Loading indicator over the entire content area.
- When loading an app, you can display the Loading indicator with the app logo.

![Loading](./media/loading.png)

## Add namespace
To implement Loading, include `Tizen.NUI.Components` namespace in your application:

```xaml
xmlns:base="clr-namespace:Tizen.NUI.BaseComponents;assembly=Tizen.NUI"
xmlns:comp="clr-namespace:Tizen.NUI.Components;assembly=Tizen.NUI.Components"
```

## Create with property

To create a Loading using property, follow these steps:

1. Create Loading using the default constructor:

    ```xaml
    <Loading x:Name="loading" WidthSpecification="-1" HeightSpecification="-1"/>
    ```

2. Set the Loading property:

    ```csharp
    string[] imageArray = new string[36];
    for (int i=0; i<36; i++)
    {
        imageArray[i] = "loading_" + i.ToString("00") + ".png";
    }
    loading.ImageArray = imageArray;
    ```

The following output is generated when the Loading is created using property:

![Loading](./media/loading.gif)

## Related information

- Dependencies
  -   Tizen 6.5 and Higher 
