# Managing UI Component Focus

Focus is a common UI concept, which refers to the state of the currently selected or otherwise active UI component on the screen. A UI component is **focused** when it is selected to receive an input event, such as a mouse button click or key press, from the user. A UI component application has, at all times, only 1 focused object to determine where the input event goes to within the application window.

Focused objects can be highlighted or decorated in a specific way to signal to the user where the focus is at any given moment.

There are 2 main ways to set focus on a graphical element:

- Direct (immediate) selection

  The user performs this selection by clicking an element using the touch screen or mouse.

  Direct selection does not really need any kind of special treatment, as the user explicitly selects the UI component to interact with.

- Relative selection

  The user performs this selection by pressing a key.

  In the relative selection, the key press moves the current selection from one UI component to another, such as going to the previous or next one.

## Focusable Objects

An object can be focused if all of the following conditions apply:

- Object is visible

- Object is enabled

- Object accepts focus

  To set an object as focusable, or to determine whether the object is focusable, use the `elm_object_focus_allow_set()` and `elm_object_focus_allow_get()` functions.

- Object's subtree (if any) is focusable

  To set an object and its children as focusable, or to determine whether the object and its children are focusable, use the `elm_object_tree_focus_allow_set()` and `elm_object_tree_focus_allow_get()` functions.

- All of the subtrees in the object's parents are focusable

If any of these conditions do not apply, the object is unfocusable.

To manage focusable objects:

- To determine whether a specific object is focused, use the `elm_object_focus_get()` function.
- To set the focus to an object:
  1. Show the object on the screen with the `evas_object_show()` function.
  2. Set the focus with the `elm_object_focus_set()` function.

     The second parameter is a Boolean value: if it is set to `EINA_TRUE`, the focus is set to the given object; if it is set to `EINA_FALSE`, the focus is unset and passed back to the previous element in the focus chain.
- When a focused UI component is hidden, deleted, or disabled, it becomes unfocusable, and the focus is automatically moved to another object.
- To monitor when the object receives or loses focus, register the `focused` or `unfocused` smart event and define a callback.

## Focus Chain

The order in which the focus moves from one UI component to another is called the focus chain. The default focus chain is the order in which the UI components have been added to the canvas.

> **Note**
>
> If the components are added programmatically in a different order than they appear on the screen, the default focus chain can be quite confusing. In that case, you must customize the focus chain to make it work as expected.

When the user wants to switch the focus to the next object, Elementary searches for the first focusable object in the focus chain. If there is a disabled or read-only object in the focus chain, the focus skips over it to the next object in the requested direction.

When the focus is changed using key presses, Elementary handles the key presses automatically. According to which key is pressed, Elementary switches the focus to the selected direction. For example, if the user presses the **Tab** key, the focus moves to the next object in the natural (default focus chain) order. On the other hand, if the user presses the direction keys, the focus moves to the next object in the requested direction.

### Customizing the Focus Chain

There can be several reasons for customizing the focus chain of an application. For example:

- If you have created a form with labels and text entries next to them, you want the focus to move to the entry field when the user clicks the associated label.
- If you have created an interface with several columns (a table), you can set the focus chain as you wish, for example, going horizontally instead of vertically, regardless of the order in which the UI components are added.

To customize the focus chain:

- Customizing the object-specific focus exit (where the focus moves to after a specific object)

  You can define where the focus moves from a specific object by using the `elm_object_focus_next_object_set()` function. The third parameter is the move direction, which can be one of the following:

  - `ELM_FOCUS_NEXT`: Next UI component in the natural order
  - `ELM_FOCUS_PREVIOUS`: Previous UI component in the natural order
  - `ELM_FOCUS_UP`: UI component to focus when moving up
  - `ELM_FOCUS_DOWN`: UI component to focus when moving down
  - `ELM_FOCUS_RIGHT`: UI component to focus when moving right
  - `ELM_FOCUS_LEFT`: UI component to focus when moving left

  Get the next object in a specific direction using the `elm_object_focus_next_object_get()` function.

- Customizing the entire application's focus chain

  To customize the application's focus chain:

  ```
  Evas_Object *main;
  Evas_Object obj1;
  Evas_Object obj2;
  Evas_Object obj3;
  Evas_Object obj4;
  Evas_Object obj5;

  Eina_List *focus_chain = NULL;
  focus_chain = eina_list_append(focus_chain, obj3);
  focus_chain = eina_list_append(focus_chain, obj2);
  /* Chain is obj3 followed by obj2. Set the chain */
  elm_object_focus_custom_chain_set(main, focus_chain);
  /* Prepend obj5 at the beginning of the chain */
  elm_object_focus_custom_chain_prepend(main, obj5, NULL);
  /* Append obj1 after obj3 */
  elm_object_focus_custom_chain_append(main, obj1, obj3);
  /* Prepend obj4 before obj1 */
  elm_object_focus_custom_chain_prepend(main, obj4, obj1);
  ```

  The focus chain is `obj5, obj3, obj4, obj1, obj2`.

  This applies to any container. It is possible to set the focus chain of a box, for example.

> **Note**
>
> The object-specific focus exit overrides the application's focus chain. This means that if an object is part of a focus chain and, in addition, has the next focused object defined, the next object takes precedence over the focus chain.
>
> Consider the above focus chain example: if `obj4` has `obj5` defined as its next object, the actual focus chain is `obj5, obj3, obj4, obj5` (the chain loops back to `obj5` after `obj4` instead of moving on the `obj1`, as defined in the application focus chain).

If an Evas object has several sub-objects, set its focus chain using the same functions as for the application. Elementary first follows the main focus chain, and then the focus chain of each UI component, as applicable.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
