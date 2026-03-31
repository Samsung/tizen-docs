### [Tizen.UI.Markdown](Tizen.UI.Markdown.md 'Tizen.UI.Markdown')

## MarkdownView Class

Represents a view component for rendering Markdown content.

```csharp
public class MarkdownView : VStack, IDisposable, IViewSignalHandler, IList<View>, ICollection<View>, IEnumerable<View>, IEnumerable, IParentObject, IStackLayout, ILayout
```

### Constructors

<a name='Tizen.UI.Markdown.MarkdownView..ctor'></a>

## MarkdownView()

Initializes a new instance of the MarkdownView class with default style.

```csharp
public MarkdownView()
```
<a name='Tizen.UI.Markdown.MarkdownView..ctor.Tizen.UI.Markdown.MarkdownStyle.'></a>

## MarkdownView(MarkdownStyle)

Initializes a new instance of the MarkdownView class with the specified style.

```csharp
public MarkdownView(MarkdownStyle style)
```
#### Parameters

`style` MarkdownStyle

The Markdown style to apply.

### Properties

<a name='Tizen.UI.Markdown.MarkdownView.Style'></a>

## Style

Gets the Markdown style applied to this view.

```csharp
public MarkdownStyle Style { get; }
```
#### Property Value

MarkdownStyle

<a name='Tizen.UI.Markdown.MarkdownView.Text'></a>

## Text

Gets or sets the Markdown text to render.
When set, the view is automatically re-rendered.

```csharp
public string Text { get; set; }
```
#### Property Value

string

### Methods

<a name='Tizen.UI.Markdown.MarkdownView.Render'></a>

## Render()

Renders the Markdown content.
This method parses the Markdown text and builds the corresponding UI elements.

```csharp
public void Render()
```
