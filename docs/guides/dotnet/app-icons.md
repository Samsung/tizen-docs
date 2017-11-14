Application Icons
=================

## Dependencies

- Tizen 4.0 and Higher

You can show the application icon as a shortcut on the home screen to
allow the user to easily launch the application. In the device
application list, you can show a badge with the application icon to
provide additional information about the application state or
notifications to the user.

The main application icon features include:

-   Creating and removing a badge

    You can use badges in your application to inform the user about
    notifications and events. A badge is an image displayed on the
    application icon.

    You can [create a badge for an application](#create) and remove it.

- Managing the badge

    You can [get and set the count and display attributes for the
    badge](#manage).

- Adding a shortcut

    You can [add a shortcut](#add) to the home screen to launch
    an application.

- Adding a widget

    If you have created a widget application, you can [add the
    widget](#add_widget) to the home screen.

**Figure: Badges and shortcuts**

![Shortcuts](../images/shortcut.png) ![Badges](../images/badge.png)


Prerequisites
-------------

To enable your application to use the application icon functionality:

-   To handle badges:
    1.  To use the
        [Tizen.Applications.Badge](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Badge.html)
        class, the application has to request permission by adding the
        following privilege to the `tizen-manifest.xml` file:

        ``` {.prettyprint}
        <privileges>
           <privilege>http://tizen.org/privilege/notification</privilege>
        </privileges>
        ```

    2. To use the methods and properties of the
        Tizen.Applications.Badge class, include it in your application:

        ``` {.prettyprint}
        using Tizen.Applications.Badge;
        ```

- To handle shortcuts:
    1.  To use the
        [Tizen.Applications.Shortcut](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Applications_1_1Shortcut.html)
        namespace, the application has to request permission by adding
        the following privilege to the `tizen-manifest.xml` file:

        ``` {.prettyprint}
        <privileges>
           <privilege>http://tizen.org/privilege/shortcut</privilege>
        </privileges>
        ```

    2. To use the methods and properties of the
        Tizen.Applications.Shortcut namespace, include it in your
        application:

        ``` {.prettyprint}
        using Tizen.Application.Shortcut;
        ```



Creating and Removing a Badge <a id="create"></a>
-----------------------------

To create and remove badges:

-   To create a badge for an application, create an instance of the
    [Tizen.Applications.Badge](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Badge.html) class.
    The parameter defines the application for which the badge is added.
    If the application is adding a badge for itself, the parameter can
    be null.

    ``` {.prettyprint}
    Badge badge = new Badge(appId);
    BadgeControl.Add(badge);
    ```

    The application that creates the badge can also update and
    remove it. When applications are signed with the same certificate,
    they can control each other's badges.

    If an application not signed with the same certificate must be
    allowed to [manage a badge](#manage), use the `Add()` method of the
    [Tizen.Applications.BadgeControl](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1BadgeControl.html)
    class with a writable application ID. The writable application ID
    enables another application to control your application to manage
    the badge. You can also configure your application to handle the
    badge itself.

- To remove the badge from the application, call the
    `Remove()` method. The only parameter is the ID of the application
    whose badge is to be removed.

    ``` {.prettyprint}
    BadgeControl.Remove(TEST_PKG);
    ```



Managing the Badge <a id="manage"></a>
------------------

To manage the badge:

-   Retrieve the badge count and visibility with the `Find()` method of
    the
    [Tizen.Applications.BadgeControl](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1BadgeControl.html) class.
    The values are stored in the `count` and `visible` properties of the
    [Tizen.Applications.Badge](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Badge.html) class.

    The badge count is displayed in the upper-right corner of the badge
    and the `count` property value must be an integer. The `visible`
    property value is of the `Bool` type.

    ``` {.prettyprint}
    uint count;
    bool visible;

    Badge badge = BadgeControl.Find(TEST_PKG);

    count = badge.Count;
    visible = badge.Visible;
    ```

- Set the `count` and `visible` properties with the `Update()` method:

    ``` {.prettyprint}
    Badge badge = new Badge(TEST_PKG);
    BadgeControl.Add(badge);

    badge.Count = 5;
    badge.Visible = false;

    BadgeControl.Update(badge);
    ```



Adding a Shortcut <a id="add"></a>
-----------------

To add a shortcut to the home screen:

1.  Define the shortcut details (such as its name, icon path, and
    whether duplicates are allowed) with the properties of the
    [Tizen.Applications.Shortcut.HomeShortcutInfo](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Shortcut_1_1HomeShortcutInfo.html) class.

    You can create 2 types of shortcuts:

    -   If you set the `Uri` property, clicking the shortcut opens
        the URI.
    -   If the `Uri` property is not set, clicking the shortcut launches
        the application that set the shortcut.

    ``` {.prettyprint}
    HomeShortcutInfo shortcut = new HomeShortcutInfo
    {
        ShortcutName = "Home",
        IconPath = "Icon_Path",
        IsAllowDuplicate = true,
        Uri = "http://www.tizen.org"
    };
    ```

2. Add the shortcut using the `Add()` method of the
    [Tizen.Applications.Shortcut.ShortcutManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Shortcut_1_1ShortcutManager.html)
    class:

    ``` {.prettyprint}
    ShortcutManager.Add(shortcut);
    ```



Adding a Widget <a id="add_widget"></a>
---------------

To add a widget to the home screen:

1.  Before adding a widget to the home screen, a widget application must
    be prepared.
2. Define the widget details (such as its ID, size, and period) with
    the properties of the
    [Tizen.Applications.Shortcut.WidgetShortcutInfo](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Shortcut_1_1WidgetShortcutInfo.html)
    class:

    ``` {.prettyprint}
    widgetshortcutinfo shortcut = new widgetshortcutinfo
    {
        shortcutname = "samplewidget",
        iconpath = "icon_path",
        isallowduplicate = false,
        widgetid = "widgetid",
        widgetsize = shortcutwidgetsize.widgetdefault,
        period = 1.0f
    };
    ```

    To add a widget, you must know the widget ID and supported sizes.

3. Add the widget using the `Add()` method of the
    [Tizen.Applications.Shortcut.ShortcutManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Applications_1_1Shortcut_1_1ShortcutManager.html)
    class:

    ``` {.prettyprint}
    ShortcutManager.Add(shortcut);
    ```


