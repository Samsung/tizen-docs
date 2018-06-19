# Data Bundle


A bundle is a string-based dictionary abstract data type (ADT). A dictionary is an ordered or unordered list of key-value pairs, where keys are used to locate elements in the list. The key is always a string.

The main features of the Bundle API include:

- Adding content to a bundle

  You can [add byte, string, or string array type content](#add) to a valid bundle.

- Managing the bundle content

  You can [delete and get values of the bundle content](#manage).

- Iterating a bundle

  You can [iterate through the bundle content](#iterate) to access individual content items.

- Encoding and decoding a bundle

  You can [encode and decode a bundle](#encode) to store it or send it over a serial connection.

## Prerequisites

To enable your application to use the bundle functionality:

1. To use the functions and data types of the Bundle API (in [mobile](../../api/mobile/latest/group__CORE__LIB__BUNDLE__MODULE.html) and [wearable](../../api/wearable/latest/group__CORE__LIB__BUNDLE__MODULE.html) applications), include the `<bundle.h>` header file in your application:

   ```
   #include <bundle.h>
   ```

2. Before you can perform any operations on a bundle, create the bundle instance. Each bundle is independent from other bundles and stores its own set of records.

   ```
   bundle* bund = NULL;

   bund = bundle_create();
   ```

3. When no longer needed, release the bundle by calling the `bundle_free()` function:

   ```
   bundle_free(bund);
   ```

<a name="add"></a>
## Adding Content to a Bundle

The bundle content is in the form of key-value pairs. The key is always a string. The value can be of the following types:

**Table: Bundle value types**

| Value constant          | Value type       |
|-------------------------|------------------|
| `BUNDLE_TYPE_STR`       | String (default) |
| `BUNDLE_TYPE_STR_ARRAY` | String array     |
| `BUNDLE_TYPE_BYTE`      | Byte             |

To add content to a bundle, use a function associated with the type of the value you want to add:

- `bundle_add_str_array()`
- `bundle_add_str()`
- `bundle_add_byte()`

```
const char* array [3] = {"Var1", "Var2", "Var3"};
int array_len = 3;

bundle_add_str(bund, "Str", "String content");

bundle_add_str_array(bund, "Array", array, array_len);

bundle_add_byte(bund, "Byte", "Byte content", 12);
```

When operating on bytes, remember to control the length of the given chain.

<a name="manage"></a>
## Managing the Bundle Content

To manage the bundle content:

1. Get values from the bundle using the function associated with the type of the value you want to get:

   - `bundle_get_str()`
   - `bundle_get_str_array()`
   - `bundle_get_byte()`

   You can also get the number of bundle items with the `bundle_get_count()` function, and the type of a value with a specific key with the `bundle_get_type()` function.

   ```
   void
   test_bundle_add_del_get(void)
   {
       bundle *b = NULL;
       int count = 0;
       char *value;

       b = bundle_create();

       bundle_add_str(b, "key1", "val1");
       bundle_add_str(b, "key2", "val2");
       bundle_get_str(b, "key2", &value);
       dlog_print(DLOG_DEBUG, LOG_TAG, "the value of key2: %s", value);

       count = bundle_get_count(b);
       dlog_print(DLOG_DEBUG, LOG_TAG, "the number of bundle items: %d", count);
   ```

2. Delete a key-value pair from the bundle content using the `bundle_del()` function:
   ```
   	   bundle_del(b, "key2");
   	   bundle_free(b);
   }
   ```

<a name="iterate"></a>
## Iterating a Bundle

To iterate through the bundle records, use the `bundle_foreach()` function, which requires a callback function to operate. The callback function must first determine the key-value pairs and then perform the specified operations.

After the `bundle_foreach()` function call, the callback function is invoked for each record in the bundle:

```
void
iterate_bundle_foreach(const char *key, const int type, bundle_keyval_t *kv, void *user_data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "key: %s, type: %d ", key, type);

    void *ptr = NULL;
    char *buff = NULL;
    unsigned int size = 0;
    if (type == BUNDLE_TYPE_STR) {
        bundle_keyval_get_basic_val((bundle_keyval_t *)kv, &ptr, &size);
        buff = malloc(sizeof(char)* size + 1);
        snprintf(buff, size + 1, "%s", ((char*)ptr));
        dlog_print(DLOG_DEBUG, LOG_TAG, "Found STR -KEY: %s, VAL: %s, SIZE: %d", key, buff, size);
        free(buff);
    } else if (type == BUNDLE_TYPE_BYTE) {
        bundle_keyval_get_basic_val((bundle_keyval_t *)kv, &ptr, &size);
        buff = malloc(sizeof(char)* size + 1);
        snprintf(buff, size + 1, "%s", ((char*)ptr));
        dlog_print(DLOG_DEBUG, LOG_TAG, "Found STR -KEY: %s, VAL: %s, SIZE: %d", key, buff, size);
        free(buff);
    } else if (type == BUNDLE_TYPE_STR_ARRAY) {
        void ** array;
        unsigned int len = 0;
        size_t *element_size = NULL;
        dlog_print(DLOG_DEBUG, LOG_TAG, "Found STR_ARRAY -KEY: %s", key);
        bundle_keyval_get_array_val((bundle_keyval_t *)kv, &array, &len, &element_size);
        dlog_print(DLOG_DEBUG, LOG_TAG, "-Array len: %d", len);
        for (int i = 0; i < len; i++)
            dlog_print(DLOG_DEBUG, LOG_TAG, "-%s", (char*)array[i]);
    }
}

void
test_bundle_foreach(void)
{
    const char *s_arr[] = {"abc", "bcd", "cde"};
    bundle *b;
    b = bundle_create();

    bundle_add_str(b, "k1", "v1");
    bundle_add_byte(b, "k2", "v2", 3);
    bundle_add_str_array(b, "k3", s_arr, 3);

    bundle_foreach(b, iterate_bundle_foreach, NULL);
    bundle_free(b);
}
```

<a name="encode"></a>
## Encoding and Decoding a Bundle

To store or send a bundle over a serial connection, encode it to `bundle_raw` (a typedef of `unsigned char`) with the `bundle_encode()` function, and write the `bundle_raw` instance to a file, for example.

To open the encoded bundle, use the `bundle_decode()` function. When you no longer need them, release the encoded data and the created bundle.

```
void
test_bundle_encode_decode(void)
{
    bundle *b1;
    bundle *b1;
    bundle_raw *r;
    int size_r;
    char *value;

    b1 = bundle_create();
    bundle_add_str(b1, "k1", "v1");
    bundle_add_str(b1, "k2", "v2");

    bundle_encode(b1, &r, &size_r);

    b2 = bundle_decode(r, size_r);

    bundle_get_str(b1, "k1", &value);
    dlog_print(DLOG_DEBUG, LOG_TAG, "value of k1 after decode: %s", value);

    bundle_free(b1);
    bundle_free(b2);
}
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
