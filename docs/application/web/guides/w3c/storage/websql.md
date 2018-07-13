# Web SQL Database

The Web SQL database provides a way to store databases that can be queried using various SQL statements. Each Tizen application can store multiple databases and each one of them can store multiple tables. Databases can be accessed using the SQL language, which is a common standard for these kinds of applications.

This feature is supported in mobile applications only.

When working with the SQL database, you can use the following approaches:

- Asynchronous database API

  A script is not blocked during calls of statements described in the API. Succession of operations is provided by event handlers. This approach does not block user interface during long operations and can be used anywhere in your application.

- Synchronous database API

  To start an operation, you must wait for the previous one to be completed. This approach can be used only with [Web Workers](../perf-opt/web-workers.md).

The main Web SQL database features include:

- SQL database creation

  You can create and open a SQL database [asynchronously](#opening-a-database-asynchronously) or [synchronously](#opening-a-database-synchronously).

- SQL statement execution

  You can execute SQL statements [asynchronously](#executing-sql-statements-asynchronously) or [synchronously](#executing-sql-statements-synchronously).

- SQL statement result access

  You can access the result object [asynchronously](#accessing-sql-results-asynchronously) or [synchronously](#accessing-sql-results-synchronously).

- Error management

  You can handle errors [asynchronously](#handling-a-syntax-error-asynchronously) or [synchronously](#handling-a-syntax-error-synchronously).

  For the properties that can be delivered with the `sqlError` object, see [Errors and exceptions](http://www.w3.org/TR/2010/NOTE-webdatabase-20101118/?cp=3_0_6_0_5_6#errors-and-exceptions).

> **Note**  
> The Web SQL Database API is still in group note state, but Tizen supports it as it is already widely used in the industry.

## Opening a Database Asynchronously

To open a database asynchronously, use the `openDatabase()` method. If the database does not exist, the method first creates it and then opens it:

```
var db;
var version = 1.0;
var dbName = 'tizendb';
var dbDisplayName = 'tizen_test_db';
var dbSize = 2 * 1024 * 1024;
try {
    db = openDatabase(dbName, version, dbDisplayName, dbSize, function(database) {
        alert('database creation callback');
    });
}
```

The method takes the following arguments: unique name of the database, expected version of the database to be opened (if an empty string is given any version can be loaded), display name, the estimated size of database (number of bytes), and, optionally, the database creation event handler.

> **Note**  
> The creation event handler is invoked only once if the database does not exist. There is no event handler for the database `opened` event.

### Source Code

For the complete source code related to this use case, see the following file:

- [websqldatabase_example.html](http://download.tizen.org/misc/examples/w3c_html5/storage/web_sql_database)

## Executing SQL Statements Asynchronously

To execute SQL statements asynchronously:

1. In the Web SQL Database API, each SQL statement must be executed under a transaction. To create a transaction, use either `transaction()` or  `readTransaction()` method returned by the `openDatabase()` method:

   ```
   db.transaction(function(t) {
       /* Place SQL statements here */
   }, function() {
       alert('SQL statements were executed successfully.');
   });
   ```

   The difference between the `transaction()` and `readTransaction()` methods is that the latter cannot be used with SQL statements that change the database (such as `INSERT`, `UPDATE`, `DELETE`, or `CREATE`).

   > **Note**  
   > When possible, use the `readTransaction()` to obtain better execution performance of SQL statements.

2. To execute a SQL statement, use the `executeSql()` method. The SQL statement is the first parameter of the method and cannot contain SQL transaction statements (such as `BEGIN`, `END`, or `ROLLBACK`):

   ```
   t.executeSql('CREATE TABLE tizenTable (id INTEGER PRIMARY KEY, title TEXT, content TEXT, insertDay DATETIME)',
                [], function(sqlTransaction, sqlResultSet) {
       alert('Table has been created.');
   }, function(sqlTransaction, sqlError) {
       /* Error handling */
   });
   ```

3. Pass arguments to the SQL statement:

   ```
   sqlTransaction.executeSql('SELECT * FROM tizenTable WHERE id=?', [value]);
   ```

   > **Note**  
   > Use an array to pass the arguments to secure SQL statements from SQL injection attacks.

### Source Code

For the complete source code related to this use case, see the following file:

- [websqldatabase_example.html](http://download.tizen.org/misc/examples/w3c_html5/storage/web_sql_database)

## Accessing SQL Results Asynchronously

When a SQL statement is executed, its event handler is invoked and returns the result as a `sqlResultSet` object.

To access the result:

- The result object of the INSERT statement contains the insert ID, which stores the identifier of the added record. If multiple records were inserted, the insert ID contains the ID of the last inserted record:

  ```
  sqlTransaction.executeSql('INSERT INTO tizenTable(title, content, insertDay) VALUES (?, ?, ?)',
                            [title, context, day], function(sqlTransaction, sqlResultSet) {
      alert('The 'id' of the new record  is ' + sqlResultSet.insertId);
  });
  ```

- The result object of the SELECT statement stores also the number of records that were inserted, changed, or deleted. It contains the number of selected rows (length field) and the `item()` method. Use the method with the index argument (integer value from 0 to `rows.length` - 1) to get individual records:

  ```
  sqlTransaction.executeSql('SELECT id, title, author FROM books', [], function(sqlTransaction, sqlResultSet) {
      var book, i, booksNumber = sqllResultSet.rows.length;
      for (i = 0; i < booksNumber; i++) {
          book = sqlResultSet.rows.item(i);
          alert('id: ' + book.id + ', title: ' + book.title +
                ', author: ' + book.author);
      }
  });
  ```

### Source Code

For the complete source code related to this use case, see the following file:

- [websqldatabase_example.html](http://download.tizen.org/misc/examples/w3c_html5/storage/web_sql_database)

## Handling a Syntax Error Asynchronously

To handle a syntax error asynchronously, use a `sqlError` object:

```
sqlTransaction.executeSql('SELECT * FROM notExistingTable', [], function(sqlTransaction, sqlResultSet) {},
                          function(sqlTransaction, sqlError) {
    switch (sqlError.code) {
        case sqlError.SYNTAX_ERR:
            alert('Syntax error has occurred. ' + sqlError.message);
            break;
        default:
             alert('Other error');
    }
});
```

Other types of errors that can occur are exceptions. The `sqlException` object has the same fields as the `sqlError` object but it must be handled in the `try - catch` block.

## Opening a Database Synchronously

To open a SQL database synchronously, use the `openDatabaseSync()` method. The method can only be used in the [Web Worker](../perf-opt/web-workers.md#js_performance) context. If the database does not exist, the method first creates it and then opens it:

```
var databaseSync = null;
try {
    databaseSync = openDatabaseSync('dbName', '1.0', 'display database name', 1024 * 1024, function(databaseSync) {
        alert('database creation callback');
    });
}
```

The method takes the following arguments: unique name of the database, expected version of the database to be opened (if an empty string is given any version can be loaded), display name, the estimated size of database (number of bytes), and, optionally, the database creation event handler.

> **Note**  
> The creation event handler is invoked only once if the database does not exist. There is no event handle for the database opened event but, in the synchronous database API, no other code is run until the database creation operation is completed.

## Executing SQL Statements Synchronously

To execute SQL statements synchronously:

1. In the Web SQL Database API, each SQL statement must be executed under a transaction. To create a transaction, use either `transaction()` or  `readTransaction()` method returned by the `openDatabaseSync()` method:

   ```
   database.transaction(function(sqlTransactionSync) {
       /* Place SQL statements here */
   }, function() {
       alert('SQL statements were executed successfully.');
   });
   ```

   The difference between the `transaction()` and `readTransaction()` methods is that the latter cannot be used with SQL statements that change the database (such as `INSERT`, `UPDATE`, `DELETE`, or `CREATE`).

   > **Note**  
   > When possible, use the `readTransaction()` to obtain better execution performance of SQL statements.

2. To execute a SQL statement, use the `executeSql()` method. The SQL statement is the first parameter of the method and cannot contain SQL transaction statements (such as `BEGIN`, `END`, or `ROLLBACK`):

   ```
   var sqlResultSet = sqlTransactionSync.executeSql('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,
                                                    title TEXT, author TEXT)', []);
   ```

3. Pass arguments to the SQL statement:

   ```
   var sqlResultSet = sqlTransactionSync.executeSql('SELECT id FROM books WHERE title=? AND author=?',
                                                    ['Ulysses', 'James Joyce']);
   ```

   > **Note**  
   > Use an array to pass the arguments to secure SQL statements from SQL injection attacks.

## Accessing SQL Results Synchronously

When a SQL statement is executed, its event handler is invoked and returns the result as a `sqlResultSet` object.

To access the result:

- The result object of the INSERT statement contains the insert ID, which stores the identifier of the added record. If multiple records were inserted, the insert ID contains the ID of the last inserted record:

  ```
  var sqlResultSet = sqlTransactionSync.executeSql('INSERT INTO books (id, title, author) VALUES(NULL, ?, ?)',
                                                   ['Ulysses', 'James Joyce']);
  alert('The 'id' of the new record is ' + sqlResultSet.insertId);
  ```

- The result object of the SELECT statement stores also the number of records that were inserted, changed, or deleted. It contains the number of selected rows (length field) and the `item()` method. Use the method with the index argument (integer value from 0 to `rows.length` - 1) to get individual records:

  ```
  var sqlResultSet = sqlTransactionSync.executeSql('SELECT id, title, author FROM books');
  var book, i, booksNumber = sqlResultSet.rows.length;
  for (i = 0; i < booksNumber; i++) {
      book = sqlResultSet.rows.item(i);
      alert('id: ' + book.id + ', title: ' + book.title + ', author: ' + book.author);
  }
  ```

## Handling a Syntax Error Synchronously

To handle a syntax error synchronously, use a `sqlException` object:

```
try {
    databaseSync.transaction(function(sqlTransactionSync) {
        var sqlResultSet = sqlTransactionSync.executeSql('DELETE FROM books WHERE id=?', [id]);
    });
    /* Instructions if the above SQL statement is executed successfully */
} catch (sqlException) {
    postMessage('An error has occurred during deleting the book from the table!
                 Error code: ' + sqlException.code + ' (' + sqlException.message + ').');
}
```

> **Note**  
> In the synchronous database API, the script execution is stopped until the transaction is completed.

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
