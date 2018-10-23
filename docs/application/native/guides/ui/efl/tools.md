# Tools

The Eina library provides a number of tools to help you when coding applications:

- Convert fast: Conversion from, for example, strings to integers and double
- Counter: Measures the number of calls and their time
- Error: Error identifiers
- File: File list and path split
- Lazy allocator: Manages item allocation
- Log: Full-featured logging system
- Magic: Provides runtime type checking
- [Memory Pool](#memory-pool): Abstraction for various memory allocators
- Module lists: Loads and shares modules using the `Eina_Module` standard
- Rectangle: Rectangle structure and standard manipulation methods
- [Safety Checks](#safety-checks): Extra checks that report unexpected conditions and can be disabled during compilation
- [String](#string): Set of functions that manage C strings

## String

When creating applications, you always need to manipulate strings. Use the following Eina functions for manipulating C strings:

- To split a string into an array of strings based on a delimiter that determines where the string is split, use the `eina_str_split()` function.

  The split is the most common string manipulation method. For example, if you have the `"Rasterman:Bluebugs:Tasn:Illogict:billiob:Puppet_Master"` string, and you want to print it in an easily readable format, you can split it using the ":" character as a delimiter.

  In the `eina_str_split()` function, the first parameter is the string to split, the second is the delimiter, and the third is the maximum number of strings to split the string into. If you set the third parameter to be smaller than 1, the function splits the string as many times as possible.

  The function returns a newly-allocated `NULL`-terminated array of strings, or `NULL`, if it fails to allocate the array. When no longer needed, free the memory allocated by the `eina_str_split()` function.

  ```
  char *nicks = "Rasterman:Bluebugs:Tasn:Illogict:billiob:Puppet_Master";
  char **result_arr;
  int i;

  /* Split the string with the ':' delimiter */
  result_arr = eina_str_split(nicks, ":", 0);
  /* Print the result */
  for (i = 0; result_arr[i]; i++)
      printf("Nick: %s\n", result_arr[i]);
  /* Free the memory */
  free(result_arr[0]);
  free(result_arr);
  ```

- To change a string to lowercase or uppercase, use the `eina_str_tolower()` and `eina_str_toupper()` functions. They modify the original string by changing the case for all characters in the string.

  ```
  char *str;
  /* Initialize the string */
  str = malloc(sizeof(char) * 4);
  strcpy(str, "bsd");
  /* Change the string to uppercase */
  eina_str_toupper((char **)&str);
  printf("%s\n", str);
  /* Change the string to lowercase */
  eina_str_tolower(&str);
  printf("%s\n", str);
  /* Free the memory */
  free(str);
  ```

- To join 2 strings of known length, use the `eina_str_join()` function. The first parameter is the buffer to store the result, the second is the size of the buffer, the third is the separator between the 2 strings, and the 2 final parameters are the stings to be joined.

  ```
  char *part1 = "Tizen powered by";
  char *part2 = "Enlightenment Foundation Libraries";
  char *res;
  size_t size;
  /* Calculate the string size + 1 for the delimiter */
  size = strlen(part1) + strlen(part2) + 1;
  /* Allocate memory for the result */
  res = malloc(sizeof(char) * size);
  /* Join the strings */
  eina_str_join(res, size, ' ', part1, part2);
  printf("%s\n", res);
  /* Free the memory */
  free(res);
  ```

- To check whether a string starts or ends with another string, use the `eina_str_has_prefix()` or `eina_str_has_suffix()` function. You can also check whether a string has a particular extension with the `eina_str_has_extension()` function.

  These functions return `EINA_TRUE` if the string contains the specified prefix, suffix, or extension, and `EINA_FALSE` if it does not.

  ```
  char *names = "Carsten;Cedric;Tom;Chidambar;Boris;Philippe";
  if (eina_str_has_prefix(names, "Carsten"))
      printf("String starts with 'Carsten'");
  if (eina_str_has_suffix(names, "Philippe"))
      printf("String ends with 'Philippe'");
  if (eina_str_has_extension(names, "philippe"))
      printf("String has extension 'philippe'");
  else
      printf("String does not have extension 'philippe'");
  ```

## Memory Pool

The `Eina_Mempool` tool provides the memory pool functionality. With a memory pool, you can preallocate fixed-size memory spaces for easy memory management.

The following memory pools are available:

- `buddy`
- `chained_pool`
- `ememoa_fixed` and `ememoa_unknown`
- `fixed_bitmap`
- `pass_through`
- `one_big`

## Safety Checks

Eina safety checks are a set of macros that can be used to check for parameters or values that must never occur. The concept is similar to the `assert()` function, but safety checks simply log the parameter or value and return, instead of aborting your program.

The following safety checks are available:

- `EINA_SAFETY_ON_NULL_RETURN(exp)`
- `EINA_SAFETY_ON_NULL_RETURN_VAL(exp, val)`
- `EINA_SAFETY_ON_NULL_GOTO(exp, label)`
- `EINA_SAFETY_ON_TRUE_RETURN(exp)`
- `EINA_SAFETY_ON_TRUE_RETURN_VAL(exp, val)`
- `EINA_SAFETY_ON_TRUE_GOTO(exp, label)`
- `EINA_SAFETY_ON_FALSE_RETURN(exp)`
- `EINA_SAFETY_ON_FALSE_RETURN_VAL(exp, val)`
- `EINA_SAFETY_ON_FALSE_GOTO(exp, label)`
- `EINA_ARG_NONNULL(...)`

The following examples show how to use the safety checks:

- To return if a variable is `NULL`, use the `EINA_SAFETY_ON_NULL_RETURN()` function. This macro calls `return` if the given parameter is `NULL`.

  ```
  Eina_Bool
  myfunction(char *param)
  {
      /* If the parameter is NULL, EINA_SAFETY_ON_NULL_RETURN calls "return" */
      EINA_SAFETY_ON_NULL_RETURN(param);

      printf("My param is: %s\n", param);

      return EINA_TRUE;
  }
  ```

- To return a specific value, use the `EINA_SAFETY_ON_NULL_RETURN_VAL()` function instead of the `EINA_SAFETY_ON_NULL_RETURN()` function. This macro returns a given value if the given parameter is `NULL`.

  ```
  Eina_Bool void
  myfunction(char *param)
  {
      /* If the parameter is NULL, return EINA_FALSE; */
      EINA_SAFETY_ON_NULL_RETURN_VAL(param, EINA_FALSE);
      printf("My param is: %s\n", param);

      return EINA_TRUE;
  }
  ```

- To call another function if a parameter is `NULL`, use the `EINA_SAFETY_ON_NULL_GOTO()` function. This macro works similarly to the `EINA_SAFETY_ON_NULL_RETURN()` function, except that it calls `goto` with the given function instead of `return`.

  ```
  static void
  isnullcb()
  {
      printf("The parameter is NULL\n");
  }

  Eina_Bool void
  myfunction(char *param)
  {
      /* If the parameter is NULL, call isnullcb() */
      EINA_SAFETY_ON_NULL_GOTO(param, isnullcb);
      printf("My param is: %s\n", param);

      return EINA_TRUE;
  }
  ```

Eina also provides macros that check whether a given value is `TRUE` or `FALSE`. For example:

- To call `return` if a given value is `TRUE`, use the `EINA_SAFETY_ON_TRUE_RETURN()` function.
- To call `goto` in a given function if a given value is `TRUE`, use the `EINA_SAFETY_ON_NULL_GOTO()` function.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
