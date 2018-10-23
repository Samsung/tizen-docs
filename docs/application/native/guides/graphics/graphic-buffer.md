# Graphic Buffer and Surface


The Tizen Buffer Manager (TBM) surface allows you to manage the graphic buffer in Tizen. The TBM provides an abstraction interface for the graphic buffer and a user interface for the TBM surface. It supports the RGB and YUV graphic formats, as well as multiple plane graphic buffers.

The TBM surface provides the following main features:

- [Creating a surface](#create) with a defined width, height, and format

  The TBM surface provides various format definitions. However, before using a specific graphic format, make sure that the system supports it.

- Getting a format list

- Accessing the surface

- Getting surface and plane information

  Get the details using the `tbm_surface_map()` or the `tbm_surface_get_info()` function. The surface information is assigned to the `tbm_surface_info_s` struct (in [mobile](../../api/mobile/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html#ga8d954dfd180e96cafbcfc7b92684b971) and [wearable](../../api/wearable/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html#ga8d954dfd180e96cafbcfc7b92684b971) applications).

  The surface information contains the surface width, height, BPP, size, and the number of planes, while the plane information includes the plane size, offset, stride, and pointer. For more information on the surface and plane details, see `_tbm_surface_info` struct (in [mobile](../../api/mobile/latest/struct__tbm__surface__info.html) and [wearable](../../api/wearable/latest/struct__tbm__surface__info.html) applications) and `_tbm_surface_plane` struct (in [mobile](../../api/mobile/latest/struct__tbm__surface__plane.html) and [wearable](../../api/wearable/latest/struct__tbm__surface__plane.html) applications).

To store data in the low-level graphic buffer, get a plane pointer in the surface and use the pointer of each plane.

## Prerequisites

To use the functions and data types of the TBM Surface API (in [mobile](../../api/mobile/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UI__TBM__SURFACE__MODULE.html) applications, include the `<tbm_surface.h>` header file in your application:

```
#include <tbm_surface.h>
```

<a name="create"></a>
## Managing the TBM Surface

To create the TBM surface:

1. Query the formats supported by the system using the `tbm_surface_query_formats()` function. Free the array of formats after viewing the formats.

    ```
    tbm_format *formats;
    uint32_t format_num;

    if (tbm_surface_query_formats(&formats, &format_num) != TBM_SURFACE_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get formats supported by the system\n");
    ```

2. Create the TBM surface (`tbm_surface`) and define its format, height, and width:

   ```
   int i;
   tbm_surface_h surface = NULL;

   for (i = 0; i < format_num; i++) {
       if (formats[i] == TBM_FORMAT_ARGB8888) {
           surface = tbm_surface_create(128, 128, TBM_FORMAT_ARGB8888);
           if (surface == NULL)
               dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create tbm_surface\n");
           break;
       }
   }
   if (i == format_num)
       dlog_print(DLOG_ERROR, LOG_TAG, "format not supported\n");
   ```

3. Map the TBM surface with the access option. After the surface is mapped, the `tbm_surface` information is saved in the `tbm_surface_info` structure:

   ```
   tbm_surface_info_s surface_info;

   if (tbm_surface_map(surface, TBM_SURF_OPTION_READ|TBM_SURF_OPTION_WRITE, &surface_info) != TBM_SURFACE_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "Failed to map tbm_surface\n");
   ```

4. Store data at the `tbm_surface` instance by using a pointer of each plane:

   ```
   for (i = 0; i < surface_info.num_planes; i++)
       memset(surface_info.planes[i].ptr, 0x0, surface_info.planes[i].size);
   ```

5. When no longer needed, unmap and destroy the `tbm_surface` instance:

    ```
    if (tbm_surface_unmap(surface) != TBM_SURFACE_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to unmap tbm_surface\n");
    if (tbm_surface_destroy(surface) != TBM_SURFACE_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to destroy tbm_surface\n");
    free(formats);
    ```


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
