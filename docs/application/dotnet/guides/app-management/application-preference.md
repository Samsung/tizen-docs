# Application Preferences

Many applications are required to save data in the persistent memory and read them in the next session in a safe way. Saved data can be sensitive, so in many cases access to the saved preference should be restricted. Preference API allows you to share stored preference data among applications in the same package.

## Store and retrieve records

To store a variable, you must create a key-value pair. Use the following function to create a preference for a specific simple type: `Preference.Set(string key, value)`.

Before storing or retrieving a variable, check whether it exists using the `Preference.Contains(string key)` function. Use the following function to retrieve a stored variable: `Preference.Get<T>()`:

  ```csharp
  //set/get integer value
  Preference.Set("test_integer", 10);

  if (Preference.Contains("test_integer"))
  {
      var testInt = Preference.Get<int>("test_integer");
  }
  ```

To store and retrieve string variables, use the following functions:

  - `Preference.Set("test_string", "TEST VALUE")`
  - `Preference.Get<string>("test_string")`

## List records 

To list all records, use `Keys` collection `Preference.Keys()`:

  ```csharp
    Preference.Set("Option_enabled", true);
    Preference.Set("active_user", "Joe");
    Preference.Set("default_volume", 10);
    Preference.Set("brightness", "0.6");

    foreach(string key in Preference.Keys)
    {
        Tizen.Log.Info("TEST", string.Format("Key name: {0}", key));
    }

  ```

## Remove records

To safely remove records, use `Preference.Remove(string key)`:

```csharp
    if (Preference.Contains("key"))
    {
        Preference.Remove("key");
    }
```

To remove all records, use the following function:
  - `Preference.RemoveAll()`

## Manage application preferences

The following code snippet shows how to store counter value when the application is closed using [Tizen.Applications.Preference](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Preference.html) module.

**Figure: Preference Application Screenshot**

![Screenshot](./media/preferences.png)

The clicked counter is stored as a pair of key-value data. When the application starts it tries to read this value and inserts it in the label component.
To use NUI components and Preference module, the following namespaces are included:

```csharp
using System;

using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

using Tizen.Applications;
```

The `ClickedPreferenceKey` key is used to store counter value. It has to be declared as a class member for it to be used in button callbacks. Also, the `TextLabel` has to be a class member to show and update the counter value:

```csharp
namespace NUIPreference
{
    class Program : NUIApplication
    {
        private readonly string LogTag = "NUI_Application";
        private readonly string ClickedPreferenceKey = "clicked_counter";

        private int ClickedCounter = 0;

        private TextLabel ResultViewer;

        //...
    }
}
```

The `OnCreate()` handler tries to read value from the `Preference` module. Try/Catch block is useful when `ClickedPreferenceKey` is not set previously:

```csharp
protected override void OnCreate()
{
    base.OnCreate();

    try
    {
        ClickedCounter = Preference.Get<int>(ClickedPreferenceKey);
    } catch (Exception e) {
        Tizen.Log.Error(LogTag, e.ToString());
    }

    Initialize();
}
```

In `OnTerminate()` method you can save key-value pairs:

```csharp
protected override void OnTerminate()
{
    Preference.Set(ClickedPreferenceKey,  ClickedCounter);
    base.OnTerminate();
}
```

The `CreateButtons()` method is a helper function. It is responsible for the following:
- Creating buttons layout,
- Creating buttons,
- Setup callbacks:

```csharp
private View CreateButtons()
{
    View buttonsContainer = new View()
    {
        WidthResizePolicy = ResizePolicyType.FillToParent,
        HeightResizePolicy = ResizePolicyType.FitToChildren,
        Layout = new LinearLayout()
        {
            HorizontalAlignment = HorizontalAlignment.Center,
            LinearOrientation = LinearLayout.Orientation.Horizontal
        }
    };

    var btnSize = new Size2D(220, 80);

    var addButton = new Button() { Size2D = btnSize, Text = "+" };
    var decButton = new Button() { Size2D = btnSize, Text = "-" };
    var saveButton = new Button() { Size2D = btnSize, Text = "Save" };
    var removeButton = new Button() { Size2D = btnSize, Text = "Remove" };

    addButton.Clicked += OnAddClicked;
    decButton.Clicked += OnDecClicked;
    saveButton.Clicked += OnSaveClicked;
    removeButton.Clicked += OnRemoveClicked;

    buttonsContainer.Add(addButton);
    buttonsContainer.Add(decButton);
    buttonsContainer.Add(saveButton);
    buttonsContainer.Add(removeButton);

    return buttonsContainer;
}
```

The `Initialize()` function creates application layout and components:

```csharp
void Initialize()
{
    Window.Instance.KeyEvent += OnKeyEvent;

    View rootView = new View()
    {
        BackgroundColor = Color.White,
        WidthResizePolicy = ResizePolicyType.FillToParent,
        HeightResizePolicy = ResizePolicyType.FillToParent,
        Layout = new LinearLayout()
        {
            CellPadding = new Size2D(30, 30),
            Padding = new Extents(30, 30, 30, 30),
            LinearOrientation = LinearLayout.Orientation.Vertical
        }
    };

    var buttonsContainer = CreateButtons();
    rootView.Add(buttonsContainer);

    ResultViewer = new TextLabel()
    {
        Text = string.Format("Current Counter: {0}", ClickedCounter)
    };

    rootView.Add(ResultViewer);
    Window.Instance.GetDefaultLayer().Add(rootView);
}
```

The `OnAddClicked()` handler increase the counter and update the result label value:

```csharp
public void OnAddClicked(object sender, ClickedEventArgs e)
{
    ClickedCounter++;
    ResultViewer.Text = string.Format("Current Counter: {0}", ClickedCounter);
}
```

The `OnDecClicked()` handler decrease the counter and also update the label:

```csharp
public void OnDecClicked(object sender, ClickedEventArgs e)
{
    ClickedCounter--;
    ResultViewer.Text = string.Format("Current Counter: {0}", ClickedCounter);
}
```

The `OnSaveClicked()` handler saves the `ClickedCounter` value in the preference module:

```csharp
public void OnSaveClicked(object sender, ClickedEventArgs e)
{
    Preference.Set(ClickedPreferenceKey, ClickedCounter);
}
```

The `OnRemoveClicked()` handler resets `ClickedCounter` value and removes it from the `Preference` module:

```csharp
public void OnRemoveClicked(object sender, ClickedEventArgs e)
{
    try
    {
        Preference.Remove(ClickedPreferenceKey);
    } catch (Exception error) {
        Tizen.Log.Error(LogTag, error.ToString());
    }

    ClickedCounter = 0;
    ResultViewer.Text = string.Format("Current Counter: {0}", ClickedCounter);
}
```

Application entry point:

```csharp
static void Main(string[] args)
{
    var app = new Program();
    app.Run(args);
}
```

## Related information
- Dependencies
  - Tizen 2.4 and Higher
- API Reference
  - [Tizen.Applications.Preference](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Preference) class
