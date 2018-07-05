# SVG Rendering



SVG (Scalable Vector Graphics) defines vector-based graphics in XML format. SVG graphics do not lose any quality when they are zoomed or resized.

Dali SVG rendering covers the following core features:

- Basic shapes and paths
- Solid and gradient color fill
- Solid color stroke, and stroke line cap and line join

Other SVG features, such as gradient color stroke, text, clip path, and animation, are not supported.

For more information on the SVG features, see [SVG Tiny 1.2 Specification](https://www.w3.org/TR/SVGTiny12).

## SVG Rendering Methods

You can render an SVG image on screen with DALi with both C++ and JSON. You can render an image in 2 ways:

- Use the SVG URL to create an `ImageView` object (in [mobile](../../../api/mobile/latest/classDali_1_1Toolkit_1_1ImageView.html) and [wearable](../../../api/wearable/latest/classDali_1_1Toolkit_1_1ImageView.html) applications).

  You can show the SVG image in a C++ file or, without using C++, write the JSON representations in a style sheet.

  ```
  // C++ example, use ImageView to render the SVG image
  ImageView myImageView = ImageView::New( "source-image-url.svg" );
  Stage::GetCurrent().Add( myImageView );

  // JSPN example, use ImageView to render SVG
  {"stage":[
    {
      "type": "ImageView",
      "image": { "url", "ome-image-url.svg" }
    }
  ] }
  ```

- Create a control, generate a property map with the SVG URL as the `ImageVisual::Property::URL` key value, and set it to `Control::Property::BACKGROUND`.

  You can show the SVG image in a C++ file or, without using C++, write the JSON representations in a style sheet.

  ```
  // C++ example, set SVG image as control background
  Control myControl = Control::New();
  Property::Map backgroundMap;
  backgroundMap[ImageVisual::Property::URL] = "source-image-url.svg";
  myControl.SetProperty( Control::Property::BACKGROUND, backgroundMap );
  Stage::GetCurrent().Add( myControl );

  // JSON example, set SVG image as control background
  {"stage":[
    {
      "type": "Control",
      "background": { "url", "some-image-url.svg" }
    }
  ] }
  ```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
