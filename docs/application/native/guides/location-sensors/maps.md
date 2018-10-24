# Maps and Maps Service

Map service features include geocoding, reverse geocoding, place searching, route calculation, and view widgets.

The main Maps Service API features are:

- Discovering and selecting a map provider

  You can also [specify basic maps preferences](#start).

- Geocoding and reverse geocoding

  You can [get the geocode](#geocode) (geographical coordinates) of a place from an address, or the reverse geocode (address) from the geographical coordinates (latitude and longitude).

- Searching places

  You can [query place information](#search_place), corresponding to specified search keys and filters.

- Searching routes

  You can [query a route](#search_route) that defines a path between a start and destination point, passing optionally through specific intermediate locations and calculated using a specified transportation method.

- Handling map service responses

  You can [receive responses from the map service](#response) through various callbacks.

- Managing a map view widget

  With the [map view widget feature](#view), you can [create a map view widget](#maps_view) and set various properties (such as theme, language, and traffic).

  You can create objects, such as markers, polylines and polygons, in the widget. You can also receive responses about events over the widget, and get various data from the events.

You can also [cancel service requests](#cancel) and [customize them](#preference).

The following map providers are supported:

- [HERE Maps](https://developer.here.com) based on the [HERE REST API](https://developer.here.com/rest-apis).

  To use the HERE Maps, you need to [get credentials](here-credentials.md).

> **Note**
>
> To use the map service, you must get an access key to the map provider from the provider developer site. The service must be used according to the provider's Term of Use.

<a name="geocode"></a>
## Geocodes

The following geocode request types are provided:

- Get place coordinates from a free text address.
- Get place coordinates from a free text address within a specified geographical area.
- Get place coordinates from a structured address (a structure with fields, such as city, street, and building number).

After performing the [geocode service request](#use_geocode), you receive the geocode response, which is a geographical location, specified with latitude and longitude values.

Only 1 type of reverse geocode request is provided:

- Get a structured address from place coordinates.

You can [parse the reverse geocode response](#address) to use its details. The response contains structured address information consisting of, for example, a street name, building number, city name, postal code, district name, state name, and country.

<a name="search_place"></a>
## Place Search

The following place search request types are provided:

- Query place information within a specific distance around a specified geographical location.
- Query place information within a specified geographical area.
- Query place information from a free text address within a specified geographical area.

After performing the [place service request](#use_search_place), you receive the place search response. You can [parse the place search response](#place) to use its details. The response contains structured place information consisting of, for example, a place ID, name and URL, address, geographical location and distance from the center of the search area, place category, rating, review, and image.

> **Note**
>
> Depending on the map provider, some types of place information can be unavailable.

<a name="search_route"></a>
## Route Search

The following route search request types are provided:

- Query a route from a starting point to a destination specified as a geographical location.
- Query a route passing through a number of geographical locations.

After performing the [route service request](#use_search_route), you receive the route search response. You can [parse the route calculation response](#route) to use its details. The response contains structured route information consisting of, for example, a route ID, geographical coordinates of the start and destination points, route bounding box, transportation mode, and total distance and duration.

> **Note**
>
> Depending on the map provider, the route can be presented as a list of geographical points or segments. The segment list can also be presented as a list of geographical points or maneuvers.

<a name="response"></a>
## Map Service Responses

The asynchronous map service responses are implemented with callback interfaces (functions whose names end with `cb`).

To handle the responses, you can use the map service response states:

- `MAPS_SERVICE_ERROR_NONE`: The map service is working correctly.
- `MAPS_ERROR_PERMISSION_DENIED`: The user has revoked a permission for the application to use the map service.
- `MAPS_ERROR_NOT_SUPPORTED`: The map request or feature you are trying to use is not supported in the map provider.
- `MAPS_ERROR_NETWORK_UNREACHABLE`, `MAPS_ERROR_SERVICE_NOT_AVAILABLE`, or `MAPS_ERROR_CONNECTION_TIME_OUT`: The map provider cannot access the map server for various reasons.

<a name="view"></a>
## Map View Widget

The map view widget feature includes drawing a map image on the map port, which is a specified rectangular area of the map application UI.

With the widget, you can:

- Show, move, and resize the widget.
- Set the map view widget theme.
- Enable a 3D building.
- Enable traffic information.
- Enable a scalebar.
- Set a language for the widget.

You can [create objects in the widget](#maps_object). The following view object types are provided:

- Marker based on a specified geographical location, image, and marker type.
- Polyline based on specified geographical locations, color, and width.
- Polygon based on specified geographical locations and color.

The object properties can be changed after the object has been created.

The map view widget can [handle events](#maps_event). The asynchronous view event responses are implemented with callback functions corresponding to the view event type:

- `MAPS_VIEW_EVENT_GESTURE`: User gesture is detected over the widget.
- `MAPS_VIEW_EVENT_ACTION`: Predefined action occurs.
- `MAPS_VIEW_EVENT_OBJECT`: Event occurs on the created object.
- `MAPS_VIEW_EVENT_READY`: Map view widget is ready.

Each event contains various data, and you can access the data with various `maps_view_event_data_get_XXX()` functions.

## Prerequisites

To enable your application to use the map service functionality:

1. To use the Maps Service API (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__SERVICE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__SERVICE__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/internet</privilege>
      <!--To use the map view-->
      <privilege>http://tizen.org/privilege/network.get</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Maps Service API, include the `<maps_service.h>` header file in your application:

   ```
   #include <maps_service.h>
   ```

3. To use the functions and data types of the View API (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__VIEW__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__VIEW__MODULE.html) applications), include the `<maps_view.h>` header file in your application:

   ```
   #include <maps_view.h>
   ```

<a name="start"></a>
## Starting the Map Service

To start using the map service:

1. The Maps Service instance relies on a particular map provider. To get a list of available map providers, use the `maps_service_foreach_provider()` function.

    ```
    static bool
    _maps_service_provider_info_cb(char* maps_provider, void* user_data)
    {
        /* Handle the map provider name, passed as maps_provider */

        return bool;
    }

    void
    get_available_providers()
    {
        void *user_data = NULL;
        const int error = maps_service_foreach_provider(_maps_service_provider_info_cb, user_data);

        if (error == MAPS_ERROR_NONE)
            /* Select a provider from the available_providers vector */
        else
            /* Error handling */
    }
    ```

2. Before you use the Maps Service API, create a Maps Service instance using the `maps_service_create()` function:

    ```
    maps_service_h maps = NULL;
    int error = maps_service_create("Maps Provider", &maps);
    ```

3. Set the security key appropriate to the selected map provider using the `maps_service_set_provider_key()` function:

    ```
    error = maps_service_set_provider_key(maps, "XXXYYYZZZ");
    ```

4. Check which services are supported by the selected map provider using the `maps_service_provider_is_service_supported()` function:

    ```
    bool supported = false;

    /* Check whether routing is available */
    error = maps_service_provider_is_service_supported(maps, MAPS_SERVICE_SEARCH_ROUTE, &supported);
    const bool is_routing_supported = (error == MAPS_ERROR_NONE) ? supported : false;

    /* Check whether routing through specified waypoints is available */
    error = maps_service_provider_is_service_supported(maps, MAPS_SERVICE_SEARCH_ROUTE_WAYPOINTS, &supported);
    const bool is_routing_waypoints_supported = (error == MAPS_ERROR_NONE) ? supported : false;
    ```

	To check for the availability of other services, follow the same approach using the keys from the `maps_service_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__SERVICE__AND__PREFERENCE__MODULE.html#ga8afd98ceb094d4c3edaf603051a69f8e) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__SERVICE__AND__PREFERENCE__MODULE.html#ga8afd98ceb094d4c3edaf603051a69f8e) applications).

5. Optionally, check which data features are available for the desired services using the `maps_service_provider_is_data_supported()` function:

    ```
    /* Check whether route path data is supported */
    error = maps_service_provider_is_data_supported(maps, MAPS_ROUTE_PATH, &supported);
    const bool is_route_path_supported = (error == MAPS_ERROR_NONE) ? supported : false;
    if (is_route_path_supported)
        /* Use route path */

    /* Check whether segment path data is supported */
    error = maps_service_provider_is_data_supported(maps, MAPS_ROUTE_SEGMENTS_PATH, &supported);
    const bool is_route_segment_path_supported = (error == MAPS_ERROR_NONE) ? supported : false;
    if (is_route_segment_path_supported)
        /* Use segment path */

    /* Check whether segment maneuver data is supported */
    error = maps_service_provider_is_data_supported(maps, MAPS_ROUTE_SEGMENTS_MANEUVERS, &supported);
    const bool is_route_segment_maneuvers_supported = (error == MAPS_ERROR_NONE) ? supported : false;
    if (is_route_segment_maneuvers_supported)
        /* Use segment maneuvers */
    ```

	To check the availability of other data features, follow the same approach using the keys from the `maps_service_data_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__SERVICE__AND__PREFERENCE__MODULE.html#ga8f22bd07fe9300b3f3f1c74e83f1e272) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__SERVICE__AND__PREFERENCE__MODULE.html#ga8f22bd07fe9300b3f3f1c74e83f1e272) applications).

6. Set general preferences, such as language and distance units, using the `maps_service_set_preference()` function:

   ```
   /* Create a preference set instance */
   maps_preference_h preference = NULL;
   int error = maps_preference_create(&preference);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */

   /* Set the distance unit preference */
   error = maps_preference_set_distance_unit(preference, MAPS_DISTANCE_UNIT_M);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */

   /* Set the language preference */
   error = maps_preference_set_language(preference, "en-US");
   if (error != MAPS_ERROR_NONE)
       /* Error handling */

   /* Apply the set of preferences for the map service */
   error = maps_service_set_preference(maps, preference);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */

   /* Destroy the preference set instance */
   error = maps_preference_destroy(preference);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */
   ```

   Optionally, you can set the maximum amount of search results and a default country code using the `maps_preference_set_max_results()` and `maps_preference_set_country_code()` functions.

   To set specific preferences for the map provider, use the `maps_preference_set_property()` function with key-value pairs, defined in the appropriate map provider documentation.

   To get the preferences currently applied in the map provider, use the following functions:

   - `maps_preference_get_distance_unit()`
   - `maps_preference_get_language()`
   - `maps_preference_get_max_results()`
   - `maps_preference_get_country_code()`
   - `maps_preference_get()` and `maps_preference_foreach_property()`

   These 2 functions retrieve the map provider-specific preferences not defined in the Maps Service API.

<a name="use_geocode"></a>
## Using Geocode and Reverse Geocode Services

To retrieve a geocode of a specified place, or the place information corresponding to given geographic coordinates, use one of the following approaches. The service requests can be [customized](#preference).

To retrieve a geocode:

1. Request the geocode:
   - Use the `maps_service_geocode()` function for a request based on a free-formed address:

    ```
    /* Search for geocode of the Samsung's campus "Digital City" in Suwon */
    error = maps_service_geocode(maps, "Suwon, Digital City", preference,
                                 __maps_service_geocode_cb, user_data, &request_id);

    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

   - Use the `maps_service_geocode_inside_area()` function for a request inside a specified area:

    ```
    maps_area_h bounds = NULL;
    /*
       Use maps_area_create_rectangle() or maps_area_create_circle()
       to create geographic bounds for geocoding
    */

    /* Search for geocode of the Digital City within a specified geographic area */
    error = maps_service_geocode_inside_area(maps, "Digital City", bounds, preference,
                                             __maps_service_geocode_cb, user_data, &request_id);

    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

   - Use the `maps_service_geocode_by_structured_address()` function for a request for a place, specified as a structured address:

    ```
    maps_address_h address = NULL;
    /* Use maps_address_create() to create an instance of an address */
    /* Then use maps_address_set_XXX() to initialize the address with values */

    /* Search for a geocode of a place, specified with a structured address */
    error = maps_service_geocode_by_structured_address(maps, address, preference, __maps_service_geocode_cb,
                                                       user_data, &request_id);


    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

2. Implement the `__maps_service_geocode_cb()` callback to receive the service response:

    ```
    static bool
    __maps_service_geocode_cb(maps_error_e result, int request_id, int index, int total,
                              maps_coordinates_h coordinates, void* user_data)
    {
        /* Handle the obtained coordinate data */

        /* Release the results */
        maps_coordinates_destroy(coordinates);

        return true;
    }
    ```

To retrieve a reverse geocode:

1. To retrieve a reverse geocode of specified geographic coordinates, use the `maps_service_reverse_geocode()` function:

    ```
    /* Obtain the reverse geocode with specified coordinates */
    error = maps_service_reverse_geocode(maps, 37.257865, 127.053659, preference,
                                         __maps_service_reverse_geocode_cb, user_data, &request_id);

    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

2. Implement the `__maps_service_reverse_geocode_cb()` callback to receive the service response:

    ```
    static void
    __maps_service_reverse_geocode_cb(maps_error_e result, int request_id, int index, int total,
                                      maps_address_h address, void* user_data)
    {
        /* Handle the obtained address */

        /* Release the results */
        maps_address_destroy(address);
    }
    ```

<a name="use_search_place"></a>
## Using the Place Search Service

To search for a place with a diversity of search parameters, use one of the following approaches. The service requests can be [customized](#preference).

- To search for a place:
  1. Search for a place:
     - Use the `maps_service_search_place()` function for a search within a specified distance around the center coordinates:

        ```
        maps_coordinates_h position = NULL;
        /* Create the coordinates with maps_coordinates_create() */

        int distance = 500;
        error = maps_service_search_place(maps, position, distance, filter, preference,
                                          __maps_service_search_place_cb, user_data, &request_id);

        if (error != MAPS_ERROR_NONE)
            /* Error handling */
        ```

     - Use the `maps_service_search_place_by_area()` function for a search for a place within a specified geographic boundary:

        ```
        maps_area_h boundary = NULL;
        /*
           Create the boundary with maps_area_create_rectangle()
           or maps_area_create_circle()
        */

        error = maps_service_search_place_by_area(maps, boundary, filter, preference,
                                                  __maps_service_search_place_cb, user_data, &request_id);

        if (error != MAPS_ERROR_NONE)
            /* Error handling */
        ```

     - Use the `maps_service_search_place_by_address()` function to search for a place based on an address within a specified geographic boundary:

        ```
        maps_area_h boundary = NULL;
        /*
           Create the boundary with maps_area_create_rectangle()
           or maps_area_create_circle()
        */

        error = maps_service_search_place_by_address(maps, "Digital City", boundary, filter, preference,
                                                     __maps_service_search_place_cb, user_data, &request_id);

        if (error != MAPS_ERROR_NONE)
            /* Error handling */
        ```

  2. Implement the `__maps_service_search_place_cb()` callback to receive the service response:

     ```
     static bool
     __maps_service_search_place_cb(maps_error_e error, int request_id, int index, int total,
                                    maps_place_h place, void* user_data)
     {
         /* Handle the obtained place data */

         /* Release the results */
         maps_place_destroy(place);

         return true;
     }
     ```

- To search for a list of places within a boundary, and get detailed information on a particular place:
  1. Search for a place list:
     - Use the `maps_service_search_place_list()` function for a search within a specified distance around the center coordinates:

        ```
        maps_area_h boundary = NULL;
        /*
           Create the boundary with maps_area_create_rectangle()
           or maps_area_create_circle()
        */

        error = maps_service_search_place_list(maps, boundary, filter, preference,
                                               __maps_service_search_place_list_cb, user_data, &request_id);

        if (error != MAPS_ERROR_NONE)
            /* Error handling */
        ```

     - Implement the `__maps_service_search_place_list_cb()` callback to receive the place list:

        ```
        static bool
        __maps_service_search_place_list_cb(maps_error_e error, int request_id, int total,
                                            maps_place_list_h place_list, void* user_data)
        {
            /* Handle the obtained place data */
            maps_place_list_foreach(place_list, __maps_place_details_cb, user_data);

            /* Release the results */
            maps_place_list_destroy(place_list);

            return true;
        }
        ```
     - Implement the `__maps_place_details_cb()` callback to receive the individual places within the place list:

        ```
        static bool
        __maps_place_details_cb(int index, maps_place_h place, void *user_data)
        {
            /* Handle the obtained place data */

            /* Get and store the URI to get the place details later */
            char *place_uri = NULL;
            maps_place_get_uri(place, &place_uri);

            /*
               Do not release the place handle,
               because it is only a reference to the list data
            */

            return true;
        }
        ```
  2. Get the place details:
     - Use the `maps_service_get_place_details()` function to retrieve the place details:

        ```
        error = maps_service_get_place_details(maps, place_uri,
                                               __maps_service_get_place_details_cb, user_data, &request_id);

        if (error != MAPS_ERROR_NONE)
            /* Error handling */
        ```

     - Implement the `__maps_service_get_place_details_cb()` callback to receive the details:

        ```
        static void
        __maps_service_get_place_details_cb(maps_error_e result, int request_id,
                                            maps_place_h place, void *user_data)
        {
            /* Handle the obtained place data */

            /* Release the results */
            maps_place_destroy(place);
        }
        ```

<a name="use_search_route"></a>
## Using the Routing Service

To query a route from point A to point B, use one of the following approaches. The service requests can be [customized](#preference).

To query a route:

1. Query the route:
   - Use the `maps_service_search_route()` function for a route from one set of geographic coordinates to another:

     ```
     maps_coordinates_h origin = NULL, destination = NULL;
     /* Create the coordinates with maps_coordinates_create() */

     error = maps_service_search_route(maps, origin, destination, preference,
                                       __maps_service_search_route_cb, user_data, &request_id);

     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - Use the `maps_service_search_route_waypoints()` function for a route passing through a specified set of waypoints:

     ```
     /* Specify the number of waypoints */
     const int waypoint_num = 5;

     /* Create an array with the waypoint coordinates */
     maps_coordinates_h* waypoint_list = NULL;

     error = maps_service_search_route_waypoints(maps, waypoint_list, waypoint_num, preference,
                                                 __maps_service_search_route_cb, user_data, &request_id);

     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

2. Implement the `__maps_service_search_route_cb()` callback to receive the service response:

    ```
    static bool
    __maps_service_search_route_cb(maps_error_e error, int request_id, int index, int total,
                                   maps_route_h route, void* user_data)
    {
        /* Handle the obtained route data */

        /* Release the results */
        maps_route_destroy(route);

        return true;
    }
    ```

<a name="cancel"></a>
## Canceling the Service Request

To cancel a geocode, place search, or routing request, use the `maps_service_cancel_request()` function:

```
/* Cancel the request with a specified ID */
error = maps_service_cancel_request(maps, request_id);

if (error != MAPS_ERROR_NONE)
    /* Error handling */
```

<a name="address"></a>
## Recognizing the Address Information

The result of the [reverse geocode request](#geocode) (`maps_service_reverse_geocode()`) is retrieved from the map service using the `maps_service_reverse_geocode_cb()` callback. The result is structured address data of the specified place.

Parse the address information using the following functions:

```
/* Obtain the building number */
char *building_number = NULL;
error = maps_address_get_building_number(address, &building_number);

if (error != MAPS_ERROR_NONE)
    /* Error handling */

/* Use the building_number */

free(building_number);

/* Obtain the street name */
char *street = NULL;
error = maps_address_get_street(address, &street);

if (error != MAPS_ERROR_NONE)
    /* Error handling */

/* Use the street name */

free(street);
```

Similarly, you can get other address features using the following functions:

- `maps_address_get_district()`
- `maps_address_get_city()`
- `maps_address_get_state()`
- `maps_address_get_country()`
- `maps_address_get_country_code()`
- `maps_address_get_county()`
- `maps_address_get_postal_code()`
- `maps_address_get_freetext()`

<a name="place"></a>
## Recognizing the Place Information

The result of the [place search request](#search_place) (`maps_service_search_place()`, `maps_service_search_place_by_area()`, or `maps_service_search_place_by_address()`) is retrieved from the map service using multiple iterations of the `maps_service_search_place_cb()` callback. The result is an instance of place data.

> **Note**
>
> Different map providers are capable of providing different sets of place data features. Some map providers can extend the place data features with extra properties that are not specified in the Maps Service API. Such properties are organized as a key-value storage where the keys are the names of the properties.
>
> If your map provider does not support a specific feature, the get function for the feature returns an error. To prevent problems, you can [check which data features are available](#start) in your map provider using the `maps_service_provider_is_data_supported()` function.

To parse place data:

1. To get the place information features, such as place name, location, and rating, use the following functions with a `maps_place_h` place handle:

   - To obtain the place name, use the `maps_place_get_name()` function:

     ```
     /* Obtain the place name */
     char *name = NULL;
     error = maps_place_get_name(place, &name);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */

     /* Use the place name */

     free(name);
     ```

   - To obtain the place location, use the `maps_place_get_location()` function:

     ```
     /* Obtain the place location */
     maps_coordinates_h location = NULL;
     error = maps_place_get_location(place, &location);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */

     /* Use the place location */

     maps_coordinates_destroy(location);
     ```

   - To obtain the place rating, use the `maps_place_get_rating()` function:

     ```
     /* Obtain the place rating */
     maps_place_rating_h rating = NULL;
     error = maps_place_get_rating(place, &rating);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */

     /* Use the place rating */

     maps_place_rating_destroy(rating);
     ```

   To obtain other place features, follow the same approach using the following functions:

   - `maps_place_get_id()`
   - `maps_place_get_address()`
   - `maps_place_get_distance()`
   - `maps_place_get_uri()`
   - `maps_place_get_supplier_link()`
   - `maps_place_get_related_link()`

2. To get lists of place information features, such as categories, reviews, and attributes, use the following iterating functions:

   1. To obtain a list of place categories, use the `maps_place_foreach_category()` function:

      ```
      /* Obtain a list of place categories */
      error = maps_place_foreach_category(place, __maps_place_categories_cb, user_data);
      if (error != MAPS_ERROR_NONE)
          /* Error handling */
      ```

   2. Implement the `__maps_place_categories_cb()` callback:

      ```
      static bool
      __maps_place_categories_cb(int index, int total, maps_place_category_h category, void* user_data)
      {
          /* Handle the obtained place category data */

          /* Release the results */
          maps_place_category_destroy(category);

          return true;
      }
      ```

   To obtain other place feature lists, follow the same approach using the following functions:

   - `maps_place_foreach_attribute()`
   - `maps_place_foreach_contact()`
   - `maps_place_foreach_editorial()`
   - `maps_place_foreach_image()`
   - `maps_place_foreach_review()`

3. To get the extra properties that some map providers provide to extend the place data features defined in the Maps Service API:

   1. To iterate through the retrieved extra properties, use the `maps_place_foreach_property()` function:

      ```
      /* Obtain the map provider-specific place data properties */
      error = maps_place_foreach_property(place, __maps_place_properties_cb, user_data);
      if (error != MAPS_ERROR_NONE)
          /* Error handling */
      ```

   2. Implement the `__maps_place_properties_cb()` callback:

      ```
      static bool
      __maps_place_properties_cb(int index, int total, char* key, void* value, void* user_data)
      {
          /* Handle the obtained property: */
          /* property_name: key */
          /* property_value: value */

          /* Release the property name and value */
          free(key);
          free(value);

          return true;
      }
      ```

<a name="route"></a>
## Recognizing the Route Information

The result of the [route calculation request](#search_route) (`maps_service_search_route()` or `maps_service_search_route_waypoints()`) is retrieved from the map service using multiple iterations of the `maps_service_search_route_cb()` callback. The result is an instance of route data.

> **Note**
>
> Different map providers are capable of providing different sets of route data features. Some map providers can extend the route data features with extra properties that are not specified in the Maps Service API. Such properties are organized as a key-value storage where the keys are the names of the properties.
>
> If your map provider does not support a specific feature, the get function for the feature returns an error. To prevent problems, you can [check which data features are available](#start) in your map provider using the `maps_service_provider_is_data_supported()` function.

To parse route data:

1. To get the route information features, such as route ID, origin, destination, and total distance, use the following functions with a `maps_route_h` place handle:

   - To obtain the route ID, use the `maps_route_get_route_id()` function:

     ```
     /* Obtain the route ID */
     char *id = NULL;
     error = maps_route_get_route_id(route, &id);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */

     /* Use the route ID */

     free(id);
     ```
   - To obtain the route origin and destination, use the `maps_route_get_origin()` and `maps_route_get_destination()` functions:

     ```
     /* Obtain the route origin and destination */
     maps_coordinates_h origin = NULL, destination = NULL;
     error = maps_route_get_origin(route, &origin);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     error = maps_route_get_destination(route, &destination);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */

     /* Use the route origin and destination */

     maps_coordinates_destroy(origin);
     maps_coordinates_destroy(destination);
     ```

   - To obtain the route total distance, use the `maps_route_get_total_distance()` function:

     ```
     /* Obtain the total route distance */
     double total_distance = .0;
     error = maps_route_get_total_distance(route, &total_distance);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */

     /* Use the total route distance */
     ```

   To obtain other route features, follow the same approach using the following functions:

   - `maps_route_get_bounding_box()`
   - `maps_route_get_transport_mode()`
   - `maps_route_get_total_duration()`
   - `maps_route_get_distance_unit()`
   - `maps_place_get_supplier_link()`
   - `maps_place_get_related_link()`

2. To get lists of route information features, such as path or list of segments, use the following iterating functions:

   - To obtain the list of geographic points defining the route, use the `maps_route_foreach_path()` function:

     ```
     error = maps_route_foreach_path(route, __maps_route_path_cb, user_data);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

	 Implement the `__maps_route_path_cb()` callback:

     ```
     static bool
     __maps_route_path_cb(int index, int total, maps_coordinates_h coordinates, void* user_data)
     {
         /* Handle the obtained route path coordinates */

         /* Release the results */
         maps_coordinates_destroy(coordinates);

         return true;
     }
     ```

   - To obtain the list of route segments, use the `maps_route_foreach_segment()` function:

     ```
     error = maps_route_foreach_segment(route, __maps_route_segment_cb, user_data);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */`
     ```

     Implement the `__maps_route_segment_cb()` callback:

     ```
     static bool
     __maps_route_segment_cb(int index, int total, maps_route_segment_h segment, void* user_data)
     {
         /* Handle the obtained route segment */

         /* Release the results */
         maps_route_segment_destroy(segment);

         return true;
     }
     ```

3. To get the extra properties that some map providers provide to extend the route data features defined in the Maps Service API:

   1. To iterate through the retrieved extra properties, use the `maps_route_foreach_property()` function:

       ```
       /* Obtain the map provider-specific route data properties */
       error = maps_route_foreach_property(route, __maps_route_properties_cb, user_data);
       if (error != MAPS_ERROR_NONE)
           /* Error handling */
       ```

   2. Implement the `__maps_route_properties_cb()` callback:

       ```
       static bool
       __maps_route_properties_cb(int index, int total, char* key, void* value, void* user_data)
       {
           /* Handle the obtained property: */
           /* property_name: key */
           /* property_value: value */

           /* Release the property name and value */
           free(key);
           free(value);

           return true;
       }
       ```

<a name="preference"></a>
## Customizing the Service Requests

All Maps Service API requests can be customized with additional preferences. Preparing and sending the `preference` parameter with the service request allows the map provider to generate more accurate results.

To customize the service request:

- To prepare preferences for the place search service, use the `maps_preference_set_property()` function with the following keys:
	- `MAPS_PLACE_FILTER_TYPE`
	- `MAPS_PLACE_FILTER_SORT_BY`

  The example from [Using the Place Search Service](#search_place) can be modified as follows to include the customized preferences:
  ```
  /* Create extra preferences for the place search service */
  error = maps_preference_create(&preference);
  if (error != MAPS_ERROR_NONE)
      /* Error handling */
  error = maps_preference_set_property(preference, MAPS_PLACE_FILTER_TYPE, "restaurant");
  if (error != MAPS_ERROR_NONE)
      /* Error handling */

  maps_coordinates_h position = NULL;
  /* Create the coordinates with maps_coordinates_create() */

  int distance = 500;
  error = maps_service_search_place(maps, position, distance, filter, preference,
                                    __maps_service_search_place_cb, user_data, &request_id);

  if (error != MAPS_ERROR_NONE)
      /* Error handling */

  maps_preference_destroy(preference);
  ```

- To prepare preferences for the routing service, use the following functions:

  - `maps_preference_set_route_optimization()`
  - `maps_preference_set_route_transport_mode()`
  - `maps_preference_set_route_feature_weight()`
  - `maps_preference_set_route_feature()`

  You can also use the `maps_preference_set_property()` function with the following keys:

  - `MAPS_ROUTE_FREEFORM_ADDR_TO_AVOID`
  - `MAPS_ROUTE_STRUCTED_ADDR_TO_AVOID`
  - `MAPS_ROUTE_CIRCLE_AREA_TO_AVOID`
  - `MAPS_ROUTE_RECT_AREA_TO_AVOID`
  - `MAPS_ROUTE_GEOMETRY_BOUNDING_BOX`
  - `MAPS_ROUTE_GEOMETRY_RETRIEVAL`
  - `MAPS_ROUTE_INSTRUCTION_GEOMETRY`
  - `MAPS_ROUTE_INSTRUCTION_BOUNDING_BOX`
  - `MAPS_ROUTE_INSTRUCTION_RETRIEVAL`
  - `MAPS_ROUTE_REALTIME_TRAFFIC`

  The example from [Using the Routing Service](#search_route) can be modified as follows to include the customized preferences:

  ```
  /* Create extra preferences for the routing service */
  error = maps_preference_create(&preference);
  if (error != MAPS_ERROR_NONE)
      /* Error handling */
  error = maps_preference_set_property(preference, MAPS_ROUTE_FREEFORM_ADDR_TO_AVOID, "Suwon, Digital City");
  if (error != MAPS_ERROR_NONE)
      /* Error handling */
  error = maps_preference_set_route_optimization(preference, MAPS_ROUTE_TYPE_SHORTEST);
  if (error != MAPS_ERROR_NONE)
      /* Error handling */

  maps_coordinates_h origin = NULL, destination = NULL;
  /* Create the coordinates with maps_coordinates_create() */

  error = maps_service_search_route(maps, origin, destination, preference,
                                    __maps_service_search_route_cb, user_data, &request_id);

  if (error != MAPS_ERROR_NONE)
      /* Error handling */

  maps_preference_destroy(preference);
  ```

If your map provider requires any specific preferences, use the `maps_preference_set_property()` function with key-value pairs defined in the appropriate map provider documentation.

<a name="maps_view"></a>
## Using the Map View

To use the map view:

1. Before you use the View API (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__VIEW__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__VIEW__MODULE.html) applications), create a map view instance using the `maps_view_create()` function:

    ```
    maps_view_h maps_view = NULL;
    /* Create an image object for the map view */
    Evas_Object *evas_object_image = evas_object_image_filled_add(evas_object_evas_get(window));

    error = maps_view_create(maps, evas_object_image, &maps_view);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

2. Set the map view properties:

   - Set the map view type with the `maps_view_set_type()` function.

     For other available types, see the `_maps_view_type_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__VIEW__MODULE.html#ga379898d515d81cf500a814571524f106) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__VIEW__MODULE.html#ga379898d515d81cf500a814571524f106) applications).

     ```
     error = maps_view_set_type(maps_view, MAPS_VIEW_TYPE_NORMAL);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - Set the 3D building of the map view with the `maps_view_set_buildings_enabled()` function:

     ```
     error = maps_view_set_buildings_enabled(maps_view, true);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - Set the map view traffic information with the `maps_view_set_traffic_enabled()` function:

     ```
     error = maps_view_set_traffic_enabled(maps_view, true);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - Set the map view scalebar with the `maps_view_set_scalebar_enabled()` function:

     ```
     error = maps_view_set_scalebar_enabled(maps_view, true);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - Set the map view language with the `maps_view_set_language()` function:

     ```
     error = maps_view_set_language(maps_view, "eng");
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

3. Set the map view location and size:

   Set the map view location with the `maps_view_set_screen_location()` function:

   ```
   error = maps_view_set_screen_location(maps_view, 0, 100, 500, 1000);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */
   ```

   You can also set the location with the `maps_view_move()` and `maps_view_resize()` functions:

   ```
   error = maps_view_move(0, 100);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */

   error = maps_view_resize(500, 1000);
   if (error != MAPS_ERROR_NONE)
       /* Error handling */
   ```

4. Set the map view visibility with the `maps_view_set_visibility()` function:

    ```
    error = maps_view_set_visibility(maps_view, true);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

5. Set the map view center with the `maps_view_set_center()` function:

    ```
    maps_coordinates_h maps_coord = NULL;

    maps_coordinates_create(28.64362, 77.19865, &maps_coord);

    error = maps_view_set_center(maps_view, maps_coord);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */

    maps_coordinates_destroy(maps_coord);
    ```

6. Set the map view zoom level with the `maps_view_set_zoom_level()` function:

    ```
    error = maps_view_set_zoom_level(maps_view, 12);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

7. When no longer needed, destroy the map view instance with the `maps_view_destroy()` function:

    ```
    maps_view_destroy(maps_view);
    ```
<a name="maps_object"></a>
## Creating Map View Objects

You can create polyline, polygon, and marker objects for the map view.

> **Note**
>
> Before you use the View Object API (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__VIEW__OBJECT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__VIEW__OBJECT__MODULE.html) applications), create a map view object instance.

To create a map view object:

1. Create a map view object:

   - To create a polyline:

     ```
     maps_view_object_h object = NULL;
     maps_coordinates_h coord1 = NULL, coord2 = NULL;
     maps_coordinates_list_h coord_list = NULL;

     maps_coordinates_list_create(&coord_list);
     maps_coordinates_create(28.64362, 77.19865, &coord1);
     maps_coordinates_list_append(coord_list, coord1);
     maps_coordinates_create(28.634418, 77.169080, &coord2);
     maps_coordinates_list_append(coord_list, coord2);

     error = maps_view_object_create_polyline(coord_list, 255, 0, 0, 0, 5, &object);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - To create a polygon:

     ```
     maps_view_object_h object = NULL;
     maps_coordinates_h coord1 = NULL, coord2 = NULL, coord3 = NULL;
     maps_coordinates_list_h coord_list = NULL;

     maps_coordinates_list_create(&coord_list);
     maps_coordinates_create(28.64362, 77.19865, &coord1);
     maps_coordinates_list_append(coord_list, coord1);
     maps_coordinates_create(28.63441, 77.16908, &coord2);
     maps_coordinates_list_append(coord_list, coord2);
     maps_coordinates_create(28.65344, 77.22803, &coord3);
     maps_coordinates_list_append(coord_list, coord3);

     error = maps_view_object_create_polyline(coord_list, 255, 0, 0, 0, 5, &object);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

   - To create a marker with the `MAPS_VIEW_MARKER_PIN` type:

     ```
     maps_view_object_h object = NULL;
     maps_coordinates_h coord = NULL;

     maps_coordinates_create(28.64362, 77.19865, &coord);

     error = maps_view_object_create_marker(coord, "image/marker_icon.png", MAPS_VIEW_MARKER_PIN, &object);
     if (error != MAPS_ERROR_NONE)
         /* Error handling */
     ```

	 You can also create the `MAPS_VIEW_MARKER_STICKER` type marker.

2. Add the object instance to the map view with the `maps_view_add_object()` function:

    ```
    error = maps_view_add_object(maps_view, object);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

3. When no longer needed, remove the instance with the `maps_view_remove_object()` function:

    ```
    maps_view_remove_object(maps_view, object);
    ```

<a name="maps_event"></a>
## Managing Map View Events

To handle map view events:

1. Register an event callback with the `maps_view_set_event_cb()` function.

    In the second parameter, define the type of the event you want to receive:
    - `MAPS_VIEW_EVENT_GESTURE`
    - `MAPS_VIEW_EVENT_ACTION`
    - `MAPS_VIEW_EVENT_OBJECT`
    - `MAPS_VIEW_EVENT_READY`

    ```
    error = maps_view_set_event_cb(maps_view, MAPS_VIEW_EVENT_GESTURE, __main_view_event_cb, NULL);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */

    static void
    __main_view_event_cb(const maps_view_event_type_e type, maps_view_event_data_h event_data, void *user_data)
    {
        /* Handle the obtained event */
    }
    ```


2. Within the callback, access the event data with various `maps_view_event_data_get_XXX()` functions of the View Event Data API (in [mobile](../../api/mobile/latest/group__CAPI__MAPS__VIEW__EVENT__DATA__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__MAPS__VIEW__EVENT__DATA__MODULE.html) applications).

3. When no longer needed, unset the callback with the `maps_view_unset_event_cb()` function:

    ```
    error = maps_view_unset_event_cb(maps_view, MAPS_VIEW_EVENT_GESTURE);
    if (error != MAPS_ERROR_NONE)
        /* Error handling */
    ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
