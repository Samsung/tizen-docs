# Progress

Progress is a common component that is used to show the ongoing status using a long narrow bar.

Following are the instances where Progress is used:

- To show the processing time
- To show the number of items in Progress
- To show the Progress rate depending on the screen layout

![Progress](./media/progress.png)

## Add namespace
To implement progress, include `Tizen.NUI.Components` namespace in your application:

```cs
using Tizen.NUI;
using Tizen.NUI.Components;
```

## Create with property

To create a Progress using property, follow these steps:

1. Create Progress using the default constructor:

    ```cs
    utilityBasicProgress = new Progress();
    ```

2. Set the Progress property:

    ```cs
    utilityBasicProgress.MaxValue = 100;
    utilityBasicProgress.MinValue = 0;
    utilityBasicProgress.CurrentValue = 45;
    utilityBasicProgress.TrackColor = Color.Green;
    utilityBasicProgress.ProgressColor = Color.Black;
    ```

Following output is generated when the Progress is created using property:

![Progress](./media/progress.gif)

## Create with style

To create a Progress using style, follow these steps:

1. Create a style for Progress:

    ```cs
    ProgressStyle style = new ProgressStyle
    {
        Track = new ImageViewStyle
        {
            BackgroundColor = Color.Cyan
        },
        Progress = new ImageViewStyle
        {
            BackgroundColor = Color.Black
        }
    };
    ```

2. Use the style to create a Progress and add it to parent:

    ```cs
    utilityBasicProgress = new Progress(style);
    utilityBasicProgress.Size = new Size(140, 4);
    utilityBasicProgress.MaxValue = 100;
    utilityBasicProgress.MinValue = 0;
    utilityBasicProgress.CurrentValue = 45;
    root.Add(utilityBasicProgress);
    ```

Following output is generated when the Progress is created using style:

![Progress](./media/progress.gif)

## Create with defined styles

You can define a style based on the user experience (UX) and then use this style to create a Progress.

1. Define a custom style:

    ```cs
    internal class CustomProgressStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            ProgressStyle style = new ProgressStyle
            {
                Track = new ImageViewStyle
                {
                    BackgroundColor = Color.Cyan
                },
                Progress = new ImageViewStyle
                {
                    BackgroundColor = Color.Black
                }
            };
            return style;
        }
    }
    ```

2. Register your custom style:

    ```cs
    StyleManager.Instance.RegisterStyle("CustomProgress", null, typeof(YourNameSpace.CustomProgressStyle));
    ```

3. Use your custom style to create a Progress instance:

    ```cs
    utilityBasicProgress = new Progress("CustomProgress");
    utilityBasicProgress.Size = new Size(140, 4);
    utilityBasicProgress.MaxValue = 100;
    utilityBasicProgress.MinValue = 0;
    utilityBasicProgress.CurrentValue = 45;
    root.Add(utilityBasicProgress);
    ```

Following output is generated when the Progress is created using the defined style:

![Progress](./media/progress.gif)

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher