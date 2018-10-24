# Media Handle Management


Your application can manage various media handles with media tools.

The main features of the Media Tool API include:

- Creating the media format handle

  You can [set and get video or audio information](#format) using the `media_format_h` handle.

- Creating the media packet handle

  You can [set and get metadata](#packet) using the created `media_packet_h` handle. Some `media_packet_h` metadata are NOT filled after creating the `media_packet_h` handle: pts, dts, duration, extradata, codec data, codec data size, and buffer flags.

The `media_format_h` handle is created by the caller, who can set and get the video or audio information. The `media_format_h` handle creates the `media_packet_h` handle and allocates the buffer. The caller can set and get the metadata with the `media_packet_h` handle.

The `media_format_h` handle has a specific design for increasing and decreasing its [reference count](#reference).

## Prerequisites

To enable your application to use the media tool functionality:

- To use the media format handle of the Media Tool API (in [mobile](../../api/mobile/latest/group__CAPI__MEDIA__TOOL__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MEDIA__TOOL__MODULE.html) applications), include the `<media_format.h>` header file in your application:

  ```
  #include <media_format.h>
  ```

- To use the media packet handle of the Media Tool API, include the `<media_packet.h>` header file in your application:

  ```
  #include <media_packet.h>
  ```
<a name="format"></a>
## Managing the Media Format Handle

To manage the media format handle:

1. Define a `media_format_h` variable for the media format handle, and pass the variable to the `media_format_create()` function, which returns the handle.

   To set the video information when creating the handle:

   ```
   media_format_h format;
   if (media_format_create(&format) == MEDIA_FORMAT_ERROR_NONE) {
       media_format_set_video_mime(format, MEDIA_FORMAT_H264_HP);
       media_format_set_video_width(format, 640);
       media_format_set_video_height(format, 480);
       media_format_set_video_avg_bps(format, 10000000);
       media_format_set_video_max_bps(format, 15000000);
   } else {
       printf("media_format_create() failed!");
   }
   ```

   To set the audio information, replace the `media_format_set_video_XXX()` functions with the relevant `media_format_set_audio_XXX()` functions in the above example code.

2. To retrieve the video format information, use the `media_format_get_video_info()` function:

   ```
   media_format_h fmt;

   media_format_mimetype_e mime;
   int w;
   int h;
   int avg_bps;
   int max_bps;

   if (media_format_get_video_info(fmt, &mimetype, &w, &h, &avg_bps, &max_bps) == MEDIA_PACKET_ERROR_NONE)
       printf("media_format_get_video_info success! width = %d, height = %d", w, h);
   else
       print("media_format_get_video failed...");
   ```

   To retrieve the audio format information, use the `media_format_get_audio_info()` function.

<a name="packet"></a>
## Managing the Media Packet Handle

To manage the media packet handle:

1. Define a `media_packet_h` variable for the media packet handle, and pass the variable to the appropriate `media_packet_create_XXX()` function (as the last parameter) with an existing media format handle (as the first parameter).

   After creating the media packet handle, call the `media_format_unref()` function for the media format handle. Because all functions that create a media packet handle increase the reference count of the media format handle, you must decrease the count.

   To reuse the media packet handle even after the `media_packet_destroy()` function is called, define a callback (the third last parameter of the `media_packet_create_XXX()` function), which is called when the handle is destroyed. Set the callback to return `MEDIA_PACKET_REUSE`.

   The following example codes show the different ways you create the media packet handle:

   - To create the handle and allocate a buffer into the heap or TBM surface, use the `media_packet_create_alloc()` function:

     ```
     {
         media_format_h fmt;
         media_packet_h packet;

         media_format_create(&fmt);
         media_format_set_video_mime(format, MEDIA_FORMAT_H264_HP);
         media_format_set_video_width(format, 640);
         media_format_set_video_height(format, 480);
         media_format_set_video_avg_bps(format, 10000000);
         media_format_set_video_max_bps(format, 15000000);

         /*
            MEDIA_FORMAT_H264_HP data type is MEDIA_FORMAT_ENCODED and the buffer
            is allocated into the heap
            If the data type is MEDIA_FORMAT_RAW,
            the buffer is allocated into the TBM surface
         */
         media_packet_create_alloc(fmt, _finalize_callback, fcb_data, &packet);
         media_format_unref(fmt);

         media_packet_destroy(packet);
     }

     int
     _finalize_callback(media_packet_h packet, int err, void* userdata)
     {
         return MEDIA_PACKET_REUSE;
     }
     ```

   - To create only the handle, use the `media_packet_create()` function:

     ```
     {
         media_format_h fmt;
         media_packet_h packet;

         media_format_create(&fmt);
         media_format_set_video_mime(format, MEDIA_FORMAT_H264_HP);
         media_format_set_video_width(format, 640);
         media_format_set_video_height(format, 480);
         media_format_set_video_avg_bps(format, 10000000);
         media_format_set_video_max_bps(format, 15000000);

         /* Only create the handle, do not allocate a buffer */
         media_packet_create(fmt, _finalize_callback, fcb_data, &packet);
         media_format_unref(fmt);
     }

     int
     _finalize_callback(media_packet_h packet, int err, void* userdata)
     {
         return MEDIA_PACKET_FINALIZE;
     }
     ```

   - To create the handle and store the TBM surface data, use the `media_packet_create_from_tbm_surface()` function:

     ```
     {
         media_format_h fmt;
         media_packet_h packet;

         media_format_create(&fmt);
         media_format_set_video_mime(format, MEDIA_FORMAT_RGBA);
         media_format_set_video_width(format, 128);
         media_format_set_video_height(format, 128);
         media_format_set_video_avg_bps(format, 10000000);
         media_format_set_video_avg_bps(format, 15000000);

         media_packet_create_from_tbm_surface(fmt, surface, _finalize_callback, fcb_data, &packet);
         media_format_unref(fmt);
     }

     int
     _finalize_callback(media_packet_h packet, int err, void* userdata)
     {
         return MEDIA_PACKET_FINALIZE;
     }
     ```

   - To create the handle with an already allocated external buffer, use the `media_packet_create_from_external_memory()` function:

     ```
     {
         media_format_h fmt;
         media_packet_h packet;

         media_format_create(&fmt);
         media_format_set_video_mime(format, MEDIA_FORMAT_H264_HP);
         media_format_set_video_width(format, 640);
         media_format_set_video_height(format, 480);
         media_format_set_video_avg_bps(format, 10000000);
         media_format_set_video_avg_bps(format, 15000000);

         media_packet_create_from_external_memory(fmt, mem_ptr, size, _finalize_callback, fcb_data, &packet);
         media_format_unref(fmt);
     }

     int
     _finalize_callback(media_packet_h packet, int err, void* userdata)
     {
         /* Do something */

         return MEDIA_PACKET_FINALIZE;
     }
     ```

2. Set and get the metadata with the media packet handle:

   ```
   int ret = MEDIA_PACKET_ERROR_NONE;

   /* format1 already exists */

   media_packet_create_alloc(format1, NULL, NULL, &packet);

   ret = media_packet_set_duration(packet, duration);

   /* After media_packet_get_format(), use media_format_unref() */
   media_format_h tmp;
   media_packet_get_format(packet, &tmp);
   media_format_unref(tmp);

   /* Set previously created format2 to packet */
   /* After media_packet_set_format(), use media_format_unref() */
   media_packet_set_format(packet, format2);

   /*
      Packet format is format2
      If format2 ref_count is 1, format2 is free
      If format2 ref_count is bigger than 1, it is not free
   */
   media_packet_destroy(packet);
   ```
<a name="reference"></a>
## Reference Count Design

The following table describes the reference count design of the `media_format_h` handle.

**Table: Media format handle reference count design**

| Function                                 | Reference count number                   | Description                              |
|------------------------------------------|------------------------------------------|------------------------------------------|
| `media_format_h fmt1, fmt2, tmp;`<br> `media_packet_h pkt1, pkt2;`<br> `media_format_create(&fmt1);` | `fmt1`: 1                                | Define the `media_format_h` and `media_packet_h` handles.<br> Create the `fmt1` handle and set the `media_format_video_mime()` or `media_format_audio_mime()` function. |
| `media_packet_create(&pkt1, fmt1);`      | `fmt1`: 2                                | After the `media_packet_create()` function, you must use the `media_format_unref()` function, because the `media_packet_create()` function increases the `media_format_h` reference count. |
| `media_format_unref(fmt1);`              | `fmt1`: 1                                | If the `ref_count` is 1, the `fmt1` is currently owned by the `pkt1` only. |
| `media_packet_copy(pkt1, &pkt2);`        | `fmt1`: 2                                | Copy the `pkt1` metadata to `pkt2`, except the allocated buffer and buffer size. `pkt2` refers to `fmt1`, and `fmt1` `ref_count` is increased. |
| `media_packet_get_format(pkt1, &tmp);`   | `fmt1`: 3                                | `fmt1` `ref_count` is increased by the `media_packet_get_format()` function. |
| `media_format_set_video_mime(tmp, ...);` | `fmt1`: 3                                | If you try to modify the `fmt1` data (call the `media_format_set_video_mime()` function) for `fmt1` (=`tmp`), the `ref_count` is bigger than 1, and `fmt1` cannot be modified.<br> To modify the `fmt1` data, call the `media_format_make_writable()` function. |
| `media_format_make_writable(tmp, &fmt2);` | `fmt1`: 2<br> `fmt2`: 1                       | If called, the `tmp` (`fmt1`) `ref_count` is decreased. Creates the `fmt2` handle and copies the `fmt1` data to `fmt2`. |
| `media_format_set_video_mime(fmt2, ...);` | `fmt1`: 2<br> `fmt2`: 1                       | `fmt2` `ref_count` is 1, which means that you can modify the `fmt2` data. |
| `media_packet_set_format(pkt2, fmt2);`   | `fmt1`: 2<br> `fmt2`: 2                      | Set the modified `fmt2` to the `pkt2` handle. You must call the `media_format_unref(fmt2)` function. |
| `media_format_unref(tmp);`               | `fmt1`: 1<br> `fmt2`: 2                      | You must call this function because of the `media_packet_get_format(pkt1, &tmp)` function call. |
| `media_format_unref(fmt2);`              | `fmt1`: 1<br> `fmt2`: 1                       | You must call this function because of the `media_packet_set_format(pkt2, fmt2)` function call. |
| `media_packet_destroy(pkt1);`            | `fmt1`: 1 > finalize<br> `fmt2`: 1            | If you destroy the `pkt1` handle, the `fmt1` `ref_count` is decreased. If the `ref_count` becomes 0, `fmt1` is freed. |
| `media_packet_destroy(pkt2);`            | `fmt1`: 1 > finalize<br> `fmt2`: 0 > finalize | If you destroy the `pkt2` handle, the `fmt2` `ref_count` is decreased. If the `ref_count` becomes 0, `fmt2` is freed. |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
