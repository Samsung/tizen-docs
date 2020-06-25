# Tizen Applications

<style>
#main:before, #main:after {
    content: "";
    display: table;
}

.docs-ui-started [class^="docs-ui-"] {
    width: 33%; 
    height: auto;
    padding: 40px 0;
    text-align: center;
    border: 0 none;
    border-top: 1px solid #dadada;
    border-bottom: 1px solid #dadada;
    box-sizing: border-box;
    position: relative;
    float: left;
    margin: 0 auto 20px;
}

.docs-ui-started [class^="docs-ui-"]>span {
    display: block;
    color: #333;
    line-height: 29px;
    font-weight: bold;
    position: relative;
}

@media (max-width: 768px)
.docs-ui-started .docs-ui-wearable:before, .docs-ui-started .docs-ui-tv:before, .docs-ui-started .docs-ui-mobile:before {
    height: 85px;
    margin: 0 auto 25px;
    align: center;
    background-position: 0 6px;
}
.docs-ui-started .docs-ui-wearable:before {
    content: "";
    display: block;
    margin: auto;
    position: relative;
    width: 60px;
    height: 90px;
    background: url(./media/icon_get_started_wearable.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-wearable {
    width: 33%;
    padding-left: 50;
    /* border-right: 1px solid #d1d1d1; */
}

.docs-ui-started .docs-ui-tv:before {
    content: "";
    margin: auto;
    position: relative;
    display: block;
    width: 93px;
    height: 90px;
    background: url(./media/icon_get_started_tv.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-tv {
    width: 33%;
    padding-left: 50;
}

.docs-ui-started .docs-ui-mobile:before {
    content: "";
    margin: auto;
    position: relative;
    display: block;
    width: 53px;
    height: 90px;
    background: url(./media/icon_get_started_mobile.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started.docs-ui-mobile {
    width: 33%;
    padding-left: 50px;
}

div {
    display: block;
}

a.docs-btn-more {
    display: inline-block;
    font-size: 14px;
    color: #008aee;
}
</style>

<section id ="main">
Tizen is a user-interactive and service-oriented open source project that allows you to create feature-rich applications for multiple device categories.

To get started with the development of your own Tizen applications:
<div class="docs-ui-started">
  <div class="docs-ui-wearable">
    <span>
    <a href="get-started/wearable.md" class="docs-btn-more">Get Started for Wearable</a>
    </span>
  </div>

  <div class="docs-ui-tv">
    <span>
     <a href="get-started/tv.md" class="docs-btn-more">Get Started for TV</a>
    </span>
  </div>

  <div class="docs-ui-mobile">
    <span>
    <a href="get-started/mobile.md" class="docs-btn-more">Get Started for Mobile</a>
    </span>
  </div>

</div>
</section>

<a name="profiles"></a>
## Tizen Profiles

Tizen is built to work on a wide variety of platforms with a focus on embedded devices. In order to accommodate the various types of devices, a set of profiles has been defined to make it easier to develop applications for specific purposes and device types. Since Tizen 3.0, there are 3 profile types you can choose from: mobile, wearable, and TV. The mobile profile is designed for smart phones, the wearable profile is designed for smart watches, and the TV profile is designed for smart TVs.

Both mobile and wearable profiles are supported in native and Web application types. The TV profile is supported in the Web application type only.

**Figure: Applications using the wearable profile**

![Applications using the wearable profile](media/profile_wearable.png)

**Figure: Applications using the TV profile**

![Applications using the TV profile](media/profile_tv.png)

**Figure: Applications using the mobile profile**

![Applications using the mobile profile](media/profile_mobile.png)

<a name="type"></a>
## Tizen Application Types

The Tizen platform supports three primary application types:

-   [Tizen .NET application](dotnet/index.md) is a new way to develop applications for the Tizen operating system, running on 50 million Samsung devices, including TVs, wearables, mobile devices, and many other IoT devices around the world. The existing Tizen frameworks are either C-based with no advantages of a managed runtime, or HTML5-based with fewer features and lower performance than the C-based solution.

    With Tizen .NET, you can use the C\# programming language and the Common Language Infrastructure standards and benefit from a managed runtime for faster application development, and efficient, secure code execution.

-  [Web application](web/index.md) is essentially a Web site stored on your device and built using Web-native languages, such as HTML5, CSS, and JavaScript. The Web application uses the Tizen Web framework to interact with the native subsystems.

    The Web applications use the Web API, which is a standard Web application project structure with basic elements. The Web API is designed to allow you to easily build applications using Web-native languages.

    A program built using the Web API is laid out much like a standard Web site. It has an `index.html` file that serves as the root, and separate directories for resources, such as JavaScript, CSS, images, and sound resources. This approach makes Web application development in Tizen extremely intuitive for developers with a background in Web development, and makes it easy to quickly write simple applications using high-level languages.

-   [Native application](native/index.md) is developed using C and can access more advanced device-specific features, such as camera, GPS, and accelerometer in addition to more advanced system settings and functionality.

    The native applications use the Native API, which provides all of the memory management and performance benefits that come with building applications for Linux in C. The Native API is extremely helpful, as it includes dozens of API modules that cover a large range of capabilities. It provides numerous interfaces to much of the hardware that is found in modern mobile and wearable devices, and does so in an environment that is tailored for limited resources.

The following figure illustrates the Tizen architecture model supporting the 3 application types.

**Figure: Tizen architecture**

![Tizen architecture](media/what_is_tizen_architecture.png)

The Tizen platform also allows you to develop a hybrid application package where native and Web applications are packaged together to make more powerful applications. The Tizen platform ensures that all Tizen applications have consistent look and feel, regardless of whether you use the native or Web framework to create them.



To become familiar with some terms that you encounter throughout this site, see [Glossary](../glossary.md).

To see the trademark notice list, see [Trademarks](../trademarks.md).

**See the following links for more information:**
- Source code (GIT/Gerrit): https://review.tizen.org/gerrit
- Tizen Build setup (OBS): https://build.tizen.org/
- Tizen Bug Tracking system (Jira): https://bugs.tizen.org/
- Download URL: http://download.tizen.org/

