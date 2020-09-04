# Create Custom Layout

You can create a custom layout with the fundamental layout of NUI. You can also use the available layouts, such as `LinearLayout` and `GridLayout`. For more information, see the [Common Layouts](./layouts.md#commonLayout).

## OnMeasure and OnLayout

With NUI component toolkit, custom layout for the applications can be created.

The custom layout must be derived from `LayoutGroup` and override the two methods, `OnMeasure` and `OnLayout`.

When creating a custom layout, `OnMeasure` and `OnLayout` methods must be extended and called during the measuring and layout phases respectively. The layout framework does all the heavy work except for measuring and layout. Measuring and layout are done by Custom Layout.

To create a layout, following two phases are required:

1. `OnMeasure`: Determining the layout size requirements of children and parents after measuring the approximate dimensions of children and parent.

2. `OnLayout`: Laying out and positioning the children within `View` itself using their measured sizes.

### Measure View and Children

This section shows how to measure children of its layout using the following method:

```
protected override void OnMeasure( MeasureSpecification widthMeasureSpec, MeasureSpecification heightMeasureSpec )
```

The `OnMeasure` is the first function to override the two parameters, width and height of parents. `MeasureSpecification` imposes the size of the custom layout.

After this, the custom layout must measure its children. To measure children size, MeasureChild API is available along with children, which is a list of the layout’s children. MeasureChild can be used to iterate and measure each one. After the children are measured, the custom layout can adjust height and width together as required.

Finally, you must call the SetMeasuredDimensions API with the size to set the required dimensions.

### Layout Children

This section shows how to lay children of its layout using the following method:

```
protected override void OnLayout( bool changed, LayoutLength left, LayoutLength top, LayoutLength right, LayoutLength bottom )
```

The `OnLayout` is where the children are positioned using NUI Layout API, which takes start, top, end, and bottom of a frame. The positioning of the vertices of the child, defines its size.
As in the `OnMeasure`, the children list can be iterated to get each child in the layout. Then the `MeasuredWidth` and `MeasuredHeight` can be queried on each child.

## LayoutLength

`LayoutLength` is a class, which encapsulates either the height or the width value used in layout. The value can be set by passing in an integer or a float. The value is retrieved as a decimal or a rounded value. The rounded value must be used as an output, for example when setting measured dimensions. The decimal value must be used during calculations.

Layout manages the floating point to rounded number differences. For example, dividing a length of 100 between 3 columns could result in a column 33, 34, 33, which is preferable to 33, 33, 33 and 1 being undefined.

## Custom Layout Example

The following code snippet shows how to create a custom layout:

```csharp

using Tizen.NUI;
using Tizen.NUI.BaseComponents;

namespace SimpleLayout
{
    internal class CustomLayout : LayoutGroup
    {
        protected override void OnMeasure( MeasureSpecification widthMeasureSpec, MeasureSpecification heightMeasureSpec )
        {
            var accumulatedWidth = new LayoutLength(0);
            var maxHeight = 0;
            var measuredWidth = new LayoutLength(0);
            LayoutLength measuredHeight = new LayoutLength(0) ;
            MeasureSpecification.ModeType widthMode = widthMeasureSpec.Mode;
            MeasureSpecification.ModeType heightMode = heightMeasureSpec.Mode;

            bool isWidthExact = (widthMode == MeasureSpecification.ModeType.Exactly);
            bool isHeightExact = (heightMode == MeasureSpecification.ModeType.Exactly);

            // In this layout we will:
            //  Measuring the layout with the children in a horizontal configuration, one after another
            //  Set the required width to be the accumulated width of our children
            //  Set the required height to be the maximum height of any of our children

            foreach (LayoutItem childLayout in _children)
            {
                if( childLayout != null )
                {
                    MeasureChild( childLayout, widthMeasureSpec, heightMeasureSpec );
                    accumulatedWidth += childLayout.MeasuredWidth.Size;
                    maxHeight = (int)System.Math.Ceiling(System.Math.Max( childLayout.MeasuredHeight.Size.AsRoundedValue(), maxHeight ));
                }
            }

            measuredHeight = new LayoutLength(maxHeight);
            measuredWidth = accumulatedWidth;

            if( isWidthExact )
            {
                measuredWidth = new LayoutLength( widthMeasureSpec.Size );
            }

            if( isHeightExact )
            {
                measuredHeight = new LayoutLength( heightMeasureSpec.Size );
            }

            // Finally, call this method to set the dimensions we would like
            SetMeasuredDimensions( new MeasuredSize( measuredWidth, MeasuredSize.StateType.MeasuredSizeOK ),
                                   new MeasuredSize( measuredHeight, MeasuredSize.StateType.MeasuredSizeOK ) );
        }

        protected override void OnLayout( bool changed, LayoutLength left, LayoutLength top, LayoutLength right, LayoutLength bottom )
        {
            LayoutLength childLeft = new LayoutLength( 0 );

            // We want to vertically align the children to the middle
            LayoutLength height = bottom - top;
            float middle = height.AsDecimal() / 2;

            // Horizontally align the children to the middle of the space they are given too
            LayoutLength width = right - left;
            int count = _children.Count;
            int childIncrement = 0;
            if (count > 0)
            {
                childIncrement = (int)System.Math.Ceiling(width.AsDecimal() /  count);
            }
            float center = childIncrement / 2;

            // Check layout direction
            var view = GetOwner();
            ViewLayoutDirectionType layoutDirection = view.LayoutDirection;

            for ( int i = 0; i < count; i++ )
            {
                int itemIndex = i;
                // If RTL, then layout the last item first
                if (layoutDirection == ViewLayoutDirectionType.RTL)
                {
                    itemIndex = count - 1 - i;
                }

                LayoutItem childLayout = _children[itemIndex];
                if(childLayout != null)
                {
                    LayoutLength childWidth = childLayout.MeasuredWidth.Size;
                    LayoutLength childHeight = childLayout.MeasuredHeight.Size;

                    LayoutLength childTop = new LayoutLength(middle - (childHeight.AsDecimal()/2));

                    LayoutLength leftPosition = new LayoutLength(childLeft.AsDecimal() + center - childWidth.AsDecimal()/2);

                    childLayout.Layout( leftPosition,
                                        childTop,
                                        leftPosition + childWidth,
                                        childTop + childHeight );
                    childLeft += new LayoutLength(childIncrement);
                }
            }
        }
    }
}

```

## Related Information

- Dependencies
  -  Tizen 5.5 and Higher
