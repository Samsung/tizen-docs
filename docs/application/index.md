<a name="training"></a>
# Getting Started

### Get Started with Tizen
![Download](media/ic_docs_download.png) [**Download Tizen Source**](open-source-project/developing/cloning.md)
- [What is Tizen?](what-is-tizen/tizen.md)
- [What is Tizen Open Source Project?](open-source-project/about/tizen-open-source-overview.md)
- Developers can register for an account at: [https://www.tizen.org/user/register](https://www.tizen.org/user/register)
- [More](open-source-project/developing/installing.md)

<!-- IOT Content (TBD) -->
<!--## IOT world on Craftroom
- What is Tizen IoT?
- How to make IoT devices
  Go to craftroom
-->

## Get Started with Tizen .NET
![Download](media/ic_docs_download.png) [**Download Visual Studio Tools for Tizen**](https://developer.tizen.org/development/tizen-.net-preview/getting-started)
- [What is Tizen .NET Application?](https://developer.tizen.org/development/tizen-.net-preview/introduction/overview)
- [Creating Tizen .NET Applications](https://developer.tizen.org/development/tizen-.net-preview/getting-started/creating-your-first-tizen-.net-application)
<!--
- Getting Started with Visual Studio Tools for Tizen  
Samsung has released a preview of Visual Studio Tools for Tizen, which will enable .NET developers to build apps for Tizen. This video preview shows you how to get started.
<p style="margin-left:50px;">
<a href="https://www.youtube.com/embed/fPORr-CqMvY" target="_blank">
<img alt="Getting Started with Visual Studio Tools for Tizen" src="https://img.youtube.com/vi/fPORr-CqMvY/0.jpg" width="254" height="158"></a>  
</p>

- An Introduction to Tizen .NET  
Sidharth Gupta from Samsung introduces Tizen .NET on the Youtube channel, 'On.NET'. Tizen is Samsung's open source OS that runs on TVs, watches, phones, and other devices.
<p style="margin-left:50px;">
<a href="https://www.youtube.com/embed/H52DdXBZh4Q" target="_blank">
<img alt="An Introduction to Tizen .NET" src="https://img.youtube.com/vi/H52DdXBZh4Q/0.jpg" width="254" height="158"></a>  
</p>

- Visual Studio Tools for Tizen: Development and Productivity Improvements  
In the first preview of Visual Studio Tools for Tizen, we began to leverage the power of C# and Xamarin.Forms to create applications for the Tizen OS which runs on smartphones, smart TVs, smartwatches, IoT devices and many more types of devices.
<p style="margin-left:50px;">
<a href="https://youtube.com/embed/NdvWwU0gKt8" target="_blnak">
<img alt="Visual Studio Tools for Tizen: Development and Productivity Improvements" src="https://img.youtube.com/vi/NdvWwU0gKt8/0.jpg" width="254" height="158"></a>
</p>
-->

- [More](https://developer.tizen.org/development/visual-studio-tools-tizen/)


## Get Started with Tizen Studio
![Download](media/ic_docs_download.png) [**Download Tizen Studio**](https://developer.tizen.org/development/tizen-studio/download)
- [What is Tizen Application?](https://developer.tizen.org/development/training/native-application)
- [Creating Tizen Native Applications](https://developer.tizen.org/development/training/native-application/getting-started)
- [Creating Tizen Web Applications](https://developer.tizen.org/development/training/web-application/getting-started)
- [More](https://developer.tizen.org/development/tizen-studio/)

  
# Tizen Applications

Tizen is a user-interactive and service-oriented open source project that allows you to create feature-rich applications for multiple device categories.

Tizen is designed to be equally friendly to embedded systems developers and Web developers alike, and its flexible nature encourages its use on an array of devices, including TVs, smart phones, watches, tablets, in-vehicle infotainment systems, and smart appliances. Tizen provides a Native API that provides the benefits of building software for embedded systems in C; it also provides a Web API that allows you to create simple programs using only HTML5, CSS, and JavaScript.

To get started with the development of your own Tizen applications:

-   [Create your first simple native application](native/getting-started-n.md), and learn about the main features available for implementing your dream application.
-   [Create your first simple Web application](web/getting-started-w.md), and learn about the main features available for implementing your dream application.
-   [Create your first Tizen .NET application](dotnet/first-app.htm), and learn about the main features available for implementing your dream application.

<a name="type"></a>
## Tizen Application Types


The Tizen platform supports 3 primary application types:

-   [Native application](native/index.md) is developed using C and can access more advanced device-specific features, such as camera, GPS, and accelerometer in addition to more advanced system settings and functionality.

    The native applications use the Native API, which provides all of the memory management and performance benefits that come with building applications for Linux in C. The Native API is extremely helpful, as it includes dozens of API modules that cover a large range of capabilities. It provides numerous interfaces to much of the hardware that is found in modern mobile and wearable devices, and does so in an environment that is tailored for limited resources.

-   [Web application](web/index.md) is essentially a Web site stored on your device and built using Web-native languages, such as HTML5, CSS, and JavaScript. The Web application uses the Tizen Web Framework to interact with the native subsystems.

    The Web applications use the Web API, which is a standard Web application project structure with basic elements. The Web API is designed to allow you to easily build applications using Web-native languages.

    A program built using the Web API is laid out much like a standard Web site. It has an `index.html` file that serves as the root, and separate directories for resources, such as JavaScript, CSS, images, and sound resources. This approach makes Web application development in Tizen extremely intuitive for developers with a background in Web development, and makes it easy to quickly write simple applications using high-level languages.

-   [Tizen .NET application](dotnet/index.md) is a new way to develop applications for the Tizen operating system, running on 50 million Samsung devices, including TVs, wearables, mobile devices, and many other IoT devices around the world. The existing Tizen frameworks are either C-based with no advantages of a managed runtime, or HTML5-based with fewer features and lower performance than the C-based solution.

    With Tizen .NET, you can use the C\# programming language and the Common Language Infrastructure standards and benefit from a managed runtime for faster application development, and efficient, secure code execution.

The following figure illustrates the Tizen architecture model supporting the 3 application types.

**Figure: Tizen architecture**

![Tizen architecture](media/what_is_tizen_architecture.png)

The Tizen platform also allows you to develop a hybrid application package where native and Web applications are packaged together to make more powerful applications. The Tizen platform ensures that all Tizen applications have consistent look and feel, regardless of whether you use the native or Web framework to create them.

<a name="profiles"></a>
## Tizen Profiles

Tizen is built to work on a wide variety of platforms with a focus on embedded devices. In order to accommodate the various types of devices, a set of profiles has been defined to make it easier to develop applications for specific purposes and device types. Since Tizen 3.0, there are 3 profile types you can choose from: mobile, wearable, and TV. The mobile profile is designed for smart phones, the wearable profile is designed for smart watches, and the TV profile is designed for smart TVs.

Both mobile and wearable profiles are supported in native and Web application types. The TV profile is supported in the Web application type only.

**Figure: Applications using the mobile profile**

![Applications using the mobile profile](media/profile_mobile.png)

**Figure: Applications using the wearable profile**

![Applications using the wearable profile](media/profile_wearable.png)

**Figure: Applications using the TV profile**

![Applications using the TV profile](media/profile_tv.png)


To become familiar with some terms that you encounter throughout this site, see [Glossary](../glossary.md).  
To see the trademark notice list, see [Trademarks](../trademarks.md).

**See the following links for more information:**
- Source code (GIT/Gerrit): https://review.tizen.org/gerrit
- Tizen Build setup (OBS): https://build.tizen.org/
- Tizen Bug Tracking system (Jira): https://bugs.tizen.org/
- Download URL: http://download.tizen.org/

