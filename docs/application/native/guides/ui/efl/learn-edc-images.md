# Images Block

The `images` block is used to list the image files used in the theme. The used compression methods are also defined here. In addition to the top level, the `images` blocks can be included inside other blocks, usually `collections`, `group`, and `part`. Using the `images` block on the top level makes file list maintenance easier when the theme is split among multiple files.

**Figure: Images block**

![Images block](./media/diagram_images.png)

```
images {
   image: "filename1.ext" COMP;
   image: "filename2.ext" LOSSY 99;
   set {}
   set {}
}
```

- `image [image file] [compression method] (compression level)`  

  This property is included for each image file. The full path to the directory holding the image can be defined later with the `edje_cc` tool's `-id` option. The available compression methods are:
  - `RAW`: Uncompressed
  - `COMP`: Lossless compression
  - `LOSSY [0-100]`: JPEG lossy compression with quality from 0 to 100
  - `USER`: Not embedded in the file, refer to an external file instead

- `images.set` block

  ```
  set {
     name: "image_name_used";
     image {}
     image {}
  }
  ```

  The `set` block is used to define an image with different content depending on its size. In addition to the top level, the `set` blocks can be included inside other blocks, normally `collections`, `group`, and `part`. Using the `set` block on the top level makes file list maintenance easier when the theme is split among multiple files.

  - `name [image name]`

    Sets the name of this image description.

  - `images.set.image` block

    ```
    image {
       image: "filename4.ext" COMP;
       size: 51 51 200 200;
       border: 0 0 0 0;
       border_scale_by: 0.0;
    }
    ```

    The `image` block defines the characteristics of an image. Every block describes one image and the size rule to use it. For full details, see [Image](./learn-edc-part.md#description_image).

    - `image [image file] [compression method] (compression level)`  

      This property is included for each image file. The full path to the directory holding the image can be defined later with the `edje_cc` tool's `-id` option.

    - `size [minw] [minh] [maxw] [maxh]`  

      Sets the minimum and maximum size that selects a specific image.

    - `border [left] [right] [top] [bottom]`  

      If set, the width (in pixels) of each side of the image is displayed as a fixed size border, from the side inwards, preventing the corners from being changed on a resize.

    - `border_scale_by [value]`  

      If border scaling is enabled, normally the output border sizes scale accordingly. For example, if 3 pixels on the left edge are set as a border, then normally at scale 1.0, those 3 columns are always the exact 3 columns of output, or at scale 2.0 they are 6 columns, or 0.33 they merge into a single column. This property multiplies the input scale factor by this multiplier, allowing the creation of supersampled borders to enable higher resolution outputs by always using the highest resolution artwork and then at runtime scaling it down. Valid values are: 0.0 or bigger (0.0 or 1.0 to switch it off).

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
