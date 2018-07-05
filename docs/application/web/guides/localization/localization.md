# Localization

By localizing your application, you can ensure that your application works around the world in different locales.

This feature is supported in mobile and wearable applications only.

To localize a Tizen Web application:

1. Create a directory for each locale.

   Create a directory for each locale that has localized content under the `locales` directory in package root. The locale names are defined in the [W3C IANA Language Subtag Registry](http://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

   The Web Runtime loads the proper resource for the current locale according to the W3C widget using the following mark-up:

   ```
   ┬index.html
   └locales
     └en
       └language.js
     └ko
       └language.js
   ```

2. Create a common JS object for language strings.

   Define a global JS object in the resource file. In the following example, the JS object is `LANG_JSON_DATA`. This object defines the key-value pairs for localized strings.

   - `en/language.js`:
      ```
      LANG_JSON_DATA = {
         'hello': 'hello'
      }
      ```
   - `ko/language.js`:
      ```
      LANG_JSON_DATA = {
         'hello': '안녕'
      }
      ```

   "hello" is the key for the localized string, to be replaced by the value from the appropriate language.

3. Load language resources.

   To load language resources, add the `<script>` element containing the language resource file in your `index.html` file:

   ```
   <script src="language.js"></script>
   ```

   The Web Runtime loads the `language.js` file for the current locale and  you can use the defined string element to display localized content. For example:

   ```
   log('hello=' + LANG_JSON_DATA['hello']);
   ```

   > **Note**  
   > When the Web Runtime fails to find a file in a local folder, it searches for the file according to the procedure in the [W3C specification](https://www.w3.org/TR/widgets/#folder-based-localization-0).  
   > If the Web Runtime still fails to find a file in a local folder, it retrieves the folders that match the parent subtag, and prioritizes the files in the subfolders over the files in the local folders closer to the root of the widget package. If after all this, the Web Runtime still cannot find the file, an unexpected problem can occur.  
   > To avoid problems, leave a default file in the root folder.

   The following table lists the acceptable locale folder names.

   **Table: Locale folder names**

   | Language                        | Folder name |
   | ------------------------------- | ----------- |
   | Albanian                        | `sq-al`     |
   | Arabic                          | `ar-ae`     |
   | Armenian                        | `hy-am`     |
   | Assamese                        | `as-in`     |
   | Azerbaijani                     | `az-az`     |
   | Basque                          | `eu-es`     |
   | Bengali                         | `bn-in`     |
   | Bulgarian                       | `bg-bg`     |
   | Catalan                         | `ca-es`     |
   | Chinese Simplified (China)      | `zh-cn`     |
   | Chinese Traditional (Hong Kong) | `zh-hk`     |
   | Chinese Traditional (Taiwan)    | `zh-tw`     |
   | Croatian                        | `hr-hr`     |
   | Czech                           | `cs-cz`     |
   | Danish                          | `da-dk`     |
   | Dutch                           | `nl-nl`     |
   | Dutch (Belgium)                 | `nl-be`     |
   | English (UK)                    | `en-gb`     |
   | English (US)                    | `en-us`     |
   | English (Australia)             | `en-au`     |
   | English (Canada)                | `en-ca`     |
   | English (Ireland)               | `en-ie`     |
   | English (New Zealand)           | `en-nz`     |
   | English (Philippines)           | `en-ph`     |
   | English (South Africa)          | `en-za`     |
   | Estonian                        | `et-ee`     |
   | Farsi                           | `fa-ir`     |
   | Filipino                        | `tl-ph`     |
   | Finnish                         | `fi-fi`     |
   | French (Canada)                 | `fr-ca`     |
   | French (France)                 | `fr-fr`     |
   | French (Belgium)                | `fr-be`     |
   | French (Switzerland)            | `fr-ch`     |
   | Galician                        | `gl-es`     |
   | Georgian                        | `ka-ge`     |
   | German                          | `de-de`     |
   | German (Switzerland)            | `de-ch`     |
   | German (Austria)                | `de-at`     |
   | Greek                           | `el-gr`     |
   | Gujarati                        | `gu-in`     |
   | Hebrew                          | `he-il`     |
   | Hindi                           | `hi-in`     |
   | Hungarian                       | `hu-hu`     |
   | Icelandic                       | `is-is`     |
   | Indonesian                      | `id-id`     |
   | Irish                           | `ga-ie`     |
   | Italian                         | `it-it`     |
   | Japanese                        | `ja-jp`     |
   | Kannada                         | `kn-ca`     |
   | Kazakh                          | `kk-kz`     |
   | Khmer                           | `km-kh`     |
   | Korean                          | `ko-kr`     |
   | Lao                             | `lo-la`     |
   | Latvian                         | `lv-lv`     |
   | Lithuanian                      | `lt-lt`     |
   | Macedonian                      | `mk-mk`     |
   | Malay                           | `ms-mw`     |
   | Malayalam                       | `ml-my`     |
   | Marathi                         | `mr-in`     |
   | Myanmar                         | `my-mm`     |
   | Nepali                          | `ne-np`     |
   | Norwegian                       | `nb-no`     |
   | Odia                            | `or-in`     |
   | Polish                          | `pl-pl`     |
   | Portuguese (Brazil)             | `pt-br`     |
   | Portuguese (Portugal)           | `pt-pt`     |
   | Punjabi                         | `pa-pk`     |
   | Romanian                        | `ro-ro`     |
   | Russian                         | `ru-ru`     |
   | Serbian                         | `sr-rs`     |
   | Sinhala                         | `si-lk`     |
   | Slovakian                       | `sk-sk`     |
   | Slovenian                       | `sl-si`     |
   | Spanish (Spain)                 | `es-es`     |
   | Spanish (Latin America)         | `es-us`     |
   | Swedish                         | `sv-se`     |
   | Tamil                           | `ta-in`     |
   | Telugu                          | `te-in`     |
   | Thai                            | `th-th`     |
   | Turkish                         | `tr-tr`     |
   | Ukrainian                       | `uk-ua`     |
   | Urdu                            | `ur-pk`     |
   | Uzbekistan                      | `uz-uz`     |
   | Vietnamese                      | `vi-vn`     |

## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
