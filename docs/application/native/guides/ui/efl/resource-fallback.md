# Resource Fallback Support

Tizen native applications can run on different types of devices, such as wearable, phone, tablet, and TV. Tizen also supports various resolutions (WVGA ~ XQXGA) and resources. To take advantage of these features, you can handle resources in the [Resource Manager](../../../../tizen-studio/native-tools/resource-manager.md) view in the Tizen Studio.

In addition to the possibilities provided by the **Resource Manager** view, you can use Edje to provide sets of alternative images in your application.

The image set elements are used to display a specific image on the screen depending on the container size. The image set is used to control the resource quality when the image part is scaled to multiple devices. According to the size of the part's container, an appropriate image is loaded.

The image sets can have the following properties:

- `image: image-name`

  Specifies the name of the image file.

- `size: minw minh maxw maxh`

  Specifies the minimum and maximum size that causes a specified image to be selected and shown.

**Example: Image set implementation**

 ![Image set](./media/fallback_imageset.png)

```
collections {
   group {
      name: "property_test";

      images {
         set {
            name: "alternative_animal";
            image {
               image: "pig.png" COMP;
               size: 640 800 1200 1500;
            }
            image {
               image: "monkey.png" COMP;
               size: 400 500 639 799;
            }
            image {
               image: "cat.png" COMP;
               size: 240 300 399 499;
            }
            image {
               image: "mouse.png" COMP;
               size: 80 100 239 299;
            }
            image {
               image: "snail.png" COMP;
               size: 0 0 79 99;
            }
         }
      }

      parts {
         part {
            name: "image1";
            description {
               state: "default" 0.0;
               rel1 {relative: 0.0 0.0;}
               rel2 {relative: 1.0 0.45;}
               image.normal: "alternative_animal";
               aspect: 4/5 4/5;
               aspect_preference: BOTH;
            }
         }
         part {
            name: "image2";
            description {
               state: "default" 0.0;
               rel1 {relative: 0.0 0.5;}
               rel2 {relative: 1.0 0.75;}
               image.normal: "alternative_animal";
               aspect: 4/5 4/5;
               aspect_preference: BOTH;
            }
         }
         part {
            name: "image3";
            description {
               state: "default" 0.0;
               rel1 {relative: 0.0 0.8;}
               rel2 {relative: 1.0 1.0;}
               image.normal: "alternative_animal";
               aspect: 4/5 4/5;
               aspect_preference: BOTH;
            }
         }
      }
   }
}
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
