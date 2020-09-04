# Current Xamarin.Forms Limitations

<style>
body a.squared-button {
  margin: 5px 20px 5px 0;
  display: block;
  font-size: 1.2em;
  line-height: 1.2em;
  text-transform: uppercase;
  text-align: center;
  background: #623580 url(media/white_right.png);
  background-repeat: no-repeat;
  background-position: right 10px bottom 13px;
  padding: 12px 35px 8px 12px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  -moz-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  color: white !important;
  text-shadow: 1px 1px 1px #666;
  float: left;
  width: 14rem;
  cursor: pointer;
}
body a.squared-button:hover {
  background-color: #7c8890;
  text-decoration: none;
}
body a.squared-button-reverse {
  margin: 5px 20px 5px 0;
  display: block;
  font-size: 1.2em;
  line-height: 1.2em;
  text-transform: uppercase;
  text-align: center;
  background: #7c8890 url(media/white_right.png);
  background-repeat: no-repeat;
  background-position: right 10px bottom 13px;
  padding: 12px 35px 8px 12px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  -moz-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  color: white !important;
  text-shadow: 1px 1px 1px #666;
  float: left;
  width: 14rem;
  cursor: pointer;
}
body a.squared-button-reverse:hover {
  background-color: #623580;
  text-decoration: none;
}

.tabcontent {
  display: none;
  clear: both;
}
.tdclass {
  vertical-align: top;
}
.tdtype {
  vertical-align: top;
}

body th, td {
  padding: 1px;
}
</style>

<script>
function openCity(evt, profile) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("squared-button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className += "-reverse";
    }
    document.getElementById(profile).style.display = "block";
    evt.currentTarget.className = "squared-button";
}
</script>

The following table lists the classes that are supported with minor limitations. With continuous development, Tizen .NET's support for the Xamarin.Forms APIs will increase.

<a class="squared-button" onclick="return openCity(event, 'Mobile')">Mobile</a><a class="squared-button-reverse" onclick="return openCity(event, 'TV')">TV</a><a class="squared-button-reverse" onclick="return openCity(event, 'Wearable')">Wearable</a>

<div id="Mobile" class="tabcontent" style="display: block">
<table>
    <thead>
        <tr>
            <th>
                Class
            </th>
            <th>
                Type
            </th>
            <th>
                Name
            </th>
            <th>
                Remarks
            </th>
            <th colspan="1">
                Result when the feature is used
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="tdclass" rowspan="7">
                <code class="prettyprint">BoxView</code>
            </td>
            <td class="tdtype" rowspan="5"> Property
            </td>
            <td>
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                <code class="prettyprint">BackgroundColor</code> is ignored, use <code class="prettyprint">Color</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsEnabled</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                <code class="prettyprint">BoxView</code> is not interactive, and enabling does not change that.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsFocused</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Always <code class="prettyprint">false</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Focus</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Unfocus</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Event
            </td>
            <td>
                <code class="prettyprint">Focused</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Never triggered.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Unfocused</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Never triggered.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="4">
                <code class="prettyprint">Button</code>
            </td>
            <td class="tdtype" rowspan="4">
                Property
            </td>
            <td>
                <code class="prettyprint">BorderColor</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">BorderRadius</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">BorderWidth</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">ContentLayout</code></td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">CarouselPage</code>
            </td>
            <td colspan="1">Class
            </td>
            <td colspan="1"><code class="prettyprint">CarouselPage</code>
            </td>
            <td colspan="1">Obsolete in Xamarin.Forms.</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <code class="prettyprint">Device</code>
            </td>
            <td class="tdtype" rowspan="2">
                Method
            </td>
            <td>
                <code class="prettyprint">OnPlatform&lt;T&gt;(T,T,T)</code>
            </td>
            <td>
                Use <code class="prettyprint">OnPlatform&lt;T&gt; (T,T,T,T)</code> instead.
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">OnPlatform(Action, Action, Action, Action)</code>
            </td>
            <td>
                Use <code class="prettyprint">OnPlatform(Action, Action, Action, Action, Action)</code> instead.
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">EntryCell</code>
            </td>
            <td colspan="1">Property
            </td>
            <td colspan="1"><code class="prettyprint">Height</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Frame</code>
            </td>
            <td colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint">CornerRadius</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">ImageSource</code>
            </td>
            <td colspan="1">Method</td>
            <td colspan="1"><code class="prettyprint">FromResource(string resource, Assembly sourceAssembly = null)</code>
            </td>
            <td colspan="1">sourceAssembly should be specified.</td>
            <td colspan="1">
                System.TypeInitializationException will be thrown when sourceAssembly is not to set.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Layout</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">IsClippedToBounds</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="10">
                <code class="prettyprint">ListView</code>
            </td>
            <td class="tdtype" rowspan="7">
                Property
            </td>
            <td>
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td></td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsPullToRefreshEnabled</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Property is always set to <code class="prettyprint">false</code>. Attempts to change it to <code class="prettyprint">true</code> are ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsRefreshing</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Always <code class="prettyprint">false</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">SeparatorColor</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Separator is not visible, so the color has no effect.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">SeparatorVisibility</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">RowHeight</code>
            </td>
            <td colspan="1">
                This is applied when <code class="prettyprint">HasUnevenRows</code> is set to <code class="prettyprint">true</code>.
                However, <code class="prettyprint">RowHeight</code> value may not be affected to Cells due to the policy of Tizen platform.
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">RefreshCommand</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Method
            </td>
            <td>
                <code class="prettyprint">BeginRefresh()</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">EndRefresh()</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                Event
            </td>
            <td>
                <code class="prettyprint">Refreshing</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                As <code class="prettyprint">IsPullToRefreshEnabled</code> is not supported, this event is never triggered.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <code class="prettyprint">MasterDetailPage</code>
            </td>
            <td>
                Method
            </td>
            <td>
                <code class="prettyprint">ShouldShowToolbarButton()</code>
            </td>
            <td></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Property
            </td>
            <td>
                <code class="prettyprint">IsGestureEnabled</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">ToolbarItems</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Only <code class="prettyprint">ToolbarItems</code> for the <code class="prettyprint">MasterDetailPage</code> are shown.
                <code class="prettyprint">ToolbarItems</code> for the <code class="prettyprint">Master</code> and <code class="prettyprint">Detail</code> pages are not shown.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="4">
                <code class="prettyprint">NavigationPage</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">Tint</code>
            </td>
            <td>
                Obsolete in Xamarin.Forms.
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="3" colspan="1">Method
            </td>
            <td colspan="1"><code class="prettyprint">SetTitleIcon()</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">GetTitleIcon()</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">SetHasBackButtonTitle()</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <code class="prettyprint">Page</code>
            </td>
            <td class="tdtype" rowspan="3">
                Property
            </td>
            <td>
                <code class="prettyprint">Icon</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">IsBusy</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">ToolbarItems</code>
            </td>
            <td>
                Only one <code class="prettyprint">ToolbarItem</code> is supported for each Order.
                    <code class="prettyprint">Primary</code> and <code class="prettyprint">Default</code> indicate the 'right' action button on the title bar.
                    <code class="prettyprint">Secondary</code> indicates the 'left' action button on the title bar.
                    Therefore, if <code class="prettyprint">Secondary</code> is used, no back button is shown.
            </td>
            <td colspan="1">
                The priority of the 'left' action button is first <code class="prettyprint">Secondary</code> and then the back button.<br>
                For example, if a toolbar item is assigned to <code class="prettyprint">Secondary</code>, the left action button is the <code class="prettyprint">Secondary</code> toolbar item.
                Only one toolbar item is supported for each order. If multiple toolbar items are specified, the first toolbar item is used.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Slider</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">Rotation</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <code class="prettyprint">SwitchCell</code>
            </td>
            <td class="tdtype" rowspan="2">
                Property
            </td>
            <td>
                <code class="prettyprint">Height</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint">Intent</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">TabbedPage</code>
            </td>
            <td>Property</td>
            <td colspan="1">
                <code class="prettyprint">BarTextColor</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1">
                <code class="prettyprint">TableView</code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1">Property</td>
            <td colspan="1">
                <code class="prettyprint">RowHeight</code>
            </td>
            <td colspan="1">
                This is applied when <code class="prettyprint">HasUnevenRows</code> is set to <code class="prettyprint">true</code>.<br>
                However, <code class="prettyprint">RowHeight</code> value may not be affected to Cells due to the policy of Tizen platform.
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">TextCell</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">Height</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">ViewCell</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">View</code>
            </td>
            <td>
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1">
                <code class="prettyprint">WebView</code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1">
                Property
            </td>
            <td colspan="1">
                <code class="prettyprint">Opacity</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
    </tbody>
</table>
</div>

<div id="TV" class="tabcontent" style="display: none">
<table>
    <thead>
        <tr>
            <th>
                Class
            </th>
            <th>
                Type
            </th>
            <th>
                Name
            </th>
            <th>
                Remarks
            </th>
            <th colspan="1">
                Result when the feature is used
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="tdclass" rowspan="7">
                <code class="prettyprint">BoxView</code>
            </td>
            <td class="tdtype" rowspan="5">
                Property
            </td>
            <td>
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td>
            </td><td>
                <code class="prettyprint">BackgroundColor</code> is ignored, use <code class="prettyprint">Color</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsEnabled</code>
            </td>
            <td>
            </td><td>
                <code class="prettyprint">BoxView</code> is not interactive, and enabling does not change that.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsFocused</code>
            </td>
            <td>
            </td><td>
                Always <code class="prettyprint">false</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Focus</code>
            </td>
            <td>
            </td><td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Unfocus</code>
            </td>
            <td>
            </td><td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Event
            </td>
            <td>
                <code class="prettyprint">Focused</code>
            </td>
            <td>
            </td><td>
                Never triggered.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Unfocused</code>
            </td>
            <td>
            </td><td>
                Never triggered.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="4">
                <code class="prettyprint">Button</code>
            </td>
            <td class="tdtype" rowspan="4">
                Property
            </td>
            <td>
                <code class="prettyprint">BorderColor</code>
            </td>
            <td>
            </td><td>
                Ignored.
            </td>
        </tr>
        <tr><td>
                <code class="prettyprint">BorderRadius</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">BorderWidth</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">ContentLayout</code></td>
            <td>
            </td><td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">CarouselPage</code></td>
            <td>Class</td>
            <td><code class="prettyprint">CarouselPage</code></td>
            <td>Obsolete in Xamarin.Forms.</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <code class="prettyprint">Device</code>
            </td>
            <td class="tdtype" rowspan="2">
                Method
            </td>
            <td>
                <code class="prettyprint">OnPlatform&lt;T&gt;(T,T,T)</code>
            </td>
            <td>
                Use <code class="prettyprint">OnPlatform&lt;T&gt; (T,T,T,T)</code> instead.
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">OnPlatform(Action, Action, Action, Action)</code>
            </td>
            <td>
                Use <code class="prettyprint">OnPlatform(Action, Action, Action, Action, Action)</code> instead.
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3"><code class="prettyprint">EntryCell</code></td>
            <td>Class</td>
            <td><code class="prettyprint">EntryCell</code></td>
            <td>Mouse pointer is required for enabling user interaction on entry of the cell.</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">Property</td>
            <td><code class="prettyprint">Height</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">Keyboard</code></td>
            <td>&nbsp;</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">Frame</code></td>
            <td>Property</td>
            <td><code class="prettyprint">CornerRadius</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">ImageSource</code></td>
            <td>Method</td>
            <td><code class="prettyprint">FromResource(string resource, Assembly sourceAssembly = null)</code></td>
            <td>sourceAssembly should be specified.</td>
            <td>
                System.TypeInitializationException will be thrown when sourceAssembly is not to set.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Layout</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">IsClippedToBounds</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="10">
                <code class="prettyprint">ListView</code>
            </td>
            <td class="tdtype" rowspan="7">
                Property
            </td>
            <td>
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td>&nbsp;</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsPullToRefreshEnabled</code>
            </td>
            <td>
            </td>
            <td>
                Property is always set to <code class="prettyprint">false</code>. Attempts to change it to <code class="prettyprint">true</code> are ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsRefreshing</code>
            </td>
            <td>
            </td>
            <td>
                Always <code class="prettyprint">false</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">SeparatorColor</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">SeparatorVisibility</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">RowHeight</code></td>
            <td>
                This is applied when <code class="prettyprint">HasUnevenRows</code> is set to <code class="prettyprint">true</code>.
                However, <code class="prettyprint">RowHeight</code> value may not be affected to Cells due to the policy of Tizen platform.
            </td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">RefreshCommand</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Method
            </td>
            <td>
                <code class="prettyprint">BeginRefresh()</code>
            </td>
            <td>
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">EndRefresh()</code>
            </td>
            <td>
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td>
                Event
            </td>
            <td>
                <code class="prettyprint">Refreshing</code>
            </td>
            <td>
            </td>
            <td>
                As <code class="prettyprint">IsPullToRefreshEnabled</code> is not supported, this event is never triggered.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <code class="prettyprint">MasterDetailPage</code>
            </td>
            <td>
                Method
            </td>
            <td>
                <code class="prettyprint">ShouldShowToolbarButton()</code>
            </td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Property
            </td>
            <td>
                <code class="prettyprint">IsGestureEnabled</code>
            </td>
            <td>
            </td>
            <td>
                <div>Does not always work as expected.</div>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">ToolbarItems</code></td>
            <td>&nbsp;</td>
            <td>
                Only <code class="prettyprint">ToolbarItems</code> for the <code class="prettyprint">MasterDetailPage</code> are shown.
                <code class="prettyprint">ToolbarItems</code> for the <code class="prettyprint">Master</code> and <code class="prettyprint">Detail</code> pages are not shown.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="5">
                <code class="prettyprint">NavigationPage</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">Tint</code>
            </td>
            <td>
                Obsolete in Xamarin.Forms.
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="4">Method</td>
            <td><code class="prettyprint">SetTitleIcon()</code></td>
            <td>&nbsp;</td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">GetTitleIcon()</code>
            </td>
            <td>
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">SetHasBackButton()</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">SetHasBackButtonTitle()</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">PinchGestureRecognizer</code></td>
            <td>Event</td>
            <td><code class="prettyprint">PinchUpdated</code></td>
            <td>&nbsp;</td>
            <td>
                Never occured.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <code class="prettyprint">Page</code>
            </td>
            <td class="tdtype" rowspan="3">
                Property
            </td>
            <td>
                <code class="prettyprint">Icon</code>
            </td>
            <td>
            </td>
            <td>
                No action.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">IsBusy</code></td>
            <td>&nbsp;</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">ToolbarItems</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">SearchBar</code></td>
            <td>Class</td>
            <td><code class="prettyprint">SearchBar</code></td>
            <td>&nbsp;</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Slider</code>
            </td>
            <td>Property</td>
            <td><code class="prettyprint">BackgroundColor</code></td>
            <td>&nbsp;</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2"><code class="prettyprint">Stepper</code></td>
            <td>
                Class
            </td>
            <td><code class="prettyprint">Stepper</code></td>
            <td>&nbsp;</td>
            <td>
                Does not always shown as expected.
            </td>
        </tr>
        <tr>
            <td>Property</td>
            <td><code class="prettyprint">BackgroundColor</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3"><code class="prettyprint">SwitchCell</code></td>
            <td>Class</td>
            <td><code class="prettyprint">SwitchCell</code></td>
            <td>Mouse pointer is required for enabling user interaction on switch of the cell.</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Property
            </td>
            <td>
                <code class="prettyprint">Height</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">Intent</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">TabbedPage</code></td>
            <td>Property</td>
            <td><code class="prettyprint">BarTextColor</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2"><code class="prettyprint">TableView</code></td>
            <td class="tdtype" rowspan="2">Property</td>
            <td><code class="prettyprint">RowHeight</code></td>
            <td>
                This is applied when <code class="prettyprint">HasUnevenRows</code> is set to <code class="prettyprint">true</code>.
                However, <code class="prettyprint">RowHeight</code> value may not be affected to Cells due to the policy of Tizen platform.
            </td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">BackgroundColor</code></td>
            <td>&nbsp;</td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <code class="prettyprint">TextCell</code>
            </td>
            <td class="tdtype" rowspan="2">
                Property
            </td>
            <td>
                <code class="prettyprint">Height</code>
            </td>
            <td>
            </td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint">Detail</code></td>
            <td>&nbsp;</td>
            <td>
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">ViewCell</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">View</code>
            </td>
            <td>
            </td>
            <td>
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass"><code class="prettyprint">WebView</code></td>
            <td class="tdtype">Class</td>
            <td><code class="prettyprint">WebView</code></td>
            <td>&nbsp;</td>
            <td>
                Application will fail to launch.
            </td>
        </tr>
    </tbody>
</table>
</div>

<div id="Wearable" class="tabcontent" style="display: none">
<table>
    <thead>
        <tr>
            <th>
                Class
            </th>
            <th>
                Type
            </th>
            <th>
                Name
            </th>
            <th>
                Remarks
            </th>
            <th colspan="1">
                Result when the feature is used
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="tdclass" rowspan="6" colspan="1"><code class="prettyprint">ActivityIndicator</code>
            </td>
            <td class="tdtype" rowspan="6" colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint">Opacity</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">HeightRequest</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">WidthRequest</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">IsEnabled</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">IsRunning</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="7">
                <code class="prettyprint">BoxView</code>
            </td>
            <td class="tdtype" rowspan="5">
                Property
            </td>
            <td>
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                <code class="prettyprint">BackgroundColor</code>&nbsp;is ignored, use&nbsp;<code class="prettyprint">Color</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsEnabled</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                <code class="prettyprint">BoxView</code>&nbsp;is not interactive, and enabling does not change that.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsFocused</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Always&nbsp;<code class="prettyprint">false</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Focus</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Unfocus</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Event
            </td>
            <td>
                <code class="prettyprint">Focused</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Never triggered.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Unfocused</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Never triggered.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="5">
                <code class="prettyprint">Button</code>
            </td>
            <td class="tdtype" rowspan="5">
                Property
            </td>
            <td>
                <code class="prettyprint">BorderColor</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                <div>Ignored.
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">BorderRadius</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                <div>Ignored.
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">BorderWidth</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">ContentLayout</code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Opacity</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">CarouselPage</code>
            </td>
            <td colspan="1">Class
            </td>
            <td colspan="1"><code class="prettyprint">CarouselPage</code>
            </td>
            <td colspan="1">Obsolete in Xamarin.Forms.
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <code class="prettyprint">Device</code>
            </td>
            <td class="tdtype" rowspan="2">
                Method
            </td>
            <td>
                <code class="prettyprint">OnPlatform&lt;T&gt;(T,T,T)</code>
            </td>
            <td>
                &nbsp;Use <code class="prettyprint">OnPlatform&lt;T&gt; (T,T,T,T)</code> instead.
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">OnPlatform(Action, Action, Action, Action)</code>
            </td>
            <td>
                &nbsp;Use <code class="prettyprint">OnPlatform(Action, Action, Action, Action, Action)</code> instead.
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">DatePicker</code>
            </td>
            <td colspan="1">Class
            </td>
            <td colspan="1"><code class="prettyprint">DatePicker</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Not Supported.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Editor</code>
            </td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint">Editor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Entry</code>
            </td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint">Entry</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1"><code class="prettyprint">EntryCell</code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1">Property
            </td>
            <td colspan="1"><code class="prettyprint">Height</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Keyboard</code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Frame</code>
            </td>
            <td colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint">CornerRadius</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Image</code>
            </td>
            <td colspan="1">Property
            </td>
            <td colspan="1"><code class="prettyprint">IsOpaque</code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">ImageSource</code>
            </td>
            <td colspan="1">Method
            </td>
            <td colspan="1"><code class="prettyprint">FromResource(string resource, Assembly sourceAssembly = null)</code>
            </td>
            <td colspan="1">sourceAssembly should be specified.
            </td>
            <td colspan="1">
                System.TypeInitializationException will be thrown when sourceAssembly is not to set.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">Layout</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">IsClippedToBounds</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="10">
                <code class="prettyprint">ListView</code>
            </td>
            <td class="tdtype" rowspan="7">
                Property&nbsp;
            </td>
            <td>
                <code class="prettyprint">BackgroundColor</code>
            </td>
            <td>&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsPullToRefreshEnabled</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Property is always set to&nbsp;<code class="prettyprint">false</code>. Attempts to change it to&nbsp;<code class="prettyprint">true</code>&nbsp;are ignored.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">IsRefreshing</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Always&nbsp;<code class="prettyprint">false</code>.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">SeparatorColor</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Separator is not visible, so the color has no effect.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">SeparatorVisibility</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">RowHeight</code>
            </td>
            <td colspan="1">
                This is applied when <code class="prettyprint">HasUnevenRows</code> is set to <code class="prettyprint">true</code>.
                However, <code class="prettyprint">RowHeight</code> value may not be affected to Cells due to the policy of Tizen platform.
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">RefreshCommand</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                Method
            </td>
            <td>
                <code class="prettyprint">BeginRefresh()</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">EndRefresh()</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                Event
            </td>
            <td>
                <code class="prettyprint">Refreshing</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                As&nbsp;<code class="prettyprint">IsPullToRefreshEnabled</code>&nbsp;is not supported, this event is never triggered.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">MasterDetailPage</code>
            </td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint">MasterDetailPage</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Not Supported.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="5">
                <code class="prettyprint">NavigationPage</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">Tint</code>
            </td>
            <td>
                Obsolete in Xamarin.Forms.
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="4" colspan="1">Method
            </td>
            <td colspan="1"><code class="prettyprint">SetTitleIcon()</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">GetTitleIcon()</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">SetHasBackButton()</code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.&nbsp;
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">SetHasBackButtonTitle()</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.&nbsp;
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <code class="prettyprint">Page</code>
            </td>
            <td class="tdtype" rowspan="3">
                Property
            </td>
            <td>
                <code class="prettyprint">Icon</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                No action.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">IsBusy</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">ToolbarItems</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Picker</code>
            </td>
            <td colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint">Opacity</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">SearchBar</code></td>
            <td colspan="1">Class
            </td>
            <td colspan="1"><code class="prettyprint">SearchBar</code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint">Slider</code>
            </td>
            <td colspan="1">
                Property
            </td><td colspan="1"><code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Stepper</code></td>
            <td colspan="1">Property&nbsp;
            </td>
            <td colspan="1"><code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <code class="prettyprint">SwitchCell</code>
            </td>
            <td class="tdtype" rowspan="2">
                Property
            </td>
            <td>
                <code class="prettyprint">Height</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Intent</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1"><code class="prettyprint">TabbedPage</code></td>
            <td class="tdtype" rowspan="2" colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint">TabbedPage</code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Not Supported.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">BarTextColor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3" colspan="1"><code class="prettyprint">TableView</code></td>
            <td class="tdtype" rowspan="3" colspan="1">Property
            </td>
            <td colspan="1"><code class="prettyprint">RowHeight</code></td>
            <td colspan="1">
                This is applied when <code class="prettyprint">HasUnevenRows</code> is set to <code class="prettyprint">true</code>.
                However, <code class="prettyprint">RowHeight</code> value may not be affected to Cells due to the policy of Tizen platform.
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">IsEnabled</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <code class="prettyprint">TextCell</code>
            </td>
            <td class="tdtype" rowspan="3">
                Property
            </td>
            <td>
                <code class="prettyprint">Height</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                <div>Ignored.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">Detail</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">IsEnabled</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">TimePicker</code></td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint">TimePicker</code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Not Supported.
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint">ViewCell</code>
            </td>
            <td>
                Property
            </td>
            <td>
                <code class="prettyprint">View</code>
            </td>
            <td>
                &nbsp;
            </td>
            <td colspan="1">
                Does not always work as expected.
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1"><code class="prettyprint">WebView</code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1">Property
            </td>
            <td colspan="1"><code class="prettyprint">Opacity</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint">BackgroundColor</code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                Ignored.
            </td>
        </tr>
    </tbody>
</table>
</div>
