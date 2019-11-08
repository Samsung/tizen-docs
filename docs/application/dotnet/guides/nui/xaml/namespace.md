# XAML Namespaces
XAML uses the `xmlns` XML attribute for namespace declarations. This article introduces the XAML namespace syntax, and demonstrates how to declare a XAML namespace to access a type.

## Default Namespaces
To use Tizen.NUI, you must define the default namespace as shown in the following code:

``` xaml
xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
```
> **Note**
>
> It must be the root element of the XAML file.

## Declare Custom Namespaces for Types
Custom types can be referenced in XAML by declaring a XAML namespace with a prefix, and specifying the namespace name, optionally an assembly name.

- `clr-namespace`: The CLR namespace is declared within the assembly that contains the types to expose as XAML elements. This is a mandatory namespace.
- `assembly`: The assembly that contains the referenced CLR namespace. This value is the name of the assembly, without the file extension. This keyword can be omitted if the `clr-namespace` value is within the same assembly as the application code that is referencing the types.

The following code example shows a XAML namespace declaration:

``` xaml
xmlns:l="clr-namespace:Tizen.NUI.Examples;assembly=TestXaml"
```

The namespace prefix is specified while declaring an instance of a type from an imported namespace, as shown in the following XAML code example:

``` xaml
<View x:Name="view" BackgroundColor="{Binding Color}" Size2D="440,400" Position2D="20,10" >
    <View.BindingContext>
      <l:HslViewModel x:Name="hsl" Color="Red" />
    </View.BindingContext>
</View>
```

The default namespace specifies the elements defined within the XAML file with no prefix referring to the Tizen.NUI classes, such as `View`.

## x:Prefix Namespace
There is a namespace declaration that uses the `x` prefix as shown in the following XAML code example:

``` xaml
xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
```

The `x` namespace declaration specifies that elements defined within the XAML with a prefix of `x` are used for elements and attributes that are intrinsic to XAML (specifically the 2009 XAML specification).  
The following table outlines the `x` namespace attributes supported by Tizen.NUI:

|Construct|Description|
|:--|:--|
| x:Arguments | Specifies a constructor argument for a non-default constructor or for a factory method object declaration.|
| x:Class | Specifies the namespace and class name for a class defined in XAML. The class name must match the class name of the code-behind file. This construct can only appear in the root element of a XAML file. |
| x:Key | Specifies a unique user-defined key for each resource in a ResourceDictionary. The value of key is use to retrieve the XAML resource and is typically used as the argument for the StaticResource markup extension. |
| x:Name | Specifies a runtime object name for the XAML element. Setting `x:Name` is similar to declaring a variable in code. |

For more information, see https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/namespaces
