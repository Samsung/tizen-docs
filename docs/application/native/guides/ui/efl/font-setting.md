# Fonts

Tizen provides various methods for setting the fonts of the application text. Basically, all UI components have a default font, which can be changed according to the system settings.

The font handling methods include:

- [Setting the font for a UI component](#setting-the-font-for-a-ui-component) using the Elementary Fonts API (in [mobile](../../../api/mobile/latest/group__Fonts.html) and [wearable](../../../api/wearable/latest/group__Elm__Fonts.html) applications)

- [Setting the font using the EDC file](#setting-the-font-using-edc)

- [Changing the font and text size](#using-the-edje-text-class) using the Edje Class: Text API (in [mobile](../../../api/mobile/latest/group__Edje__Object__Text__Class.html) and [wearable](../../../api/wearable/latest/group__Edje__Object__Text__Class.html) applications)

  In the application, you can create text classes to apply the same font and font size to various text (textblock) parts.

  The following words in the `text_class` definition are reserved for the system. If you use these text classes in a text or text block, a system font is applied to their texts. When the system font changes, the new font and size are applied to the texts too (except for the `tizen` text class, which only applies the new font, not the size).
  - `button`
  - `label`
  - `entry`
  - `title_bar`
  - `list_item`
  - `grid_item`
  - `toolbar_item`
  - `menu_item`
  - `tizen`

- Creating your own font resources

  You can create your own font resources in the Tizen Studio to be distributed as a downloadable font package in the Tizen Store.

## Using the System Font

Tizen provides a special "Tizen" font name, which does not match with any specific font; it is simply an alias for the system-defined font (system font). If you create a text object (with EDC or in the C code) with the "Tizen" font name, the system font is loaded into the user application when the object is created.

You can use the "Tizen" font name when you [create a text or textblock part](#setting-the-font-using-edc) in the application's EDC file, when you [use the text class](#using-the-edje-text-class), or when you  [set the UI component text font](#setting-the-font-for-a-ui-component) in the C code.

For example:

- Use the system font when creating a text part with a reserved text class name.

  When the object is created or if the system setting changes, the part loads the current system font and size.

  ```
  description {
     text {
        font: "Tizen:style=Regular";
        font_size: 36;
        text_class: "label";
     }
  }
  ```

- Use the system font when creating a text part with the `tizen` text class.

  When the object is created or if the system setting changes, the part loads the new system font. However, the part font size remains 36 regardless of the new system font size, because the `tizen` text class does not apply system font size changes.
  ```
  description {
     text {
        font: "Tizen:style=Regular";
        font_size: 36;
        text_class: "tizen";
     }
  }
  ```

- Use the system font when creating a text part or setting the UI component text font.

  When the object is created or if the system setting changes, the part loads the current system font and size.

  ```
  description {
     text {
        font: "Tizen:style=Regular";
        font_size: 50;
     }
  }
  ```

  ```
  char *buf = "<font=Tizen:style=Regular font_size=50>Hello</font/>Font";
  elm_object_part_text_set(layout, "textblock1", buf);
  ```

## Supported Font Styles

The font styles supported by the EFL are listed in the following table.

**Table: Supported font styles**
<table>
<tr><th>Font feature</th><th>Style attribute</th></tr>
<tr><td rowspan="3"><code>font_style</code> </td><td> <code>normal</code></td></tr>
<tr><td> <code>oblique</code></td></tr>
<tr><td> <code>italic</code> </td></tr>
<tr><td rowspan="9"> <code>font_width</code><td> <code>normal</code></tr>
<tr><td> <code>ultracondensed</code> </td></tr>
<tr><td>  <code>extracondensed</code></td></tr>
<tr><td>  <code>condensed</code> </td></tr>
<tr><td>  <code>semicondensed</code> </td></tr>
<tr><td>  <code>semiexpanded</code></td></tr>
<tr><td>  <code>expanded</code></td></tr>
<tr><td>  <code>extraexpanded</code> </td></tr>
<tr><td>  <code>ultraexpanded</code></td></tr>
<tr><td rowspan="11"> <code>font_weight</code></td><td> <code>normal</code> </td></tr>
<tr><td>   <code>thin</code>  </td></tr>
<tr><td>   <code>ultralight</code></td></tr>
<tr><td> <code>light</code>  </td></tr>
<tr><td>  <code>book</code>   </td></tr>
<tr><td> <code>medium</code> </td></tr>
<tr><td> <code>semibold</code>  </td></tr>
<tr><td>   <code>bold</code>   </td></tr>
<tr><td> <code>ultrabold</code>   </td></tr>
<tr><td> <code>black</code>    </td></tr>
<tr><td> <code>extrablack</code> </td></tr>
</table>

The style attributes are not case-sensitive (however, the font feature names are).

If you set the weight or width attribute to `style=`, it is processed to the right attribute.

```
font=TizenSans:style=Bold /* Textblock */
"TizenSans:style=Bold"; /* Text font */
<font=TizenSans:style=Bold> /* Markup tag */
```

You can also use each attribute separately:

```
font=TizenSans font_style=Regular font_weight=Bold /* Textblock */
<font=TizenSans font_style=Regular font_weight=Bold> /* Markup tag */
```

## Setting the Font for a UI Component

You can use the Elementary Fonts API (in [mobile](../../../api/mobile/latest/group__Fonts.html) and [wearable](../../../api/wearable/latest/group__Fonts.html) applications) to set the font for an application.

To set a font for a UI component:

- Set the font for a common UI component:

  > **Note**
  >
  > If you add markup tags for the font inside the text, you can change the font of the text. However, you cannot set the font for a text part in EDC the same way (using markup tags), because the `TEXT` type does not support markup tags.

  ```
  char *buf = "<font=Sans:style=Regular font_size=50>Hello</font/>Font";
  elm_object_part_text_set(layout, "textblock1", buf);
  ```

- Set the font for an entry component (in [mobile](../../../api/mobile/latest/group__Entry.html) and [wearable](../../../api/wearable/latest/group__Entry.html) applications) using the `elm_entry_text_style_user_push()` function. It overrides the default style of the entry component for each attribute.

  > **Note**
  >
  > The `elm_entry_text_style_user_push()` function only affects the main text of the UI component. To change the font of the guide text, you have to add markup tags.

  ```
  /* Main text font */
  char *user_style = "DEFAULT='font=Sans:style=Regular font_size=40'";
  elm_entry_text_style_user_push(entry, user_style);
  /* Guide text font */
  elm_object_part_text_set(entry, "elm.guide",
                           "<font=Sans:style=Regular font_size=40>Guide Text</font>");
  ```

## Setting the Font Using EDC

To create a layout with text using the EDC, you can set the font for each text or textblock part:

- Set the font of a single text or textblock part using the font family name and a specific style of the font family:

  ```
  part {
     name: "text";
     type: TEXT;
     scale: 1;
     description {
        state: "default" 0.0;
        rel1.relative: 0.0 0.5;
        rel2.relative: 0.5 1.0;
        color: 0 136 170 255;
        color2: 0 136 170 50;
        color3: 0 136 170 25;
        text {
           size: 25;
           font: "Sans:style=Bold";
           text: "Enventor";
           align: 0.5 0.5;
        }
     }
  }

  part {
     name: "textblock";
     type: TEXTBLOCK;
     scale: 1;
     description {
        state: "default" 0.0;
        align: 0.5 0.5;
        fixed: 0 0;
        min: 0 0;
        visible: 1;
        text.text: "TEXTBLOCK";
        text.font: "Sans:style=Bold";
        rel1.relative: 0.16 0.18;
        rel2.relative: 0.88 0.38;
     }
  }
  ```

- Set the font of multiple textblock parts using the style information:

  ```
  styles {
     style {
        name: "textblock_style1";
        base: "font=Sans:style=Regular font_size=30";
     }
  }

  part {
     name: "textblock";
     type: TEXTBLOCK;
     scale: 1;
     description {
        state: "default" 0.0;
        align: 0.5 0.5;
        fixed: 0 0;
        min: 0 0;
        visible: 1;
        text.text: "TEXTBLOCK";
        text.style: "textblock_style1";
        rel1.relative: 0.16 0.18;
        rel2.relative: 0.88 0.38;
     }
  }
  ```

## Using the Edje Text Class

You can use the Edje Class: Text API (in [mobile](../../../api/mobile/latest/group__Edje__Object__Text__Class.html) and [wearable](../../../api/wearable/latest/group__Edje__Object__Text__Class.html) applications) to change multiple text occurrences as a batch. If you set a new font or font size to a text class, the change is applied to multiple objects.

> **Note**
>
> Note that the `text_class` cannot be used in a UI component with markup text or the `elm_entry_text_style_user_push()` function. You must set the `text_class` in EDC.

To set the text class, you can use reserved words or make your own text class:

- Set a class for a text part:

  ```
  part {
     name: "text";
     type: TEXT;
     scale: 1;
     description {
        state: "default" 0.0;
        rel1.relative: 0.0 0.5;
        rel2.relative: 0.5 1.0;
        color: 0 136 170 255;
        color2: 0 136 170 50;
        color3: 0 136 170 25;
        text {
           size: 25;
           font: "Sans:style=Bold";
           text: "Enventor";
           align: 0.5 0.5;
           text_class: "my_class";
        }
     }
  }
  ```

- Set a class for a textblock:

  ```
  styles {
     style {
        name: "textblock_style1";
        base: "font=Sans:style=Regular font_size=30 ... text_class=my_class";
     }
  }

  part {
     name: "textblock";
     type: TEXTBLOCK;
     scale: 1;
     description {
        state: "default" 0.0;
        align: 0.5 0.5;
        fixed: 0 0;
        min: 0 0;
        visible: 1;
        text.text: "TEXTBLOCK";
        text.style: "textblock_style1";
        rel1.relative: 0.16 0.18;
        rel2.relative: 0.88 0.38;
     }
  }
  ```

- Set the font, style, and size of a text class that you have created in the EDC file:

  ```
  elm_config_font_overlay_set("my_class", "TizenSans:style=Bold", 30);
  elm_config_font_overlay_apply();
  ```

- Set a specific ratio to a given font size for each object through the text class. If you give a negative value as font size, it is used as the percentage of the originally given font size. The following example code sets the font size as 150% of the given font size.

  ```
  elm_config_font_overlay_set("my_class", "TizenSans:style=Bold", -150);
  elm_config_font_overlay_apply();
  ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
