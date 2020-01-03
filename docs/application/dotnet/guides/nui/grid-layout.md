# Grid Layout

[Overview](#overview)<br>
[Column](#column)<br>

<a name="overview"></a>
## Overview

`GridLayout` is a grid box for the two-dimensional layout. It constraints the x and y position, width, and height of the child actors.

Positioning children in a grid form, the cells are of uniform size based on the first child added to the parent View.

The number of **columns** can be specified and the rows will automatically increased to hold the children. Once the available space is used up, further rows will not be added.

| Property               | Type            | Description |
| -----------------------| --------------- | ------------ |
| `Columns`              | int             | Gets/Sets the number of columns in the Grid |

<a name="column"></a>
## Column

<table style="width:100%">
<tr>
<td style="width:100%" align="center">
<img src="./media/columnLayout.png">
</td>
</tr>
</table>

```csharp
View layoutView = new View();
var gridLayout = new GridLayout();
gridLayout.Columns = 2;
layoutView.Layout = gridLayout;
```


## Related information

- Dependencies
  -  Tizen 5.5 and Higher
