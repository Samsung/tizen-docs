# Native API Reference

Tizen Native API is carefully selected and tightly managed APIs from the Tizen native subsystems. The Native API is divided into dozens of API modules; each module represents a logically similar set of submodule APIs, which can be grouped into the same category.


## Required Header

To be able to use an API, you need to include a header in which API is defined. You can find required headers in API reference as illustrated below:

Figure:Required Header

![Required Header](media/required_header.png)


## Related Feature

Some of the Tizen native APIs require features to prevent your application from being shown in the application list on the Tizen store. If related Feature is included in API reference as shown below and your application uses that feature, then you need to declare the feature in the tizen-manifest.xml file. For more information, see Application Filtering.

Figure:Related Feature

![Related Feature](media/related_feature.png)


## Structure of Function Descriptions

In the function documentation for each module, the functions are described using a unified structure, illustrated in the below example.

Figure:Reference Structure

![Reference Structure](media/function_structure.png)


## Privilege

The privilege is essential part to get access grant for privacy related data or sensitive system resources. For more information, see Privileges.
Some of Tizen Native API functions require adding appropriate privileges (defined in each API's Privilege section in the specification) to the tizen-manifest.xml file. If required privileges are not included in the tizen-manifest.xml file, then the function will return TIZEN_ERROR_PERMISSION_DENIED error.

For example, see the "Privilege:" section in the following picture:

Figure:Privilege

![Privilege](media/native_privilege.png)


## Versions
<ul>
<li>Mobile
  <ul>
    <li><a href="mobile/4.0/launch.md">4.0</a></li>
    <li><a href="mobile/3.0/launch.md">3.0</a></li>
    <li><a href="mobile/2.4/launch.md">2.4</a></li>
    <li><a href="https://developer.tizen.org/development/api-references/native-application?redirect=https://developer.tizen.org/dev-guide/2.3.1/org.tizen.native.mobile.apireference/index.html" target="api">2.3.1</a>&nbsp;&nbsp;&nbsp;<strong>You can see 2.3.1 on Tizen Developer Site(https://developer.tizen.org)</strong></li>
    <li><a href="https://developer.tizen.org/development/api-references/native-application?redirect=https://developer.tizen.org/dev-guide/2.3/org.tizen.native.mobile.apireference/index.html" target="api">2.3</a>&nbsp;&nbsp;&nbsp;<strong>You can see 2.3 on Tizen Developer Site(https://developer.tizen.org)</strong></li>
  </ul>
</li>

<li>Wearable
  <ul>
    <li><a href="wearable/4.0/launch.md">4.0</a></li>
    <li><a href="wearable/3.0/launch.md">3.0</a></li>
    <li><a href="wearable/2.3.2/launch.md">2.3.2</a></li>
    <li><a href="https://developer.tizen.org/development/api-references/native-application?redirect=https://developer.tizen.org/dev-guide/2.3.1/org.tizen.native.wearable.apireference/index.html" target="api">2.3.1</a>&nbsp;&nbsp;&nbsp;<strong>You can see 2.3.1 on Tizen developer site(https://developer.tizen.org).</strong></li>
    <li><a href="https://developer.tizen.org/development/api-references/native-application?redirect=https://developer.tizen.org/dev-guide/2.3/org.tizen.native.wearable.apireference/index.html" target="api">2.3</a><strong>  You can see 2.3 on Tizen developer site(https://developer.tizen.org).</strong></li>
  </ul>
</li>

</ul>
