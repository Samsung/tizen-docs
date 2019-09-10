# Data Binding
Data bindings allow the properties of two objects to be linked together. Therefore, a change of one property causes the corresponding change of the other property.
There are two objects, the source and the target. The target property must be a bindable property, which means that the target object must derive from `BindableObject`. A property of `TextLabel` such as Text is associated with the bindable property `TextProperty`.

## View-to-View Bindings
You can define data bindings to link properties of two views on the same page. You can set the data binding in XAML using the following code:

- Set the `BindingContext` property of the target element to an `x:Reference` markup extension that references the source element.
- Set the target property to a `Binding` markup extension that references the source property.

Following is a XAML file that contains a `Slider` and two `TextLabel` views. One of the `TextLabel` view is rotated by the `Slider` value and the other displays the `Slider` value.

``` xaml
<TextLabel Text="ROTATION" BindingContext="{x:Reference Name=slider}" Position2D="50,50" Rotation="{Binding Path=Value}" Size2D="300,50" HorizontalAlignment="Center" VerticalAlignment="Center" PivotPoint="Center" />

<Slider x:Name="slider" Name="slider" LowerBound="0" UpperBound="360" Value="10" ShowPopup="true" ShowValue="true" ValuePrecision="1" Position2D="50,200" Size2D="300,20" />

<TextLabel BindingContext="{x:Reference slider}" Position2D="50,300" Size2D="300,50" Text="{Binding Value, StringFormat='The angle is {0:F0} degrees'}" /> 
```

The `Slider` contains an `x:Name` attribute that is referenced by the two `TextLabel`views using the `x:Reference` markup extension.

## Source and BindingContext
The `BindingContext` property is one of the two ways to link the source and target objects. You can include a reference to the source object within the binding expression.
The following code shows how the source object and source property can be specified in the Binding markup extension:

``` xaml
<TextLabel x:Name="label" Name ="label" Text="Text" Position2D="100,100" Size2D="300,50" PositionX="{Binding Source={x:Reference Name=slider}, Path=Value}" />

<Slider x:Name="slider" Name="slider" LowerBound="100" UpperBound="800" Value="100" ShowPopup="true" ShowValue="false" Position2D="400,400" Size2D="300,20" />
```

The `Binding` markup extension has two arguments, one of which is a markup extension for `x:Reference`. Therefore, a pair of curly braces are nested within the main curly braces:


``` xaml
PositionX="{Binding Source={x:Reference Name=slider}, Path=Value}"
```

Following are the two ways to specify the link between the source object with the target object:
- Use the `BindingContext` to reference the source object.
- Use the `Source` property of the `Binding` markup extension.

If you specify both, the `Source` property takes precedence over the `BindingContext`.

For more information, see https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/xaml-basics/data-binding-basics