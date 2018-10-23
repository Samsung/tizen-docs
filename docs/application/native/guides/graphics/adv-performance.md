# Advanced Performance


The following general principles can help you to resolve performance problems on Tizen devices. (Some principles are valid for general embedded systems.)

The first 2 principles are very basic, but still quite important, since the CPU-GPU bandwidth and memory capacity of embedded systems are limited in general.

1. As presented in [Polygon Mesh in OpenGL&reg; ES](polygon-mesh.md), although the vertex array is intuitive, it is inefficient to use only the vertex array. It is almost always recommended to use an **index array** and the `glDrawElements()` function. This reduces the amount of data transferring from CPU to GPU. The bigger the model is, the more efficient the index array approach is.
2. If the polygon mesh is not frequently changed, you can use **vertex buffer objects** (VBO) in order to cache the data into the GPU memory, as illustrated in [Uniforms and Attributes in OpenGL&reg; ES](vertex-shader.md#uniforms_attributes).
3. In general, you do not need to call the `glFinish()` function. As drawing commands are requested by the `draw_glview()` callback and are executed in the background, it is enough to call the `glFlush()` function at the end of the `draw_glview()` callback.
4. You are not required to clear every buffer, or to clear them at the same time. Instead, you can obtain the best performance by calling the `glClear()` function once per frame with all the buffers to be simultaneously cleared.
5. Do not create and destroy the graphic resources (such as textures and FBO) per frame. You can create and store them in the `app_data` structure in the `init_glview()` callback and reuse them later.
6. Try to avoid using the `if` statement in the shader code. Since the vertex and fragment shaders are executed in parallel (in batches) on most GPU architectures, `if-then-else` statement can block some other batches to determine which one can be run next. It means that parallel processing cannot be fully implemented.
7. Try to avoid writing a heavy fragment shader. If the same data apply to all fragments, do not compute the data in the fragment shader but compute them at the CPU side and provide them as uniforms. On the other hand, whenever the data can be computed at the vertex shader, use it.
8. In general, the `glReadPixels()` function is quite slow, because it reinforces CPU-GPU synchronization, drastically decreasing the overall performance. In most cases, it is possible to obtain the desired result with the framebuffer object (FBO), avoiding the use of `glReadPixels()`. With FBO, you can access the pixels of the framebuffer (the output of GPU processing) through a texture object (render-to-texture). Since it uses texture data from a GPU stage to another GPU stage, CPU does not have to be synchronized. If the application must use the `glReadPixels()`function, use another thread to avoid blocking the main thread.
9. With FBO, various effects can be made. Consider an application requiring a number of rendering chains for making a complex effect: A framebuffer is mapped to a texture, the texture is used to render another framebuffer, the framebuffer is mapped to another texture, and so on. This enables you to create a very complex scene, but unfortunately the rendering chain cannot be parallelized. Make the rendering chains as small as possible.
10. According to the [application life-cycle](../app-management/efl-ui-app.md#state_trans), the application gets the `app_pause()` callback when the application runs in the background. Then, you must stop calling drawcalls during the pause state.

    As presented in [Interactive UI](interactive-ui.md), the application can control the rendering loop by using an animator internally and then stop the animator in the `app_pause()` callback.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
