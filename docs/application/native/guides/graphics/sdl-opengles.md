# SDL Graphics with OpenGL&reg; ES


OpenGL&reg; ES is a standard specification defining a cross-language, cross-platform API for writing applications that produce 2D and 3D computer graphics. Tizen supports OpenGL&reg; ES versions 1.1, 2.0, 3.0, 3.1, and 3.2. For general information on OpenGL&reg;ES, and the comparative merits of Vulkan&reg; and OpenGL&reg;, see the official Khronos [OpenGL&reg; ES Web site](https://www.khronos.org/opengles/) and [Vulkan&reg; vs. OpenGL&reg;](sdl.md#vulkan_vs_opengles).

**Figure: OpenGL&reg; ES in Tizen**

![opengles in Tizen](./media/sdl_opengles.png)

The main OpenGL ES API features include [rendering 3D objects in an SDL application](#render).

## Prerequisites

To enable your application to use the OpenGL&reg; ES functionality:

1. To use OpenGL&reg; ES for 3D rendering, you must create an SDL application, and understand both [OpenGL&reg; ES](https://www.khronos.org/opengles/) and [SDL](https://www.libsdl.org/).

2. Check whether the device supports a specific version of OpenGL&reg; ES.

   Check for device support using the `system_info_get_platform_bool()` function, before using the OpenGL ES APIs. If the device can support the specific OpenGL&reg; ES version, the function returns `true` in the second parameter.

   ```
   bool opengles_support;
   /* Check support for the OpenGL ES 2.0 version */
   system_info_get_platform_bool("http://tizen.org/feature/opengles.version.2_0", &opengles_support);
   ```

3. To use the functions and data types of the OpenGL ES (in [mobile](../../api/mobile/latest/group__OPENSRC__OPENGLES__FRAMEWORK.html) and [wearable](../../api/wearable/latest/group__OPENSRC__OPENGLES__FRAMEWORK.html) applications) and SDL (in [mobile](../../api/mobile/latest/group__OPENSRC__SDL__FRAMEWORK.html) and [wearable](../../api/wearable/latest/group__OPENSRC__SDL__FRAMEWORK.html) applications) APIs, include the `<SDL.h>` header file and the appropriate OpenGL&reg; ES version header file in your application:

    ```
    #include <SDL.h>
    /* Header file for the OpenGL ES 2.0 version */
    #include <GLES2/GLES2.h>
    ```

**Table: OpenGL&reg; ES feature keys and header files**

| Version        | Feature key                              | Header file                              |
|----------------|------------------------------------------|------------------------------------------|
| OpenGL&reg; ES 1.1 | `http://tizen.org/feature/opengles.version.1_1` | `<GLES/GLES.h>` or `<SDL_opengles.h>`    |
| OpenGL&reg; ES 2.0 | `http://tizen.org/feature/opengles.version.2_0` | `<GLES2/GLES2.h>` or `<SDL_opengles2.h>` |
| OpenGL&reg; ES 3.0 | `http://tizen.org/feature/opengles.version.3_0` | `<GLES3/GLES3.h>`                        |
| OpenGL&reg; ES 3.1 | `http://tizen.org/feature/opengles.version.3_1` | `<GLES3/GLES3.h>`                        |
| OpenGL&reg; ES 3.2 | `http://tizen.org/feature/opengles.version.3_2` | `<GLES3/GLES3.h>`                        |

<a name="render"></a>
## Rendering a Cube with OpenGL&reg; ES

To render a cube using OpenGL&reg; ES in an SDL application:

1. Initialize the SDL library and create the SDL window.

   Before using any other SDL functions, call the `SDL_Init()` function to properly initialize the SDL library and start each of its various subsystems. The function accepts as a parameter a set of allowed flags combined using the "|" pipe operation.

   After SDL is initialized successfully, create the `SDL_Window` instance using the `SDL_CreateWindow()` function. The parameters define the title of the window, the X and Y position coordinates, width, height, and a set of `SDL_WindowFlags` combined using the "|" pipe operation.

   > **Note**
   >
   > To use the OpenGL&reg; ES context, use the `SDL_WINDOW_OPENGL` flag when you create a window. Do not use both `SDL_WINDOW_VULKAN` and `SDL_WINDOW_OPENGL` simultaneously.

   The `SDL_main()` function is mandatory for the Tizen framework to initialize the SDL application. You must use the `SDL_main()` function instead of the usual `main()` function in your SDL application.

   ```
   int
   SDL_main(int argc, char *argv[])
   {
       SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS);
       demo.sdl_window = SDL_CreateWindow("SDL OpenGL ES Sample", 0, 0, demo.sdl_mode.w, demo.sdl_mode.h,
                                          SDL_WINDOW_SHOWN | SDL_WINDOW_FULLSCREEN | SDL_WINDOW_OPENGL);
   }
   ```

2. Initialize the OpenGL&reg; ES context:

   1. Set the context properties using the [available attributes](#attributes):

      ```
      int
      initGL(appdata_s* ad)
      {
          SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_ES);
          SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2);
          SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
          SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1);
          SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1);
          SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
      ```

   2. Create the context:

      ```
          /* Create context for OpenGL window */
          ad->gl = SDL_GL_CreateContext(ad->window);
          if (ad->gl == NULL) {
              SDL_LogInfo(SDL_LOG_CATEGORY_APPLICATION, "[SDL] GL context creation failed!");

              return (-1);
          }

          /* Set context as current */
          SDL_GL_MakeCurrent(ad->window, ad->gl);

          return (0);
      }
      ```

3. Initialize the shaders, identity matrix, and buffer.

   Shaders are created and compiled in the `init_shaders()` function, and attached to the `glProgram` object.

   The `generateAndBindBuffer()` function creates a vertex buffer object, which is managed using the `glGenBuffers()`, `glBindBuffer()`, and `glBufferData()` functions.

   ```
   /* Initialize shaders */
   init_shaders(&ad);

   /* Initialize matrix for camera view */
   init_matrix(ad.view);

   /* Generate and bind vertex buffer object */
   generateAndBindBuffer(&(ad.vbo));
   ```

4. Calculate the view aspect ratio and apply an orthographic matrix.

   The aspect ratio determines the field of view in the X direction, and is the ratio of X (width) to Y (height).

   ```
   float aspect = (ad.mode.w > ad.mode.h ? (float)ad.mode.w / ad.mode.h : (float)ad.mode.h / ad.mode.w);
   if (ad.mode.w > ad.mode.h)
       view_set_ortho(ad.view, -1.0 * aspect, 1.0 * aspect, -1.0, 1.0, -1.0, 100.0);
   else
       view_set_ortho(ad.view, -1.0, 1.0, -1.0 * aspect, 1.0 * aspect, -1.0, 100.0);
   ```

5. To draw the scene:

   1. Clear the buffer.

      The `glClear()` function clears buffers to preset values. The function accepts as a parameter a set of allowed flags, indicating the buffers to be cleared, combined using the "|" pipe operation. The available flags are `GL_COLOR_BUFFER_BIT`, `GL_DEPTH_BUFFER_BIT`, `GL_ACCUM_BUFFER_BIT`, and `GL_STENCIL_BUFFER_BIT`.

      The `glClearColor()` function specifies the `red`, `green`, `blue`, and `alpha` values used when the color buffers are cleared.

      ```
      void
      drawScene(appdata_s* ad)
      {
          glViewport(0, 0, ad->w, ad->h);
          glClearColor(0.5f, 0.5f, 0.5f, 1.0f);
          glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
      ```

   2. Render the scene:

      ```
          init_matrix(ad->model);
          rotate_xyz(ad->model, ad->anglePoint.x, ad->anglePoint.y, ad->window_rotation);

          multiply_matrix(ad->mvp, ad->view, ad->model);
          glUseProgram(ad->program);

          glBindBuffer(GL_ARRAY_BUFFER, ad->vbo);
          glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(float) * 6, 0);
          glEnableVertexAttribArray(0);

          glBindBuffer(GL_ARRAY_BUFFER, ad->vbo);
          glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, sizeof(float) * 6, (void*)(sizeof(float) * 3));
          glEnableVertexAttribArray(1);

          glUniformMatrix4fv(glGetUniformLocation(ad->program, "mvpMatrix"), 1, GL_FALSE, ad->mvp);

          /* Render primitives from array data*/
          glDrawArrays(GL_TRIANGLES, 0, 36);

      ```

   3. Update the OpenGL&reg; rendering window:

      ```
          SDL_GL_SwapWindow(ad->window);
      }
      ```

6. Quit SDL.

   Before exiting the application, destroy the SDL objects:

   ```
   SDL_Quit();
   ```

<a name="attributes"></a>
## OpenGL&reg; Context Attributes

The following table lists the attributes whose values can be set using the `SDL_GL_SetAttribute()` function.

**Table: OpenGL&reg; context attributes**

| Attribute                           | Description                              | Default value           |
|-------------------------------------|------------------------------------------|-------------------------|
| `SDL_GL_ACCELERATED_VISUAL`         | Set to 1 to require hardware acceleration; set to 0 to force software rendering<br> In Tizen, hardware acceleration is used regardless of the value set to this attribute. | -                       |
| `SDL_GL_ACCUM_ALPHA_SIZE`           | Minimum number of bits for the accumulation buffer alpha channel | 0                       |
| `SDL_GL_ACCUM_BLUE_SIZE`            | Minimum number of bits for the accumulation buffer blue channel | 0                        |
| `SDL_GL_ACCUM_GREEN_SIZE`           | Minimum number of bits for the accumulation buffer green channel | 0                        |
| `SDL_GL_ACCUM_RED_SIZE`             | Minimum number of bits for the accumulation buffer red channel | 3                       |
| `SDL_GL_ALPHA_SIZE`                 | Minimum number of bits for the color buffer alpha channel | 0                       |
| `SDL_GL_BLUE_SIZE`                  | Minimum number of bits for the color buffer blue channel | 2                       |
| `SDL_GL_BUFFER_SIZE`                | Minimum number of bits for the frame buffer | 0                       |
| `SDL_GL_CONTEXT_FLAGS`              | Combination of 0 or more elements of the `SDL_GLcontextFlag` enumeration |           0              |
| `SDL_GL_CONTEXT_MAJOR_VERSION`      | OpenGL&reg; context major version            | -                       |
| `SDL_GL_CONTEXT_MINOR_VERSION`      | OpenGL&reg; context minor version            | -                         |
| `SDL_GL_CONTEXT_PRIORITY`           | Allow a GL context to be created with a priority hint |  -                       |
| `SDL_GL_CONTEXT_PROFILE_MASK`       | Type of GL context (Core, Compatibility, ES) | Depends on the platform |
| `SDL_GL_CONTEXT_RELEASE_BEHAVIOR`   | Set the context release behavior (since SDL 2.0.4) | 1                       |
| `SDL_GL_DEPTH_SIZE`                 | Minimum number of bits for the depth buffer | 16                      |
| `SDL_GL_DOUBLEBUFFER`               | Whether the output is double-buffered    | 1 (Double-buffered)     |
| `SDL_GL_FRAMEBUFFER_SRGB_CAPABLE`   | Request sRGB-capable visuals (since SDL 2.0.1) | 0                       |
| `SDL_GL_GREEN_SIZE`                 | Minimum number of bits for the color buffer green channel | 3                       |
| `SDL_GL_MULTISAMPLEBUFFERS`         | Number of buffers used for multisample anti-aliasing | 0                       |
| `SDL_GL_MULTISAMPLESAMPLES`         | Number of samples around the current pixel used for multisample anti-aliasing |   0                       |
| `SDL_GL_RED_SIZE`                   | Minimum number of bits for the color buffer red channel | 3                       |
| `SDL_GL_SHARE_WITH_CURRENT_CONTEXT` | Whether OpenGL&reg; context sharing is enabled | 0                       |
| `SDL_GL_STENCIL_SIZE`               | Minimum number of bits for the stencil buffer | 0                         |
| `SDL_GL_STEREO`                     | Whether stereo 3D output is enabled      | `off`                   |

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
