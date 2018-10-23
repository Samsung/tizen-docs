
# Contact Management

The basic tasks involved in contact management operations are creating
and updating contacts, retrieving and deleting persons, and linking
contacts and persons. The following sections provide you with the
fundamental building blocks for managing contact details in the Contacts
database.

<a name="initializing"></a>
## Connecting to the Contact Service

To initialize the contact service and use the functions and data types
of the Contacts API, you must include the `<contacts.h>` header file in
your application. To be able to access the Contacts database and
operations, such as fetching, inserting, or updating, you must also
connect to the contact service by calling the `contacts_connect()`
function.

```c++
#include <contacts.h>

int error_code;
error_code = contacts_connect();

if (error_code != CONTACTS_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "failed to connect contacts: error code = %d", error_code);
```

When you no longer need it, disconnect from the contact service using
the `contacts_disconnect()` function.

> **Note**  
> To use the Contacts API, your application has to request
permission by adding the following privileges to the
`tizen-manifest.xml` file in the application package:  
> ```xml
> <privileges>
>   <privilege>http://tizen.org/privilege/contact.read</privilege>
>   <privilege>http://tizen.org/privilege/contact.write</privilege>
> </privileges>
> ```



<a name="retrieving"></a>
## Retrieving Persons

You can retrieve person details in many ways:

-   If a person ID is known in your application, you can retrieve the
    person's details using the `contacts_db_get_record()` function,
    whose first parameter is the `_contacts_person._uri` view:

    ```c++
    contacts_record_h person = NULL;
    const int person_id = ... /* Get the person ID */
    int error_code;

    error_code = contacts_db_get_record(_contacts_person._uri, person_id, &person);

    if (error_code != CONTACTS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to get record: error code = %d", error_code);
    ```

- If you need to retrieve a list of persons matching a search keyword
    without knowing a specific person ID, you can use the
    `contacts_db_search_records()` function. The third parameter is the
    offset, meaning the record index from which to search, and the
    fourth parameter sets a limit to the number of results, where 0
    means that all the matched records are retrieved.

    The following example shows how to find all person records that
    contain the keyword "John".

    ```c++
    contacts_list_h list = NULL;

    error_code = contacts_db_search_records(_contacts_person._uri, "John", 0, 0, &list);

    if (error_code != CONTACTS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to search records: error code = %d", error_code);
    ```

- If you have more complex search requirements, you can use queries
    and filters to retrieve records:

    -   Queries are used to retrieve data that satisfies given criteria,
        for example, an `integer` property being greater than a given
        value, or a `string` property containing a given substring.
    - Filters specify the search conditions for queries. When creating
        a filter, you must specify the filter type using the
        `_uri` property.

        Conditions can be joined by using the logical operators `AND`
        and `OR`. For contact filters, there are enumerations of
        operators and conditions for each type:
        `contacts_filter_operator_e` (in
        [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#ga2111e378d844cc7659ed5b4ff96bc433)
        and
        [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#ga2111e378d844cc7659ed5b4ff96bc433)
        applications), `contacts_match_int_flag_e` (in
        [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#gad0453305468fab6453b07183e31628ba)
        and
        [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#gad0453305468fab6453b07183e31628ba)
        applications), and `contacts_match_str_flag_e` (in
        [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#ga5a4ee5c71ae14d0fbf7520597514f0c2)
        and
        [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__FILTER__MODULE.html#ga5a4ee5c71ae14d0fbf7520597514f0c2) applications).

    The following code demonstrates how to retrieve the contacts
    associated with a person using queries and filters. As a person can
    be associated with 1 or more contacts, the number of the contact
    records for the person can be 1 or more.

    To simplify the example code, error handling has been omitted,
    except for the final check.

    ```c++
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
        error_code += contacts_filter_add_int(filter, _contacts_contact.person_id, CONTACTS_MATCH_EQUAL, person_id);
        error_code += contacts_query_set_filter(query, filter);

        /* Run the query to retrieve a list of contacts associated with the person ID */
        error_code += contacts_db_get_records_with_query(query, 0, 0, associated_contacts);

        /* Destroy the filter and query handles and release all their resources */
        error_code += contacts_filter_destroy(filter);
        error_code += contacts_query_destroy(query);

        if (error_code != CONTACTS_ERROR_NONE)
            return false;

        return true;
    }
    ```

    The following example uses queries and filters to retrieve a
    person's default phone number. If a person is associated with
    multiple phone numbers, one of them is defined as the default
    phone number. To determine the default phone number, you can check
    the `is_primary_default` property of the
    `_contacts_person_number` view. For the default phone number, the
    property is set to `true`.

    ```c++
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
        error_code += contacts_filter_add_int(filter, _contacts_person_number.person_id, CONTACTS_MATCH_EQUAL, person_id);
        error_code += contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_AND);
        error_code += contacts_filter_add_bool(filter, _contacts_person_number.is_primary_default, true);
        error_code += contacts_query_set_filter(query, filter);

        /*
           Run the query to retrieve the phone number records
           containing the default phone number
        */
        error_code += contacts_db_get_records_with_query(query, 0, 0, &list);

        /* Retrieve the current record from the query list */
        error_code += contacts_list_get_current_record_p(list, &record_person_number);

        /* Retrieve the phone number from the phone number record */
        error_code += contacts_record_get_str(record_person_number, _contacts_person_number.number, default_phone_number);

        /* Destroy the list, filter, and query handles and release all their resources */
        contacts_list_destroy(list, true);
        contacts_filter_destroy(filter);
        contacts_query_destroy(query);

        if (error_code != CONTACTS_ERROR_NONE)
            return false;

        return true;
    }
    ```


<a name="updating"></a>
## Updating Contacts

To update the information for existing contacts, you must retrieve,
change, and save the information you want to update:

1.  Retrieve the contact you want to update using the
    `contacts_db_get_record()` function with the contact ID as the
    second parameter. Alternatively, you can retrieve the contact using
    a search function, such as `contacts_db_get_records_with_query()`.

    ```c++
    int contact_id = ... /* Get the contact ID */
    contacts_record_h contact = NULL;

    error_code = contacts_db_get_record(_contacts_contact._uri, contact_id, &contact);
    ```

2. Set the properties you want to update:
    -   The following example sets a new first name for the contact
        record by updating a child record:

        ```c++
        contacts_record_h name = NULL;
        /* Retrieve the contact's name record */
        /* Record index is set to 0, since there is only 1 child record of type "name" */
        error_code = contacts_record_get_child_record_at_p(contact, _contacts_contact.name, 0, &name);
        /* Change the first name in the name record */
        error_code = contacts_record_set_str(name, _contacts_name.first, "Mark");
        ```

    - The following example sets a new birthday event for the contact
        by updating another child record.

        The example assumes that the birthday is the only event for the
        contact, meaning that the event record can be retrieved using
        the `contacts_record_get_child_record_at_p()` function with
        index 0 as the second parameter. If the contact has multiple
        events, you must iterate through them.

        ```c++
        contacts_record_h event = NULL;
        /* Retrieve the contact's birthday event record */
        error_code = contacts_record_get_child_record_at_p(contact, _contacts_contact.event, 0, &event);
        /* Change the date in the event record */
        int new_date = 1990 * 10000 + 6 * 100 + 21;
        error_code = contacts_record_set_int(event, _contacts_event.date, new_date);
        ```

    - The following example shows the iteration to change the country
        in all contact addresses, which are child records of
        the contact. Each address can be traversed by using the
        `contacts_record_get_child_record_at_p()` function.

        ```c++
        int contact_id = ... /* Get the contact ID */
        int address_num = 0;
        int i = 0;

        contacts_db_get_record(_contacts_contact._uri, contact_id, &contact);
        contacts_record_get_child_record_count(count, _contacts_contact.address, &address_num);

        for (i = 0; i < address_num; i++) {
            contacts_record_h address = NULL;
            contacts_record_get_child_record_at_p(contact, _contacts_contact.address, i, &address);
            contacts_record_set_str(address, _contacts_address.country, "Korea");
        }
        ```

3. Apply the changes to the database using the
    `contacts_db_update_record()` function:

    ```c++
    error_code = contacts_db_update_record(contact);

    if (error_code != CONTACTS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to update record: error code = %d", error_code);
    ```

    > **Note**  
    > The `contacts_record_set_XXX()` functions only change the
    data in the memory object, not in the Contacts database. Normally,
    to update the database, you must update each record separately using    the `contacts_db_update_record()` function. However, if you retrieve    a child record using the `contacts_record_get_child_record_at_p()`    function, you only need to update the parent record to the database;    the child record is updated automatically with the parent record.

4. When no longer needed, destroy the contact handle and release all
    its resources using the `contacts_record_destroy()` function.

    If you set the second parameter to `true`, the function destroys any
    child records automatically, irrespective of how the child records
    were added (individually or along with their parent record).

    ```c++
    error_code = contacts_record_destroy(contact, true);

    if (error_code != CONTACTS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to destroy record: error code = %d", error_code);
    ```


<a name="creating"></a>
## Creating a Contact

To create a new contact, you must create a contact handle, set the
contact properties, insert the contact into the database, and destroy
the handle:

1.  Create a contact handle using the `contacts_record_create()`
    function with the `_contacts_contact._uri` property as the first
    parameter:

    ```c++
    contacts_record_h contact;

    error_code = contacts_record_create(_contacts_contact._uri, &contact);

    if (error_code != CONTACTS_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "failed to create record: error code = %d", error_code);
    ```

    Remember that records created with the `contacts_record_create()`
    function are memory objects, with `contacts_record_h` type variables
    as their handles. If you change these objects, the changes are not
    reflected in the Contacts database until you explicitly insert or
    update the objects to the database using the
    `contacts_db_insert_record()` or
    `contacts_db_update_record()` function.

2. Set the contact properties.

    The following examples set the contact name, image, phone number,
    and event.

    To simplify the example code, error handling has been omitted.

    -   Name

        Create a name record, set the string values, "John" and "Smith",
        to the name, and set the name record as a child record of the
        contact record.

        When creating the name record, the first parameter of the
        `contacts_record_create()` function is the
        `_contacts_name._uri` property.

        ```c++
        contacts_record_h name;

        error_code = contacts_record_create(_contacts_name._uri, &name);

        error_code = contacts_record_set_str(name, _contacts_name.first, "John");
        error_code = contacts_record_set_str(name, _contacts_name.last, "Smith");

        error_code = contacts_record_add_child_record(contact, _contacts_contact.name, name);
        ```

    - Image

        Similarly, create an image record, set the values of the
        property, and add the image record to the contact as a child
        record:

        -   Create the image record with the
            `_contacts_image._uri` property.
        -   Set the path for the image in the `caller_id_path[]`
            variable, which is saved in the `_contacts_image.path`
            property by the `contacts_record_set_str()` function.

        ```c++
        contacts_record_h image;

        error_code = contacts_record_create(_contacts_image._uri, &image);

        char *resource_path = app_get_resource_path();
        char caller_id_path[1024];

        snprintf(caller_id_path, sizeof(caller_id_path), "%s/caller_id.jpg", resource_path);
        free(resource_path);

        error_code = contacts_record_set_str(image, _contacts_image.path, caller_id_path);

        error_code = contacts_record_add_child_record(contact, _contacts_contact.image, image);
        ```

    - Phone number

        Similarly again, create a phone number record, set the number,
        and add the phone number record to the contact as a
        child record.

        When creating a phone number record, use the
        `_contacts_number._uri` property as the second parameter of the
        `contacts_record_create()` function.

        ```c++
        contacts_record_h number;

        error_code = contacts_record_create(_contacts_number._uri, &number);

        error_code = contacts_record_set_str(number, _contacts_number.number, "+8210-1234-5678");

        error_code = contacts_record_add_child_record(contact, _contacts_contact.number, number);
        ```

    - Event

        An event consists of a type, date, and other properties. You can
        set various types of events, as defined in the
        `contacts_event_type_e` enumeration (in
        [mobile](../../api/mobile/latest/group__CAPI__SOCIAL__CONTACTS__SVC__RECORD__MODULE.html#ga434cc4b7cec62ccab70fa4825ce0801d)
        and
        [wearable](../../api/wearable/latest/group__CAPI__SOCIAL__CONTACTS__SVC__RECORD__MODULE.html#ga434cc4b7cec62ccab70fa4825ce0801d) applications).
        If the event type is `CUSTOM`, you can set a custom label for
        the event using the `_contacts_event.label` property.

        The following example sets a birthday event:

        -   In creating an event record, use the
            `_contacts_event._uri` property.
        -   The event type is set as `CONTACTS_EVENT_TYPE_BIRTH` in the
            `_contacts_event.type` property.
        -   When you set the event date, the date is an `integer` type
            property (`_contact_event.date`), calculated as year \*
            10000 + month \* 100 + day.

        Add the event record to the contact as a child record using the
        `contacts_record_add_child_record()` function.

        ```c++
        contacts_record_h event;

        error_code = contacts_record_create(_contacts_event._uri, &event);

        error_code = contacts_record_set_int(event, _contacts_event.type, CONTACTS_EVENT_TYPE_BIRTH);

        int year = 1990;
        int month = 5;
        int day = 21;
        int int_date = year * 10000 + month * 100 + day;

        error_code = contacts_record_set_int(event, _contacts_event.date, int_date);

        error_code = contacts_record_add_child_record(contact, _contacts_contact.event, event);
        ```

    For other contact properties, you can follow the same steps: create
    an appropriate record, set the values in the properties, and add the
    record to the contact as a child record.

3. Insert the contact into the Contacts database using the
    `contacts_db_insert_record()` function. All the child records added
    to the contact are inserted automatically along with the parent. The
    second parameter of the function is for the contact ID, which is
    unique and assigned by the system.

    ```c++
    int id = -1;

    error_code = contacts_db_insert_record(contact, &id);
    ```

4. Destroy the contact handle and release all its resources using the
    `contacts_record_destroy()` function.

    If you set the second parameter to `true`, the function destroys any
    child records automatically, irrespective of how the child records
    were added (individually or along with their parent record).

    ```c++
    error_code = contacts_record_destroy(contact, true);
    ```


<a name="deleting"></a>
## Deleting a Person

By using the `contacts_db_delete_record()` function, you can delete a
person record from the database with related child records. The person
ID is given to the function as the second parameter.

```c++
int person_id = ... /* Get the person ID */

error_code = contacts_db_delete_record(_contacts_person._uri, person_id);
```

<a name="linking"></a>
## Linking and Unlinking Persons and Contacts

A person can be associated with multiple contacts, so you need to know
how to manage the associations between a person and its contacts:
linking and unlinking.

When you create a contact, it is automatically linked to a person:

-   You can link the new contact to an existing person by setting the
    `_contacts_contact.link_mode` property as
    `CONTACTS_CONTACT_LINK_MODE_NONE`.

    Linking is determined based on the contact properties for phone
    numbers and email addresses (`_contacts_number.number` and
    `_contacts_email.email`). If an existing person has the same phone
    number or email address, but in a different address book, the
    contact is automatically linked to that person. However, if the
    phone number or email address leads to an existing contact in the
    same address book, the linking does not work.

- If the contact cannot be linked to any existing person, a new person
    is automatically created and linked to the contact.

```c++
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
   Contact is linked automatically if an existing person has the same number
   in a different address book
*/
error_code += contacts_db_insert_record(contact, NULL);

contacts_record_destroy(contact, true);
```

You can modify the contact and person linking, as needed:

-   To merge existing contacts into 1 person, use the
    `contacts_person_link_person()` function to link the contacts of one
    person to another person. The first parameter of the function is the
    ID of the person to be merged, and the second parameter is the ID of
    the person who will have all the merged contacts. After the linking,
    the former is deleted from the Contacts database. The latter person
    is left with both their original contacts and the other
    person's contacts.

    ```c++
    int person_id1 = ... /* Get the person ID whose contacts are merged elsewhere */
    int person_id2 = ... /* Get the person ID to which contacts are merged */

    error_code = contacts_person_link_person(person_id1, person_id2);
    ```

    The following figure illustrates the process of linking a person.
    Even though the contacts have different address books, they can be
    linked to the same person. After linking, the person2 record is
    destroyed automatically.

    **Figure: Linking a person**

    ![Linking a person](./media/app_contacts_linking.png)

- To separate (unlink) a contact record from the person record, use
    the `contacts_person_unlink_contact()` function. The function
    removes the contact from the person, creates a new person, and links
    the contact to the new person.

    ```c++
    int person_id = ... /* Get the person ID */
    int contact_id = ... /* Get the contact ID */
    int unlinked_person_id;

    error_code = contacts_person_unlink_contact(person_id, contact_id, &unlinked_person_id);
    ```

    The following figure illustrates the process of unlinking a contact.
    After unlinking, the person3 record is newly created.

    **Figure: Unlinking a contact**

    ![Unlinking a contact](./media/app_contacts_unlinking.png)
