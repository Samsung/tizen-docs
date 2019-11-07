# TypeConverters and XAML

This topic introduces the purpose of type conversion from string as a general XAML language feature. Such as converter "Red" to <code>Color.Red</code>. If you write a custom class, and you want instances of your class to be usable as XAML settable attribute values, you might need to write a custom TypeConverter class.

## Type Conversion Concepts

When you set an attribute value in a XAML file, the initial type of that value is a string in pure text. Even other primitives such as Double are initially text strings to a XAML processor.

If the value is a primitive(such as a numeric value), a direct conversion of the string is attempted. If the value is an enumeration, the string is used to check for a name match to a named constant in that enumeration. If the value is neither a parser-understood primitive nor an enumeration, then need a type converter class.

For instance, Tizen.NUI defines some properties that take a value of type <code>Size2D</code>. A <code>Size2D</code> is a value that describes two-dimensional size, and it really just has two important properties: Width and Height. When you specify a size2D in XAML, you specify it as a string with a comma between the Width and Height values you provide. For example:

``` xml
<ImageView PositionX="10" PositionY="320" Size2D="300, 300" ResourceUrl="ImageResourcePath" />
```

In this case type converter is the class <code>Size2DTypeConverter</code>.

Without a type converter here, you would need the following much more verbose markup for the same example shown previously:

``` xml
<ImageView PositionX="100" PositionY="320" ResourceUrl="ImageResourcePath">
  <ImageView.Size2D>
    <Size2D Width="300" Height="300" />
  </ImageView.Size2D>
</ImageView>
```

### NUI TypeConverter

Currently, <code>ColorTypeConverter</code>, <code>PositionTypeConverter</code>, <code>  Position2DTypeConverter</code>, <code>SizeTypeConverter</code>, <code>Size2DTypeConverter</code>, <code>Vector2TypeConverter</code>, <code>Vector3TypeConverter</code>, <code>Vector4TypeConverter</code>, <code>RelativeVector2TypeConverter</code>, <code>RelativeVector3TypeConverter</code>, <code>RelativeVector4TypeConverter</code>,
are supported in Tizen.NUI, so you can define the <code>Color</code>, <code>Position</code>, <code>Size2D</code>... as string in XAML.

For example:

``` xml
<TextLabel Text="HelloWorld!" BackgroundColor="1.0,0.0,0.0,1.0" Position="20,10,0" Size2D="440,400" />
```

## Implementing a Type Converter

### TypeConverter

All type converters that are used for XAML purposes are classes that derive from the base class <code>TypeConverter</code>. If you want to converter string to some custom type in XAML, you need to define a TypeConverter.

The most important method in <code>TypeConverter</code> is <code>ConvertFromInvariantString</code>. This method converts the input string to the required object type. Have a look at the implementation of the <code>Size2DTypeConverter</code>:

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