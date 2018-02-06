# Styling Controls with JSON

You can style a toolkit control with JSON. This topic uses a PushButton as an example control.

## Visuals

Visuals are the main building block of controls. A control is built from visuals with properties set as required.

The following Visual types are available:

| Type           | Example                                  |
| -------------- | ---------------------------------------- |
| Border         | ![Border visual](media/border-visual.png) |
| Color          | ![Color visual](media/color-visual.png)  |
| Gradient       | ![Gradient visual](media/linear-gradient-visual.png) |
| Image          | ![Image visual](media/image-visual.png)  |
| N-Patch        | ![NPatch visual](media/n-patch-visual.png) |
| SVG            | ![SVG visual](media/svg-visual.svg)      |
| Animated Image | ![SVG visual](media/animated-image-visual.gif) |
| Mesh           | ![Mesh visual](media/mesh-visual.png)    |
| Primitive      | ![Primitive visual](media/cube.png)      |
| Text           | **Hello there**                          |

For more information on how to create, register, and use visuals, and lists all properties associated with each visual type, see [Visuals](visuals.md).

<a name="newview"></a>
## Styling a New View

Styling is inherited, so styling a parent automatically affects its child, unless overridden.

The following table describes the Style properties offered by View and PushButton.

| Name                 | Type      | Description                              |
|--------------------|---------|----------------------------------------|
| `heightResizePolicy` | `string`  | See [Size Negotiation](creating-custom-view-controls.md#sizenegotiation). |
| `widthResizePolicy`  | `string`  | See [Size Negotiation](creating-custom-view-controls.md#sizenegotiation). |
| `sizeModeFactor`     | `vector3` | Gets/sets the relative to the parent size factor of the view. |
| `minimumSize`        | `Size2D`  | Gets/sets the minimum size a view can be assigned in size negotiation. |
| `maximumSize`        | `Size2D`  | Gets/sets the maximum size a view can be assigned in size negotiation. |

> **Note**   
> `sizeModeFactor` is only used when `ResizePolicyType` is set to either `ResizePolicyType.SizeRelativeToParent` or `ResizePolicyType.SizeFixedOffsetFromParent`. The view's size is set to the view's size multiplied by or added to this factor, depending on `ResizePolicyType`.

<a name="state"></a>
## Styling for State

A control has 3 states: `NORMAL`, `FOCUSED`, and `DISABLED`. In addition, a button has 2 substates, `SELECTED` and `UNSELECTED`, applicable for each of the 3 main states. Each state must have the required visuals, either as its own set of visuals or as a visual shared between states.

A different `backgroundVisual` can be supplied for `NORMAL`, `FOCUSED`, and `DISABLED`, if required. A different `backgroundVisual` can also be defined for the `SELECTED` and `UNSELECTED` states.

In the following example:

-   **"inherit"** means that the Push Button inherits any styles defined for Button.
-   **"visuals"** means that specific visual types can be put in that section.
-   **"states"** means that visuals for specific states can be put in that section.

```
"styles":
{
  "PushButton":
  {
    "inherit":["Button"],
    "visuals":
    {
      "iconVisual": { "visualType":"IMAGE", "url":"icon1.png" },
      "labelVisual": { "visualType":"TEXT", "text":"OK", "fontWeight":"bold" }
    },
    "states":
    {

    }
  }
}
```

The following process shows how you can build up a stylesheet, state by state:

1.  The following example defines the states common to all controls:

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

2. The following example adds the button substates (`UNSELECTED` and `SELECTED`) to the stylesheet, but still provides no visuals.

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

3. The following example defines a background visual for each substate in the `NORMAL` state. The same can be done for `FOCUSED` and `DISABLED`.

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
                 "visualType":"IMAGE",
                 "url":"backgroundUnSelected.png"
               }
            }
          },
          "SELECTED":
          {
            "visuals":
            {
              "backgroundVisual":
               {
                 "visualType":"IMAGE",
                 "url":"backgroundSelected.png"
               }
            }
          }
        }
      },
    }
    ```

## Transitions

The control (Button) changes states based on user interaction. All controls can move between the `NORMAL`, `FOCUSED`, and `DISABLED` states. In addition, a button can have the `UNSELECTED` and `SELECTED` substates.

To move between states and substates, transition animations can be defined. Each state and substate can have an "entry" and "exit" transition.

To make defining common transitions easier, an effect can be used with a "from" and "to" state. One such effect is CROSSFADE, which animates the opacity of visuals fading in and out to give a nice transition. Initially, only CROSSFADE is available, but in time further effects can be provided.

The transition can be placed in the state section, such as `NORMAL`. In the following example, the transition cross-fades between unselected and selected visuals:

```
"transitions":
[
  {
     "from":"UNSELECTED",
     "to":"SELECTED",
     "visualName":"*",
     "effect":"CROSSFADE",
     "animator":
     {
       "alphaFunction":"EASE_OUT",
       "duration":"0.2,
       "delay":0
     }
  }
]
```

The following example uses the entry and exit transition for the `UNSELECTED` substate:

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
               "visualType":"IMAGE",
               "url":"backgroundUnSelected.png"
             }
          },
          "entryTransition":
          {
            "target":"backgroundVisual",
            "property":"mixColor",
            "targetValue":[1,1,1,1],
            "animator":
            {
              "alphaFunction":"LINEAR",
              "duration":0.3,
              "delay":0.0
            }
         },
         "exitTransition":
         {
            "target":"backgroundVisual",
            "property":"mixColor",
            "targetValue":[1,1,1,0.0],
            "animator":
            {
              "alphaFunction":"LINEAR",
              "duration":0.3,
              "delay":0.0
            }
         }
       }
     }
   }
  }
]
```

<a name="example"></a>
## Example Stylesheet

The following example shows a button stylesheet covering all states and various transitions:

```
{
  "styles":
  {
    "PushButton":
    {
      "inherit":["Button"],
      "visuals":
      {
        "iconVisual":
        {
          "visualType":"IMAGE",
          "url":"icon1.png"
        },
        "label":
        {
          "visualType":"TEXT",
          "text":"OK",
          "fontWeight":"bold"
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
                  "visualType":"IMAGE",
                  "url":"backgroundSelected.png"
                }
              }
            },
            "SELECTED":
            {
              "visuals":
              {
                "backgroundVisual":
                {
                  "visualType":"IMAGE",
                  "url":"backgroundUnselected.png"
                }
              }
            }
          },
          "transitions":
          [
            {
              "from":"UNSELECTED",
              "to":"SELECTED",
              "visualName":"*",
              "effect":"CROSSFADE",
              "animator":
              {
                "alphaFunction":"EASE_OUT",
                "duration":0.2,
                "delay":0
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
              "visualType":"TEXT",
              "text":"OK",
              "fontWeight":"bold"
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
            "visualName":"*",
            "effect":"CROSSFADE",
            "animator":
            {
              "alphaFunction":"EASE_IN_OUT",
              "duration":0.3
            }
          }
        }
      },
      "autoRepeating":false,
      "togglable":false,
      "labelPadding":[ 12.0, 12.0, 12.0, 12.0 ],

      "transitions":
      [
        {
          "from":"NORMAL",
          "to":"DISABLED",
          "visualName":"*",
          "effect":"CROSSFADE",
          "animator":
          {
            "alphaFunction":"EASE_OUT",
            "duration":0.2,
            "delay":0
          }
        }
      ]
    }
  }
}
```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
