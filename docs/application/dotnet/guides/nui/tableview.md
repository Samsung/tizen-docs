# TableView

The `TableView` class is a layout container for aligning child actors in a grid like layout.
`TableView` constraints the x and y position, width, and height of the child actors.
The Z position and depth are left intact, so that the three-dimensional model actors can also be laid out in a grid without losing their depth scaling.

In this tutorial, the following subjects are covered:

[Creating a TableView](#1)<br>
[TableView Properties](#2)<br>

<a name="1"></a>
## Creating a TableView

The following example illustrates how to create a `TableView` object:

```
// Create a TableView instance
Window window = Window.Instance;
TableView tableView = new TableView( 4, 4 );
tableView.Focusable = true;
tableView.PivotPoint = PivotPoint.Center;
tableView.Size2D = new Size2D( 300, 300 );

for( int row = 0; row < 4; ++row )
{
  for( int col = 0; col < 4; ++col )
  {
    TextLabel textLabel = new TextLabel();
    textLabel.Focusable = true;
    textLabel.BackgroundColor = Color.White;
    tableView.AddChild( textLabel, new TableView.CellPosition(row, col));
  }
}
window.Add(tableView);
```
<a name="2"></a>
## TableView Properties

The following table lists the available `TableView` properties:

**Table: TableView properties**

| Property        | Type         | Description                        |
|-----------------|--------------|------------------------------------|
| `Rows`          | Integer      | The amount of rows in the table.    |
| `Columns`       | Integer      | The amount of columns in the table. |
| `CellPadding`   | Vector2      | Padding between the cells.              |
| `LayoutRows`    | PropertyMap  | The number of layout rows.          |
| `LayoutColumns` | PropertyMap  | The number of layout columns.       |



## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
