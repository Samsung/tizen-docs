# Debugging with Web Inspector
## Dependencies
- Tizen Studio 1.0 and Higher


You can [debug Web applications](https://developer.tizen.org/development/training/web-application/application-development-process/running-and-debugging-applications) using the JavaScript Debugger tool. The JavaScript Debugger is based on Webkit Web Inspector, and has been modified to support remote debugging. 

The JavaScript Debugger supports the following panels:

- [Elements Panel](web-inspector-w.md#element)
- [Resources Panel](web-inspector-w.md#resource)
- [Network Panel](web-inspector-w.md#network)
- [Sources Panel](web-inspector-w.md#source)
- [Timeline Panel](web-inspector-w.md#time)
- [Profiles Panel](web-inspector-w.md#profile_panel)
- [Console Panel](web-inspector-w.md#console)

**Figure: JavaScript Debugger panels**

![JavaScript Debugger panels](./media/jsdebugger_panels.png)

When debugging with the [emulator](https://developer.tizen.org/development/tizen-studio/web-tools/running-and-testing-your-app/emulator), the emulator communicates with the Google Chrome™ browser through the HTTP protocol.

When the JavaScript Debugger is started, the **Network** panel is off. To enable the **Network** panel and start monitoring the resource loading status, press the F5 key. This reloads the current page and displays the load time on the **Network** panel.

## Elements Panel<a name="element"></a>

The **Elements** panel of the JavaScript Debugger allows you to see the Web page components (the DOM tree, CSS style, and Document Object Model).

**Figure: Elements panel**

![Elements panel](./media/remote_inspector_elements.png)

## Resources Panel<a name="resource"></a>

The **Resources** panel of the JavaScript Debugger allows you to inspect resources. You can interact with frames containing resources, such as HTML, JavaScript, CSS, images, and fonts. You can also inspect HTML5 databases, local storage, cookies, and application cache.

**Figure: Resources panel**

![Resources panel](./media/remote_inspector_resources.png)

## Network Panel<a name="network"></a>

The **Network** panel of the JavaScript Debugger allows you to inspect resources downloaded over the network. You can also inspect the HTTP header, response, cookies, and preview.

**Figure: Network panel**

![Network panel](./media/remote_inspector_network.png)

## Sources Panel<a name="source"></a>

The **Sources** panel of the JavaScript Debugger allows you to inspect the JavaScript source page. You can debug your JavaScript code. This panel supports watch expressions, callstack, scope variables, and break point operation. In addition, it supports basic debugging operations: continue, step over, step into, and step out.

**Figure: Sources panel**

![Sources panel](./media/remote_inspector_sources.png)

## Timeline Panel<a name="time"></a>

The **Timeline** panel of the JavaScript Debugger allows you to perform advanced timing and speed analysis. You can see how long the browser takes to handle DOM events, and render and paint windows.

**Figure: Timeline panel**

![Timeline panel](./media/remote_inspector_timeline.png)

## Profiles Panel<a name="profile_panel"></a>

The **Profiles** panel of the JavaScript Debugger allows you to inspect the JavaScript performance analyses. You can inspect CPU profiles or CSS Select profiles.

**Figure: Profiles panel**

![Profiles panel](./media/remote_inspector_profiles.png)

## Console Panel<a name="console"></a>

The **Console** panel of the JavaScript Debugger allows you to inspect the JavaScript console operation. You can interact with your page programmatically. Any errors or warnings on your page are shown in the console.

**Figure: Console panel**

![Console panel](./media/remote_inspector_console.png)