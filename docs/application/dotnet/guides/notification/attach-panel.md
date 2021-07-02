# Attach Panel


The attach panel allows you to attach various content into an application that contains an attach panel. You can attach images, take pictures, record voice, and select files on the attach panel.

This API is supported on Tizen mobile devices that support [attach panel features](#prerequisites).

The main features of the Tizen.Applications.AttachPanel namespace are the following:

-   Create an attach panel

    You can [create an attach panel](#create) and manage events related to user selections and panel visibility. You can add and remove content categories.

    You can also [create an attach panel in xamarin](#createInxamarin) by using [Custom Renderers](https://developer.xamarin.com/guides/xamarin-forms/application-fundamentals/custom-renderer/).

-   Manage an attach panel

    You can [set extra data](#manage) to a content category to manage its content.


![Attach panel](./media/attach_panel_area.png)

**Figure: Attach panel**

The attach panel contains UI components that manages user interactions on its interface. The layout component includes the tabBar and scroller components, which are connected to show the content synchronously. The scroller component contains pages that displays content. For example, images, camera, and voice recorder. The contents are shown as a page on the panel. However, some contents can be launched from the  **More** tab of the panel using [application controls](../app-management/app-controls.md).

The attach panel contains half and full display modes. The mode can be changed by swiping up and down the page.


![Attach panel modes](./media/attach_mode.png)

**Figure: Attach panel modes**

<a name="categories"></a>
## Content Categories

You can manage the following types of content:

-   Images

    In half mode, you can select and attach only one image at a time. In full mode, you can select and attach multiple images at a time.

-   Camera

    You can take a picture and attach it to the content using a device camera.

-   Voice

    You can attach voice recording to the content.

-   Various content in the **More** tab

    You can use the additional category icons in the **More** tab, for example, video, audio, calendar, contact, myfiles, and video recorder. Click the respective icon to launch the category.
	
The following figure explains the content types. From left to right: images, camera, voice, and **More** tab content.


![Images content](./media/attach_images.png) ![Camera content](./media/attach_camera.png) ![Voice content](./media/attach_voice.png) ![More content](./media/attach_more.png)

**Figure: Content categories**

<a name="prerequisites"></a>
## Prerequisites


This section explains, how you can enable your application to use the attach panel functionality:

1.  To use the [Tizen.Applications.AttachPanel](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AttachPanel.html) namespace, the application must request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <!--To add the image viewer and camera UI gadget in the attach panel-->
       <privilege>http://tizen.org/privilege/mediastorage</privilege>
       <!--To add the camera UI gadget in the attach panel-->
       <privilege>http://tizen.org/privilege/camera</privilege>
       <!--To launch the camera, verify that the video call status is not active-->
       <privilege>http://tizen.org/privilege/telephony</privilege>
       <!--To add the voice recorder UI gadget in the attach panel-->
       <privilege>http://tizen.org/privilege/recorder</privilege>
       <!--To launch apps from the More tab-->
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
    </privileges>
    ```

2. To use the attach panel features, include the following feature in your tizen-manifest.xml file.

	```XML
	<feature name="http://tizen.org/feature/attach_panel"/>
	```
	
3.  To use the methods and properties of the Tizen.Applications.AttachPanel namespace, include the following namespace in your application:

    ```csharp
    using Tizen.Applications.AttachPanel;
    ```
	
4.  To create an attach panel instance, an [ElmSharp.Conformant](/application/dotnet/api/TizenFX/latest/api/ElmSharp.Conformant.html) instance is required. To create the instance, follow any of the step mentioned:
    -   For Tizen platform conformant, see [Get the Tizen platform conformant](#getConformant).
    -   Create a conformant, into which you can add the attach panel later:

        ```csharp
        class App : CoreUIApplication
        {
            Conformant conformant;

            protected override void OnCreate()
            {
                /// Application initialization

                conformant = new Conformant(window);
                conformant.Show();
                conformant.SetContent(bg);

            }
        }
        ```

<a name="create"></a>		
## Create an Attach Panel


1.  Create an attach panel using the [Tizen.Applications.AttachPanel.AttachPanel](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AttachPanel.AttachPanel.html) class.

    When the attach panel is created, the state is hidden by default. To show the created panel, use the `Show()` method of the `Tizen.Applications.AttachPanel.AttachPanel` class.

    ```csharp
    AttachPanel attachPanel;

    public void CreateAttachPanel(Conformant conformant)
    {
        if (attachPanel == null)
        {
            attachPanel = new AttachPanel(conformant);
            attachPanel.AddCategory(ContentCategory.Image, null);
            attachPanel.Show();
        }
    }
    ```

2.  Select the type of content for the attach panel. Add content categories using the AddCategory() method, based on the type of content. The available content categories are defined in the [Tizen.Applications.AttachPanel.ContentCategory](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AttachPanel.ContentCategory.html) enumeration.

    The content categories in the **More** tab are shown in the frequency of recently used and alphabetical sequence.

    To deliver more information to the UI gadget or called application, add the data within a bundle.

    ```csharp
    Bundle bundle = new Bundle();
    bundle.AddItem("http://tizen.org/appcontrol/data/total_count", "3");

    attachPanel.AddCategory(ContentCategory.Image, bundle);

    attachPanel.AddCategory(ContentCategory.Camera, null);
    attachPanel.AddCategory(ContentCategory.Voice, null);
    attachPanel.AddCategory(ContentCategory.Video, null);
    attachPanel.AddCategory(ContentCategory.Audio, null);
    attachPanel.AddCategory(ContentCategory.Calendar, null);
    attachPanel.AddCategory(ContentCategory.Contact, null);
    attachPanel.AddCategory(ContentCategory.Myfiles, null);
    attachPanel.AddCategory(ContentCategory.VideoRecorder, null);
    attachPanel.AddCategory(ContentCategory.Document, null);
    attachPanel.AddCategory(ContentCategory.TakePicture, null);
    attachPanel.AddCategory(ContentCategory.Memo, null);

    attachPanel.Show();
    ```
    > **Note**
    >
    > To use the camera content category `attachPanel.AddCategory(ContentCategory.Camera, null)`, you must verify the video call status. To launch the camera, the video call status must not be active. To verify the status of video call, Telephony API `telephony_call_get_type()`  is called, ensure that the telephony privilege is added to the tizen-manifest.xml file.

3.  Register the required event handlers:

    -   To access the data that you select in the called application, register the `ResultCallback` event of the `Tizen.Applications.AttachPanel.AttachPanel` class and define an event handler for it.

        Select and confirm the content category to trigger the event. In the event handler, you can retrieve the selected items from the `Result.ExtraData` property of the [Tizen.Applications.AttachPanel.ResultEventArgs](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AttachPanel.ResultEventArgs.html) class.

    -   To monitor published events from the panel side, register the `EventChanged` event of the `Tizen.Applications.AttachPanel.AttachPanel` class and define an event handler for it.

        Publish the reserved events (defined in the [Tizen.Applications.AttachPanel.EventType](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AttachPanel.EventType.html) enumeration) from the panel side to trigger the event.

    ```csharp
    private void AttachPanelResultCallback(object sender, ResultEventArgs e)
    {
        if (e.ResultCode != AppControlReplyResult.Succeeded)
        {
            /// Error handling

            return;
        }

        IEnumerable<string> selectedItems;
        if (e.Result.ExtraData.TryGet("http://tizen.org/appcontrol/data/selected", out selectedItems))
        {
            foreach (var item in selectedItems)
            {
                Tizen.Log.Debug("AttachPanelTest", $"Selected content type is {e.Category}, selected item is {item}");
            }
        }
        else
        {
            /// Error handling
        }
    }

    private void AttachPanelEventChanged(object sender, StateEventArgs e)
    {
        switch (e.EventType)
        {
            case EventType.ShowStart:
                /// Attach panel showing starts
                break;
            case EventType.ShowFinish:
                /// Attach panel showing ends
                break;
            case EventType.HideStart:
                /// Attach panel hiding starts
                break;
            case EventType.HideFinish:
                /// Attach panel hiding ends
                break;
        }
    }

    attachPanel.ResultCallback += AttachPanelResultCallback;
    attachPanel.EventChanged += AttachPanelEventChanged;
    ```

4.  When the content category is not required, you can remove the content category using the RemoveCategory() method:

    ```csharp
    public void RemoveCategory()
    {
        attachPanel.RemoveCategory(ContentCategory.Image);
        attachPanel.RemoveCategory(ContentCategory.Camera);
    }
    ```

<a name="createInxamarin"></a>
## Create an Attach Panel in Xamarin

To create an attach panel in Xamarin, use the custom renderers:

1.  <a name="getConformant"></a>Get the Tizen platform conformant.

    In Tizen, `BaseLayout.Parent` is the conformant of the main window.

    ```csharp
    public static EvasObject WindowConformant
    {
        set; get;
    }

    protected override void OnCreate()
    {
        base.OnCreate();
        WindowConformant = BaseLayout.Parent;
        LoadApplication(new App());
    }
    ```

2.  Create the custom control.

    The following example creates an `AttachPanelLayout` custom control, which is a custom renderer showing the attach panel in the `ContentView`. The control also has the `IsAttachPanelVisibleProperty` property, which determines whether the attach panel is shown or hidden.

    ```csharp
    public partial class AttachPanelLayout : ContentView
    {
        public static readonly BindableProperty IsAttachPanelVisibleProperty =
            BindableProperty.Create("IsAttachPanelVisible", typeof(bool), typeof(AttachPanelLayout), true);

        public bool IsAttachPanelVisible
        {
            get
            {
                return (bool)GetValue(IsAttachPanelVisibleProperty);
            }
            set
            {
                SetValue(IsAttachPanelVisibleProperty, value);
            }
        }

        public AttachPanelLayout()
        {
            InitializeComponent();
        }
    }
    ```

3.  Use the custom control.

    The following code example shows how the `attachPanelLayout` custom control can be used by a C\# page:

    ```csharp
    private void OpenAttachPanelClicked(object sender, EventArgs e)
    {
        if (attachPanelLayout != null)
        {
            attachPanelLayout.IsAttachPanelVisible = true;
        }
        else
        {
            if (Content is StackLayout layout)
            {
                attachPanelLayout = new AttachPanelLayout();
                layout.Children.Add(attachPanelLayout);
            }
        }
    }
    ```

4.  Create the custom renderer on the Tizen platform:

    ```csharp
    [assembly: ExportRenderer(typeof(AttachPanelLayout), typeof(AttachPanelLayoutRenderer))]
    namespace AttachPanelSample.Tizen.Mobile
    {
        public class AttachPanelLayoutRenderer : LayoutRenderer
        {
            private AttachPanel attachPanel;

            protected override void OnElementChanged(ElementChangedEventArgs<Xamarin.Forms.Layout> e)
            {
                base.OnElementChanged(e);

                if (attachPanel == null)
                {
                    attachPanel = new AttachPanel(Program.WindowConformant);

                    attachPanel.AddCategory(ContentCategory.Image, null);
                }

                attachPanel.Show();

                if (e.OldElement != null)
                {
                    attachPanel.ResultCallback -= AttachPanelResultCallback;
                    attachPanel.EventChanged -= AttachPanelEventChanged;
                    attachPanel = null;
                }

                if (e.NewElement != null)
                {
                    attachPanel.ResultCallback += AttachPanelResultCallback;
                    attachPanel.EventChanged += AttachPanelEventChanged;
                }
            }
        }
    }
    ```

<a name="manage"></a>
## Manage an Attach Panel
To manage an attach panel content, you can set extra data to a previously added content category using a bundle. Use the `SetExtraData()` method of the [Tizen.Applications.AttachPanel.AttachPanel](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AttachPanel.AttachPanel.html) class.

The following are the extra data supported by the attach panel:
-   `http://tizen.org/appcontrol/data/total_count`: Total count of selected items in the Images category
-   `http://tizen.org/appcontrol/data/total_size`: Total size of selected items in the VideoRecorder category within the **More** tab

```csharp
public void SetTotalCountOfSelectedImages()
{
    Bundle bundle = new Bundle();
    bundle.AddItem("http://tizen.org/appcontrol/data/total_count", "3");

    attachPanel.SetExtraData(ContentCategory.Image, bundle);
}

public void SetTotalSizeOfSelectedItems()
{
    Bundle bundle = new Bundle();
    bundle.AddItem("http://tizen.org/appcontrol/data/total_size", "200000");

    attachPanel.SetExtraData(ContentCategory.VideoRecorder, bundle);
}
```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
