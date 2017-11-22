# Control
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 3.0 and Higher for Wearable

The `Dali::Toolkit::Control` class is the base class for all UI components in DALi. With this class, you can, for example, manage the background color and images for UI components.

## Setting the Background Color

You can set a background color for a UI component. To set a red background for a component:

```
Control control = Control::New();
control.SetSize( 200.0f, 200.0f );
control.SetBackgroundColor( Color::RED );
```

**Figure: Control object with a red background**

![Control object with a red background](./media/background_control_color.png)

You can handle all existing controls similarly. For example, to set the background color for a TextLabel:

```
TextLabel label = TextLabel::New( "Hello World" );
label.SetBackgroundColor( Dali::Color::RED );
```

**Figure: TextLabel object with a red background**

![TextLabel object with a red background](./media/background_textlabel.png)

## Setting the Background Image

You can set a background image of a control:

```
Control control = Control::New();
Image image = Image::New( "image.png" );
control.SetBackgroundImage( image );
```

**Figure: Control object with a background image**

![Control object with a background image](./media/background_image.png)