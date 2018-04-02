# Styling Components with JSON

You can style a toolkit component with a JSON stylesheet. When styling a component, you can use visuals, which are the main building block of UI components. A component is built from visuals with properties set as required. For more information on how to create, register, and use visuals, and the properties associated with each visual type, see [Visuals](visuals.md).

The examples in this topic illustrate the styling of a push button control.

<a name="newview"></a>
## Inherited Styles

Styling is inherited. This means that styling a parent automatically affects its child, unless overridden.

The following table describes the style properties of the [Tizen.NUI.BaseComponents.View](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.BaseComponents.View.html) class that automatically affect a push button, as it is a child of the view.

**Table: View style properties affecting a push button**

| Name                     | Type                     | Description              |
|----------------|--------------------|----------------|
| `HeightResizePolicy`     | `string`                 | See [Size Negotiation](creating-custom-view-controls.md#sizenegotiation) |
| `WidthResizePolicy`      | `string`                 | See [Size Negotiation](creating-custom-view-controls.md#sizenegotiation) |
| `SizeModeFactor`         | `vector3`                | Factor used to calculate the view size<br><br> **Note**<br> This property is used only when `ResizePolicyType` is set to `ResizePolicyType.SizeRelativeToParent` or `ResizePolicyType.SizeFixedOffsetFromParent`.<br> The view's size is accordingly set by  multiplying the view size by this factor, or by adding the factor to the view size.           |
| `MinimumSize`            | `Size2D`                 | Minimum size a view can  be assigned in size negotiation  |
| `MaximumSize`            | `Size2D`                 | Maximum size a view can  be assigned in size negotiation              |

<a name="state"></a>
## Styling for States

Every control has three states: `NORMAL`, `FOCUSED`, and `DISABLED`. In addition, buttons have two substates for each state: `SELECTED` and `UNSELECTED`.

You can provide a different style for each state using visuals. When using visuals, you must define a visual for each state and substate (although you can share the same visual across multiple states). The control's current state and substate determines which visuals are shown.

In addition to the basic icon and label visuals, you can define a different background visual for the `NORMAL`, `FOCUSED`, and `DISABLED` states. A different background visual can also be defined for the `SELECTED` and `UNSELECTED` substates.

In the following example:

-   `inherit` means that the `PushButton` element inherits any styles defined for the `Button` element.
-   `visuals` means that specific visual types can be put in that section.
-   `states` means that visuals for specific states can be put in that section.

```
"styles":
{
   "PushButton":
   {
      "inherit": ["Button"],
      "visuals":
      {
         "iconVisual": {"visualType": "IMAGE", "url": "icon1.png"},
         "labelVisual": {"visualType": "TEXT", "text": "OK", "fontWeight": "bold"}
      },
      "states":
      {

      }
   }
}
```

The following process shows how you can build up a JSON stylesheet, state by state:

1.  Define the states common to all controls:

    ```
    "states":
    {
       "NORMAL":
       {
       },
       "DISABLED":
       {
       },
       "FOCUSED":
       {
       },
    }
    ```

    At this point, the states have been defined, but no visuals are provided.

2.  Add the button substates (`UNSELECTED` and `SELECTED`) to the stylesheet.

    Still, no visuals are provided.

    ```
    "states":
    {
       "NORMAL":
       {
          "states":
          {
             "UNSELECTED":
             {
             },
             "SELECTED":
             {
             }
          }
       },
       "DISABLED":
       {
          "states":
          {
             "UNSELECTED":
             {
             },
             "SELECTED":
             {
             }
          }
       },
    }
    ```

3.  Define a background visual for each substate in the `NORMAL` state.

    You can do the same for the `FOCUSED` and `DISABLED` states too.

    ```
    "states":
    {
       "NORMAL":
       {
          "states":
          {
             "UNSELECTED":
             {
                "visuals":
                {
                   "backgroundVisual":
                   {
                      "visualType": "IMAGE",
                      "url": "backgroundUnSelected.png"
                   }
                }
             },
             "SELECTED":
             {
                "visuals":
                {
                   "backgroundVisual":
                   {
                      "visualType": "IMAGE",
                      "url": "backgroundSelected.png"
                   }
                }
             }
          }
       },
    }
    ```

## Transitions

Controls change states based on user interaction. As a control moves between states and substates, transition animations can be used to show visually how the control state changes.

In addition to animations, you can use a predefined effect during the transition. Currently, only a `CROSSFADE` effect is available, animating the opacity of visuals fading in and out. In time, further effects can be provided.

You can implement transitions in two ways:

-   You can define a transition between two specific states, by using the `from` and `to` properties.

    The following example defines a transition from the `UNSELECTED` state to the `SELECTED` state, cross-fading all visuals with the `CROSSFADE` effect:

    ```
    "transitions":
    [
       {
          "from": "UNSELECTED",
          "to": "SELECTED",
          "visualName": "*",
          "effect": "CROSSFADE",
          "animator":
          {
             "alphaFunction": "EASE_OUT",
             "duration": 0.2,
             "delay": 0
          }
       }
    ]
    ```

-   You can define an "entry" and "exit" transition for each state and substate. The transition animations are run as the control enters or exits a specific state. The transitions can be placed in a state section, such as `NORMAL`.

    The following example defines an entry and exit transition for the `UNSELECTED` substate:

    ```
    "states":
       {
          "NORMAL":
          {
             "states":
             {
                "UNSELECTED":
                {
                   "visuals":
                   {
                      "backgroundVisual":
                      {
                         "visualType": "IMAGE",
                         "url": "backgroundUnSelected.png"
                      }
                   },
                   "entryTransition":
                   {
                      "target": "backgroundVisual",
                      "property": "mixColor",
                      "targetValue": [1,1,1,1],
                      "animator":
                      {
                         "alphaFunction": "LINEAR",
                         "duration": 0.3,
                         "delay": 0.0
                      }
                   },
                   "exitTransition":
                   {
                      "target": "backgroundVisual",
                      "property": "mixColor",
                      "targetValue": [1,1,1,0.0],
                      "animator":
                      {
                         "alphaFunction": "LINEAR",
                         "duration": 0.3,
                         "delay": 0.0
                      }
                   }
                }
             }
          }
       }
    ]
    ```

<a name="example"></a>
## Example JSON Stylesheet

The following example shows a push button stylesheet covering all states and various transitions:

```
{
   "styles":
   {
      "PushButton":
      {
         "inherit": ["Button"],
         "visuals":
         {
            "iconVisual":
            {
               "visualType": "IMAGE",
               "url": "icon1.png"
            },
            "label":
            {
               "visualType": "TEXT",
               "text": "OK",
               "fontWeight": "bold"
            }
         },
         "states":
         {
            "NORMAL":
            {
               "states":
               {
                  "UNSELECTED":
                  {
                     "visuals":
                     {
                        "backgroundVisual":
                        {
                            "visualType": "IMAGE",
                            "url": "backgroundSelected.png"
                        }
                     }
                  },
                  "SELECTED":
                  {
                     "visuals":
                     {
                        "backgroundVisual":
                        {
                           "visualType": "IMAGE",
                           "url": "backgroundUnselected.png"
                        }
                     }
                  }
               },
               "transitions":
               [
                  {
                     "from": "UNSELECTED",
                     "to": "SELECTED",
                     "visualName": "*",
                     "effect": "CROSSFADE",
                     "animator":
                     {
                        "alphaFunction": "EASE_OUT",
                        "duration": 0.2,
                        "delay": 0
                     }
                  }
               ]
            },
            "FOCUSED":
            {
               "visuals":
               {
                  "labelVisual":
                  {
                     "visualType": "TEXT",
                     "text": "OK",
                     "fontWeight": "bold"
                  }
               },
               "states":
               {
                  "SELECTED":
                  {
                  },
                  "UNSELECTED":
                  {
                  }
               }
            },
            "DISABLED":
            {
               "states":
               {
                  "SELECTED":
                  {
                     "visuals":
                     {
                        "backgroundVisual":
                        {
                           "visualType": "IMAGE",
                           "url": "{DALI_IMAGE_DIR}button-down-disabled.9.png"
                        }
                     }
                  },
                  "UNSELECTED":
                  {
                     "visuals":
                     {
                        "backgroundVisual":
                        {
                           "visualType": "IMAGE",
                           "url": "{DALI_IMAGE_DIR}button-disabled.9.png"
                        }
                     }
                  }
               },
               "transitions":
               {
                  "visualName": "*",
                  "effect": "CROSSFADE",
                  "animator":
                  {
                     "alphaFunction": "EASE_IN_OUT",
                     "duration": 0.3
                  }
               }
            }
         },
         "autoRepeating": false,
         "togglable": false,
         "labelPadding": [12.0, 12.0, 12.0, 12.0],
         "transitions":
         [
            {
               "from": "NORMAL",
               "to": "DISABLED",
               "visualName": "*",
               "effect": "CROSSFADE",
               "animator":
               {
                  "alphaFunction": "EASE_OUT",
                  "duration": 0.2,
                  "delay": 0
               }
            }
         ]
      }
   }
}
```

## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
