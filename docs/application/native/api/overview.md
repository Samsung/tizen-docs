# Native API Reference

Tizen Native API is carefully selected and tightly managed APIs from the Tizen Native subsystems. The Native API is divided into dozens of API modules; each module represents a logically similar set of submodule APIs, which can be grouped into the same category.

Tizen Native APIs supports mobile and wearable devices. They contain somewhat different modules. For more information, see API Reference for <a href="mobile/latest/index.html" target="_blank">mobile</a> or <a href="wearable/latest/index.html" target="_blank">wearable</a>.

## Required Header

To be able to use an API, you need to include a header in which API is defined. You can find required headers in API reference as illustrated below:

**Figure: Required Header**

![Required Header](media/required_header.png)


## Related Feature

Some of the Tizen Native APIs require features to prevent your application from being shown in the application list on Tizen Store. If related Feature is included in API reference as shown below and your application uses that feature, then you need to declare the feature in the tizen-manifest.xml file. For more information, see Application Filtering.

**Figure: Related Feature**

![Related Feature](media/related_feature.png)


## Structure of Function Descriptions

In the function documentation for each module, the functions are described using a unified structure, illustrated in the below example.

**Figure: Reference Structure**

![Reference Structure](media/function_structure.png)


## Privilege

The privilege is essential part to get access grant for privacy related data or sensitive system resources. For more information, see Privileges.
Some of Tizen Native API functions require adding appropriate privileges (defined in each API's Privilege section in the specification) to the tizen-manifest.xml file. If required privileges are not included in the tizen-manifest.xml file, then the function will return TIZEN_ERROR_PERMISSION_DENIED error.

For example, see the "Privilege:" section in the following picture:

**Figure: Privilege**

![Privilege](media/native_privilege.png)


## Versions
<ul>
<li>Wearable
  <ul>
    <li><a href="wearable/6.0/index.html" target="_blank">6.0</a></li>
    <li><a href="wearable/5.5/index.html" target="_blank">5.5</a></li>
    <li><a href="wearable/5.0/index.html" target="_blank">5.0</a></li>
    <li><a href="wearable/4.0/index.html" target="_blank">4.0</a></li>
    <li><a href="wearable/3.0/index.html" target="_blank">3.0</a></li>
    <li><a href="wearable/2.3.2/index.html" target="_blank">2.3.2</a></li>
    <li><a href="archive/org.tizen.apireference_2.3.1.zip">2.3.1</a></li>
  </ul>
</li>
<li>Mobile
  <ul>
    <li><a href="mobile/6.0/index.html" target="_blank">6.0</a></li>
    <li><a href="mobile/5.5/index.html" target="_blank">5.5</a></li>
    <li><a href="mobile/5.0/index.html" target="_blank">5.0</a></li>
    <li><a href="mobile/4.0/index.html" target="_blank">4.0</a></li>
    <li><a href="mobile/3.0/index.html" target="_blank">3.0</a></li>
    <li><a href="mobile/2.4/index.html" target="_blank">2.4</a></li>
    <li><a href="archive/org.tizen.apireference_2.3.1.zip">2.3.1</a></li>
    <li><a href="archive/org.tizen.apireference_2.3.0.zip">2.3</a></li>
  </ul>
</li>
<li>Iot-Headed
  <ul>
    <li><a href="iot-headed/5.5/index.html" target="_blank">5.5</a></li>
    <li><a href="iot-headed/5.0/index.html" target="_blank">5.0</a></li>
    <li><a href="iot-headed/4.0/index.html" target="_blank">4.0</a></li>
  </ul>
</li>
<li>Iot-Headless
  <ul>
    <li><a href="iot-headless/5.5/index.html" target="_blank">5.5</a></li>
    <li><a href="iot-headless/5.0/index.html" target="_blank">5.0</a></li>
    <li><a href="iot-headless/4.0/index.html" target="_blank">4.0</a></li>
  </ul>
</li>
</ul>
