
# Group Management

The basic tasks involved in group management operations are retrieving
group information, creating, updating, and deleting groups, and managing
group members. The following sections provide you with the fundamental
building blocks for combining individual contacts to groups to manage
them more efficiently.

<a name="retrieving"></a>
## Retrieving Groups

A group is a collection of contacts from the same address book.
Retrieving a single group is very similar to retrieving a single person:
use the same function (`contacts_db_get_record()`) while setting the
first parameter to the relevant group view (`_contacts_group._uri`).

```c++
contacts_record_h group;
int group_id = ... /* Get the group ID */
int error_code;

error_code = contacts_db_get_record(_contacts_group._uri, group_id, &group);

if (error_code != CONTACTS_ERROR_NONE)
    dlog_print(DLOG_ERROR, LOG_TAG, "failed to get record: error code = %d", error_code);
```

The following example retrieves a list of groups, whose name contains
the strings "neighbors" or "friend". You can search for the groups
meeting the condition using queries and filters:

1.  Create a filter handle.
2. Add search conditions to the filter handle.

    As shown in the example, the search strings and the `OR` operator
    are added to the filter handle.

3. Make a query with the filter, and apply the query to the
    Contacts database.

To simplify the example code, error handling has been omitted.

```c++
contacts_list_h list = NULL;
contacts_query_h query = NULL;
contacts_filter_h filter = NULL;
int error_code;

error_code = contacts_query_create(_contacts_group._uri, &query);
error_code = contacts_filter_create(_contacts_group._uri, &filter);

error_code = contacts_filter_add_str(filter, _contacts_group.name, CONTACTS_MATCH_CONTAINS, "neighbors");
error_code = contacts_filter_add_operator(filter, CONTACTS_FILTER_OPERATOR_OR);
error_code = contacts_filter_add_str(filter, _contacts_group.name, CONTACTS_MATCH_CONTAINS, "friend");

error_code = contacts_query_set_filter(query, filter);
error_code = contacts_db_get_records_with_query(query, 0, 0, &list);

/* Destroy the filter and query handles and release all their resources */
error_code = contacts_filter_destroy(filter);
error_code = contacts_query_destroy(query);
```

The third parameter of the `contacts_db_get_records_with_query()`
function defines a limit for the number of results. Since the parameter
is set to `0` in the above example, the function returns all the groups
matching the query.

<a name="updating"></a>
## Updating Groups

To update information in an existing group, you must first retrieve the
group to update. Then, you can change the group properties, apply the
changes to the database, and finally destroy the group handle and
release all the resources for it.

1.  Retrieve the group you want to update:

    ```c++
    int group_id = ... /* Get the group ID */

    contacts_record_h group = NULL;

    error_code = contacts_db_get_record(_contacts_group._uri, group_id, &group);
    ```

    You can also retrieve the group using a search function with
    queries, such as `contacts_db_get_records_with_query()`.

2. Set the properties to be changed.

    The following example changes the name and image of the group:

    ```c++
    error_code = contacts_record_set_str(group, _contacts_group.name, "Family");

    char *resource_path = app_get_resource_path();
    char temp_path[1024];
    snprintf(temp_path, sizeof(temp_path), "%s/group_image_new.jpg", resource_path);
    free(resource_path);
    error_code = contacts_record_set_str(group, _contacts_group.image_path, temp_path);
    ```

3. Apply the changes to the database:

    ```c++
    error_code = contacts_db_update_record(group);
    ```

4. Destroy the handle and release its resources.

    If you set the second parameter to `true`, the function destroys any
    child records automatically.

    ```c++
    error_code = contacts_record_destroy(group, true);
    ```


<a name="creating"></a>
## Creating a Group

To create a new group, you must create a group handle, set the group
properties, insert the group into the database, and destroy the group
handle:

1.  Create a group handle.

    The first parameter of the `contacts_record_create()` function
    specifies the record type to be created. In this case, the value is
    the `_contacts_group._uri` property, because you are creating
    a group. The second parameter stores the new group handle.

    ```c++
    contacts_record_h group = NULL;

    error_code = contacts_record_create(_contacts_group._uri, &group);
    ```

2. Set the group properties.

    You can set the group properties using the
    `contacts_record_set_XXX()` functions with the relevant properties
    as the second parameter. Depending on the property type, you must
    use the proper functions, respectively.

    -   If you set the group name, which is a `string` type, use the
        `contacts_record_set_str()` function with the
        `_contacts_group.name` property as the second parameter:

        ```c++
        error_code = contacts_record_set_str(group, _contacts_group.name, "Neighbors");
        ```

    - If you set the group image property, first define the image file
        path and then set it to the property similarly as the group name
        above:

        ```c++
        char *resource_path = app_get_resource_path();
        char temp_path[1024];
        snprintf(temp_path, sizeof(temp_path), "%s/group_image.jpg", resource_path);
        free(resource_path);
        error_code = contacts_record_set_str(group, _contacts_group.image_path, temp_path);
        ```

    Set other group properties similarly, as needed.

3. Insert the group into the Contacts database:

    ```c++
    int added_group_id = -1;

    error_code = contacts_db_insert_record(group, &added_group_id);
    ```

4. Destroy the group handle and release its resources.

    If you set the second parameter to `true`, the function destroys any
    child records automatically.

    ```c++
    error_code = contacts_record_destroy(group, true);
    ```


<a name="deleting"></a>
## Deleting a Group

You can delete a group record from the Contacts database exactly like
you delete a person: use the `contacts_db_delete_record()` function. The
difference is the first parameter, which for the group deletion is set
to the group property (`_contacts_group._uri`). The ID of the group to
be deleted is given as the second parameter.

```c++
int group_id = ... /* Get the group ID */

error_code = contacts_db_delete_record(_contacts_group._uri, group_id);
```

<a name="managing"></a>
## Managing Group Members

Group members are contacts from the same address book. With a contact ID
and group ID on hand, you can add and remove contacts within a group
using the `contacts_group_add_contact()` and
`contacts_group_remove_contact()` functions:

-   Adding a group member:

    ```c++
    int contact_id = ... /* Get the contact ID */
    int group_id = ... /* Get the group ID */

    error_code = contacts_group_add_contact(group_id, contact_id);
    ```

- Removing a group member:

    ```c++
    int contact_id = ... /* Get the contact ID */
    int group_id = ... /* Get the group ID */

    error_code = contacts_group_remove_contact(group_id, contact_id);
    ```

Since each contact is associated with a person, you can retrieve all the
member details of a group as follows:

1.  Create and run a query for retrieving a list of all persons in the
    group:

    ```c++
    contacts_query_h query = NULL;
    contacts_filter_h filter = NULL;
    contacts_list_h list = NULL;

    /* Create a person query with a filter for the group ID */
    contacts_query_create(_contacts_person_group_assigned._uri, &query);
    contacts_filter_create(_contacts_person_group_assigned._uri, &filter);
    contacts_filter_add_int(filter, _contacts_person_group_assigned.group_id, CONTACTS_MATCH_EQUAL, group_id);
    contacts_query_set_filter(query, filter);

    /* Run the query to retrieve a list of all persons assigned to the specified group */
    contacts_db_get_records_with_query(query, 0, 0, &list);
    ```

2. Iterate through the query answer list and retrieve the
    person details.

    The following example retrieves the ID and display name of
    each person.

    ```c++
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

3. When no longer needed, destroy the handles to release all the
    resources assigned to them:

    ```c++
    contacts_list_destroy(list, true);
    contacts_filter_destroy(filter);
    contacts_query_destroy(query);
    ```
