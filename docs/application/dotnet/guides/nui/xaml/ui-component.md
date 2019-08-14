# How to define the UI Component in XAML

## XAML Object Elements

Object element syntax always starts with an opening angle bracket (<). This is followed by the name of the type where you want to create an instance. After this, you can optionally declare attributes on the object element. To complete the object element tag, end with a forward slash and closing angle bracket in succession (/>). For example:

``` xml
<TextLabel Text="TextLabel"/>
```

The <code>TextLabel</code> instance is created by calling the default constructor of the underlying type when parsing and loading the XAML.

## Parent and Child

If you want to add a child view to the Parent View, You can do it like this:

``` xml
<View>
  <TextLabel Text="TextLabel"/>
</View>
```

The <code>TextLabel</code> instance will be add to the <code>View</code> instance.

## Attribute Syntax (Properties)

An attribute syntax names the property that is being set in attribute syntax, followed by the assignment operator (=). The value of an attribute is always specified as a string that is contained within quotation marks. For example, the following markup creates a <code> TextLabel</code> that has red text and a blue background in addition to display text specified as TextLabel.

``` xml
<TextLabel TextColor="Red" BackgroundColor="Blue" Text="TextLabel" />
```

In the above sample, we can use string "Red" and "Blue" to set the <code>Color</code>, because there is a [TypeConverter](./TypeConverter.md).

## Property Element Syntax

The syntax for the property element start tag is <typeName.propertyName>. The content of that tag is an object element of the type that the property takes as its value . After specifying content, you must close the property element with an end tag. The syntax for the end tag is </typeName.propertyName>.

The following example shows the same properties being set as in the previous attribute syntax example, but this time by using property element syntax for all properties of the <code>TextLabel</code>.

``` xml
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

Sometimes particular property takes a collection type, like the <code>ImageView.Image</code> property, you can set the Property like this:

``` xml
<ImageView PositionX="10" PositionY="320" Size2D="300, 300" PixelArea="0.1,0.0,0.4,0.6" >
  <ImageView.Image>
    <PropertyMap>
      <KeyValue Key="Visual.Property.Type" Value="{VisualType Image}" />
      <KeyValue Key="ImageVisualProperty.URL" Value="{x:String ImageResourcepatch}" />
    </PropertyMap>
  </ImageView.Image>
</ImageView>
```

If the type of the property is an array, you can use the <code>x:Array</code> Markup Extension to implement that.

Reference: `https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/markup-extensions/consuming`

## Events and Callback

Attribute syntax can also be used for events. In this case, the attribute's name is the name of the event. In the Tizen.NUI implementation of events for XAML, the attribute's value is the name of a handler that implements that event's delegate. For example, the following markup assigns a handler for the Click event to a PushButton created in markup:

``` xml
<ContentPage x:Class="Tizen.NUI.Examples.TestEventHandler"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <PushButton Name="PushButton" PositionX="100" PositionY="100" LabelText="PushButton" Size2D="260, 84" Clicked="OnClicked" />
</ContentPage>
```

You should define the event handle in the partial class within the CLR namespace identified by x:Class. :

``` csharp
public class TestEventHandler : ContentPage
{

    public TestEventHandler(Window win) : base(win)
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

You can check it in the **TestMultiResolutionSample** sample.

## x:Arguments

In above samples, each element in the XAML file is instantiated with a call to the parameterless constructor of the corresponding class or structure. <code>x:Arguments</code> element support to instantiate objects with constructors that require arguments.
The following code example demonstrates using the x:Arguments attribute with <code>ImageView</code>:

``` xml
<ImageView Name="img1" Position2D="0,0" Size2D="400,400" >
  <x:Arguments>
    <x:String>../../res/images/AmbientScreenUXControl/Cut/traffic_content.png</x:String>
  </x:Arguments>
</ImageView>
```

Reference:
`https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/passing-arguments`
