# Display

Screen resolutions vary from device to device. When designing layouts for your applications, make sure you consider the range of possible resolutions, as well as both landscape and portrait screen orientations.


## Resolution




Tizen 2.3 offers UI components for WVGA (480 x 800), HD (720 x 1280) and FHD (1080 x 1920) resolutions, so you can choose the components most suitable for your target device. All resolutions have the same basic layout, so when they are displayed in the screen of the same width, the size of the text and height of the list appear identical. However, due to difference in the ratio, the FHD resolution can display more content. Text size and other components must be adjusted in a smaller screen to provide enough touch space.

 

**Figure: WVGA, HD and FHD resolutions**  
<img alt="" height="427" src="media/display_resolutions_02.png" width="740" />
 



## Screen Orientation




Tizen 2.3 supports both landscape and portrait modes.

In the main body content, component sizes, such as text and list height, do not change in the list view between different modes. However, in the grid view where the layout depends on the ratio of the display area, the sizes do change.

 

**Figure: Screen orientation with a list view**  
<img alt="" height="400" src="media/display_listview.png" width="650" />
 

**Figure: Screen orientation with a grid view**  
<img alt="" height="400" src="media/display_gridview.png" width="650" />
