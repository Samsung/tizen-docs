
# Coding Applications

When coding your application, you must consider the following issues:

1.  Initialize the application resources.

    Typically, at least take care of creating the UI and restoring the latest application state.

2.  Write code for application-specific features and functionalities, and handle events.

    Define how the application behaves during the application's state transitions, such as switching between foreground and background.  You must also define event handlers corresponding to system events, if necessary.

3.  Destroy allocated resources and save the current application state.

<a name="hover"></a>
## Using Hover Help

The Tizen Studio supports hover help for Web API and W3C Widget APIs.

The hover help provides input from the [API Reference](../../api/latest/device_api/mobile/index.html).

**Figure: Hover help**

![Hover help](./media/hover_help.png)

<a name="add"></a>
## Adding External Source Code or Library

External source files are located in the project directory, and its `/js` and `/css` sub-directories. You can add a new folder or source file (such as CSS, HTML, JSON, XML, and JavaScript) to your existing project.

You can add files in the following ways (as an example, the instructions illustrate the adding of a CSS file):

-   Adding a new file:
    1.  In the **Project Explorer** view, right-click an existing project and select **New &gt; CSS File**.
    2.  In the **New CSS File** view, select the location of the new CSS file and enter the file name.

        Optionally, you can select a template as initial content in the CSS file.

    3.  Click **Finish**.

-   Adding an existing file:
    1.  In the **Project Explorer** view, right-click the `/css` sub-directory and select **Import &gt; General &gt; File System**.
    2.  In the **Import** view, click **Browse** and select the import location.
    3.  Click **Finish**.



> **Note**  
> You can also drag and drop external source files or libraries.  If you drop a file to the **Project Explorer** view, the **File Operation** dialog appears, and allows you to either copy the file or create a link to it.
