# How to define and use the Resource in XAML

XAML resources are definitions of objects that can be shared and re-used throughout a Tizen.NUI application. These resource objects are stored in a resource dictionary.

<code>ContentPage</code> defines a property named <code>Resources</code> that is of type <code>ResourceDictionary</code> — a dictionary with <code>string</code> keys and values of type <code>object</code>. Items can be added to this dictionary right in XAML, and they can be accessed in XAML with the <code>StaticResource</code> and <code>DynamicResource</code> markup extensions.
DynamicResource is for dictionary keys associated with values that might change during runtime, while StaticResource accesses elements from the dictionary just once when the elements on the page are constructed.

## Creating and Consuming a ResourceDictionary

Each resource has a key that is specified using the <code>x:Key attribute</code>, which becomes it dictionary key in the <code>ResourceDictionary</code>.

As demonstrated in the **TestStaticDynamicResource** example that shows the usage of the <code>StaticResource</code> and <code>DynamicResource</code>:

``` xml
<ContentPage x:Class="Tizen.NUI.Examples.TestStaticDynamicResourcePage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ContentPage.XamlResources>
    <ResourceDictionary>
      <x:String x:Key="urlKey">
          ../../res/images/ambient/default/picture_m_1.jpg
      </x:String>
      <x:String x:Key="positionKey">
          200, 200
      </x:String>
    </ResourceDictionary>
  </ContentPage.XamlResources>

  <ImageView x:Name="img1" ResourceUrl="{StaticResource urlKey}"  Position2D="{DynamicResource positionKey}/>
</ContentPage>
```

<code>StaticResource</code> accesses the item in the dictionary only once while the XAML is being parsed and the page is being built. But <code>DynamicResource</code> maintains a link between the dictionary key and the property set from that dictionary item. If the item in the resource dictionary referenced by the key changes, <code>DynamicResource</code> will detect that change and set the new value to the property.

When you changed the value of the "positionKey", <code>DynamicResource</code> will detect that change and set the new value to the Position2D property.

``` csharp
Tizen.NUI.Binding.ResourceDictionary dict = Tizen.NUI.GetResourcesProvider.Get().Resources;
Tizen.NUI.GetResourcesProvider.Get().Resources["positionKey"] = positionX.ToString() + "," + positionY.ToString();
```

Reference: `https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/resource-dictionaries`
