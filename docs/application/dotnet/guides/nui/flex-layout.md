# Flex Layout

## Overview

`FlexLayout` is a flexible box layout, providing a more efficient way to lay out, align and distribute space among items in the container, even when their size is unknown or dynamic.

A layout which provides features like wrapping so if items no long fit on an axis they can automatically be positioned on another row or column.

`FlexLayout` defines four properties that affect the size, orientation, and alignment of child views. These properties are described in more detail in the table below.
Please see each categories below.

| Property               | Type            | Description |
| -----------------------| --------------- | ------------ |
| `Direction`            | FlexDirection   | The orientation the flex items are laid out in (Column/Row) |
| `Justification`        | FlexJustification | Alignment of items along the flex axis when free space available |
| `Alignment`            | AlignmentType     | Alignment of items along the cross axis when free space available |
| `WrapType`             | FlexWrapType    | Enable wrapping of items |


Natural size of items are used which can be different for each item. And setting the size of an item has no effect.

`Justification` applies to the flex Direction axis whilst `Alignment` is the (other) cross axis. Changing the Direction will apply the `Justification` to the new direction.


## FlexDirection

`Direction` property specifies the main axis direction along which flex items are placed.

<table style="width:100%">
<tr>
<td style="width:100%" align="center">
<img src="./media/flexDirection.png">
</td>
</tr>
</table>

| Property value |  Description |
|----------------|--------------|
| `Row`          | Place items horizontally in a row |
| `RowReverse`   | Place items horizontally in a row, but in reverse order |
| `Column`       | Place items vertically in a column |
| `ColumnReverse` | Place items vertically in a column, but in reverse order |

### Usage

```csharp
View layoutView = new View();
var flexLayout = new FlexLayout();
flexLayout.Direction = FlexLayout.FlexDirection.Column;
layoutView.Layout = flexLayout;
```


## FlexJustification

`Justification` property specifies the alignment for flex items, when they do not use all available space on the main axis.

<table style="width:100%">
<tr>
<td style="width:100%" align="center">
<img src="./media/justifyContent.png">
</td>
</tr>
</table>

| Property value  |   Description |
|-----------------|---------------|
| `FlexStart`     | Position items at the beginning of the container |
| `FlexEnd`       | Position items at the end of the container |
| `Center`        | Position items at the center of the container |
| `SpaceBetween`  |  Position items with equal spacing between them |
| `SpaceAround`   |  Position items with equal spacing before, between, and after them |

### Usage

```csharp
View layoutView = new View();
var flexLayout = new FlexLayout();
flexLayout.Justification = FlexLayout.FlexJustification.SpaceBetween;
layoutView.Layout = flexLayout;
```


## AlignmentType

`Alignment` property specifies the alignment for flex items when they do not use all the available space on the cross axis.

<table style="width:100%">
<tr>
<td style="width:100%" align="center">
<img src="./media/alignItems.png">
</td>
</tr>
</table>

|  Property value  |   Description  |
|------------------|----------------|
|  `Auto`          | Inherits the same alignment from the parent |
|  `FlexStart`     | Align items to the beginning of the container |
|  `Center`        | Align items to the center of the container |
|  `FlexEnd`       | Align items to the end of the container |
|  `Stretch`       | Stretch items to fit the container |

### Usage

```csharp
View layoutView = new View();
var flexLayout = new FlexLayout();
flexLayout.Alignment = FlexLayout.AlignmentType.Center;
layoutView.Layout = flexLayout;
```


## FlexWrapType

`WrapType` property specifies whether the flex items must wrap if there is not enough room for them on 1 flex line.

<table style="width:100%">
<tr>
<td style="width:100%" align="center">
<img src="./media/flexWrap.png">
</td>
</tr>
</table>


| Property value |  Description  |
|----------------|---------------|
|  `NoWrap`      | Reduce item sizes to fit them in a single line along the main axis |
|  `Wrap`        | Show items over multiple lines, if needed |

### Usage

```csharp
View layoutView = new View();
var flexLayout = new FlexLayout();
flexLayout.WrapType = FlexLayout.FlexWrapType.NoWrap;
layoutView.Layout = flexLayout;
```


## Related information

- Dependencies
  -  Tizen 5.5 and Higher
