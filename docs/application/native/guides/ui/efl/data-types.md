# Data Types

The Eina library is a central part of the EFL. It implements an API for data types, and allows you to create and manipulate several data types:

- [Inline Array](#creating-and-destroying-an-inline-array): Standard array of inlined members
- [Array](#arrays): Standard array of `void*` data
- [Hash Table](#hash-tables): Standard hash of `void*` data
- [Inline List](#using-an-inline-list): List with nodes inlined into the user type
- Compact List
- [List](#lists): Standard list of `void*` data
- [Iterator Functions](#iterator-functions)
- Sparse Matrix: Sparse matrix of `void*` data
- Red-Black tree: Red-black tree with nodes inlined into the user type
- [String Buffer](#string-buffer): Mutable string to prepend, insert, or append strings to a buffer
- [Stringshare](#stringshare): Shares read-only string references
- Tiler split: Merges and navigates into 2D tiled regions
- Trash: Container of unused but allocated data
- [Generic Value Storage](#generic-value): Container for generic value storage and access
- Data Model API: Container for data with a user-defined hierarchy or structure

## Iterator Functions

Eina provides a set of iterator functions to manipulate data types, such as arrays.

These functions allow access to container elements in a generic way, without knowing which container is used (similar to iterators in the C++ STL). Iterators only allow sequential access (that is, from one element to the next one). For random access, Eina provides accessor functions.

Getting an iterator to access elements of a given container is done through the functions of that particular container. There is no function to create a generic iterator as iterators absolutely depend on the container. Note that all iterators, regardless of the container type, are always deleted with the same `eina_iterator_free()` function.

To get the data and iterate, use the `eina_iterator_next()` function. To call a function on every single element of a container, use the `eina_iterator_foreach()` function.

In addition to iterator functions, each data type also owns a set of macros that provide the iterators, such as `FOREACH` or `REVERSE_FOREACH`.

## Strings

### Stringshare

The `Eina_Stringshare` data type functions allow you to store a single copy of a string and use it in multiple places throughout your program. This way you can save a lot of strings with less memory. It improves string creation and destruction speed, reduces memory use, and decreases memory fragmentation.

With this data type you can reduce the number of duplicated strings kept in memory. It is common for the same strings to be dynamically allocated repeatedly between applications and libraries, especially in circumstances where you can have multiple copies of a structure that allocates the string. Rather than duplicating and freeing these strings, request a read-only pointer to an existing string and only incur the overhead of a hash lookup. This can sound like micro-optimizing, but profiling has shown that this can have a significant impact as the number of copies grows.

To manage stringshares:

1. To create a stringshare, declare a string variable and call the `eina_stringshare_add()` function:

   ```
   const char *mystr;
   const char *prologue = "Enlightenment is not just a window manager for Linux/X11 and others";

   mystr = eina_stringshare_add(prologue);
   ```

2. To retrieve or modify the string data:

   - Retrieve a string for use in a program from a format string using the `eina_stringshare_printf()` function. If you have a "format" string to pass to a function like `printf`, you can store it as a stringshare as well.

     The following example produces "1 desktop manager to rule them all".

     ```
     const char *myfmtstr = "%d desktop manager to rule them all";
     const char *str;

     str = eina_stringshare_printf(myfmtstr, 1);

     print(str);
     ```

   - Replace the value of a stringshare with the `eina_stringshare_replace()` function. Pass the pointer address and the new value to the function.

     ```
     eina_stringshare_replace(&str, "One desktop manager to rule them all");
     ```

   - Retrieve the length of the stringshare value with the `eina_stringshare_strlen()` function.

     ```
     printf("length: %d\n", eina_stringshare_strlen(str));
     ```

3. When the string is no longer needed, delete it using the `eina_stringshare_del()` function:

   ```
   eina_stringshare_del(mystr);
   ```

### String Buffer

The string buffer data type is designed to be a mutable string, allowing you to append, prepend or insert a string to a buffer. It allows easy handling of buffers in your applications.

To manage string buffers:

1. Initialize the `Eina_Strbuf` instance and create the buffer:

   ```
   Eina_Strbuf *buf;
   mybuffer = eina_strbuf_new();
   ```

2. Manage the buffer content:

   - To append characters to the buffer:

     - For basic strings, use the `eina_strbuf_append()` function:

       ```
       eina_strbuf_append(mybuffer, "This is my string.");
       ```

     - To append 1 character to your buffer, use the `eina_strbuf_append_char()` function. You can also append a sized string to the buffer using the `eina_strbuf_append_length()` function.

       ```
       eina_strbuf_append_length(mybuffer, "Buffe", 5);
       eina_strbuf_append_char(mybuffer, 'r');
       ```

     - To handle "printf" format strings, use the `eina_strbuf_append_printf()` function to add formatted strings to the buffer:
       ```
       eina_strbuf_append_printf(buf, "%s%c", "buffe", 'r');
       ```

   - To remove characters from one position to another, use the `eina_strbuf_remove()` function. The first parameter is the buffer, the second is the start position of the characters you want to delete, and the last the end position.

     This example removes the first 19 characters of the buffer:

     ```
     eina_strbuf_remove(buf, 0, 18);
     ```

   - To replace characters:

     - `eina_strbuf_replace()` replaces a specific occurrence of a given string in the buffer with another string.
     - `eina_strbuf_replace_all()` replaces all occurrences of a given string in the buffer with another string.

     ```
     eina_strbuf_append(mybuffer, "buffer buffer buffer");

     /* Replacing 1 occurrence of "buffer" by "B-U-F-F-E-R" */
     eina_strbuf_replace(mybuffer, "buffer", "B-U-F-F-E-R", 1);

     /* Replacing all the occurrences of "buffer" by "B-U-F-F-E-R" */
     eina_strbuf_replace_all(mybuffer, "buffer", "B-U-F-F-E-R");

     /* Replacing all the occurrences of "B-U-F-F-E-R" by "Buffer" */
     eina_strbuf_replace_all(mybuffer, "B-U-F-F-E-R", "Buffer");
     ```

   - To insert a string at the specified position, use the `eina_strbuf_insert()` function. Use the `eina_strbuf_insert_printf()` function with formatted strings.

     ```
     eina_strbuf_insert(mybuffer, "More buffer", 10);

     /* Using eina_strbuf_length_get to get the buffer length */
     eina_strbuf_insert_printf(buf, "%s: %d", 6, "length", eina_strbuf_length_get(buf));
     ```

   - To get the complete length of the string and the buffer, use the `eina_strbuf_string_get()` and `eina_strbuf_length_get()` functions:

     ```
     printf("%s: %d\n", eina_strbuf_string_get(mybuffer), eina_strbuf_length_get(buf));
     ```

3. When no longer needed, free the buffer with the `eina_strbuf_free()` function. You can also free the content of `Eina_Strbuf` without freeing the buffer itself using the `eina_strbuf_string_free()` function.

   ```
   eina_strbuf_free(mybuffer);
   ```

## Arrays

An array is a data type which describes an ordered collection of values. The values are accessed by their index.

```
INDEX | VALUE
--------------
0     | value0
1     | value1
2     | value2
3     | value3
4     | value4
5     | value5
6     | value6
7     | value7
```

Eina provides 2 array types: the classic array and an inline array.

### Creating and Destroying a Classic Array

The `eina_array_new()` function creates a new array. You can store strings or objects in the created array. The function returns a new array, or if memory allocation fails, `NULL`.

The first parameter of the `eina_array_new()` function defines the size of the array allocation step. For example, if you set it to 4, the function returns an array of 4 elements and the next time you grow the array it grows by 4 elements. Unless you have pushed 4 elements inside, it does not grow. But once you add the fifth element, it grows again and becomes an array of 8 elements. The allocation step feature is very useful for optimizing performance, and it also reduces memory fragmentation by having a size that fits the array usage. If you set the step to 0, the function sets a default safe value.

To create an array to store strings:

1. Create the array:

   ```
   /* Strings to store in the array */
   const char*
   strings[] =
   {
       "helo", "hera", "starbuck", "kat", "boomer",
       "hotdog", "longshot", "jammer", "crashdown", "hardball",
       "duck", "racetrack", "apolo", "husker", "freaker",
       "skulls", "bulldog", "flat top", "hammerhead", "gonzo"
   };
   /* Declaring the array (type Eina_Array) */
   Eina_Array *array;
   unsigned int i;

   /* Creating the array */
   array = eina_array_new(20);

   /* Inserting elements in the array */
   for (i = 0; i < 20; i++)
       eina_array_push(array, strdup(strings[i]));
   ```

2. To change the allocation step, use the `eina_array_step_set()` function:
   - The first parameter is the array you want to change.
   - The second parameter is the size of that specific array (retrieved with the `sizeof()` function).
   - The last parameter is the new step size.

   In this example, the array step changes from 20 to 30.

   ```
   eina_array_step_set(array, sizeof(*array), 30);
   ```

3. When no longer used, use the `eina_array_free()` function to free the array. It first calls the `eina_array_flush()` function and frees the memory of the pointer. It does not free the memory allocated for the elements of the array. To free them, use a `while` statement with the `eina_array_pop()` function.

   ```
   /* Freeing the array elements */
   while (eina_array_count(array))
       free(eina_array_pop(array));

   /* Freeing the array itself */
   eina_array_free(array);
   ```

### Modifying Classic Array Content

To modify classic array content:

- To set the data of an element, use the `eina_array_data_set()` function. The first parameter is the array, the second is the index of the element you want to set, and the last one is the data. You must first get the related pointer if you need to free it, as this function replaces the previously held data. Be careful, as there is no array or index check. If the value is `NULL` or invalid, the application can crash.

  ```
  free(eina_array_data_get(array, 0));
  eina_array_data_set(array, 0, strdup(strings[3]);
  ```

- To add elements to the end of the array, use the `eina_array_push()` function. The function returns `EINA_TRUE` on success, and `EINA_FALSE` on failure. The first parameter is the array to store the element, the second one is the data you want to store. If you store strings, remember to allocate the memory first. The example uses the `strdup()` function to duplicate the string contained in `strings[]`. This function allocates the memory of the returned string, so you do not have to do it yourself.

  ```
  for (i = 0; i < 20; i++)
      eina_array_push(array, strdup(strings[i]));
  ```

- To remove the last element of an array, use the `eina_array_pop()` function. It takes the array as a parameter, and if the operation is successful, returns a pointer to the data of the removed element.

  ```
  while (eina_array_count(array))
      free(eina_array_pop(array));
  ```

- To rebuild the array by specifying the data to be kept, use the `eina_array_remove()` function:

  - The first parameter is the array to be changed.
  - The second parameter is the function which selects the data to keep in the rebuilt array.
  - The last parameter is the data to pass to the selector function defined as the second parameter.

  The selector function has to return an `Eina_Bool`, `EINA_TRUE` if the element stays, and `EINA_FALSE` if it has to be removed.

  The following example shows how to remove all the elements of the array that are longer than 5.

  ```
  /* Selector function */
  Eina_Bool
  keep(void *data, void *gdata)
  {
      if (strlen((const char*)data) <= 5)
          return EINA_TRUE;

      return EINA_FALSE;
  }

  int
  remove_array()
  {
      Eina_Array *array;
      Eina_Array_Iterator iterator;
      const char *item;
      unsigned int i;

      /* Creating and populating an array */

      /* Removing the undesired elements */
      eina_array_remove(array, keep, NULL);

      /* Flushing and freeing the array */

      return 0;
  }
  ```

- To completely wipe an array out, use the `eina_array_flush()` function. This function sets the count and total members of an array to 0, and frees and sets its data members to `NULL`. For performance reasons, there is no array check. If the value is `NULL` or invalid, the program can crash. The only parameter of this function is a pointer to the `Eina_Array` array you want to flush.

  ```
  eina_array_flush(array);
  ```

- To empty an array quickly, use the `eina_array_clean()` function. This function sets the counting of members in the array to 0. It does not free any space so you have to use it carefully. For performance reasons, there is no array check. If the value is `NULL` or invalid, the program can crash.

  ```
  eina_array_clean(array);
  ```

### Accessing Classic Array Data

To access classic array data:

- To access the data in the array, use the `eina_array_data_get()` function with the array and the index of the element you want to get. The function returns a pointer to the data.

  ```
  /* Getting the data of the first element */
  char *mydata;
  mydata = eina_array_data_get(array, 0);
  ```

- To get the number of elements in an array, use the `eina_array_count()` function. The first parameter is a pointer to the array variable returned by the `eina_array_new()` function.

  The function returns the number of elements.

  ```
  unsigned int nb_elm;
  nb_elm = eina_array_count(array);
  ```

- To iterate through an array, you can use various methods:

  - Use the `Eina_Array` iterator called `ITER_NEXT`.

    You can use the iterator by calling the macro `EINA_ARRAY_ITER_NEXT()`. It takes the array to iterate as the first parameter, a counter for the current index during the iteration, and a variable of the same type as the item data and an `Eina_Iterator`. To use it, declare an `Eina_Iterator`, an `int` counter, and, for example, a `char *` item if your array contains any strings.

    ```
    Eina_Array_Iterator iterator;
    const char *item;
    unsigned int i;

    EINA_ARRAY_ITER_NEXT(array, i, item, iterator)
        printf("item #%d: %s\n", i, item);
    ```

  - Use the `eina_array_foreach()` function to iterate over the array.

    The first parameter is the array to iterate, the second is a callback function which determines whether the iteration can continue, and the last is the data passed to the callback function.

    To iterate over the array and to print the data of each array element:

    ```
    /* Callback function */
    static Eina_Bool
    elm_print(const void *container, void *data, void *fdata)
    {
        printf("%s\n", (char *)data);

        return EINA_TRUE;
    }

    int
    iterating_array()
    {
        Eina_Array *array;
        unsigned int i;

        /* Creating and populating an array */

        /* Iterating over the array and calling elm_print on each element */
        eina_array_foreach(array, elm_print, NULL);

        /* Freeing the element data and array */

        return 0;
    }
    ```

  - Use the `eina_array_iterator_new()` function to create an iterator for the array.

    The function returns a newly allocated iterator associated with the array. If the array is `NULL` or the count of the array members is less than or equal to 0, the function returns `NULL`. If the memory cannot be allocated, `NULL` is returned and `EINA_ERROR_OUT_OF_MEMORY` is thrown. Otherwise, a valid iterator is returned.

    Pass to this function the array for which you want to create a new iterator. The iterator is used to run a sequential walk through the array, exactly like the `eina_array_foreach()` function.

    To create an iterator and use it to print the data of each array element:

    ```
    static Eina_Bool
    print_one(const void *container, void *data, void *fdata)
    {
        printf("%s\n", (char*)data);

        return EINA_TRUE;
    }

    int
    new_iterator()
    {
        Eina_Array *array;
        Eina_Iterator *it;
        unsigned short int i;
        void *uninteresting;
        Eina_Bool rt;

        /* Creating and populating an array */

        it = eina_array_iterator_new(array);

        it = eina_iterator_next(it, &uninteresting);
        eina_iterator_foreach(it, print_one, NULL);
        eina_iterator_free(it);

        return 0;
    }
    ```

  - Use the `eina_array_accessor_new()` function to get random access to the array elements.

    The function returns a newly allocated accessor associated with the array. If the array is `NULL` or the counting of array members is less than or equal to 0, this function returns `NULL`. If the memory cannot be allocated, `NULL` is returned and `EINA_ERROR_OUT_OF_MEMORY` is thrown. Otherwise, a valid accessor is returned.

    To use the accessor to retrieve and print the data of every other array element:

    ```
    int
    random_access()
    {
        /* Declaration of the array */
        Eina_Array *array;
        /* Declaration of the accessor */
        Eina_Accessor *acc;

        /* Generic counter */
        unsigned short int i;

        /* Variable to put the data retrieved from an array element */
        void *data;

        /* Creating and populating an array */

        /* Creating the array accessor */
        acc = eina_array_accessor_new(array);

        /* Random access to the data of the array elements */
        for (i = 1; i < 10; i += 2) {
            /* Putting the data in the variable 'data' */
            eina_accessor_data_get(acc, i, &data);
            printf("%s\n", (const char *)data);
        }

        /* Freeing the accessor */
        eina_accessor_free(acc);

        /* Freeing the array */

        return 0;
    }
    ```

### Creating and Destroying an Inline Array

An inline array is a container that stores the data itself, not the pointers to the data. This means there is no memory fragmentation, and for small data types, such as char, short, and int, it is more memory-efficient. This is because the data is stored in the cache and is faster to access. The bigger the data gets, however, the less likely it is and the less interesting it becomes.

To create an inline array, use the `eina_inarray_new()` function:

- The first parameter is the size of the value. In this example, only the characters are stored, and because of that, only `sizeof(char)` is passed to the function.

- The second parameter defines the size of the array allocation step. For example, if you set it to 4, the function returns an inline array of 4 elements, and the next time you grow the inline array, it grows by 4 elements and becomes an array of 8 elements. If you set the step to 0, the function sets a default safe value.

  The step can be changed later using the `eina_inarray_step_set()` function.

The `eina_inarray_new()` function returns a pointer to the new `Eina_Inarray` variable.

```
int
inline_array()
{
    /* Declare an inline array variable of the type Eina_Inarray */
    Eina_Inarray *iarr;

    /* Create an inline array of "char" */
    iarr = eina_inarray_new(sizeof(char), 0);

    /* When no longer needed, free the array memory */
    eina_inarray_free(iarr);

    return 0;
}
```

### Modifying Inline Array Content

To modify inline array content:

- To add data as the last element of the inline array, use the `eina_inarray_push()` function. The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function. The second parameter is the data you want to push to the inline array.

  If everything runs fine, the function returns the index of the new element. If something goes wrong, it returns `-1`.

  ```
  ch = 'a';
  eina_inarray_push(iarr, &ch);
  ```

- To insert data to a given position of the inline array, use the `eina_inarray_insert_at()` function:

  - The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function.
  - The second parameter is the index of the element you want to add to the inline array.
  - The last parameter is a pointer to the content to be added.

  The content of the pointer is copied to the given position in the inline array. All the members from the position to the end of the array are shifted towards the end. If the position is equal to the end of the array, the member is appended. If the position is bigger than the array length, the function fails.

  ```
  ch = 'a';
  eina_inarray_push(iarr, &ch);
  ch = 'b';
  eina_inarray_push(iarr, &ch);
  ch = 'd';
  eina_inarray_push(iarr, &ch);

  /* Adding data on position 3 */
  ch = 'c';
  eina_inarray_insert_at(iarr, 2, &ch);
  ```

- To insert data with your own position criteria, use the `eina_inarray_insert()` or `eina_inarray_insert_sorted()` function. The only difference between these functions is that the `eina_inarray_insert_sorted()` function assumes that the array is already sorted and consequently optimizes the insertion position by doing a binary search.

  In both functions:

  - The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function.

  - The second parameter is the data you want to push to the inline array.

  - The last parameter is the callback comparison function.

    The `Eina_Compare_Cb` callback function compares data1 and data2. data1 is the value contained in the inline array and data2 is the data you pass to the `eina_inarray_insert()` or `eina_inarray_insert_sorted()` function as the second parameter. If data1 is less than data2, -1 must be returned, if it is greater, 1 must be returned, and if they are equal, 0 must be returned.

  The following example shows how to insert a value before a greater value:

  ```
  /* Defining the comparison function with the position criteria */
  Eina_Compare_Cb
  cmp(const void *a, const void *b)
  {
      return *(int*)a > *(int*)b;
  }

  int
  inline_insert()
  {
      Eina_Inarray *iarr;
      char ch;
      char *ch3;
      int a;
      int *b;

      /* Creating an inline array */

      /* Adding data to the inline array */
      a = 97;
      eina_inarray_push(iarr, &a);
      a = 98;
      eina_inarray_push(iarr, &a);
      a = 100;
      eina_inarray_push(iarr, &a);

      /* Inserting data with the criteria */
      a = 99;
      eina_inarray_insert_sorted(iarr, &a, cmp);

      eina_inarray_free(iarr);
  }
  ```

- To remove the last element of the inline array, use the `eina_inarray_pop()` function. The only parameter is a pointer to the array variable returned by the `eina_inarray_new()` function. This function returns the data removed from the inline array.

  ```
  eina_inarray_pop(iarr);
  ```

- To remove specific data from an inline array, use the `eina_inarray_remove()` function. The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function. The second parameter is the data you want to remove from the inline array.

  The `eina_inarray_remove()` function finds the data and removes the matching members from the array. The data can be an existing member of an inline array for optimized usage. In other cases, the content is matched using the `memcmp()` function.

  The `eina_inarray_remove()` function returns the index of the removed member, or -1 if failed.

  ```
  iarr = eina_inarray_new(sizeof(char), 0);

  ch = 'a';
  eina_inarray_push(iarr, &ch);

  /* Removing data from the array */
  eina_inarray_remove(iarr, &ch);
  ```

- To remove data from a defined position in an inline array, use the `eina_inarray_remove_at()` function. The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function. The second parameter is the index of the element you want to remove from the inline array.

  The function returns `EINA_TRUE` on success and `EINA_FALSE` if something goes wrong. The member is removed from the inline array and any members after it are moved towards the array's head.

  ```
  /* Removing data from position 2 */
  eina_inarray_remove_at(iarr, 2);
  ```

- To remove all the elements of the array, use the `eina_inarray_flush()` function. The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function. The function removes every member from the array.

  ```
  eina_inarray_flush(iarr);
  ```

- To replace values in the inline array, use the `eina_inarray_replace_at()` function, which copies the data over the given position:

  - The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function.
  - The second parameter is the index of the element you want to remove from the inline array.
  - The last parameter is the data you want to copy in place of the current data.

  The function returns `EINA_TRUE` on success, and `EINA_FALSE` on failure. The given pointer content is copied to the given position in the array. The pointer is not referenced, instead its contents are copied to the member's array using the previously defined `member_size`. If the position does not exist, the function fails.

  ```
  /* Replacing the member at position 3 */
  ch = 'd';
  eina_inarray_replace_at(iarr, 3, &ch);
  ```

- To sort an inline array, use the `eina_inarray_sort()` function, which applies a quick sort algorithm to the inline array:

  - The first parameter is a pointer to the array returned by the `eina_inarray_new()` function.
  - The last parameter is the `Eina_Compare_Cb` callback comparison function, which compares data1 and data2.

    data1 and data2 are values contained in the inline array. If the data matches, the function must return 0, if data1 is less than data2, -1 must be returned and if it is greater, 1 must be returned.

  ```
  static int
  short_cmp(const void *pa, const void *pb)
  {
      const short *a = pa, *b = pb;

      return *a - *b;
  }

  int
  sorting_inline_array()
  {
      Eina_Inarray *array;
      int i;

      /* Creating and populating the inline array */

      eina_inarray_sort(array, short_cmp);
      eina_inarray_free(array);
  }
  ```

  Be careful, the data given to the compare function is the pointer to the member memory itself. Do not change it.

### Accessing Inline Array Data

To access inline array data:

- To search for a member in an inline array, use the `eina_inarray_search()` function that runs a linear walk looking for the given data:

  - The first parameter is a pointer to the array variable returned by the `eina_inarray_new()` function.
  - The second parameter is the data used by the callback function to run the comparison.
  - The last parameter is the `Eina_Compare_Cb` callback comparison function, which compares data1 and data2.

    data1 is the value contained in the inline array and data2 is the data you pass to the `eina_inarray_search()` function as the second parameter. If the data matches, the function must return 0, if data1 is less than data2, -1 must be returned and if it is greater, 1 must be returned.

  The function returns the member index, or -1 if not found.

  ```
  Eina_Compare_Cb
  compare(const void *pa, const void *pb)
  {
      const short *a = pa, *b = pb;
      if (*a == *b)
          return EINA_TRUE;

      return EINA_FALSE;
  }

  int
  search_inline_array()
  {
      Eina_Inarray *array;
      int i;
      int elm_index;
      int to_search = 3;

      /* Creating and populating the inline array */

      elm_index = eina_inarray_search(array, &to_search, compare);
      eina_inarray_free(array);
  }
  ```

  Be careful, the data given to the compare function is the pointer to the member memory itself. Do not change it.

  The `eina_inarray_search_sorted()` function does exactly the same as `eina_inarray_search()`, but uses a binary search for the given data.

- To get the number of elements in an inline array, use the `eina_inarray_count()`. The first parameter is a pointer to the array returned by the `eina_inarray_new()` function. The function returns an unsigned `int`, the number of elements.

  ```
  printf("Inline array of integers with %d elements:\n", eina_inarray_count(iarr));
  ```

- To iterate through an inline array, you can use various methods:

  - You can use the iterator macros for the inline arrays: `FOREACH` and `REVERSE_FOREACH`.

  - To run a linear walk over an array of elements, use the `EINA_INARRAY_FOREACH()` macro. The first parameter is a pointer to the array variable returned by `eina_inarray_new()`, and the second parameter is the variable into which the current value is put during the walk. The `EINA_INARRAY_REVERSE_FOREACH()` macro does the same thing but starts from the last element.

    The following example illustrates the printing of each element and its pointer:

    ```
    iarr = eina_inarray_new(sizeof(char), 0);
    int a;
    int *b;

    a = 97;
    eina_inarray_push(iarr, &a);
    a = 98;
    eina_inarray_push(iarr, &a);
    a = 99;
    eina_inarray_push(iarr, &a);

    EINA_INARRAY_FOREACH(iarr, b)
        printf("int: %d(pointer: %p)\n", *b, b);
    ```

  - To process the array data, use the `eina_inarray_foreach()` function, which invokes the given function on each element of the array with the given data:
    - The first parameter is a pointer to the array variable returned by `eina_inarray_new()`.
    - The second parameter is the function to run on each element.

      The function must return `EINA_TRUE` as long as you want to continue iterating. By returning `EINA_FALSE`, you stop the iteration and make the `eina_inarray_foreach()` function return `EINA_FALSE`.

      The data given to the function is the pointer to the member itself.

    - The last parameter is the data passed to the function called on each element.

    The `eina_inarray_foreach()` function returns `EINA_TRUE` if it successfully iterates through all items of the array. Call the function for every given data in the array. This is a safe way to iterate over an array.

    ```
    static Eina_Bool
    array_foreach(const void *array __UNUSED__, void *p, void *user_data __UNUSED__)
    {
        short *member = p;
        int *i = user_data;
        (*p)++;
        (*i)++;

        return EINA_TRUE;
    }

    int
    inline_array_foreach()
    {
        Eina_Inarray *iarr;
        iarr = eina_inarray_new(sizeof(char), 1);
        int i;

        for (i = 0; i < numbers_count; i++) {
            short val = i;
            eina_inarray_push(iarr, &val);
        }

        i = 0;
        eina_inarray_foreach(iarr, array_foreach, &i);

        eina_inarray_free(iarr);

        return 0;
    }
    ```

  - To remove some elements based on your own criteria, use the `eina_inarray_foreach_remove()` function, which walks through the array and, if the value matches in the callback function, removes the element:
    - The first parameter is a pointer to the array returned by `eina_inarray_new()` function.
    - The second parameter is the callback function to run on each element.

      The callback function returns `EINA_TRUE` if the value matches, or `EINA_FALSE` if it does not match.

    - The last parameter is the data passed to the callback function.

    The function returns the number of removed entries or -1 if something goes wrong.

    ```
    static Eina_Bool
    array_foreach(const void *array __UNUSED__, void *p, void *user_data __UNUSED__)
    {
        short *member = p;
        int *i = user_data;
        if (*i == *p)
            return EINA_TRUE;

        return EINA_FALSE;
    }

    int
    inline_array_foreach_remove()
    {
        Eina_Inarray *iarr;
        iarr = eina_inarray_new(sizeof(char), 1);
        int i;

        for (i = 0; i < numbers_count; i++) {
            short val = i;
            eina_inarray_push(iarr, &val);
        }

        i = 6;
        eina_inarray_foreach_remove(iarr, array_foreach, &i);

        eina_inarray_free(iarr);

        return 0;
    }
    ```

## Hash Tables

The `Eina_Hash` provides a way to store values in association with a key. For example, if you want to store some tuples into a table, you can do it using the `Eina_Hash`.

The `Eina_Hash` is implemented using an array of "buckets" where each bucket is a pointer to a structure that is the head of a red-black tree. This implementation makes it very robust against weak keys as, in the worst case scenario, you can still depend on an efficient binary tree implementation.

### Creating a Hash Table

To create the hash table, use the `eina_hash_new()` function:

- The first parameter is the function called when getting the size of the key.
- The second parameter is the function called when comparing the keys.
- The third parameter is the function called when getting the values.
- The fourth parameter is the function called on each value when the hash table is freed, or when an item is deleted from it. `NULL` can be passed as the callback.
- The last parameter is the size of the buckets.

When you create an `Eina_Hash` instance, you have to create 4 potentially long callback functions. To make the functions shorter, `Eina_Hash` offers some predefined functions to create the following kinds of hash tables:

- `eina_hash_string_djb2_new()` creates a new hash table using the djb2 algorithm for strings.
- `eina_hash_string_superfast_new()` creates a new hash table for use with strings (better with long strings).
- `eina_hash_string_small_new()` creates a new hash table for use with strings with a small bucket size.
- `eina_hash_int32_new()` and `eina_hash_int64_new()` create a new hash table for use with 32-bit and 64-bit integers.
- `eina_hash_pointer_new()` creates a new hash table for use with pointers.
- `eina_hash_stringshared_new()` creates a new hash table for use with shared strings.

All these predefined functions require only 1 parameter, which is the function to free the data you store in the hash table.

The following example shows how to manage a small phone book using the `eina_hash_string_superfast_new()` function to create the hash table.

1. Create the phone book structure and some static data:

   ```
   struct _Phone_Entry {
       const char *name; /* Full name */
       const char *number; /* Phone number */
   };

   typedef struct _Phone_Entry Phone_Entry;

   static Phone_Entry
   _start_entries[] =
   {
       {"Wolfgang Amadeus Mozart", "+01 23 456-78910"},
       {"Ludwig van Beethoven", "+12 34 567-89101"},
       {"Richard Georg Strauss", "+23 45 678-91012"},
       {"Heitor Villa-Lobos", "+34 56 789-10123"},
       {NULL, NULL}
   };
   ```

2. Create the callback to free the data:

   ```
   static void
   _phone_entry_free_cb(void *data)
   {
       free(data);
   }
   ```

   The free callback can be changed later using the `eina_hash_free_cb_set()` function. You need to pass the hash and the new callback function.

3. Create and destroy the hash table.

   The `eina_hash_free_buckets()` function frees all hash table buckets. It empties the hash but does not destroy it, and you can still use it for another purpose. When `eina_hash_free()` is called, the space allocated for the hash is freed.

   ```
   int
   free_data()
   {
       Eina_Hash *phone_book = NULL;
       phone_book = eina_hash_string_superfast_new(_phone_entry_free_cb);

       /* Empty the phone book without destroying it */
       eina_hash_free_buckets(phone_book);
       eina_hash_free(phone_book);
   }
   ```

### Modifying Hash Table Content

To modify hash table content:

- To add some data to a hash, use the `eina_hash_add()` function. This function takes the hash, the key to access the data, and the data as its parameters.

  The following example shows how to add the initial data declared earlier to the hash:

  ```
  for (i = 0; _start_entries[i].name != NULL; i++)
      eina_hash_add(phone_book, _start_entries[i].name, strdup(_start_entries[i].number));
  ```

  The `Eina_Hash` offers various ways to add elements to a hash, such as the `eina_hash_direct_add()` function, which adds the entry without duplicating the string key. The key is stored in the struct, so this function can be used with `eina_stringshare` to avoid key data duplication.

  ```
  for (i = 0; _start_entries[i].name != NULL; i++) {
      /* Allocating memory for the phone entry */
      Phone_Entry *e = malloc(sizeof(Phone_Entry));

      /* Creating an eina_stringshare for the name and the phone number */
      e->name = eina_stringshare_add(_start_entries[i].name);
      e->number = eina_stringshare_add(_start_entries[i].number);

      /* Adding the entry to the hash */
      eina_hash_direct_add(phone_book, e->name, e);
  }
  ```

- To modify an entry, use `eina_hash_modify()` function passing the hash, the key of the data to change, and the new data. The function returns the old data on success.

  The `eina_hash_set()` function does the same work as `eina_hash_modify()`, but if the entry does not exist, the function creates a new one.

  ```
  char *old_phone = NULL;
  char *phone = NULL;
  /* Replace the phone number of Richard Strauss */
  old_phone = eina_hash_modify(phone_book, "Richard Georg Strauss", strdup("+23 45 111-11111"));
  phone = eina_hash_set(phone_book, "Philippe de Magalhães", strdup("+33 6 111-11111"));
  eina_hash_set(phone_book, "Richard Georg Strauss", strdup("+23 45 111-117711"));
  ```

- To change the key associated with the data without freeing and creating a new entry, use the `eina_hash_move()` function. You only have to pass the hash, the old key, and the new key. If the operation succeeds, the function returns `EINA_TRUE`, if not, it returns `EINA_FALSE`.

  ```
  Eina_Bool res;
  res = eina_hash_move(phone_book, "Philippe de Magalhães", "Filipe de Magalhães");
  ```

- To delete entries from a hash table:

  - Use the `eina_hash_del()` function to remove the entry identified by a key or data from the given hash table:
    ```
    Eina_Bool r;
    const char *entry_name = "Heitor Villa-Lobos";
    r = eina_hash_del(phone_book, entry_name, NULL);
    ```

  - Use the `eina_hash_del_by_key()` function to remove an entry based on the key:
    ```
    r = eina_hash_del_by_key(phone_book, "Richard Georg Strauss");
    ```

  - Use the `eina_hash_del_by_data()` function to remove an entry based on the data:
    ```
    r = eina_hash_del_by_data(phone_book, "+12 34 567-89101");
    ```

### Accessing Hash Table Data

To find hash table elements and get data based on the key name:

- To retrieve an entry based on its key, use the `eina_hash_find()` function by passing the hash and the key you are looking for:

  ```
  char *phone = NULL;
  const char *entry_name = "Heitor Villa-Lobos";

  /* Look for a specific entry and get its phone number */
  phone = eina_hash_find(phone_book, entry_name);
  ```

- To get the number of entries in a hash, use the `eina_hash_population()` function. Pass the hash as the only argument.

  ```
  unsigned int nb_elm;
  nb_elm = eina_hash_population(phone_book);
  ```

- To iterate through a hash table, you can use various methods:

  - To iterate over the hash table, use the `eina_hash_foreach()` function:
    - The first parameter is the hash.
    - The second parameter is the callback function called on each iteration.

      The callback function has to return an `Eina_Bool`, `EINA_TRUE` if the iteration has to continue and `EINA_FALSE` if the iteration has to stop.

    - The last parameter is the data passed to the callback function.

      The following example prints the key and the data of the hash entry (the name and the phone number):

    ```
    static Eina_Bool
    pb_foreach_cb(const Eina_Hash *phone_book, const void *key, void *data, void *fdata)
    {
        const char *name = key;
        const char *number = data;
        printf("%s: %s\n", name, number);

        /* Return EINA_FALSE to stop this callback from being called */
        return EINA_TRUE;
    }

    printf("List of phones:\n");

    /* Running the callback on the hash called phone_book */
    eina_hash_foreach(phone_book, pb_foreach_cb, NULL);
    printf("\n");
    ```

  - To iterate over the keys, use the `eina_hash_iterator_key_new()` function:

    ```
    /* Declaration of the Eina_Iterator */
    Eina_Iterator *it;

    /* Variable to handle the current iteration "data" */
    void *data;

    /* Iterate over the keys (names) */
    printf("List of names in the phone book:\n");

    it = eina_hash_iterator_key_new(phone_book);

    /* Use the generic eina_iterator_next() */
    while (eina_iterator_next(it, &data)) {
        const char *name = data;
        printf("%s\n", name);
    }

    /* Free the iterator */
    eina_iterator_free(it);
    ```

  - To iterate over the hash data, use the `eina_hash_iterator_data_new()` function the same way as `eina_hash_iterator_key_new()`:

    ```
    /* Declaration of the Eina_Iterator */
    Eina_Iterator *it;

    /* Variable to handle the current iteration "data" */
    void *data;

    /* Iterate over hash data */
    printf("List of numbers in the phone book:\n");

    it = eina_hash_iterator_data_new(phone_book);
    while (eina_iterator_next(it, &data)) {
        const char *number = data;
        printf("%s\n", number);
    }

    /* Free the iterator */
    eina_iterator_free(it);
    ```

  - To iterate over a tuple composed of keys and data, use the `eina_hash_iterator_tuple_new()` function:

    ```
    /* Declaration of the Eina_Iterator */
    Eina_Iterator *tit;

    /* Variable to handle the current iteration "data" */
    void *tuple;

    printf("List of phones:\n");
    tit = eina_hash_iterator_tuple_new(phone_book);
    while (eina_iterator_next(tit, &tuple)) {
        Eina_Hash_Tuple *t = tuple;
        const char *name = t->key;
        const char *number = t->data;
        printf("%s: %s\n", name, number);
    }

    /* Always free the iterator after its use */
    eina_iterator_free(tit);
    ```

## Lists

The `Eina_List` is a double-linked list that can store data of any type as void pointers. It provides a set of functions to create and manipulate the list to avoid the access to the struct's fields, similar to a self-made double-link list.

In addition to the previous and next node and its data, the `Eina_List` nodes keep a reference to an accounting structure. The accounting structure is used to improve the performance of some functions. The structure is private and must not be modified.

In an `Eina_List`, everything is a "list": the list itself is a list where each node is a list as well.

Eina provides 2 list types: the classic list (`Eina_List`) and an inline list (`Eina_Inlist`).

### Creating and Destroying a List

To use an `Eina_List`:

1. Declare the list with `NULL` as the default value:

   ```
   int
   list()
   {
       /* Declaration of the Eina_List with NULL as default value */
       Eina_List *list = NULL;
   ```

2. Call the `eina_list_append()` function with the list and the data you want to append as parameters.

   The list must be a pointer to the first element of the list (or `NULL`). The function returns a pointer to the list.

   ```
       /* Creating the first element of the list */
       list = eina_list_append(list, "watch");

       /* Adding more elements */
       list = eina_list_append(list, "phone");
       list = eina_list_append(list, "ivi");
       list = eina_list_append(list, "notebook");
   ```

3. When you no longer need the list, free it:

   ```
       /* Free the Eina_List */
       eina_list_free(list);

       return 0;
   }
   ```

### Modifying List Content

To modify list content:

- To add data to a list:

  - To add data at the end of the list, use the `eina_list_append()` function. To add data at the top of the list, use `eina_list_prepend()`. The functions work in the same way, only adding the data to different places.

    ```
    list = eina_list_prepend(list, "set-top box");
    ```

  - To insert data into the list after a specified data, use the `eina_list_append_relative()` function. As the last parameter, define the element after which the data is added.

    For example to append data after the "phone" element:

    ```
    list = eina_list_append_relative(list, "single-board computer", "phone");
    ```

  - To add a new entry before a specified data, use the `eina_list_prepend_relative()` function. It is similar to the `eina_list_append_relative()` function.

    ```
    list = eina_list_prepend_relative(list, "ultrabook", "ivi");
    ```

  - To append a list node to a linked list after a specified member, use the `eina_list_append_relative_list()` function. To prepend a list node to a linked list before a specified member, use the `Eina_List * eina_list_prepend_relative_list()` function.

- To set data in a list member, use the `eina_list_data_set()` function. Pass the "list" (node) as the first argument and the data to set as the second.

  The following example also shows the usage of the `eina_list_last()` function, which returns the last element of an `Eina_List`.

  ```
  /* Setting new data for the last element */
  eina_list_data_set(eina_list_last(list), eina_stringshare_add("Boris"));
  ```

- To remove a node from the list, use the `eina_list_remove()` function. This function removes the first instance of the specified data from the given list.

  ```
  list = eina_list_remove(list, "ultrabook");
  ```

  You can also remove a "list" (node) from a list using the `eina_list_remove_list()` function. Pass the list you want to delete an element from and a 'list' (node) you want to delete.

  ```
  Eina_List *app_list = NULL;
  Eina_List *to_remove = NULL;

  /* Adding some elements to the list (using stringshares) */
  app_list = eina_list_append(app_list, eina_stringshare_add("enna"));
  app_list = eina_list_append(app_list, eina_stringshare_add("ebird"));
  app_list = eina_list_append(app_list, eina_stringshare_add("calaos"));
  app_list = eina_list_append(app_list, eina_stringshare_add("rage"));
  app_list = eina_list_append(app_list, eina_stringshare_add("terminology"));
  app_list = eina_list_append(app_list, eina_stringshare_add("enlightenment"));
  app_list = eina_list_append(app_list, eina_stringshare_add("eyelight"));
  app_list = eina_list_append(app_list, eina_stringshare_add("ephoto"));

  /* Finding the "list" to remove */
  to_remove = eina_list_data_find_list(list, eina_string_share_add("enlightenment"));

  list = eina_list_remove_list(list, to_remove);
  ```

- To move elements in a list, you can use various functions, such as `eina_list_promote_list()` that promotes an element to the top of the list or `eina_list_demote_list()` that puts the specified element at the end of the list. Remember that everything is a list so the second parameter represents the "list" (node) you want to move. Use the functions exactly like the `eina_list_remove_list()` function.

  ```
  list = eina_list_promote_list(list, eina_list_data_find_list(list, "ivi"));
  ```

- To reverse all the elements of a list, use the `eina_list_reverse()` function. To obtain a reversed copy of the list while keeping the initial list unchanged, use the `eina_list_reverse_clone()` function.

  ```
  Eina_List *rev_copy;

  app_list = eina_list_reverse(app_list);
  rev_copy = eina_list_reverse_clone(app_list);
  ```

- To sort a list, use the `eina_list_sort()` function. This function takes a list which needs to be sorted, the maximum number of elements to be sorted, and a callback function that compares data. To sort all list elements, set the maximum number of elements to 0.

  ```
  int
  sort_cb(const void *d1, const void *d2)
  {
      const char *txt = d1;
      const char *txt2 = d2;
      if (!txt)
          return(1);
      if (!txt2)
          return(-1);

      return(strcmp(txt, txt2));
  }

  extern Eina_List *list;
  list = eina_list_sort(list, 0, sort_cb);
  ```

- To merge 2 list into 1, use the `eina_list_merge()` function. The `eina_list_sorted_merge()` function merges 2 sorted lists according to the ordering function that you pass as the last argument.

  ```
  int
  sort_cb(void *d1, void *d2)
  {
      const char *txt = NULL;
      const char *txt2 = NULL;
      if (!d1)
          return(1);
      if (!d2)
          return(-1);

      return(strcmp((const char*)d1, (const char*)d2));
  }

  Eina_List *sorted1;
  Eina_List *sorted2;
  Eina_List *newlist;

  /* Insert some values and sort your lists */

  /* Simply merge 2 lists without any process */
  newlist = eina_list_merge(sorted1, sorted2);

  newlist = eina_list_sorted_merge(sorted1, sorted2, sort_cb);
  ```

- To split a list, use the `eina_list_split_list()` function:

  - The first parameter is the list to split.

  - The second parameter is the "list" (element) after which the list is split.

  - The last parameter is the head of the second list.

    ```
    /* Original list (left list) */
    Eina_List *list = NULL;

    /* New list (right list) */
    Eina_List *other_list = NULL;

    /* Eina_List (element) */
    Eina_List *l;

    list = eina_list_append(list, "super tux");
    list = eina_list_append(list, "frozen bubble");
    list = eina_list_append(list, "lincity-ng");

    /* Sorting the list (just for fun) */
    list = eina_list_sort(list, 0, cmp_func);

    /* Looking for the 'split' element */
    l = eina_list_search_sorted_list(list, cmp_func, "frozen bubble");

    /* Splitting the list */
    list = eina_list_split_list(list, l, &other_list);
    ```

- To copy a list, use the `eina_list_clone()` function. The function copies all the elements in the list in the exact same order.

  ```
  Eina_List *app_list_copy;

  app_list_copy = eina_list_clone(app_list);
  ```

### Accessing List Data

To access list data:

- To find some data on your list, use the `eina_list_data_find()` function. Pass the list containing your data as the first parameter and the data you are looking for as the last one. The function returns the found member data pointer if found, `NULL` otherwise.

  The `eina_list_data_find()` function searches the list from the beginning to the end for the first member for which the data pointer is data. If it is found, the data is returned, otherwise `NULL` is returned. The function only compares pointers, which is why using `Eina_Stringshare` is very useful with lists, because it always returns the same pointer for the same string.

  ```
  Eina_List *app_list = NULL;
  const char *res_str;

  /* Adding some elements to the list (using stringshares) */
  app_list = eina_list_append(app_list, eina_stringshare_add("enna"));
  app_list = eina_list_append(app_list, eina_stringshare_add("ebird"));
  app_list = eina_list_append(app_list, eina_stringshare_add("calaos"));
  app_list = eina_list_append(app_list, eina_stringshare_add("rage"));
  app_list = eina_list_append(app_list, eina_stringshare_add("terminology"));
  app_list = eina_list_append(app_list, eina_stringshare_add("enlightenment"));
  app_list = eina_list_append(app_list, eina_stringshare_add("eyelight"));
  app_list = eina_list_append(app_list, eina_stringshare_add("ephoto"));

  /* Finding the data */
  res_str = eina_list_data_find(list, eina_string_share_add("enlightenment"));
  if (res_str == eina_stringshare_add("enlightenment"))
      printf("Data is present");
  else
      printf("Data not present");
  ```

  The above example returns "Data is present".

  The `eina_list_data_find_list()` function does the same thing as `eina_list_data_find()`, but returns an `Eina_List`. For an example, see the [`eina_list_remove_list()` function](#remove_list).

  You can access the data or a "list" (node) of an `Eina_List` using the `eina_list_nth()` and `eina_list_nth_list()` functions. The first one returns a pointer to the data of the "n" element and the second a pointer to the "list". To access the data of the third element of an `Eina_List`:

  ```
  const char *res;
  Eina_List *res_lst;

  res = eina_list_nth(app_list, 2);
  res_lst = eina_list_nth_list(app_list, 2);
  ```

  The `res` variable contains the pointer to the string "calaos". The `res_lst` variable is the list containing "calaos".

- To search for data in a list, select your function based on whether the list is sorted or unsorted.

  - To search in an unsorted list, use the `eina_list_search_unsorted()` function:

    - The first parameter is the list.
    - The second parameter is a callback function for comparison.
    - The last parameter is the data you are looking for.

    The `eina_list_search_unsorted_list()` function does the same but returns an "Eina_List".

    The following example shows 2 searches using both the `eina_list_search_unsorted()` and `eina_list_search_unsorted_list()` functions:

    ```
    int
    search_list()
    {
        /* Declaring the list */
        Eina_List *list = NULL;
        Eina_List *l;
        /* Little trick to use strcmp as Eina_Compare_Cb */
        Eina_Compare_Cb cmp_func = (Eina_Compare_Cb)strcmp;

        void *data;
        int cmp_result;

        list = eina_list_append(list, "debian");
        list = eina_list_append(list, "archlinux");
        list = eina_list_append(list, "centos");

        data = eina_list_search_unsorted(list, cmp_func, "archlinux");
        l = eina_list_search_unsorted_list(list, cmp_func, "archlinux");
        if (l->data != data) {
            eina_list_free(list);

            return 1;
        }

        eina_list_free(list);

        return 0;
    }
    ```

  - To search in sorted lists, use the `eina_list_search_sorted_list()` and `eina_list_search_sorted()` functions. They work similarly as the `eina_list_search_unsorted()` function.

- To get data from a list element, use the `eina_list_data_get()` function. The function returns the data contained in the given list.

  The following example uses the `eina_list_next()` function to move through the list in a statement.

  ```
  int
  list_data_set()
  {
      /* Declaring the list */
      Eina_List *list = NULL;
      /* Eina_List in which to place the elements or lists */
      Eina_List *l;

      void *list_data;

      list = eina_list_append(list, eina_stringshare_add("Bertrand"));
      list = eina_list_append(list, eina_stringshare_add("Cedric"));
      list = eina_list_append(list, eina_stringshare_add("Nicolas"));
      list = eina_list_append(list, eina_stringshare_add("Vincent"));
      list = eina_list_append(list, eina_stringshare_add("Raoul"));
      list = eina_list_append(list, eina_stringshare_add("Fabien"));
      list = eina_list_append(list, eina_stringshare_add("Philippe"));
      list = eina_list_append(list, eina_stringshare_add("billiob"));

      for (l = list; l; l = eina_list_next(l)) {
          /* Printing the data returned by eina_list_data_get */
          printf("%s\n", (char*)eina_list_data_get(l));
      }

      EINA_LIST_FREE(list, list_data)
          eina_stringshare_del(list_data);

      return 0;
   }
  ```

- To move in a list, use the `eina_list_last()`, `eina_list_next()`, or `eina_list_prev()` functions to move to the last, next, or previous element in the list.

  The following example scrolls backwards starting from the end of the list:

  ```
  for (l = eina_list_last(list); l; l = eina_list_prev(l))
      printf("%s\n", (char*)eina_list_data_get(l));
  ```

- To count the list elements, use the `eina_list_count()` function. The function returns the number of items in a list.

  ```
  printf("List size: %d\n", eina_list_count(list));
  ```

- To iterate through an array, you can use various iterators:

  - To iterate over a list from the beginning to the end, use the `EINA_LIST_FOREACH` macro:

    - The first parameter is the list to iterate.
    - The second parameter is an `Eina_List *` to hold the current "List" (node).
    - The last parameter receives the current data during the run.

    The following example prints the data of each "List" (node) of the list:

    ```
    Eina_List *list = NULL;
    Eina_List *l;
    void *list_data;

    list = eina_list_append(list, "ls");
    list = eina_list_append(list, "top");
    list = eina_list_append(list, "rmdir");
    list = eina_list_append(list, "uname");

    EINA_LIST_FOREACH(list, l, list_data)
        printf("%s\n", (char*)list_data);

    eina_list_free(list);
    ```

  - To iterate from the last element to the first, use the `EINA_LIST_REVERSE_FOREACH` macro. It works similarly as `EINA_LIST_FOREACH()`.

  - To iterate over a list from the beginning to the end, you can also use the `EINA_LIST_FOREACH_SAFE` macro. It is called safe, because it stores the next "List" (node), so you can safely remove the current "List" (node) and continue the iteration.

    ```
    Eina_List *list;
    Eina_List *l;
    Eina_List *l_next;
    char *data;

    list = eina_list_append(list, "tizen");
    list = eina_list_append(list, "tizen");
    list = eina_list_append(list, "tizen");
    list = eina_list_append(list, "tizen");

    /* Using EINA_LIST_FOREACH_SAFE to free the elements that match "tizen" */

    EINA_LIST_FOREACH_SAFE(list, l, l_next, data) {
        if (strcmp(data, "tizen") == 0) {
            free(data);
            list = eina_list_remove_list(list, l);
        }
    }
    ```

  - To remove each list element while having access to the node's data, use the `EINA_LIST_FREE` macro. Pass the list and a pointer to hold the current data.

    ```
    Eina_List *list;
    char *data;

    /* List is filled */

    EINA_LIST_FREE(list, data)
        free(data);
    ```

### Using an Inline List

The `Eina_Inlist` is a special data type drawn to store nodes pointers in the same memory as data. This way the memory is less fragmented, but operations, such as sort and count, are slower. The `Eina_Inlist` has its own purpose, but if you do not understand what the purpose is, use the regular `Eina_List` instead.

The `Eina_Inlist` nodes can be part of a regular `Eina_List`, simply added with the `eina_list_append()` or `eina_list_prepend()` functions.

To use the inline list:

1. Define the structure of the data before creating the inline list:

   ```
   struct my_struct {
       EINA_INLIST;
       int a;
       int b;
   };
   ```

   The structure is composed of 2 integers, the real data, and the `EINA_INLIST` type which is composed of 3 pointers defining the inline list structure:

   - `Eina_Inlist * next`: next node
   - `Eina_Inlist * prev`: previous node
   - `Eina_Inlist * last`: last node

2. To create the inlist nodes, allocate the memory and use the `eina_inlist_append()` function:

   - The first parameter is the existing list head or `NULL` to create a new list.

     The following example passes `NULL` to create a new list.

   - The second parameter is the new list node, and it must not be `NULL`.

     You must use the `EINA_INLIST_GET()` macro to get the inlist object of the datastruct.

   ```
   struct my_struct *d;
   struct my_struct *cur;
   Eina_Inlist *list;
   Eina_Inlist *itr;
   Eina_Inlist *tmp;

   d = malloc(sizeof(*d));
   d->a = 1;
   d->b = 10;

   list = eina_inlist_append(NULL, EINA_INLIST_GET(d));
   ```

   Repeat this operation for every new node:

   ```
   d = malloc(sizeof(*d));
   d->a = 2;
   d->b = 20;
   list = eina_inlist_append(list, EINA_INLIST_GET(d));
   ```

3. To add data to the inline list:

   - Put data at the end of the inline list with the `eina_inlist_prepend()` function:

     ```
     d = malloc(sizeof(*d));
     d->a = 3;
     d->b = 30;
     list = eina_inlist_prepend(list, EINA_INLIST_GET(d));
     ```

   - Add a node before or after a given node with the `eina_inlist_prepend_relative()` and `eina_inlist_append_relative()` functions.

     In both functions, the first parameter is the target list, the second is the element you want to add, and the last is the reference element to place data after (in this case). Similarly as in a regular `Eina_List`, everything is a list, so the last parameter is an `Eina_Inlist` typed variable.

     ```
     d = malloc(sizeof(*d));
     d->a = 4;
     d->b = 40;
     list = eina_inlist_append_relative(list, EINA_INLIST_GET(d), list);
     ```

4. To sort and iterate an inline list, to find and move list elements, and to perform other inline list operations, see the [Inline List](../../../api/mobile/latest/group__Eina__Inline__List__Group.html) API.

5. When the inline list is no longer needed, destroy it by looping over the list to free each `EINA_INLIST` structure and the data using allocated memory. Use the `eina_inlist_remove()` function on each node.

   In the following example, the `EINA_INLIST_CONTAINER_GET()` macro returns the container object of an inlist (the `EINA_INLIST` of `my_struct`), and the list element is removed and the allocated memory of the container "object" is freed.

   ```
   while (list) {
       struct my_struct *aux = EINA_INLIST_CONTAINER_GET(list, struct my_struct);

       /* Remove the current list element */
       list = eina_inlist_remove(list, list);
       free(aux);
   }
   ```

## Generic Value

The `Eina_Value` object provides generic data storage and access, allowing you to store what you want in one single type of `Eina_Value`. It is meant for simple data types, providing uniform access and release functions, useful to exchange data preserving their types. The `Eina_Value` comes with predefined types for numbers, array, list, hash, blob, and structs, and it can convert between data types, including string.

The `Eina_Value` can handle the following types:

- `EINA_VALUE_TYPE_UCHAR`: unsigned char
- `EINA_VALUE_TYPE_USHORT`: unsigned short
- `EINA_VALUE_TYPE_UINT`: unsigned int
- `EINA_VALUE_TYPE_ULONG`: unsigned long
- `EINA_VALUE_TYPE_TIMESTAMP`: unsigned long used for timestamps
- `EINA_VALUE_TYPE_UINT64`: unsigned integer of 64 bits
- `EINA_VALUE_TYPE_CHAR`: char
- `EINA_VALUE_TYPE_SHORT`: short
- `EINA_VALUE_TYPE_INT`: int
- `EINA_VALUE_TYPE_LONG`: long
- `EINA_VALUE_TYPE_INT64`: integer of 64 bits
- `EINA_VALUE_TYPE_FLOAT`: float
- `EINA_VALUE_TYPE_DOUBLE`: double
- `EINA_VALUE_TYPE_STRINGSHARE`: stringshared string
- `EINA_VALUE_TYPE_STRING`: string
- `EINA_VALUE_TYPE_ARRAY`: array
- `EINA_VALUE_TYPE_LIST`: list
- `EINA_VALUE_TYPE_HASH`: hash
- `EINA_VALUE_TYPE_TIMEVAL`: 'struct timeval'
- `EINA_VALUE_TYPE_BLOB`: blob of bytes
- `EINA_VALUE_TYPE_STRUCT`: struct

To set up a generic value:

1. Declare the necessary variables:

   ```
   /* Eina_Value itself */
   Eina_Value v;
   /* Integer */
   int i;
   /* And char* */
   char *newstr;
   ```

2. To set up an `Eina_Value` for an integer, use the `eina_value_setup()` function. The first argument is the `Eina_Value` and the second is the type.

   ```
   eina_value_setup(&v, EINA_VALUE_TYPE_INT);
   ```

To manage the generic value:

- To set an integer, use the `eina_value_set()` function:

  ```
  eina_value_set(&v, 123);
  ```

- To get the value, use the `eina_value_get()` function. Pass the `Eina_Value` as the first argument, and a pointer to a variable to store the value (the target variable must have the same type as the `Eina_Value`).

  ```
  eina_value_get(&v, &i);
  printf("v=%d\n", i);
  ```

  The above example prints "v=123".

- To store an `Eina_List`, use the `Eina_Value` that corresponds to the `EINA_VALUE_TYPE_LIST` type.

- To create an `Eina_Value_List`, use the `eina_value_list_setup()` function. The function initializes a generic value storage of the list type. The first parameter is the "object" value, and the second one is the type (how to manage the stored list members).

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
