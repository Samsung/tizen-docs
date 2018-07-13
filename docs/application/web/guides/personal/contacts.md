# Contacts

You can manage the contacts and persons listed in your address books. A `Contact` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Contact) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Contact) applications) is always associated with a specific address book. A `Person` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Person) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Person) applications) is an aggregation of 1 or more contacts associated with the same person.

This feature is supported in mobile and wearable applications only.

The main features of the Contact API include:

- Address book management

  You can [create a new address book](#creating-an-address-book), or [access the device address books](#getting-address-books) to access existing contacts.

- Contact management

  You can [add](#adding-a-contact) and [manage](#managing-a-contact) a single contact at a time using synchronous operations.

  You can also keep the address book in your application synchronized with an external contact manager by [receiving notifications](#receiving-notifications-on-contact-changes) in your application when contact information changes. Every change made to the address book triggers an event for which you can define a notification.

- Group and multiple contact management

  You can [manage contact groups](#managing-contact-groups), including getting, updating, and deleting them, using the applicable methods of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications).

  You can also [create](#adding-multiple-contacts-in-the-batch-mode) and [manage](#managing-multiple-contacts-in-the-batch-mode) multiple contacts simultaneously using the batch mode. The batch mode provides faster, optimized processing of multiple contacts.

   > **Note**  
   > The batch mode does not provide progress information about operations. To ensure that you can view the progress, break the batch operation down into multiple smaller batch operations. For example, break down a batch of 100 update requests into 10 batch operations that update 10 records at a time. Additionally, breaking down a batch operation helps you avoid blocking other database operations, such as add or remove.

  If you want to receive notifications for batch mode operations, note that each requested batch operation generates only a single event.

- Person management

  You can [manage persons](#managing-persons) using the applicable methods of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications).

  Persons are automatically added or modified when contacts are added to or unlinked from existing persons. You cannot add persons directly.

- vCard format conversions

  You can convert the contacts to [vCard format](https://tools.ietf.org/html/rfc2426) or back to [import](#importing-contacts) and [export](#exporting-contacts) contacts.

  The vCard (RFC 2426) file format (`.vcf` or `.vcard`) is a standard for electronic business cards, which contain contact information, such as name, address, phone numbers, email addresses, URLs, logos, photographs, and audio clips.

  The Contact API supports vCard version 3.0.

## Prerequisites

To enable your application to use the contact functionality:

1. To make your application visible in the Tizen Store only for devices that support the contact feature, the application must specify the following feature in the `config.xml` file:

   ```
   <widget>
      <tizen:feature name="http://tizen.org/feature/contact"/>
   </widget>
   ```

   Additionally, to double-check the Contact API support (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html) applications) while the application is running, use the `tizen.systeminfo.getCapability()` method and enable or disable the code that needs the API, as needed.

2. To use the Contact API, the application has to request permission by adding the following privileges to the `config.xml` file:

   ```
   <tizen:privilege name="http://tizen.org/privilege/contact.read"/>
   <tizen:privilege name="http://tizen.org/privilege/contact.write"/>
   ```

## Creating an Address Book

> **Note**  
> The created address book is associated with a specified account. Therefore, you must retrieve the account before creating a new address book.

To create a new address book:

1. Declare a variable to store the created address book:

   ```
   var myAddressBook = null;
   ```

2. Define a success callback for the `getAccounts()` method. The callback receives a list of `Account` objects (in [mobile](../../api/latest/device_api/mobile/tizen/account.html#Account) and [wearable](../../api/latest/device_api/wearable/tizen/account.html#Account) applications). Use the first account ID to construct a new `AddressBook` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications).   
  Add the new address book to the system using the `addAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications):

   ```
   function getAccountsSuccess(accounts) {
       var account = accounts[0];
       if (account) {
           /* New address book can be created and added */
           myAddressBook = new tizen.AddressBook(account.id, 'remote address book');
           tizen.contact.addAddressBook(myAddressBook);
           console.log('New address book created with ID=' + myAddressBook.id);
       }
   }
   ```

3. To retrieve available accounts, use the `getAccounts()` method. The following method call invokes the `getAccountsSuccess` event handler defined above.

   ```
   tizen.account.getAccounts(getAccountsSuccess, function(err));
   ```

## Getting Address Books

You must retrieve the `Contact` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Contact) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Contact) applications) from the applicable address book to access an existing contact.

To access the address books in which the contacts are listed:

- To get the default address book, use the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications) to retrieve the default address book as an `AddressBook` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications):

  ```
  var myAddressbook;

  /* Get the default address book */
  myAddressbook = tizen.contact.getDefaultAddressBook();
  ```

- To get all available address books, use the `getAddressBooks()` method. This method passes an array of `AddressBook` objects to the success event handler.

  ```
  var addressBook;

  function addressBooksCB(addressBooks) {
      if (addressBooks.length > 0) {
          addressBook = addressBooks[0];
          console.log('The address book name is ' + addressBook.name);
      }
  }

  /* Get the list of available address books */
  tizen.contact.getAddressBooks(addressBooksCB);
  ```

  All available address books on the device are retrieved. You can use an `AddressBook` object ID to select a specific address book with the `getAddressBook()` method, if you know the ID of the address book in advance.

## Adding a Contact

You can add a contact using the applicable methods of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications).

To add a contact to an address book:

1. Retrieve the default system address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications):

   ```
   var addressbook = tizen.contact.getDefaultAddressBook();
   ```

2. Create a `Contact` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Contact) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Contact) applications) and define its properties as a `ContactInit` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactInit) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactInit) applications) (the parameter of the `Contact` constructor):

   ```
   var contact = new tizen.Contact({
       name: new tizen.ContactName({firstName: 'Jeffrey', lastName: 'Hyman'}),
       emails: [new tizen.ContactEmailAddress('user@example.com')]
   });
   ```

3. Add the `Contact` object to the default address book with the `add()` method of the `AddressBook` interface:

   ```
   addressbook.add(contact);
   ```

## Managing a Contact

You can manage a contact by using the applicable methods of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications). When managing a single contact at a time, the operations are handled in a synchronous mode.

To manage a contact in your address book:

1. To retrieve a single contact, use the `get()` method of the `AddressBook` interface with the `ContactID` as a parameter:  
   The following example uses the object of the `ContactRef` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactRef) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactRef) applications). The `ContactRef` object contains both `AddressBook` ID and `Contact` ID (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Contact) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Contact) applications).

   ```
   /* contactRef is retrieved by other APIs */
   var contactRef;
   try {
       /* Retrieve the contact corresponding to the given reference */
       var addressBook = tizen.contact.getAddressBook(contactRef.addressBookId);
       var contact = addressBook.get(contactRef.contactId);
   }
   ```

2. To manage a single contact:    

   1. Retrieve the default address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications).

      ```
      var addressbook = tizen.contact.getDefaultAddressBook();
      ```

   2. Retrieve contacts stored in the address book by using the `find()` method of the `AddressBook` interface:

      ```
      var filter = new tizen.AttributeFilter('name.firstName', 'CONTAINS', 'Chris');
      var sortMode = new tizen.SortMode('name.lastName', 'ASC');

      try {
          addressbook.find(contactsFoundCB, null, filter, sortMode);
      }
      ```

      When searching for contacts, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#contact-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, contacts whose first name contains "Chris" are retrieved and sorted in the ascending order based on their last name. The filter includes the standard English characters in the uppercase and lowercase. The entire list consists of ASCII characters from 32 to 126, and from 160 to 255.

      The contacts that match the filter are passed as an array to the registered success event handler in the selected sorting order.

   3. Update or delete the found contact inside the `contactsFoundCB` event handler.

      In this example, the first name of the first contact is changed and the contact is updated in the address book using the `update()` method. The second contact is deleted using the `remove()` method.

      ```
      /* Define the event success callback */
      function contactsFoundCB(contacts) {
          contacts[0].name.firstName = 'Christopher';
          try {
              /* Update the first found contact */
              addressbook.update(contacts[0]);

              /* Delete the second found contact */
              addressbook.remove(contacts[1].id);
          }
      }
      ```

## Receiving Notifications on Contact Changes

You can keep the address book in your application synchronized with the external contact manager by receiving notifications in your application when contact information is added, updated, or deleted.

The `addChangeListener()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications) registers an event listener, which starts asynchronously once the `addChangeListener()` method returns the subscription identifier for the listener. You can use the `AddressBookChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBookChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBookChangeCallback) applications) to define listener event handlers for receiving the notifications.

To receive notifications when contact information changes:

1. Define the needed variables:

   ```
   /* Watcher identifier */
   var watcherId = 0;

   /* This example assumes that the address book is initialized */
   var addressbook;
   ```

2. Define the event handlers for different notifications about changes in the selected address book using the `AddressBookChangeCallback` listener interface:

   ```
   var watcher = {
       /* When contacts are added */
       oncontactsadded: function(contacts) {
           console.log(contacts.length + ' contacts were added');
       },

       /* When contacts are updated */
       oncontactsupdated: function(contacts) {
           console.log(contacts.length + ' contacts were updated');
       },

       /* When contacts are deleted */
       oncontactsremoved: function(ids) {
           console.log(ids.length + ' contacts were deleted');
       }
   };
   ```

3. Register the listener to use the defined event handlers:

   ```
   watcherId = addressbook.addChangeListener(watcher);
   ```

   > **Note**  
   > The listener object that is the first argument of the `addChangeListener()` method must have at least 1 event handler defined. If no handlers are defined, a `TypeMismatchError` error occurs.

4. To stop the notifications, use the `removeChangeListener()` method of the `Addressbook` interface:

   ```
   addressbook.removeChangeListener(watcherId);
   ```

<a name="adding_multiple_contact"></a>
## Adding Multiple Contacts in the Batch Mode

You can create multiple contacts simultaneously using the `addBatch()` method.

To add multiple contacts to an address book in the batch mode:

1. Retrieve the default system address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications):

   ```
   addressbook = tizen.contact.getDefaultAddressBook();
   ```

2. Define the items to be added as an array:

   ```
   var c1 = new tizen.Contact({
       name: new tizen.ContactName({firstName:'Jeffrey', lastName:'Hyman'}),
       emails: [new tizen.ContactEmailAddress('user1@example.com')]
   });

   var c2 = new tizen.Contact({
       name: new tizen.ContactName({firstName:'Elton', lastName:'John'}),
       emails: [new tizen.ContactEmailAddress('user2@example.com')]
   });
   ```

3. Use the `addBatch()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications) to add the contacts in the array to the address book:

   ```
   addressbook.addBatch([c1, c2]);
   ```

   > **Note**  
   > The `addBatch()` method is asynchronous. Make sure you provide success and error callbacks with it.

## Managing Multiple Contacts in the Batch Mode

You can manage multiple contacts simultaneously using the applicable batch methods: `updateBatch()` and `removeBatch()`.

To manage multiple contacts in your address books in the batch mode:

1. Retrieve the default address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications).

   ```
   var addressbook = tizen.contact.getDefaultAddressBook();
   ```

2. Retrieve contacts stored in the address book by using the `find()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications):

   ```
   var filter = new tizen.AttributeFilter('name.firstName', 'CONTAINS', 'Chris'};
   var sortMode = new tizen.SortMode('name.lastName', 'ASC');

   try {
       addressbook.find(contactsFoundCB, null, filter, sortMode);
   }
   ```

   When searching for contacts, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#contact-filter-attributes). You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, contacts whose first name contains "Chris" are retrieved and sorted in the ascending order based on their last name.

3. To update contacts:      

   1. Define the contact changes to be made in the success event handler of the `find()` method:

      ```
      function contactsFoundCB(contacts) {
          /* Change the first names of all the found contacts */
          for (var i = 0; i < contacts.length; i++) {
              contacts[i].name.firstName = 'Christopher';
          }
      ```

   2. Use the `updateBatch()` method to update multiple contacts asynchronously:

      ```
          /* Update all found contacts */
          addressbook.updateBatch(contacts);
      }
      ```

4. To delete contacts, use the `removeBatch()` method in the success event handler of the `find()` method to delete multiple contacts asynchronously:

   ```
   function contactsFoundCB(contacts) {
       /* Delete the first 2 found contacts */
       addressbook.removeBatch([contacts[0].id, contacts[1].id]);
   }
   ```

> **Note**  
> The `updateBatch()` and `removeBatch()` methods are asynchronous. Make sure you provide success and error callbacks with them.

## Managing Contact Groups

To create engaging applications with various contact features, learn to manage contact groups:

1. Retrieve the default system address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications):

   ```
   var addressbook = tizen.contact.getDefaultAddressBook();
   ```

2. To create a `ContactGroup` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactGroup) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactGroup) applications) and add the newly create group to the system, use the constructor and the `addGroup()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications):

   ```
   var group;
   try {
       group = new tizen.ContactGroup('Company');
       addressbook.addGroup(group)
       console.log('Group added with ID ' + group.id);
   }
   ```

3. To manage groups:

   - To retrieve all the contact groups from the address book, use the `getGroups()` method   of the `AddressBook` interface:

     ```
     var groups;
     try {
         groups = addressbook.getGroups();
     }
     ```

   - To change the name of the group, assign the `name` property a new value and use the `updateGroup()`   method of the `AddressBook` interface:

     ```
     try {
         groups[0].name = 'Friends';
         addressbook.updateGroup(groups[0]);
         console.log('First group updated');
     }
     ```

   - To retrieve a specific group, use the `getGroup()` method of   the `AddressBook` interface:

     ```
     try {
         group = addressbook.getGroup(group.id);
     }
     ```

   - To remove a group from the address book, use the `removeGroup()` method of   the `AddressBook` interface:

     ```
     try {
         addressbook.removeGroup(group.id);
         console.log('Group was removed');
     }
     ```

## Managing Persons

You can manage persons, including searching, updating, and deleting, using the applicable methods of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications).

To manage persons in your contact database:

- To manage a single person:   

  When you are managing a single person at a time, the operations are handled in a synchronous mode.

  1. To retrieve persons, use the `find()` method of the `ContactManager` interface.

     You can retrieve the most frequently used persons using the sort mode as the final parameter.

     ```
     var sortMode = new tizen.SortMode('usageCount', 'ASC');
     tizen.contact.find(personsFoundCB, personsErrorCB, null, sortMode);
     ```

     When searching for persons, you can create [attribute filters](../data/data-filter.md#creating-attribute-filters), [attribute range filters](../data/data-filter.md#creating-attribute-range-filters), and [composite filters](../data/data-filter.md#creating-composite-filters) based on [specific filter attributes](../data/data-filter.md#contact-filter-attributes).  You can also [sort the search results](../data/data-filter.md#using-sorting-modes). In this example, all contacts are retrieved (since no filter is defined), and the result is sorted in the ascending order based on the most frequently used persons.

  2. Update or delete the found persons in the `personsFoundCB()` event handler. In this example, the favorite flag of the first person is changed and the contact is updated using the `update()` method. The second person is deleted using the `remove()` method.

     ```
     /* Define the event success callback */
     function personsFoundCB(persons) {
         persons[0].isFavorite = true;
         try {
             /* Update the first found person */
             tizen.contact.update(persons[0]);

             /* Delete the second found person */
             tizen.contact.remove(persons[1].id);
         }
     }
     ```

- To handle multiple persons simultaneously, use the applicable batch methods: `updateBatch()` and `removeBatch()`.

- To merge multiple persons into a single person item:    

  1. Retrieve the persons as described above.

  2. Define the persons to be merged in the `personsFoundCB()` event handler:

     ```
     function personsFoundCB(persons) {
         var sourcePerson = persons[0];
         var targetPerson = persons[1];
     ```

  3. Use the `link()` method to link contacts that are linked to the other person:

     ```
         /*
            Link 2 persons, contacts from sourcePerson are added to targetPerson
            and sourcePerson is removed
         */
         targetPerson.link(sourcePerson.id);
     }
     ```

- To get or reset the number of person's calls, messages, and emails:   

  You can get the total number of each person's calls, messages, and emails by using the `getUsageCount()` method. You can also reset the usage count of a person using the `resetUsageCount()` method of the `Person` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Person) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Person) applications), which works in a synchronous mode. To reset the usage count for multiple persons, use the `resetUsageCountBatch()` method, which works in an asynchronous mode.

  - Retrieve the total number of calls, messages, and emails of a particular person:

    ```
    /* Get a person first */
    var person = tizen.contact.get(person_id);
    /* Get the total number of calls, messages, and emails */
    var usage_count = person.getUsageCount();
    ```

  - Retrieve the number of usages of a specified type:

    ```
    /* Get a person first */
    var person = tizen.contact.get(person_id);
    /* Get number of incoming calls */
    var usage_count = person.getUsageCount('INCOMING_CALLS');
    ```

  - Reset the total number of calls, messages, and emails of a particular person:

    ```
    /* Get a person first */
    var person = tizen.contact.get(person_id);
    /* Reset all usage counts */
    person.resetUsageCount();
    ```

  - Reset the number of usages of a specified type:

    ```
    /* Get a person first */
    var person = tizen.contact.get(person_id);
    /* Reset incoming calls */
    person.resetUsageCount('INCOMING_CALLS');
    ```

  - Reset the total number of calls, messages, and emails for a few persons:

    ```
    tizen.contact.resetUsageCountBatch([person1_id, person2_id]);
    ```

  - Reset the number usages of a specified type for a few persons:

    ```
    tizen.contact.resetUsageCountBatch([person1_id, person2_id], 'INCOMING_CALLS');
    ```

## Importing Contacts

To create engaging applications with various contacts features, import contacts with the help of the vCard format:

1. Retrieve the default system address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications):

   ```
   var addressbook = tizen.contact.getDefaultAddressBook();
   ```

2. Create a new `Contact` object (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#Contact) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#Contact) applications) from the vCard string and add it to the default address book:

   ```
   var contact = null;

   try {
       contact = new tizen.Contact('BEGIN:VCARD\n' +
                                   'VERSION:3.0\n' +
                                   'N:Gump;Forrest\n' +
                                   'FN:Forrest Gump\n' +
                                   'ORG:Bubba Gump Shrimp Co.\n' +
                                   'TITLE:Shrimp Man\n' +
                                   'TEL;WORK:(111) 555-1212\n' +
                                   'TEL;HOME:(404) 555-1212\n' +
                                   'EMAIL;WORK;PREF:forrestgump@example.com\n' +
                                   'END:VCARD');

       addressbook.add(contact);
       console.log('Contact was added with ID ' + contact.id);
   }
   ```

To convert multiple strings and import them to an address book, convert the strings one by one and then use the `addBatch()` method of the `AddressBook` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#AddressBook) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#AddressBook) applications) to [add all the contacts at once in the batch mode](#adding_multiple_contact).

## Exporting Contacts

To create engaging applications with various contacts features, export contacts with the help of the vCard format:

1. Retrieve the default system address book using the `getDefaultAddressBook()` method of the `ContactManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/contact.html#ContactManager) and [wearable](../../api/latest/device_api/wearable/tizen/contact.html#ContactManager) applications) and find all contacts with "Chris" in the first name:

   ```
   var addressbook;

   var addressbook = tizen.contact.getDefaultAddressBook();

   /* Define a filter */
   var filter = new tizen.AttributeFilter('name.firstName', 'CONTAINS', 'Chris');

   /* Search for the contacts */
   addressbook.find(contactsFoundCB, errorCB, filter);
   ```

2. Convert a contact to a vCard string in the success event handler of the `find()` method.

   In the following example, the first found contact is exported by converting it to the vCard version 3.0 format.

   ```
   function contactsFoundCB(contacts) {
       /* Convert the first contact */
       var vcard = contacts[0].convertToString('VCARD_30');
   }
   ```

## Related Information
* Dependencies   
  - Tizen 2.4 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
