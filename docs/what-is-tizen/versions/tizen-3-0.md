# Tizen 3.0

In the last 4 years, Tizen has expanded its horizon first from mobile devices to smart watches, and now to TVs. Tizen currently runs on many commercially available devices. However, the true potential of Tizen lies ahead and is going to be realized with support for the **Internet of Things (IoT)**, which connects everything.

**Figure: Tizen expanding through releases**

![Tizen expanding through releases](media/3.0_introduction_1.png)

Tizen supports multiple device profiles, each optimized for a specific device category and taking care of diverse requirements related to display, connectivity, user interface, sensors, health, security, memory and performance. All profiles are built on top of a common, shared infrastructure called Tizen Common providing the best optimized components. And even better, new profiles can be created and extended with ease, allowing new convergence device classes to be added.

**Figure: Tizen profiles**

![Tizen profiles](media/3.0_introduction_2.png)

![Tizen profiles](media/3.0_introduction_3.png)

## New Features for Enhancing Performance

Tizen 3.0 adopts various new features, such as high-performance graphics, latest Web technology, intensified security, and multi-user support:

- **Vulkan - new generation graphics API**  
Vulkan, the new Khronos graphics API, provides 1 unified API framework for desktop, mobile, console, and embedded - unlike its predecessor OpenGL, which had different versions for embedded and desktop (OpenGL ES and OpenGL). Vulkan minimizes driver overhead and provides an architecture that enables you to take advantage of multi-core CPUs. Vulkan also enables reduced load on CPUs through the use of batching, leaving the CPU free to do additional computation or rendering.
- **Wayland - lighter and better display server**  
To improve Tizen performance, a better and lighter display server, Wayland, has replaced the old X Windowing system. Compared to X, Wayland's simplified architecture brings better performance, memory usage, and scalability. It is an optimal solution for IoT devices with a small display.
- **UHD support, optimized native graphics**  
Tizen 3.0 has improved native graphics performance greatly. Tizen 3.0 supports the UHD display format, and runs 30% faster than Tizen 2.4.
- **Crosswalk**  
Tizen now supports Crosswalk, an open source based Web runtime built with the latest releases of Chromium and Blink. It is designed to support multiple platforms, to allow you to code once and reuse on other platforms. By using the Crosswalk Project, you can:
  - Use all the features available in modern Web browsers: HTML5, CSS3, and JavaScript.
  - Access the latest recommended and emerging Web standards.
  - Use experimental APIs not available in mainstream Web browsers.
- **Latest Linux LTS (Long Term Support) kernel**  
LTS ensures stability and performance, and enables Tizen to use the latest kernel features. In addition, it makes Tizen more secure and up to date with latest kernel features.
- **64-bit support**  
In order to extend the Tizen HW ecosystem to cover powerful CPU cores, Tizen 3.0 supports 64-bit CPUs, including both Intel and ARM architectures. Utilizing high performance with more address space available in the 64-bit CPUs, Tizen 3.0 helps you when developing high performance applications, such as video editing and games.
- **Multi-user support**  
Many devices, such as Smart TVs, tablets, and cars, are shared by all family members, while everyone wants to keep the device personalized to their own preferences and needs. To accommodate such needs, Tizen 3.0 supports multiple users through logins and multiple sessions. Using Tizen 3.0, each device user can control their own services, private content, and favorite settings independently from other users.
- **Simple and flexible security**  
Security has been one of Tizen's major strengths. Strong security, however, has sometimes caused difficulties in managing security policies. To solve these difficulties, Tizen 3.0 introduces a new security model.

  By grouping the similarly privileged system resources, policy management complexity at the kernel level is greatly reduced. For user space access control, a policy checker called Cynara checks that the application has the required privilege to use a privileged API. This approach implements a flexible, fast, and safe policy-checking service for granting applications any necessary access to system resources, while it allows access control on the API-level granularity.

  Tizen 3.0 also introduces a new anti-virus framework and privacy guard. The privacy guard reports statistics on how applications are using each resource, such as GPS and connectivity, and the user can control the configuration of the same.
- **User interface**  
Tizen 3.0 introduces a host of changes to the User Interface module. Tizen 3.0 has enhanced voice framework support, which includes speech-to-text support for around 11 languages and text-to-speech support for around 28 languages. Tizen 3.0 also supports voice control through S-Voice.
- **Multimedia**  
Tizen 3.0 supports face and image recognition. Using new, simplified face recognition APIs, you can detect the facial expression of a user or recognize faces on images. These newly added multimedia features enable you to develop rich applications with seamless user interaction.


## IoT Capability of Tizen 3.0

The most important features that enable Tizen to move to the next level are IoT and convergence capabilities:

- **Device Convergence**  
With the increase of devices being connected together, users are expecting more synergy among those devices. Tizen 3.0 provides a device-to-device convergence framework for easy data sharing and remote application control directly between devices. Using this framework, you can handle events or data on a remote device as if they were local. For example, imagine setting up your morning alarm and that event being shared by all your devices so that in addition to your phone sounding the alarm, your microwave oven starts cooking and the TV automatically displays the news brief. Imagine also that, without any effort, the contact list on the phone is shared and synchronized among your devices. Device Convergence in Tizen opens up a host of capabilities that you can use to create a path-breaking user experience.
- **IoTivity for Connectivity**  
In an IoT world where everything is connected, it is important that a software platform supports seamless connectivity among all devices. For seamless connectivity, Tizen is closely cooperating with Open Connected Foundation (OCF), which is defining a global standard for IoT connectivity. OCF is getting great support from companies including Cisco, GE, Mediatek, Intel and Samsung. OCF's standard is being implemented as open source and called IoTivity. Its first version is ready to be released, and all profiles in Tizen 3.0 include Iotivity by default. It means that all Tizen devices are Iotivity-ready.


For more information, see [Tizen 3.0 public M3 release note](../../open-source-tizen/release-notes/tizen-3-0-m3.md).
