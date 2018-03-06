# Scroll

The body area supports the following types of scrolling and functionality:

-   [Scroll bar](#scroll_bar)
-   [Screen handler](#screen_handler)
-   [Fast scroll](#fast_scroll)

<a name="scroll_bar"></a>
## Scroll Bar

Scrolling body content up and down displays the basic scroll bar, which offers visual information, such as the total length and location of a list.

However, the basic scroll bar disappears after a certain amount of time, and the users cannot adjust it by touch.

**Figure: Scroll bar**

<img alt="" height="400" src="media/tizen-lite-ux-design-guide_designlibrary_v1.1_140922_core_11.png" width="240" />

<a name="screen_handler"></a>
## Screen Handler
You can apply additional handlers if your application requires faster scrolling.

However, use screen handlers only when the scrolling range is relatively long or if there is not enough space for users to tap on the object to scroll up and down.

**Figure: Screen handler**

<img alt="" height="400" src="media/tizen-lite-ux-design-guide_designlibrary_v1.1_140922_core_12.png" width="240" />

<a name="fast_scroll"></a>
## Fast Scroll

The fast scroll feature allows users to scroll rapidly up and down any list that includes an index.

Normally, the index is in alphabetical order, but it can also be based on fields, such as local language characters, numbers, and symbols.

**Table: Index order hierarchy**

| PRIMARY LANGUAGE                 | INDEX ORDER                      |
|----------------------------------|----------------------------------|
| Latin (including English) | 1.  Local language <br>  2.  Symbols<br>  3.  Numbers    |
| Non-Latin                 | 1.  Local language <br> 2.  English<br> 3. Symbols <br> 4.  Numbers |

**Video: Interaction with fast scroll (click to play)**

<video controls height="400">
  <source src="media/designlibrary_01.mp4" type=video/mp4>
</video>
