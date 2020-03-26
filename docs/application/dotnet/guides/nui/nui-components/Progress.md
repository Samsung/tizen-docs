# Progress

Progress is a common component that is used to show the ongoing status using a long narrow bar.

Following are the instances where progress is used:

- To show the processing time
- To show the number of items in progress
- To show the progress rate depending on the screen layout

![Progress](./media/progress.png)

## Create with Property

To create a progress using property, follow these steps:

1. Create progress using the default constructor:

    ```cs
    utilityBasicProgress = new Progress();
    ```

2. Set the progress property:

    ```cs
    utilityBasicProgress.MaxValue = 100;
    utilityBasicProgress.MinValue = 0;
    utilityBasicProgress.CurrentValue = 45;
    utilityBasicProgress.TrackColor = Color.Green;
    utilityBasicProgress.ProgressColor = Color.Black;
    ```

Following output is generated when the progress is created using property:

![Progress](./media/progress.gif)

## Create with style

To create a progress using style, follow these steps:

1. Create progress style

    ```cs
    ProgressStyle style = new ProgressStyle
    {
        Track = new ImageViewStyle
        {
            BackgroundColor = Color.Cyan,
        },
        Progress = new ImageViewStyle
        {
            BackgroundColor = Color.Black,
        },
    };
    ```

2. Use the style to create a progress and add it to parent

```cs
utilityBasicProgress = new Progress(style);
utilityBasicProgress.Size = new Size(140, 4);
utilityBasicProgress.MaxValue = 100;
utilityBasicProgress.MinValue = 0;
utilityBasicProgress.CurrentValue = 45;
root.Add(utilityBasicProgress);
```

Following output is generated when the progress is created using style:

![Progress](./media/progress.gif)

## Create with defined styles

You can define a style according to the UX, then you can use the this style to ceate a progress.

1. User define a custom style as the whole view.

    ```cs
    internal class CustomProgressStyle : StyleBase
    {
        protected override ViewStyle GetViewStyle()
        {
            ProgressStyle style = new ProgressStyle
            {
                Track = new ImageViewStyle
                {
                    BackgroundColor = Color.Cyan,
                },
                Progress = new ImageViewStyle
                {
                    BackgroundColor = Color.Black,
                },
            };
            return style;
        }
    }
    ```

2. Register your custom style.

    ```cs
    StyleManager.Instance.RegisterStyle("CustomProgress", null, typeof(YourNameSpace.CustomProgressStyle));
    ```

3. Use your custom style to create a progress instance

    ```cs
    utilityBasicProgress = new Progress("CustomProgress");
    utilityBasicProgress.Size = new Size(140, 4);
    utilityBasicProgress.MaxValue = 100;
    utilityBasicProgress.MinValue = 0;
    utilityBasicProgress.CurrentValue = 45;
    root.Add(utilityBasicProgress);
    ```

Following output is generated when the progress is created using defined style:

![Progress](./media/progress.gif)

## Related Information

- Dependencies
  -   Tizen 5.5 and Higher