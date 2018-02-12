# Fonts Block

The `fonts` block is used to list each font file with an alias used later in the theme. As with the `images` block, additional `fonts` blocks can be included inside other blocks.

**Figure: Fonts block**

![Fonts block](./media/diagram_fonts.png)

```
fonts {
   font: "filename1.ext" "fontname";
   font: "filename2.ext" "otherfontname";
}
```

- `font [font filename] [font alias]`  

  This property is included for each font, and it defines the `font file` and `alias`. The full path to the directory containing the font files can be defined later with the `edje_cc` tool's `-fd` option.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
