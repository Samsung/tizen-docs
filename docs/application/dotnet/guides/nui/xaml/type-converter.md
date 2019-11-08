# TypeConverters
If you want to convert a string to some custom type in XAML, you need to define a TypeConverter. This changes the string format as a XAML format such as converting `Red` to `Color.Red`.
If you write a custom class, and you want instances of your class to be usable as XAML settable attribute values, you might need to write a custom TypeConverter class.

> **Note**
> 
> NUI XAML is very similar to WPF XAML. For more information on basic concepts, see
https://docs.microsoft.com/en-us/dotnet/framework/wpf/advanced/typeconverters-and-xaml

## Type Conversion
In the XAML file, all the attribute values are represented as type of string with pure text.
Even primitives (ex: Int, Double) are simple text string and they are needed to be changed as the type that XAML processor can understand.
For instance, **Tizen.NUI** defines some properties that take a value of type `Size2D`. 
`Size2D` is a value that describes two-dimensional sizes and has two important properties, width and height. 
When you are specifying size2D in XAML, you must specify it as a string with a comma between the width and height values:

``` xml
<ImageView PositionX="100" PositionY="320" Size2D="300, 300" ResourceUrl="ImageResourcePath"/>
```

In this scenario, the type converter is the `Size2DTypeConverter` class.
If a type converter is not available, you must use verbose markup as shown in the following code:

``` xml
<ImageView PositionX="100" PositionY="320" ResourceUrl="ImageResourcePath">
  <ImageView.Size2D>
    <Size2D Width="300" Height="300"/>
  </ImageView.Size2D>
</ImageView>
```

### NUI TypeConverter
Currently, Tizen.NUI supports the following type converters:
- `ColorTypeConverter`
- `PositionTypeConverter`
- `Position2DTypeConverter`
- `SizeTypeConverter`
- `Size2DTypeConverter`
- `Vector2TypeConverter`
- `Vector3TypeConverter`
- `Vector4TypeConverter`
- `RelativeVector2TypeConverter`
- `RelativeVector3TypeConverter`
- `RelativeVector4TypeConverter`

Therefore, you can define the color, position, Size2D, and so on as string in XAML as shown in the following code:

``` xml
<TextLabel Text="HelloWorld!" BackgroundColor="1.0,0.0,0.0,1.0" Position="20,10,0" Size2D="440,400"/>
```

### Implement a Type Converter
If you want to convert a string to some custom type in XAML, you need to define a `TypeConverter`.
The most important method in `TypeConverter` is the `ConvertFromInvariantString` which converts the input string to the required object type. 
You can see `Size2DTypeConverter` as shown in the following code:

``` csharp
internal class Size2DTypeConverter : TypeConverter
{
    public override object ConvertFromInvariantString(string value)
    {
        if (value != null)
        {
            string[] parts = value.Split(',');
            if (parts.Length == 2)
            {
                return new Size2D(Int32.Parse(parts[0].Trim(), CultureInfo.InvariantCulture), 
                                Int32.Parse(parts[1].Trim(), CultureInfo.InvariantCulture));
            }
        }

        throw new InvalidOperationException($"Cannot convert \"{value}\" into {typeof(Size2D)}");
    }
}
```
