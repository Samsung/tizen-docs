# Markdown Template

All basic and GitHub Flavored Markdown (GFM) is supported. For more information on these, see:

- [Baseline Markdown syntax](https://daringfireball.net/projects/markdown/syntax)
- [GFM documentation](https://guides.github.com/features/mastering-markdown)

Markdown uses special characters such as \*, \`, and \# for formatting. If you wish to include one of these characters in your content, you must do one of two things:

- Put a backslash before the special character to "escape" it (for example, `\*` for a \*)
- Use the [HTML entity code](http://www.ascii.cl/htmlcodes.htm) for the character (for example, `&#42;` for a &#42;).

## File name

File names use the following rules:
* Contain only lowercase letters, numbers, and hyphens.
* No spaces or punctuation characters. Use the hyphens to separate words and numbers in the file name.
* Use action verbs that are specific, such as develop, buy, build, troubleshoot. No -ing words.
* No small words - don't include a, and, the, in, or, etc.
* Must be in Markdown and use the .md file extension.
* Keep file names reasonably short. They are part of the URL for your articles.  
> **Note**   
> It doesn't apply to media file names.


## Headings

Use sentence-style capitalization. Always capitalize:
- The first word of a heading. 
- The word following a colon in a title or heading (for example, "How to: Sort an array"). 

Headings should be done using atx-style, that is, use 1-6 hash characters (#) at the start of the line to indicate a heading, corresponding to HTML headings levels H1 through H6. Examples of first- and second-level headers are used above. 

There **must** be only one first-level heading (H1) in your topic, which will be displayed as the on-page title.

If your heading finishes with a `#` character, you need to add an extra `#` character in the end in order for the title to render correctly. For example, `# Async Programming in F# #`.     

Second-level headings will generate the on-page TOC that appears in the "In this article" section underneath the on-page title.

### Third-level heading
#### Fourth-level heading
##### Fifth level heading
###### Sixth-level heading

## Text styling

**Bold**
Use for UI elements.

`Code`
Use for inline code, language keywords, package names, command-line commands, database table and column names, and URLs that you don't want to be clickable.  
Use for files, folders, paths (for long items, split onto their own line), new terms.

## Links

### Internal Links

To link to a header in the same Markdown file (also known as anchor links), you'll need to find out the id of the header you're trying to link to. To confirm the ID, view the source of the rendered article, find the id of the header (for example, `id="blockquote"`), and link using # + id (for example, `#blockquote`).
The id is auto-generated based on the header text. So, for example, given a unique section named `## Step 2`, the id would look like this `id="step-2"`.

- Example: [Chapter 1](#chapter-1)

To link to a Markdown file in the same repo, use [relative links](https://www.w3.org/TR/WD-html40-970917/htmlweb.html#h-5.1.2), including the ".md" at the end of the filename.

- Example: [Readme file](../readme.md)
- Example: [Welcome to .NET](../docs/welcome.md)

To link to a header in a Markdown file in the same repo, use relative linking + hashtag linking.

- Example: [Open Source Tizen](../docs/open-source-tizen/developing/setting-up.md)

### External Links

To link to an external file, use the full URL as the link.

- Example: [GitHub](http://www.github.com)

If a URL appears in a Markdown file, it will be transformed into a clickable link.

- Example: http://www.github.com


## Lists

### Ordered lists

1. This
2. Is
3. An
4. Ordered
5. List


#### Ordered list with an embedded list

1. Here
2. comes
3. an
4. embedded
    1. Miss Scarlett
    2. Professor Plum
5. ordered
6. list


### Unordered Lists

- This
- is
- a
- bulleted
- list


##### Unordered list with an embedded list

- This
- bulleted
- list
    - Item1
    - Item2
- contains
- other
    1. Item1
    2. Item2
- lists


## Horizontal rule

---

## Tables

| Tables           |      Are      |  Cool |
| ---------------- | :-----------: | ----: |
| col 1 is default | left-aligned  |    $1 |
| col 2 is         |   centered    |   $12 |
| col 3 is         | right-aligned | $1600 |

You can use a [Markdown table generator tool](http://www.tablesgenerator.com/markdown_tables) to help creating them more easily.

## Code

### Inline code blocks with language identifier

Use three backticks (\`\`\`) + a language ID to apply language-specific color coding to a code block. Here is the list of supported languages showing the markdown label for each language ID. 

#### Supported Languages
| Name        | Markdown Label |
| ----------- | -------------- |
| C++         | cpp            |
| C#          | csharp         |
| JavaScript  | javascript     |
| JSON        | json           |
| NodeJS      | nodejs         |
| PHP         | php            |
| Bash        | bash           |
| Python      | python         |
| Ruby        | ruby           |
| SQL / T-SQL | sql            |
| XAML        | xaml           |
| XML         | xml            |


The following are examples of code blocks using the language IDs for C# (\`\`\`csharp), Python (\`\`\`python), and Bash (\`\`\`bash).

##### C&#9839;

```csharp
using System;
namespace HelloWorld
{
    class Hello 
    {
        static void Main() 
        {
            Console.WriteLine("Hello World!");

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }
    }
}
```
#### Python

```python
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)
```
#### Bash

```bash
$ mkdir ~/bin/$ PATH=~/bin:$PATH
$ sudo vim /usr/local/bin/git-proxy
```

### Generic code block

Use three backticks (&#96;&#96;&#96;) for generic code block coding.   

> The recommended approach is to use code blocks with language identifiers as explained in the previous section to ensure the proper syntax highlighting in the documentation site. Use generic code blocks only when necessary.
```
function fancyAlert(arg) {
    if(arg) {
        $.docs({div:'#foo'})
    }
}
```

## Images

### Static Image or Animated gif

![this is the alt text](https://portal.stage.tizen.org/images/tizen-branding-pinwheel-on-light.png)

### Linked Image

[![alt text for linked image](https://portal.stage.tizen.org/images/tizen-branding-pinwheel-on-light.png)](https://www.tizen.org) 

## Videos

Currently, you can embed both YouTube videos with the following syntax:

### YouTube

To get the video's correct URL, right-click on the video, select **Copy Embed Code**, and copy the URL from the `<iframe>` element.

```markdown
[![VIDEO](<youtube_video_link>)](<youtube_video_link>)
```

For example:

```markdown
[![An Introduction to Tizen .NET](https://youtube.com/embed/NdvWwU0gKt8)](https://youtube.com/embed/NdvWwU0gKt8)
```

You can use HTML for videos.
