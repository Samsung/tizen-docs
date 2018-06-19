# SQLite Database Engine


You can use open-source modules to access SQLite and OpenSSL, and use them to encrypt and store application data. The open source modules supported by Tizen are listed within the [API modules](../../tutorials/details/tizen-apis.md).

The main features of the Sqlite API include:

- Preparing the database

  You can [prepare the database](#prepare) for encrypted data.

- Encrypting and decrypting data

  You can [encrypt messages and store them in the database](#prepare) with the Base64 encoding. You can also decrypt stored messages.

<a name="prepare"></a>
## Preparing the Database

This guide only covers the basics of encryption and database usage. For more information, see the [OpenSSL](http://www.openssl.org) and [SQLite](http://www.sqlite.org) Web pages.

> **Note**
>
> While operating with real data, make sure that you fulfill all security requirements. This guide demonstrates how to use the library APIs on Tizen, but does not show how to perform fully secure encryption.

To prepare the database:

1. Define the needed variables:

   ```
   #define BUFLEN 300 /* Buffer size, used in functions */
   const int key_len = 256; /* AES key length */

   /* Password to generate key */
   static const unsigned char password[] = {"DummyPassword"};

   sqlite3 *db; /* Database handle */

   unsigned char salt[9]; /* Encryption salt */
   unsigned char iv[17]; /* Encryption initial vector */
   ```

2. To operate on a SQL database provided by SQLite:

   1. Configure the database interface to set the path to the database using URI:

      ```
      sqlite3_shutdown();
      sqlite3_config(SQLITE_CONFIG_URI, 1);
      ```

   2. Initialize the interface with the `sqlite3_initialize()` function:

      ```
      sqlite3_initialize();
      ```

   3. Open the database using the `sqlite3_open()` function.

      The function creates a new database file, if the URI in the first parameter points to a non-existing one. The handle to the database is stored in the second parameter.

      ```
      char file_path[BUFLEN];
      char *document_path;
      /*
         Fill the variable with the value obtained
         using storage_foreach_device_supported()
      */
      int internal_storage_id = 0;
      storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_DOCUMENTS, &document_path);
      snprintf(file_path, size, "%s/test.db", document_path);
      free(document_path);

      sqlite3_open(file_path, &db);

      free(file_path);
      ```

   4. Create a table:

      ```
      CreateTable();
      ```

      The `CreateTable()` function prepares a SQL query, and uses the `sqlite3_exec()` function to execute the query in the defined database.

      The `sqlite3_exec()` function passes a return message to a callback function as an array of strings. It creates a database only if one does not exist already. In the following example, the created database name is `EncryptedData`, and it contains the DATA, ENCRYPTED, SALT, IV, PART, and KEY fields.

      ```
      static int
      CreateTable()
      {
          int ret;
          char *ErrMsg;
          char *sql = "CREATE TABLE IF NOT EXISTS EncryptedData("  \
                                                                "DATA TEXT NOT NULL," \
                                                                "ENCRYPTED INT NOT NULL,"\
                                                                "SALT TEXT NOT NULL," \
                                                                "IV TEXT NOT NULL," \
                                                                "PART INTEGER," \
                                                                "KEY INTEGER PRIMARY KEY);";

          sqlite3_exec(db, sql, callback, 0, &ErrMsg);

          return 0;
      }
      ```

3. To operate with OpenSSL AES, salt and initial vectors are needed. Those are auxiliary variables which are used to generate a cryptographic key:

   - `RAND_bytes()` generates a random chain of bytes.
   - An additional character is appended after the last character of a chain to point the end of the salt[8]=0x00 variable.
   - `PrepareToSQL()` removes some of the SQL special characters from the chain to make it possible to insert it to the database.

   ```
   RAND_bytes(salt, 8);
   RAND_bytes(iv, 16);

   salt[8]=0x00;
   iv[16]=0x00;

   PrepareToSQL(salt);
   PrepareToSQL(iv);
   ```

   In the following example, only the string delimiting characters are removed. In a real implementation, you must replace other characters too, such as the comment sequence.

   ```
   void
   PrepareToSQL(unsigned char* msg)
   {
       int i = 0;
       while (msg[i] != 0x00) {
           if (msg[i] == '\'')
               msg[i] = 'a';
           if (msg[i] == '\"')
               msg[i] = 'b';
           ++i;
       }
   }
   ```

4. Include the required headers:

   - `#include <string.h>`
   - `#include <time.h>`
   - `#include <stdint.h>`
   - `#include <stdlib.h>`
   - `#include <sqlite3.h>`
   - `#include <openssl/aes.h>`
   - `#include <openssl/crypto.h>`
   - `#include <openssl/rand.h>`
   - `#include <openssl/evp.h>`

   The `time.h` is obtained to create an example message to encrypt and store.

## Storing Encrypted Data

This use case shows how to:

1. Encrypt a message with OpenSSL, prepare it, and store it in the SQLite database with Base64 encoding.
2. Check that the message has been successfully stored by listing the database content.
3. Retrieve the database content and decrypt the message.

To store encrypted data:

1. Store a short message.

   ```
   char *ShortMsg = "Short Msg.";
   EncryptMsg(ShortMsg, decrypted_out, password, salt, iv);
   InsertRecord(decrypted_out, 1, 0, strlen(ShortMsg));
   ```

   The OpenSSL `AES_encrypt()` function allows encrypting up to 16 characters at once. Adding a short message (at most 16 characters long) requires the following steps:

   1. Encrypt plain text with the `EncryptMsg()` function:
   	  - Generate a string for key generation from a password and salt using `PKCS5_PBKDF2_HMAC_SHA1()`.

        An initial vector can be used in different hash functions. In this example, only the first byte of the initial vector is used as an iteration variable for a hash algorithm.

   	  - Generate the encryption key using the `AES_set_encrypt_key()` function.

        The second parameter defines the AES key length. Check the actual recommended length and encoding type before use. This example uses AES 256 (defined in [Preparing the Database](#prepare)).

      - Encrypt the data with the `AES_encrypt()` function.

      - Encode Base64 with the `base64_encode()` function.

        The data is encoded to make it safe to insert it to the database. Base 64 does not contain any special characters. For the encoding and decoding function details, see [Base64 functions](#base64).

      - Add a delimiting 0x00 character at the end of the byte array.

       ```
       static int
       EncryptMsg(char* in, unsigned char* out, const unsigned char* password, unsigned char *localsalt, unsigned char *vector)
       {
           AES_KEY encryption_key;
           int iter = (int)vector[0];
           unsigned char key[key_len + 1];
           char *msgbuff;
           unsigned char buf[BUFLEN];
           unsigned int retlen;
           int x;

           memset(buf, 0x00, BUFLEN);

           PKCS5_PBKDF2_HMAC_SHA1((char *)password,
                                  sizeof(password)/sizeof(unsigned char),
                                  localsalt,
                                  sizeof(localsalt)/sizeof(unsigned char),
                                  iter,
                                  key_len,
                                  key);

           AES_set_encrypt_key(key, key_len, &encryption_key);
           AES_encrypt((unsigned char *)in, (unsigned char *)buf, &encryption_key);

           msgbuff = base64_encode(buf, 16, &retlen);

           memcpy(buf, msgbuff, retlen);
           buf[retlen + 1] = 0x00;
           free(msgbuff);

           memcpy(out, buf, retlen + 1);

           for (x = 0; buf[x] != 0x00; x++);

           return x;
       }
       ```

   2. Execute the database insertion with the `InsertRecord()` function.

      To insert data to the database, use the `sqlite3_exec()` function. A query is prepared with common C functions. The encrypted variable is stored in the database and indicates whether the DATA field in the database is encrypted.

      ```
      static int
      InsertRecord(unsigned char *msg, int encrypted,
                   int part, int len)
      {
          char sqlbuff[BUFLEN];
          char *ErrMsg;
          snprintf(sqlbuff, BUFLEN, "INSERT INTO EncryptedData
                   VALUES(\'%s\', %d, \'%s\', \'%s\', %d, NULL);",
                   msg, encrypted, salt, iv, part);

          ret = sqlite3_exec(db, sqlbuff, callback, 0, &ErrMsg);
          if (ret) {
              dlog_print(DLOG_DEBUG, LOG_TAG, "Error: %s\n", ErrMsg);
              sqlite3_free(ErrMsg);
          }

          return 0;
      }
      ```

      To store longer messages (more than 16 characters), split them into shorter parts. In the following example, the message is divided into blocks 16 characters long. Each block is tagged by its own number with a `parts` variable, and the tag is stored in the database in the `PART` field. Each block is then stored in its own record to simplify the decoding procedure.

      ```
      ret = InsertMessage((unsigned char *)text);

      static int
      InsertMessage(unsigned char* text)
      {
          unsigned char encrypted_out[BUFLEN];
          int ret = 0;
          int x;
          int len;
          int retlen;
          int parts = 0;
          int pos;
          char membuf[17];

          for (len = 0; text[len] != 0x00; len++);

          for (pos = 0; (len - pos) > 16; pos += 16) {
              memcpy(membuf, &text[pos], 16);
              membuf[16] = 0x00;

              EncryptMsg((char *)membuf, encrypted_out, password, salt, iv);

              for (x = 0; encrypted_out[x] != 0x00; x++);

              InsertRecord(encrypted_out, 1, parts, x);

              parts++;
          }

          if (len - pos > 0) {
              retlen = EncryptMsg((char *)&text[pos],
                                  encrypted_out, password, salt, iv);
              InsertRecord(encrypted_out, 1, parts, retlen);
          }

          return 0;
      }
      ```

2. List the database content.

   After the previous step, the database contains AES-encrypted content, stored in a Base64 notation. For example:

   ```
   0: DATA = xPRnJYwvQTc4VJKkW4EroQ==
   1: DATA = EZI+uOGxcnUseJnbH57/Bg==
   ```

   To list the records in the database, use the `ShowRecords()` function:

   - To list all records, use the `SELECT * FROM EncryptedData` query.

     The callback function is invoked for each record returned by SQLite. To pass user data to the callback, use the fourth parameter of the `sqlite3_exec()` function.

   - The callback simply prints the obtained record.

     The record is passed in the form of a few arrays of strings: the `argv` array contains the column content and `azColName` the column name. The `argc` parameter is the number of columns.

     The first parameter, `counter`, is the user data, which in this example is used to indicate the record number in a row (not a SQL primary key) while listing.

     If the content of any column is empty, the `NULL` string is printed.

   ```
   static void
   ShowRecords()
   {
       char *sql = "select * from EncryptedData";
       int counter = 0;
       int ret = 0;
       char *ErrMsg;

       sqlite3_exec(db, sql, callback, &counter, &ErrMsg);

       return;
   }

   static int
   callback(void *counter, int argc, char **argv, char **azColName)
   {
       int *localcounter = (int *)counter;
       int i;

       dlog_print(DLOG_DEBUG, LOG_TAG, "-%d: ", *localcounter);

       for (i = 0; i < argc; i++)
           dlog_print(DLOG_DEBUG, LOG_TAG, "%s = %s | ", azColName[i], argv[i] ? argv[i] : "NULL");

       (*localcounter)++;
       dlog_print(DLOG_DEBUG, LOG_TAG, "\n");

       return 0;
   }
   ```

3. Decrypt the database records.

   Use the `DecryptRecords()` function to select all encrypted records from the database, and decrypt and list them:

   - Use the `SELECT * FROM EncryptedData` query where `ENCRYPTED='1'` query to retrieve all encrypted records.

   - The `callbackdecrypt()` callback is invoked for each found record. If there is an error, the Sqlite API requires you to release the error message memory with the `sqlite3_free()` function.

   - The callback is similar to the earlier callback used to list the database content.

     There is an action added for the `argv[ i ] && i == 0` case, which includes the encrypted content in columns that are not empty and are DATA.

     To decrypt the message, decode the data from Base 64, add a delimiting character, perform the actual decryption with the `DecryptMsg()` function, and list the decrypted data.

   ```
   static void
   DecryptRecords()
   {
       char *sql = "select * from EncryptedData where ENCRYPTED='1'";
       int counter = 0;
       int ret = 0;
       char *ErrMsg;

       ret = sqlite3_exec(db, sql, callbackdecrypt, &counter, &ErrMsg);
       if (ret) {
           dlog_print(DLOG_DEBUG, LOG_TAG, "Error: %s\n", ErrMsg);
           sqlite3_free(ErrMsg);
       }
   }

   static int
   callbackdecrypt(void *counter, int argc, char **argv, char **azColName)
   {
       unsigned char decrypted_out[BUFLEN];
       int *localcounter = (int *)counter;
       int i;
       unsigned int olen;

       dlog_print(DLOG_DEBUG, LOG_TAG, "-%d: ", *localcounter);

       for (i = 0; i < argc; i++) {
           if (argv[i] && i == 0) {
               unsigned char *basebuffer = base64_decode(argv[i], strlen(argv[i]), &olen);
               unsigned char *decryptbuffer = malloc(sizeof(char)* olen + 1);

               memset(decryptbuffer, 0x00, olen + 1);
               memcpy(decryptbuffer, basebuffer, olen);
               decryptbuffer[olen] = 0x00;
               free(basebuffer);

               DecryptMsg((unsigned char *)decryptbuffer, decrypted_out,
                          password, (unsigned char *)argv[2], (unsigned char *)argv[3]);

               free(decryptbuffer);

               dlog_print(DLOG_DEBUG, LOG_TAG, "%s = %s | ", azColName[i],
                          (char*)decrypted_out);

           } else {
               dlog_print(DLOG_DEBUG, LOG_TAG, "%s = %s | ", azColName[i], argv[i] ? argv[i] : "NULL");
           }
       }

       (*localcounter)++;
       dlog_print(DLOG_DEBUG, LOG_TAG, "\n");

       return 0;
   }
   ```

   The actual decryption routine is similar to encryption:

   ```
   static int
   DecryptMsg(unsigned char* in, unsigned char* out, const unsigned char* password,
              unsigned char* localsalt, unsigned char* vector)
   {
       AES_KEY decryption_key;
       int iter = (int)vector[0];
       unsigned char key[key_len + 1];
       int x;

       memset(out, 0x00, BUFLEN);

       PKCS5_PBKDF2_HMAC_SHA1((char *)password,
                              sizeof(password)/sizeof(unsigned char),
                              localsalt,
                              sizeof(localsalt)/sizeof(unsigned char),
                              iter,
                              key_len,
                              key);

       AES_set_decrypt_key(key, key_len, &decryption_key);
       AES_decrypt((unsigned char *)in, out, &decryption_key);

       for (x = 0; out[x] != 0x00; x++);

       return x;
   }
   ```

4. When no longer needed, close the SQLite library properly:

   ```
   base64_cleanup();
   sqlite3_close(db);
   sqlite3_shutdown();
   ```

<a name="base64"></a>The following code snippets illustrate the functions related to the Base64 encoding and decoding operations, and the main function that performs the entire process of encrypting, storing, listing, and decrypting:

- Base64 functions:

  ```
  static char
  encoding_table[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                      'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                      'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                      'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                      'w', 'x', 'y', 'z', '0', '1', '2', '3',
                      '4', '5', '6', '7', '8', '9', '+', '/'};
  static char *decoding_table = NULL;
  static int mod_table[] = {0, 2, 1};

  void
  build_decoding_table()
  {
      decoding_table = malloc(256);
      int i;
      for (i = 0; i < 64; i++)
          decoding_table[(unsigned char)encoding_table[i]] = i;
  }

  char
  *base64_encode(const unsigned char *data, size_t input_length, size_t *output_length)
  {
      *output_length = 4 * ((input_length + 2) / 3);

      char *encoded_data = malloc(*output_length);
      if (encoded_data == NULL)
          return NULL;

      int i;
      int j;
      for (i = 0, j = 0; i < input_length;) {
          uint32_t octet_a = i < input_length ? (unsigned char)data[i++] : 0;
          uint32_t octet_b = i < input_length ? (unsigned char)data[i++] : 0;
          uint32_t octet_c = i < input_length ? (unsigned char)data[i++] : 0;
          uint32_t triple = (octet_a << 0x10) + (octet_b << 0x08) + octet_c;

          encoded_data[j++] = encoding_table[(triple >> 3 * 6) & 0x3F];
          encoded_data[j++] = encoding_table[(triple >> 2 * 6) & 0x3F];
          encoded_data[j++] = encoding_table[(triple >> 1 * 6) & 0x3F];
          encoded_data[j++] = encoding_table[(triple >> 0 * 6) & 0x3F];
      }

      for (i = 0; i < mod_table[input_length % 3]; i++)
          encoded_data[*output_length - 1 - i] = '=';

      return encoded_data;
  }

  unsigned char
  *base64_decode(const char *data, size_t input_length, size_t *output_length)
  {
      if (decoding_table == NULL)
          build_decoding_table();

      if (input_length % 4 != 0)
          return NULL;

      *output_length = input_length / 4 * 3;
      if (data[input_length - 1] == '=')
          (*output_length)--;
      if (data[input_length - 2] == '=')
          (*output_length)--;

      unsigned char *decoded_data = malloc(*output_length);
      if (decoded_data == NULL)
          return NULL;

      int i;
      int j;

      for (i = 0, j = 0; i < input_length;) {
          uint32_t sextet_a = data[i] == '=' ? 0 & i++ : decoding_table[(int)data[i++]];
          uint32_t sextet_b = data[i] == '=' ? 0 & i++ : decoding_table[(int)data[i++]];
          uint32_t sextet_c = data[i] == '=' ? 0 & i++ : decoding_table[(int)data[i++]];
          uint32_t sextet_d = data[i] == '=' ? 0 & i++ : decoding_table[(int)data[i++]];

          uint32_t triple = (sextet_a << 3 * 6) + (sextet_b << 2 * 6)
                            + (sextet_c << 1 * 6) + (sextet_d << 0 * 6);

          if (j < *output_length)
              decoded_data[j++] = (triple >> 2 * 8) & 0xFF;
          if (j < *output_length)
              decoded_data[j++] = (triple >> 1 * 8) & 0xFF;
          if (j < *output_length)
              decoded_data[j++] = (triple >> 0 * 8) & 0xFF;
      }

      return decoded_data;
  }

  void
  base64_cleanup()
  {
      free(decoding_table);
      decoding_table = NULL;
  }
  ```

- Main function:

  ```
  int
  OpenSQL_AES_example_1(void)
  {
      unsigned char decrypted_out[BUFLEN];
      int ret;
      char *hellomsg = {"Hello Tizen! SQLite OpenSSL"};
      char text[BUFLEN];
      time_t rawtime;
      struct tm *timeinfo;

      if (init_err) {
          dlog_print(DLOG_DEBUG, LOG_TAG, "Initial error\n");

          return 1;
      }

      time(&rawtime);
      timeinfo = localtime(&rawtime);
      sprintf(text, "%s %s", hellomsg, asctime(timeinfo));

      /* Insert long message */
      ret = InsertMessage((unsigned char *)text);
      if (ret) {
          dlog_print(DLOG_DEBUG, LOG_TAG, "Insert ENCRYPTED MessageError\n");

          return 1;
      }

      /* Insert message up to 16 characters */
      char *ShortMsg = "Short Msg.";
      EncryptMsg(ShortMsg, decrypted_out, password, salt, iv);
      ret = InsertRecord(decrypted_out, 1, 0, strlen(ShortMsg));
      if (ret) {
          dlog_print(DLOG_DEBUG, LOG_TAG, "Insert ENCRYPTED MessageError\n");

          return 1;
      }

      /* Show raw database */
      ShowRecords();

      /* Show decrypted database */
      DecryptRecords();

      return 0;
  }
  ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
