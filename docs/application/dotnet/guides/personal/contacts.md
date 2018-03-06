# Contacts


You can help the user manage their contact information, such as address books, groups, persons, and phone logs. Since the contact information is stored in a contacts database, you must use the [Tizen.Pims.Contacts.ContactsManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsManager.html) class to manage the information.

The following figure illustrates the structure of the contact information in the database:

-   Each contact has their own details, such as a name, phone number, and email address.
- Each contact object is associated with a specific address book.

    The address book can be the local device address book, or an address book related to a specific service provider or application account (such as Samsung or Joyn).

- Multiple contacts can be associated with the same physical person.

    A [person object is an aggregation of one or multiple contact objects](#person).

In the figure, the Person1 is an aggregation of the Contact1, Contact2, and Contact3 instances, which all belong to different address books.

**Figure: Contact structure**

![Contact structure](./media/contacts_contact_structure.png)

The main features of the Tizen.Pims.Contacts namespace include:

-   Contact management
    -   You can manage individual [contact record details](#record), such as name, phone number, email, address, job, instant messenger, and company, with the help of [contact data-views](#view).

        You can also create lists of similar contacts to [manage them in batches](#list).

    - You can [insert contacts to](#create_contact), update them in, and remove them from the contacts database.
    - You can monitor [changes in the contacts database](#db).
    - You can search for and organize contacts using [filters and queries](#filter).
    - You can store social activities.

- Persons
    -   You can delete persons when no longer needed.
- Groups
    -   You can combine contacts in the same address book to create groups, allowing you to easily set the same properties (such as ringtones) for all contacts within the group.
    -   You can update and delete groups.
- Address books
    -   You can create address books using the local device (with no account), service providers (such as Samsung account), or applications (such as Joyn).
    -   You can determine to which address book each contact and group belong.
    -   If the address book is related to an account, you can handle the account using an account ID created with the [Account Manager](account.md). If the local device address book has no account, the related account ID is 0. You can create only one address book for each account.
- Speed dials
    -   You can create a speed dial, which is a shortcut dialing number key.
    -   You can update and delete speed dials.
- Phone logs
    -   You can create and store call or message logs.
    -   You can delete logs.

The contact service supports [vCards](#vcard), allowing you to import contact information from a vCard or export it to vCard format.

The following figure illustrates the different entities and their relationships in the contact service.

**Figure: Contact entities**

![Contact entities](./media/contacts_contact_entity.png)

<a name="person"></a>
## Contacts and Persons

Each contact is linked to at least 1 person, which is a kind of virtual contact that can be used to combine the details when multiple contacts from different address books represent the same individual.

The linking between contacts and persons functions as follows:

-   A person record cannot be created directly - it is created automatically when a contact record is inserted in the contacts database, and at the same time the contact is linked to the person.

    **Figure: Person is created along with the contact**

    ![Person is created along with the contact](./media/contacts_person_record.png)

- 2 persons (with contacts in different address books) can be linked together.

    As a result, the second person is destroyed automatically, and all the contacts linked to both persons are consequently linked to the 1 remaining person.

    **Figure: 2 persons can be linked**

    ![2 persons can be linked](./media/contacts_link_person.png)

    <a name="record"></a>
## Records
A record represents an actual record in the internal database, but you can also consider it a piece of information, such as an address, a phone number, or a group of contacts. A record can be a complex set of data, containing other data. For example, a contact record contains the `Address` property, which is a reference to an address record. An address record belongs to a contact record, and its `Id` property is set to the identifier of the corresponding contact. In this case, the address is the child record of the contact and the contact is the parent record.

You can create records in the database, retrieve individual record details or lists of multiple records, and delete records:

-   Creating a record

    When creating a record, you must specify what type of record you want to create by using its `Uri` property.

    ```
    /// Create a contact record
    ContactsRecord contact = new ContactsRecord(Contact.Uri);

    /// Create a name record
    ContactsRecord name = new ContactsRecord(Name.Uri);

    name.Set(Name.First, "first name");
    contact.AddChildRecord(Contact.Name, name);
    ```

- Obtaining the record using the ID

    An ID is a unique number for identifying records. Therefore, if you know the ID of a record, you can directly handle the record. The ID is a read-only property, which is available after the record has been inserted into the database. The following example gets a contact record using its ID:

    ```
    int contactId = 0;
    ContactsManager manager = new ContactsManager();
    /// Insert the contact made above to the database
    contactId = manager.Database.Insert(contact);
    contact.Dispose(); /// contact is no longer usable

    /// Retrieve the record; contact is the same record as before
    contact = manager.Database.Get(Contact.Uri, contactId);
    string displayName = NULL;
    displayName = contact.Get<string>(Contact.DisplayName);
    contact.Dispose(); /// Contact is no longer usable
    manager.Dispose();
    ```

- Obtaining the record from the parent record

    The following code example changes the country of addresses which are child records of a contact. Each address can be traversed by using the `GetChildRecord()` function. It is possible to apply the changes by updating the contact which is the parent record:

    ```
    int contactId = ... /// Acquire ID of the created contact

    int i = 0;
    ContactsManager manager = new ContactsManager();
    ContactsRecord contact = manager.Database.Get(Contact.Uri, contactId);
    int addressNum = contact.GetChildRecordCount(Contact.Address);
    for (i = 0; i < addressNum; i++)
    {
        ContactsRecord address = NULL;
        /// Get the address record
        address = contact.GetChildRecord(Contact.Address, i);
        address.Set(Address.Country, "Korea");
    }
    manager.Database.Update(contact);
    contact.Dispose();
    manager.Dispose();
    ```

To manage the record, you can use the URI or views:

-   URI

    A record type is identified by a structure called the view, which contains identifiers of its properties. Every class in the [Tizen.Pims.Contacts.ContactsViews](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.html) namespace has a `Uri` field that uniquely identifies the view. In many cases, you must provide the `Uri` value to indicate what type of record you want to create or operate on.

- <a name="view"></a>Views

    Views are provided to access and handle entities. A data-view is a structure which has property elements. For example, the [Tizen.Pims.Contacts.ContactsViews.Contact](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Contact.html) class describes the properties of the contact record. Its properties include, for example, name, company, and nickname of the contact. The property elements have their data types and names.

    The record types that have an `Id` property hold identifiers of other records. For example, the name, number, and email views hold the ID of their corresponding contacts in the `ContactId` property as children of the corresponding contact records. A data-view is almost the same as a database "VIEW", which limits access and guarantees performance. A "record" represents a single row of the data-views.

    The property type `record` means that the parent record can have child records. For example, a Contact record has `Name`, `Number`, and `Email` properties, which means that records of those types can be children of the contact type records.

    For more information, see the view classes in the `Tizen.Pims.Contacts.ContactsViews` namespace.

### Child Records

Some record types can be a parent of other records. Effectively, a record can be a node in a tree or graph of relations between records.

The following code example inserts an address record into a contact record. It is not necessary to insert or destroy all records. Only the parent record needs to be inserted into the database to store all the information, and when the parent record is destroyed, the child records are also destroyed automatically.

```
ContactsRecord contact = new ContactsRecord(Contact.Uri);

/// Image and address record can be child records of contact record
ContactsRecord image = new ContactsRecord(Image.Uri);
image.Set(Image.Path, "resource/image.jpg");
contact.AddChildRecord(Contact.Image, image);

ContactsRecord address = new ContactsRecord(Address.Uri);
address.Set(Address.Country, "Korea");
contact.AddChildRecord(Contact.Address, address);

/// Insert contact to the database
ContactsManager manager = new ContactsManager();
int contactId = 0;
contactId = manager.Database.Insert(contact);
contact.Dispose();
manager.Dispose();
```

Identifiers can be used to establish a relationship between 2 records. The following code example sets an address record's `ContactId` property to the ID of the contact. The `ContactId` property relates between the address record and the contact which is identified by the `ContactId` property. After the ID is set, the address becomes one of the addresses connected to the contact. The address is now the contact's child record, and the contact is the parent record.

```
int contactId = ... /// Acquire the ID of the created contact
ContactsRecord address = new ContactsRecord(Address.Uri);
address.Set(Address.ContactId, contactId);

/// Insert address record to the database
ContactsManager manager = new ContactsManager();
manager.Database.Insert(address);
address.Dispose();
manager.Dispose();
```

<a name="list"></a>
## Contact Lists and Batch Operations

Use the [Tizen.Pims.Contacts.ContactsList](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsList.html) class to handle lists of records with the same type.

To create a list:

-   Create a list:

    ```
    ContactsList list = new ContactsList();

    /// Use the list

    list.Dispose();
    ```

- Obtain a list by performing a query to the database:

    ```
    ContactsManager manager = new ContactsManager();
    ContactsList list = manager.Database.GetAll(Person.Uri, 0, 0);

    /// Use the list

    list.Dispose();
    ```

To manage the list:

-   Traversing

    The list can be traversed. Use the `MoveFirst()`, `MoveLast()`, `MoveNext()`, and `MovePrevious()` methods of the `Tizen.Pims.Contacts.ContactsList` class to move the cursor in the list.

    To get a record of the current cursor, use the `GetCurrentRecord()` method.

    The following example loops through a list:

    ```
    ContactsManager manager = new ContactsManager();
    ContactsList list = manager.Database.GetAll(Person.Uri, 0, 0);

    do
    {
        ContactsRecord record = list.GetCurrentRecord();
        string name = record.Get<string>(Person.DisplayName);
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, name);
    } while (list.MoveNext());

    list.Dispose();
    manager.Dispose();
    ```

- Adding and removing

    Use the `AddRecord()` method to add records and the `RemoveRecord()` method to remove records.

    The following example adds records to the list:

    ```
    ContactsRecord group1 = new ContactsRecord(Group.Uri);
    group1.Set(Group.Name, "group test1");
    ContactsRecord group2 = new ContactsRecord(Group.Uri);
    group2.Set(Group.Name, "group test2");

    ContactsList list = new ContactsList();

    /// Add records to the list
    list.AddRecord(group1);
    list.AddRecord(group2);

    ContactsManager manager = new ContactsManager();
    manager.Database.Insert(list);

    list.Dispose();
    manager.Dispose();
    ```

    <a name="filter"></a>
## Filters and Queries

Queries are used to retrieve [person](#get_contact) data which satisfies a given criteria, such as an integer property being greater than a given value, or a string property containing a given substring. A query needs a filter which can set the conditions for the search. The [Tizen.Pims.Contacts.ContactsQuery](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsQuery.html) class provides methods for sorting set projections and removing duplicated results.

To filter, sort, and query contact data:

-   Filtering

    When creating a filter, specify the filter type you want to create using the `Uri` property.

    To manage filters, multiple conditions can be added to a filter. Join the conditions or multiple filters by using the [Tizen.Pims.Contacts.ContactsFilter.LogicalOperator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsFilter.LogicalOperator.html) enumerator values:

    -   To create a composite filter with the `Or` operator:

        ```
        /// Filtering for contacts whose display name is James or Jake
        ContactsFilter filter = new ContactsFilter(Person.Uri, Person.DisplayName, ContactsFilter.StringMatchType.Contains, "James");
        filter.AddCondition(ContactsFilter.LogicalOperator.Or, Person.DisplayName, ContactsFilter.StringMatchType.Contains, "Jake");
        ```

    - To create a joined filter with the `And` operator:

        ```
        /// Filtering for contacts who are both favorites and whose display name is James or Jake
        ContactsFilter filter1 = new ContactsFilter(Person.Uri, Person.DisplayName, ContactsFilter.StringMatchType.Contains, "James");
        filter1.AddCondition(ContactsFilter.LogicalOperator.Or, Person.DisplayName, ContactsFilter.StringMatchType.Contains, "Jake");

        ContactsFilter filter2 = new ContactsFilter(Person.Uri, Person.IsFavorite, true);

        filter1.AddFilter(ContactsFilter.LogicalOperator.And, filter2);
        ```

    The operator precedence in filters is determined by the order in which the conditions and filters are added. The following table shows the results, if the following sequences are added.

    **Table: Filters**

    | Filters                                  | Result                                   |
    |----------------------------------------|----------------------------------------|
    | Condition C1<br>OR<br>Condition C2<br>AND<br>Condition C3 | (C1 OR C2) AND C3                        |
    | **Filter F1**:<br>Condition C1<br>OR<br>Condition C2<br><br>**Filter F2**:<br>Condition C3<br>OR<br>Condition C4<br><br>**Filter F3**:<br>Condition C5<br>AND<br>F1<br>AND<br>F2 | (C5 AND F1) AND F2, which is<br>(C5 AND (C1 OR C2)) AND (C3 OR C4) |

    The following example creates a filter which accepts addresses with their contact's ID equal to a given ID (integer filter), or their country property equal to "Korea" (string filter). To get the filtered results, create a query and add the filter to it. The results are received in a list.

    ```
    int contactId = ... /// Acquire the ID of the created contact

    ContactsFilter filter = new ContactsFilter(Address.Uri, Address.ContactId, ContactsFilter.IntegerMatchType.Equal, contactId);
    filter.AddCondition(ContactsFilter.LogicalOperator.Or, Address.Country, ContactsFilter.StringMatchType.Exactly, "Korea");
    ContactsQuery query = new ContactsQuery(Address.Uri);
    query.SetFilter(filter);

    ContactsManager manager = new ContactsManager();
    ContactsList list = manager.Database.GetRecordsWithQuery(query, 0, 0);

    filter.Dispose();
    query.Dispose();

    /// Use the list

    list.Dispose();
    manager.Dispose();
    ```

- Sorting

    To sort the query result list by the property ID, use the `SetSort()` method. The first parameter is the property ID.

    The following example sorts the query results by the person ID:

    ```
    ContactsFilter filter = new ContactsFilter(Person.Uri, Person.DisplayName, ContactsFilter.StringMatchType.Contains, "Joe");
    ContactsQuery query = new ContactsQuery(Person.Uri);
    query.SetFilter(filter);
    query.SetSort(Person.Id, true);

    ContactsManager manager = new ContactsManager();
    ContactsList list = manager.Database.GetRecordsWithQuery(query, 0, 0);

    filter.Dispose();
    query.Dispose();
    list.Dispose();
    manager.Dispose();
    ```

- Projection querying

    Projection allows you to query the data for only the specific properties of a record that you need, at lower latency and cost than retrieving all properties. To use projection, use the `SetProjection()` method.

    The following example creates a filter which gets only the person ID, display name, and image thumbnail path from the person records which have "test" (string filter) as the vibration path. Create a query and add the filter to it; the results are received in a list.

    ```
    ContactsFilter filter = new ContactsFilter(Person.Uri, Person.Vibration, ContactsFilter.StringMatchType.Contains, "test");
    ContactsQuery query = new ContactsQuery(Person.Uri);
    query.SetFilter(filter);

    uint[] projection = {Person.Id, Person.DisplayName, Person.ThumbnailPath};
    query.SetProjection(projection);

    ContactsManager manager = new ContactsManager();
    ContactsList list = manager.Database.GetRecordsWithQuery(query, 0, 0);
    filter.Dispose();
    query.Dispose();

    /// Use the list

    list.Dispose();
    manager.Dispose();
    ```

- Removing duplicates

    If you query a read-only view with a set projection, the result list can contain duplicates. Remove duplicates using the `SetDistinct()` method.

    The following example removes duplicates:

    ```
    ContactsFilter filter = new ContactsFilter(PersonNumber.Uri, PersonNumber.HasPhoneNumber, true);
    ContactsQuery query = new ContactsQuery(PersonNumber.Uri);
    query.SetFilter(filter);

    uint[] projection = {PersonNumber.PersonId, PersonNumber.DisplayName};
    query.SetProjection(projection);
    /// Set distinct (remove duplicates)
    query.SetDistinct(true);

    ContactsManager manager = new ContactsManager();
    ContactsList list = manager.Database.GetRecordsWithQuery(query, 0, 0);
    filter.Dispose();
    query.Dispose();

    /// Use the list

    list.Dispose();
    manager.Dispose();
    ```

## Prerequisites

To enable your application to use the contacts functionality:

1.  To use the [Tizen.Pims.Contacts](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/contact.read</privilege>
       <privilege>http://tizen.org/privilege/contact.write</privilege>
       <privilege>http://tizen.org/privilege/callhistory.read</privilege>
       <privilege>http://tizen.org/privilege/callhistory.write</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Pims.Contacts and [Tizen.Pims.Contacts.ContactsViews](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.html) namespaces, include them in your application:

    ```
    using Tizen.Pims.Contacts;
    using Tizen.Pims.Contacts.ContactsViews;
    ```

    <a name="create_contact"></a>
## Creating a Contact

Creating a new contact involves setting the contact properties and inserting the contact into the contact database.

Some contact properties are defined as child records that are associated with the parent record. For a detailed list of the contact properties, see the [Tizen.Pims.Contacts.ContactsViews.Contact](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Contact.html) class. If the property type is `record`, the property is defined as a child record. The property description defines whether a single child record or multiple child records are allowed for a specific property.

When you create a new contact, the system automatically creates a new person associated with that contact. A person is an aggregation of 1 or more contacts associated with the same individual. A contact is always associated with a person.

To create a new contact:

1.  Create a contact with the `Uri` property of the `Tizen.Pims.Contacts.ContactsViews.Contact` class:

    ```
    ContactsRecord record = new ContactsRecord(Contact.Uri);
    ```

2. Set the contact properties:

    -   To set the contact's name:

        1.  Create a name record with the `Uri` property of the [Tizen.Pims.Contacts.ContactsViews.Name](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Name.html) class:

            ```
            ContactsRecord name = new ContactsRecord(Name.Uri);
            ```

        2. Set the contact's first name with the `First` property:

            ```
            name.Set(Name.First, "John");
            ```

        3. Set the contact's last name with the `Last` property:

            ```
            name.Set(Name.Last, "Smith");
            ```

        4. Set the name record as a child record of the contact record with the `Name` property of the `Tizen.Pims.Contacts.ContactsViews.Contact` class:

            ```
            contact.AddChildRecord(Contact.Name, name);
            ```

    - To set an image for the contact:

        1.  Create an image record with the `Uri` property of the [Tizen.Pims.Contacts.ContactsViews.Image](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Image.html) class:

            ```
            ContactsRecord image = new ContactsRecord(Image.Uri);
            ```

        2. Define the image, and set the image with the `Path` property:

            ```
            image.Set(Image.Path, "imagePath/image.jpg");
            ```

        3. Set the image record as a child record of the contact record with the `Image` property of the `Tizen.Pims.Contacts.ContactsViews.Contact` class:

            ```
            contact.AddChildRecord(Contact.Image, image);
            ```

    - To set an event for the contact:

        An event consists of an event type, date, and other properties. You can set various types of events for the contact, as defined in the [Tizen.Pims.Contacts.ContactsViews.Event.TypeValue](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Event.TypeValue.html) enumeration. If the event type is `Custom`, you can set a custom label for the event with the `Label` property of the [Tizen.Pims.Contacts.ContactsViews.Event](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Event.html) class.

        To set a birthday event:

        1.  Create an event record with the `Uri` property of the `Tizen.Pims.Contacts.ContactsViews.Event` class:

            ```
            ContactsRecord birthday = new ContactsRecord(Event.Uri);
            ```

        2. Set the event date with the `Date` property. The date is an integer.

            ```
            int year = 1990;
            int month = 5;
            int day = 21;
            int date = year * 10000 + month * 100 + day;

            birthday.Set(Event.Date, date);
            ```

        3. Set the event type to birthday with the `Type` property:

            ```
            birthday.Set(Event.Type, Event.TypeValue.Birthday);
            ```

        4. Set the event record as a child record of the contact record with the `Event` property of the `Tizen.Pims.Contacts.ContactsViews.Contact` class:

            ```
            contact.AddChildRecord(Contact.Event, birthday);
            ```

    - To set the contact's phone number:

        1.  Create a phone number record with the `Uri` property of the [Tizen.Pims.Contacts.ContactsViews.Number](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsViews.Number.html) class:

            ```
            ContactsRecord number = new ContactsRecord(Number.Uri);
            ```

        2. Set the phone number with the `NumberData` property:

            ```
            number.Set(Number.NumberData, "+8210-1234-5678");
            ```

        3. Set the phone number record as a child record of the contact record with the `Number` property of the `Tizen.Pims.Contacts.ContactsViews.Contact` class:

            ```
            contact.AddChildRecord(Contact.Number, number);
            ```

    Set other contact properties similarly, as needed.

3. Insert the contact into the contact database using the `Insert()` method of the [Tizen.Pims.Contacts.ContactsDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsDatabase.html) class. All child records added to the contact are inserted automatically along with the parent.

    The system assigns a unique ID to the contact, and the method returns it.

    ```
    ContactsManager manager = new ContactsManager();
    int ContactId = manager.Database.Insert(contact);
    ```

4. When no longer needed, destroy the contact instance to release all its resources:

    ```
    contact.Dispose();
    manager.Dispose();
    ```

    All child records of the given record are also destroyed.

    <a name="get_contact"></a>
## Retrieving Persons

You can access contact details through persons.

To retrieve a single person:

1.  Retrieve a person record using the person ID:

    ```
    int personId = ...; /// Get the person ID
    ContactsManager manager = new ContactsManager();
    ContactsRecord person = manager.Database.Get(Person.Uri, personId);
    ```

2. When no longer needed, destroy the person instance:

    ```
    person.Dispose();
    manager.Dispose();
    ```

To retrieve multiple persons:

1.  Retrieve a list of all persons, or a filtered list of persons:

    -   To retrieve a list of all persons:

        ```
        ContactsManager manager = new ContactsManager();
        ContactsList persons = manager.Database.GetAll(Person.Uri, 0, 0);
        ```

    - To retrieve a filtered list of persons:

        1.  Create a filter.

            The following example adds a string-based filtering condition that retrieves the persons whose display name contains the string "John":

            ```
            ContactsFilter filter = new ContactsFilter(Person.Uri, Person.DisplayName, ContactsFilter.StringMatchType.Contains, "John");
            ```

        2. To add more conditions, use an operator between the conditions.

            The following example adds an AND operator and an additional condition which retrieves the persons who are set as favorites.

            The combination of the AND operator and the 2 conditions means that the filter only retrieves the persons whose display name contains the string "John" and who are set as favorites.

            ```
            filter.AddCondition(ContactsFilter.LogicalOperator.And, Person.IsFavorite, true);
            ```

        3. Set the filter to the query:

            ```
            ContactsQuery query = new ContactsQuery(Person.Uri);
            query.SetFilter(filter);
            ```

        4. Retrieve the filtered list of persons:

            ```
            ContactsManager manager = new ContactsManager();
            ContactsList persons = manager.Database.GetRecordsWithQuery(query, 0, 0);
            ```

            The third parameter defines a limit for the number of results. If you set it to 0, the list returns all persons matching the query.

        5. When no longer needed, destroy the filter and query instances:

            ```
            filter.Dispose();
            query.Dispose();
            manager.Dispose();
            ```

    - To retrieve a list of persons matching a search keyword, use the `Search()` method of the [Tizen.Pims.Contacts.ContactsDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsDatabase.html) class with the search keyword.

        The following example shows how to find all person records that contain the keyword "John":

        ```
        ContactsManager manager = new ContactsManager();
        ContactsList persons = manager.Database.Search(Person.Uri, "John", 0, 0);
        ```

2. Iterate through the list of found persons, and retrieve person details:

    The following example iterates through the list and retrieves the display name of each person:

    ```
    do
    {
        ContactsRecord person = persons.GetCurrentRecord();
        String displayName = person.Get<String>(Person.DisplayName);
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, displayName);
    } while (persons.MoveNext());
    ```

    <a name="db"></a>
## Managing Database Change Notifications

To detect the person and group changes in the contacts database, add event handlers using the `AddDBChangedEventHandler()` method of the [Tizen.Pims.Contacts.ContactsDatabase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsDatabase.html) class. To ignore database changes, remove the event handler using the `RemoveDBChangedEventHandler()` method.

```
public static void DBChangedHandler(object sender, DBChangedEventArgs args)
{
    var viewUri = args.ViewUri;
    /// Do something about the change
}

/// Add an event handler
manager = new ContactsManager();
manager.Database.AddDBChangedEventHandler(Contact.Uri, DBChangedHandler);
```

<a name="vcard"></a>
## Managing vCards

The [Tizen.Pims.Contacts.ContactsVcard](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Pims.Contacts.ContactsVcard.html) class provides methods for parsing and making vCards. The vCard functions are based on the [vCard v3.0 specification](http://www.ietf.org/rfc/rfc2426.txt).

-   You can import contact information by parsing vCards from stream or from a file:

    -   To parse a vCard from a stream and insert it to the database:

        ```
        /// Make a contact record list from the vCard stream
        ContactsList list = ContactsVcard.Parse(vcardStream);

        /// Use the contact record list

        list.Dispose();
        ```

    - To parse a vCard from a file and insert it to the database:

        ```
        ContactsManager manager = new ContactsManager();

        /// Get a contact record
        static bool ParseCallback(ContactsRecord record)
        {
            manager.Database.Insert(record);

            /// Return false to break out of the loop
            /// Return true to continue parsing with the next iteration of the loop
            return true;
        }

        /// Parse the vCard from a file
        ContactsVcard.ParseForEach("/filepath/test.vcf", ParseCallback);
        manager.Dispose();
        ```

- You can export contact information and make a vCard stream from a contact, person, or My profile record. To make a vCard stream using a contact record:

    ```
    int contactId = ... /// Acquire ID of the created contact

    ContactsManager manager = new ContactsManager();
    ContactsRecord record = manager.Database.Get(Contact.Uri, contactId);
    string vcardStream = ContactsVcard.Compose(record);

    /// Use the vCard stream

    record.Dispose();
    manager.Dispose();
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
