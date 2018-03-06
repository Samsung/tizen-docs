# Maps and Map Service


Map service features include geocoding, reverse geocoding, place searching, route calculation, and view widgets.

The main Tizen.Maps namespace features are:

-   Discovering and selecting a map provider

    You can also [specify basic maps preferences](#start).

-   Geocoding and reverse geocoding

    You can [get the geocode](#geocode) (geographical coordinates) of a place from an address, or the reverse geocode (address) from the geographical coordinates (latitude and longitude).

-   Searching places

    You can [query place information](#search_place), corresponding to specified search keys and filters.

-   Searching routes

    You can [query a route](#search_route) that defines a path between a start and destination point, passing optionally through specific intermediate locations and calculated using a specified transportation method.

-   Managing a map view widget

    With the [map view widget feature](#view), you can [create a map view widget](#maps_view) and set various properties (such as theme, language, and traffic).

    You can create objects, such as markers, polylines and polygons, in the widget. You can also receive responses about events over the widget, and get various data from the events.

You can also [customize service requests](#preference).

The following map providers are supported:

-   [HERE Maps](https://developer.here.com) based on the [HERE REST API](https://developer.here.com/rest-apis).

    To use the HERE Maps, set the provider name to "HERE" and [get the HERE API keys](here-credentials.md).


> **Note**   
> To use the map service, you must get an access key to the map provider from the provider developer site. The service must be used according to the provider's Term of Use.

<a name="geocode"></a>
## Geocodes

The following geocode request types are provided:

-   Get place coordinates from a free text address.
-   Get place coordinates from a free text address within a specified geographical area.
-   Get place coordinates from a structured address (a structure with fields, such as city, street, and building number).

After performing the [geocode service request](#use_geocode), you receive the geocode response, which is a geographical location, specified with latitude and longitude values.

Only 1 type of reverse geocode request is provided:

-   Get a structured address from place coordinates.

You can parse the reverse geocode response to use its details. The response contains structured address information consisting of, for example, a street name, building number, city name, postal code, district name, state name, and country.

<a name="search_place"></a>
## Place Search

The following place search request types are provided:

-   Query place information within a specific distance around a specified geographical location.
-   Query place information within a specified geographical area.
-   Query place information from a free text address within a specified geographical area.

After performing the [place service request](#use_search_place), you receive the place search response. You can parse the place search response to use its details. The response contains structured place information consisting of, for example, a place ID, name and URL, address, geographical location and distance from the center of the search area, place category, rating, review, and image.


> **Note**   
> Depending on the map provider, some types of place information can be unavailable.

<a name="search_route"></a>
## Route Search

The following route search request types are provided:

-   Query a route from a starting point to a destination specified as a geographical location.
-   Query a route passing through a number of geographical locations.

After performing the [route service request](#use_search_route), you receive the route search response. You can parse the route calculation response to use its details. The response contains structured route information consisting of, for example, a route ID, geographical coordinates of the start and destination points, route bounding box, transportation mode, and total distance and duration.


> **Note**   
> Depending on the map provider, the route can be presented as a list of geographical points or segments. The segment list can also be presented as a list of geographical points or maneuvers.

<a name="view"></a>
## Map View Widget

The map view widget feature includes drawing a map image on the map port, which is a specified rectangular area of the map application UI.

With the widget, you can:

-   Show, move, and resize the widget.
-   Set the map view widget theme.
-   Enable a 3D building.
-   Enable traffic information.
-   Enable a scalebar.
-   Set a language for the widget.

You can [create objects in the widget](#maps_object). The following view object types are provided:

-   Marker based on a specified geographical location, image, and marker type.
-   Polyline based on specified geographical locations, color, and width.
-   Polygon based on specified geographical locations and color.

The object properties can be changed after the object has been created.

The map view and map object can [handle events](#maps_event). Each object has handlers to invoke callbacks for selected events of the [Tizen.Maps.MapObject](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapObject.html) and [Tizen.Maps.MapView](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapView.html) classes:

-   Gestures
    -   `Tizen.Maps.MapView.Scrolled`: Scroll gesture is detected over the widget.
    -   `Tizen.Maps.MapView.TwoFingerZoomed`: Two-finger zoom gesture is detected over the widget.
    -   `Tizen.Maps.MapView.Clicked`: Click gesture is detected over the widget.
    -   `Tizen.Maps.MapView.DoubleClicked`: Double-click gesture is detected over the widget.
    -   `Tizen.Maps.MapView.TwoFingerClicked`: Two-finger click gesture is detected over the widget.
    -   `Tizen.Maps.MapView.TwoFingerRotated`: Two-finger rotation gesture is detected over the widget.
    -   `Tizen.Maps.MapView.LongPressed`: Long-press gesture is detected over the widget.
-   Others
    -   `Tizen.Maps.MapView.ViewReady`: Map view widget is ready.


> **Note**   
> To use the map view on Xamarin.Forms, use Xamarin.Forms.Maps.


## Prerequisites

To enable your application to use the map service functionality:

1.  To use the [Tizen.Maps](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/mapservice</privilege>
       <privilege>http://tizen.org/privilege/internet</privilege>
       <privilege>http://tizen.org/privilege/network.get</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Maps namespace, include it in your application:

    ```
    using Tizen.Maps;
    ```

<a name="start"></a>
## Starting the Map Service

To start using the map service:

1.  The [Tizen.Maps.MapService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapService.html) instance relies on a particular map provider. To get a list of available map providers, use the `Providers` property of the `Tizen.Maps.MapService` class:

    ```
    var providerList = MapService.Providers;

    foreach (var provider in providerList)
    {
        Log.Info("Tizen.Maps", $"Available Provider Name = {provider}");
    }
    ```

2.  Create a `Tizen.Maps.MapService` class instance using the provider name and provider key issued by the map provider:

    ```
    var maps = new MapService("MAPS_PROVIDER_NAME", "Your-Maps-Provider-Key");
    ```

3.  You must make sure that the device user has consented to allow the map provider to use their location information. Depending on the map provider, a UI window to get user consent can be shown on the screen.

    If the consent request returns `false`, you cannot use most of the methods and properties of the Tizen.Maps namespace.

    ```
    bool isConsented = await maps.RequestUserConsent();
    Log.Info("Tizen.Maps", $"User consent = {isConsented}");
    ```

4.  Check which services are supported by the [selected map provider](#supported_maps) using the `IsSupported()` method of the `Tizen.Maps.MapService` class:

    ```
    /// Check whether routing is available
    bool isRoutingSupported = maps.IsSupported(ServiceRequestType.SearchRoute);

    /// Check whether routing through specified waypoints is available
    bool isRoutingWaypointsSupported = maps.IsSupported(ServiceRequestType.SearchRouteWithWaypoints);
    ```

    To check for the availability of other services, follow the same approach using the keys from the [Tizen.Maps.ServiceRequestType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.ServiceRequestType.html) enumerator.

5.  Optionally, check which data features are available for the desired services using the same `IsSupported()` method:

    ```
    /// Check whether route path data is supported
    bool isRoutePathSupported = maps.IsSupported(ServiceData.RoutePath);

    /// Check whether segment path data is supported
    bool isRouteSegmentsPathSupported = maps.IsSupported(ServiceData.RouteSegmentsPath);

    /// Check whether segment maneuver data is supported
    bool isRouteSegmentsManeuversSupported = maps.IsSupported(ServiceData.RouteSegmentsManeuvers);
    ```

    To check the availability of other data features, follow the same approach using the keys from the [Tizen.Maps.ServiceData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.ServiceData.html) enumerator.

<a name="use_geocode"></a>
## Using Geocode and Reverse Geocode Services

To retrieve a geocode of a specified place, or the place information corresponding to given geographic coordinates, use one of the following approaches. The service requests can be [customized](#preference).

To retrieve a geocode:

-   To retrieve a geocode, use a string of free-formed address for the `CreateGeocodeRequest()` method of the [Tizen.Maps.MapService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapService.html) object:

    ```
    try
    {
        var request = maps.CreateGeocodeRequest("Seoul, Seoul R&D Campus");
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", result.ToString());
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To retrieve a geocode inside a specified area, use a string and an instance of the [Tizen.Maps.Area](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.Area.html) object for the `CreateGeocodeRequest()` method of the `Tizen.Maps.MapService` object:

    ```
    try
    {
        var area = new Area(new Geocoordinates(12.980260, 77.60653), new Geocoordinates(12.96738, 77.697405));
        var request = maps.CreateGeocodeRequest("Bangalore", area);
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", result.ToString());
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To retrieve places specified as a structured address, use an instance of the [Tizen.Maps.PlaceAddress](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.PlaceAddress.html) object for the `CreateGeocodeRequest()` method of the `Tizen.Maps.MapService` object:

    ```
    try
    {
        var address = new PlaceAddress
        {
            Building = "Ub City", City = "Bengaluru", PostalCode = "560025", Country = "India"
        };
        var request = maps.CreateGeocodeRequest(address);
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", result.ToString());
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

To retrieve a reverse geocode:

-   To retrieve a reverse geocode of specified geographic coordinates, use latitude and longitude for the `CreateReverseGeocodeRequest()` method of the `Tizen.Maps.MapService` object:

    ```
    try
    {
        var request = maps.CreateReverseGeocodeRequest(12.975491, 77.697182);
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", result.ToString());
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To retrieve reverse geocodes of specified multiple geographic coordinates, use the `CreateMultiReverseGeocodeRequest()` method of the `Tizen.Maps.MapService` object:

    ```
    try
    {
        var request = maps.CreateMultiReverseGeocodeRequest(new List<Geocoordinates>
        {
            new Geocoordinates(12.975491, 77.697182),
            new Geocoordinates(48.85784, 2.29516),
        });
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", result.ToString());
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="use_search_place"></a>
## Using the Place Search Service

To search for a place with a diversity of search parameters, use one of the following approaches. The service requests can be [customized](#preference).

-   To retrieve places within a specified distance around the center coordinates, use an instance of the [Tizen.Maps.Geocoordinates](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.Geocoordinates.html) object for the `CreatePlaceSearchRequest()` method of the [Tizen.Maps.MapService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapService.html) object:

    ```
    try
    {
        var request = maps.CreatePlaceSearchRequest(new Geocoordinates(48.85784, 2.29516), 50);
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", string.Format("Name=\"{0}\", Distance={1}m, Position={2}",
                                                 result.Name, result.Distance, result.Coordinates));
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To retrieve places within a specified geographic boundary, use an instance of the [Tizen.Maps.Area](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.Area.html) object for the `CreatePlaceSearchRequest()` method of the `Tizen.Maps.MapService` object:

    ```
    try
    {
        var request = maps.CreatePlaceSearchRequest(new Area(new Geocoordinates(12.980260, 77.697405), 500));
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", string.Format("Name=\"{0}\", Distance={1}m, Position={2}",
                                                 result.Name, result.Distance, result.Coordinates));
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To retrieve places based on an address within a specified geographic boundary, use a string of free-formed address and an instance of the `Area` object for the `CreatePlaceSearchRequest()` method of the `Tizen.Maps.MapService` object:

    ```
    try
    {
        var request = maps.CreatePlaceSearchRequest("The Taj Mahal Palace", new Area(new Geocoordinates(18.921729, 72.833031), 50));
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", string.Format("Name=\"{0}\", Distance={1}m, Position={2}",
                                                 result.Name, result.Distance, result.Coordinates));
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="use_search_route"></a>
## Using the Routing Service

To query a route from point A to point B, use one of the following approaches. The service requests can be [customized](#preference).

-   To query a route from one set of geographic coordinates to another:

    ```
    try
    {
        var request = maps.CreateRouteSearchRequest(new Geocoordinates(12.975491, 77.697182),
                                                    new Geocoordinates(12.990647, 77.687907));
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", $"From={result.Origin}");
            foreach (var path in result.Path)
            {
                Log.Info("Tizen.Maps", $"Path={path.ToString()}");
            }
            Log.Info("Tizen.Maps", $"To  ={result.Destination}");
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To query a route passing through a specified set of waypoints:

    ```
    try
    {
        var request = maps.CreateRouteSearchRequest(new Geocoordinates(12.975491, 77.697182),
                                                    new Geocoordinates(12.990647, 77.687907));
        request.Waypoints = new List<Geocoordinates>()
        {
            new Geocoordinates(12.985043, 77.691285)
        };
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", $"From={result.Origin}");
            foreach (var path in result.Path)
            {
                Log.Info("Tizen.Maps", $"Path={path.ToString()}");
            }
            Log.Info("Tizen.Maps", $"To  ={result.Destination}");
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

<a name="preference"></a>
## Customizing the Service Requests

All map service requests can be customized with additional preferences. Preparing and sending the `preference` parameter with the service request allows the map provider to generate more accurate results.

To customize the service request:

-   The example from [Using the Place Search Service](#use_search_place) can be modified as follows to include the customized preferences:

    ```
    try
    {
        maps.Preferences = new SearchPreference
        {
            MaxResults = 10, Unit = DistanceUnit.Yard
        };
        var request = maps.CreatePlaceSearchRequest("store", new Area(new Geocoordinates(37.5758418, 126.982763), 50));
        var response = await request.GetResponseAsync();
        foreach (var result in response)
        {
            Log.Info("Tizen.Maps", string.Format("Name=\"{0}\", Distance={1} yard(s), Position={2}",
                                                 result.Name, result.Distance, result.Coordinates));
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To prepare preferences for the routing service, use the [Tizen.Maps.SearchPreference](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.SearchPreference.html) or [Tizen.Maps.IRouteSearchPreference](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.IRouteSearchPreference.html) methods.

    The example from [Using the Routing Service](#use_search_route) can be modified as follows to include the customized preferences:

    ```
    try
    {
        maps.Preferences = new SearchPreference
        {
            Mode = TransportMode.Car
        };
        var request = maps.CreateRouteSearchRequest(new Geocoordinates(12.975491, 77.697182),
                                                    new Geocoordinates(12.990647, 77.677907));
        var response = await request.GetResponseAsync();
        var route = response.First();
        foreach (var segment in route.Segments)
        {
            foreach (var maneuver in segment.Maneuvers)
            {
                Log.Info("Tizen.Maps", string.Format("Position={0}, Instruction={1} ",
                                                     maneuver.Position, maneuver.Instruction));
            }
        }
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

If your map provider requires any specific preferences, use the `Tizen.Maps.SearchPreference` class with key-value pairs defined in the appropriate map provider documentation.

<a name="maps_view"></a>
## Using the Map View

To use the map view:

1.  Before you use the view features, create a [Tizen.Maps.MapView](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapView.html) instance:

    ```
    try
    {
        window = new Window("Test");
        mapview = new MapView(window, maps);

        mapview.Resize(w, h - 100);
        mapview.Move(0, 100);
        mapview.Show();
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

2.  Set the map view properties:
    -   Set the map view type with the `MapType` property of the `Tizen.Maps.MapView` class.

        For other available types, see the [Tizen.Maps.MapTypes](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapTypes.html) enumerator.

        ```
        mapview.MapType = MapTypes.Satellite;
        ```

    -   Set the 3D building of the map view with the `BuildingsEnabled` property:

        ```
        mapview.BuildingsEnabled = true;
        ```

    -   Set the public transit information of the map view with the `PublicTransitEnabled` property:

        ```
        mapview.PublicTransitEnabled = true;
        ```

    -   Set the map view traffic information with the `TrafficEnabled` property:

        ```
        mapview.TrafficEnabled = true;
        ```

    -   Set the map view scalebar with the `ScaleBarEnabled` property:

        ```
        mapview.ScaleBarEnabled = true;
        ```

    -   Set the map view language with the `Language` property:

        ```
        mapview.Language = "en-US";
        ```



    > **Note**   
	> To check whether a feature is supported, use `IsSupported()` method of the [Tizen.Maps.MapService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapService.html) class with the [Tizen.Maps.ServiceData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.ServiceData.html) enumerator.



3.  Set the map view location and size:

    Set the map view location with the `Resize()` method of the `Tizen.Maps.MapView` class, inherited from the `EvasObject` class:

    ```
    mapview.Resize(400, 800);
    ```

    You can also set the location with the `Move()` method of the `Tizen.Maps.MapView` class, inherited from the `EvasObject` class:

    ```
    mapview.Move(0, 0);
    ```

    Set the map view visibility with the `Show()` method of the `Tizen.Maps.MapView` class, inherited from the `EvasObject` class:

    ```
    mapview.Show();
    ```

4.  Set the map view center with the `Center` property:

    ```
    mapview.Center = new Geocoordinates(37.5758418, 126.982763);
    ```

5.  Set the map view orientation with the `Orientation` property:

    ```
    mapview.Orientation = 45.0;
    ```

6.  Set the map view zoom level with the `ZoomLevel`, `MinimumZoomLevel`, and `MaximumZoomLevel` properties:

    ```
    mapview.ZoomLevel = 12;
    ```

<a name="maps_object"></a>
## Creating Map View Objects

You can create polyline, polygon, and marker objects for the map view.

To create a map view object:

-   To create a polyline:

    ```
    try
    {
        var coordinatesList = new List<Geocoordinates>
        {
            new Geocoordinates(37.15, 126.88), new Geocoordinates(37, 127.12),
            new Geocoordinates(36.523, 127.20)
        };
        var color = new ElmSharp.Color(255, 1, 1);
        var thick = 5;
        Polyline polyline = new Polyline(coordinatesList, color, thick);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To create a polygon:

    ```
    try
    {
        var coordinatesList = new List<Geocoordinates>
        {
            new Geocoordinates(37.15, 126.88), new Geocoordinates(37, 127.12),
            new Geocoordinates(36.85, 126.99), new Geocoordinates(37, 126.79)
        };
        var color = new ElmSharp.Color(50, 200, 50, 128);
        Polygon polygon = new Polygon(coordinatesList, color);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

-   To create a marker:

    ```
    Pin pin = new Pin(new Geocoordinates(28.64362, 77.19865));
    Sticker sticker = new Sticker(new Geocoordinates(28.64362, 77.19865));
    ```

    To create a marker using a customized image:

    ```
    Pin pin = new Pin(new Geocoordinates(28.64362, 77.19865), "image/marker_pin.png");
    Sticker sticker = new Sticker(new Geocoordinates(28.64362, 77.19865), "image/marker_sticker.png");
    ```

To add a map view object to a map view widget:

1.  Add the object instance to the map view with the `Add()` method of the [Tizen.Maps.MapView](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Maps.MapView.html) class:

    ```
    mapview.Add(pin);
    ```

2.  When no longer needed, remove the instance with the `Remove()` method of the `Tizen.Maps.MapView` class:

    ```
    mapview.Remove(pin);
    ```

<a name="maps_event"></a>
## Managing Map View Events

To handle map view events:

1.  Register an event handler, which is triggered when map view events occur:

    ```
    EventHandler<MapGestureEventArgs> handler = (s, e) =>
    {
        Log.Info("Tizen.Maps", $"DoubleClicked={e.Position} {e.Geocoordinates}");
    };
    mapview.DoubleClicked += handler; /// Double-click gesture is enabled
    ```

    After the gesture handler is added, the gesture is enabled. Exceptionally, the click gesture is always enabled.

2.  When no longer needed, unset the event handler:

    ```
    /// Double-click gesture is disabled, if there is no handler added
    mapview.DoubleClicked -= handler;
    ```

To handle map object events:

1.  Register an event handler, which is triggered when map object events occur:

    ```
    Pin pin = new Pin(new Geocoordinates(37, 127), s_imagePath);
    EventHandler handler = (s, e) => {
        Pin myPin = (Pin)s;
        Log.Info("Tizen.Maps", $"Position={myPin.Coordinates.ToString()}");
    };
    pin.Clicked += handler;
    ```

2.  When no longer needed, unset the event handler:

    ```
    /// When the pin object no longer needs to accept click gestures
    pin.Clicked -= handler;
    ```

To handle map view ready events:

1.  Register an event handler, which is triggered when map view ready events occur:

    ```
    EventHandler handler = (s, e) =>
    {
        Log.Info("Tizen.Maps", "Map view is ready.");
    };
    mapview.ViewReady += handler;
    ```

2.  When no longer needed, unset the event handler:

    ```
    /// Map view ready event is disabled
    mapview.ViewReady -= handler;
    ```

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
