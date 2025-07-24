# Styles Block

The `styles` block contains 1 or more `style` blocks. A `style` block is used to create style `<tags>` for advanced textblock formatting.

**Figure: Styles block**

![Styles block](./media/diagram_styles.png)

```
styles {
   style {
      name: "stylename";
      base: "..default style properties..";
      tag: "tagname" "..style properties..";
   }
}
```

- `name [style name]`

  Sets the name of the style to be used as a reference later in the theme.

- `base [style properties string]`

  Sets the default style properties applied to the complete text. The following tags can be used in the style property:

  - `font`
  - `font_size`
    > **Note**
    >
    > The font size is a point size, and the size of the rendered text is affected by the ppi information. The system basic ppi is 96, and you can change it in the emulator menu.
  - `color`
  - `color_class`
  - `text_class`
  - `ellipsis`
  - `wrap`
  - `style`
  - `valign`
  - `align`

- `tag [tag name] [style properties string]`

  Sets the style to be applied only to text between style `<tags>..</tags>`. When creating paired tags, like `<bold></bold>`, a '+' sign must be added at the start of the style properties of the first part (`<bold>`). If the second part (`</bold>`) is also defined, a '-' sign must be added to its style properties. This applies only to paired tags; single tags, like `<tab>`, must not have a starting '+'.

  - `br`
  - `tab`
  - `b`
  - `match`

  The following code is the style sample for the text style:

  ```
  style {
     name: "list_text_main";
     base: "font=Tizen:style=Regular font_size=30 color=#ffffff ellipsis=1.0";
     tag: "br" "\n";\
     tag: "ps" "ps";\
     tag: "tab" "\t";\
     tag: "b" "+ font_weight=Bold";
  }
  ```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
