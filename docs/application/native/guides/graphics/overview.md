# Graphics


The graphics features introduce how you can improve the visual look of your application through efficient use of images. You can handle graphics using various graphic libraries and interfaces, such as Cairo and OpenGL&reg; ES. You can also improve the performance of your graphic application with hardware acceleration.

You can use the following graphics features in your native applications:

- [Graphic Buffer and Surface](graphic-buffer.md)

  The Tizen Buffer Manager (TBM) surface is used to handle the graphic buffer in Tizen. TBM provides the abstraction interface for the graphic buffer and the user interface for the TBM surface. It supports the RGB and YUV graphic formats, as well as multiple plane graphic buffers.

- [Hardware Acceleration](hw-acceleration.md)

  You can enable hardware acceleration for the application. When the hardware acceleration is active, it increases rendering performance and allows you to use OpenGL&reg; ES smoothly.

- [OpenGL&reg; ES](opengl.md)

  You can create OpenGL&reg; ES applications in Tizen with the EGL&trade; layer. Tizen native applications can use OpenGL&reg; ES not only for creating a 3D scene but also for a 2D scene that requires fast interaction. OpenGL&reg; ES is also good for improving performance and reducing power consumption when the native application performs computation-intensive tasks that can be run in parallel.

## Related Information
- Dependencies
  - Since Tizen 2.4
