# Styles

##### Theme Colors

The Tizen offers a single background gradient called “Midday” as the default Home screen background since Tizen SDK 2.4. It captures colors and natural gradients of the sky.


![Midday, the new theme color for the Tizen mobile.](media/2.4_a.png)  
*Midday, the new theme color for the Tizen mobile since Tizen SDK 2.4.*



 

##### Color Swatch

For basic action buttons, such as 'Go' and 'Stop', Tizen 2.4 uses clear and distinct colors for focus and emphasis. Transparency may be applied to text colors to add subtle nuances.


| No.            | Color          | HSB code       | Swatch         | Component      |
|----------------|----------------|----------------|----------------|----------------|
| 1              | White          | \#FFFFFF       | <div style="width: 150px; height:25px; background-color:#FFFFFF; border:1px solid #eeeeee;"></div>         | Primary text / Primary color|
| 2              | Gray           | \#666666       |  <div style="width: 150px; height:25px; background-color:#666666; border:1px solid #eeeeee;"></div>        | Secondary text |
| 3              | Black          | \#000000       | <div style="width: 150px; height:25px; background-color:#000000; border:1px solid #eeeeee;"></div>         | Primary text / Primary color |
| 4              | Green          | \#2AB842       | <div style="width: 150px; height:25px; background-color:#2AB842; border:1px solid #eeeeee;"></div>        | Start          |
| 5              | Red            | \#E12222       | <div style="width: 150px; height:25px; background-color:#E12222; border:1px solid #eeeeee;"></div>          | Stop           |
| 6              | Yellow         | \#FFB400       | <div style="width: 150px; height:25px; background-color:#FFB400; border:1px solid #eeeeee;"></div>          | Snooze, Favorite(star) |


 

##### Font Styles

Different text colors may be used depending on the level of text information and background colors. The following are examples of the primary and secondary text colors in the Tizen Mobile SDK 2.4.

 

<img src="media/2.3_a.png" alt="White text against a dark background (theme color)" style="width:260px;" />  
*White text against a dark background (theme color)*

<img src="media/2.3_b.png" alt="Colored text against a white background" style="width:260px;" />  
*Colored text against a white background*

<img src="media/2.3_c.png" alt="Black primary text against a white background" style="width:260px;" />   
*Black primary text against a white background*

<img src="media/2.3_d.png" alt="Gray secondary text against a light blue background" style="width:260px;" />   
*Gray secondary text against a light blue background*


The following examples show how different text colors appear on the call log screen. White primary text displays well over the header area (dark theme color). Primary text in black and secondary text in gray also look fine over the lightly colored list area.

Once again, the text colors should be decided based on the color of the background. Black or gray text usually fails to stand out against darker backgrounds, resulting in decreased visibility.


 | <img src="media/2.3_g.png" alt="#" style="width:260px;" />| <img src="media/2.3_f.png" alt="#" style="width:260px;" /> |
| :--: | :--: |
| *Do* | *Don't* |



Text with vivid colors, such as red, yellow, blue, and green is not recommended. Such color choice may cause the usability of your design to suffer, because they may impose excessive stress to a user’s vision and distract them.


### List Principles

Tizen mobile devices use multilayered page structure, with the main theme background (gradient) in the bottom layer position. By separating the layers based on their roles, sophisticated effects may be applied on the pages with a minimal set of rules to follow.

The list view is one example that can help you understand how superimposed layers with gradient and text items appear against the background. Semi-transparent stripes of gradient on top of the main background create subtle dividers for each list item, above which list item text layer is placed.

<img alt="Multilayered screen structurecreated by layers of different opacities over the background gradient." src="media/2.4.3_c.png" style="height:300px; margin-right:4px;" /><img alt="Multilayered screen structurecreated by layers of different opacities over the background gradient." src="media/2.2.2_a.png" style="height:300px; margin-right:4px;" />  
*Multilayered screen structurecreated by layers of different opacities over the background gradient.*



Different opacity levels on a list create an interesting gradient. On the item list layer, the opacity level of the first list item is 100 percent, and it decreases by 4 percent for each item after it until the twentieth item. After the twentieth item, the opacity level begins to increase by 4 percent until it reaches 100 percent again.

<img alt="Scrolling a list" src="media/list_scroll.png" style="width:91%;" />  
*Scrolling a list*
