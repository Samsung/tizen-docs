# Swipe to Refresh



This gesture is used when users want to load more content than is currently displayed in an app. It comes in handy when an app’s content is updated in real-time, or when an app provides content to browse through.

At the top of content, users swipe down or rotate the bezel counterclockwise to refresh. Conversely, they swipe up or rotate the bezel clockwise when they’ve reached the bottom of content. Refer to [Swipe](../interaction/touch.mdl#swipe) for more details.

When content is refreshing, provide feedback such as a progress bar to indicate that content is being loading.
<a name="update"></a>
## Update content

Users can refresh to load new emails in a mailing app or update the news feed in a news app. Of course it’s best if the app updates automatically, but users should also be able to choose to manually trigger an update when they want.

 

![](media/pattern_9.14.1_1-850x174.png)  
          Displaying overscroll effect                               Load more or read more content

![](media/pattern_9.14.1_2-850x206.png)  
          Displaying overscroll effect                               Load more or read more content

*Swiping down or rotating the bezel counterclockwise updates content.*

## Load more content

Refreshing can also load more content than is currently displayed. Content is loaded when users swipe up or rotate the bezel clockwise at the bottom of content collections.

![](media/pattern_9.14.2_1-850x174.png)  
         Displaying overscroll effect                                 Load more or read more content


![](media/pattern_9.14.2_2-850x206.png)  
          Displaying overscroll effect                                Load more or read more content


> **Tip**  
> -  Home screen, widgets, and pop-ups can’t load more content through refreshing.
> -  A progress bar is displayed at the center of the empty space where the refreshed content will appear and should remain there until the new content is fully loaded.
