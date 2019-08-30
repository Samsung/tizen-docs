# BindingConverter and XAML

This topic introduces binding value converters. During binding, we usually use value converter, also called a bindig converter. Such as we want to bind a float property to a string property. XAML don't support implicit converter, we must need a converter.

## Binding Value Converters Concepts

It is a class that implements the <code>IValueConverter</code> interface, which means it has two methods named <code>Convert</code> and <code>ConvertBack</code>. The <code>Convert</code> method is called when a value is transferred from source to target; the <code>ConvertBack</code> method is called for transfers from target to source in <code>OneWayToSource</code> or <code>TwoWay</code> bindings.

Let us see an example:

``` xml
<?xml version="1.0" encoding="UTF-8" ?>
<ContentPage x:Class="Tizen.NUI.Examples.ViewToViewPage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:l="clr-namespace:Tizen.NUI.Examples;"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">
  <ContentPage.XamlResources>
    <ResourceDictionary>
      <l:FloatToRotationConverter x:Key="floatToRotationConverter" />
    </ResourceDictionary>
  </ContentPage.XamlResources>

  <TextLabel Text="ROTATION" BindingContext="{x:Reference slider}" Orientation="{Binding Path=Value, Converter={StaticResource floatToRotationConverter}}" Position2D="50,50" Size2D="300,50" HorizontalAlignment="Center" VerticalAlignment="Center" PivotPoint="Center" />

  <Slider x:Name="slider" Name="slider" LowerBound="0" UpperBound="360" Value="10" ShowPopup="true" ShowValue="true" ValuePrecision="1" Position2D="50,200" Size2D="300,20" />
</ContentPage>
```

In this example, we bind the <code> Orientation </code> of <code> TextLabel </code> to <code> Value </code> of <code> Slider </code>. The type of source <code> Value </code> is <code> float</code>, while the type of target <code> Orientation </code> is <code> Rotation </code>. They can't convert implicit, so we need a binding value converter, named <code>FloatToRotationConverter</code>.

The converter is instantiated in the resource dictionary so it can be shared among multiple bindings:

``` xml
  <l:FloatToRotationConverter x:Key="floatToRotationConverter" />
```

Notice that the <code>Binding</code> markup extension contains an embedded <code>StaticResource</code> markup extension:

``` xml
<TextLabel BindingContext="{x:Reference slider}" Orientation="{Binding Path=Value, Converter={StaticResource floatToRotationConverter}}" />
```

## Implementing a Binding Value Converter

### IValueConverter

All binding value converters should derive from the interface <code>IValueConverter</code>.

The most important method in <code>IValueConverter</code> is <code>Convert</code>. This method converts the object value to the required target type. The <code>ConvertBack</code> method won't play a role if the bindings are only one way from source to target. Have a look at the implementation of the <code>FloatToRotationConverter</code>:

``` csharp
using System;
using System.Globalization;
using Tizen.NUI;

namespace Tizen.NUI.Examples
{
    public class FloatToRotationConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            return new Rotation(new Radian(new Degree((float)value)), Vector3.ZAxis);
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            return null;
        }
    }
}
```
