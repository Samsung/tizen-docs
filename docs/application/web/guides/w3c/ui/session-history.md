# HTML5 Session History

You can manage the session history of browsing contexts. The `history` interface (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#the-history-interface), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#the-history-interface), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#the-history-interface) applications) is used to save in the session history the page information that has been read by the user. You can also use the `state` object (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#state-object), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#state-object), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#state-object) applications) to directly store the page information which has already been analyzed in the URL, or general information which is not stored in the URL (such as location, or the scroll state of the page or a certain DOM element).

The main features of the HTML5 session history of browsing contexts API include:

- Adding entries to the session history

  You can use the `pushState()` method of the `history` interface to [add an entry to the session history](#managing-session-history-entries). With the `replaceState()` method, you can update the session history details.

- Detecting session history status changes

  The `popstate` event (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#event-popstate), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#event-popstate), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#event-popstate) applications) is fired when the user navigates to a page stored in the session history. The `popstate` event references the information stored with the `pushState()` or `replaceState()` methods, and enables you to [change the status of the page based on the stored session history](#detecting-session-history-changes) (such as moving focus to a certain DOM element).

## Managing Session History Entries

Learning how to manage the session history enhances the user browsing experience in your application:

1. To add an entry to the session history, use the `pushState()` method of the `history` interface (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#the-history-interface), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#the-history-interface), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#the-history-interface) applications):

   ```
   <script>
       history.pushState({index: currentIndex}, document.title);
   </script>
   ```

   > **Note**  
   > The `pushState()` method accepts the `data`, `title`, and `url` (optional) parameters. The `title` parameter refers to the key value used to search for entries saved in the session history, and is currently ignored in all browsers.

2. To update the entry details, use the `replaceState()` method:

   ```
   <script>
       history.replaceState({index: currentIndex}, document.title, '#page' + currentIndex);
   </script>
   ```

   The `replaceState()` method uses the same parameters as the `pushState()` method. The `history_sample.html` is the `url` parameter, which refers to the address of the page that is to be changed.

3. To use the session history information:

   1. Implement a page with the **Prev** and **Next** buttons:

      ```
      <nav class="paging">
         <a href="#">Prev</a>
         <a href="#">Next</a>
      </nav>
      <p>Current Index: <output> </output></p>

      <a href="http://tizen.org/">Tizen.org</a>
      ```

   2. When the user clicks the buttons, the current index value (representing page numbers) is changed and stored in the `state` object (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#state-object), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#state-object), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#state-object) applications) of the `history` interface:

      ```
      var currentIndex = 0;
      var prev = document.querySelector('.paging > a:nth-child(1)');
      var next = document.querySelector('.paging > a:nth-child(2)');

      /* Prev button click event */
      prev.onclick = function() {
          currentIndex -= 1;
          setState(currentIndex);

          return false;
      };

      /* Next button click event */
      next.onclick = function() {
          currentIndex += 1;
          setState(currentIndex);

          return false;
      };
      ```

   3. If the `state` object has data in it, use the `replaceState()` method to change the previously stored information. Otherwise, add new info with the `pushState()` method.

      ```
      function setState(currentIndex) {
          if (history.state) {
             history.replaceState({index: currentIndex}, document.title, '#page' + currentIndex);
          } else {
             history.pushState({index: currentIndex}, document.title);
          }
          output.textContent = currentIndex;
      }
      ```

### Source Code

For the complete source code related to this use case, see the following file:

- [history_state.html](http://download.tizen.org/misc/examples/w3c_html5/communication/html5_the_session_history_of_browsing_contexts)

## Detecting Session History Changes

Learning how to track session history changes enhances the user browsing experience in your application:

1. A page with data stored in the session history fires a `popstate` event (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#event-popstate), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#event-popstate), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#event-popstate) applications) when the page is loaded (for example, because it is refreshed or moved to from the previous page).

   Register the event listener:

   ```
   window.addEventListener('popstate', foo, false);
   ```

2. Define the event handler for the event. You can use the data stored in the `state` object (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#state-object), [wearable](http://www.w3.org/TR/2014/CR-html5-20140429/browsers.html#state-object), and [TV](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#state-object) applications) to retrieve the correct location on the page to be loaded.

   ```
   var output = document.querySelector('output');

   window.onpopstate = function() {
       currentIndex = history.state.index;
       output.textContent = currentIndex;
   };
   ```

   In the snippet above, when a `popstate` event is fired, it saves the index value stored in the `state` object to the `currentIndex` variable, and outputs the `<output>` element from the correct index location.

### Source Code

For the complete source code related to this use case, see the following file:

- [history_state.html](http://download.tizen.org/misc/examples/w3c_html5/communication/html5_the_session_history_of_browsing_contexts)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
