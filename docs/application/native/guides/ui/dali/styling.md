# Styling UI Components



You can style DALi UI components with a theme bundle or a folder containing a JSON style file and resources. Styling allows you to modify the look of your application. You can alter the images, colors, and other properties specifying the look of each control type. You can also change the visuals of a control, for example, instead of a background image, you can use a fill color or gradient instead.

You can specify how each application component looks by using a stylesheet with the JSON file format:

- Application-specific resources must be installed into a particular directory, and you can access them in the stylesheet indirectly through the `APPLICATION_RESOURCE_PATH` constant, which has the value returned by the `app_get_resource_path()` function. For more information on the resource directory, see the `app_get_resource_path()` function in the App Common API (in [mobile](../../../api/mobile/latest/group__CAPI__APP__COMMON__MODULE.html) and [wearable](../../../api/wearable/latest/group__CAPI__APP__COMMON__MODULE.html) applications).

- You can style particular controls or sub-groups of controls by specifying their style name programmatically.

- Styles can be inherited and tweaked, so you can create minor updates to existing styles with very little code.

- The platform can change the default system font family and logical size. This is handled by the default stylesheets, but it is possible to override this behavior in your own stylesheets. You can also listen for the style manager's `StyleChangedSignal()` in order to determine when the platform style has changed.

## Stylesheet Loading

The stylesheet is usually supplied at the application start-up or through the `Dali::Toolkit::StyleManager` API:

- At the start-up, use the `Dali::Application::New()` function:

  ```
  int main( int argc, char** argv )
  {
    Application application = Application::New( &argc, &argv, "stylesheet.json" );
    {
      Demo::StylingApplication stylingApplication( application );
      application.MainLoop();
    }

    return 0;
  }
  ```

- During runtime, use the `Dali::Toolkit::StyleManager::ApplyTheme()` function:

  ```
  StyleManager::Get().ApplyTheme( "stylesheet.json" );
  ```

When the stylesheet is loaded, it is automatically merged with the default DALi toolkit stylesheet, and applied to each `Control` instance.


## Stylesheet Format

A style sheet has several top-level **sections**, which are named JSON objects. The following table lists the available sections.

**Table: Stylesheet sections**

| Section     | Description                              |
|-------------|------------------------------------------|
| `constants` | An object containing a map of tokens that are replaced in JSON value strings. |
| `includes`  | An array of filenames to include and merge. |
| `mappings`  | An object containing a map of keys to property maps. These maps replace the key as a value when converting to DALi properties. |
| `styles`    | An object containing a map of style names to property maps. These property maps contain key-value pairs with the key matching a DALi property name for the object being styled, and the value is an appropriate type for that property. |

### Constants Section

The `constants` section contains string constants that can be used by any string value in the current stylesheet or included stylesheets. The following table lists the predefined constants.

**Table: Predefined constants**

| Constant                    | Description                              |
|-----------------------------|------------------------------------------|
| `APPLICATION_RESOURCE_PATH` | This points to the application-specific resource path returned by the `app_get_resource_path()` function. |
| `PACKAGE_PATH`              | This points to the DALi toolkit resource path. |

Constants can also be set programmatically by using the `StyleManager::SetStyleConstant()` function. However, the function only works after the `Application::New()` function has been called, so it does not affect stylesheets loaded in the `Application::New()` function.

The constants can be used in any string value in the JSON files, delimited by '{' and '}' characters. In the following example, the `IMAGE_DIR` constant is defined within the stylesheet, and is used to access the `unselectedStateImage` image path in the `Dali::Toolkit::PushButton` control:

```
{
  "constants": {
    IMAGE_DIR="{APPLICATION_RESOURCE_PATH}/images"
  },

  "styles": {
    "PushButton": {
      "unselectedStateImage": "{IMAGE_DIR}/button-up.9.png"
    }
  }
}
```

### Includes Section

The `includes` section allows inclusion of other JSON files into the stylesheet. Note that since this section is a JSON array, it is delimited by square brackets ('[' and ']').

The content of the included files are merged with the other content of the current stylesheet. If more than one included file supplies values for a particular key-value pair, then the last file has the highest priority.

In the following example, the `include/first-include.json` and `include/second-include.json` files are loaded. These include files can also include other files, and use constants defined in this top-level stylesheet.

```
{
  "constants": {
    "INCLUDE_DIR": "include"
  },
  "includes":
  [
    "{INCLUDE_DIR}/first-include.json",
    "{INCLUDE_DIR}/second-include.json"
  ]
}
```

### Mappings Section

To reduce the number of repeated key-values, you can use the `mappings` section. It contains an object of key-value pairs, where the value is any valid JSON type (so can also form a tree).

If a value in any section is a JSON string delimited by '<' and '>', it is checked against the keys in the mapping section, and the value is replaced by the mapping.

In the following example, the confirmation popup's `backingColor` property value becomes the JSON array representing RGBA values, which is converted internally into a `Dali::Vector4` when it is applied to an object:

```
{
  "mappings": {
    "backgroundColor": [0.12, 0.0, 0.25, 1.0]
  },
  "styles": {
    "ConfirmationPopup": {
      "backingColor": "<backgroundColor>"
    }
  }
}
```

### Styles Section

The `styles` section is the main section of the stylesheet. Each key in this JSON object is a style name, which is used to match against control instances in your application:

- By default, a `Dali::Toolkit::Control` class's name is also its style name. For finer control, you can programmatically set a style name for a given control using the `Control::SetStyleName()` function. In the following example, the slider control handle text label has been given the style name `SliderHandleTextLabel`. This means that for any instance of the slider, the handle label style can be specified independently of any other label.

- For each entry in the `styles` section, the children of the entry are the property names of the matching control. In the following example, `showPopup` is the name of a property in the slider. For more information on the properties of a specific control, see its API Reference.

- Each control has a `background` property, which can specify a visual. In addition, properties named `visual`, such as those in the following example, specify a visual.

The following example switches on the value label of the handle and the popup tooltip, and changes the visuals of the slider control to use the specified 9-patch images with the given sizes. It changes the property of the slider handle text label to alter the color of the text, and changes the background of the slider to show a gradient fill.

```
{
  "styles": {
    "Slider": {
      "showValue": true,
      "showPopup": true,
      "trackVisual": {
        "url": "{IMAGE_DIR}/slider-skin.9.png",
        "size": [27, 27]
      },
      "progressVisual": {
        "url": "{IMAGE_DIR}/slider-skin-progress.9.png",
        "size": [27, 27]
      },
      "handleVisual": {
        "url": "{IMAGE_DIR}/slider-skin-handle.png",
        "size": [72,72]
      },
      "background": {
        "visualType": "GRADIENT",
        "startPosition": [0.0, -0.5],
        "endPosition": [0.0, 0.5],
        "stopOffset": [0.0, 0.5, 0.75, 1.0],
        "stopColor": [[0.0,0.0,1.0,1.0], [0.0,0.0,0.75,1.0], [0.0,0.0,0.5,1.0], [1.0,1.0,1.0,0.0]]
      }
    },
    "SliderHandleTextLabel": {
      "textColor":[0.8, 0.8, 1.0, 1.0]
    }
  }
}
```

| Before styling:                          | After styling:                           |
|------------------------------------------|------------------------------------------|
| ![Slider before styling](./media/dali_styling1.png) | ![Slider after styling](./media/dali_styling2.png) |

When styling UI components, consider the following issues:

- Setting the font size

  Setting an explicit font size for text controls is generally considered to be a bad idea: the Tizen platform offers 5 levels of logical font size that can be set by the user, and the stylesheet can be used on multiple devices with different screen sizes and resolutions.

  To handle the logical to point size conversion after a settings change, the style manager appends `FontSize` and the logical value ("0"-"4") to each style name during the update, and uses that style in preference to the control class name or style name if it can find it in the style sheet.

  This means that you can specify alternative mappings for particular text labels. The following example shows how to map the alternative logical sizes, if you have a text label that has a style name of `FolderLabel`:

  ```
  {
    "styles": {
      "FolderLabelFontSize0": {
        "pointSize": 8
      },
      "FolderLabelFontSize1": {
        "pointSize": 10
      },
      "FolderLabelFontSize2": {
        "pointSize": 12
      },
      "FolderLabelFontSize3": {
        "pointSize": 16
      },
      "FolderLabelFontSize4": {
        "pointSize": 20
      }
    }
  }
  ```

- Using style inheritance

  It is possible to "inherit" properties from one style into another by specifying the style names in a `styles` array. More than 1 style can be merged in this way. The inherited styles are first merged in order, and then any properties that follow are merged on top.

  In the following example, the ColorSlider inherits all of the properties from the slider entry, and changes the background to a gradient:

  ```
  {
    "styles": {
      "ColorSlider": {
        "styles": ["Slider"], // Inherit from Slider style
        "background": {
          "visualType": "GRADIENT",
          "startPosition": [0.0, -0.5],
          "endPosition": [0.0, 0.5],
          "stopOffset": [0.0, 0.5, 0.75, 1.0],
          "stopColor": [[0.0,0.0,1.0,1.0], [0.0,0.0,0.75,1.0], [0.0,0.0,0.5,1.0], [1,1,1,0.09]]
        }
      }
    }
  }
  ```

- Applying a style to your own control instances

  If you require finer-grained control of styling, such as for particular labels in your application, you can use an alternative style. Set the style name of these instances after they are created:

  ```
  TextLabel label = TextLabel::New( myLabelText );
  label.SetStyleName( "AppLabel" );
  ```

  You can add the alternative style to the application stylesheet as usual:

  ```
  {
    "styles": {
      "AppLabel": {
        "textColor": [0.8, 0.8, 1.0, 1.0]
      }
    }
  }
  ```

- Using alternative color representations

  For style properties that explicitly map to a known DALi property with the `Vector4` type, the style system can deduce that the map can also represent a color. In this case, the style system also accepts alternative color representations.

  > **Note**  
  > This type deduction does not work in the visual property maps where there is no explicit mapping.

  The usual representation is a `Vector4` with its components mapped to the R, G, B and A components in the range of 0-1:

  ```
  {
    "styles": {
      "AppLabel": {
        "textColor": [0.49, 0.235, 0.596, 1.0]
      }
    }
  }
  ```

  For example, in the following text label example, the `textColor` is a known property of `TextLabel`, so it can use an alternative color format, in this case, the HTML #code:

  ```
  {
    "styles": {
      "AppLabel": {
        "textColor": "#7D3C98"
      }
    }
  }
  ```

  As well as HTML code, you can use device-specific strings, or you can also use the object format with separately specified RGB components (and optional alpha component):

  ```
  {
    "styles": {
      "AppLabel": {
        "textColor": {"r":125, "g":60, "b":152}
      }
    }
  }
  ```

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
