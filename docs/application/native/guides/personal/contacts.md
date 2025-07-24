# Contacts


You can help the user manage their contact information, such as address books, groups, persons, and phone logs. Since the contact information is stored in a contacts database, you must [connect to the contact service](#prerequisites) to manage the information.

The following figure illustrates the structure of the contact information in the database:

- Each contact has their own details, such as a name, phone number, and email address.

- Each contact object is associated with a specific address book.

  The address book can be the local device address book, or an address book related to a specific service provider or application account (such as Samsung or Joyn).

- Multiple contacts can be associated with the same physical person.

  A person object is an aggregation of one or multiple contact objects.

In the figure, the Person1 is an aggregation of the Contact1, Contact2, and Contact3 instances, which all belong to different address books.

**Figure: Contact structure**

![Contact structure](./media/contacts_contact_structure.png)

The main features of the Contacts API include:

- Contact management
  - You can manage individual [contact record details](#record), such as name, phone number, email, address, job, instant messenger, and company, with the help of [contact data-views](#view).

    You can also create [lists](#list) of similar contacts to manage them in [batches](#bulk).

  - You can [insert contacts](#create_contact) to, [update them](#update_contact) in, and remove them from the contacts database.
  - You can monitor [changes in the contacts database](#db).
  - You can search for and organize contacts using [filters and queries](#filter).
  - You can [manage the display and sorting order settings](#settings) for contacts.
  - You can manage My profile. It has similar details as contact information in general, but no properties, such as group relation, ringtone, and message alert. My profile can have a single entry in each address book.
  - You can store social activities.
- Persons
  - You can [link multiple contacts together](#link_contact) to set up a [virtual contact](#person) (person) to be shown and managed when more than 1 contact from different sources designate the same individual.
  - You can [set a person as favorite](#manage_contact) to make it easier to access their information.
  - You can [delete persons](#delete_contact) when no longer needed.
- Groups
  - You can combine contacts in the same address book to [create groups](#create), allowing you to easily set the same properties (such as ringtones) for all contacts within the group.
  - You can [update](#update) and [delete](#delete) groups.
  - You can [manage group members](#manage) and set up many-to-many relationships between groups and contacts.
- Address books
  - You can create address books using the local device (with no account), service providers (such as Samsung account), or applications (such as Joyn).
  - You can determine to which address book each contact and group belong.
  - If the address book is related to an account, you can handle the account using an account ID created with the [Account Manager](account.md). If the local device address book has no account, the related account ID is 0. You can create only one address book for each account.
- Speed dials
  - You can [create a speed dial](#sd_create), which is a shortcut dialing number key.
  - You can [update](#sd_update) and [delete](#sd_delete) speed dials.
- Phone logs
  - You can [create and store call or message logs](#pl_create).
  - You can [delete logs](#pl_delete).

The contact service supports [vCards](#vcard), allowing you to import contact information from a vCard or export it to vCard format. You can also [import contacts from the device SIM card](#sim) to the contacts database.

The following figure illustrates the different entities and their relationships in the contact service.

**Figure: Contact entities**

![Contact entities](./media/contacts_contact_entity.png)

<a name="person"></a>
## Links Between Contacts and Persons

Each contact is linked to at least 1 person, which is a kind of virtual contact that can be used to combine the details when multiple contacts from different address books represent the same individual.

The linking between contacts and persons functions as follows:

- A person record cannot be created directly - it is created automatically when a contact record is inserted in the contacts database, and at the same time the contact is linked to the person.

  **Figure: Person is created along with the contact**

  ![Person is created along with the contact](./media/contacts_person_record.png)

- 2 persons (with contacts in different address books) can be linked together.

  As a result, the second person is destroyed automatically, and all the contacts linked to both persons are consequently linked to the 1 remaining person.

  **Figure: 2 persons can be linked**

  ![2 persons can be linked](./media/contacts_link_person.png)

- A contact can be separated (unlinked) from the person.

  As a result, a new person is automatically created and the separated contact is linked to that.

  **Figure: Unlinking a contact**

  ![Unlinking a contact](./media/contacts_unlink_contact.png)

<a name="record"></a>
## Records

A record represents an actual record in the internal database, but you can also consider it a piece of information, such as an address, a phone number, or a group of contacts. A record can be a complex set of data, containing other data. For example, a contact record contains the `address` property, which is a reference to an address record. An address record belongs to a contact record, and its `contact_id` property is set to the identifier of the corresponding contact. In this case, the address is the child record of the contact and the contact is the parent record.

You can [create records](#insert2) in the database, [retrieve individual record details](#get2) or [lists of multiple records](#list2), [delete records](#delete2), and combine contact records by [linking them into a single person](#link2).

To use a record, you must obtain its handle. To get the handle, you can either create a record, use the ID, or get the handle through the parent record:

- Obtaining the handle when creating a record

  When creating a record, you must specify what type of record you want to create by using the URI property.

  ```
  contacts_record_h contact = NULL;
  /* Create contact record and receive a handle for it */
  contacts_record_create(_contacts_contact._uri, &contact);

  contacts_record_h name = NULL;
  /* Create a name record and receive a handle for it */
  contacts_record_create(_contacts_name._uri, &name);
  contacts_record_set_str(name, _contacts_name.first, "first name");
  contacts_record_add_child_record(contact, _contacts_contact.name, name);
  ```

- Obtaining the handle using the ID

  An ID is a unique number for identifying records. Therefore, if you know the ID of a record, you can directly handle the record. The ID is a read-only property, which is available after the record has been inserted into the database. The following example gets a contact record with an ID:

  ```
  int contact_id = 0;
  contacts_db_insert_record(contact, &contact_id);
  contacts_record_destroy(contact, true); /* Contact is no longer usable */

  /* Retrieve the record; contact is now a handle to the same record as before */
  contacts_db_get_record(_contacts_contact._uri, contact_id, &contact);
  char *display_name = NULL;
  contacts_record_get_str(contact, _contacts_contact.display_name, &display_name);
  contacts_record_destroy(contact, true); /* Contact is no longer usable */
  ```

- Obtaining the handle using the parent record

  The following code example changes a country of addresses which are child records of a contact. Each address can be traversed by using the `contacts_record_get_child_record_at_p()` function. It is possible to apply the changes by updating the contact which is the parent record:

  ```
  int contact_id = ... /* Acquire ID of the created contact */
  unsigned int address_num = 0;
  int i = 0;
  contacts_db_get_record(_contacts_contact._uri, contact_id, &contact);
  contacts_record_get_child_record_count(contact, _contacts_contact.address, &address_num);
  for (i = 0; i < address_num; i++) {
      contacts_record_h address = NULL;
      /* Get the address record handle */
      contacts_record_get_child_record_at_p(contact, _contacts_contact.address, i, &address);
      contacts_record_set_str(address, _contacts_address.country, "Korea");
  }
  contacts_db_update_record(contact);
  contacts_record_destroy(contact, true);
  ```

To manage the record using the handle, you can use the URI, views, or basic types:

- URI

  A record type is identified by a structure called the view, which contains identifiers of its properties. Every view has a special `_uri` field that uniquely identifies the view. In many cases, you must provide the `_uri` value as a parameter to indicate what type of record you want to create or operate on.

  For a list of functions that need the `_uri` postfix, see the list of functions in the Contacts API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html#CAPI_SOCIAL_CONTACTS_SVC_MODULE_RECORDS_URI) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html#CAPI_SOCIAL_CONTACTS_SVC_MODULE_RECORDS_URI) applications).

<a name="view"></a>
- Views

  Views are provided to access and handle entities. A data-view is a structure, which has property elements. For example, the `_contacts_contact` view describes the properties of the contact record. Its properties include, for example, name, company, and nickname of the contact. The property elements have their data types and names. The generic access functions, such as `contacts_db_insert_record()` and `contacts_record_get_int()`, can be used to access the contact views.

  The record types that have `*_id` as their property, hold identifiers of other records. For example, the name, number, and email views hold the ID of their corresponding contacts in the `contact_id` property as children of the corresponding contact records. A data-view is almost the same as a database "VIEW", which limits access and guarantees performance. A "record" represents a single row of the data-views.

  The property type `record` means that the parent record can have child records. For example, a contact record has `name`, `number`, and `email` properties, which means that records of those types can be children of the contact type records. The following figure illustrates macros in a `contacts_view.h` header file.

  **Figure: Properties**

  ![Properties](./media/contact_property.png)

  For more information, see the View/Property API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html) applications).

- Basic types

  Records contain properties of basic types: `integer`, `string`, `boolean`, `long integer`, `lli` (long long int), and `double`.

  The following table lists the setter and getter functions for each type.

  **Table: Setter and getter functions**

  | Property            | Setter                         | Getter                         |
  |---------------------|--------------------------------|--------------------------------|
  | `string`            | `contacts_record_set_str()`    | `contacts_record_get_str()`    |
  | `integer`           | `contacts_record_set_int()`    | `contacts_record_get_int()`    |
  | `boolean`           | `contacts_record_set_bool()`   | `contacts_record_get_bool()`   |
  | `long long integer` | `contacts_record_set_lli()`    | `contacts_record_get_lli()`    |
  | `double`            | `contacts_record_set_double()` | `contacts_record_get_double()` |

  These functions also require specifying which property to get and set, and for this, every getter and setter function needs a record and property ID. Create a property ID by combining the data-view and property name. For example, the property ID of a contact `display_name` property is `_contacts_contact.display_name`.

  The following example sets the `ringtone_path` property of a contact record:

  ```
  char *resource_path = app_get_resource_path();
  char ringtone_path[1024];
  snprintf(ringtone_path, sizeof(ringtone_path), "%s/ringtone.mp3", resource_path);
  free(resource_path);
  contacts_record_set_str(contact, _contacts_contact.ringtone_path, ringtone_path);
  ```

  With a record handle, you can access all records of a specific type related to the given record.

  > **Note**
  >
  > The string getter functions have the `_p` postfix. It means that the returned value should not be freed by the application, as it is a pointer to data in an existing record.
  >
  > The following example shows that there are 2 ways of getting the string property:
  > ```
  > contacts_record_get_str(record, _contacts_person.display_name, &display_name);
  > contacts_record_get_str_p(record, _contacts_person.display_name, &display_name);
  > ```
  > In the first case, the returned string must be freed by the application. In the second one, the `display_name` value is freed automatically when destroying the record handle.

### Child Records

A record can have properties of the `record` type called child records. Effectively, a record can be a node in a tree or graph of relations between records.

The following figure illustrates the relationships between the parent and child records.

**Figure: Child records**

![Child records](./media/contacts_children.png)

The following code example inserts an address record into a contact record. Note that it is not necessary to insert or destroy all records. Only the parent record needs to be inserted into the database to store all the information, and when the parent record is destroyed, the child records are also destroyed automatically.

```
contacts_record_h address = NULL;
contacts_record_h image = NULL;

int contact_id = 0;

contacts_record_create(_contacts_contact._uri, &contact);

/* Image and address record can be child records of contact record */
contacts_record_create(_contacts_image._uri, &image);
char *resource_path = app_get_resource_path();
char caller_id_path[1024];
snprintf(caller_id_path, sizeof(caller_id_path), "%s/caller_id.jpg", resource_path);
free(resource_path);
contacts_record_set_str(image, _contacts_image.path, caller_id_path);
contacts_record_add_child_record(contact, _contacts_contact.image, image);

contacts_record_create(_contacts_address._uri, &address);
contacts_record_set_str(address, _contacts_address.country, "Korea");
contacts_record_add_child_record(contact, _contacts_contact.address, address);

/* Insert contact to the database */
contacts_db_insert_record(contact, &contact_id);
contacts_record_destroy(contact, true);
```

> **Note**
>
> For an application to insert private images in contacts, the following conditions apply:
> 	- The application must have the `http://tizen.org/privilege/contact.write` privilege to use the database modifying functions, such as `contacts_db_insert_record()`.
> 	- The application's private directory and files must have the `read` permission of others, such as `644`. SMACK protects the `read` permission from the other applications.
> 	- The application can erase the image after destroying the contact record using the `contacts_record_destroy()` function.

Identifiers can be used to establish a relationship between 2 records. The following code example sets an address record's `contact_id` property to the ID of the contact. The `contact_id` relates between the address record and the contact which is identified by the `contact_id`. After the ID is set, the address becomes one of the addresses connected to the contact. The address is now the contact's child record, and the contact is the parent record.

```
int contact_id = ... /* Acquire the ID of the created contact */
int address_id = 0;
contacts_record_create(_contacts_address._uri, &address);
contacts_record_set_int(address, _contacts_address.contact_id, contact_id);

/* Set other address properties */

contacts_db_insert_record(address, &address_id);
```

<a name="list"></a>
## Contact Lists and Batch Operations

The contact service provides functions which can handle lists of records with the same type. The list concept is based on a standard doubly-linked list.

To operate a list, you must obtain its handle. The handle is provided during the list creation using the `contacts_list_create()` function.

To create a list:

- Create a list from scratch and receive a handle for it:

  ```
  /* Get a list handle with a query */
  contacts_list_h list = NULL;
  contacts_list_create(&list);

  /* Use the list */

  contacts_list_destroy(list, true);
  ```

  Destroy the list handle after use with the `contacts_list_destroy()` function. If the last parameter is `true`, child resources are destroyed automatically.

- Create a list by performing a query to the database, and receive a handle for the list:

  ```
  /* Get a list handle with a query */
  contacts_list_h list = NULL;
  contacts_db_get_all_records(_contacts_person._uri, 0, 0, &list);

  /* Use the list */

  contacts_list_destroy(list, true);
  ```

To manage the list:

- Traversing

  The list can be traversed using a cursor. Use the `contacts_list_first()`, `contacts_list_last()`, `contacts_list_next()`, and `contacts_list_prev()` functions to move the cursor in the list.

  To get a record of the current cursor, use the `contacts_list_get_current_record_p()` function.

  The following example loops through a list:

  ```
  contacts_list_h list = NULL;
  contacts_record_h record = NULL;
  contacts_db_get_all_records(_contacts_person._uri, 0, 0, &list);
  do {
      contacts_list_get_current_record_p(list, &record);
      if (NULL == record)
          break;
      char *name = NULL;
      contacts_record_get_str_p(record, _contacts_person.display_name, &name);
      dlog_print(DLOG_DEBUG, LOG_TAG, "name=%s", name);
  } while (CONTACTS_ERROR_NONE == contacts_list_next(list));
  contacts_list_destroy(list, true); /* Destroy child records automatically */
  ```

- Adding and removing

  Use the `contacts_list_add()` function to add, and the `contacts_list_remove()` function to remove child records.

  The following example adds records to the list:

  ```
  contacts_record_h group1 = NULL;
  contacts_record_create(_contacts_group._uri, &group1);
  contacts_record_set_str(group1, _contacts_group.name, "group test1");

  contacts_record_h group2 = NULL;
  contacts_record_create(_contacts_group._uri, &group2);
  contacts_record_set_str(group2, _contacts_group.name, "group test2");

  contacts_list_h list = NULL;
  contacts_list_create(&list);

  /* Add records to the list */
  contacts_list_add(list, group1);
  contacts_list_add(list, group2);

  contacts_db_insert_records(list, NULL, NULL);
  contacts_list_destroy(list, true);
  ```

<a name="bulk"></a>
- Using batch operations

  With batch functions, you can use insert, update, and delete operations for multiple records simultaneously. There is no limit on the record count for a batch function, but it causes a process to hang while the function is operated. Batch functions guarantee atomicity. That is, the batch operations are performed either for all, or nothing.

  - To insert records, use the `contacts_db_insert_records()` function.
  - To update the records database, use the `contacts_db_update_records()` function.
  - To delete the contacts, use the `contacts_db_delete_records()` function.
  - To replace the contact records, use the `contacts_db_replace_records()` function.

  The following code example inserts 2 contact records using a batch function:

  ```
  contacts_record_h contact1;
  contacts_record_create(_contacts_contact.uri, &contact1);

  /* Fill contact record */

  contacts_record_h contact2;
  contacts_record_create(_contacts_contact._uri, &contact2);

  /* Fill contact record */

  contacts_list_h list = NULL;
  contacts_list_create(&list);

  contacts_list_add(list, contact1);
  contacts_list_add(list, contact2);

  int **ids = NULL;
  unsigned int count = 0;

  /* Insert contact records using a batch function */
  contacts_db_insert_records(list, &ids, &count);

  /* Use IDs */

  contacts_list_destroy(list, true);
  free(ids);
  ```

<a name="filter"></a>
## Filters and Queries

Queries are used to retrieve [person](#get_contact), [group](#get), [speed dial](#sd_get), and [log](#pl_get) data which satisfies a given criteria, such as an integer property being greater than a given value, or a string property containing a given substring. A query needs a filter which can set the conditions for the search. The contact service provides query functions for sorting set projections and removing duplicated results.

To filter, sort, and query contact data:

- Filtering

  The Filter API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html) applications) provides the set of definitions and interfaces that enable you to make filters to set queries.

  When creating a filter, use the `contacts_filter_create()` function, and specify the filter type you want to create using the `_uri` property. A filter handle must be destroyed after use with the `contacts_filter_destroy()` function.

  To manage filters:

  - To set the filter condition to contain a given substring, use the `contacts_filter_add_str()` function.

  - To set the filter condition to property value as `true`, use the `contacts_filter_add_bool()` function.

  - Multiple conditions can be added to a filter. Join the conditions by using the logical operators `AND` and `OR`.

    The following example creates a composite filter with the `OR` operator.

    ```
    contacts_filter_add_str(filter1, _contacts_person.display_name, CONTACTS_MATCH_CONTAINS, "1234");
    contacts_filter_add_operator(filter1, CONTACTS_FILTER_OPERATOR_OR);
    contacts_filter_add_str(filter1, _contacts_person.display_name, CONTACTS_MATCH_CONTAINS, "5678");
    ```

  - Additionally, multiple filters can join each other by using the logical operators `AND` and `OR`.

    The following example creates a joined filter with the `AND` operator.

    ```
    contacts_filter_add_str(filter1, _contacts_person.display_name, CONTACTS_MATCH_CONTAINS, "1234");
    contacts_filter_add_operator(filter1, CONTACTS_FILTER_OPERATOR_OR);
    contacts_filter_add_str(filter1, _contacts_person.display_name, CONTACTS_MATCH_CONTAINS, "5678");

    contacts_filter_add_bool(filter2, _contacts_person.is_favorite, true);

    contacts_filter_add_operator(filter1, CONTACTS_FILTER_OPERATOR_AND);
    contacts_filter_add_filter(filter1, filter2);
    ```

    The operator precedence in filters is determined by the order in which the conditions and filters are added. The following table shows the results, if the following sequences are added.

    **Table: Filters**

    | Filters                                  | Result                                   |
    |------------------------------------------|------------------------------------------|
    | Condition C1<br> OR<br>Condition C2<br>AND<br>Condition C3 | (C1 OR C2) AND C3                        |
    | **Filter F1**:<br>Condition C1<br>OR<br>Condition C2<br><br>**Filter F2**:<br>Condition C3<br>OR<br>Condition C4<br><br>**Filter F3**:<br>Condition C5<br>AND<br>F1<br>AND<br>F2 | (C5 AND F1) AND F2, which is<br>(C5 AND (C1 OR C2)) AND (C3 OR C4) |

  The following example creates a filter which accepts addresses with their contact's ID equal to a given ID (integer filter), or their country property equal to "Korea" (string filter). To get the filtered results, create a query and add the filter to it. The results are received in a list.

  ```
  contacts_filter_h filter = NULL;
  contacts_list_h list = NULL;
  contacts_query_h query = NULL;

  contacts_filter_create(_contacts_address._uri, &filter);
  contacts_filter_add_int(filter, _contacts_address.contact_id, CONTACTS_MATCH_EQUAL, id);
  contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_OR);
  contacts_filter_add_str(filter, _contacts_address.country, CONTACTS_MATCH_EXACTLY, "Korea");
  contacts_query_create(_contacts_address._uri, &query);
  contacts_query_set_filter(query, filter);

  contacts_db_get_records_with_query(query, 0, 0, &list);

  contacts_filter_destroy(filter);
  contacts_query_destroy(query);

  /* Use the list */

  contacts_list_destroy(list, true);
  ```

- Sorting

  To sort the query result list by the property ID, use the `contacts_query_set_sort()` function. The second parameter is the property ID.

  The following example sorts the query results by the person ID:

  ```
  contacts_filter_add_str(filter, _contacts_person.display_name, CONTACTS_MATCH_CONTAINS, "Joe");
  contacts_query_set_filter(query, filter);
  contacts_query_set_sort(query, _contacts_person.id, true);

  contacts_db_get_records_with_query(query, 0, 0, &list);

  contacts_query_destroy(query);
  contacts_filter_destroy(filter);
  contacts_list_destroy(person_list, true);
  ```

- Projection querying

  Projection allows you to query data for specific properties of a record, at lower latency and cost than retrieving all properties. To use projection, use the `contacts_query_set_projection()` function.

  The following example creates a filter which gets only the person ID, display name, and image thumbnail path from the person records which have "test" (string filter) as the vibration path. Create a query and add the filter to it; the results are received in a list.

  ```
  contacts_filter_add_str(filter, _contacts_person.vibration, CONTACTS_MATCH_CONTAINS, "test");
  contacts_query_set_filter(query, filter);

  /* Set projections */
  unsigned int person_projection[] =
  {
      _contacts_person.id,
      _contacts_person.display_name,
      _contacts_person.image_thumbnail_path,
  };

  contacts_query_set_projection(query, person_projection, sizeof(person_projection)/sizeof(int));

  contacts_db_get_records_with_query(query, 0, 0, &person_list);

  /* Use the list */

  contacts_query_destroy(query);
  contacts_filter_destroy(filter);
  contacts_list_destroy(person_list, true);
  ```

- Removing duplicates

  If you query a read-only view with a set projection, the result list can contain duplicates. Remove duplicates using the `contacts_query_set_distinct()` function.

  The following example removes duplicates:

  ```
  unsigned int projection[] =
  {
      _contacts_person_number.person_id,
      _contacts_person_number.display_name,
  };
  contacts_filter_create(_contacts_person_number._uri, &filter);
  contacts_filter_add_bool(filter, _contacts_person_number.has_phonenumber, true);

  contacts_query_create(_contacts_person_number._uri, &query);
  contacts_query_set_projection(query, projection, sizeof(projection)/sizeof(int));
  contacts_query_set_filter(query, filter);

  /* Set distinct (remove duplicates) */
  contacts_query_set_distinct(query, true);

  contacts_db_get_records_with_query(query, 0, 0, &list);

  /* Use the list */

  contacts_list_destroy(list, true);
  contacts_query_destroy(query);
  contacts_filter_destroy(filter);
  ```

<a name="db"></a>
## Database Change Notifications

To detect the [person](#monitor_contact) and [group](#monitor) changes in the contacts database, use the Database API functions (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__DATABASE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__DATABASE__MODULE.html) applications). Register a callback with the `contacts_db_add_changed_cb()` function. To deregister the callback and ignore database changes, use the `contacts_db_remove_changed_cb()` function.

Clients wait for contact change notifications on the client side. If the contact is changed by another module, the server publishes a notification. The notification module broadcasts to the subscribed modules and a user callback function is called with the user data. The following example registers a person change notification callback:

```
static void
__person_changed_cb(const char *view_uri, void *user_data)
{
    /* Jobs for the callback function */
}
/* Add a change notification callback */
contacts_db_add_changed_cb(_contacts_person._uri, __person_changed_cb, NULL);
```

<a name="vcard"></a>
## vCards

The contact service provides functions for [parsing](#parse) and [making](#make) vCards. The vCard functions are based on the [vCard v3.0 specification](http://www.ietf.org/rfc/rfc2426.txt).

- You can [import contact information](#import) by parsing vCards from stream or from a file:

  - The following example shows parsing a vCard from a stream and inserting it to the database:

    ```
    /* Make a contact record list from the vCard stream */
    contacts_list_h list = NULL;
    contacts_vcard_parse_to_contacts(vcard_stream, &list);

    /* Use the contact record list */

    contacts_list_destroy(list, true);
    ```

  - The following example shows parsing a vCard from a file and inserting it to the database:

    ```
    /* Get a record handle of the _contacts_contact view */
    static bool
    __vcard_parse_cb(contacts_record_h record, void *user_data)
    {
        int id = 0;
        contacts_db_insert_record(record, &id);

        /* Return false to break out of the loop */
        /* Return true to continue with the next iteration of the loop */
        return true;
    }

    /* Parse the vCard from a file */
    char *resource_path = app_get_resource_path();
    char vcard_path[1024];
    snprintf(vcard_path, sizeof(vcard_path), "%s/vcard.vcf", resource_path);
    free(resource_path);
    contacts_vcard_parse_to_contact_foreach(vcard_path, __vcard_parse_cb, NULL);
    ```

- You can [export contact information](#export) and make a vCard stream from a contact, person, or My profile record. The following code example makes a vCard stream using a contact record:

  ```
  contacts_record_h contact;
  char *vcard_stream = NULL;

  contacts_db_get_record(_contacts_contact._uri, contact_id, &contact);
  contacts_vcard_make_from_contact(contact, &vcard_stream);

  /* Use the vCard stream */

  free(vcard_stream);
  contacts_record_destroy(contact, true);
  ```

<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the contact functionality:

1. To use the Contacts API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/contact.read</privilege>
      <privilege>http://tizen.org/privilege/contact.write</privilege>
      <privilege>http://tizen.org/privilege/callhistory.read</privilege>
      <privilege>http://tizen.org/privilege/callhistory.write</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Contacts API, include the `<contacts.h>` header file in your application:

   ```
   #include <contacts.h>
   ```

   To ensure that a Contacts function has been executed properly, make sure that the return value is equal to `CONTACTS_ERROR_NONE`. If the function returns an error, handle it accordingly.

3. To access the contact database, connect to the contacts service using the `contacts_connect()` function:

   ```
   int error_code;
   error_code = contacts_connect();
   ```

   When the contacts service is no longer needed, disconnect from the service using the `contacts_disconnect()` function:

   ```
   error_code = contacts_disconnect();
   ```
<a name="create_contact"></a>
## Creating a Contact

Creating a new contact involves creating a contact handle, setting the contact properties, and inserting the contact into the contact database.

Some contact properties are defined as child records that are associated with the parent record. For a detailed list of the contact properties, see the `_contacts_contact` view description in the Contacts API (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html#CAPI_SOCIAL_CONTACTS_SVC_VIEW_MODULE_contacts_contact) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html#CAPI_SOCIAL_CONTACTS_SVC_VIEW_MODULE_contacts_contact) applications). If the property type is `record`, the property is defined as a child record. The property description defines whether a single or multiple child records are allowed for a specific property.

When you create a new contact, the system automatically creates a new person associated with that contact. A person is an aggregation of 1 or more contacts associated with the same individual. A contact is always associated with a person.

To create a new contact:

1. Create a contact handle using the `contacts_record_create()` function with the `_contacts_contact._uri` property as the first parameter and the contact handle variable as the second parameter:

   ```
   contacts_record_h contact;

   error_code = contacts_record_create(_contacts_contact._uri, &contact);
   ```

   > **Note**
   >
   > Records created with the `contacts_record_create()` function are memory objects, with `contacts_record_h` type variables as their handles. If you changes these objects, the changes are not reflected in the contact database until you explicitly insert or update the objects to the database using the `contacts_db_insert_record()` or `contacts_db_update_record()` function.

2. Set the contact properties:

   - To set the contact's name:

     1. Create a name record using the `contacts_record_create()` function with the `_contacts_name._uri` property as the first parameter:

        ```
        contacts_record_h name;

        error_code = contacts_record_create(_contacts_name._uri, &name);
        ```

     2. Set the contact's first name using the `contacts_record_set_str()` function with the `_contacts_name.first` property as the second parameter:

        ```
        error_code = contacts_record_set_str(name, _contacts_name.first, "John");
        ```

     3. Set the contact's last name using the `contacts_record_set_str()` function with the `_contacts_name.last` property as the second parameter:

        ```
        error_code = contacts_record_set_str(name, _contacts_name.last, "Smith");
        ```

     4. Set the name record as a child record of the contact record using the `contacts_record_add_child_record()` function with the `_contacts_contact.name` property as the second parameter:

        ```
        error_code = contacts_record_add_child_record(contact, _contacts_contact.name, name);
        ```

   - To set an image for the contact:

     1. Create an image record using the `contacts_record_create()` function with the `_contacts_image._uri` property as the first parameter:

        ```
        contacts_record_h image;

        error_code = contacts_record_create(_contacts_image._uri, &image);
        ```

     2. Define the image, and set the image using the `contacts_record_set_str()` function with the `_contacts_image.path` property as the second parameter:

        ```
        char *resource_path = app_get_resource_path();
        char caller_id_path[1024];
        snprintf(caller_id_path, sizeof(caller_id_path), "%s/caller_id.jpg", resource_path);
        free(resource_path);
        error_code = contacts_record_set_str(image, _contacts_image.path, caller_id_path);
        ```

     3. Set the image record as a child record of the contact record using the `contacts_record_add_child_record()` function with the `_contacts_contact.image` property as the second parameter:

        ```
        error_code = contacts_record_add_child_record(contact, _contacts_contact.image, image);
        ```

     > **Note**
     >
     > To set private images for contacts, the application must meet the following conditions:
     > - The application's private directory and files must have the `read` permission for others, such as `644`. SMACK protects the `read` permission from other applications.
     > - The application must delete the image after destroying the contact record (using the `contacts_record_destroy()` function).

   - To set an event for the contact:

     An event consists of an event type, date, and other properties. You can set various types of events for the contact, as defined in the `contacts_event_type_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__RECORD__MODULE.html#ga434cc4b7cec62ccab70fa4825ce0801d) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__RECORD__MODULE.html#ga434cc4b7cec62ccab70fa4825ce0801d) applications). If the event type is `CONTACTS_EVENT_TYPE_CUSTOM`, you can set a custom label for the event using the `contacts_record_set_str()` function with the `_contacts_event.label` property as the second parameter.

     To set a birthday event:

     1. Create an event record using the `contacts_record_create()` function with the `_contacts_event._uri` property as the first parameter:

        ```
        contacts_record_h event;

        error_code = contacts_record_create(_contacts_event._uri, &event);
        ```

     2. Set the event date using the `contacts_record_set_int()` function with the `_contacts_event.date` property as the second parameter. The date is an integer calculated as year * 10000 + month * 100 + day.

        ```
        int year = 1990;
        int month = 5;
        int day = 21;
        int int_date = year * 10000 + month * 100 + day;

        error_code = contacts_record_set_int(event, _contacts_event.date, int_date);
        ```

     3. Set the event type to birthday using the `contacts_record_set_int()` function with the `_contacts_event.type` property as the second parameter and the `CONTACTS_EVENT_TYPE_BIRTH` enumerator as the third parameter:

        ```
        error_code = contacts_record_set_int(event, _contacts_event.type, CONTACTS_EVENT_TYPE_BIRTH);
        ```

     4. Set the event record as a child record of the contact record using the `contacts_record_add_child_record()` function with the `_contacts_contact.event` property as the second parameter:

        ```
        error_code = contacts_record_add_child_record(contact, _contacts_contact.event, event);
        ```

   - To set the contact's phone number:

     1. Create a phone number record using the `contacts_record_create()` function with the `_contacts_number._uri` property as the first parameter:

        ```
        contacts_record_h number;

        error_code = contacts_record_create(_contacts_number._uri, &number);
        ```

     2. Set the phone number using the `contacts_record_set_str()` function with the `_contacts_number.number` property as the second parameter:

        ```
        error_code = contacts_record_set_str(number, _contacts_number.number, "+8210-1234-5678");
        ```

     3. Set the phone number record as a child record of the contact record using the `contacts_record_add_child_record()` function with the `_contacts_contact.number` property as the second parameter:

        ```
        error_code = contacts_record_add_child_record(contact, _contacts_contact.number, number);
        ```

   Set other contact properties similarly, as needed.

3. Insert the contact into the contact database using the `contacts_db_insert_record()` function. All child records added to the contact using the `contacts_record_add_child_record()` function are inserted automatically along with the parent.

   The system assigns a unique ID to the contact, and the function returns it as its second parameter

   ```
   int id = -1;

   error_code = contacts_db_insert_record(contact, &id);
   ```

4. Destroy the contact handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(contact, true);
   ```

   If you set the second parameter to `true`, all child records of the given record are also destroyed, irrespective of how the child records were added (individually or along with their parent record).

<a name="get_contact"></a>
## Retrieving Persons

You can access contact details through persons.

To retrieve a single person:

1. Retrieve a person record using the `contacts_db_get_record()` function with the person ID as the second parameter:

   ```
   contacts_record_h person = NULL;
   const int person_id = ...; /* Get the person ID */
   int error_code;

   error_code = contacts_db_get_record(_contacts_person._uri, person_id, &person);
   ```

2. When no longer needed, destroy the person handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(person, true);
   ```

To retrieve multiple persons:

1. Retrieve a list of all persons, or a list limited with a filter or search keyword:

   - To retrieve a list of all persons, use the `contacts_db_get_all_records()` function:

     ```
     contacts_list_h list = NULL;

     error_code = contacts_db_get_all_records(_contacts_person._uri, 0, 0, &list);
     ```

   - To retrieve a filtered list of persons:

     1. Define a list handle variable, and create a query handle using the `contacts_query_create()` function:

        ```
        contacts_list_h list = NULL;
        contacts_query_h query = NULL;

        error_code = contacts_query_create(_contacts_person._uri, &query);
        ```

     2. Create a filter handle using the `contacts_filter_create()` function:

        ```
        contacts_filter_h filter = NULL;

        error_code = contacts_filter_create(_contacts_person._uri, &filter);
        ```

     3. Add a filtering condition using a `contacts_filter_add_XXX()` function.

        The following example adds a string-based filtering condition that retrieves the persons whose display name contains the string "John":

        ```
        error_code = contacts_filter_add_str(filter, _contacts_person.display_name,
                                             CONTACTS_MATCH_CONTAINS, "John");
        ```

     4. To add more conditions, define an operator between the conditions.

        The following example first adds an AND operator and then a bool-based filtering condition that retrieves the persons who are set as favorites.

        The combination of the AND operator and the 2 conditions means that the filter only retrieves the persons whose display name contains the string "John" and who are set as favorites.

        ```
        error_code = contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_AND);

        error_code = contacts_filter_add_bool(filter, _contacts_person.is_favorite, true);
        ```

     5. Set the filter to the query using the `contacts_query_set_filter()` function:

        ```
        error_code = contacts_query_set_filter(query, filter);
        ```

     6. Retrieve the filtered list of persons using the `contacts_db_get_records_with_query()` function:

        ```
        error_code = contacts_db_get_records_with_query(query, 0, 0, &list);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all persons matching the query.

     7. When no longer needed, destroy the filter and query handles and release all their resources using the `contacts_filter_destroy()` and `contacts_query_destroy()` functions:

        ```
        contacts_filter_destroy(filter);
        contacts_query_destroy(query);
        ```

   - To retrieve a list of persons matching a search keyword, use the `contacts_db_search_records()` function with the search keyword as the second parameter.

     The following example shows how to find all person records that contain the keyword "John":

     ```
     contacts_list_h list = NULL;

     error_code = contacts_db_search_records(_contacts_person._uri, "John", 0, 0, &list);
     ```

2. Iterate through the list of found persons, and retrieve person details:

   1. Use a loop to iterate through the list and retrieve the person details.

      Move forward and backward within the list using the `contacts_list_next()` and `contacts_list_prev()` functions, and retrieve the current person using the `contacts_list_get_current_record_p()` function.

      > **Note**
      >
      > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

      The following example iterates through the list and retrieves the display name of each person:

      ```
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          char *display_name;
          error_code = contacts_record_get_str_p(record, _contacts_person.display_name, &display_name);
          dlog_print(DLOG_DEBUG, LOG_TAG, "display_name: %s", display_name);

          error_code = contacts_list_next(list);
      }
      ```

   2. Optionally, retrieve more details of each person using the `contacts_gl_person_data_t` structure:

      ```
      contacts_gl_person_data_t *gl_person_data = NULL;
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          gl_person_data = _create_gl_person_data(record);
          /* You can get, for example, display name: */
          /* gl_person_data->display_name */

          _free_gl_person_data(gl_person_data);

          error_code = contacts_list_next(list);
      }
      ```

      Define the `contacts_gl_person_data_t` structure and the functions for using the structure:

      ```
      struct _contacts_gl_person_data {
          int id;
          char *display_name;
          char *default_phone_number;
          contacts_list_h associated_contacts;
      };
      typedef struct _contacts_gl_person_data contacts_gl_person_data_t;

      /* Release the resources allocated to the structure */
      static void
      _free_gl_person_data(contacts_gl_person_data_t *gl_person_data)
      {
          if (NULL == gl_person_data)
              return;

          free(gl_person_data->display_name);
          free(gl_person_data->default_phone_number);
          contacts_list_destroy(gl_person_data->associated_contacts, true);
          free(gl_person_data);
      }

      /* Create the structure for a person */
      static contacts_gl_person_data_t*
      _create_gl_person_data(contacts_record_h record)
      {
          contacts_gl_person_data_t *gl_person_data;

          gl_person_data = malloc(sizeof(contacts_gl_person_data_t));
          memset(gl_person_data, 0x0, sizeof(contacts_gl_person_data_t));
          if (contacts_record_get_int(record, _contacts_person.id, &gl_person_data->id) != CONTACTS_ERROR_NONE) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get person id failed ");
              _free_gl_person_data(gl_person_data);

              return NULL;
          }
          if (false == _get_display_name(record, &gl_person_data->display_name)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "_get_display_name() failed ");
              _free_gl_person_data(gl_person_data);

              return NULL;
          }
          if (false == _get_default_phone_number(record, &gl_person_data->default_phone_number)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "_get_default_phone_number() failed ");
              _free_gl_person_data(gl_person_data);

              return NULL;
          }
          if (false == _get_associated_contacts(record, &gl_person_data->associated_contacts)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "_get_associated_contacts() failed ");
              _free_gl_person_data(gl_person_data);

              return NULL;
          }
          _print_phone_numbers(gl_person_data->associated_contacts);
          _print_events(gl_person_data->associated_contacts);

          return gl_person_data;
      }
      ```

      Define the functions for retrieving the person details:

      - Retrieve the person's display name using the `contacts_record_get_str()` function with the `_contacts_person.display_name` property as the second parameter:

        ```
        static bool
        _get_display_name(contacts_record_h record, char **display_name)
        {
            int error_code;

            error_code = contacts_record_get_str(record, _contacts_person.display_name, display_name);
            dlog_print(DLOG_DEBUG, LOG_TAG, "display name: %s", *display_name);
            if (error_code != CONTACTS_ERROR_NONE)
                return false;

            return true;
        }
        ```

      - Retrieve the contacts associated with the person using a query:

        ```
        static bool
        _get_associated_contacts(contacts_record_h record, contacts_list_h *associated_contacts)
        {
            int error_code;
            int person_id;
            contacts_query_h query = NULL;
            contacts_filter_h filter = NULL;

            /* Retrieve the person ID from the person record */
            error_code = contacts_record_get_int(record, _contacts_person.id, &person_id);

            /* Create a contact query with a filter for the person ID */
            error_code = CONTACTS_ERROR_NONE;
            error_code += contacts_query_create(_contacts_contact._uri, &query);
            error_code += contacts_filter_create(_contacts_contact._uri, &filter);
            error_code += contacts_filter_add_int(filter, _contacts_contact.person_id,
                                                  CONTACTS_MATCH_EQUAL, person_id);
            error_code += contacts_query_set_filter(query, filter);

            /* Query to get a list of all contacts associated with the person ID */
            error_code += contacts_db_get_records_with_query(query, 0, 0, associated_contacts);

            /* Destroy the handles and release all their resources */
            contacts_filter_destroy(filter);
            contacts_query_destroy(query);

            if (error_code != CONTACTS_ERROR_NONE)
                return false;

            return true;
        }
        ```

      - Retrieve the phone numbers of the associated contacts by iterating through the contacts list retrieved in the previous step.

        ```
        static void
        _print_phone_numbers(contacts_list_h associated_contacts)
        {
            int error_code;
            contacts_record_h contact;
            if (NULL == associated_contacts) {
                dlog_print(DLOG_ERROR, LOG_TAG, "associated_contacts is NULL");

                return;
            }
            /* Iterate through the list of associated contacts */
            while (contacts_list_get_current_record_p(associated_contacts, &contact) == CONTACTS_ERROR_NONE) {
                int i;
                unsigned int count = 0;

                /*
                   Determine the number of phone number records
                   associated with the contact (as child records)
                */
                error_code = contacts_record_get_child_record_count(contact, _contacts_contact.number, &count);
                if (CONTACTS_ERROR_NONE != error_code) {
                    dlog_print(DLOG_ERROR, LOG_TAG, "contacts_record_get_child_record_count(%d)", error_code);

                    return;
                }
                /*
                   Iterate through the contact's phone number records
                   and retrieve the phone number details
                */
                for (i = 0; i < count; i++) {
                    contacts_record_h number = NULL;
                    error_code = contacts_record_get_child_record_at_p(contact, _contacts_contact.number,
                                                                       i, &number);
                    if (error_code != CONTACTS_ERROR_NONE)
                        continue;

                    /* Retrieve the phone number ID */
                    int number_id;
                    contacts_record_get_int(number, _contacts_number.id, &number_id);
                    dlog_print(DLOG_DEBUG, LOG_TAG, "number id: %d", number_id);

                    /* Retrieve the actual phone number */
                    char *number_str = NULL;
                    contacts_record_get_str_p(number, _contacts_number.number, &number_str);
                    dlog_print(DLOG_DEBUG, LOG_TAG, "number: %s", number_str);
                }
                error_code = contacts_list_next(associated_contacts);
            }
        }
        ```

      - Retrieve the person's default phone number.

        If a person is associated with multiple phone numbers, one of them is defined as the person's default phone number. To determine the default phone number, check the `is_primary_default` property of the `_contacts_person_number` view for the person's phone numbers. For the default phone number, the property is set to `true`.

        The following example shows how to retrieve a person's default phone number using a query:

        ```
        static bool
        _get_default_phone_number(contacts_record_h record, char **default_phone_number)
        {
            contacts_query_h query = NULL;
            contacts_filter_h filter = NULL;
            contacts_list_h list = NULL;
            contacts_record_h record_person_number = NULL;
            int person_id;
            int error_code = CONTACTS_ERROR_NONE;

            /* Retrieve the person ID from the person record */
            error_code += contacts_record_get_int(record, _contacts_person.id, &person_id);

            /*
               Create a phone number query with filters
               for the person ID and default phone number
            */
            error_code += contacts_query_create(_contacts_person_number._uri, &query);
            error_code += contacts_filter_create(_contacts_person_number._uri, &filter);
            error_code += contacts_filter_add_int(filter, _contacts_person_number.person_id,
                                                  CONTACTS_MATCH_EQUAL, person_id);
            error_code += contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_AND);
            error_code += contacts_filter_add_bool(filter, _contacts_person_number.is_primary_default,
                                                   true);
            error_code += contacts_query_set_filter(query, filter);

            /* Query to get phone number records containing the default number */
            error_code += contacts_db_get_records_with_query(query, 0, 0, &list);

            /* Retrieve the current record from the query list */
            error_code += contacts_list_get_current_record_p(list, &record_person_number);

            /* Retrieve the phone number from the phone number record */
            error_code += contacts_record_get_str(record_person_number, _contacts_person_number.number,
                                                  default_phone_number);

            /* Destroy the handles and release all their resources */
            contacts_list_destroy(list, true);
            contacts_filter_destroy(filter);
            contacts_query_destroy(query);

            if (error_code != CONTACTS_ERROR_NONE)
                return false;

            return true;
        }
        ```

      - Retrieve the events associated with the person (events of the associated contacts) by iterating through the contacts list:

        ```
        static void
        _print_events(contacts_list_h associated_contacts)
        {
            int error_code;
            contacts_record_h contact;
            if (NULL == associated_contacts) {
                dlog_print(DLOG_ERROR, LOG_TAG, "associated_contacts is NULL");

                return;
            }
            /* Iterate through the list of associated contacts */
            while (contacts_list_get_current_record_p(associated_contacts, &contact) == CONTACTS_ERROR_NONE) {
                int i;
                unsigned int count = 0;

                /*
                   Determine the number of event records
                   associated with the contact (as child records)
                */
                error_code = contacts_record_get_child_record_count(contact, _contacts_contact.event, &count);
                if (CONTACTS_ERROR_NONE != error_code) {
                    dlog_print(DLOG_ERROR, LOG_TAG, "contacts_record_get_child_record_count(%d)", error_code);

                    return;
                }
                /* Iterate through the contact events and retrieve the details */
                for (i = 0; i < count; i++) {
                    contacts_record_h event = NULL;
                    error_code = contacts_record_get_child_record_at_p(contact, _contacts_contact.event,
                                                                       i, &event);
                    if (error_code != CONTACTS_ERROR_NONE)
                        continue;

                    /* Retrieve the event ID */
                    int event_id;
                    contacts_record_get_int(event, _contacts_event.id, &event_id);
                    dlog_print(DLOG_DEBUG, LOG_TAG, "event id: %d", event_id);

                    /* Retrieve the event date */
                    int date;
                    contacts_record_get_int(event, _contacts_event.date, &date);
                    dlog_print(DLOG_DEBUG, LOG_TAG, "event: %d", date);
                }
                error_code = contacts_list_next(associated_contacts);
            }
        }
        ```

3. When no longer needed, destroy the list handle and release all its resources using the `contacts_list_destroy()` function:

   ```
   contacts_list_destroy(list, true);
   ```

<a name="update_contact"></a>
## Updating a Contact

To update contact details:

1. Retrieve the contact you want to update using the `contacts_db_get_record()` function with the contact ID as the second parameter:

   ```
   int contact_id = ...; /* Get the contact ID */
   contacts_record_h contact = NULL;

   error_code = contacts_db_get_record(_contacts_contact._uri, contact_id, &contact);
   ```

   You can also retrieve the contact using a search function, such as `contacts_db_get_records_with_query()`.

2. Set the properties you want to update.

   The following example sets a new first name for the contact:

   ```
   contacts_record_h name = NULL;
   /* Retrieve the contact's name record */
   /* Record index is set to 0, since there is only 1 child record of type "name" */
   error_code = contacts_record_get_child_record_at_p(contact, _contacts_contact.name, 0, &name);
   /* Change the first name in the name record */
   error_code = contacts_record_set_str(name, _contacts_name.first, "Mark");
   ```

   The following example sets a new birthday event for the contact:

   ```
   contacts_record_h event = NULL;
   /* Retrieve the contact's birthday event record */
   error_code = contacts_record_get_child_record_at_p(contact, _contacts_contact.event, 0, &event);
   /* Change the date in the event record */
   int new_date = 1990 * 10000 + 6 * 100 + 21;
   error_code = contacts_record_set_int(event, _contacts_event.date, new_date);
   ```

   The example assumes the birthday event is the only event defined for the contact, meaning you can retrieve the event record using the `contacts_record_get_child_record_at_p()` function with the record index set to 0. If the contact has multiple events defined, you must iterate through them.

   > **Note**
   >
   > The `contacts_record_set_XXX()` functions only change the data in the memory object, not in the contact database. Normally, to update the database, you need to update each record separately using the `contacts_db_update_record()` function. However, if you retrieve a child record using the `contacts_record_get_child_record_at_p()` function, you only need to update the parent record to the database; the child record is updated automatically with the parent record.

3. Update the contact using the `contacts_db_update_record()` function:

   ```
   error_code = contacts_db_update_record(contact);
   ```

4. When no longer needed, destroy the contact handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(contact, true);
   ```

<a name="delete_contact"></a>
## Deleting a Person

To delete a person, use the `contacts_db_delete_record()` function with the person ID as the second parameter:

```
int person_id = ...; /* Get the person ID */

error_code = contacts_db_delete_record(_contacts_person._uri, person_id);
```

<a name="link_contact"></a>
## Linking and Unlinking Persons and Contacts

Linking a contact to a person associates the contact with that person. Unlinking the contact from the person removes the association.

To link and unlink persons and contacts:

- To manually link a person to another person, use the `contacts_person_link_person()` function. The function links the contacts of the other person (second parameter) to the base person (first parameter) and deletes the former from the contact database. The base person is left with both their original contacts and the other person's contacts.

  ```
  int person_id1 = ...; /* Get the base person ID */
  int person_id2 = ...; /* Get another person ID */

  error_code = contacts_person_link_person(person_id1, person_id2);
  ```

- To automatically link a new contact to an existing person, set the `_contacts_contact.link_mode` property of the contact to `CONTACTS_CONTACT_LINK_MODE_NONE` when [creating the contact](#create_contact).

  The contacts service determines the link based on the `_contacts_number.number` and `_contacts_email.email` properties of the contact. If an existing person has the same phone number or email address, but in a different address book, the contact is automatically linked to the person. If the phone number or email address lead to an existing contact in the same address book, the link does not work.

  ```
  contacts_record_h contact = NULL;

  error_code = CONTACTS_ERROR_NONE;
  error_code += contacts_record_create(_contacts_contact._uri, &contact);
  error_code += contacts_record_set_int(contact, _contacts_contact.link_mode, CONTACTS_CONTACT_LINK_MODE_NONE);

  contacts_record_h name = NULL;
  error_code += contacts_record_create(_contacts_name._uri, &name);
  error_code += contacts_record_set_str(name, _contacts_name.first, "John");
  error_code += contacts_record_add_child_record(contact, _contacts_contact.name, name);

  contacts_record_h number = NULL;
  error_code += contacts_record_create(_contacts_number._uri, &number);
  error_code += contacts_record_set_str(number, _contacts_number.number, "+8210-1234-5678");
  error_code += contacts_record_add_child_record(contact, _contacts_contact.number, number);

  /*
     Contact is linked automatically if an existing person
     has the same number in a different address book
  */
  error_code += contacts_db_insert_record(contact, NULL);

  contacts_record_destroy(contact, true);
  ```

- To unlink a contact from a person, use the `contacts_person_unlink_contact()` function. The function removes the contact (second parameter) from the person (first parameter), creates a new person (third parameter), and links the contact to the new person.

  ```
  int person_id = ...; /* Get the person ID */
  int contact_id = ...; /* Get the contact ID */
  int unlinked_person_id;

  error_code = contacts_person_unlink_contact(person_id, contact_id, &unlinked_person_id);
  ```

<a name="manage_contact"></a>
## Managing Favorites

To set or unset a person as a favorite:

- To set a new person as a favorite when creating the corresponding new contact, set the `_contacts_contact.is_favorite` property of the contact to `true`. When you insert the contact into the contact database, the new person that is created for the contact is automatically set as a favorite.

  ```
  contacts_record_h contact = NULL;

  error_code = CONTACTS_ERROR_NONE;
  error_code += contacts_record_create(_contacts_contact._uri, &contact);
  error_code += contacts_record_set_bool(contact, _contacts_contact.is_favorite, true);
  /* Set other properties */

  /* New person is set as a favorite */
  error_code += contacts_db_insert_record(contact, NULL);

  contacts_record_destroy(contact, true);
  ```

- To set an existing person as a favorite, update the person record by setting its `_contacts_person.is_favorite` property to `true`:

  ```
  int person_id = ...; /* Get the person ID */
  contacts_record_h person = NULL;

  error_code = contacts_db_get_record(_contacts_person._uri, person_id, &person);

  error_code = contacts_record_set_bool(person, _contacts_person.is_favorite, true);

  error_code = contacts_db_update_record(person);

  contacts_record_destroy(person, true);
  ```

- To unset an existing person as a favorite, update the person record by setting its `_contacts_person.is_favorite` property to `false`:

  ```
  int person_id = ...; /* Get the person ID */
  contacts_record_h person = NULL;

  error_code = contacts_db_get_record(_contacts_person._uri, person_id, &person);

  error_code = contacts_record_set_bool(person, _contacts_person.is_favorite, false);

  error_code = contacts_db_update_record(person);

  contacts_record_destroy(person, true);
  ```

<a name="monitor_contact"></a>
## Monitoring Person Changes

To receive a notification whenever the person details change:

1. Register a callback using the `contacts_db_add_changed_cb()` function:

   ```
   error_code = contacts_db_add_changed_cb(_contacts_person._uri, _person_changed_callback, NULL);
   ```

2. Define the person change callback.

   The following example shows how to retrieve the new person details in the callback:

   ```
   static contacts_gl_person_data_t *_gl_person_data = ...;

   static void
   _person_changed_callback(const char *view_uri, void *user_data)
   {
       if (0 != strcmp(view_uri, _contacts_person._uri))
           return;

       if (_gl_person_data == NULL)
           return;

       int person_id = _gl_person_data->id;
       _free_gl_person_data(_gl_person_data);
       _gl_person_data = NULL;

       contacts_record_h record = NULL;
       int error_code;
       error_code = contacts_db_get_record(_contacts_person._uri, person_id, &record);
       if (error_code != CONTACTS_ERROR_NONE)
           return;

       _gl_person_data = _create_gl_person_data(record);
       /* Use _gl_person_data */

       contacts_record_destroy(record, true);
   }
   ```

<a name="create"></a>
## Creating a Group

A group is a collection of contacts from the same address book. Creating a new group involves creating a group handle, setting the group properties, and inserting the group into the contact database. To add contacts to the group, see [Managing Group Members](#manage).

To create a new group:

1. Create a group handle using the `contacts_record_create()` function with the `_contacts_group._uri` property as the first parameter and the group handle variable as the second parameter:

   ```
   contacts_record_h group = NULL;

   error_code = contacts_record_create(_contacts_group._uri, &group);
   ```

2. Set the group properties:

   - To set the group name, use the `contacts_record_set_str()` function with the `_contacts_group.name` property as the second parameter:

     ```
     error_code = contacts_record_set_str(group, _contacts_group.name, "Neighbors");
     ```

   - To set the group image, define the path to the image file, and set the path to the group using the `contacts_record_set_str()` function with the `_contacts_group.image_path` property as the second parameter:

     ```
     char *resource_path = app_get_resource_path();
     char temp_path[1024];
     snprintf(temp_path, sizeof(temp_path), "%s/group_image.jpg", resource_path);
     error_code = contacts_record_set_str(group, _contacts_group.image_path, temp_path);
     free(resource_path);
     ```

   - To set the group ringtone, define the path to the ringtone file, and set the path to the group using the `contacts_record_set_str()` function with the `_contacts_group.ringtone_path` property as the second parameter:

     ```
     char *resource_path = app_get_resource_path();
     char temp_path[1024];
     snprintf(temp_path, sizeof(temp_path), "%s/ringtone.mp3", resource_path);
     error_code = contacts_record_set_str(group, _contacts_group.ringtone_path, temp_path);
     free(resource_path);
     ```

   Set other group properties similarly, as needed.

3. Insert the group into the contact database using the `contacts_db_insert_record()` function:

   ```
   int added_group_id = -1;

   error_code = contacts_db_insert_record(group, &added_group_id);
   ```

4. When no longer needed, destroy the group handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(group, true);
   ```

<a name="get"></a>
## Retrieving Groups

To retrieve a single group:

1. Retrieve a group record using the `contacts_db_get_record()` function with the group ID as the second parameter:

   ```
   contacts_record_h group;
   int group_id = ...; /* Get the group ID */
   int error_code;

   error_code = contacts_db_get_record(_contacts_group._uri, group_id, &group);
   ```

2. When no longer needed, destroy the group handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(group, true);
   ```

To retrieve multiple groups:

1. Retrieve a list of all groups, or retrieve a filtered list of groups:

   - To retrieve a list of all groups, use the `contacts_db_get_all_records()` function:

     ```
     contacts_list_h list = NULL;

     error_code = contacts_db_get_all_records(_contacts_group._uri, 0, 0, &list);
     ```

   - To retrieve a filtered list of groups:

     1. Define a list handle variable, and create a query handle using the `contacts_query_create()` function:

        ```
        contacts_list_h list = NULL;
        contacts_query_h query = NULL;

        error_code = contacts_query_create(_contacts_group._uri, &query);
        ```

     2. Create a filter handle using the `contacts_filter_create()` function:

        ```
        contacts_filter_h filter = NULL;

        error_code = contacts_filter_create(_contacts_group._uri, &filter);
        ```

     3. Add a filtering condition using a `contacts_filter_add_XXX()` function.

        The following example adds a string-based filtering condition that retrieves any group whose name contains the string "neighbors":

        ```
        error_code = contacts_filter_add_str(filter, _contacts_group.name,
                                             CONTACTS_MATCH_CONTAINS, "neighbors");
        ```

     4. To add more conditions, define an operator between the conditions.

        The following example first adds an OR operator and then a string-based filtering condition that retrieves any group whose name contains the string "friend".

        The combination of the OR operator and the 2 conditions means that the filter only retrieves groups whose name contains the string "neighbors" or "friend".

        ```
        error_code = contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_OR);

        error_code = contacts_filter_add_str(filter, _contacts_group.name,
                                             CONTACTS_MATCH_CONTAINS, "friend");
        ```

     5. Set the filter to the query using the `contacts_query_set_filter()` function:

        ```
        error_code = contacts_query_set_filter(query, filter);
        ```

     6. Retrieve the filtered list of groups using the `contacts_db_get_records_with_query()` function:

        ```
        error_code = contacts_db_get_records_with_query(query, 0, 0, &list);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all groups matching the query.

     7. When no longer needed, destroy the filter and query handles and release all their resources using the `contacts_filter_destroy()` and `contacts_query_destroy()` functions:

        ```
        contacts_filter_destroy(filter);
        contacts_query_destroy(query);
        ```

2. Iterate through the list of found groups, and retrieve group details:

   1. Use a loop to iterate through the list and retrieve the group details.

      Move forward and backward within the list using the `contacts_list_next()` and `contacts_list_prev()` functions, and retrieve the current group using the `contacts_list_get_current_record_p()` function.

      > **Note**
      >
      > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

      The following example iterates through the list and retrieves the name of each group:

      ```
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          char *name;
          error_code = contacts_record_get_str_p(record, _contacts_group.name, &name);
          dlog_print(DLOG_DEBUG, LOG_TAG, "group name: %s", name);

          error_code = contacts_list_next(list);
          if (error_code != CONTACTS_ERROR_NONE)
              break;
      }
      ```

   2. Optionally, retrieve more details of each group using the `contacts_gl_group_data_t` structure:

      ```
      contacts_gl_group_data_t *gl_group_data = NULL;
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          gl_group_data = _create_gl_group_data(record);
          /* You can get, for example, display name: */
          /* gl_group_data->name */

          error_code = contacts_list_next(list);
          if (error_code != CONTACTS_ERROR_NONE)
              break;
      }
      ```

      Define the `contacts_gl_group_data_t` structure and the functions for using the structure:

      ```
      struct _contacts_gl_group_data {
          int id;
          char *name;
          char *image_path;
          char *ringtone_path;
      };
      typedef struct _contacts_gl_group_data contacts_gl_group_data_t;

      /* Release the resources allocated to the structure */
      static void
      _free_gl_group_data(contacts_gl_group_data_t *gl_group_data)
      {
          if (NULL == gl_group_data)
              return;

          free(gl_group_data->name);
          free(gl_group_data->image_path);
          free(gl_group_data->ringtone_path);
          free(gl_group_data);
      }

      /* Create the structure for a group */
      static contacts_gl_group_data_t*
      _create_gl_group_data(contacts_record_h record)
      {
          contacts_gl_group_data_t *gl_group_data;
          int error_code;

          gl_group_data = malloc(sizeof(contacts_gl_group_data_t));
          memset(gl_group_data, 0x0, sizeof(contacts_gl_group_data_t));

          if (CONTACTS_ERROR_NONE != contacts_record_get_int(record, _contacts_group.id,
                                                             &gl_group_data->id)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get group ID failed ");
              _free_gl_group_data(gl_group_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record, _contacts_group.name,
                                                             &gl_group_data->name)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get group name failed ");
              _free_gl_group_data(gl_group_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record, _contacts_group.image_path,
                                                             &gl_group_data->image_path)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get group image failed ");
              _free_gl_group_data(gl_group_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record, _contacts_group.ringtone_path,
                                                             &gl_group_data->ringtone_path)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get group ringtone failed ");
              _free_gl_group_data(gl_group_data);

              return NULL;
          }

          return gl_group_data;
      }
      ```

3. When no longer needed, destroy the list handle and release all its resources using the `contacts_list_destroy()` function:

   ```
   contacts_list_destroy(list, true);
   ```

<a name="update"></a>
## Updating a Group

To update group details:

1. Retrieve the group you want to update using the `contacts_db_get_record()` function with the group ID as the second parameter:

   ```
   int group_id = ...; /* Get the group ID */
   contacts_record_h group = NULL;

   error_code = contacts_db_get_record(_contacts_group._uri, group_id, &group);
   ```

   You can also retrieve the group using a search function, such as `contacts_db_get_records_with_query()`.

2. Set the properties you want to update.

   The following example sets a new name and image for the group:

   ```
   error_code = contacts_record_set_str(group, _contacts_group.name, "Family");

   char *resource_path = app_get_resource_path();
   char temp_path[1024];
   snprintf(temp_path, sizeof(temp_path), "%s/group_image_new.jpg", resource_path);
   free(resource_path);
   error_code = contacts_record_set_str(group, _contacts_group.image_path, temp_path);
   ```

3. Update the group using the `contacts_db_update_record()` function:

   ```
   error_code = contacts_db_update_record(group);
   ```

   Since the update concerns direct properties of the group record, not child records, updating the group record by definition also updates the properties.

4. When no longer needed, destroy the group handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(group, true);
   ```
<a name="delete"></a>
## Deleting a Group

To delete a group, use the `contacts_db_delete_record()` function with the group ID as the second parameter:

```
int group_id = ...; /* Get the group ID */

error_code = contacts_db_delete_record(_contacts_group._uri, group_id);
```

<a name="manage"></a>
## Managing Group Members

Group members are contacts from the same address book. Each contact is associated with a person.

To add, remove, and retrieve group members:

- To add a new contact to a group, retrieve the contact ID and the group ID, and use the `contacts_group_add_contact()` function:

  ```
  int contact_id = ...; /* Get the contact ID */
  int group_id = ...; /* Get the group ID */

  error_code = contacts_group_add_contact(group_id, contact_id);
  ```

- To remove a contact from a group, use the `contacts_group_remove_contact()` function:

  ```
  error_code = contacts_group_remove_contact(group_id, contact_id);
  ```

- To retrieve all persons assigned to a group:

  1. Create and run a query for retrieving a list of all persons assigned to the group:

     ```
     contacts_query_h query = NULL;
     contacts_filter_h filter = NULL;
     contacts_list_h list = NULL;

     /* Create a person query with a filter for group ID */
     contacts_query_create(_contacts_person_group_assigned._uri, &query);
     contacts_filter_create(_contacts_person_group_assigned._uri, &filter);
     contacts_filter_add_int(filter, _contacts_person_group_assigned.group_id,
                             CONTACTS_MATCH_EQUAL, group_id);
     contacts_query_set_filter(query, filter);

     /* Query to get a list of all persons assigned to the specified group */
     contacts_db_get_records_with_query(query, 0, 0, &list);
     ```

  2. Iterate through the list, and retrieve the person details.

     The following example iterates through the list and retrieves the ID and display name of each person:

     ```
     contacts_record_h person = NULL;
     int error_code;

     while (contacts_list_get_current_record_p(list, &person) == CONTACTS_ERROR_NONE) {
         int person_id;
         contacts_record_get_int(person, _contacts_person_group_assigned.person_id, &person_id);
         dlog_print(DLOG_DEBUG, LOG_TAG, "Person id: %d", person_id);

         char *display_name;
         contacts_record_get_str_p(person, _contacts_person_group_assigned.display_name, &display_name);
         dlog_print(DLOG_DEBUG, LOG_TAG, "Display name: %s", display_name);

         error_code = contacts_list_next(list);
         if (error_code != CONTACTS_ERROR_NONE)
             break;
     }
     ```

  3. When no longer needed, destroy the list, filter, and query handles and release all their resources using the `contacts_list_destroy()`, `contacts_filter_destroy()`, and `contacts_query_destroy()` functions:

     ```
     contacts_list_destroy(list, true);
     contacts_filter_destroy(filter);
     contacts_query_destroy(query);
     ```
<a name="monitor"></a>
## Monitoring Group Changes

To receive a notification whenever the group details change:

1. Register a callback using the `contacts_db_add_changed_cb()` function:

   ```
   error_code = contacts_db_add_changed_cb(_contacts_group._uri, _group_changed_callback, NULL);
   ```

2. Define the group change callback.

   The following example shows how to retrieve the new group details in the callback:

   ```
   static contacts_gl_group_data_t *_gl_group_data = ...;

   static void
   _group_changed_callback(const char *view_uri, void *user_data)
   {
       if (0 != strcmp(view_uri, _contacts_group._uri))
           return;

       if (_gl_group_data == NULL)
           return;

       int group_id = _gl_group_data->id;
       _free_gl_group_data(_gl_group_data);
       _gl_group_data = NULL;

       contacts_record_h record = NULL;
       int error_code;
       error_code = contacts_db_get_record(_contacts_group._uri, group_id, &record);
       if (error_code != CONTACTS_ERROR_NONE)
           return;

       _gl_group_data = _create_gl_group_data(record);
       /* Use _gl_group_data */

       contacts_record_destroy(record, true);
   }
   ```

<a name="make"></a>
## Creating a vCard

To create a vCard stream from a person:

1. Retrieve the person:

   ```
   int person_id = ...; /* Get the person ID */
   contacts_record_h record = NULL;

   error_code = contacts_db_get_record(_contacts_person._uri, person_id, &record);
   ```

2. Create the vCard stream from the person:

   ```
   char *vcard_stream = NULL;
   error_code = contacts_vcard_make_from_person(record, &vcard_stream);
   ```

   > **Note**
   >
   > The contacts service allows you to create a vCard stream from a person, contact, or my profile (using the `contacts_vcard_make_from_person()`, `contacts_vcard_make_from_contact()`, or `contacts_vcard_make_from_my_profile()` function).

3. When no longer needed, free the vCard stream, destroy the person handle, and release all its resources:

   ```
   free(vcard_stream);
   contacts_record_destroy(record, true);
   ```

<a name="parse"></a>
## Parsing a vCard

To parse a vCard from a file and insert its content into the content database:

1. Parse the vCard stream using the `contacts_vcard_parse_to_contact_foreach()` function:

   ```
   char *resource_path = app_get_resource_path();
   char temp_path[1024];
   snprintf(temp_path, sizeof(temp_path), "%s/vcard.vcf", resource_path);
   free(resource_path);

   error_code = contacts_vcard_parse_to_contact_foreach(/* vCard file path */
                                                        temp_path,
                                                        /* Callback to invoke */
                                                        _vcard_parse_cb,
                                                        /* User data for callback */
                                                        NULL);
   ```

2. Define a callback that inserts the parsed contact into the contact database.

   The vCard stream can contain multiple contacts. The `contacts_vcard_parse_to_contact_foreach()` function invokes a separate callback for each parsed contact. As long as the callbacks return `true`, the foreach function continues to parse new contacts.

   ```
   static bool
   _vcard_parse_cb(contacts_record_h contact, void *user_data)
   {
       if (NULL == contact)
           return false;

       int contact_id = -1;
       error_code = contacts_db_insert_record(contact, &contact_id);
       /* Use the contact record */

       return true;
   }
   ```

<a name="sd_create"></a>
## Creating a Speed Dial

Creating a new speed dial involves creating a speed dial handle, setting the speed dial properties, and inserting the speed dial into the contact database.

To create a new speed dial:

1. Create a speed dial handle using the `contacts_record_create()` function with the `_contacts_speeddial._uri` property as the first parameter and the speed dial handle variable as the second parameter:

   ```
   contacts_record_h speeddial;

   error_code = contacts_record_create(_contacts_speeddial._uri, &speeddial);
   ```

2. Set the speed dial properties:

   - To set the speed dial number, use the `contacts_record_set_int()` function with the `_contacts_speeddial.speeddial_number` property as the second parameter:

     ```
     int speeddial_number = ...; /* Get the speed dial number */
     error_code = contacts_record_set_int(speeddial, _contacts_speeddial.speeddial_number,
                                          speeddial_number);
     ```

   - To set the ID for the speed dial number, use the `contacts_record_set_int()` function with the `_contacts_speeddial.number_id` property as the second parameter:

     ```
     int number_id = ...; /* Get the speed dial number ID */
     error_code = contacts_record_set_int(speeddial, _contacts_speeddial.number_id, number_id);
     ```

   Set other speed dial properties similarly, as needed.

3. Insert the speed dial into the contact database using the `contacts_db_insert_record()` function:

   ```
   int added_speeddial_id = -1;

   error_code = contacts_db_insert_record(speeddial, &added_speeddial_id);
   ```

4. When no longer needed, destroy the speed dial handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(speeddial, true);
   ```

<a name="sd_get"></a>
## Retrieving Speed Dials

To retrieve a single speed dial:

1. Retrieve a speed dial record using the `contacts_db_get_record()` function with the speed dial ID as the second parameter:

   ```
   contacts_record_h speeddial;
   int speeddial_id = ...; /* Get the speed dial ID */
   int error_code;

   error_code = contacts_db_get_record(_contacts_speeddial._uri, speeddial_id, &speeddial);
   ```

2. When no longer needed, destroy the speed dial handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(speeddial, true);
   ```

To retrieve multiple speed dials:

1. Retrieve a list of all speed dials, or retrieve a filtered list of speed dials:

   - To retrieve a list of all speed dials, use the `contacts_db_get_all_records()` function:

     ```
     contacts_list_h list = NULL;

     error_code = contacts_db_get_all_records(_contacts_speeddial._uri, 0, 0, &list);
     ```

   - To retrieve a filtered list of speed dials:

     1. Define a list handle variable, and create a query handle using the `contacts_query_create()` function:

        ```
        contacts_list_h list = NULL;
        contacts_query_h query = NULL;

        error_code = contacts_query_create(_contacts_speeddial._uri, &query);
        ```

     2. Create a filter handle using the `contacts_filter_create()` function:

        ```
        contacts_filter_h filter = NULL;

        error_code = contacts_filter_create(_contacts_speeddial._uri, &filter);
        ```

     3. Add a filtering condition using a `contacts_filter_add_XXX()` function.

        The following example adds an integer-based filtering condition that retrieves only speed dials whose number is less than 3:

        ```
        error_code = contacts_filter_add_int(filter, _contacts_speeddial.speeddial_number,
                                             CONTACTS_MATCH_LESS_THAN, 3);
        ```

     4. To add more conditions, define an operator between the conditions.

        The following example first adds an OR operator and then an integer-based filtering condition that retrieves only speed dials whose number is greater than 15.

        The combination of the OR operator and the 2 conditions means that the filter only retrieves speed dials whose number is less than 3 or greater than 15.

        ```
        error_code = contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_OR);

        error_code = contacts_filter_add_int(filter, _contacts_speeddial.speeddial_number,
                                             CONTACTS_MATCH_GREATER_THAN, 15);
        ```

     5. Set the filter to the query using the `contacts_query_set_filter()` function:

        ```
        error_code = contacts_query_set_filter(query, filter);
        ```

     6. Retrieve the filtered list of speed dials using the `contacts_db_get_records_with_query()` function:

        ```
        error_code = contacts_db_get_records_with_query(query, 0, 0, &list);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all speed dials matching the query.

     7. When no longer needed, destroy the filter and query handles and release all their resources using the `contacts_filter_destroy()` and `contacts_query_destroy()` functions:

        ```
        contacts_filter_destroy(filter);
        contacts_query_destroy(query);
        ```

2. Iterate through the list of found speed dials, and retrieve speed dial details:

   1. Use a loop to iterate through the list and retrieve the speed dial details.

      Move forward and backward within the list using the `contacts_list_next()` and `contacts_list_prev()` functions, and retrieve the current speed dial using the `contacts_list_get_current_record_p()` function.

      > **Note**
      >
      > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

      The following example iterates through the list and retrieves the number of each speed dial:

      ```
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          int number;
          error_code = contacts_record_get_int(record, _contacts_speeddial.speeddial_number,
                                               &number);
          dlog_print(DLOG_DEBUG, LOG_TAG, "speed dial number: %d", number);

          error_code = contacts_list_next(list);
          if (error_code != CONTACTS_ERROR_NONE)
              break;
      }
      ```

   2. Optionally, retrieve more details of each speed dial using the `contacts_gl_speeddial_data_t` structure:

      ```
      contacts_gl_speeddial_data_t *gl_speeddial_data = NULL;
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          gl_speeddial_data = _create_gl_speeddial_data(record);

          _free_gl_speeddial_data(gl_speeddial_data);

          error_code = contacts_list_next(list);
          if (error_code != CONTACTS_ERROR_NONE)
              break;
      }
      ```

      Define the `contacts_gl_speeddial_data_t` structure and the functions for using the structure:

      ```
      struct _contacts_gl_speeddial_data {
          int speeddial_number;
          char *number;
          char *display_name;
          char *image_thumbnail_path;
      };
      typedef struct _contacts_gl_speeddial_data contacts_gl_speeddial_data_t;

      /* Release the resources allocated to the structure */
      static void
      _free_gl_speeddial_data(contacts_gl_speeddial_data_t *gl_speeddial_data)
      {
          if (NULL == gl_speeddial_data)
              return;

          free(gl_speeddial_data->number);
          free(gl_speeddial_data->display_name);
          free(gl_speeddial_data->image_thumbnail_path);
          free(gl_speeddial_data);
      }

      /* Create the structure for a speed dial */
      static contacts_gl_speeddial_data_t*
      _create_gl_speeddial_data(contacts_record_h record)
      {
          contacts_gl_speeddial_data_t *gl_speeddial_data;
          int error_code;

          gl_speeddial_data = malloc(sizeof(contacts_gl_speeddial_data_t));
          memset(gl_speeddial_data, 0x0, sizeof(contacts_gl_speeddial_data_t));

          if (CONTACTS_ERROR_NONE != contacts_record_get_int(record,
                                                             _contacts_speeddial.speeddial_number,
                                                             &gl_speeddial_data->speeddial_number)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get speed dial number failed ");
              _free_gl_speeddial_data(gl_speeddial_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record,
                                                             _contacts_speeddial.number,
                                                             &gl_speeddial_data->number)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get contact number failed ");
              _free_gl_speeddial_data(gl_speeddial_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record,
                                                             _contacts_speeddial.display_name,
                                                             &gl_speeddial_data->display_name)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get display name failed ");
              _free_gl_speeddial_data(gl_speeddial_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record,
                                                             _contacts_speeddial.image_thumbnail_path,
                                                             &gl_speeddial_data->image_thumbnail_path)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get thumbnail failed ");
              _free_gl_speeddial_data(gl_speeddial_data);

              return NULL;
          }

          return gl_speeddial_data;
      }
      ```

3. When no longer needed, destroy the list handle and release all its resources using the `contacts_list_destroy()` function:

   ```
   contacts_list_destroy(list, true);
   ```

<a name="sd_update"></a>
## Updating a Speed Dial

To update speed dial details:

1. Retrieve the speed dial you want to update using the `contacts_db_get_record()` function with the speed dial number as the second parameter:

   ```
   int speeddial_number = ...; /* Get the speed dial number */
   contacts_record_h speeddial = NULL;

   error_code = contacts_db_get_record(_contacts_speeddial._uri, speeddial_number, &speeddial);
   ```

   You can also retrieve the speed dial using a search function, such as `contacts_db_get_records_with_query()`.

2. Set the properties you want to update.

   The following example sets a new ID for the speed dial number:

   ```
   int number_id = ...; /* Get the number ID */

   error_code = contacts_record_set_int(speeddial, _contacts_speeddial.number_id, number_id);
   if (error_code != CONTACTS_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "get number ID failed: %x", error_code);
   ```

3. Update the speed dial using the `contacts_db_update_record()` function:

   ```
   error_code = contacts_db_update_record(speeddial);
   ```

   Since the update concerns a direct property of the speed dial record, not a child record, updating the speed dial record by definition also updates the property.

4. When no longer needed, destroy the speed dial handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(speeddial, true);
   ```

<a name="sd_delete"></a>
## Deleting a Speed Dial

To delete a speed dial, use the `contacts_db_delete_record()` function with the speed dial number as the second parameter:

```
int speeddial_number = ...; /* Get the speed dial number */

error_code = contacts_db_delete_record(_contacts_speeddial._uri, speeddial_number);
```

<a name="pl_create"></a>
## Creating a Log

Creating a new log entry involves creating a log handle, setting the log properties, and inserting the log entry into the contact database.

To create a new log entry:

1. Create a log handle using the `contacts_record_create()` function with the `_contacts_phone_log._uri` property as the first parameter and the log handle variable as the second parameter:

   ```
   contacts_record_h log;

   error_code = contacts_record_create(_contacts_phone_log._uri, &log);
   if (error_code != CONTACTS_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "contacts_record_create failed: %x", error_code);
   ```

2. Set the log properties:

   - To set the log type, use the `contacts_record_set_int()` function with the `_contacts_phone_log.log_type` property as the second parameter. The third parameter defines the log type using the values of the `contacts_phone_log_type_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__RECORD__MODULE.html#gaafc3f61866231c01314c1d3f7da6038b) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__RECORD__MODULE.html#gaafc3f61866231c01314c1d3f7da6038b) applications).

     ```
     error_code = contacts_record_set_int(log, _contacts_phone_log.log_type,
                                          CONTACTS_PLOG_TYPE_VOICE_INCOMING);
     if (error_code != CONTACTS_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set log type failed: %x", error_code);
     ```

   - To set the log time (calculated as number of seconds since 1970-01-01 00:00:00 UTC), use the `contacts_record_set_int()` function with the `_contacts_phone_log.log_time` property as the second parameter:

     ```
     error_code = contacts_record_set_int(log, _contacts_phone_log.log_time, (int)time(NULL));
     if (error_code != CONTACTS_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set log time failed: %x", error_code);
     ```

   - To set the log duration (in practice, the message ID, email ID, or call duration in seconds), use the `contacts_record_set_int()` function with the `_contacts_phone_log.extra_data1` property as the second parameter:

     ```
     error_code = contacts_record_set_int(log, _contacts_phone_log.extra_data1, 37);
     if (error_code != CONTACTS_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set duration failed: %x", error_code);
     ```

   - To set the log address (in practice, the phone number or email address), use the `contacts_record_set_str()` function with the `_contacts_phone_log.address` property as the second parameter:

     ```
     error_code = contacts_record_set_str(log, _contacts_phone_log.address, "+8231-1234-5678");
     if (error_code != CONTACTS_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "set address failed: %x", error_code);
     ```

   Set other log properties similarly, as needed.

3. Insert the log into the contact database using the `contacts_db_insert_record()` function:

   ```
   int added_log_id = -1;

   error_code = contacts_db_insert_record(log, &added_log_id);
   if (error_code != CONTACTS_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "contacts_db_insert_record failed: %x", error_code);
   ```

4. When no longer needed, destroy the log handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(log, true);
   ```

<a name="pl_get"></a>
## Retrieving Logs

To retrieve a single log entry:

1. Retrieve a log record using the `contacts_db_get_record()` function with the log ID as the second parameter:

   ```
   contacts_record_h log;
   int log_id = ...; /* Get the log ID */
   int error_code;

   error_code = contacts_db_get_record(_contacts_phone_log._uri, log_id, &log);
   if (error_code != CONTACTS_ERROR_NONE)
       dlog_print(DLOG_ERROR, LOG_TAG, "get log failed: %x", error_code);
   ```

2. When no longer needed, destroy the log handle and release all its resources using the `contacts_record_destroy()` function:

   ```
   contacts_record_destroy(log, true);
   ```

To retrieve multiple log entries:

1. Retrieve a list of all logs, or retrieve a filtered list of logs:

   - To retrieve a list of all logs, use the `contacts_db_get_all_records()` function:

     ```
     contacts_list_h list = NULL;

     error_code = contacts_db_get_all_records(_contacts_phone_log._uri, 0, 0, &list);
     if (error_code != CONTACTS_ERROR_NONE)
         dlog_print(DLOG_ERROR, LOG_TAG, "contacts_db_get_all_records failed: %x", error_code);
     ```

   - To retrieve a filtered list of logs:

     1. Define a list handle variable, and create a query handle using the `contacts_query_create()` function:

        ```
        contacts_list_h list = NULL;
        contacts_query_h query = NULL;

        error_code = contacts_query_create(_contacts_phone_log._uri, &query);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "contacts_query_create failed: %x", error_code);
        ```

     2. Create a filter handle using the `contacts_filter_create()` function:

        ```
        contacts_filter_h filter = NULL;

        error_code = contacts_filter_create(_contacts_phone_log._uri, &filter);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "contacts_filter_create failed: %x", error_code);
        ```

     3. Add a filtering condition using a `contacts_filter_add_XXX()` function.

        The following example adds an integer-based filtering condition that retrieves any log whose type is `CONTACTS_PLOG_TYPE_VOICE_INCOMING`:

        ```
        error_code = contacts_filter_add_int(filter, _contacts_phone_log.log_type,
                                             CONTACTS_MATCH_EQUAL,
                                             CONTACTS_PLOG_TYPE_VOICE_INCOMING);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x", error_code);
        ```

     4. To add more conditions, define an operator between the conditions.

        The following example first adds an OR operator and then an integer-based filtering condition that retrieves any log whose type is `CONTACTS_PLOG_TYPE_VOICE_OUTGOING`.

        The combination of the OR operator and the 2 conditions means that the filter only retrieves logs whose type is `CONTACTS_PLOG_TYPE_VOICE_INCOMING` or `CONTACTS_PLOG_TYPE_VOICE_OUTGOING`.

        ```
        error_code = contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_OR);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "contacts_filter_add_operator failed: %x", error_code);

        error_code = contacts_filter_add_int(filter, _contacts_phone_log.log_type,
                                             CONTACTS_MATCH_EQUAL,
                                             CONTACTS_PLOG_TYPE_VOICE_OUTGOING);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "filter add condition failed: %x", error_code);
        ```

     5. Set the filter to the query using the `contacts_query_set_filter()` function:

        ```
        error_code = contacts_query_set_filter(query, filter);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "contacts_query_set_filter failed: %x", error_code);
        ```

     6. Retrieve the filtered list of logs using the `contacts_db_get_records_with_query()` function:

        ```
        error_code = contacts_db_get_records_with_query(query, 0, 0, &list);
        if (error_code != CONTACTS_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "contacts_db_get_records_with_query failed: %x", error_code);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all logs matching the query.

     7. When no longer needed, destroy the filter and query handles and release all their resources using the `contacts_filter_destroy()` and `contacts_query_destroy()` functions:

        ```
        contacts_filter_destroy(filter);
        contacts_query_destroy(query);
        ```

2. Iterate through the list of found logs, and retrieve log details:

   1. Use a loop to iterate through the list and retrieve the log details.

      Move forward and backward within the list using the `contacts_list_next()` and `contacts_list_prev()` functions, and retrieve the current log using the `contacts_list_get_current_record_p()` function.

      > **Note**
      >
      > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

      The following example iterates through the list and retrieves the type of each log:

      ```
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          int type;
          error_code = contacts_record_get_int(record, _contacts_phone_log.log_type, &type);
          dlog_print(DLOG_DEBUG, LOG_TAG, "log type: %d", type);

          error_code = contacts_list_next(list);
          if (error_code != CONTACTS_ERROR_NONE)
              break;
      }
      ```

   2. Optionally, retrieve more details of each log using the `contacts_gl_log_data_t` structure:

      ```
      contacts_gl_log_data_t *gl_log_data = NULL;
      contacts_record_h record;
      while (contacts_list_get_current_record_p(list, &record) == CONTACTS_ERROR_NONE) {
          gl_log_data = _create_gl_log_data(record);

          _free_gl_log_data(gl_log_data);
          error_code = contacts_list_next(list);
          if (error_code != CONTACTS_ERROR_NONE)
              break;
      }
      ```

      Define the `contacts_gl_log_data_t` structure and the functions for using the structure:

      ```
      struct _contacts_gl_log_data {
          int id;
          char *address;
          int log_type;
          int log_time;
      };
      typedef struct _contacts_gl_log_data contacts_gl_log_data_t;

      /* Release the resources allocated to the structure */
      static void
      _free_gl_log_data(contacts_gl_log_data_t *gl_log_data)
      {
          if (NULL == gl_log_data)
              return;

          free(gl_log_data->address);
          free(gl_log_data);
      }

      /* Create the structure for a log */
      static contacts_gl_log_data_t*
      _create_gl_log_data(contacts_record_h record)
      {
          contacts_gl_log_data_t *gl_log_data;
          int error_code;

          gl_log_data = malloc(sizeof(contacts_gl_log_data_t));
          memset(gl_log_data, 0x0, sizeof(contacts_gl_log_data_t));

          if (CONTACTS_ERROR_NONE != contacts_record_get_int(record,
                                                             _contacts_phone_log.id,
                                                             &gl_log_data->id)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get log ID failed ");
              _free_gl_log_data(gl_log_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_str(record,
                                                             _contacts_phone_log.address,
                                                             &gl_log_data->address)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get log address failed ");
              _free_gl_log_data(gl_log_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_int(record,
                                                             _contacts_phone_log.log_type,
                                                             &gl_log_data->log_type)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get log type failed ");
              _free_gl_log_data(gl_log_data);

              return NULL;
          }
          if (CONTACTS_ERROR_NONE != contacts_record_get_int(record,
                                                             _contacts_phone_log.log_time,
                                                             &gl_log_data->log_time)) {
              dlog_print(DLOG_ERROR, LOG_TAG, "get log time failed ");
              _free_gl_log_data(gl_log_data);

              return NULL;
          }

          return gl_log_data;
      }
      ```

3. When no longer needed, destroy the list handle and release all its resources using the `contacts_list_destroy()` function:

   ```
   contacts_list_destroy(list, true);
   ```

<a name="pl_delete"></a>
## Deleting a Log

To delete a log entry, use the `contacts_db_delete_record()` function with the log ID as the second parameter:

```
int log_id = ...; /* Get the log ID */

error_code = contacts_db_delete_record(_contacts_phone_log._uri, log_id);
if (error_code != CONTACTS_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "contacts_db_delete_record failed: %x", error_code);
```

<a name="insert2"></a>
## Creating a Record

The basic concept in the Contacts API is a record. A record can be a complex set of data, containing other data. For example, an address record can contain data about the country, region, and street. Also, the contained data can be a reference to another record. For example, a contact record contains the `address` property, which is a reference to an address record. A record can therefore be a node in a tree of relations between records.

Each record type has a special `view` structure, which contains identifiers of its properties. For example, the `_contacts_contact` view describes the properties of the contact record. It contains properties, such as the name, company, and nickname of the contact. A special property in such structures is the URI, which is used to identify the record type. Every view describing a record has this property.

To insert a new record into the contact database:

1. Create a new record.

   For example, to create a new contact record, create a record using the `_contacts_contact` view:

   ```
   contacts_record_h hcontact = NULL;

   error_code = contacts_record_create(_contacts_contact._uri, &hcontact);
   ```

   Creating another type of record, such as a group or speed dial, is similar to creating a record. The only difference is using another view, for example, `_contacts_group` for a group or `_contacts_speeddial` for a speed dial.

2. Set the record properties.

   Most properties in the contact view are separate records, so create more records, as needed. For example, to set the address for the contact:

   1. Create a new address record using the `_contacts_address` view:

      ```
      contacts_record_h haddress = NULL;

      error_code = contacts_record_create(_contacts_address._uri, &haddress);
      ```

   2. Set the address record properties.

      The following example sets the country of the address:

      ```
      error_code = contacts_record_set_str(haddress, _contacts_address.country, "Korea");
      ```

   3. Add the address record as a child record to the contact record:

      ```
      error_code = contacts_record_add_child_record(hcontact, _contacts_contact.address, haddress);
      ```

      > **Note**
      >
      > Do not destroy the child record handle.

3. Insert the record into the contact database. You receive the ID of the record in the database.

   ```
   int id;

   error_code = contacts_db_insert_record(hcontact, &id);
   ```

   > **Note**
   >
   > Do not manually insert any of the child records into the database. The system inserts the child records automatically along with the parent record.

4. When no longer needed, destroy the record handle and release all its resources:

   ```
   error_code = contacts_record_destroy(hcontact, true);
   ```

<a name="get2"></a>
## Retrieving Record Details

Before you can retrieve details (properties) from a record, you must first retrieve the record. You must know the ID of the record you want to retrieve.

To retrieve a record, retrieve a handle for it with the record ID:

```
contacts_record_h record;
const int ID = 2;

contacts_db_get_record(_contacts_contact._uri, ID, &record);
```

To retrieve the record details:

- Retrieve direct record details.

  To retrieve details directly from the record, use a `contacts_record_get_XXX()` function. The specific function depends on the data type of the detail (property) you want to retrieve.

  The following example uses the `contacts_record_get_str()` function to retrieve a contact's display name, which is a string value:

  ```
  char *d_name;
  contacts_record_get_str(record, _contacts_contact.display_name, d_name);
  free(d_name);
  ```

- Retrieve child record details.

  When working with a record from one view, you sometimes need details from its child record from another view. To retrieve details from a child record, use the `contacts_record_get_child_record_at_p()` function.

  The following example first retrieves a name record associated as a child record of a contact record, and then retrieves the first name from the name record:

  ```
  contacts_record_h child_record;
  contacts_record_get_child_record_at_p(record, _contacts_contact.name, 0, &child_record);

  /* From the child record, retrieve the first name using the name view */
  char *f_name = NULL;
  contacts_record_get_str(child_record, _contacts_name.first_name, &f_name);
  free(f_name);
  ```

- Retrieve parent record details.

  When working with a child record from one view, you sometimes need details from its parent record from another view. To access the parent record, first determine its ID, and then retrieve the parent record.

  The following example first retrieves the parent contact record ID for a name record using the `contact_id` property, then retrieves the contact record, and finally checks whether the contact has an email address:

  ```
  contacts_record_h parent_record;
  int parent_id;
  contacts_record_get_int(record, _contacts_name.contact_id, &parent_id);
  contacts_db_get_record(_contacts_contact._uri, parent_id, &parent_record);

  /* From the parent record, check the boolean has_email property */
  bool h_email;
  contacts_record_get_bool(parent_record, _contacts_contact.has_email, &h_email);
  ```

<a name="structure"></a>
- Retrieve more record details using a structure:

  1. Create the structure.

     The following example defines the `contact_gl_data_t` structure for contacts and implements the create function for the structure:

     ```
     gldata = _create_gl_data(record);
     char *number = gldata->number;

     /* Define the structure */
     struct _contact_gl_data {
         int id;
         char *first;
         char *last;
         char *number;
         char *image_path;
     };
     typedef struct _contact_gl_data contact_gl_data_t;

     /* Create the structure */
     static contact_gl_data_t*
     _create_gl_data(contacts_record_h r_contact)
     {
         contact_gl_data_t *data;
         data = malloc(sizeof(contact_gl_data_t));
         memset(data, 0x0, sizeof(contact_gl_data_t));

         if (! _get_contact_id(r_contact, &data->id)) {
             free(data);

             return NULL;
         }

         if (!_get_contact_number(r_contact, &data->number)) {
             free(data);

             return NULL;
         }
         if (!_get_contact_first(r_contact, &data->first)) {
             free(data->number);
             free(data);

             return NULL;
         }
         if (!_get_contact_last(r_contact, &data->last)) {
             free(data->number);
             free(data->first);
             free(data);

             return NULL;
         }
         if (!_get_contact_image(r_contact, &data->image_path)) {
             free(data->number);
             free(data->first);
             free(data->last);
             free(data);

             return NULL;
         }

         return data;
     }
     ```

  2. Retrieve record data into the structure.

     Contacts, for example, are organized in a parent-child structure, where the contact record is the parent. To retrieve specific data from a contact record:

     - If the data is stored directly in the contact record, access the correct property using the appropriate `contacts_record_get_XXX()` function.
     - If the data is stored in a child record, retrieve the child record responsible for the data type using the `contacts_record_get_child_record_at_p()` function, and then access the correct property in the child record using the appropriate `contacts_record_get_XXX()` function.

     For a list of properties by view, see View/Property (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html) applications).

     > **Note**
     >
     > Do not pass any data returned by a function with the `_p` suffix to the `free()` function.

     To retrieve contact details into the `contact_gl_data_t` structure:

     - To retrieve the ID of the contact record, use the `contacts_record_get_int()` function on the contact record with the `_contacts_contact.id` property.

       The ID is a unique number representing the record key in the contact database. If you know the ID of a record, you can access and manipulate the record with different functions, such as `contacts_db_get_record()` or `contacts_db_delete_record()`.

       ```
       static bool
       _get_contact_id(contacts_record_h r_contact, int *id)
       {
           int error_code;

           error_code = contacts_record_get_int(r_contact, _contacts_contact.id, id);

           return true;
       }
       ```

     - To retrieve the contact's phone number, first check whether the contact has at least 1 phone number using the `contacts_record_get_bool()` function on the contact record with the `_contacts_contact.has_phonenumber` property. If the contact has 1 or more phone numbers, retrieve the numbers using the various Query (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__QUERY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__QUERY__MODULE.html) applications) and Filter (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html) applications) functions from the Contacts API. The numbers are stored in the number child records (the `_contacts_number` view). After you are done, free any data returned by a function not containing the `_p` suffix.

       The following example checks whether the contact has any phone numbers. Then, it queries all phone numbers and filters the search so that only the numbers that are default numbers and belong to the specific contact are included in the search result.

       ```
       static bool
       _get_contact_number(contacts_record_h r_contact, char **number)
       {
           int id;
           int error_code;
           contacts_record_h r_number;
           contacts_query_h query = NULL;
           contacts_filter_h filter = NULL;
           contacts_list_h list = NULL;

           if (!_get_contact_id(r_contact, &id))
               return false;

           bool has_number;
           error_code = contacts_record_get_bool(r_contact, _contacts_contact.has_phonenumber, &has_number);

           error_code = contacts_query_create(_contacts_number._uri, &query);

           unsigned int fields[] = {_contacts_number.number};
           error_code = contacts_query_set_projection(query, fields, 1);

           error_code = contacts_filter_create(_contacts_number._uri, &filter);

           error_code = contacts_filter_add_int(filter, _contacts_number.contact_id,
                                                CONTACTS_MATCH_EXACTLY, id);

           error_code = contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_AND);

           error_code = contacts_filter_add_bool(filter, _contacts_number.is_default, true);

           error_code = contacts_query_set_filter(query, filter);

           error_code = contacts_db_get_records_with_query(query, 0, 1, &list);

           error_code = contacts_list_get_current_record_p(list, &r_number);

           error_code = contacts_record_get_str(r_number, _contacts_number.number, number);

           contacts_query_destroy(query);
           contacts_filter_destroy(filter);
           contacts_list_destroy(list, true);
       }
       ```

       The following alternative example retrieves the contact's default phone number directly:

       ```
       static bool
       _get_contact_number(contacts_record_h r_contact, char **number)
       {
           int error_code;
           contacts_record_h r_number;

           bool has_number;
           error_code = contacts_record_get_bool(r_contact, _contacts_contact.has_phonenumber, &has_number);

           if (!has_number) {
               *number = NULL;

               return true;
           }

           int i;
           unsigned int count = 0;
           bool is_default = false;
           error_code = contacts_record_get_child_record_count(contact, _contacts_contact.number, &count);

           for (i = 0; i < count; i++) {
               error_code = contacts_record_get_child_record_at_p(r_contact, _contacts_contact.number, i, &r_number);
               error_code = contacts_record_get_bool(r_number, _contacts_number.is_default, &is_default);
               if (is_default) {
                   error_code = contacts_record_get_str(r_number, _contacts_number.number, number);

                   return true;
               }
           }
           *number = NULL;

           return false;
       }
       ```

       To retrieve a second number, change the third parameter of the `contacts_record_get_child_record_at_p()` function from 0 to 1.

     - To retrieve the contact's name details, retrieve the name child record of the contact record using the `contacts_record_get_child_record_at_p()` function with the `_contacts_contact.name` property. From the child record, retrieve the name data using the `contacts_record_get_str()` function.

       The following example retrieves the contact's first name from the name record:

       ```
       static bool
       _get_contact_first(contacts_record_h r_contact, char **first)
       {
           contacts_record_h r_name;
           int error_code;

           error_code = contacts_record_get_child_record_at_p(r_contact, _contacts_contact.name, 0, &r_name);

           error_code = contacts_record_get_str(r_name, _contacts_name.first, first);
       }
       ```

       The following example retrieves the contact's last name from the name record:

       ```
       static bool
       _get_contact_last(contacts_record_h r_contact, char **last)
       {
           contacts_record_h r_name;
           int error_code;

           error_code = contacts_record_get_child_record_at_p(r_contact, _contacts_contact.name, 0, &r_name);

           error_code = contacts_record_get_str(r_name, _contacts_name.last, last);
       }
       ```

     - To retrieve the contact's image, use the `contacts_record_get_str()` function on the contact record with the `_contacts_contact.image_thumbnail_path` property:

       ```
       static bool
       _get_contact_image(contacts_record_h r_contact, char **image_path)
       {
           int error_code;

           error_code = contacts_record_get_str(r_contact, _contacts_contact.image_thumbnail_path, image_path);

           dlog_print(DLOG_ERROR, LOG_TAG, "Thumb path: \'%s\'", *image_path);

           return true;
       }
       ```

<a name="list2"></a>
## Using Record Lists

To retrieve multiple records at the same time using a list:

1. Retrieve a list of records:

   - To retrieve a list of all records of a given type, use the `contacts_db_get_all_records()` function.

     The following example retrieves a list of all contacts:

     ```
     contacts_list_h list = NULL;

     contacts_db_get_all_records(_contacts_contact._uri, 0, 0, &list);
     ```

   - To retrieve a filtered and sorted list of records of a given type:

     1. Create a query using the `contacts_query_create()` function.

        The following example creates a query for contact names:

        ```
        contacts_list_h list = NULL;
        contacts_query_h query = NULL;

        contacts_query_create(_contacts_name._uri, &query);
        ```

     2. Create a filter for the query using the `contacts_filter_create()` function:

        The following example creates a name filter:

        ```
        contacts_filter_h filter = NULL;

        contacts_filter_create(_contacts_name._uri, &filter);
        ```

        The first parameter defines in which view to place the filter. To filter contacts by first and last name, use the `_contacts_name` view. The first parameter must be the same as the first parameter of the `contacts_query_create()` function, that is, the query and its filter must both use the same view. For more information on views, see View/Property (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__VIEW__MODULE.html) applications).

     3. Add a filtering condition using a `contacts_filter_add_XXX()` function.

        The following example adds a string-based filtering condition that retrieves name records where the last name starts with "Za":

        ```
        contacts_filter_add_str(filter, _contacts_name.last_name, CONTACTS_MATCH_STARTSWITH, "Za");
        ```

        The available matching options (third parameter) for string-based filtering conditions are defined in the `contacts_match_str_flag_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#ga5a4ee5c71ae14d0fbf7520597514f0c2) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#ga5a4ee5c71ae14d0fbf7520597514f0c2) applications).

     4. To add more conditions, add a logical operator before each new condition using the `contacts_filter_add_operator()` function. The conditions and operators together define the filtering logic as a whole.

        The following example first adds an AND operator and then a string-based filtering condition that retrieves name records where the last name ends with "ra".

        The combination of the AND operator and the 2 conditions means that the filter only retrieves name records where the last name starts with "Za" and ends with "ra".

        ```
        contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_AND);

        contacts_filter_add_str(filter, _contacts_name.last_name, CONTACTS_MATCH_ENDSWITH, "ra");
        ```

     5. If you need to use a logical expression with brackets, such as "C1 AND C2 AND (C3 OR C4)", define the bracketed conditions in a separate filter, and add the new filter to the parent filter as a filtering condition using the `contacts_filter_add_filter()` function.

        The following example extends the previous example by first adding an AND operator and then a child filter with 2 string-based filtering conditions separated by an OR operator.

        The combination of all the filtering conditions means that the parent filter only retrieves name records where (1) the last name starts with "Za" and ends with "ra" and (2) the first name starts with either "Ada" or "Igo".

        ```
        contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_AND);

        contacts_filter_h n_filter = NULL;
        contacts_filter_create(_contacts_name._uri, &n_filter);
        contacts_filter_add_str(n_filter, _contacts_name.first_name, CONTACTS_MATCH_STARTSWITH, "Ada");
        contacts_filter_add_operator(n_filter, CONTACTS_FILTER_OPERATOR_OR);
        contacts_filter_add_str(n_filter, _contacts_name.first_name, CONTACTS_MATCH_STARTSWITH, "Igo");

        contacts_filter_add_filter(filter, n_filter);
        ```

     6. Set the filter to the query using the `contacts_query_set_filter()` function:

        ```
        contacts_query_set_filter(query, filter);
        ```

     7. Sort the query results by one of its view properties using the `contacts_query_set_sort()` function.

        The following example sorts the contact name query by first name:

        ```
        contacts_query_set_sort(query, _contacts_name.first, true);
        ```

     8. Set a projection to the query using the `contacts_query_set_projection()` function.

        A projection allows you to query the data for specific properties of a record. Using a projection can reduce latency when querying a large database.

        The following example limits the properties from the previous steps to the first and last name:

        ```
        unsigned my_projection[] = {_contacts_name.contact_id, _contacts_name.first, _contacts_name.last}
        contacts_query_set_projection(query, my_projection, sizeof(my_projection)/sizeof(int));
        ```

        The results of a filtered query can contain records that differ only in a few properties. After setting a projection to the filtered query, the results can contain identical records. To avoid these, use the `contacts_query_set_distinct()` function, which removes duplicates from the results:

        ```
        contacts_query_set_distinct(query, true);
        ```

     9. Retrieve the filtered list using the `contacts_db_get_records_with_query()` function:

        ```
        contacts_db_get_records_with_query(query, 0, 0, &list);
        ```

        The third parameter defines a limit for the number of results. If you set it to 0, the list returns all records matching the query.

2. Iterate through the list of found records, and retrieve the record details:

   Use a loop to iterate through the list and retrieve the details:

   - Move forward and backward within the list using the `contacts_list_prev()`, `contacts_list_next()`, `contacts_list_first()`, and `contacts_list_last()` functions.
   - Retrieve the current record using the `contacts_list_get_current_record_p()` function. By default, before iterating through the list, the current record is the first record.

   > **Note**
   >
   > Some functions have the `_p` postfix. The postfix means that the returned value must not be freed by the application, as it is a pointer to the data in an existing record.

   To retrieve the record details:

   - To retrieve only basic details, use a `contacts_record_get_XXX()` function on the record.

     The following example use the `contacts_record_get_str()` function to retrieve a contact's display name:

     ```
     contacts_record_h record;

     while (contacts_list_get_current_record_p(list, &record) == 0) {
         /* Get details */
         char *disp_name;
         contacts_record_get_str(record, _contacts_contact.display_name, &disp_name);
         free(disp_name);
         error_code = contacts_list_next(list);
     }
     ```

   - To retrieve more details, including child record details, use a structure. For more information, see [Retrieving Record Details](#structure).

     The following example uses the `contact_gl_data_t` structure to retrieve contact details:

     ```
     contacts_record_h record;
     contact_gl_data_t *gldata = NULL;

     while (contacts_list_get_current_record_p(list, &record) == 0) {
         gldata = _create_gl_data(record);

         error_code = contacts_list_next(list);
     }
     ```

   - The previous examples work only if you use the `_contacts_contact` view, that is, if you are dealing with contact records. If you use filtering in another view, as shown in the filtering examples, and you want to use the same contact structure with those records, first retrieve the parent contact record of the current record, and then use the structure for the parent record. This is basically a way to switch to the `_contacts_contact` view from another view.

     In the following example, the loop iterates through a list of name records. To retrieve the full details of the contact record corresponding to the current name record, the code retrieves the parent of the name record, which is a contact, and creates the `contact_gl_data_t` structure for the parent, retrieving its full details.

     ```
     contacts_record_h record;
     contact_gl_data_t *gldata = NULL;

     while (contacts_list_get_current_record_p(list, &record) == 0) {
         int record_id;
         contacts_record_h c_record;

         /* Get the ID of the parent contact record */
         contacts_record_get_int(record, _contacts_name.contact_id, &contact_id);

         /* Get the parent contact record */
         contacts_db_get_record(_contacts_contact._uri, contact_id, &c_record);

         /* Create the structure for the parent contact record */
         gldata = _create_gl_data(c_record);

         error_code = contacts_list_next(list);
     }
     ```

3. When no longer needed, destroy the filter, query, and list handles and release all their resources using the `contacts_filter_destroy()`, `contacts_query_destroy()`, and `contacts_list_destroy()` functions:

   ```
   contacts_filter_destroy(filter);
   contacts_query_destroy(query);
   contacts_list_destroy(list, true);
   ```

You can insert a whole list into the contact database. This is useful when you have several records to create and want to insert them all at once.

To insert a list into the contact database:

1. Create the list:

   ```
   contacts_list_h list;
   contacts_list_create(&list);
   ```

2. Add records to the list:

   ```
   contacts_list_add(list, record);
   ```

3. Insert the list into the contact database and get the IDs of the inserted records:

   ```
   int *ids = NULL;
   unsigned int count = 0;
   contacts_db_insert_records(list, &ids, &count);
   dlog_print(DLOG_DEBUG, LOG_TAG, "%d records inserted", count);
   free(ids);
   ```

4. When no longer needed, destroy the list handle and release all its resources using the `contacts_list_destroy()` function:

   ```
   contacts_list_destroy(list, true);
   ```

<a name="delete2"></a>
## Deleting a Record

To delete a record, use the `contacts_db_delete_record()` function with the view URI as the first parameter and the record ID as the second parameter.

The following example deletes a contact record:

```
int id = ...; /* Get the record ID */

error_code = contacts_db_delete_record(_contacts_contact._uri, id);
```

If you only have the record handle, retrieve the ID first:

```
error_code = contacts_record_get_int(record, _contacts_contact.id, &id);
```

<a name="link2"></a>
## Linking Persons

Linking one person to another is a useful method for combining contacts under a single person.

To link 2 persons and manage the linked person:

- Link a person to another person using the `contacts_person_link_person()` function with the corresponding person IDs.

  The following example first retrieves the person IDs using the `contacts_record_get_int()` function and then links the persons:

  ```
  /* Get the ID of the first person */
  contacts_record h record1;
  int first_person_id;
  int error_code = contacts_record_get_int(record1, _contacts_contact.person_id, &first_person_id);

  /* Get the ID of the second person */
  contacts_record h record2;
  int second_person_id;
  error_code = contacts_record_get_int(record2, _contacts_contact.person_id, &second_person_id);

  /* Link the persons */
  contacts_person_link_person(first_person_id, second_person_id);

  int person_id = first_person_id;
  ```

- Set the default properties for the linked person.

  Set the default properties from one of the associated contacts using the `contacts_person_set_default_property()` function. The first parameter uses the values of the `contacts_person_property_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__PERSON__MODULE.html#ga641465951ce76daa56bb430b37cc8d90) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__PERSON__MODULE.html#ga641465951ce76daa56bb430b37cc8d90) applications), which defines the available default properties for a person.

  For example, to set the person's default phone number based on the number of one of the associated contacts:

  1. Retrieve the contact whose phone number you want to use.
  2. Retrieve the correct phone number record associated with the contact using the `contacts_record_get_child_record_at_p()` function.
  3. Retrieve the phone number ID from the phone number record using the `contacts_record_get_int()` function with the `_contacts_number` view.
  4. Set the phone number as the default for the person using the `contacts_person_set_default_property()` function.

  ```
  contacts_record_h record;
  int error_code = -1;

  /* Get the contact record */

  /* Get the phone number record */
  contacts_record_h record_number;
  error_code = contacts_record_get_child_record_at_p(record, _contacts_contact.number, 0, &record_number);

  /* Get the phone number ID */
  int number_id;
  error_code = contacts_record_get_int(record_number, _contacts_number.id, &number_id);
  error_code = contacts_record_destroy(record_number, true);

  /* Set the phone number as the default for the person */
  error_code = contacts_person_set_default_property(CONTACTS_PERSON_PROPERTY_NUMBER, person_id, number_id);
  ```

- Retrieve the default properties of the linked person using the `contacts_person_get_default_property()` function.

  For example, to retrieve the default email address:

  1. Retrieve the ID of the default email record using the `contacts_person_get_default_property()` function with the `CONTACTS_PERSON_PROPERTY_EMAIL` property:

     ```
     int person_email_number;
     error_code = contacts_person_get_default_property(CONTACTS_PERSON_PROPERTY_EMAIL, person_id,
                                                       &person_email_number);
     ```

  2. Retrieve the default email record using the `contacts_db_get_record()` function with the email record ID:

     ```
     contacts_record_h email_record;
     error_code = contacts_db_get_record(_contacts_email._uri, person_email_number, &email_record);
     ```

  3. Retrieve the email address from the email record:

     ```
     char *default_email;
     error_code = contacts_record_get_str_p(email_record, _contacts_email.email, &default_email);

     /* Use default_email */

     error_code = contacts_record_destroy(email_record, true);
     ```

- Unlink a contact from the linked person using the `contacts_person_unlink_contact()` function. The function removes the contact (second parameter) from the person (first parameter), creates a new person (third parameter), and links the contact to the new person.

  ```
  int contact_id = ...; /* Get the contact ID */
  int unlinked_person_id;

  error_code = contacts_person_unlink_contact(person_id, contact_id, &unlinked_person_id);
  ```

<a name="settings"></a>
## Managing Contact Settings

To manage the display and sorting order settings for contacts:

1. Check the current display order using the `contacts_setting_get_name_display_order()` function. The display order defines the order in which contacts (names) are displayed on the device screen.

   ```
   contacts_name_display_order_e display_order;
   contacts_setting_get_name_display_order(&display_order);
   /* Now you have the display order */
   sprintf("Display order: %s",
           display_order==CONTACTS_NAME_DISPLAY_ORDER_FIRSTLAST ?
           "CONTACTS_NAME_DISPLAY_ORDER_FIRSTLAST" : "CONTACTS_NAME_DISPLAY_ORDER_LASTFIRST");
   ```

2. Check the current sorting order using the `contacts_setting_get_name_sorting_order()` function. The sorting order defines the order in which contact records are returned.

   ```
   contacts_name_sorting_order_e sorting_order;
   contacts_setting_get_name_sorting_order(&sorting_order);
   /* Now you have the sorting order */
   sprintf("Sorting order: %s",
           sorting_order==CONTACTS_NAME_SORTING_ORDER_FIRSTLAST ?
           "CONTACTS_NAME_SORTING_ORDER_FIRSTLAST" : "CONTACTS_NAME_SORTING_ORDER_LASTFIRST");
   ```

3. Change the display and sorting orders using the `contacts_setting_set_name_display_order()` and `contacts_setting_set_name_sorting_order()` functions. Both functions use as a parameter a value of an enumeration: `contacts_name_display_order_e` (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__SETTING__MODULE.html#ga0b52839d82e7ca998436b174e1f807d8) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__SETTING__MODULE.html#ga0b52839d82e7ca998436b174e1f807d8) applications) and `contacts_name_sorting_order_e` (in [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__SETTING__MODULE.html#ga28fdacd75efe1b14b33a3215fc5c3854) and [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__SETTING__MODULE.html#ga28fdacd75efe1b14b33a3215fc5c3854) applications) that define the available display and sorting orders.

   ```
   contacts_setting_set_name_display_order(CONTACTS_NAME_DISPLAY_ORDER_FIRSTLAST);

   contacts_setting_set_name_sorting_order(CONTACTS_NAME_SORTING_ORDER_FIRSTLAST);
   ```

4. Receive a notification whenever the display or sorting order changes:

   1. Register callbacks using the `contacts_setting_add_name_display_order_changed_cb()` and `contacts_setting_add_name_sorting_order_changed_cb()` functions.

   2. Define the order change callbacks.

      The following example shows how to print a message when the display or sorting order changes:

      ```
      static void
      display_changed_cb(contacts_name_display_order_e name_display_order, void *user_data)
      {
          dlog_print(DLOG_DEBUG, LOG_TAG, "changed display order: %s",
                     name_display_order==CONTACTS_NAME_DISPLAY_ORDER_FIRSTLAST ?
                     "CONTACTS_NAME_DISPLAY_ORDER_FIRSTLAST" : "CONTACTS_NAME_DISPLAY_ORDER_LASTFIRST");
      }

      static void
      sorting_changed_cb(contacts_name_sorting_order_e name_display_order, void *user_data)
      {
          dlog_print(DLOG_DEBUG, LOG_TAG, "changed sorting order: %s",
                     name_display_order==CONTACTS_NAME_SORTING_ORDER_FIRSTLAST ?
                     "CONTACTS_NAME_SORTING_ORDER_FIRSTLAST" : "CONTACTS_NAME_SORTING_ORDER_LASTFIRST");
      }
      ```

      To track the changes, implement a timeout function after setting the callbacks.

   3. When no longer needed, deregister the callbacks using the `contacts_setting_remove_name_display_order_changed_cb()` and `contacts_setting_remove_name_sorting_order_changed_cb()` functions.

<a name="sim"></a>
## Importing Contacts from the SIM Card

To import contacts from the SIM card:

1. Make sure the SIM card has been initialized:

   ```
   bool completed = false;
   contacts_sim_get_initialization_status(&completed);
   dlog_print(DLOG_DEBUG, LOG_TAG, "SIM %s completed", completed ? "" : "not ");
   ```

   > **Note**
   >
   > You cannot access contacts on a SIM card that has not been initialized.

2. Import the contacts:

   ```
   int error_code = contacts_sim_import_all_contacts();
   ```

<a name="import"></a>
## Importing from vCard

Importing contacts from a vCard file involves parsing the vCard file for contacts and inserting the parsed contacts into the contact database. You have the following options for parsing a vCard file:

- Parse a vCard stream of the file. This option gives you a list of all contact records in a single function call, but you must first create the vCard stream.
- Parse the file directly. This option requires that you use a callback to handle each parsed contact record separately.

To import contacts from vCard streams:

> **Note**
>
> This use case imports contacts from every vCard file in a given directory.

1. Retrieve the path to the source directory containing the vCard files you want to import.

   The following example retrieves the path to the downloads directory of the device's internal storage:

   ```
   int internal_storage_id;
   char *vcf_path = NULL;

   /* Handle the storages found on the device */
   static bool
   storage_cb(int storage_id, storage_type_e type, storage_state_e state, const char *path, void *user_data)
   {
       /* Check whether the storage is the device's internal storage */
       if (type == STORAGE_TYPE_INTERNAL) {
           /* Get the internal storage ID */
           internal_storage_id = storage_id;

           /* Internal storage found, end the callback loop */
           return false;
       }

       /* Internal storage not found, continue the callback loop */
       return true;
   }

   /* Get the source directory path */
   void
   get_storage_path()
   {
       int error_code = 0;
       char *path = NULL;

       /* Get the storages available on the device */
       /* Handle each storage in the storage_cb() callback */
       error_code = storage_foreach_device_supported(storage_cb, NULL);

       /*
          Get the absolute path to the downloads directory
          of the device's internal storage
       */
       error_code = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_DOWNLOADS, &path);
       if (error_code != STORAGE_ERROR_NONE) {
           vcf_path = strdup(path);
           free(path);
       }
   }
   ```

2. Create a vCard stream of each vCard file in the source directory. You can do this with the `dirent` structure and the directory stream functions available in the `<dirent.h>` header file.

   The following example implements a `while` loop that cycles through the vCard files in the source directory and creates a vCard stream of each file:

   ```
   /* Open a directory stream for the source directory */
   DIR *dir = opendir(vcf_path);

   /* Parse the directory stream for directory entries (dirent) */
   struct dirent *pDirent = NULL;

   if (dir == NULL) {
       free(vcf_path);

       return;
   }

   if (dir) {
       while ((pDirent = readdir(dir)) != NULL) {
           /*
              If the directory entry is not a regular file,
              skip to the next directory entry
           */
           if (pDirent->d_type != DT_REG)
               continue;

           /*
              If the file is not a vCard file,
              skip to the next directory entry
           */
           char *extension = strrchr(pDirent->d_name, '.');
           if (!extension || strcmp(extension, ".vcf"))
               continue;
           dlog_print(DLOG_DEBUG, LOG_TAG, "file %s", pDirent->d_name);

           /* Get the vCard file path */
           char *file_path = malloc(strlen(vcf_path) + strlen(pDirent->d_name) + 4);
           sprintf(file_path, "%s/%s", vcf_path, pDirent->d_name);

           /*
              If the vCard file does not contain any records,
              skip to the next directory entry
           */
           int count;
           int error_code = contacts_vcard_get_entity_count(file_path, &count);
           if (count < 1)
               continue;

           /* Calculate the vCard file size */
           FILE *fp = fopen(file_path, "r");
           if (fseek(fp, 0, 2) != 0)
               /* Error handling */
           int bufsize = ftell(fp);
           rewind(fp);
           dlog_print(DLOG_DEBUG, LOG_TAG, "file size: %i", bufsize);
           if (bufsize < 1)
               return 1;

           /* Create the vCard stream */
           char *vcard_stream = malloc(sizeof(char) * (bufsize));
           memset(vcard_stream, '\0', sizeof(vcard_stream));
           if (fp != NULL) {
               char str[150];
               while (fgets(str, 150, fp) != NULL)
                   sprintf(vcard_stream + strlen(vcard_stream), "%s", str);
               fclose(fp);
           } else {
               return 1;
           }
   ```

3. Parse the vCard streams for contacts using the `contacts_vcard_parse_to_contacts()` function. The function returns a list of all contact records parsed from the stream.

   The following example first parses a list of contact records from the vCard stream and then iterates through the list inserting each record to the contact database:

   ```
           contacts_list_h contacts_list;
           contacts_record_h record;

           /* Get the contact list from the vCard stream */
           error_code = contacts_vcard_parse_to_contacts(vcard_stream, &contacts_list);
           if (error_code != 0)
               dlog_print(DLOG_ERROR, LOG_TAG, "contacts_vcard_parse_to_contacts failed: %d", error_code);
           free(vcard_stream);

           /* Iterate through the contact list */
           while (contacts_list_get_current_record_p(contacts_list, &record) == 0) {
               int id = -1;
               /* Add to the database */
               error_code = contacts_db_insert_record(record, &id);
               if (error_code != 0)
                   dlog_print(DLOG_ERROR, LOG_TAG, "contacts_db_insert_record failed");

               /* Move to the next record */
               error_code = contacts_list_next(contacts_list);
           }
           error_code = contacts_list_destroy(contacts_list, true);
           if (error_code != 0)
               dlog_print(DLOG_ERROR, LOG_TAG, "contacts_list_destroy failed: %d", error_code);
           free(file_path);
       }
       closedir(dir);
   }
   ```

To import contacts directly from a vCard file:

1. Parse the vCard file using the `contacts_vcard_parse_to_contact_foreach()` function. The function invokes a callback for each contact record it parses from the file.

   The following example first defines the vCard file path and then parses the vCard file:

   ```
   /* Get the vCard file path */
   char *resource_path = app_get_resource_path();
   char vcard_path[1024] = {0};
   snprintf(vcard_path, sizeof(vcard_path), "%s/vcard.vcf", resource_path);
   free(resource_path);

   /* Get the contacts from the vCard file */
   int error_code = contacts_vcard_parse_to_contact_foreach(vcard_path, _contacts_vcard_cb, NULL);
   ```

   To check how many records are contained in a vCard file, use the `contacts_vcard_get_entity_count()` function.

2. Implement the callback for handling the contact records parsed from the vCard file. You can use the callback to insert the records into the contact database.

   The callback is invoked separately for each parsed contact record. As long as the callbacks return `true`, the `contacts_vcard_parse_to_contact_foreach()` function continues to parse new contacts.

   The following example implements a callback that inserts the parsed record into the contact database:

   ```
   bool
   _contacts_vcard_cb(contacts_record_h record, void *user_data)
   {
       int id = -1;
       int error_code = contacts_db_insert_record(record, &id);

       return true;
   }
   ```

<a name="export"></a>
## Exporting to vCard

To export all contact records from the contact database and store them to a single vCard file:

1. Define the location of the vCard file where the contacts are to be exported, and retrieve a list of all records using the `contacts_db_get_all_records()` function:

   ```
   char file_path[] = "/path/contacts.vcf";
   contacts_list_h list = NULL;
   error_code = contacts_db_get_all_records(_contacts_contact._uri, 0, 0, &list);
   ```

2. Open the vCard file for writing:

   ```
   FILE *file = fopen(file_path, "w");
   ```

3. Loop through the contact list, export each contact record in vCard format, and write the record to the file:

   - To export a contact from the `_contacts_contact` view, use the `contacts_vcard_make_from_contact()` function.
   - To export details from the `_contacts_person` view, use the `contacts_vcard_make_from_person()` function.
   - To export details from the `_contacts_my_profile` view, use the `contacts_vcard_make_from_my_profile()` function.

   The following example uses the `_contacts_contact` view, but other views work the same way.

   ```
   contacts_record_h contact;
   char *vcard_stream;

   while (contacts_list_get_current_record_p(list, &record) == 0) {
       error_code = contacts_vcard_make_from_contact(record, &vcard_stream);
       /* Save to file */
       fwrite(vcard_stream, 1, strlen(vcard_stream), file);
       free(vcard_stream);
       error_code = contacts_list_next(list);
   }
   fclose(file);
   contacts_list_destroy(list, true);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
