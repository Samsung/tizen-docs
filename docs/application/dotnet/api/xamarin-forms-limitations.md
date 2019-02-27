# Current Xamarin.Forms Limitations

<style>
.tabcontent {
    display: none;
    clear: both;
}
.squared-button {
  width: 8rem;
}
.squared-button-reverse {
  width: 8rem;
}
.tdclass {
  vertical-align: top;
}
.tdtype {
  vertical-align: top;
}
</style>


The following table lists the classes that are supported with minor limitations. With continuous development, Tizen .NET's support for the Xamarin.Forms APIs will increase.

<a class="squared-button" onclick="return openCity(event, 'Mobile')">Mobile</a><a class="squared-button-reverse" onclick="return openCity(event, 'TV')">TV</a><a class="squared-button-reverse" onclick="return openCity(event, 'Wearable')">Wearable</a>

<div id="Mobile" class="tabcontent" style="display: block">
<table>
    <tbody>
        <tr>
            <th>
                <p><strong>Class</strong>
                </p>
            </th>
            <th>
                <p><strong>Type</strong>
                </p>
            </th>
            <th>
                <p><strong>Name</strong>
                </p>
            </th>
            <th>
                <p><strong>Remarks</strong>
                </p>
            </th>
            <th colspan="1">
                <p><strong>Result when the feature is used</strong>
                </p>
            </th>
        </tr>
        <tr>
            <td class="tdclass" rowspan="7">
                <p><code class="prettyprint"><span class="typ">BoxView</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="5">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code> is ignored, use <code class="prettyprint"><span class="typ">Color</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsEnabled</span></code></p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><code class="prettyprint"><span class="typ">BoxView</span></code> is not interactive, and enabling does not change that.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsFocused</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Always <code class="prettyprint"><span class="typ">false</span></code>.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Focus</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Unfocus</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Event</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Focused</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Never triggered.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Unfocused</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Never triggered.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="4">
                <p><code class="prettyprint"><span class="typ">Button</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="4">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderColor</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderRadius</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderWidth</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">ContentLayout</span></code></td>
            <td colspan="1"></td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">CarouselPage</span></code>
            </td>
            <td colspan="1">Class
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">CarouselPage</span></code>
            </td>
            <td colspan="1">Obsolete in Xamarin.Forms.</td>
            <td colspan="1">
                <p>Does not always work as expected.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <p><code class="prettyprint"><span class="typ">Device</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="2">
                <p>Method</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">OnPlatform&lt;T&gt;(T,T,T)</span></code>
                </p>
            </td>
            <td>
                <p>Use <code class="prettyprint"><span class="typ">OnPlatform&lt;T&gt; (T,T,T,T)</span></code> instead.</p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">OnPlatform(Action, Action, Action, Action)</span></code>
                </p>
            </td>
            <td>
                <p>Use <code class="prettyprint"><span class="typ">OnPlatform(Action, Action, Action, Action, Action)</span></code> instead.</p>
            </td>
            <td colspan="1">
                <p>No action.
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">EntryCell</span></code>
            </td>
            <td colspan="1"><span>Property</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Height</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Frame</span></code>
            </td>
            <td colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">CornerRadius</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">ImageSource</span></code>
            </td>
            <td colspan="1">Method</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">FromResource(string resource, Assembly sourceAssembly = null)</span></code>
            </td>
            <td colspan="1">sourceAssembly should be specified.</td>
            <td colspan="1">
                <p>System.TypeInitializationException will be thrown when sourceAssembly is not to set.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Layout</span></code>
                </p>
            </td>
            <td>
                <p>Property
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">IsClippedToBounds</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="10">
                <p><code class="prettyprint"><span class="typ">ListView</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="7">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
                </p>
            </td>
            <td></td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsPullToRefreshEnabled</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Property is always set to <code class="prettyprint"><span class="typ">false</span></code>. Attempts to change it to <code class="prettyprint"><span class="typ">true</span></code> are ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsRefreshing</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>Always <code class="prettyprint"><span class="typ">false</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">SeparatorColor</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>Separator is not visible, so the color has no effect.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">SeparatorVisibility</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">RowHeight</span></code>
            </td>
            <td colspan="1">
                <p>This is applied when <code class="prettyprint"><span class="typ">HasUnevenRows</span></code> is set to <code class="prettyprint"><span class="typ">true</span></code>.</p>
                <p>However, <code class="prettyprint"><span class="typ">RowHeight</span></code> value may not be affected to Cells due to the policy of Tizen platform.</p>
            </td>
            <td colspan="1">
                <p>Does not always work as expected.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">RefreshCommand</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p>Method</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BeginRefresh()</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">EndRefresh()</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><span>Event</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Refreshing</span></code></p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>As <code class="prettyprint"><span class="typ">IsPullToRefreshEnabled</span></code> is not supported, this event is never triggered.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <p><code class="prettyprint"><span class="typ">MasterDetailPage</span></code>
                </p>
            </td>
            <td>
                <p>Method</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">ShouldShowToolbarButton()</span></code>
                </p>
            </td>
            <td></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">IsGestureEnabled</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">ToolbarItems</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Only <code class="prettyprint"><span class="typ">ToolbarItems</span></code> for the <code class="prettyprint"><span class="typ">MasterDetailPage</span></code> are shown.</p>
                <p><code class="prettyprint"><span class="typ">ToolbarItems</span></code> for the <code class="prettyprint"><span class="typ">Master</span></code> and <code class="prettyprint"><span class="typ">Detail</span></code> pages are not shown.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="4">
                <p><code class="prettyprint"><span class="typ">NavigationPage</span></code>
                </p>
            </td>
            <td>
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Tint</span></code>
                </p>
            </td>
            <td>
                <p><span>Obsolete in Xamarin.Forms.</span>
                </p>
            </td>
            <td colspan="1">
                <p>No action.</p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="3" colspan="1"><span>Method</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">SetTitleIcon()</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">GetTitleIcon()</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>No action.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">SetHasBackButtonTitle()</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <p><code class="prettyprint"><span class="typ">Page</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="3">
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Icon</span></code>
                </p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>No action.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsBusy</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Does not always work as expected.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">ToolbarItems</span></code>
                </p>
            </td>
            <td>
                <p>Only one <code class="prettyprint"><span class="typ">ToolbarItem</span></code> is supported for each Order.
                    <code class="prettyprint"><span class="typ">Primary</span></code> and <code class="prettyprint"><span class="typ">Default</span></code> indicate the 'right' action button on the title bar.
                    <code class="prettyprint"><span class="typ">Secondary</span></code> indicates the 'left' action button on the title bar.
                    Therefore, if <code class="prettyprint"><span class="typ">Secondary</span></code> is used, no back button is shown.
                </p>
            </td>
            <td colspan="1">
                <p>The priority of the 'left' action button is first <code class="prettyprint"><span class="typ">Secondary</span></code> and then the back button.
                </p>
                <p>For example, if a toolbar item is assigned to <code class="prettyprint"><span class="typ">Secondary</span></code>, the left action button is the <code class="prettyprint"><span class="typ">Secondary</span></code> toolbar item.
                Only one toolbar item is supported for each order. If multiple toolbar items are specified, the first toolbar item is used.
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Slider</span></code></p>
            </td>
            <td>
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Rotation</span></code></p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>Does not always work as expected.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <p><code class="prettyprint"><span class="typ">SwitchCell</span></code></p>
            </td>
            <td class="tdtype" rowspan="2">
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Height</span></code></p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint"><span class="typ">Intent</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td>
                <code class="prettyprint"><span class="typ">TabbedPage</span></code>
            </td>
            <td>Property</td>
            <td colspan="1">
                <code class="prettyprint"><span class="typ">BarTextColor</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1">
                <code class="prettyprint"><span class="typ">TableView</span></code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1">Property</td>
            <td colspan="1">
                <code class="prettyprint"><span class="typ">RowHeight</span></code>
            </td>
            <td colspan="1">
                <p>This is applied when <code class="prettyprint"><span class="typ">HasUnevenRows</span></code> is set to <code class="prettyprint"><span class="typ">true</span></code>.</p>
                <p>However, <code class="prettyprint"><span class="typ">RowHeight</span></code> value may not be affected to Cells due to the policy of Tizen platform.</p>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Does not always work as expected.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">TextCell</span></code></p>
            </td>
            <td>
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Height</span></code></p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">ViewCell</span></code></p>
            </td>
            <td>
                <p>Property</p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">View</span></code></p>
            </td>
            <td>
                <p></p>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1">
                <code class="prettyprint"><span class="typ">WebView</span></code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1">
                <span>Property</span>
            </td>
            <td colspan="1">
                <code class="prettyprint"><span class="typ">Opacity</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
    </tbody>
</table>
</div>

<div id="TV" class="tabcontent" style="display:none">
<table>
    <tbody>
        <tr>
            <th>
                <p><span><strong>Class</strong></span></p>
            </th>
            <th>
                <p><span><strong>Type</strong></span></p>
            </th>
            <th>
                <p><span><strong>Name</strong></span></p>
            </th>
            <th>
                <p><span><strong>Remarks</strong></span></p>
            </th>
            <th colspan="1">
                <p><span><strong>Result when the feature is used</strong></span></p>
            </th>
        </tr>
        <tr>
            <td class="tdclass" rowspan="7">
                <p><code class="prettyprint"><span class="typ">BoxView</span></code></p>
            </td>
            <td class="tdtype" rowspan="5">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code></p>
            </td>
            <td>
            </td><td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code> is ignored, use <code class="prettyprint"><span class="typ">Color</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsEnabled</span></code></p>
            </td>
            <td>
            </td><td>
                <p><code class="prettyprint"><span class="typ">BoxView</span></code> is not interactive, and enabling does not change that.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsFocused</span></code></p>
            </td>
            <td>
            </td><td>
                <p>Always <code class="prettyprint"><span class="typ">false</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Focus</span></code></p>
            </td>
            <td>
            </td><td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Unfocus</span></code></p>
            </td>
            <td>
            </td><td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Event</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Focused</span></code></p>
            </td>
            <td>
            </td><td>
                <p><span>Never triggered.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Unfocused</span></code></p>
            </td>
            <td>
            </td><td>
                <p><span>Never triggered.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="4">
                <p><code class="prettyprint"><span class="typ">Button</span></code></p>
            </td>
            <td class="tdtype" rowspan="4">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderColor</span></code></p>
            </td>
            <td>
            </td><td>
                <p>Ignored.</p>
            </td>
        </tr>
        <tr><td>
                <p><code class="prettyprint"><span class="typ">BorderRadius</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <span>Ignored.</span>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderWidth</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">ContentLayout</span></code></td>
            <td>
            </td><td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">CarouselPage</span></code></td>
            <td><span>Class</span></td>
            <td><code class="prettyprint"><span class="typ">CarouselPage</span></code></td>
            <td><span>Obsolete in Xamarin.Forms.</span></td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <p><code class="prettyprint"><span class="typ">Device</span></code></p>
            </td>
            <td class="tdtype" rowspan="2">
                <p><span>Method</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">OnPlatform&lt;T&gt;(T,T,T)</span></code></p>
            </td>
            <td>
                <p>Use <code class="prettyprint"><span class="typ">OnPlatform&lt;T&gt; (T,T,T,T)</span></code> instead.</p>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">OnPlatform(Action, Action, Action, Action)</span></code></p>
            </td>
            <td>
                <p>Use <code class="prettyprint"><span class="typ">OnPlatform(Action, Action, Action, Action, Action)</span></code> instead.</p>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3"><code class="prettyprint"><span class="typ">EntryCell</span></code></td>
            <td><span>Class</span></td>
            <td><code class="prettyprint"><span class="typ">EntryCell</span></code></td>
            <td><span>Mouse pointer is required for enabling user interaction on entry of the cell.</span></td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2"><span>Property</span></td>
            <td><code class="prettyprint"><span class="typ">Height</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">Keyboard</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">Frame</span></code></td>
            <td>Property</td>
            <td><code class="prettyprint"><span class="typ">CornerRadius</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">ImageSource</span></code></td>
            <td><span>Method</span></td>
            <td><code class="prettyprint"><span class="typ">FromResource(string resource, Assembly sourceAssembly = null)</span></code></td>
            <td><span>sourceAssembly should be specified.</span></td>
            <td>
                <p><span>System.TypeInitializationException will be thrown when sourceAssembly is not to set.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Layout</span></code></p>
            </td>
            <td>
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">IsClippedToBounds</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="10">
                <p><code class="prettyprint"><span class="typ">ListView</span></code></p>
            </td>
            <td class="tdtype" rowspan="7">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code></p>
            </td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsPullToRefreshEnabled</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p>Property is always set to <code class="prettyprint"><span class="typ">false</span></code>. Attempts to change it to <code class="prettyprint"><span class="typ">true</span></code> are ignored.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsRefreshing</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p>Always <code class="prettyprint"><span class="typ">false</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">SeparatorColor</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">SeparatorVisibility</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">RowHeight</span></code></td>
            <td>
                <p>This is applied when <code class="prettyprint"><span class="typ">HasUnevenRows</span></code> is set to <code class="prettyprint"><span class="typ">true</span></code>.</p>
                <p>However, <code class="prettyprint"><span class="typ">RowHeight</span></code> value may not be affected to Cells due to the policy of Tizen platform.</p>
            </td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">RefreshCommand</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Method</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BeginRefresh()</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">EndRefresh()</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><span>Event</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Refreshing</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p>As <code class="prettyprint"><span class="typ">IsPullToRefreshEnabled</span></code> is not supported, this event is never triggered.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <p><code class="prettyprint"><span class="typ">MasterDetailPage</span></code></p>
            </td>
            <td>
                <p><span>Method</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">ShouldShowToolbarButton()</span></code></p>
            </td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">IsGestureEnabled</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <div><span>Does not always work as expected.</span></div>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">ToolbarItems</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p>Only <code class="prettyprint"><span class="typ">ToolbarItems</span></code> for the <code class="prettyprint"><span class="typ">MasterDetailPage</span></code> are shown.
                <code class="prettyprint"><span class="typ">ToolbarItems</span></code> for the <code class="prettyprint"><span class="typ">Master</span></code> and <code class="prettyprint"><span class="typ">Detail</span></code> pages are not shown.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="5">
                <p><code class="prettyprint"><span class="typ">NavigationPage</span></code></p>
            </td>
            <td>
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Tint</span></code></p>
            </td>
            <td>
                <p><span>Obsolete in Xamarin.Forms.</span></p>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="4"><span>Method</span></td>
            <td><code class="prettyprint"><span class="typ">SetTitleIcon()</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">GetTitleIcon()</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">SetHasBackButton()</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">SetHasBackButtonTitle()</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">PinchGestureRecognizer</span></code></td>
            <td><span>Event</span></td>
            <td><code class="prettyprint"><span class="typ">PinchUpdated</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Never occured.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <p><code class="prettyprint"><span class="typ">Page</span></code></p>
            </td>
            <td class="tdtype" rowspan="3">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Icon</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>No action.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">IsBusy</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">ToolbarItems</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">SearchBar</span></code></td>
            <td><span>Class</span></td>
            <td><code class="prettyprint"><span class="typ">SearchBar</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Slider</span></code></p>
            </td>
            <td><span>Property</span></td>
            <td><code class="prettyprint"><span class="typ">BackgroundColor</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2"><code class="prettyprint"><span class="typ">Stepper</span></code></td>
            <td>
                <p><span>Class</span></p>
            </td>
            <td><code class="prettyprint"><span class="typ">Stepper</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always shown as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td><span>Property</span></td>
            <td><code class="prettyprint"><span class="typ">BackgroundColor</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3"><code class="prettyprint"><span class="typ">SwitchCell</span></code></td>
            <td><span>Class</span></td>
            <td><code class="prettyprint"><span class="typ">SwitchCell</span></code></td>
            <td><span>Mouse pointer is required for enabling user interaction on switch of the cell.</span></td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Height</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">Intent</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">TabbedPage</span></code></td>
            <td><span>Property</span></td>
            <td><code class="prettyprint"><span class="typ">BarTextColor</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2"><code class="prettyprint"><span class="typ">TableView</span></code></td>
            <td class="tdtype" rowspan="2"><span>Property</span></td>
            <td><code class="prettyprint"><span class="typ">RowHeight</span></code></td>
            <td>
                <p>This is applied when <code class="prettyprint"><span class="typ">HasUnevenRows</span></code> is set to <code class="prettyprint"><span class="typ">true</span></code>.</p>
                <p>However, <code class="prettyprint"><span class="typ">RowHeight</span></code> value may not be affected to Cells due to the policy of Tizen platform.</p>
            </td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">BackgroundColor</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <p><code class="prettyprint"><span class="typ">TextCell</span></code></p>
            </td>
            <td class="tdtype" rowspan="2">
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Height</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <div><span>Ignored.</span></div>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">Detail</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">ViewCell</span></code></p>
            </td>
            <td>
                <p><span>Property</span></p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">View</span></code></p>
            </td>
            <td>
            </td>
            <td>
                <p><span>Does not always work as expected.</span></p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2"><code class="prettyprint"><span class="typ">WebView</span></code></td>
            <td class="tdtype" rowspan="2"><span>Property</span></td>
            <td><code class="prettyprint"><span class="typ">Opacity</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td><code class="prettyprint"><span class="typ">BackgroundColor</span></code></td>
            <td>&nbsp;</td>
            <td>
                <p><span>Ignored.</span></p>
            </td>
        </tr>
    </tbody>
</table>
</div>

<div id="Wearable" class="tabcontent" style="display:none">
<table>
    <tbody>
        <tr>
            <th>
                <p><span><strong>Class</strong></span>
                </p>
            </th>
            <th>
                <p><span><strong>Type</strong></span>
                </p>
            </th>
            <th>
                <p><span><strong>Name</strong></span>
                </p>
            </th>
            <th>
                <p><span><strong>Remarks</strong></span>
                </p>
            </th>
            <th colspan="1">
                <p><span><strong>Result when the feature is used</strong></span>
                </p>
            </th>
        </tr>
        <tr>
            <td class="tdclass" rowspan="6" colspan="1"><code class="prettyprint"><span class="typ">ActivityIndicator</span></code>
            </td>
            <td class="tdtype" rowspan="6" colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Opacity</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>Does not always work as expected</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">HeightRequest</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>Does not always work as expected</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">WidthRequest</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>Does not always work as expected</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsEnabled</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsRunning</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>Does not always work as expected</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>ignored.</p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="7">
                <p><code class="prettyprint"><span class="typ">BoxView</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="5">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code>&nbsp;is ignored, use&nbsp;<code class="prettyprint"><span class="typ">Color</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsEnabled</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><code class="prettyprint"><span class="typ">BoxView</span></code>&nbsp;is not interactive, and enabling does not change that.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsFocused</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p>Always&nbsp;<code class="prettyprint"><span class="typ">false</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Focus</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Unfocus</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Event</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Focused</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Never triggered.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">Unfocused</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Never triggered.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="5">
                <p><code class="prettyprint"><span class="typ">Button</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="5">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderColor</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <div><span>Ignored.</span>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderRadius</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <div><span>Ignored.</span>
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">BorderWidth</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">ContentLayout</span></code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Opacity</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">CarouselPage</span></code>
            </td>
            <td colspan="1"><span>Class</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">CarouselPage</span></code>
            </td>
            <td colspan="1"><span>Obsolete in Xamarin.Forms.</span>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <p><code class="prettyprint"><span class="typ">Device</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="2">
                <p><span>Method</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">OnPlatform&lt;T&gt;(T,T,T)</span></code></p>
            </td>
            <td>
                <p><span>&nbsp;Use <code class="prettyprint"><span class="typ">OnPlatform&lt;T&gt; (T,T,T,T)</span></code> instead.</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">OnPlatform(Action, Action, Action, Action)</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;Use <code class="prettyprint"><span class="typ">OnPlatform(Action, Action, Action, Action, Action)</span></code> instead.</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">DatePicker</span></code>
            </td>
            <td colspan="1"><span>Class</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">DatePicker</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Not Supported.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Editor</span></code>
            </td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Editor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Entry</span></code>
            </td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Entry</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1"><code class="prettyprint"><span class="typ">EntryCell</span></code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1"><span>Property</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Height</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p>Ignored.</p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Keyboard</span></code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span><span>Does not always work as expected.</span></span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Frame</span></code>
            </td>
            <td colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">CornerRadius</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Image</span></code>
            </td>
            <td colspan="1"><span>Property</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsOpaque</span></code>
            </td>
            <td colspan="1"></td>
            <td colspan="1">
                <p><span>Ignored.</span></p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">ImageSource</span></code>
            </td>
            <td colspan="1"><span>Method</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">FromResource(string resource, Assembly sourceAssembly = null)</span></code>
            </td>
            <td colspan="1"><span>sourceAssembly should be specified.</span>
            </td>
            <td colspan="1">
                <p><span>System.TypeInitializationException will be thrown when sourceAssembly is not to set.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span>Layout</span></code>
                </p>
            </td>
            <td>
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span>IsClippedToBounds</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="10">
                <p><code class="prettyprint"><span class="typ">ListView</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="7">
                <p><span>Property&nbsp;</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
                </p>
            </td>
            <td>&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsPullToRefreshEnabled</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Property is always set to&nbsp;<code class="prettyprint"><span class="typ">false</span></code>. Attempts to change it to&nbsp;<code class="prettyprint"><span class="typ">true</span></code>&nbsp;are ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">IsRefreshing</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p>Always&nbsp;<code class="prettyprint"><span class="typ">false</span></code>.</p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">SeparatorColor</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Separator is not visible, so the color has no effect.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">SeparatorVisibility</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">RowHeight</span></code>
            </td>
            <td colspan="1">
                <p>This is applied when <code class="prettyprint"><span class="typ">HasUnevenRows</span></code> is set to <code class="prettyprint"><span class="typ">true</span></code>.</p>
                <p>However, <code class="prettyprint"><span class="typ">RowHeight</span></code> value may not be affected to Cells due to the policy of Tizen platform.</p>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">RefreshCommand</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="2">
                <p><span>Method</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">BeginRefresh()</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">EndRefresh()</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><span>Event</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Refreshing</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p>As&nbsp;<code class="prettyprint"><span class="typ">IsPullToRefreshEnabled</span></code>&nbsp;is not supported, this event is never triggered.
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">MasterDetailPage</span></code>
            </td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">MasterDetailPage</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Not Supported.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="5">
                <p><code class="prettyprint"><span class="typ">NavigationPage</span></code>
                </p>
            </td>
            <td>
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Tint</span></code>
                </p>
            </td>
            <td>
                <p><span>Obsolete in Xamarin.Forms.</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdtype" rowspan="4" colspan="1"><span>Method</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">SetTitleIcon()</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">GetTitleIcon()</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">SetHasBackButton()</span></code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.&nbsp;</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">SetHasBackButtonTitle()</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.&nbsp;</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <p><code class="prettyprint"><span class="typ">Page</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="3">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Icon</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>No action.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsBusy</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">ToolbarItems</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span><span>Does not always work as expected.</span></span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Picker</span></code>
            </td>
            <td colspan="1">Property</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Opacity</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">SearchBar</span></code></td>
            <td colspan="1"><span>Class</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">SearchBar</span></code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1">
                <p><code class="prettyprint"><span class="typ">Slider</span></code></p>
            </td>
            <td colspan="1">
                <p><span>Property</span></p>
            </td><td colspan="1"><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Stepper</span></code></td>
            <td colspan="1"><span>Property&nbsp;</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2">
                <p><code class="prettyprint"><span class="typ">SwitchCell</span></code></p>
            </td>
            <td class="tdtype" rowspan="2">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Height</span></code>
                </p>
            </td>
            <td>
                <p>&nbsp;</p>
            </td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Intent</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1"><code class="prettyprint"><span class="typ">TabbedPage</span></code></td>
            <td class="tdtype" rowspan="2" colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">TabbedPage</span></code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Not Supported.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">BarTextColor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3" colspan="1"><code class="prettyprint"><span class="typ">TableView</span></code></td>
            <td class="tdtype" rowspan="3" colspan="1"><span>Property</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">RowHeight</span></code></td>
            <td colspan="1">
                <p>This is applied when <code class="prettyprint"><span class="typ">HasUnevenRows</span></code> is set to <code class="prettyprint"><span class="typ">true</span></code>.</p>
                <p>However, <code class="prettyprint"><span class="typ">RowHeight</span></code> value may not be affected to Cells due to the policy of Tizen platform.</p>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span><span>Does not always work as expected.</span></span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsEnabled</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span><span>Does not always work as expected.</span></span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="3">
                <p><code class="prettyprint"><span class="typ">TextCell</span></code>
                </p>
            </td>
            <td class="tdtype" rowspan="3">
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">Height</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <div><span>Ignored.</span>
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">Detail</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">IsEnabled</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">TimePicker</span></code></td>
            <td colspan="1">Class</td>
            <td colspan="1"><code class="prettyprint"><span class="typ">TimePicker</span></code></td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Not Supported.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <p><code class="prettyprint"><span class="typ">ViewCell</span></code>
                </p>
            </td>
            <td>
                <p><span>Property</span>
                </p>
            </td>
            <td>
                <p><code class="prettyprint"><span class="typ">View</span></code>
                </p>
            </td>
            <td>
                <p><span>&nbsp;</span>
                </p>
            </td>
            <td colspan="1">
                <p><span>Does not always work as expected.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td class="tdclass" rowspan="2" colspan="1"><code class="prettyprint"><span class="typ">WebView</span></code>
            </td>
            <td class="tdtype" rowspan="2" colspan="1"><span>Property</span>
            </td>
            <td colspan="1"><code class="prettyprint"><span class="typ">Opacity</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
        <tr>
            <td colspan="1"><code class="prettyprint"><span class="typ">BackgroundColor</span></code>
            </td>
            <td colspan="1">&nbsp;</td>
            <td colspan="1">
                <p><span>Ignored.</span>
                </p>
            </td>
        </tr>
    </tbody>
</table>
</div>

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
