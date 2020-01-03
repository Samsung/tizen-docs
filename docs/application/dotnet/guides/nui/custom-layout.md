# Create Custom Layout

You can create custom layouts with the fundamental layout of NUI for building your own layouting.

Or you can just use the available layouts, such as `LinearLayout` and `GridLayout`. For more information, see [Common Layouts](./layouting.md#commonLayout) category.

## OnMeasure and OnLayout

Custom layouts can be created for use in applications or to add to the current "Toolkit".

The custom layout must derive from `LayoutGroup` and override the 2 methods : `OnMeasure` and `OnLayout` described below.

When creating a custom Layout, these are the methods that should be extended and will be called during the Measure and Layout phases respectively. And the layouting framework does all the heavy work leaving just the Measuring and Layouting to the Custom Layout.

Layouting is a 2 phase process :

1. First, Measuring of the children hence determining the layouts own dimensions.

2. Second, Layouting (Positioning) the children within itself using their measured sizes.

### Measure the view and its children

```protected override void OnMeasure( MeasureSpecification widthMeasureSpec, MeasureSpecification heightMeasureSpec )```

    The `OnMeasure` is the first function to overrid that 2 parameters are provided. They are the parents' width and height MeasureSpecifications which impose the size that the custom layout can be.

    Then, the Custom layout should measure its children.
    To measure children size, `MeasureChild` API is available along with children which is an List of the Layouts children. It can be used to iterate and measure each one.

    After the children are measured, the Custom Layout can add up their height and width together in any way it needs to.
    Finally, the `SetMeasuredDimensions` API with the size is called it needs to be.

### Layout its children

```protected override void OnLayout( bool changed, LayoutLength left, LayoutLength top, LayoutLength right, LayoutLength bottom )```

    The `OnLayout` is where the children are positioned using the Layout API which takes a frame : start, top, end, bottom.
    The positioning of the vertices of the child in turn defines its size.

    As in the `OnMeasure`, the children List can be iterated to get each child in the Layout, then the `MeasuredWidth` and `MeasuredHeight` can be queried on each child.

## LayoutLength

`LayoutLength` is a class which encapsulates either the height or width value used in Layouting.  The value can be set by passing in a integer or float and retrieved as a decimal or rounded value. The rounded value should be used in outputting like when setting measured dimensions. The decimal value should be used during calculations.

It is up to the layout to deal with the floating point to rounded number differences. For example, dividing a length of 100 between 3 columns could result in a column 33,34,33. Which would be preferable to 33,33,33 and 1 being undefined.

## Example code for a Custom Layout

The following code snippet explains shows how to create a custom layout.
You can see a custom Layout positioning children in a horizontal line.

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
            SetMeasuredDimensions( new MeasuredSize( measuredWidth, MeasuredSize.StateType.MeasuredSizeOK),
                                   new MeasuredSize( measuredHeight, MeasuredSize.StateType.MeasuredSizeOK) );
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

## Related information

- Dependencies
  -  Tizen 5.5 and Higher
