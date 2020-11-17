# Linear Layout

`LinearLayout` is a linear box layout in which the children of a layout are arranged vertically or horizontally by using [`LinearOrientation`](#orientation) property.

![LinearLayout](./media/linearTotal.png)

`LinearAlignment` defines from where you can start positioning children. It can be used when children do not use all the space of a parent.

While positioning children in a linear form that is one after the other, you can use [`CellPadding`](#cellPadding) to insert a space between each child. Unlike generic padding, `CellPadding` does not insert a space at the start, end, top, or bottom of the layout.

Here are the properties of `LinearLayout`:

| Property               | Type            | Description  |
| -----------------------| --------------- | ------------ |
| `LinearOrientation`    | LinearLayout.Orientation | Gets or sets the vertical or horizontal orientation of the linear layout. |
| `LinearAlignment`      | LinearLayout.Alignment  | Gets or sets the global child alignment. |
| `CellPadding`          | Size2D      | Gets or sets the horizontal or vertical spacing between the cells. |


<a name="orientation"></a>
## Orientation

`LinearOrientation` indicates the direction of a child layout such as horizontal or vertical. The default value is horizontal.

| Horizontal | Vetical |
| -----------------------| --------------- |
| ![Horizontal](./media/horizontalLayout.png) | ![Vertical](./media/verticalLayout.png)  |

```csharp
View layoutView = new View();
var linearLayout = new LinearLayout();
linearLayout.LinearOrientation = LinearLayout.Orientation.Horizontal;
layoutView.Layout = layout;
```

<a name="alignment"></a>
## Alignment

`LinearAlignment` handles how the layout items are positioned within their parent layout. By default, items are aligned at **Top** and **Begin**.
You can choose from the following alignment options:

| Alignment  | Description        |
| ---------- | ------------------ |
| Begin      | At the left or right edge of the container, according to Left to Right (LTR) or Right to Left (RTL) direction for horizontal orientation |
| End        | At the right or left edge of the container, according to LTR or RTL direction for horizontal orientation |
| CenterHorizontal | At the horizontal center of the container (vertical will be set to top) |
| Top        | At the top edge of the container |
| Bottom     | At the bottom edge of the container |
| CenterVertical | At the vertical center of the container (horizontal will be set to begin) |
| Center    | At both the vertical and horizontal center of the container |

The following example shows how to set the layout alignment to `Center`:

![LinearAlignment](./media/linearAlignment.png)

```csharp
View layoutView = new View();
var linearLayout = new LinearLayout();
linearLayout.LinearAlignment = LinearLayout.Alignment.Center;
layoutView.Layout = layout;
```

<a name="cellPadding"></a>
## CellPadding

`CellPadding` is to set the padding between cells in the layout. It is used to insert a space between each child.
The type of `CellPadding` is [Size2D](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.Size2D.html), which is two-dimensional. Height and width values are considered in `CellPadding`.
After setting `CellPadding` to parent view, the interval between children is located by the width of CellPadding in the case of horizontal layout or by the height of `CellPadding` in the case of vertical layout.

The type of `CellPadding` is not `Extents` which has start, end, top, and bottom, but `Size2D` which as float width and float height. And in the following image, the arrow is the width (10) because the orientation of container layout is horizontal.

![CellPadding](./media/cellPadding.png)

```csharp
View layoutView = new View();
var linearLayout = new LinearLayout();
linearLayout.CellPadding = new Size2D(10, 20);
layoutView.Layout = layout;
```

<a name="weight"></a>
## Weight

`Weight` is used to determine how much space is occupied by a view and how a view shares the available space in a layout with its siblings.

Depending on each weight, children take up their parent's view space. Therefore, child views can set the `Weight` value to float type. The default weight value is zero. If the weight is zero, then the size of child would be its natural size or specific size the user sets.

The following example shows how to set the layout weight to each child. The weight of `imageView1` is 0.75f and the weight of `imageView2` is 0.25f. According to the weight, children are arranged in the parent view space.

![Weight](./media/weight.png)

```csharp
View layoutView = new View();
var linearLayout = new LinearLayout();
layoutView.Layout = linearLayout;

ImageView imageView1 = new ImageView();
imageView1.Weight = 0.75f;

ImageView imageView2 = new ImageView();
imageView2.Weight = 0.25f;

layoutView.Add(imageView1);
layoutView.Add(imageView2);
```


## Related Information

- Dependencies
  -  Tizen 5.5 and Higher
