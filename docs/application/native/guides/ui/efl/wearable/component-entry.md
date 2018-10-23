# Entry

This feature is supported in wearable applications only.

The entry component is a box where the user can enter text. It supports the following features:

- Multiline
- Scrolling
- Password mode
- Filtering text
- Read/write from a file
- Theme style overrides

The entry component includes an Evas [Textblock](../../../../api/wearable/latest/group__Evas__Object__Textblock.html) in it, which means that it supports the features of the textblock component, such as text wrapping and formatted markup text.

For more information, see the [Entry](../../../../api/wearable/latest/group__Elm__Entry.html) API.

**Figure: Entry component**

![Entry component](./media/entry_wn.png)

**Figure: Entry hierarchy**

![Entry hierarchy](./media/entry_tree.png)

## Adding an Entry Component

To create an entry component, use the `elm_entry_add()` function. You can set the text inside it with the `elm_entry_entry_set()` function.

```
Evas_Object *entry;
Evas_Object *parent;

entry = elm_entry_add(parent);
elm_entry_entry_set(entry, "A short text.");
```

## Managing the Text

To manage the entry component content:

- Add text to the entry:

  - Append text to the end of the existing content:

    ```
    elm_entry_entry_append(entry, "END");
    ```

  - Insert text at the current cursor position:

    ```
    elm_entry_entry_insert(entry, "CURSOR");
    ```

- Check whether the entry is empty:

  ```
  Eina_Bool Empty = elm_entry_is_empty(entry);
  ```

  If the entry has content, the function returns the Boolean `EINA_FALSE` variable.

- Select text:

  - Select all the content of the entry component:

    ```
    elm_entry_select_all(entry);
    ```

  - Select a part of the text with the `elm_entry_select_region_set()` function.

    The following example selects the first 20 characters of the entry content:

    ```
    elm_entry_select_region_set(entry, 0, 20);
    ```

  - Clear the current selection:

    ```
    elm_entry_select_none(entry);
    ```

- Retrieve the currently selected text:

  ```
  const char *selection;

  selection = elm_entry_selection_get(entry);
  ```

  If the entry text is empty, the function returns `NULL`.

- Copy or cut the selection to the clipboard:

  ```
  elm_entry_selection_cut(entry);
  ```

  Paste the selection in the same or a different entry:

  ```
  elm_entry_selection_paste(entry);
  ```

- Filter the text.

  You can filter the size and individual characters within the entry text by appending a filter with the `elm_entry_markup_filter_append()` function.

  - To limit the size of the entry to 8 characters:

    ```
    static Elm_Entry_Filter_Limit_Size
    limit_size =
    {
        .max_char_count = 8,
        .max_byte_count = 0
    };

    /*
       Append a new callback to the list, this function is called each time
       a text is inserted in the entry. Pass the previously created limit_size struct
       to set the maximum number of characters allowed to 8
    */

    elm_entry_markup_filter_append(entry, elm_entry_filter_limit_size, &limit_size);
    ```

  - To define a list of accepted or rejected characters, append the filter with the `Elm_Entry_Filter_Accept_Set` structure.

   The following example shows how to reject the '+', '-', '*', and '/' characters:

    ```
    static Elm_Entry_Filter_Accept_Set
    accept_set =
    {
        .accepted = NULL,
        .rejected = "+*-/"
    };

    elm_entry_markup_filter_append(entry, elm_entry_filter_accept_set, &accept_set);
    ```

You can define a file (for example, `/tmp/test.txt`) to save the entry content. The content in the file is implicitly loaded and displayed. After the file is set, any content changes in the entry are automatically saved after a short delay.

```
/* Set the file in which the entry text is saved */
/* Implicitly load the existing file content */
elm_entry_file_set(entry, "/tmp/test.txt", ELM_TEXT_FORMAT_MARKUP_UTF8);
```

You can also deactivate the automatic saving feature and explicitly save the content when needed:

```
/* Disable autosaving */
elm_entry_autosave_set(entry, EINA_FALSE);

/* Trigger saving when needed */
elm_entry_file_save(entry);
```

## Managing the Cursor

The cursor represents the current position in the entry, where the next action, for example, text insertion or deletion, is done. Usually, the cursor is represented as a blinking character, but its appearance depends on the theme configuration.

To manage the cursor position:

- Move the cursor to the beginning of the entry:

  ```
  elm_entry_cursor_begin_set(entry);
  ```

- Move the cursor to the end of the entry:

  ```
  elm_entry_cursor_end_set(entry);
  ```

- Move the cursor 1 line down or up:

  ```
  elm_entry_cursor_down(entry);
  elm_entry_cursor_up(entry);
  ```

- Move the cursor 1 character left or right:

  ```
  elm_entry_cursor_prev(entry);
  elm_entry_cursor_next(entry);
  ```

- Set the cursor at a specific position (15th character, for example):

  ```elm_entry_cursor_pos_set(entry, 15);```

- Make a text selection while moving the cursor.

  The following example starts a selection at the current cursor position, moves 5 characters right, and ends the selection:

  ```
  elm_entry_cursor_selection_begin(entry);

  for (i = 0; i < 5; i++)
      elm_entry_cursor_next(entry);

  elm_entry_cursor_selection_end(entry);
  ```

## Configuring the Entry

To configure the entry functionality:

- Make the entry uneditable by the user.

  By default, the user can enter text in the entry component when it is in focus.

  ```
  elm_entry_editable_set(entry, EINA_FALSE);
  ```

  > **Note**
  >
  > Even when the entry component is set to be uneditable by the user, you can still use the `elm_entry_entry_append()` and `elm_entry_entry_insert()` functions to modify its text programmatically.

- Set the password mode.

  If the password mode is set, the entry component hides what the user is typing. In this mode, the display of any text is replaced by asterisks (*), and the entry is a single line (there is no line wrap).

  ```
  elm_entry_password_set(entry, EINA_TRUE);
  ```

- Define the line mode and wrapping.

  The entry component has 2 line modes: single and multiline:

  - To set the entry to the single line mode:

    ```
    elm_entry_single_line_set(entry, EINA_TRUE);
    ```

    In this mode, the text does not wrap when reaching the edge, but the entry grows horizontally instead. Pressing the **Enter** key in this mode generates an `activate` event instead of adding a new line.

  - To set the entry to the multiline mode with wrapping:

    ```
    elm_entry_single_line_set(entry, EINA_FALSE);
    elm_entry_line_wrap_set(entry, ELM_WRAP_WORD);
    ```

    In this mode, the text wraps at the end of the entry and pressing the **Enter** key creates a new line.

    In multiline entries, the `elm_entry_line_wrap_set()` function provides a way to cut the text implicitly into a new line when it reaches the far edge of the UI component. The following wrap modes are available:

    - `ELM_WRAP_NONE`: No wrap
    - `ELM_WRAP_CHAR`: Wrap between characters
    - `ELM_WRAP_WORD`: Wrap in allowed wrapping points (as defined in the Unicode standard)
    - `ELM_WRAP_MIXED`: Word wrap, and if that fails, character wrap

## Modifying Formatting and Using Special Markups

You can format the entry text in many ways:

- Format the entry text with markup elements that are defined in the theme.

  For example, you can use the `<br>` element to insert a line break. For a list of available markup elements, see [Formatted text](../../../../api/wearable/latest/group__Elm__Entry.html#entry-markup).

- Add special markups within the entry text:

  - Anchors: `<a href = ..>...</a>`
  The anchors generate an `anchor,clicked` signal when the user clicks them. The `href` attribute is used to identify the anchor. The anchor also reacts to the `anchor,in` (mouse in), `anchor,out` (mouse out), `anchor,down` (mouse down), and `anchor,up` (mouse up) events.

  - Items: `<item size = .. vsize = .. href = ..>...</item>`
  The items provide a way to insert any `Evas_Object` in the text. The `Evas_Object` name must be specified in the `href` attribute.

- Override the textblock object style.

  To tweak the style of the text within the entry component, you can override parts of the theme style to the textblock object using the `elm_entry_text_style_user_push()` function. The function pushes a new style on top of the user style stack that overrides the current style. Remove the style at the top of the user style stack with the `elm_entry_text_style_user_pop()` function.

- Modify the content and text parts of the default theme:

  - You can modify 2 content parts of the default theme: `icon` and `end`.

    The following example shows how to set an icon in the `end` content part:

    ```
    Evas_Object *icon;

    ic = elm_icon_add(entry);
    elm_image_file_set(ic, "icon.png", NULL);
    elm_object_part_content_set(entry, "end", icon);
    ```

  - You can modify 2 text parts of the default theme: `elm.text` (entry text) and `elm.guide` (entry placeholder).

    The following example shows how to set the placeholder text to `Hello World`:

    ```
    elm_object_part_text_set(entry, "elm.guide", "Hello World");
    ```

## Using the Entry Callbacks

To receive notifications about the entry events, listen for the following signals:

- `aborted`: The **Escape** key is pressed on a single line entry.
- `activated`: The **Enter** key is pressed on a single line entry.
- `anchor,clicked`: An anchor is clicked.
  The `event_info` callback parameter points to an `Elm_Entry_Anchor_Info` object.
- `anchor,down`: The mouse button is pressed on an anchor.
  The `event_info` callback parameter points to an `Elm_Entry_Anchor_Info` object.
- `anchor,hover,opened`: The anchor is clicked.
  The `event_info` callback parameter points to an `Elm_Entry_Anchor_Info` object.
- `anchor,in`: The mouse cursor is moved into an anchor.
  The `event_info` callback parameter points to an `Elm_Entry_Anchor_Info` object.
- `anchor,out`: The mouse cursor is moved out of an anchor.
  The `event_info` callback parameter points to an `Elm_Entry_Anchor_Info` object.
- `anchor,up`: The mouse button is released on an anchor.
  The `event_info` callback parameter points to an `Elm_Entry_Anchor_Info` object.
- `changed`: The text within the entry is changed.
- `changed,user`: The text within the entry is changed because of user interaction.
  The `event_info` callback parameter points to an `Edje_Entry_Change_Info` object.
- `clicked`: The entry is clicked (mouse press and release).
- `clicked,double`: The entry is double-clicked.
- `clicked,triple`: The entry is triple-clicked.
- `cursor,changed`: The cursor position is changed.
- `cursor,changed,manual`: The cursor position is changed manually.
- `focused`: The entry receives focus.
  The `event_info` callback parameter points to an `Elm_Focus_Info` object.
- `unfocused`: The entry loses focus.
- `language,changed`: The program language is changed.
- `longpressed`: The mouse button is pressed and held for a couple of seconds.
- `maxlength,reached`: The maximum length is reached.
- `preedit,changed`: The preedit string is changed.
- `press`: The mouse button is pressed on the entry.
- `redo,request`: The request is redone.
- `selection,changed`: The current selection is changed.
- `selection,cleared`: The current selection is cleared.
- `selection,copy`: A copy of the selected text into the clipboard is requested.
- `selection,cut`: A cut of the selected text into the clipboard is requested.
- `selection,paste`: A paste of the clipboard content is requested.
- `selection,start`: A selection is begun and no previous selection exists.
- `text,set,done`: The whole text is set to the entry.
- `theme,changed`: The theme is changed.
- `undo,request`: The request is undone.

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

If not mentioned separately, the `event_info` callback parameter in all signals is `NULL`.

To register and define a callback for the `focused` signal:

```
{
    evas_object_smart_callback_add(entry, "focused", focused_cb, data);
}

/* Callback for the "focused" signal */
/* Called when the entry receives the focus */
void
focused_cb(void *data, Evas_Object *obj, void *event_info)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Entry focused\n");
}
```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
