# Customizing UI Components

This topic explains how to customize UI components. Before learning the process of customization, you must understand the concept of "style" and "theme" in EFL and how EFL applies the right style for a UI component.

EFL provides the EDC script as a way for defining a look for UI components. For more information on how to write an EDC script, see [Layouting with EDC](learn-edc-intro.md).

## Style, Theme, and EDC

The style of a UI component refers to its graphical appearance determined by the layout, shapes, fonts, and colors. A theme is a collection of styles for every UI component. Tizen provides a default theme for each profile and version, which includes all available styles of every UI component.

When more than one style is defined for a UI component in the current theme, you can set a different style than the default one using the `elm_object_style_set()` function. It is also possible to access the current style with the `elm_object_style_get()` function.

The default theme of the mobile profile specifies several [styles for the check UI component](mobile/component-check.md#styles). The following example shows how to set the `favorite` style to a newly created check object:

```
Evas_Object *check;

check = elm_check_add(parent);
elm_object_style_set(check, "favorite");
```

A theme is defined in [EDC](learn-edc-intro.md) (`.edc`) files, and they are compiled into an EDJ (`.edj`) file during the project building. An EDC file is a collection of [group](learn-edc-group.md) blocks, and one group is composed of [parts](learn-edc-part.md) and [programs](learn-edc-program.md). A theme corresponds to one EDJ file, and a style corresponds to 1 group in an EDJ file.

The following example shows some groups in an EDC file (`check.edc`), which correspond to the styles of the check component in mobile profile:

```
group {
   name: "elm/check/base/default";
   /* Other content */
}

group {
   name: "elm/check/base/favorite";
   /* Other content */
}

group {
   name: "elm/check/base/on&off";
   /* Other content */
}
```

The groups have a certain format of names according to the naming rule of Elementary. These 3 groups define 3 different styles for the check component: `default`, `favorite`, and `on&off`.

## Customization

In the best scenario, every application can find the style it needs in the already provided theme. However, you can sometimes need customized styles. EFL allows you to define a new style and add it to an existing theme, or even make a new theme.

To customize a UI component:

1. Create a project for a basic EDC UI application.

   See [Creating Your First Tizen Mobile Native Application](../../../getting-started/mobile/first-app.md) or [Creating Your First Tizen Wearable Native Application](../../../getting-started/wearable/first-app.md) for creating a EDC UI project.

2. Create an EDJ file in the `/res/edje/` directory.

   If you add the `custom.edc` file, the Tizen Studio calls Edje tools automatically to build the final `custom.edj` file when building the project.

   The EDJ file is installed under the application data path. You can get the full path of where the EDJ file is installed using the `app_get_resource()` function.

   ```
   char edj_path[PATH_MAX] = {0,};

   app_get_resource("/edje/custom.edj", edj_path, (int)PATH_MAX);
   ```

3. Write a style in the EDC file.

4. Register the EDJ file in the C code. You can attach the EDJ file to an existing theme in the following ways:

   - As an extension: extend the default theme by adding new styles
   - As an overlay: override the styles in the default theme

   The following code snippet shows how to add the new theme file as an extension:

   ```
   char edj_path[PATH_MAX] = {0,};

   /* Get the full path of the EDJ file */
   app_get_resource("/edje/custom.edj", edj_path, (int)PATH_MAX);

   /* Load the check custom style as an extension */
   elm_theme_extension_add(NULL, edj_path);
   ```

5. Set the new style to the UI component.

   To use the `custom` style on a new check component:

   ```
   Evas_Object *check;

   check = elm_check_add(parent);

   /* Set the newly defined custom style */
   elm_object_style_set(check, "custom");
   ```

You can see the above steps implemented in the "ThemeExtension" section within the [EFL Core samples](https://developer.tizen.org/development/sample/native/UI/EFL_Core_samples) sample application.

### Extension and Overlay

To attach an EDJ file to an existing theme, you can use:

- Extension

  A theme extension enables you to extend a theme with only a part of the UI component's style (not all of it).

  Applications can add and delete a theme in the list of extensions with the following calls:

  ```
  elm_theme_extension_add(NULL, "./theme_button_style_custom.edj");
  elm_theme_extension_del(NULL, "./theme_button_style_custom.edj");
  ```

  The above example assumes that the `theme_button_style_custom.edj` file contains a new button style called `custom`.

- Overlay

  A theme overlay enables you to replace the look of all UI components by overriding the default style.

  If a new style called `default` is created for a button component and it is added as an overlay, Elementary uses the overlay for all button components overriding the default theme.

  Applications can add and delete a theme in the list of overlays with the following calls:

  ```
  elm_theme_overlay_add(NULL, "./theme_button.edj");
  elm_theme_overlay_del(NULL, "./theme_button.edj");
  ```

  The above example assumes that the `theme_button.edj` file only contains a new theme for the button component.

  Adding a theme with a default style as an overlay is not recommended, since it makes Elementary to use the new theme for all the objects defined in the application. You must make sure that the `theme_button.edj` file reimplements everything that was previously defined in the default theme concerning the button component.

  > **Note**
  >
  > With overlays, you can replace the default view and affect every UI component. This is very similar to setting the theme for the whole application, and probably clashes with the end user options. Using overlays also runs the risk of non-matching styles across the application. Unless you have a very good reason to use them, avoid overlays.

The following process shows how Elementary loads a style of a certain name:

1. Check the list of overlays registered on the current theme.

2. If the right style is not found, check the default theme.

3. If the right style is not found, check the list of extensions registered on the current theme.

4. If the right style is not found, use the default style.

   This means that the style with the certain name is not defined in the current theme.

For example, if you make your own EDJ file and name a group `elm/button/base/default`:

- If you use the `elm_theme_overlay_add` function, the newly defined style is applied to a button object.
- If you use the `elm_theme_extension_add` function, the newly defined style is not applied, since there is a group with the same name in the default theme.

> **Note**
>
> When using the `elm_theme_extension_add()` or `elm_theme_overlay_add()` function to add a new theme extension or overlay to a theme object (the default theme), Elementary calls the `elm_theme_flush()` function to flush the Elementary theme caches. This means that the theme of all UI components that use the default theme is reloaded.

### Example: Creating a Customized Style for the Check Component

An easy way to create a customized style is to copy one of the existing styles and modify some parts or programs. The following example shows how to define a custom style of the check component based on the default style. The aim is to update the background and the check images of the UI component with custom images.

When customizing a style, you need to respect the parts and signals in the default style. If something is missing, it can break the UI component's behavior. You can add new `SWALLOW` parts, if you want to control more content from the application. However, removing existing `SWALLOW` parts can change the UI component's behavior.

To create a customized check component style:

1. Copy the group corresponding to the `default` style to a new file and rename the group to `custom` to create a new `custom` style:

   ```
   group {
      name: "elm/check/base/custom";
      /* Copy of the content of "default" style */
   }
   ```

2. In the new `elm/check/base/custom` group, find the parts you want to modify.

   To modify the background and check images, you must locate the `bg` and `check` parts.

   ```
   part {
      name: "bg";
      mouse_events: 0;
      scale: 1;
      description {
         state: "default" 0.0;
         rel1.offset: 1 1;
         rel2.relative: 0.0 1.0;
         rel2.offset: 1 -2;
         align: 0.0 0.5;
         min: 16 16;
         max: 16 16;
         aspect: 1.0 1.0;
         aspect_preference: VERTICAL;
         image {
            normal: "check_base.png";
            border: 5 5 5 5;
            middle: 0;
         }
         fill.smooth: 0;
      }
   }
   part {
      name: "check";
      mouse_events: 0;
      scale: 1;
      description {
         state: "default" 0.0;
         rel1 {
            to: "bg";
            offset: 1 1;
         }
         rel2 {
            to: "bg";
            offset: -2 -2;
         }
         visible: 0;
         color: 255 255 255 255;
         image.normal: "check.png";
      }
      description {
         state: "visible" 0.0;
         inherit: "default" 0.0;
         visible: 1;
      }
      description {
         state: "disabled" 0.0;
         inherit: "default" 0.0;
         visible: 0;
         color: 128 128 128 128;
      }
      description {
         state: "disabled_visible" 0.0;
         inherit: "default" 0.0;
         color: 128 128 128 128;
         visible: 1;
      }
   }
   ```

3. Replace the default images with the new custom images by updating the `image.normal` properties in both parts:

   - In the background part, replace `check_base.png` with `check_base_custom.png`.
   - In the check part, replace `check.png` with `check_custom.png`.

   > **Note**
   >
   > This example assumes that the custom images are the same size as the `default` images.

   ```
   part {
      name: "bg";
      description {
         state: "default" 0.0;
         image {
            normal: "check_base_custom.png";
            border: 5 5 5 5;
            middle: 0;
         }
      }
   }
   part {
      name: "check";
      description {
         state: "default" 0.0;
         image.normal: "check_custom.png";
      }
   }
   ```

### Example: Removing Sound Effects from the Button Component

Sound effects played by the button component are defined and executed in the button styles. The following example shows how to remove sound effects from the button component by defining a custom button style.

To create a customized button component style:

1. Copy the group corresponding to the `default` style to a new file and rename the group to `custom` to create a new `custom` style:

   ```
   group {
      name: "elm/button/base/custom";
      /* Copy of the content of "default" style */
   }
   ```

2. In the new `elm/button/base/custom` group, find the programs playing sound effects.

   > **Note**
   >
   >
   > In the EDC file, sound effects are played by program actions, such as `RUN_PLUGIN`, `PLAY_SAMPLE`, and `PLAY_TONE`.

   ```
   program {
      name: "touch_sound";
      action: RUN_PLUGIN "touch_sound";
   }
   ```

3. Remove the programs related to sound effects.

4. Remove the code lines that execute the removed programs (the line to be removed is marked with a background highlight in the following example).

   > **Note**
   >
   > In the EDC file, programs are executed by the `after` keyword or the `run_program` script function. For example:
   > ```
   > after: "touch_sound";
   > /* OR */
   > run_program(PROGRAM: "touch_sound");
   > ```

   ```
   program {
      name: "clicked";
      signal: "mouse,clicked,1";
      source: "event";
      script {
         run_program(PROGRAM: "touch_sound");
         run_program(PROGRAM: "clicked_signal");
      }
   }
   ```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
