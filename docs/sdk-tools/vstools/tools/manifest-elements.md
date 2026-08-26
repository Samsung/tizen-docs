# Using Additional Manifest Elements

The following sections summarize some of the common child elements used in the `tizen-manifest.xml` file of a Tizen .NET application.

<a name="appcontrol"></a>
## &lt;app-control&gt; Element

This element represents Tizen application control configuration information.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Expected children:**

| Child element | Occurrences |
|---------------|----------------------|
| `<operation>` | 1 or more (optional) |
| `<uri>`   | 1 or more (optional) |
| `<mime>`  | 1 or more (optional) |

**For example:**

```
<app-control>
   <operation name="http://tizen.org/appcontrol/operation/compose"/>
   <uri name="testuristring"/>
   <mime name="application/pdf"/>
</app-control>
```

<a name="operation"></a>
### &lt;operation&gt; Element

This element represents the operation type of the application control.

**Attributes:**

- `name`

   Name of the application control, for example, `http://tizen.org/appcontrol/operation/compose`

**For example:**

```
<operation name="http://tizen.org/appcontrol/operation/compose"/>
```
<a name="uri"></a>
### &lt;uri&gt; Element

This element represents the URI scheme of the application control.

**Attributes:**

- `name`

   Name of the URI scheme (string)

**For example:**

```
<uri name="testuristring"/>
```

<a name="mime"></a>
### &lt;mime&gt; Element

This element represents the MIME type of the application control.

**Attributes:**

- `name`

  Name of the MIME type (string)

**For example:**

```
<mime name="application/pdf"/>
```

<a name="bg-category"></a>
## &lt;background-category&gt; Element

This element represents the category of an application that runs in the background.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Attributes:**

- `value`

  Value of the background category (string)

**For example:**

```
<background-category value="download"/>
```
<a name="datacontrol"></a>
## &lt;datacontrol&gt; Element

This element represents configuration information for the Tizen data controls.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Expected children:**

| Child element | Occurrences |
|---------------|-------------|
| `<privilege>` | 1 or more (optional) |

**Attributes:**

- `access`

  Access mode of the data control (string)

- `providerid`

  ID of the data control provider (string)

- `type`

  Type of the data control (string)

**For example:**

```
<datacontrol access="WriteOnly" providerid="http://uiapp.com/datacontrol/provider/uiapp" type="Sql">
   <privilege>.....</privilege>
</datacontrol>
```

<a name="icon"></a>
## &lt;icon&gt; Element

This element represents the icon relative or absolute file path for the Tizen application.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 (optional)

**Expected value:**

- Icon path

**For example:**

```
<icon>testicon.png</icon>
```
<a name="label"></a>
## &lt;label&gt; Element

This element represents the label value for the Tizen application. It is a set of human readable names for the Tizen application according to the language.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Attributes:**

- `xml:lang`

  Language of the label (available value: "&lt;2-letter lowercase language code (ISO 639-1)&gt;-&lt;2-letter lowercase country code (ISO 3166-1 alpha-2)&gt;")

**Expected value:**

- Label value in string

**For example:**

```
<label>testlabel</label>
<label xml:lang="en-gb">testlabel</label>
```
<a name="metadata"></a>
## &lt;metadata&gt; Element

This element represents user-defined key-value pairs for the application.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Attributes:**

- `key`

  Key of metadata (string)

- `value`

  Value of metadata (string)

**For example:**

```
<metadata key="testkey" value="testvalue"/>
```

<a name="splash-screens"></a>
## &lt;splash-screens&gt; Element 
This element represents Tizen splash-screen configuration information.

For more information on the relationship between the elements, see the [element hierarchy](manifest-editor.md#hierarchy).

**Occurrences:**

- 1 or more (optional)

**Expected children:**

| Child element     | Occurrences |
|-------------------|-------------|
| `<splash-screen>` | 1 or more |

**For example:**

```
<splash-screens>
   <splash-screen src="test1.jpg" type="img" dpi="hdpi" orientation="portrait" indicator-display="true"\>
   <splash-screen src="test2.edj" type="edj" dpi="hdpi" orientation="landscape" indicator-display="false"\>
</splash-screens>
```

<a name="splash-screen"></a>
### &lt;splash-screen&gt; Element

This element represents a splash-screen of the application. The splash-screen is an image that covers the entire screen. It is displayed when the application is launched, and disappears after the application main screen is loaded.

**Attributes:**

- `src`

  Source of the splash-screen (string)

- `type`

  Type of the splash-screen (available values: `img`, `edj`)

- `dpi`

  Resolution of the splash-screen (available values: `ldpi`, `mdpi`, `hdpi`, `xhdpi`, `xxhdpi`)

- `orientation`

  Orientation of the splash-screen (available values: `portrait`, `landscape`)

- `indicator-display`

  Indicates whether the indicator area is visible on the splash-screen (available values: `true`, `false`)

- `app-control-operation`

  Application control operation of the splash-screen (string)

  If this value is defined, the splash-screen image is shown when the application is launched by the application control operation.

**For example:**

```
<splash-screen src="test1.jpg" type="img" dpi="hdpi" orientation="portrait" indicator-display="true"
         app-control-operation="http://tizen.org/appcontrol/operation/default"\>
```
