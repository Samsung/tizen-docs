# TableView

The `Dali::Toolkit::TableView` class is a layout container for aligning child actors in a grid like layout.

`TableView` constraints the x and y position and width and height of the child actors.

**Figure: TableView**

![TableView](./media/tableview.png)

In this tutorial, the following subjects are covered:

[Creating a TableView](#1)<br>
[TableView Properties](#2)<br>

<a name="1"></a>
## Creating a TableView

The following example shows how to create a `TableView` object:

```
void HelloWorldExample::Create( Application& application )
{
  TableView tableView = TableView::New( 4, 4 );
  tableView.SetKeyboardFocusable( true );
  tableView.SetParentOrigin( ParentOrigin::CENTER );
  tableView.SetSize( 300, 300 );

  for( int row = 0; row < 4; ++row )
  {
    for( int col = 0; col < 4; ++col )
    {
      std::ostringstream str;
      str << row << "-" << col;
      TextLabel textLabel = TextLabel::New( str.str() );
      textLabel.SetKeyboardFocusable( true );
      textLabel.SetBackgroundColor( Color::WHITE );
      tableView.AddChild( textLabel, TableView::CellPosition( row, col ) );
    }
  }
  Stage::GetCurrent().Add( tableView );
}
```

<a name="2"></a>
## TableView Properties

The following table lists the available TableView properties.

**Table: TableView properties**

| Property         | Type             | Description           |
|----------------|----------------|---------------------|
| `ROWS`           | UNSIGNED INTEGER | The number of rows    |
| `COLUMNS`        | UNSIGNED INTEGER | The number of columns |
| `CELL_PADDING`   | VECTOR2          | The cell padding      |
| `LAYOUT_ROWS`    | MAP              | The rows layout       |
| `LAYOUT_COLUMNS` | MAP              | The columns layout    |


The following table lists the available TableView's child properties.

 **Table: TableView Child properties**

| Property                    | Type     | Description                               |
|---------------------------|--------|-----------------------------------------|
| `CELL_INDEX`                | VECTOR2  | The top-left cell this child occupies     |
| `ROW_SPAN`                  | FLOAT    | The number of rows this child occupies    |
| `COLUMN_SPAN`               | FLOAT    | The number of columns this child occupies |
| `CELL_HORIZONTAL_ALIGNMENT` | STRING   | The horizontal alignment of this child inside the cells |
| `CELL_VERTICAL_ALIGNMENT`   | STRING   | The vertical alignment of this child inside the cells |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
