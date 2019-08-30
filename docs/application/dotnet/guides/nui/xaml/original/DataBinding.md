# DataBinding

Data bindings allow properties of two objects to be linked so that a change in one causes a change in the other.

The two objects, called the source and the target. The target property must be a bindable property, which means that the target object must derive from <code>BindableObject</code>. A property of <code>TextLabel</code> such as Text is associated with the bindable property <code>TextProperty</code>.

## View-to-View Bindings

You can define data bindings to link properties of two views on the same page. Here’s how you set the data binding in XAML:

• Set the <code> BindingContext </code> property of the target element to an <code>x:Reference</code> markup extension that references the source element.

• Set the target property to a <code> Binding </code> markup extension that references the source property.

Here’s a XAML file that contains a Slider and two Label views, one of which is rotated by the Slider value and another which displays the Slider value:

``` xml
<TextLabel Text="ROTATION" BindingContext="{x:Reference Name=slider}" Position2D="50,50" Rotation="{Binding Path=Value}" Size2D="300,50" HorizontalAlignment="Center" VerticalAlignment="Center" PivotPoint="Center" />

<Slider x:Name="slider" Name="slider" LowerBound="0" UpperBound="360" Value="10" ShowPopup="true" ShowValue="true" ValuePrecision="1" Position2D="50,200" Size2D="300,20" />

<TextLabel BindingContext="{x:Reference slider}" Position2D="50,300" Size2D="300,50" Text="{Binding Value, StringFormat='The angle is {0:F0} degrees'}" />
```

The <code>Slider</code> contains an <code>x:Name</code> attribute that is referenced by the two Label views using the <code>x:Reference</code> markup extension.
You can check the above sample in the **ViewToViewTest** demo.

## Source and BindingContext

The BindingContext property is actually one of two ways to link the source and target objects. You can include a reference to the source object within the binding expression itself.
The **BindingMarkUpExtensionDemo** demo demonstrates how both the source object and source property can be specified in the Binding markup extension:

``` xml
<TextLabel x:Name="label" Name ="label" Text="Text" Position2D="100,100" Size2D="300,50" PositionX="{Binding Source={x:Reference Name=slider}, Path=Value}" />

<Slider x:Name="slider" Name="slider" LowerBound="100" UpperBound="800" Value="100" ShowPopup="true" ShowValue="false" Position2D="400,400" Size2D="300,20" />
```

The <code> Binding </code> markup extension now has two arguments, one of which is another markup extension for <code>x:Reference</code>, so a pair of curly braces are nested within the main curly braces:

``` xml
PositionX="{Binding Source={x:Reference Name=slider}, Path=Value}"
```

You have now seen two ways to specify the link between the source object with the target object:

• Use the <code>BindingContext</code> to reference the source object.

• Use the <code>Source</code> property of the <code>Binding</code> markup extension.

If you specify both, the <code>Source</code> property takes precedence over the <code>BindingContext</code>.

Reference: `https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/xaml-basics/data-binding-basics`
