# Data Filtering and Sorting

When managing large amounts of data, you can create filters to search for specific information, and make queries to receive only the information you are looking for. You can use various filter attributes and sort the received data.

The Tizen API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main data handling features of the Tizen API include:

- Filters

  The Tizen API supports the following filter types, which are subtypes of the `AbstractFilter` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#AbstractFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#AbstractFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#AbstractFilter) applications):

  - `AttributeFilter` (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#AttributeFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#AttributeFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#AttributeFilter) applications)  
  	 Matches objects containing a defined attribute or attribute value. The match is determined based on match flags defined with the `FilterMatchFlag` type definition.

  - `AttributeRangeFilter`(in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#AttributeRangeFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#AttributeRangeFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#AttributeRangeFilter) applications)  
  	 Matches objects containing an attribute whose values are within a particular range.

  - `CompositeFilter` (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#CompositeFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#CompositeFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#CompositeFilter) applications)	  
   Combines several filters into a set.

  You can create [attribute filters](#creating-attribute-filters), [attribute range filters](#creating-attribute-range-filters), and [composite filters](#creating-composite-filters) to search for specific data and [make complex queries](#making-complex-queries-using-filters). The attributes you can use with the filter types vary depending on the API you are using. For example, query methods related to the [calendar](#calendar-filter-attributes), [call history](#call-history-filter-attributes), [contact](#contact-filter-attributes), [content](#content-filter-attributes), and [messaging](#messaging-filter-attributes) data each have their own sets of supported filter attributes.

- Sorting   

  You can [sort the results of queried data](#using-sorting-modes) using the `SortMode` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#SortMode), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#SortMode), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#SortMode) applications).

## Creating Attribute Filters

 Learning how to create attribute filters allows you effectively incorporate query methods in your application:

1. The `AttributeFilter` filter (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#AttributeFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#AttributeFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#AttributeFilter) applications) is used to filter the search results based on an attribute value. In this example, the filter finds contacts, with the first name Chris, from the default address book.

   Create the filter with the `AttributeFilter` constructor. You can specify attribute options, such as the attribute name, match flag, and match value.

   ```
   /* Use the firstName attribute with the EXACTLY match flag and the Chris value */
   var firstNameFilter = new tizen.AttributeFilter('name.firstName', 'EXACTLY', 'Chris');
   ```

2. Call the `find()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications) to find contacts. The filter (`firstNameFilter`) you created is included as a parameter.

   ```
   tizen.contact.getDefaultAddressBook().find(successCB, errorCB, firstNameFilter);
   ```

## Creating Attribute Range Filters

 Learning how to use attribute range filters allows you effectively incorporate query methods in your application:

1. The `AttributeRangeFilter` filter (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#AttributeRangeFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#AttributeRangeFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#AttributeRangeFilter) applications)is used to search for results based on a range of attribute values. In this example, the filter finds all events starting on a defined day from the calendar.

   Create the filter with the `AttributeRangeFilter` constructor. Specify the attribute, and the start and end points of the value range.

   ```
   /* Use the startDate attribute with a range that starts today and ends in 1 day */
   /* (meaning that you search for all events occurring today) */
   var now = tizen.time.getCurrentDateTime();
   var today_begin = new tizen.TZDate(now.getFullYear(), now.getMonth(), now.getDate());
   var today_end = today_begin.addDuration(new tizen.TimeDuration(1, 'DAYS'));
   var dateRangeFilter = new tizen.AttributeRangeFilter('startDate', today_begin, today_end);
   ```

2.  Call the `find()` method of the `Calendar` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications) to find events. The filter (`dateRangeFilter`) you created is included as a parameter.

    ```
    tizen.calendar.getDefaultCalendar('EVENT').find(successCB, errorCB, dateRangeFilter);
    ```

## Creating Composite Filters

 Learning how to use composite filters allows you effectively incorporate query methods in your application:

1. The `CompositeFilter` filter (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#CompositeFilter), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#CompositeFilter), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#CompositeFilter) applications) is used to search for results based on a set of filters. In this example, the filter finds contacts, whose first name contains Chris and last name is Smith, from the default address book.

   Create the filter with the `CompositeFilter` constructor. You can specify multiple sub-filters for the filter set.

   ```
   /* Create an attribute filter based on the firstName attribute */
   var firstNameFilter = new tizen.AttributeFilter('name.firstName', 'CONTAINS', 'Chris');

   /* Create an attribute filter based on the lastName attribute */
   var lastNameFilter = new tizen.AttributeFilter('name.lastName', 'EXACTLY', 'Smith');

   /*
      Create a composite filter based on the intersection of these 2 filters
      (intersection means that both filters must match
      for the contact to be included in the results)
   */
   var nameCompositeFilter = new tizen.CompositeFilter('INTERSECTION', [firstNameFilter, lastNameFilter]);
   ```

2.  Call the `find()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications) to find matching contacts. The filter (`nameCompositeFilter`) you created is included as a parameter.

    ```
    tizen.contact.getDefaultAddressBook().find(successCB, errorCB, nameCompositeFilter);
    ```

## Using Sorting Modes

The following sorting modes are supported:

- `'ASC'`: Ascending sorting order
- `'DESC'`: Descending sorting order

 Learning how to use sorting modes allows you effectively incorporate query methods in your application:

1. The `SortMode` interface (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#SortMode), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#SortMode), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#SortMode) applications) is created to sort the search results. In this example, it is used to sort contacts in the device address book in ascending order by first name.

   Create the sort order with the `SortMode()` method. Specify an attribute name to sort by and an order option.

   ```
   /* Use the firstName attribute with an ASC order */
   var sortMode = new tizen.SortMode('name.firstName', 'ASC');
   ```

2.  Call the `find()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications) to find matching contacts. In this example, the filter parameter in the `find()` method is defined as `null`, which means that the method retrieves all contacts in the address book.

    ```
    tizen.contact.getDefaultAddressBook().find(successCB, errorCB, null, sortMode);
    ```

> **Note**  
> If you use a type attribute as a sort mode parameter, the sorting is not performed alphabetically since the attribute values are stored normally after the type conversion in the platform implementation.  
> For example, if the `ContentType` enumeration (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentType), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentType), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentType) applications) is the type attribute and the sorting order is `"DESC"`, the sorting result is ordered according to the listed enumerator order:
> - Image
> - Video
> - Audio
> - Other

## Making Complex Queries Using Filters

Learning how to use filters allows you effectively incorporate complex query methods in your application. You can create queries using AND and OR conditions, like in SQL queries. The following example shows how to make the following query:

`"where ((type='VIDEO' OR type='IMAGE') AND title like '%special%')"`

Basically, you search the content of the device for media items where the media type is video or image, and the title contains the word "special".

1. Create attribute filters to include all content whose media type is either video or image:

   ```
   function makeQueryAndFire() {
       /* Filter for the video media type */
       var typeVideoFilter = new tizen.AttributeFilter('type', 'EXACTLY', 'VIDEO');

       /* Filter for the image media type */
       var typeImageFilter = new tizen.AttributeFilter('type', 'EXACTLY', 'IMAGE');
   ```

2. Create a composite filter that finds all content that matches one of the media type filters:

   ```
       var typeFilter =
           new tizen.CompositeFilter('UNION', [typeVideoFilter, typeImageFilter]);
   ```

3. Create another attribute filter that includes content containing the word "special" in its title:

   ```
       var titleFilter = new tizen.AttributeFilter('title', 'CONTAINS', 'special');
   ```

4. Create the final composite filter that finds all content that matches both the composite media type filter and the title filter:

   ```
       var finalFilter =
           new tizen.CompositeFilter('INTERSECTION', [typeFilter, titleFilter]);
   ```

5. Call the `find()` method of the Content API's `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications) to retrieve the media items that match the final filter:

   ```
       tizen.content.find(findMediaContentsCallback, onError, null, finalFilter);
   }
   ```

   The `findMediaContentsCallback()` event handler returns the query result.

## Calendar Filter Attributes

The following table lists the filter types you can use with specific calendar item attributes in the methods of the `Calendar` interface (in [mobile](../../api/latest/device_api/mobile/tizen/calendar.html#Calendar) and [wearable](../../api/latest/device_api/wearable/tizen/calendar.html#Calendar) applications).

**Table: Calendar filter attributes**

| Attribute               | Attribute filter supported | Attribute range filter supported |
| ----------------------- | -------------------------- | -------------------------------- |
| `id`                    | Yes                        | No                               |
| `id.uid`                | Yes                        | No                               |
| `description`           | Yes                        | No                               |
| `summary`               | Yes                        | No                               |
| `isAllDay`              | Yes                        | No                               |
| `isDetached`            | Yes                        | No                               |
| `startDate`             | Yes                        | Yes                              |
| `location`              | Yes                        | No                               |
| `geolocation.latitude`  | Yes                        | Yes                              |
| `geolocation.longitude` | Yes                        | Yes                              |
| `organizer`             | Yes                        | No                               |
| `visibility`            | Yes                        | No                               |
| `status`                | Yes                        | No                               |
| `priority`              | Yes                        | No                               |
| `categories`            | Yes                        | No                               |
| `dueDate`               | Yes                        | Yes                              |
| `completedDate`         | Yes                        | Yes                              |
| `progress`              | Yes                        | Yes                              |
| `endDate`               | Yes                        | Yes                              |
| `availability`          | Yes                        | No                               |
| `lastModificationDate`  | Yes                        | Yes                              |
| `alarms`                | No*                        | No                               |
| `attendees`             | No*                        | No                               |
| `recurrenceRule`        | No*                        | No                               |

\* The attribute filter is only supported with the `EXISTS` flag.

## Call History Filter Attributes

The following table lists the filter types you can use with specific call history attributes in the methods of the [CallHistory](../../api/latest/device_api/mobile/tizen/callhistory.html#CallHistory) interface.

**Table: Call History filter attributes**

| Attribute                   | Attribute filter supported | Attribute range filter supported |
| --------------------------- | -------------------------- | -------------------------------- |
| `uid`                       | Yes                        | Yes                              |
| `type`                      | Yes                        | No                               |
| `features`                  | Yes                        | No                               |
| `remoteParties.remoteParty` | Yes                        | Yes                              |
| `remoteParties.personId`    | Yes                        | Yes                              |
| `startTime`                 | Yes                        | Yes                              |
| `duration`                  | Yes                        | Yes                              |
| `direction`                 | Yes                        | No                               |

## Contact Filter Attributes

The following table lists the filter types you can use with specific contact attributes in the methods of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications).

**Table: Contact filter attributes**

| Attribute                         | Attribute filter supported | Attribute range filter supported |
| --------------------------------- | -------------------------- | -------------------------------- |
| `id`                              | Yes                        | Yes                              |
| `personId`                        | Yes                        | Yes                              |
| `lastUpdated`                     | Yes                        | Yes                              |
| `isFavorite`                      | Yes                        | Yes                              |
| `birthday`                        | Yes                        | Yes                              |
| `photoURI`                        | Yes                        | No                               |
| `ringtoneURI`                     | Yes                        | No                               |
| `name.prefix`                     | Yes                        | No                               |
| `name.suffix`                     | Yes                        | No                               |
| `name.firstName`                  | Yes                        | No                               |
| `name.middleName`                 | Yes                        | No                               |
| `name.lastName`                   | Yes                        | No                               |
| `name.nicknames`                  | Yes                        | No                               |
| `name.phoneticFirstName`          | Yes                        | No                               |
| `name.phoneticLastName`           | Yes                        | No                               |
| `name.displayName`                | Yes                        | No                               |
| `addresses.country`               | Yes                        | No                               |
| `addresses.region`                | Yes                        | No                               |
| `addresses.city`                  | Yes                        | No                               |
| `addresses.streetAddress`         | Yes                        | No                               |
| `addresses.additionalInformation` | Yes                        | No                               |
| `addresses.postalCode`            | Yes                        | No                               |
| `addresses.isDefault`             | Yes                        | No                               |
| `addresses.types`                 | No                         | No                               |
| `phoneNumbers.number`             | Yes                        | No                               |
| `phoneNumbers.isDefault`          | Yes                        | No                               |
| `phoneNumbers.types`              | No                         | No                               |
| `emails.email`                    | Yes                        | No                               |
| `emails.isDefault`                | Yes                        | No                               |
| `emails.types`                    | No                         | No                               |
| `anniversaries.date`              | Yes                        | Yes                              |
| `anniversaries.label`             | Yes                        | No                               |
| `organizations.name`              | Yes                        | No                               |
| `organizations.department`        | Yes                        | No                               |
| `organizations.title`             | Yes                        | No                               |
| `organizations.role`              | Yes                        | No                               |
| `organizations.logoUri`           | Yes                        | No                               |
| `urls.url`                        | Yes                        | No                               |
| `urls.type`                       | No                         | No                               |
| `groupIds`                        | Yes                        | Yes                              |

The following table lists the filter types you can use with specific person attributes in the methods of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications).

**Table: Person filter attributes**

| Attribute          | Attribute filter supported | Attribute range filter supported |
| ------------------ | -------------------------- | -------------------------------- |
| `id`               | Yes                        | No                               |
| `displayName`      | Yes                        | No                               |
| `contactCount`     | Yes                        | Yes                              |
| `hasPhoneNumber`   | Yes                        | No                               |
| `hasEmail`         | Yes                        | No                               |
| `isFavorite`       | Yes                        | No                               |
| `photoURI`         | Yes                        | No                               |
| `ringtoneURI`      | Yes                        | No                               |
| `displayContactId` | Yes                        | No                               |

## Content Filter Attributes

The following table lists the filter types you can use with specific content attributes in the methods of the `ContentManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/content.html#ContentManager), [wearable](../../api/latest/device_api/wearable/tizen/content.html#ContentManager), and [TV](../../api/latest/device_api/tv/tizen/content.html#ContentManager) applications).

**Table: Content filter attributes**

| Attribute               | Attribute filter supported | Attribute range filter supported |
| ----------------------- | -------------------------- | -------------------------------- |
| `id`                    | Yes                        | No                               |
| `type`                  | Yes                        | No                               |
| `mimeType`              | No                         | No                               |
| `name`                  | Yes                        | No                               |
| `title`                 | Yes                        | No                               |
| `contentURI`            | Yes                        | No                               |
| `thumbnailURIs`         | Yes                        | No                               |
| `releaseDate`           | Yes                        | Yes                              |
| `modifedDate`           | Yes                        | Yes                              |
| `size`                  | No                         | No                               |
| `description`           | Yes                        | No                               |
| `rating`                | Yes                        | Yes                              |
| `geolocation.latitude`  | Yes                        | Yes                              |
| `geolocation.longitude` | Yes                        | Yes                              |
| `album`                 | Yes                        | No                               |
| `genres`                | Yes                        | No                               |
| `artists`               | Yes                        | No                               |
| `composers`             | No                         | No                               |
| `lyrics`                | No                         | No                               |
| `copyright`             | No                         | No                               |
| `bitrate`               | No                         | No                               |
| `trackNumber`           | No                         | No                               |
| `duration`              | No                         | No                               |
| `orientation`           | No                         | No                               |

## Messaging Filter Attributes

The following tables list the filter types you can use with specific message attributes in the methods of the [MessageStorage](../../api/latest/device_api/mobile/tizen/messaging.html#MessageStorage) interface.

The following table lists the filter attributes related to the `findMessage()` method.

**Table: Filter attributes for finding messages**

| Attribute        | Attribute filter supported | Attribute range filter supported |
| ---------------- | -------------------------- | -------------------------------- |
| `id`             | Yes                        | No                               |
| `serviceId`      | Yes                        | No                               |
| `conversationId` | No                         | No                               |
| `folderId`       | Yes                        | No                               |
| `type`           | Yes                        | No                               |
| `timestamp`      | No                         | Yes                              |
| `from`           | Yes                        | No                               |
| `to`             | Yes                        | No                               |
| `cc`             | Yes                        | No                               |
| `bcc`            | Yes                        | No                               |
| `body.plainBody` | Yes                        | No                               |
| `isRead`         | Yes                        | No                               |
| `hasAttachment`  | Yes                        | No                               |
| `isHighPriority` | Yes                        | No                               |
| `subject`        | Yes                        | No                               |
| `isResponseTo`   | No                         | No                               |
| `messageStatus`  | No                         | No                               |
| `attachments`    | No                         | No                               |

The following table lists the filter attributes related to the `findConversations()` method.

**Table: Filter attributes for finding conversations**

| Attribute        | Attribute filter supported | Attribute range filter supported |
| ---------------- | -------------------------- | -------------------------------- |
| `id`             | Yes                        | No                               |
| `type`           | Yes                        | No                               |
| `timestamp`      | No                         | Yes                              |
| `messageCount`   | Yes                        | No                               |
| `unreadMessages` | Yes                        | No                               |
| `preview`        | Yes                        | No                               |
| `subject`        | No                         | No                               |
| `isRead`         | No                         | No                               |
| `from`           | Yes                        | No                               |
| `to`             | Yes                        | No                               |
| `cc`             | No                         | No                               |
| `bcc`            | No                         | No                               |
| `lastMessageId`  | No                         | No                               |

The following table lists the filter attributes related to the `findFolders()` method.

**Table: Filter attributes for finding message folders**

| Attribute        | Attribute filter supported | Attribute range filter supported |
| ---------------- | -------------------------- | -------------------------------- |
| `id`             | No                         | No                               |
| `parentId`       | No                         | No                               |
| `serviceId`      | Yes                        | No                               |
| `contentType`    | No                         | No                               |
| `name`           | No                         | No                               |
| `path`           | No                         | No                               |
| `type`           | No                         | No                               |
| `synchronizable` | No                         | No                               |

> **Note**  
> The `FULLSTRING` value of the `FilterMatchFlag` enumerator (in [mobile](../../api/latest/device_api/mobile/tizen/tizen.html#FilterMatchFlag), [wearable](../../api/latest/device_api/wearable/tizen/tizen.html#FilterMatchFlag), and [TV](../../api/latest/device_api/tv/tizen/tizen.html#FilterMatchFlag) applications) is not supported and returns an error callback.

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
