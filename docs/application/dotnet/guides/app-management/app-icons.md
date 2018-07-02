# Application Icons


You can show the application icon as a shortcut on the home screen to allow the user to easily launch the application. In the device application list, you can show a badge with the application icon to provide additional information about the application state or notifications to the user.

The main application icon features include:

-   Creating and removing a badge

    You can use badges in your application to inform the user about notifications and events. A badge is an image displayed on the application icon.

    You can [create a badge for an application](#create) and remove it.

- Managing the badge

    You can [get and set the count and display attributes for the badge](#manage).

- Adding a shortcut

    You can [add a shortcut](#add) to the home screen to launch an application.

- Adding a widget

    If you have created a widget application, you can [add the widget](#add_widget) to the home screen.

**Figure: Badges and shortcuts**

![Shortcuts](./media/shortcut.png) ![Badges](./media/badge.png)


## Prerequisites


To enable your application to use the application icon functionality:

-   To handle badges:
    1.  To use the [Tizen.Applications.Badge](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Badge.html) class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

        ```
        <privileges>
           <privilege>http://tizen.org/privilege/notification</privilege>
        </privileges>
        ```

    2. To use the methods and properties of the Tizen.Applications.Badge class, include it in your application:

        ```
        using Tizen.Applications.Badge;
        ```

- To handle shortcuts:
    1.  To use the [Tizen.Applications.Shortcut](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Shortcut.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

        ```
        <privileges>
           <privilege>http://tizen.org/privilege/shortcut</privilege>
        </privileges>
        ```

    2. To use the methods and properties of the Tizen.Applications.Shortcut namespace, include it in your application:

        ```
        using Tizen.Application.Shortcut;
        ```

<a name="create"></a>
## Creating and Removing a Badge

To create and remove badges:

-   To create a badge for an application, create an instance of the [Tizen.Applications.Badge](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Badge.html) class. The parameter defines the application for which the badge is added. If the application is adding a badge for itself, the parameter can be null.

    ```
    Badge badge = new Badge(appId);
    BadgeControl.Add(badge);
    ```

    The application that creates the badge can also update and remove it. When applications are signed with the same certificate, they can control each other's badges.

    If an application not signed with the same certificate must be allowed to [manage a badge](#manage), use the `Add()` method of the [Tizen.Applications.BadgeControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.BadgeControl.html) class with a writable application ID. The writable application ID enables another application to control your application to manage the badge. You can also configure your application to handle the badge itself.

- To remove the badge from the application, call the `Remove()` method. The only parameter is the ID of the application whose badge is to be removed.

    ```
    BadgeControl.Remove(TEST_PKG);
    ```

<a name="manage"></a>
## Managing the Badge

To manage the badge:

-   Retrieve the badge count and visibility with the `Find()` method of the [Tizen.Applications.BadgeControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.BadgeControl.html) class. The values are stored in the `count` and `visible` properties of the [Tizen.Applications.Badge](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Badge.html) class.

    The badge count is displayed in the upper-right corner of the badge and the `count` property value must be an integer. The `visible` property value is of the `Bool` type.

    ```
    uint count;
    bool visible;

    Badge badge = BadgeControl.Find(TEST_PKG);

    count = badge.Count;
    visible = badge.Visible;
    ```

- Set the `count` and `visible` properties with the `Update()` method:

    ```
    Badge badge = new Badge(TEST_PKG);
    BadgeControl.Add(badge);

    badge.Count = 5;
    badge.Visible = false;

    BadgeControl.Update(badge);
    ```

<a name="add"></a>
## Adding a Shortcut

To add a shortcut to the home screen:

1.  Define the shortcut details (such as its name, icon path, and whether duplicates are allowed) with the properties of the [Tizen.Applications.Shortcut.HomeShortcutInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Shortcut.HomeShortcutInfo.html) class.

    You can create 2 types of shortcuts:

    -   If you set the `Uri` property, clicking the shortcut opens the URI.
    -   If the `Uri` property is not set, clicking the shortcut launches the application that set the shortcut.

    ```
    HomeShortcutInfo shortcut = new HomeShortcutInfo
    {
        ShortcutName = "Home",
        IconPath = "Icon_Path",
        IsAllowDuplicate = true,
        Uri = "http://www.tizen.org"
    };
    ```

2. Add the shortcut using the `Add()` method of the [Tizen.Applications.Shortcut.ShortcutManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Shortcut.ShortcutManager.html) class:

    ```
    ShortcutManager.Add(shortcut);
    ```

<a name="add_widget"></a>
## Adding a Widget

To add a widget to the home screen:

1.  Before adding a widget to the home screen, a widget application must be prepared.
2. Define the widget details (such as its ID, size, and period) with the properties of the [Tizen.Applications.Shortcut.WidgetShortcutInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Shortcut.WidgetShortcutInfo.html) class:

    ```
    Widgetshortcutinfo shortcut = new Widgetshortcutinfo
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

3. Add the widget using the `Add()` method of the [Tizen.Applications.Shortcut.ShortcutManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Shortcut.ShortcutManager.html) class:

    ```
    ShortcutManager.Add(shortcut);
    ```



## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
