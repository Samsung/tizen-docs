# Recommendations

Recommendations are not strict rules, but you should follow them anyway, when possible.

The following recommendations apply to the Tizen 4.0 TV platform:

-   [Always show the focus](#show-focus-always) on the screen
-   [Make a partial screen partial](#define-screen-size-based-on-layer)
-   [Provide confirmation](#provide-confirmation) for crucial actions

## Show Focus Always

The selectable elements on the screen are controlled by the remote control.

Since it is important that the user knows which item is currently focused, the focus should always appear on 1 item.

## Define Screen Size Based on Layer

To keep the user fully aware of the current screen:

-   The full screen has history information, and it is located on the main screen layer of each application. Consequently, the full screen must be full-sized.
-   The partial screen has no history and appears temporarily. To clearly differentiate the partial screen from the full screen, make it smaller than the full screen.

## Provide Confirmation

A confirmation within a popup is necessary when an item is deleted or an application is terminated.

The confirmation prevents unexpected critical actions which the user does not intend to perform.


