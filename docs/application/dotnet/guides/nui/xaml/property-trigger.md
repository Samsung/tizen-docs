# Property Trigger
Property trigger occurs when a property on a control is set to a particular value. Property trigger allow you to express actions declaratively in XAML that change the appearance of controls based on the property changes.

For more information, see https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/triggers#targetText=Triggers%20allow%20you%20to%20express,on%20events%20or%20property%20changes.&targetText=Property%20Trigger%20%2D%20occurs%20when%20a,the%20properties%20of%20another%20control


The following example shows two triggers that changes `PositionX` of the `ImageView` property when the `ResourceUrl` property is changed to or set equal to `../res/bixby_detail.png` or `../res/bixby_sendtophone.png`:

``` xaml
<ContentPage x:Class="Tizen.NUI.Examples.StyleDemoPage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ContentPage.Resources>
    <ResourceDictionary>
      <Style x:Key="CustomStyle" TargetType="ImageView">
        <Style.Triggers>
          <Trigger TargetType="ImageView" Property="ResourceUrl" Value="../res/bixby_detail.png">
            <Trigger.Setters >
              <Setter Property="PositionX" Value="200" />
            </Trigger.Setters>
          </Trigger>
          <Trigger TargetType="ImageView" Property="ResourceUrl" Value="../res/bixby_sendtophone.png">
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
      <x:String>../res/traffic_content.png</x:String>
    </x:Arguments>
  </ImageView>

  <PushButton Name="Click" LabelText="Click" Size2D="400,80" Position2D="1000,100" />
</ContentPage>
```

- `TargetType`: The control type that the trigger applies to.
- `Property`: The property on the control that is monitored.
- `Value`: The value, when it occurs for the monitored property that causes the trigger to activate.
- `Setter`: A collection of Setter elements can be added when the trigger condition is met. You must specify the `Property` and set `Value`.

> **Note**
>
> The Property for Trigger and Setter must not be same.

For more information, see https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/triggers#targetText=Triggers%20allow%20you%20to%20express,on%20events%20or%20property%20changes.&targetText=Property%20Trigger%20%2D%20occurs%20when%20a,the%20properties%20of%20another%20control
