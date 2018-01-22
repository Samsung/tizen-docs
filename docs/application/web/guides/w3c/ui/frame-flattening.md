# Frame Flattening

In the Tizen WebKit, content placed within the `<frame>` and `<iframe>` tags is expanded automatically according to the content size. This enables users to view the whole content at once without scrolling.

This feature is supported in mobile applications only.

The Tizen WebKit supports this feature since scrolling through small subframes on small screen devices is a tedious task and, occasionally, causes confusion between scrolling subframes and scrolling the Web page itself.

To implement scrollable content in the Tizen WebKit, use the CSS `overflow: scroll` or `webkit-overflow-scrolling: touch` property instead of `iframe`.

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
