# Property Trigger

Property triggers allow you to express actions declaratively in XAML that change the appearance of controls based on property changes.

The following example shows two triggers that change a ImageView's <code> PositionX </code> property when it <code> ResourceUrl </code> property changed and equal to "../../res/images/AmbientScreenUXControl/Cut/bixby_detail.png" or "../../res/images/AmbientScreenUXControl/Cut/bixby_sendtophone.png":

``` xml
<ContentPage x:Class="Tizen.NUI.Examples.StyleDemoPage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ContentPage.Resources>
    <ResourceDictionary>
      <Style x:Key="CustomStyle" TargetType="ImageView">
        <Style.Triggers>
          <Trigger TargetType="ImageView" Property="ResourceUrl" Value="../../res/images/AmbientScreenUXControl/Cut/bixby_detail.png">
            <Trigger.Setters >
              <Setter Property="PositionX" Value="200" />
            </Trigger.Setters>
          </Trigger>
          <Trigger TargetType="ImageView" Property="ResourceUrl" Value="../../res/images/AmbientScreenUXControl/Cut/bixby_sendtophone.png">
            <Trigger.Setters >
              <Setter Property="PositionX" Value="500" />
            </Trigger.Setters>
          </Trigger>
        </Style.Triggers>
      </Style>
    </ResourceDictionary>
  </ContentPage.Resources>

  <ImageView Name="ImageView" Position2D="0,0" Size2D="400,400" Style="{StaticResource CustomStyle}">
    <x:Arguments>
      <x:String>../../res/images/AmbientScreenUXControl/Cut/traffic_content.png</x:String>
    </x:Arguments>
  </ImageView>

  <PushButton Name="Click" LabelText="Click" Size2D="400,80" Position2D="1000,100" />
</ContentPage>
```

• <code> TargetType </code> - the control type that the trigger applies to.

• <code> Property </code> - the property on the control that is monitored.

• <code> Value </code> - the value, when it occurs for the monitored property, that causes the trigger to activate.

• <code> Setter </code> - a collection of Setter elements can be added and when the trigger condition is met. You must specify the <code> Property </code> and <code> Value </code> to set.

**Attention**: the <code> Property </code> for <code>Trigger</code> and the <code>Property</code> for <code>Setter</code> can not be same.
