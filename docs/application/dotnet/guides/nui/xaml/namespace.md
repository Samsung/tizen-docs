# XAML namespaces

XAML uses the xmlns XML attribute for namespace declarations. This article introduces the XAML namespace syntax, and demonstrates how to declare a XAML namespace to access a type.

## Default namespaces

To use the Tizen.NUI, you should define the default nameSpace like this:

``` xml
xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
```

It should be the root element of a XAML file.

## Declaring Custom namespaces for Types

Custom types can be referenced in XAML by declaring a XAML namespace with a prefix, with the namespace declaration specifying the namespace name, and optionally an assembly name.

  • **clr-namespace**: – the CLR namespace declared within the assembly that contains the types to expose as XAML elements. This keyword is required.

  • **assembly=** – the assembly that contains the referenced CLR namespace. This value is the name of the assembly, without the file extension. This keyword can be omitted if the **clr-namespace** value is within the same assembly as the application code that's referencing the types.

The following code example shows a XAML namespace declaration:

``` xml
xmlns:l="clr-namespace:Tizen.NUI.Examples;assembly=TestXaml"
```

The namespace prefix is then specified when declaring an instance of a type from an imported namespace, as demonstrated in the following XAML code example:

``` xml
<View x:Name="view" BackgroundColor="{Binding Color}" Size2D="440,400" Position2D="20,10" >
    <View.BindingContext>
      <l:HslViewModel x:Name="hsl" Color="Red" />
    </View.BindingContext>
</View>
```

You can find and test it in the **HslColorScrollTest** sample.

The default namespace specifies that elements defined within the XAML file with no prefix refer to Tizen.NUI classes, such as <code>View</code>.

## x: Prefix namespace

There are a namespace declaration uses the <code>x</code> prefix, as shown in the following XAML code example:

``` xml
xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
```

The <code>x</code> namespace declaration specifies that elements defined within the XAML with a prefix of <code>x</code>.
The following table outlines the <code>x</code> namespace attributes supported by Tizen.NUI:

|Construct|Description|
|:--|:--|
| x:Arguments | Specifies constructor arguments for a non-default constructor, or for a factory method object declaration.|
| x:Class | Specifies the namespace and class name for a class defined in XAML. The class name must match the class name of the code-behind file. Note that this construct can only appear in the root element of a XAML file. |
| x:FactoryMethod | Specifies a factory method that can be used to initialize an object. |
| x:Key | Specifies a unique user-defined key for each resource in a ResourceDictionary. The key's value is used to retrieve the XAML resource, and is typically used as the argument for the StaticResource markup extension. |
| x:Name | Specifies a runtime object name for the XAML element. Setting x:Name is similar to declaring a variable in code. |

Reference: `https://docs.microsoft.com/en-US/xamarin/xamarin-forms/xaml/namespaces`
