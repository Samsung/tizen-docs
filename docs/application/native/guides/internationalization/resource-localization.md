# Resource Localization


Tizen provides localized resources to make your application usable for different countries. The localization is based on the Internationalization API (in [mobile](../../api/mobile/latest/group__CAPI__I18N__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__I18N__MODULE.html) applications), which makes strings translatable and places them in `.po` (portable object) files.

> **Note**
>
> The `.po` files must be placed in the `res/po` directory of the application. The files can be edited using the [PO file editor](../../../tizen-studio/native-tools/po-file-editor.md) provided by the Tizen Studio.
>
> The `.po` file is compiled into a `.mo` file, and the `.mo` file name is defined using the project name that you define when you create the project in the Tizen Studio. The application ID is made based on the project name, and the framework finds the application `.mo` file based on the application ID.
>
> Be careful if you change the application ID in the Tizen manifest editor later, because the `.mo` file name is not automatically changed, and problems can occur when getting the string resources.

The application must load the proper resource set depending on the current device locale. If no matching resource set is found for the current locale, the default resource set is used.

To get the localized value of a string, use the **string KEY** shown in the PO file editor (the `msgid` field in the `.po` file), with the `_()` function (for example, `_(<msgid>)`). The underlying implementation calls the `i18n_get_text()` function to retrieve the localized value:

```
char *hello_text = i18n_get_text("Hello");
```

The `hello_text` variable is set to the localized text for the "Hello" string key (`msgid`) for the current device locale.

When the user changes the device language setting, the text in the application changes to the new language.

## Marking Text Parts Translatable

The most common way to use a translation in your application strings involves the `elm_object_translatable_text_set()` and `elm_object_item_translatable_text_set()` functions. They set the untranslated string for the "default" part of the given `Evas_Object` or `Elm_Object_Item`, and mark the string as translatable.

To set the text for a "non-default" part as translatable, use the `elm_object_translatable_part_text_set()` and `elm_object_item_translatable_part_text_set()` functions.

> **Note**
>
> Always provide the untranslated string as a parameter to the above functions. The EFL triggers the translation itself and re-translates the string automatically, if the system language changes.

## Translating Texts Directly

The process of marking texts as translatable is not applicable in some cases. For example, it does not work if you are populating a genlist, if you need plurals in the translation, or if you want to do something else than put the translation in an Elementary UI component.

To retrieve the translation for a given text, use the `i18n_get_text()` function. The function takes as input a string (the `msgid` field in the `.po` file), and returns the translation (the corresponding `msgstr` field in the `.po` file).

```
char *i18n_get_text(const char *msgid);
```

> **Note**
>
> Do not modify or free the return value of the `i18n_get_text()` function. It is statically allocated.

The following example shows how you can define the text translation for a genlist item, when the "Some Text" string is defined as a `msgid` field in the `.po` file:

```
#include "app_i18n.h"
static char*
_genlist_text_get(void *data, Evas_Object *obj, const char *part)
{
    return strdup(i18n_get_text("Some Text"));
}
```

### Plurals

Plurals are handled through the `ngettext()` function, with the untranslated text (the `msgid` field) as the first parameter, the plural form of the text as the second parameter, and the quantity as the last parameter. (In English, 1 is singular and anything else is plural.)

For example, the `.po` file for French can contain the following lines (for one plural form):

```
msgid "%d Comment"
msgid_plural "%d Comments"
msgstr[0] "%d commentaire"
msgstr[1] "%d commentaires"
```

The following example shows a situation where a language has several plural forms. For example, the `.po` file for Polish can contain the following lines:

```
msgid "%d Comment"
msgid_plural "%d Comments"
msgstr[0] "%d Komentarz"
msgstr[1] "%d Komentarze"
msgstr[2] "%d Komentarzy"
```

The index values in the `msgstr` field are defined in system-wide settings. The ones for Polish are defined in the following example. They mean that there are 3 forms (including singular). The index is 0 (singular), if the given integer n is 1. If `(n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 | | n % 100 >= 20)`, the index is 1, otherwise it is 2.

```
"Plural-Forms: nplurals = 3; plural = n = = 1 ? 0 : n%10> = 2 && n%10< = 4 && (n%100<10 | | n%100> = 20) ? 1 : 2;\n"
```

### Language Changes at Runtime

The user can change the system language settings at any time. When that is done, the framework notifies the application, which changes the language used in the Elementary. The UI components receive a `language,changed` signal (a typical smart event signal), and reset their texts.

To handle the framework language change event in the application, add an event handler for it, and use the `elm_language_set()` function in the event handler code to trigger the emission of the `language,changed` signal:

```
static void
_app_language_changed(void *data)
{
    char *language;
    /* Retrieve the current system language */
    system_settings_get_value_string(SYSTEM_SETTINGS_KEY_LOCALE_LANGUAGE, &language);
    /* Set the language in Elementary */
    elm_language_set(language);
    free(language);
}
int
main(int argc, char *argv[])
{
    ui_app_add_event_handler(&handlers[APP_EVENT_LANGUAGE_CHANGED],
                             APP_EVENT_LANGUAGE_CHANGED, _app_language_changed, &ad);
}
```

## Extracting Messages for Translation

The `xgettext` tool extracts strings to translate to a `.pot` file (a PO template), while the `msgmerge` tool maintains the existing `.po` files. The typical workflow is as follows:

- Run the `xgettext` tool once to generate a `.pot` file.

- When adding a new translation language, copy the `.pot` file content to the `<locale>.po` file and translate that file.

  New runs of the `xgettext` tool update the existing `.pot` file and the `msgmerge` tools updates the `.po` files.

The following examples show typical calls to the tools:

- `xgettext`:

    ```
    xgettext --directory = src --output-dir = res/po --keyword = _ --keyword = N_
             --keyword = elm_object_translatable_text_set:2 --keyword = elm_object_item_translatable_text_set:2
             --add-comments = --from-code = utf-8 --foreign-use
    ```

The above call extracts all strings that are used inside the `_()` function (optional shorthand for `i18n_get_text()`), uses UTF-8 as the encoding, and adds comments right before the strings to the output files.

- `msgmerge`:

    ```
    msgmerge --width=120 --update res/po/fr.po res/po/ref.pot
    ```

## Resource Localization Tips

Take advantage of the following tips to smoothly internationalize your application:

- Make no assumptions about languages

  Languages vary greatly and even if you know several of them, do not assume there is any common logic to them all. For example, with English typography, no character must appear before colons and semicolons (':' and ';'). However, with French typography, there must be "espace fine insécable", that is, a non-breakable space (HTML's &nbsp;) that is narrower than regular spaces.

  To prevent problems with typography, avoid breaking your strings into multiple parts, if possible. The following example results in incorrect punctuation:

  ```
  snprintf(buf, some_size, "%s: %s", i18n_get_text(error), i18n_get_text(reason));
  ```

  Instead, use a single string and let the translators manage the punctuation:

  ```
  snprintf(buf, some_size, i18n_get_text("%s: %s"), i18n_get_text(error), i18n_get_text(reason));
  ```

- Remember that translations have different lengths

  Depending on the language, the translation has a different length on the screen. In some cases, a language has a shorter construct than another. In other cases, a language can have a word for a specific concept, while another does not and requires a circumlocution (designating something by using several words).

- Do not commit the `.po` file, if only line indicators have changed

    A translation block can look like this:

    ```
    #: some_file.c:43 another_file.c:41
    msgid "Click Here"
    msgstr "Cliquez ici"
    ```

	If you insert a new line at the top of the `some_file.c` file, the line indicator changes to look like this:

    ```
    #: some_file.c:44 another_file.c:41
    ```

	In non-trivial projects, such changes often happen. If you use source control and commit such changes even though no actual translation changes were made, each commit probably contains a change to the `.po` files. This hampers readability of the change history, and if several people are working in parallel and need to merge their changes, this creates extensive merge conflicts each time.

    For source control, only commit changes to `.po` files when there are actual translation changes, not because line comments have changed.

- Use `_()` as shorthand for `i18n_get_text()`

    Since the `i18n_get_text()` function calls are very common, the Tizen Studio provides an abbreviation for this function. You can call it simply with `_()`.

- Sort properly with `strcoll()`

    The `strcoll()` function is a string comparison tailored for sorting data for display. It works the same way as `strcmp()`, but sorts the data according to the current locale settings.

    Use the `strcoll()` function as the comparison function for sorting the data set you are using.

- Help the translators in their work

    The PO file-based translation system is a common one and is likely to be known to translators. To provide the necessary information to help the translators in their work, it can be enough to mention its name (`gettext`). There is extensive additional documentation as well as questions and answers available on the Internet.

    Do not hesitate to put comments in your code above the strings to be translated, since they can be extracted along with the strings and saved in the `.po` files for the translator to see.

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
