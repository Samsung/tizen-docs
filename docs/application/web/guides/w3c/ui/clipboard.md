# Clipboard API and events

The clipboard and events feature is used for cutting, copying, and pasting content to easily transfer it between Web applications.

This feature is supported in mobile applications only.

The main features of Clipboard API and events include:

- Copying

  You can fire the `copy` event to [place the selected data on the clipboard](#copying-content).

- Cutting

  You can fire the `cut` event to place the selected data on the clipboard, and [remove the selected content in the document](#cutting-content).

- Pasting

  You can fire the `paste` event to [retrieve data from the clipboard and insert it into a document](#pasting-content). The data is retrieved in the format most appropriate to the assigned context.

The most common way of providing clipboard features in an application is to create an editable element, and allow the user to [copy content and then paste it into the editable element](#copying-and-pasting-content-into-an-editable-element).

## Copying Content

To copy content using the `copy` event:

1. Add an event listener to detect the `copy` event:

   ```
   <script>
       document.addEventListener('copy', function(e) {
           copyHandler(e);
       }, false);
   ```

2. When you start copying, the `copy` event is fired and the `copyHandler()` method is called.

   Stop the system clipboard basic operation and set the range you want to copy:

   ```
       function copyHandler(e) {
           e.preventDefault();

           var range = window.getSelection();
   ```

   > **Note**  
   > If the current selection is not influenced and there is no selected range, the clipboard imports the `setData()` method. The copied content cannot be edited apart from adding a [DataTransferItemList](http://www.w3.org/TR/2014/WD-html51-20140617/editing.html#the-datatransferitemlist-interface) item.

3. Store the data of the selected range:

   ```
           e.clipboardData.setData('text/plain', range);
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [clipboard.html](http://download.tizen.org/misc/examples/w3c_html5/ui/clipboard_api_and_events)

## Cutting Content

To cut content using the `cut` event:

1. Add an event listener to detect the `cut` event:

   ```
   <script>
       document.addEventListener('cut', function(e) {
           cutHandler(e);
       }, false);
   ```

2. When you start cutting, the `cut` event is fired and the `cutHandler()` method is called.

   Stop the system clipboard basic operation and set the range you want to cut:

   ```
       function cutHandler(e) {
           e.preventDefault();

           var range = window.getSelection();
   ```

3. Store the data of the selected range:

   ```
           e.clipboardData.setData('text/plain', range);
       }
   </script>
   ```

   > **Note**  
   > Before the `setData()` method is imported, the basic motion of the system event must be cancelled using the `preventDefault()` method. Otherwise, the data to be allocated to the clipboard is overwritten by the system clipboard.

### Source Code

For the complete source code related to this use case, see the following file:

- [clipboard.html](http://download.tizen.org/misc/examples/w3c_html5/ui/clipboard_api_and_events)

## Pasting Content

To paste content using the `paste` event:

1. Add an event listener to detect the `paste` event:

   ```
   <script>
       document.addEventListener('paste', function(e) {
           pasteHandler(e);
       }, false);
   ```

2. When you start pasting, the `paste` event is fired and the `pasteHandler()` method is called.

   Stop the system clipboard basic operation:

   ```
       function pasteHandler(e) {
           e.preventDefault();
   ```

3. Paste the clipboard data to the target using the `getData()` method:

   ```
           pasteTarget.innerHTML = e.clipboardData.getData('text/plain');
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [clipboard.html](http://download.tizen.org/misc/examples/w3c_html5/ui/clipboard_api_and_events)

## Copying and Pasting Content into an Editable Element

To copy and paste content in an editable HTML element:

1. Define the editable element into which copied data is to be pasted:

   ```
   <head>
      <style>
         .log {border: 1px solid #d9d9d9; margin: 10px; padding: 5px;}
         .target {border: 1px solid #36c; margin: 10px; padding: 5px;}
      </style>
   </head>
   <body>
      <h1>Clipboard API</h1>
      <div style="width: 300px; height: 100px; border: 1px solid #d9d9d9" contenteditable >
         Edit Section
      </div>
      <div  class="target">
         <h4>Target Element</h4>
         <p id="target contenteditable">Paste content</p>
      </div>
      <div id="ev-log" class="log">Event log</div>
      <div contenteditable>
         This section is informative
         This specification defines the common clipboard operations of cutting,
         copying and pasting, in such a way that they are exposed to Web Applications
         and can be adapted to provide advanced functionalities.
         Its goal is to provide for compatibility where possible with existing implementations.
      </div>
   <body>
   ```

2. Add event listeners to detect the `copy` and `paste` events:

   ```
   <script>
       var pasteTarget = document.getElementById('target');
       var evLogBox = document.getElementById('ev-log');

       document.addEventListener('copy', function(e) {
           copyHandler(e);
       }, false);

       document.addEventListener('paste', function(e) {
           pasteHandler(e);
        }, false);
   ```

3. When the `copy` event occurs, stop the system clipboard basic operation and set the range you want to copy:

   ```
       function copyHandler(e) {
           e.preventDefault();

           var range = window.getSelection();
   ```

4. Store the data of the selected range:

   ```
           e.clipboardData.setData('text/plain', range);
           evLogBox.innerHTML = 'Event log: copy';
       }
   ```

5. When the `paste` event occurs, stop the system clipboard basic operation and paste the clipboard data to the target using the `getData()` method:

   ```
       function pasteHandler(e) {
           e.preventDefault();

           pasteTarget.innerHTML = e.clipboardData.getData('text/plain');
           evLogBox.innerHTML = 'Event log: paste';
       }
   </script>
   ```

**Figure: Copying and pasting**

![Copying and pasting](./media/copy_pasting.png)

### Source Code

For the complete source code related to this use case, see the following file:

- [clipboard.html](http://download.tizen.org/misc/examples/w3c_html5/ui/clipboard_api_and_events)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
