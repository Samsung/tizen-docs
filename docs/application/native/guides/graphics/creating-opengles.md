# Creating OpenGL&reg; ES Applications


The easiest way to use the OpenGL&reg; ES API in a Tizen application is to rely on the `Elm_GLView` component. The `Elm_GLView` component is one of the Elementary UI components, which creates an OpenGL&reg; ES target surface and a context. The `Elm_GLView` component can be embedded in any Tizen UI application. It is basically a wrapper of `Evas_GL`, the OpenGL&reg;/EGL™ abstraction layer of EFL. By using the `Elm_GLView` component, you avoid having to consider how the EGL™ environment is coupled with the native windowing systems. Some macros provided by EFL also allow you to use OpenGL&reg; ES APIs directly. In addition, the UI framework can access the surface where the GPU outputs the rendering result and make the entire scene as a combination of 2D and 3D components on a single canvas.

The following example shows the steps to create an OpenGL&reg; ES application. From now on, the `Elm_GLView` component is shortened to GLView.

1. Create a basic application as presented in the [mobile](../../getting-started/mobile/first-app.md#create) and [wearable](../../getting-started/wearable/first-app.md#create) Tizen first application example.

   The UI application's skeleton makes available the window object, which can contain the GLView component.

2. Enable hardware acceleration.

   To develop an OpenGL&reg; ES application, call the `elm_config_accel_preference_set()` function before creating the window. It makes an application use the GPU.

   For developing an application with Elementary, create a window with the `elm_win_util_standard_add()` Elementary utility function.

   ```
   Evas_Object *win;
   elm_config_accel_preference_set("opengl");
   win = elm_win_util_standard_add(name, "OpenGL example");
   ```

   You must also set hardware acceleration in the manifest file. For more information, see [Hardware Acceleration](hw-acceleration.md).

3. Initialize the GLView.

   After creating the window, you can set the GLView mode with the `elm_glview_mode_set()` function to enable alpha channel, depth buffer, stencil buffer, MSAA, and the client-side rotation features. The following modes are supported:

   - `ELM_GLVIEW_ALPHA`: Enable the alpha channel for rendering.
   - `ELM_GLVIEW_DEPTH`: Enable the depth buffer for rendering.
   - `ELM_GLVIEW_STENCIL`: Enable the stencil buffer for rendering.
   - `ELM_GLVIEW_MULTISAMPLE_LOW`: Use MSAA with a minimum number of samples.

   For more information, see the `Elm_GLView_Mode` enumerator (in [mobile](../../api/mobile/latest/group__Elm__GLView.html#ga4d0a2281e13c66d7274987ef24e7abe7) and [wearable](../../api/wearable/latest/group__Elm__GLView.html#ga4d0a2281e13c66d7274987ef24e7abe7) applications).

   In the following example, the alpha channel and depth buffer are enabled.

   ```
   /* Request a surface with alpha and a depth buffer */
   elm_glview_mode_set(glview, ELM_GLVIEW_ALPHA | ELM_GLVIEW_DEPTH);
   ```

   Additionally, you can select the policies for resizing and rendering. The following example shows how to decide what to do with the OpenGL&reg; ES surface when the GLView component is resized. With the default `ELM_GLVIEW_RESIZE_POLICY_RECREATE` option, the OpenGL&reg; ES surface is destroyed and created again with the new size. The resizing policy can also be set to `ELM_GLVIEW_RESIZE_POLICY_SCALE`. In that case, only the image object is scaled, not the underlying OpenGL&reg; ES surface.

   ```
   /*
      Resize policy tells GLView what to do with the surface when it
      resizes. ELM_GLVIEW_RESIZE_POLICY_RECREATE tells it to
      destroy the current surface and recreate it to the new size
   */
   elm_glview_resize_policy_set(glview, ELM_GLVIEW_RESIZE_POLICY_RECREATE);
   ```

4. Get the OpenGL&reg; ES function pointer.

   Originally, an application must call the OpenGL&reg; ES APIs using the `Evas_GL` abstraction layer in EFL. It means that you must get a set of function pointers for abstract OpenGL&reg; ES functions from the `Evas_GL` object and call functions through the object. This can be annoying, especially when you want to reuse OpenGL&reg; ES parts implemented at other platforms. To resolve this problem, EFL provides convenient helper macros, which are defined in the `Elementary_GL_Helpers.h` header file. The following example shows how to use the macros.

   ```
   #include <Elementary_GL_Helpers.h>
   ELEMENTARY_GLVIEW_GLOBAL_DEFINE();

   static Evas_Object*
   add_glview(Evas_Object* parent, appdata_s *ad)
   {
       Evas_Object* glview;

       /* Create and initialize GLView */
       glview = elm_glview_add(parent);

       /* Prepare to use OpenGL ES APIs directly */
       ELEMENTARY_GLVIEW_GLOBAL_USE(glview);
   }
   ```

   The `ELEMENTARY_GLVIEW_GLOBAL_DEFINE()` and `ELEMENTARY_GLVIEW_GLOBAL_USE()` macros must be in the same source code. If you have a global header file in your application, the `ELEMENTARY_GLVIEW_GLOBAL_DECLARE()` macro can be in the header file. However, you must be very careful when using these macros. The recommended solution is to use the `ELEMENTARY_GLVIEW_USE()` macro in every client function. The following are some situations where you must not use the helper macros:

   - When you use more than one Evas canvas at a time, such as multiple windows.
   - If you use multiple OpenGL&reg; ES APIs, such as OpenGL&reg; ES 1.1, OpenGL&reg; ES 2.0, and OpenGL&reg; ES 3.0.
   - If you write or port a library that can be used by other applications.

   The helper macros must be used only for the following situations:

   - When a single surface is used for OpenGL&reg; ES rendering.
   - When a single API set (either OpenGL&reg; ES 1.1, OpenGL&reg; ES 2.0, or OpenGL&reg; ES 3.0) is used. In this case, the `ELEMENTARY_GLVIEW_GLOBAL_DECLARE()` macro must be used in a global header for the application.

5. Set up callback functions.

   When you use the GLView component, you can set up necessary callback functions, which are called in the main loop to render a scene.

   ```
   /* Initialization callback */
   elm_glview_init_func_set(glview, init_glview);
   /* Resizing callback */
   elm_glview_resize_func_set(glview, resize_glview);
   /* Drawing callback */
   elm_glview_render_func_set(glview, draw_glview);
   /* Deletion callback */
   elm_glview_del_func_set(glview, del_glview);
   ```

   1. Set up the initialization callback.

      The initialization callback is called when the GLView is created.

      ```
      /* OpenGL ES init callback */
      static void
      init_glview(Evas_Object *glview)
      {
          /* Set OpenGL ES state color to pink */
          glClearColor(1.0, 0.2, 0.6, 1.0);

          /* Do any form of OpenGL ES initialization here */
          /* init_shaders(); */
          /* init_vertices(); */
      }
      ```

   2. Set up the resizing callback.

      The resizing callback is called whenever the GLView component is resized. A common action is to reset the viewport. Because the GLView size can be changed by a parent container, you must set up a resizing callback and reset the viewport size with the new GLView size.

      ```
      /* GLView resize callback */
      static void
      resize_glview(Evas_Object *glview)
      {
          int w;
          int h;
          elm_glview_size_get(glview, &w, &h);
          glViewport(0, 0, w, h);
      }
      ```

   3. Set up the drawing callback.

      The drawing callback is called whenever the GLView must be updated. The OpenGL&reg; ES draw commands must be made here.

      ```
      /* OpenGL ES draw callback */
      static void
      draw_glview(Evas_Object *glview)
      {
          /* Paint it pink */
          glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

          /* Usual OpenGL ES draw commands come here */
          /* draw_scene(); */
      }
      ```

   4. Set up the deletion callback.

      The deletion callback is triggered when the GLView is being destroyed. No other callback can be called on the same object afterwards.

      ```
      /* GLView deletion callback */
      static void
      del_glview(Evas_Object *glview)
      {
          /* Destroy all the OpenGL ES resources here */
          /* destroy_shaders(); */
          /* destroy_objects(); */
      }
      ```

> **Note**
>
> If the OpenGL&reg; ES functions are called outside the 4 GLView callback functions, you must call the `evas_gl_make_current()` function before the OpenGL&reg; ES function is called. However, this results in a performance degradation due to context switching, and only works if the direct rendering mode is not used.
>
> If Direct Rendering is enabled, all OpenGL&reg; ES functions must be called from the 4 GLView callback functions only. All other operations can break the rendering order and cause unexpected rendering.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
