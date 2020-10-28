# Define UI Components in XAML

## XAML Object Elements

Object element syntax always starts with an opening angle bracket (<). This is followed by the name of the type where you want to create an instance. After this, you can optionally declare attributes on the object element. To complete the object element tag, end with a forward slash and closing angle bracket in succession (/>). The following example shows how to write an object element syntax:

```xml
<TextLabel Text="TextLabel"/>
```

The `TextLabel` instance is created by calling the default constructor of the underlying type when parsing and loading the XAML.

## Parent and Child

The following example shows how to add a child view to the parent view:

```xml
<View>
  <TextLabel Text="TextLabel"/>
</View>
```

The `TextLabel` instance will be added to the `View` instance.

## Attribute Syntax Properties

An attribute syntax names the property that is being set in the attribute syntax, followed by the assignment operator (=). The value of an attribute is always specified as a string that is contained within the quotation marks. For example, the following markup creates a `TextLabel` that has a red text and a blue background in addition to the display text specified as `TextLabel`.

```xml
<TextLabel TextColor="Red" BackgroundColor="Blue" Text="TextLabel" />
```

In the preceding sample, we can use the string **Red** and **Blue** to set color, because there is a **TypeConverter**.

## Property Element Syntax

The syntax for the property element start tag is `<typeName.propertyName>`. The content of that tag is an object element of the type that the property takes as its value . After specifying content, you must close the property element with an end tag. The syntax for the end tag is `</typeName.propertyName>`.

The following example shows the same properties being set as in the previous attribute syntax example, but this time by using property element syntax for all properties of the `TextLabel`:

```xml
<TextLabel>
  <TextLabel.TextColor>
    Red
  </TextLabel.TextColor>
  <TextLabel.BackgroundColor>
    Blue
  </TextLabel.BackgroundColor>
  <TextLabel.Text>
    TextLabel
  </TextLabel.Text>
</TextLabel>
```

## Collection Syntax

In some cases, particular property takes a collection type, such as the `ImageView.Image` property. The following example shows the syntax to set the property in the collection type:

```xml
<ImageView PositionX="10" PositionY="320" Size2D="300, 300" PixelArea="0.1,0.0,0.4,0.6" >
  <ImageView.Image>
    <PropertyMap>
      <KeyValue Key="Visual.Property.Type" Value="{VisualType Image}" />
      <KeyValue Key="ImageVisualProperty.URL" Value="{x:String ImageResourcepatch}" />
    </PropertyMap>
  </ImageView.Image>
</ImageView>
```

If the type of the property is an array, you can use the `x:Array` markup extension to implement it.

For more information, see https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/markup-extensions/consuming.

## Events and Callback

Attribute syntax can also be used for events. In this case, the attribute's name is the name of the event. In the Tizen.NUI implementation of events for XAML, the attribute's value is the name of a handler that implements that event's delegate.
For example, the following markup assigns a handler for the `Click` event to a `PushButton` created in markup:

```xml
<View x:Class="Tizen.NUI.Examples.TestEventHandler"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <PushButton Name="PushButton" PositionX="100" PositionY="100" LabelText="PushButton" Size2D="260, 84" Clicked="OnClicked" />
</View>
```

You must define the event handle in the partial class within the CLR namespace identified by `x:Class`:

```csharp
public class TestEventHandler : View
{

    public TestEventHandler() : base()
    {
       InitializeComponent();
    }

    private bool OnClicked(object sender, EventArgs e)
    {
        if (sender is Button)
        {
            Button button = sender as Button;
            button.LabelText = "Click Me";
        }
        return true;
    }
}
```

## x:Arguments

In the preceding examples explained in this file, each element in the XAML file is instantiated with a call.
The XAML file can either instantiate a call to the parameterless constructor of the corresponding class or to a structure.
The `x:Arguments` element supports instantiating objects with constructors that require arguments.
The following code example demonstrates using the `x:Arguments` attribute with `ImageView`:

```xml
<ImageView Name="img1" Position2D="0,0" Size2D="400,400" >
  <x:Arguments>
    <x:String>*Resource*/res/traffic_content.png</x:String>
  </x:Arguments>
</ImageView>
```

For more information, see [Passing Arguments in XAML](https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/passing-arguments).
