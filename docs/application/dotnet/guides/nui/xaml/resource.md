# How to Define and Use XAML Resources
XAML resources are definitions of objects that can be shared and reused throughout a Tizen.NUI application. These resource objects are stored in a resource dictionary.

`ContentPage` defines a property named `Resources` that is of type `ResourceDictionary`. `ResourceDictionary` is a dictionary with `string` keys and values of object. Items can be added to this dictionary in XAML, and they can be accessed in XAML with the `StaticResource` and `DynamicResource` markup extensions.
`DynamicResource` is for the dictionary keys associated with values that might change during runtime, while `StaticResource` accesses elements from the dictionary only once when the elements on the page are constructed.

## Create and Consume ResourceDictionary

Each resource has a key that is specified using the `x:Key` attribute, which becomes a dictionary key in `ResourceDictionary`.
The following **TestStaticDynamicResource** example explains the usage of `StaticResource` and `DynamicResource`:

``` xaml
<ContentPage x:Class="Tizen.NUI.Examples.TestStaticDynamicResourcePage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ContentPage.XamlResources>
    <ResourceDictionary>
      <x:String x:Key="urlKey">
          *Resource*/res/picture_m_1.jpg
      </x:String>
      <x:String x:Key="positionKey">
          200, 200
      </x:String>
    </ResourceDictionary>
  </ContentPage.XamlResources>`

  <ImageView x:Name="img1" ResourceUrl="{StaticResource urlKey}"  Position2D="{DynamicResource positionKey}/>
</ContentPage>
```

`StaticResource` accesses the item in the dictionary only once, while XAML is being parsed and the page is being built. However, `DynamicResource` maintains a link between the dictionary key and the property set from that dictionary item. If the item in the resource dictionary referenced by the key changes, then `DynamicResource` will detect that change and set the new value to the property.
When you change the value of `"positionKey"`, `DynamicResource` will detect that change and set the new value to the `Position2D` property.

``` csharp
Tizen.NUI.Binding.ResourceDictionary dict = Tizen.NUI.GetResourcesProvider.Get().Resources;
Tizen.NUI.GetResourcesProvider.Get().Resources["positionKey"] = positionX.ToString() + "," + positionY.ToString();
```

For more information, see https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/resource-dictionaries
