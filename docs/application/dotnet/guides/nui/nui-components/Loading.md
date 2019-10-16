# Loading
This tutorial describes how to create and use loading.

![Loading](./media/loading.png)

## Overview
Loading is a kind of common component and it's used to indicate informs users of the ongoing operation.

- Loading indicators display the loading status of the content or screen.
- Use this component if it is not possible to measure the time or progress status.
- If users cannot interact with any other components or content on the current screen while it is loading, dim the UI or content and display the loading indicator in the center of the screen.
- If the content cannot be displayed or the completion time is unpredictable while it is loading, display the loading indicator over the whole content area.
- While loading an app, display the loading indicator with the app logo.

## Create with property
1. Create Loading by default constructor

~~~{.cs}
utilityBasicLoading = new Loading();
~~~

2. Set loading property

~~~{.cs}
string[] imageArray = new string[36];
for (int i=0; i<36; i++)
{
    
    imageArray[i] = "loading_" + i.ToString("00") + ".png";
}
utilityBasicLoading.ImageArray = imageArray;
~~~


Loading created by property:

![Loading](./media/loading.gif)

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher
