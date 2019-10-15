# Progress
It's used to show the ongoing status with a long narrow bar.

![Progress](./media/progress.png)

## Overview
Progress is a kind of common component and  used to show the ongoing status with a long narrow bar. This is useful in a long list of items or to show the processing time.

- Use progress to show the number of items in progress or the processing time.
- Use progress to show the progress rate, depending on the screen layout.

## Create with property
1. Create Progress by default constructor

~~~{.cs}
utilityBasicProgress = new Progress();
~~~

2. Set progress property

~~~{.cs}
utilityBasicProgress.MaxValue = 100;
utilityBasicProgress.MinValue = 0;
utilityBasicProgress.CurrentValue = 45;
utilityBasicProgress.TrackColor = Color.Green;
utilityBasicProgress.ProgressColor = Color.Black;
~~~

Progress created by property:

![Progress](./media/progress.gif)

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher