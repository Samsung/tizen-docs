# Migrate Xamarin.Forms App to NUI Xaml

The process for migrating a Xamarin.Forms app to Xmarin.Tizen is expected to be:

1. Create empty NUI Xaml App
2. Update namespaces and declared assemblies
3. Convert elements
3. Build and fix any issues
4. Run the converted app and verify that is functions correctly.

## Migration process

### Create empty NUI Xaml App

Follow [Get-Started](../user-interface/nui/xaml/get-started-xaml.md) to create empty Tizen NUI XAML App

### Update namespaces and declared assembiles

| Old namespace and assembly           | New namespace and assembly               |
| ------------------------------------ | ---------------------------------------- |
| xmlns="http://zamarin.com/schemas/2014/forms  | xmlns="http://tizen.org/Tizen.NUI/2018/XAML"  |
|  | xmlns:base="clr-namespace:Tizen.NUI.BaseComponets;assembly=Tizen.NUI"  |
|  | xmlns:comp="clr-namespace:Tizen.NUI.Componets;assembly=Tizen.NUI.Components"  |
| xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml" | xmlns:x="https://schemas.microsoft.com/winfx/2009/xaml"  |

### Convert elements

Basing on sample app source code

| Xamarin.Forms | Xmarin.Tizen |
| ------------- | ------------ |
|[XAML Forms Page](FormsXamlPage.xaml)|[XAML Tizen Page](TizenXamlPage.xaml) |

#### XAML Source 

Below table shows UI elements form Xamarin.Forms and their replacement in NUI Xaml

| Xamarin.Forms | NUI Xaml |
| ------------- | ------------ |
| Frame         | View         |
| Label         | TextLabel    |
| FontSize      | PointSize    |

### Verification

| Xamarin.Forms | NUI Xaml  |
| ------------- | ------------ |
|<img src="./xaml-forms.png" width="300"> | <img src="./xaml-tizen.png" width="300"> |

## Related information
- Dependencies
  - Tizen 6.5 and Higher
