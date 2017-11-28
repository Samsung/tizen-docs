# i18n
##Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

You can generate flexible number or date format patterns, format and parse dates and numbers for any locale, and manage time zones. The i18n API is implemented by using the ICU library.

The main features of the i18n API include:

- Managing text and strings

  You can [handle general Unicode strings](#ustring) with Ustring and [find the location of boundaries in text](#ubrk) with Ubrk.

  For search and access, you can [perform locale-sensitive string comparison](#ucoll) with Ucollator to build searching and sorting routines, [search language-sensitive text](#usearch) based on the Ucollator comparison rules with Usearch, and get low-level [access to the Unicode Character Database](#uchar) with Uchar.

  You can manage multiple strings by [creating and obtaining enumerations](#uenumeration) out of a given set of strings with Uenumeration, or [managing a set of Unicode characters and multicharacter strings](#uset) with Uset.

  With Unormalization, you can perform [standard Unicode normalization](#unormal).

- Managing the calendar and dates

  With Udatepg, you can [generate date format patterns](#udatepg), such as "yy-MM-dd". You can also handle various conversions: you can [convert between a Udate object and a set of integer fields](#ucalendar) with Ucalendar, and you can [convert dates and times](#udate) from their internal representations to textual form and back with Udate.

- Managing numbers

  You can [format and parse numbers](#unumber) for any locale with Unumber.

- Managing locales and time zones

  You can use the Ulocale functions to [tailor information according to a specific geographical, cultural, or political region](#ulocale). With the Timezone functions, you can [get the time zone name, ID, DST settings, raw offset, and region code](#tmz).

- Retrieving the ICU version

  You can [retrieve the currently-used version of the ICU library](#manage_version) with Uversion.

- Iterating through strings

  You can [iterate through strings](#uchar_iter), in a safe way, with UCharIter.

**Note**
The Uversion and UCharIter APIs are supported since Tizen 4.0.

## Location Boundaries with Ubrk

The Ubrk API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UBRK__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UBRK__MODULE.html) applications) is used to [find the location of boundaries in text](#manage_ubrk). The `i18n_ubreak_iterator_h` handle maintains a current position and scans over the text returning the index of characters where the boundaries occur.

The following boundary analyzing methods are available:

- Line boundary analysis determines where a text string can be broken when line-wrapping. The mechanism correctly handles punctuation and hyphenated words.
- Sentence boundary analysis allows selection with correct interpretation of periods within numbers and abbreviations, and trailing punctuation marks, such as quotation marks and parentheses.
- Word boundary analysis is used by search and replace functions, as well as within text editing applications that allow the user to select words with a double-click. Word selection provides correct interpretation of punctuation marks within and following words. Characters that are not part of a word, such as symbols or punctuation marks, have word-breaks on both sides.
- Character boundary analysis identifies the boundaries of Extended Grapheme Clusters, which are groupings of codepoints that must be treated as character-like units for many text operations. For more information on grapheme clusters and guidelines on their use, see [Unicode Standard Annex #29, Unicode Text Segmentation](http://www.unicode.org/reports/tr29/tr29-21.html).
- Title boundary analysis locates all positions, typically starts of words, that must be set to Title Case when title casing the text.
- The text boundary positions are found according to the rules described in [Unicode Standard Annex #29, Unicode Text Segmentation](http://www.unicode.org/reports/tr29/tr29-21.html), and [Unicode Standard Annex #14, Unicode Line Breaking Algorithm](http://www.unicode.org/reports/tr14/tr14-30.html).

## Calendar Dates with Ucalendar

The Ucalendar API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html) applications) is used for [converting between a Udate object and a set of integer fields](#dates), such as `I18N_UCALENDAR_YEAR`, `I18N_UCALENDAR_MONTH`, `I18N_UCALENDAR_DAY`, and `I18N_UCALENDAR_HOUR`. A [Udate](#udate) object represents a specific instant in time with one millisecond precision.

The types of Ucalendar interpret a Udate according to the rules of a specific calendar system, such as the Gregorian or traditional system.

A Ucalendar object can produce all the time field values needed to implement the date-time formatting for a particular language and calendar style (for example, Japanese-Gregorian, Japanese-Traditional).

**Table: Available calendar field combinations**

| Date information to be determined        | Field combination                        |
| ---------------------------------------- | ---------------------------------------- |
| Day                                      | `I18N_UCALENDAR_MONTH + I18N_UCALENDAR_DAY_OF_MONTH` |
| Day| `I18N_UCALENDAR_MONTH + I18N_UCALENDAR_WEEK_OF_MONTH + I18N_UCALENDAR_DAY_OF_WEEK` |                                          
| Day| `I18N_UCALENDAR_MONTH + I18N_UCALENDAR_DAY_OF_WEEK_IN_MONTH + I18N_UCALENDAR_DAY_OF_WEEK` |                                          
| Day| `I18N_UCALENDAR_DAY_OF_YEAR`             |                                          
| Day| `I18N_UCALENDAR_DAY_OF_WEEK + I18N_UCALENDAR_WEEK_OF_YEAR` |                                          
| Time of day                              | `I18N_UCALENDAR_HOUR_OF_DAY`             |
| Time of day | `I18N_UCALENDAR_AM_PM + I18N_UCALENDAR_HOUR` |                                          

**Note**
For some non-Gregorian calendars, different fields are necessary for complete disambiguation. For example, a full specification of the historical Arabic astronomical calendar requires the year, month, day-of-month and day-of-week in some cases.

When computing a Udate from the time fields, 2 special circumstances can arise. The information can be insufficient to compute the Udate (you have only the year and the month, but not the day of the month), or the information can be inconsistent (such as "Tuesday, July 15, 1996" even though July 15, 1996 is actually a Monday).

- **Insufficient information**The calendar uses the default information to specify the missing fields. This can vary by calendar: for the Gregorian calendar, the default for a field is the same as that of the start of the epoch, such as `I18N_UCALENDAR_YEAR = 1970`, `I18N_UCALENDAR_MONTH = JANUARY`, `I18N_UCALENDAR_DATE = 1`.
- **Inconsistent information**If the fields conflict, the calendar prefers the most recently set fields. For example, when determining the day, the calendar looks for one of the following field combinations listed in the following table. The most recent combination, as determined by the most recently set single field, is used.

## Unicode Character Management with Uchar

The Uchar API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html) applications) provides low-level access to the Unicode Character Database.

Unicode assigns each code point (not only the assigned character) values for several properties. Most of them are simple boolean flags, or constants from a small enumerated list. For some properties, values are strings or other relatively more complex types.

For more information, see [About the Unicode Character Database](http://www.unicode.org/ucd/) and [ICU User Guide chapter on Properties](http://icu-project.org/userguide/properties.html).

The following table describes the details of script codes that you can get using the `i18n_uchar_get_int_property_value()` function.

**Table: Script codes**

| Value | Code | English name                             | Value | Code | English name                             |
| ----- | ---- | ---------------------------------------- | ----- | ---- | ---------------------------------------- |
| 0     | Zyyy | Code for undetermined script             | 80    | Latf | Latin (Fraktur variant)                  |
| 1     | Zinh | Code for inherited script                | 81    | Latg | Latin (Gaelic variant)                   |
| 2     | Arab | Arabic                                   | 82    | Lepc | Lepcha (Rong)                            |
| 3     | Armn | Armenian                                 | 83    | Lina | LinearA                                  |
| 4     | Beng | Bengali                                  | 84    | Mand | Mandaic, Mandaean                        |
| 5     | Bopo | Bopomofo                                 | 85    | Maya | Mayan hieroglyphs                        |
| 6     | Cher | Cherokee                                 | 86    | Mero | Meroitic hieroglyphs                     |
| 7     | Copt | Coptic                                   | 87    | Nkoo | N’Ko                                     |
| 8     | Cyrl | Cyrillic                                 | 88    | Orkh | Old Turkic, Orkhon Runic                 |
| 9     | Dsrt | Deseret (Mormon)                         | 89    | Perm | Old Permic                               |
| 10    | Deva | Devanagari (Nagari)                      | 90    | Phag | Phags-pa                                 |
| 11    | Ethi | Ethiopic (Geʻez)                         | 91    | Phnx | Phoenician                               |
| 12    | Geor | Georgian (Mkhedruli)                     | 92    | Plrd | Miao (Pollard)                           |
| 13    | Goth | Gothic                                   | 93    | Roro | Rongorongo                               |
| 14    | Grek | Greek                                    | 94    | Sara | Sarati                                   |
| 15    | Gujr | Gujarati                                 | 95    | Syre | Syriac (Estrangelo variant)              |
| 16    | Guru | Gurmukhi                                 | 96    | Syrj | Syriac (Western variant)                 |
| 17    | Hani | Han (Hanzi, Kanji, Hanja)                | 97    | Syrn | Syriac (Eastern variant)                 |
| 18    | Hang | Hangul (Hangŭl, Hangeul)                 | 98    | Teng | Tengwar                                  |
| 19    | Hebr | Hebrew                                   | 99    | Vaii | Vai                                      |
| 20    | Hira | Hiragana                                 | 100   | Visp | Visible Speech                           |
| 21    | Knda | Kannada                                  | 101   | Xsux | Cuneiform, Sumero-Akkadian               |
| 22    | Kana | Katakana                                 | 102   | Zxxx | Code for unwritten documents             |
| 23    | Khmr | Khmer                                    | 103   | Zzzz | Code for uncoded script                  |
| 24    | Laoo | Lao                                      | 104   | Cari | Carian                                   |
| 25    | Latn | Latin                                    | 105   | Jpan | Japanese (alias for Han+Hiragana+Katakana) |
| 26    | Mlym | Malayalam                                | 106   | Lana | TaiTham (Lanna)                          |
| 27    | Mong | Mongolian                                | 107   | Lyci | Lycian                                   |
| 28    | Mymr | Myanmar (Burmese)                        | 108   | Lydi | Lydian                                   |
| 29    | Ogam | Ogham                                    | 109   | Olck | Ol Chiki (Ol Cemet’, Ol Santali)         |
| 30    | Ital | Old Italic (Etruscan, Oscan)             | 110   | Rjng | Rejang (Redjang, Kaganga)                |
| 31    | Orya | Oriya                                    | 111   | Saur | Saurashtra                               |
| 32    | Runr | Runic                                    | 112   | Sgnw | SignWriting                              |
| 33    | Sinh | Sinhala                                  | 113   | Sund | Sundanese                                |
| 34    | Syrc | Syriac                                   | 114   | Moon | Moon (Mooncode, Moonscript, Moontype)    |
| 35    | Taml | Tamil                                    | 115   | Mtei | Meitei Mayek (Meithei, Meetei)           |
| 36    | Telu | Telugu                                   | 116   | Armi | Imperial Aramaic                         |
| 37    | Thaa | Thaana                                   | 117   | Avst | Avestan                                  |
| 38    | Thai | Thai                                     | 118   | Cakm | Chakma                                   |
| 39    | Tibt | Tibetan                                  | 119   | Kore | Korean (alias for Hangul+Han)            |
| 40    | Cans | Unified Canadian Aboriginal Syllabics    | 120   | Kthi | Kaithi                                   |
| 41    | Yiii | Yi                                       | 121   | Mani | Manichaean                               |
| 42    | Tglg | Tagalog (Baybayin, Alibata)              | 122   | Phli | Inscriptional Pahlavi                    |
| 43    | Hano | Hanunoo (Hanunoo)                        | 123   | Phlp | Psalter Pahlavi                          |
| 44    | Buhd | Buhid                                    | 124   | Phlv | Book Pahlavi                             |
| 45    | Tagb | Tagbanwa                                 | 125   | Prti | Inscriptional Parthian                   |
| 46    | Brai | Braille                                  | 126   | Samr | Samaritan                                |
| 47    | Cprt | Cypriot                                  | 127   | Tavt | TaiViet                                  |
| 48    | Limb | Limbu                                    | 128   | Zmth | Mathematical notation                    |
| 49    | Linb | LinearB                                  | 129   | Zsym | Symbols                                  |
| 50    | Osma | Osmanya                                  | 130   | Bamu | Bamum                                    |
| 51    | Shaw | Shavian (Shaw)                           | 131   | Lisu | Lisu (Fraser)                            |
| 52    | Tale | TaiLe                                    | 132   | Nkgb | Nakhi Geba ('Na-'Khi ²Ggŏ-¹baw, Naxi Geba) |
| 53    | Ugar | Ugaritic                                 | 133   | Sarb | Old South Arabian                        |
| 54    | Hrkt | Japanese syllabaries (alias for Hiragana+Katakana) | 134   | Bass | BassaVah                                 |
| 55    | Bugi | Buginese                                 | 135   | Dupl | Duployan shorthand, Duployan stenography |
| 56    | Glag | Glagolitic                               | 136   | Elba | Elbasan                                  |
| 57    | Khar | Kharoshthi                               | 137   | Gran | Grantha                                  |
| 58    | Sylo | Syloti Nagri                             | 138   | Kpel | Kpelle                                   |
| 59    | Talu | New Tai Lue                              | 139   | Loma | Loma                                     |
| 60    | Tfng | Tifinagh (Berber)                        | 140   | Mend | Mende Kikakui                            |
| 61    | Xpeo | Old Persian                              | 141   | Merc | Meroitic Cursive                         |
| 62    | Bali | Balinese                                 | 142   | Narb | Old North Arabian (Ancient North Arabian) |
| 63    | Batk | Batak                                    | 143   | Nbat | Nabataean                                |
| 64    | Blis | Blissymbols                              | 144   | Palm | Palmyrene                                |
| 65    | Brah | Brahmi                                   | 145   | Sind | Khudawadi, Sindhi                        |
| 66    | Cham | Cham                                     | 146   | Wara | Warang Citi (Varang Kshiti)              |
| 67    | Cirt | Cirth                                    | 147   | Afak | Afaka                                    |
| 68    | Cyrs | Cyrillic (Old Church Slavonic variant)   | 148   | Jurc | Jurchen                                  |
| 69    | Egyd | Egyptian demotic                         | 149   | Mroo | Mro, Mru                                 |
| 70    | Egyh | Egyptian hieratic                        | 150   | Nshu | Nushu                                    |
| 71    | Egyp | Egyptian hieroglyphs                     | 151   | Shrd | Sharada, Śāradā                          |
| 72    | Geok | Khutsuri (Asomtavruli and Nuskhuri)      | 152   | Sora | Sora Sompeng                             |
| 73    | Hans | Han (Simplified variant)                 | 153   | Takr | Takri, Ṭākrī, Ṭāṅkrī                     |
| 74    | Hant | Han (Traditional variant)                | 154   | Tang | Tangut                                   |
| 75    | Hmng | Pahawh Hmong                             | 155   | Wole | Woleai                                   |
| 76    | Hung | Old Hungarian (Hungarian Runic)          | 156   | Hluw | Anatolian hieroglyphs (Luwian hieroglyphs, Hittite hieroglyphs) |
| 77    | Inds | Indus (Harappan)                         | 157   | Khoj | Khojki                                   |
| 78    | Java | Javanese                                 | 158   | Tirh | Tirhuta                                  |
| 79    | Kali | KayahLi                                  | -1    |      | Invalid code                             |

Since Tizen 4.0, you can also check for specific Unicode character properties, retrieve alternate representations of the same character, such as uppercase and lowercase, and get the name for a specific character.

To check whether a character is in a specific character class, use the `i18n_uchar_is_xxx()` function corresponding to the binary property in the following table.

**Table: Binary properties**

| Binary property   | Description                              |
| ----------------- | ---------------------------------------- |
| `alnum`           | Alphanumeric characters (letters and digits) |
| `alpha`           | Alphabetic characters                    |
| `blank`           | Horizontal space characters. This category includes tab characters and space separators, but excludes zero-width spaces. |
| `control`         | Control characters, such as backspace, tab, and escape |
| `digit`           | Decimal digits                           |
| `graph`           | Graphic characters. This category includes all printable characters, excluding spaces. |
| `java_space_char` | Separator characters or non-breaking space. The same characters are detected by the `isSpaceChar()` function in Java. |
| `lower`           | Lowercase characters                     |
| `printable`       | Non-control characters                   |
| `punct`           | Punctuation characters                   |
| `space`           | Space characters. The category includes separators, whitespace ISO controls, and non-breaking spaces. |
| `title`           | Titlecase characters                     |
| `upper`           | Uppercase characters                     |
| `whitespace`      | Separator characters or whitespace ISO control characters, excluding non-breaking space. The same characters are detected by the `isWhitespace()` function in Java. |
| `white_space`     | Characters with the Unicode `White_Space` property. The category includes most separators and whitespace ISO controls, including non-breaking spaces, but excludes IS1 to IS4 control characters and zero-width spaces. |
| `xdigit`          | Hexadecimal digits                       |

You can retrieve alternate representations of Unicode characters, such as the upper- or lowercase form, using the `i18n_uchar_to_xxx()` functions, or perform case folding using the `i18n_uchar_fold_case()` function.

For more information on case mapping, see the [ICU User Guide chapter on Case Mappings](http://userguide.icu-project.org/transforms/casemappings).

## String Comparison with Ucollator

The Ucollator API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCOLLATOR__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCOLLATOR__MODULE.html) applications) performs locale-sensitive string comparison. It builds searching and sorting routines for natural language text and provides correct sorting orders for most supported locales. If specific data for a locale is not available, the order eventually falls back to the [CLDR root sort order](http://www.unicode.org/reports/tr35/tr35-31/tr35-collation.html#Root_Collation). The sorting order can be customized by providing your own set of rules. For more information, see the [ICU Collation Customization](http://userguide.icu-project.org/collation/customization) section of the User Guide.

## Date Formats with Udate

The Udate API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UDATE__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UDATE__MODULE.html) applications) consists of functions that convert dates and times from their internal representations to textual form and back again in a language-independent manner. Converting from the internal representation (milliseconds since midnight, January 1, 1970) to text is known as formatting, and converting from text to milliseconds is known as parsing. Tizen currently defines only one concrete handle (`i18n_udate_format_h`), which can handle practically all normal date formatting and parsing actions.

The Udate format helps you to format and parse dates for any locale. Your code can be completely independent of the locale conventions for months, days of the week, or even the lunar or solar calendar format.

You can pass in different options for the arguments for date and time style to control the length of the result; you can select from `SHORT`, `MEDIUM`, `LONG`, and `FULL`. The exact result depends on the locale.

- `I18N_UDATE_SHORT` is completely numeric, such as 12/13/52 or 3:30pm
- `I18N_UDATE_MEDIUM` is longer, such as Jan 12, 1952
- `I18N_UDATE_LONG` is longer, such as January 12, 1952 or 3:30:32pm
- `I18N_UDATE_FULL` is completely specified, such as Tuesday, April 12, 1952 AD or 3:30:42pm PST.

### Date and Time Patterns

The date and time formats are specified by the `date and time pattern` strings. Within the date and time pattern strings, all unquoted ASCII letters (A-Z and a-z) are reserved as pattern letters representing calendar fields. The `i18n_udate_format_h` handle supports the date and time formatting algorithm and pattern letters defined by the [Unicode Technical Standard #35, Unicode Locale Data Markup Language (LDML)](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Date_Field_Symbol_Table). It is further documented in the [ICU User Guide](https://sites.google.com/site/icuprojectuserguide/formatparse/datetime?pli=1#TOC-Date-Field-Symbol-Table).

## Date Format Patterns with Udatepg

The Udatepg API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UDATEPG__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UDATEPG__MODULE.html) applications) enables flexible generation of date format patterns, such as "yy-MM-dd". The user can build up the generator by adding successive patterns. After this, a query can be made using a pattern that includes only the desired fields and lengths. The generator returns the a pattern that is most similar to it.

The main method is the `i18n_udatepg_get_best_pattern()` function, since normally the Udatepg API is prebuilt with data from a particular locale. However, generators can be built directly from other data as well.

## Enumeration Management with Uenumeration

The Uenumeration API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UENUMERATION__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UENUMERATION__MODULE.html) applications) enables you to [create an enumeration object](#uenum) out of a given set of strings. The object can be created out of an array of `const char*` strings or an array of `i18n_uchar*` strings.

The enumeration object enables navigation through the enumeration values, with the use of the `i18n_uenumeration_next()` or `i18n_uenumeration_unext()` function (depending on the type used for creating the enumeration object), and with the `i18n_uenumeration_reset()` function.

You can get the number of values stored in the enumeration object with the `i18n_uenumeration_count()` function.

## Locale-sensitive Operations with Ulocale

The Ulocale API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__ULOCALE__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__ULOCALE__MODULE.html) applications) represents a specific geographical, political, or cultural region. Locale-sensitive operations [use the Ulocale functions to tailor information](#locales) for the user. For example, displaying a number is a locale-sensitive operation. The number must be formatted according to the customs and conventions of the user's native country, region, or culture.

You create a locale with one of the following options. Each component is separated by an underscore in the locale string.

- `newLanguage`A valid [ISO language code](http://www.loc.gov/standards/iso639-2/php/code_list.php) (lower-case 2-letter code as defined by the ISO-639 standard).
- `newLanguage + newCountry`A valid ISO language code and an additional [ISO country code](http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html).
- `newLanguage + newCountry + newVariant`A valid ISO language code, ISO country code, and additional information on the variant. The variant codes are vendor and browser-specific. For example, use `WIN` for Windows, `MAC` for Macintosh, and `POSIX` for POSIX. Where there are 2 variants, separate them with an underscore, and put the most important one first. For example, a Traditional Spanish collation might be referenced, with `ES`, `ES`, `Traditional_WIN`.

Because a locale is simply an identifier for a region, no validity check is performed when you specify a locale. If you want to see whether particular resources are available for the locale you asked for, you must query those resources.

Once you have specified a locale you can query it for information about itself. Use `i18n_ulocale_get_language()` to get the ISO Language Code. You can use `i18n_ulocale_get_display_name()` to get the name of the language suitable for display to the user.

## Unicode Normalization with Unormalization

The Unicode normalization API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UNORMALIZATION__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UNORMALIZATION__MODULE.html) applications) is for the standard Unicode normalization. All instances of `i18n_unormalizer_s` are unmodifiable and immutable. Instances returned by `i18n_unormalization_get_instance()` are singletons that must not be deleted by the caller.

## Number Formats with Unumber

The Unumber API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UNUMBER__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UNUMBER__MODULE.html) applications) helps you to [format and parse numbers for any locale](#numbers). Your code can be completely independent of the locale conventions for decimal points, thousands-separators, or even the particular decimal digits used, or whether the number format is even decimal. There are different number format styles like decimal, currency, percent and spellout.

## Text Search with Usearch

The Usearch API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__USEARCH__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__USEARCH__MODULE.html) applications) provides language-sensitive text searching based on the comparison rules defined in a Ucollator data struct. This ensures that language eccentricity can be handled. For example, for the German collator, characters ß and SS are matched if case is chosen to be ignored. That is why it can be important to pass a locale when creating the usearch with the `i18n_usearch_create_new()` function.

## Character and String Management with Uset

Uset is a mutable [set of Unicode characters and multicharacter strings that you can manage](#manage_uset). The sets represent character classes used in regular expressions. A character specifies a subset of the Unicode code points. The legal code points are U+0000 to U+10FFFF, inclusive.

The set supports 2 functions:

- The operand function allows the caller to modify the value of the set. The operand function works similarly to the boolean logic: a boolean OR is implemented by add, a boolean AND is implemented by retain, a boolean XOR is implemented by a complement taking an argument, and a boolean NOT is implemented by a complement with no argument. In terms of traditional set theory function names, add is a union, retain is an intersection, remove is an asymmetric difference, and complement with no argument is a set complement with respect to the superset range `MIN_VALUE-MAX_VALUE`.
- The `i18n_uset_apply_pattern()` or `i18n_uset_to_pattern()` function. Unlike the functions that add characters or categories, and control the logic of the set, the `i18n_uset_apply_pattern()` function sets all attributes of a set at once, based on a string pattern.

### Pattern Syntax

Patterns are accepted by the `i18n_uset_create_pattern()`, `i18n_uset_create_pattern_options()`, and `i18n_uset_apply_pattern()` functions and returned by the `i18n_uset_to_pattern()` function. The patterns follow a syntax similar to that employed by version 8 regular expression character classes.

**Table: Examples of simple pattern syntaxes**

| Pattern       | Description                              |
| ------------- | ---------------------------------------- |
| `[]`          | No characters                            |
| `[a]`         | Character 'a'                            |
| `[ae]`        | Characters 'a' and 'e'                   |
| `[a-e]`       | Characters 'a' through 'e' inclusive, in Unicode code point order |
| `[\u4E01]`    | Character U+4E01                         |
| `[a{ab}{ac}]` | Character 'a' and the multicharacter strings 'ab' and 'ac' |
| `[\p{Lu}]`    | All characters in the general category 'uppercase letter' |

Any character can be preceded by a backslash in order to remove any special meaning. Whitespace characters are ignored, unless they are escaped.

Property patterns specify a set of characters having a certain property as defined by the Unicode standard. Both the POSIX-like `[:Lu:]` and the Perl-like syntax `\\p{Lu}` are recognized.

Patterns specify individual characters, ranges of characters, and Unicode property sets. When the elements are concatenated, they specify their union. To complement a set, place a '^' immediately after the opening '['. Property patterns are inverted by modifying their delimiters, `[:^foo]` and `\\P{foo}`. In any other location, '^' has no special meaning.

Ranges are indicated by placing a '-' between 2 characters, as in "a-z". This specifies the range of all characters from the left to the right, in Unicode order. If the left character is greater than or equal to the right character, it is a syntax error. If a '-' occurs as the first character after the opening '[' or '[^', or if it occurs as the last character before the closing ']', it is taken as a literal. This means that `[a\-b]`, `[-ab]`, and `[ab-]` all indicate the same set of 3 characters, 'a', 'b', and '-'.

Sets can be intersected using the '&' operator or the asymmetric set difference can be taken using the '-' operator. For example, `[[:L:]&[\\u0000-\\u0FFF]]` indicates the set of all Unicode letters with values less than 4096. Operators ('&' and '|') have equal precedence and bind left-to-right. This means that `[[:L:]-[a-z]-[\\u0100-\\u01FF]]` is equivalent to `[[[:L:]-[a-z]]-[\\u0100-\\u01FF]]`. This only really matters for difference; intersection is commutative.

**Table: Examples of set syntaxes**

| Set                   | Description                              |
| --------------------- | ---------------------------------------- |
| `[a]`                 | Set containing 'a'                       |
| `[a-z]`               | Set containing 'a' through 'z' and all letters in between, in Unicode order |
| `[^a-z]`              | Set containing all characters but 'a' through 'z', that is, U+0000 through 'a'-1 and 'z'+1 through U+10FFFF |
| `[[pat1][pat2]]`      | Union of sets specified by pat1 and pat2 |
| `[[[pat1]&[pat2]]`    | Intersection of sets specified by pat1 and pat2 |
| `[[pat1]-[pat2]]`     | Asymmetric difference of sets specified by pat1 and pat2 |
| `[:Lu:]` or `\p{Lu}`  | Set of characters having the specified Unicode property, in this case Unicode uppercase letters |
| `[:^Lu:]` or `\P{Lu}` | Set of characters not having the given Unicode property |

**Note**You cannot add an empty string ("") to a set.

### Formal Syntax

The following table provide examples of formal syntax patterns.

**Table: Formal syntax patterns**

| Pattern           | Description                              |
| ----------------- | ---------------------------------------- |
| `pattern :=`      | ('[' '^'? item* ']') \| property         |
| `item :=`         | char \| (char '-' char) \| pattern-expr  |
| `pattern-expr :=` | pattern \| pattern-expr pattern \| pattern-expr or pattern |
| `op :=`           | '&' \| '-'                               |
| `special :=`      | '[' \| ']' \| '-'                        |
| `char :=`         | Any character that is not special \| ('\' any character) \| ('\u' hex hex hex hex) |
| `property :=`     | Unicode property set pattern             |
| `a := b`          | a can be replaced by b                   |
| `a?`              | 0 or 1 instance of a                     |
| `a*`              | 1 or more instances of a                 |
| `a | b`           | Either a or b                            |
| `'a'`             | Literal string between the quotes        |

## Unicode Strings with Ustring

The Ustring API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__USTRING__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__USTRING__MODULE.html) applications) allows you to [handle general Unicode strings](#characters). Some functions are similar in name, signature, and behavior to the ANSI C `<string.h>` functions, and other functions provide more Unicode-specific functionality.

The i18n uses 16-bit Unicode (UTF-16) in the form of arrays of `i18n_uchar` code units. UTF-16 encodes each Unicode code point with either 1 or 2 `i18n_uchar` code units. This is the default form of Unicode, and a forward-compatible extension of the original, fixed-width form that was known as UCS-2. UTF-16 superseded UCS-2 with Unicode 2.0 in 1996.

The i18n also handles 16-bit Unicode text with unpaired surrogates. Such text is not well-formed UTF-16. Code-point-related functions treat unpaired surrogates as surrogate code points, such as separate units.

Although UTF-16 is a variable-width encoding form, such as some legacy multi-byte encodings, it is much more efficient even for random access because the code unit values for single-unit characters versus lead units versus trail units are completely disjoint. This means that it is easy to determine character (code point) boundaries from random offsets in the string.

Unicode (UTF-16) string processing is optimized for the single-unit case. Although it is important to support supplementary characters, which use pairs of lead/trail code units called "surrogates", their occurrence is rare. Almost all characters in modern use require only a single `i18n_uchar` code unit (such as their code point values are <=0xffff).

### Character Set Mapping Tables

The i18n API provides a character set conversion with mapping tables for a number of important codepages. The default tables are a subset of IBM's CDRA conversion table repository. ICU's [Converter Explorer](http://demo.icu-project.org/icu-bin/convexp) shows aliases and codepage charts for the default tables that are built into a standard ICU distribution.

Conversions for most codepages are implemented differently on different platforms. We are providing mapping tables here from many different sources, so that the i18n users and others can use these tables to get the same conversion behavior as on the original platforms.

The mapping tables and some of the source code of the tools that collected these tables are checked into a [CVS repository](http://source.icu-project.org/repos/icu/data/trunk/charset/data/ucm/).

For more information on character sets, codepages, and encodings, see [Coded Character Sets](http://www.ibm.com/software/globalization/topics/charsets/) on the IBM site.

## String Iteration with UCharIter

The UCharIter API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCHARITER__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCHARITER__MODULE.html) applications) allows you to [iterate through strings](#uchar_iter_examples).

The `current()` and `next()` functions only check the current index against the limit, and the `previous()` function only checks the current index against the start, to see if the iterator has already reached the beginning of the iteration range. The assumption - in all iterators - is that the index is moved though the API, which means that it cannot go out of bounds, or that the index is modified though the application code by a developer who knows enough about the iterator implementation to set valid index values.

The UCharIter functions return code unit values in the range of 0 - 0xffff. Before any functions operating on strings are called, the string must be set with the `i18n_uchar_iter_set_string()`, `i18n_uchar_iter_set_UTF16BE()`, or `i18n_uchar_iter_set_UTF8()`function.

## Prerequisites

To use the functions and data types of the i18n API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__MODULE.html) applications) and its submodules, include the `<utils_i18n.h>` header file in your application:

```
#include <utils_i18n.h>
```

## Managing Characters and Strings

Character and string management tasks include:

- [Comparing Ustrings](#compare)
- [Converting strings to Ustrings](#strings)
- [Converting Ustrings to strings](#ustrings)
- [Getting the Unicode block of a character](#unicode)
- [Getting the property value of a character](#property)
- [Getting the name of a character](#uchar_name)
- [Getting the decimal digit value of a character](#uchar_value)
- [Checking for a character binary property](#uchar_binary_property)
- [Getting an alternate representation of a character](#uchar_representation)
- [Getting the character age and Unicode version](#uchar_age)
- [Normalizing Ustrings](#normalize)
- [Searching text in a Ustring](#search)
- [Changing the case in a Ustring](#uppercase)
- [Concatenating Ustrings](#concatenate)
- [Finding a substring](#substring)

**Note**All source and destination buffers must be different.

### Comparing Ustrings

To compare 2 Ustrings for bitwise equality, use the `i18n_ustring_compare()` function.

The obtained result is equal to 0 if the compared Ustrings are equal. The result is a negative value if the first Ustring is smaller bitwise than the second one, and a positive value if the first Ustring is greater than the second one.

```
#define BUF_SIZE 64

i18n_uchar s1[BUF_SIZE];
i18n_ustring_copy_ua(s1, "Tizen");
i18n_uchar s2[BUF_SIZE];
i18n_ustring_copy_ua(s2, "Bada");
int32_t result = i18n_ustring_compare(s1, s2);
```

For a more complex, locale-sensitive comparison, use the Ucollator API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCOLLATOR__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCOLLATOR__MODULE.html) applications):

1. Create a Ucollator using the `i18n_ucollator_create()` function.Specify the locale as the first parameter and a handle to the created Ucollator as the second parameter.

    ```
    i18n_ucollator_h coll;
    i18n_ucollator_create(I18N_ULOCALE_US, &coll);
    ```

2. Set the Ucollator strength using the `i18n_ucollator_set_strength()` function.The strength influences how the strings are compared. The following strength levels are available:`I18N_UCOLLATOR_DEFAULT_STRENGTH`: Default`I18N_UCOLLATOR_PRIMARY`: Compares the primary differences only, such as different base letters ("a" vs. "b").`I18N_UCOLLATOR_SECONDARY`: Compares primary and secondary differences, such as different accented forms of the same base letter ("a" vs. "ä").`I18N_UCOLLATOR_TERTIARY`: Compares primary, secondary, and tertiary differences, such as case differences ("a" vs. "A").

    ```
    i18n_ucollator_set_strength(coll, I18N_UCOLLATOR_DEFAULT_STRENGTH);
    ```

	Since Tizen 4.0, you can also retrieve the current Ucollator strength using the `i18n_ucollator_get_strength()` function:

    ```
    i18n_ucollator_strength_e strength;
    i18n_ucollator_get_strength(coll, &strength);\
    ```

3. Compare 2 Ustrings.

   To compare 2 Ustrings, you have 2 options:

   - `i18n_ucollator_equal()`: Shows whether the compared Ustrings are equal.
   - `i18n_ucollator_str_collator()`: Shows whether the first Ustring is equal to, smaller, or greater than the second Ustring (`I18N_UCOLLATOR_EQUAL`, `I18N_UCOLLATOR_LESS`, or `I18N_UCOLLATOR_GREATER`).

   ```
   i18n_ubool equal;
   i18n_ucollator_equal(coll, s1, -1, s2, -1, &equal);

   i18n_ucollator_result_e result;
   i18n_ucollator_str_collator(coll, s1, -1, s2, -1, &result);
   ```

   Since Tizen 4.0, you can use the `i18n_ucollator_greater_or_equal()` function to check whether the first string is greater or equal to the second string:

   ```
   i18n_ubool result;
   i18n_ucollator_greater_or_equal(coll, s1, -1, s2, -1, &result);
   ```

4. When no longer needed, destroy the Ucollator using the `i18n_ucollator_destroy()` function:

    ```
    i18n_ucollator_destroy(coll);
    ```

Since Tizen 4.0, you can also:

- Check which locales the Ucollator API works with:

  - Retrieve an enumeration with all supported locales with the `i18n_ucollator_create_available_locales()` function:

    ```
    i18n_uenumeration_h locales;
    i18n_ucollator_create_available_locales(&locales);
    ```

  - Retrieve the count of all supported locales with the `i18n_ucollator_count_available()` function:

    ```
    int32_t n_available;
    i18n_ucollator_count_available(&n_available);
    ```

  - Retrieve a locale with a specified index by using the `i18n_ucollator_get_available()` function:

    ```
    const char *locale = NULL;
    int32_t locale_index = 0;
    i18n_ucollator_get_available(locale_index, &locale);
    ```

- Clone a given collator in a thread-safe way:

  ```
  i18n_ucollator_h collator;
  i18n_collator_create(I18N_ULOCALE_US, &collator);
  i18n_ucollator_h clone;

  i18n_ucollator_safe_clone(collator, &clone);
  ```

- Retrieve version information:

  - Ucollator version:

    ```
    i18n_uversion_info info;
    i18n_ucollator_get_version(coll, info);
    ```

  - UCA version information for Ucollator:

    ```
    i18n_uversion_info info;
    i18n_ucollator_get_uca_version(coll, info);
    ```

- Manage keywords:

  - Retrieve an enumeration containing all possible keywords that are relevant to a collation:

    ```
    i18n_uenumeration_h keywords;
    i18n_ucollator_get_keywords(&keywords);
    ```

  - Retrieve all currently-used values of a keyword:

    ```
    i18n_uenumeration_h keyword_values;
    i18n_ucollator_get_keyword_values("collation", &keyword_values);
    ```

  - Retrieve an array of string values in a preferred order that can make a difference, based on the keyword and locale:

    ```
    i18n_uenumeration_h keywords;
    i18n_ucollator_get_keyword_values_for_locale("collation", "en_US", false, &keywords);
    ```

- Manage sort keys:

  - Retrieve a sort key with the `i18n_ucollator_get_sort_key()` function:

    ```
    i18n_uchar src[64];
    i18n_ustring_copy_ua(src, str1);
    uint8_t sort_key[64];
    int32_t result_length;
    i18n_ucollator_get_sort_key(g_coll, src, -1, 64, sort_key, &result_length);
    ```

  - Retrieve the next count bytes of a sort key with the `i18n_ucollator_next_sort_key_part()` function:

    ```
    uint32_t state[2];
    uint8_t dest[64];
    int32_t result_length;
    i18n_uchar_iter_h iter = NULL;

    i18n_uchar_iter_create(&iter);
    i18n_uchar_iter_set_utf8(iter, str1, strlen(str1));
    i18n_ucollator_next_sort_key_part(g_coll, iter, state, dest, 1, &result_length);
    ```

  - Retrieve a bound for a given sort key and a number of levels by using the `i18n_ucollator_get_bound()` function:

    ```
    i18n_uchar src[64];
    i18n_ustring_copy_ua(src, str1);
    uint8_t sort_key[64];
    int32_t result_length;
    uint8_t bound[128];
    int32_t bound_length;

    i18n_ucollator_get_sort_key(g_coll, src, -1, 64, sort_key, &result_length);
    i18n_ucollator_get_bound(sort_key, result_length, I18N_UCOLLATOR_BOUND_UPPER, 1, bound, 128, &bound_length);
    ```

  - Merge 2 sort keys with the `i18n_ucollator_merge_sort_keys()` function:

    ```
    i18n_uchar src1[64];
    i18n_uchar src2[64];
    i18n_ustring_copy_ua(src1, "First string");
    i18n_ustring_copy_ua(src2, "Second string");
    uint8_t sort_key1[64];
    uint8_t sort_key2[64];

    int32_t result_length1;
    int32_t result_length2;
    uint8_t merged[128];
    int32_t merged_length;

    i18n_ucollator_get_sort_key(g_coll, src1, -1, 64, sort_key1, &result_length1);
    i18n_ucollator_get_sort_key(g_coll, src2, -1, 64, sort_key2, &result_length2);
    i18n_ucollator_merge_sort_keys(sort_key1, result_length1, sort_key2, result_length2, 128, merged, &merged_length);
    ```

### Converting Strings to Ustrings

To convert strings to Ustrings:

- To convert a byte string to a Unicode string (Ustring), use the `i18n_ustring_copy_ua()` function:

  ```
  const char *src = "Tizen";
  i18n_uchar dest[BUF_SIZE];
  i18n_ustring_copy_ua(dest, src);
  ```

- To convert a byte string to a Ustring while defining a maximum number of characters to be copied, use the `i18n_ustring_copy_ua_n()` function and set the character limit as the third parameter:

  ```
  const char *src = "Tizen";
  i18n_uchar dest[BUF_SIZE];
  i18n_ustring_copy_ua_n(dest, src, BUF_SIZE);
  ```

- To convert a UTF-8 string to a UTF-16 string, use the `i18n_ustring_from_UTF8()` function.

  The function returns the length of the converted string and an error code variable as out parameters.

  ```
  const char *src = "Tizen";
  i18n_uchar dest[BUF_SIZE];
  int dest_len;
  i18n_uerror_code_e error_code = I18N_ERROR_NONE;
  i18n_ustring_from_UTF8(dest, BUF_SIZE, &dest_len, src, -1, &error_code);
  ```

### Converting Ustrings to Strings

To convert Ustrings to strings:

- To convert a Ustring to a byte string, use the `i18n_ustring_copy_au()` function:

  ```
  i18n_uchar src[BUF_SIZE];
  i18n_ustring_copy_ua(src, "Tizen");
  char dest[BUF_SIZE];
  i18n_ustring_copy_au(dest, src);
  ```

- To convert a Ustring to a byte string while defining a maximum number of characters to be copied, use the `i18n_ustring_copy_au_n()` function and set the character limit as the third parameter:

  ```
  i18n_uchar src[BUF_SIZE];
  i18n_ustring_copy_ua(src, "Tizen");
  char dest[BUF_SIZE];
  i18n_ustring_copy_au_n(dest, src, BUF_SIZE);
  ```

- To convert a UTF-16 string to a UTF-8 string, use the `i18n_ustring_to_UTF8()` function.

  The function returns the length of the converted string and an error code variable as out parameters.

  To get the length of a Ustring, use the `i18n_ustring_get_length()` function.

  ```
  i18n_uchar src[BUF_SIZE];
  i18n_ustring_copy_ua(src, "Tizen");
  char dest[BUF_SIZE];
  int dest_len;
  i18n_uerror_code_e error_code = I18N_ERROR_NONE;
  i18n_ustring_to_UTF8(dest, BUF_SIZE, &dest_len, src, i18n_ustring_get_length(src), &error_code);
  ```

### Getting the Unicode Block of a Character

To get information about the location of a specified character, use the `i18n_uchar_get_ublock_code()` function.

The function returns, as an out parameter, the Unicode allocation block that contains the specified character. The Unicode blocks are defined in the `i18n_uchar_ublock_code_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html#gaa338daff96b0e62243e25fe240e4eda5) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html#gaa338daff96b0e62243e25fe240e4eda5) applications).

```
i18n_uchar character = 0xC131;
i18n_uchar_ublock_code_e ublock;
i18n_uchar_get_ublock_code(character, &ublock);
```

### Getting the Property Value of a Character

To get the property value of a specified character, use the `i18n_uchar_get_int_property_value()` function.

The character properties are defined in the `i18n_uchar_uproperty_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html#gaa57de8e60ee941839fdfd80833106757) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html#gaa57de8e60ee941839fdfd80833106757) applications).

The following example shows how to read the East Asian width property:

```
i18n_uchar character = 0xC131;
int32_t property_value;
i18n_uchar_get_int_property_value(character, I18N_UCHAR_EAST_ASIAN_WIDTH, &property_value);
```

### Getting the Name of a Character

You can retrieve the name of a Unicode character or retrieve the character from its name:

- To retrieve the name of a Unicode character, use the `i18n_uchar_char_name()` function:

  ```
  i18n_uchar32 c = 0x03B1; /* Hexadecimal code for "α" character */
  i18n_uchar_u_char_name_choice_e name_choice = I18N_UCHAR_U_UNICODE_CHAR_NAME;
  char buffer[BUF_SIZE];
  int32_t *name_length;

  i18n_uchar_char_name(c, name_choice, buffer, BUF_SIZE, &name_length); /* Buffer contains "GREEK SMALL LETTER ALPHA" */
  ```

- To retrieve the character from its name, use the `i18n_uchar_char_from_name()` function:

  ```
  i18n_uchar_u_char_name_choice_e name_choice = I18N_UCHAR_U_UNICODE_CHAR_NAME;
  const char *name = "GREEK SMALL LETTER ALPHA";
  i18n_uchar32 char_from_name;

  i18n_uchar_char_from_name(name_choice, name, &char_from_name);
  ```

### Getting the Decimal Digit Value of a Character

To retrieve the decimal digit value of a character, use the `i18n_uchar_digit_value()` function:

```
i18n_uchar32 c = 0x39; /* Hexadecimal code for digit "9" */
int32_t char_digit_value = 0;

i18n_uchar_char_digit_value(c, &char_digit_value); /* char_digit_value has value "9" */
```

### Checking for a Character Binary Property

You can check whether a Unicode character has a specific binary property in 2 ways:

- Use the corresponding `i18n_uchar_is_xxx()` function.

  The following example checks whether the character has the lowercase property:

  ```
  i18n_uchar32 c = 0x6D;
  i18n_ubool is_lowercase = false;
  i18n_uchar_is_lowercase(c, &is_lowercase);
  ```

- Use the `i18n_uchar_has_binary_property()` function with the name of the binary property.

  The binary properties are defined in the `i18n_uchar_uproperty_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html#gaa57de8e60ee941839fdfd80833106757) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCHAR__MODULE.html#gaa57de8e60ee941839fdfd80833106757) applications).

  ```
  i18n_uchar32 c = 0x6D;
  i18n_uchar_uproperty_e which = I18N_UCHAR_LOWERCASE;
  i18n_ubool has_binary_property = false;
  i18n_uchar_has_binary_property(c, which, &has_binary_property);
  ```

### Getting an Alternate Representation of a Character

To get an alternate representation of a character, use the `i18n_uchar_to_xxx()` functions.

The following example shows how to obtain the uppercase representation of the letter "m":

```
i18n_uchar32 c = 0x6D;
i18n_uchar32 to_upper;
i18n_uchar_to_upper(c, &to_upper);
```

### Getting the Character Age and Unicode Version

The character age is the Unicode version in which the character was first designated (as a non-character or for private use) or assigned:

- To retrieve the character age:

  ```
  i18n_uchar32 c = 0x1207;
  i18n_uversion_info char_age;
  i18n_uchar_char_age(c, &char_age);
  ```

- To retrieve the Unicode version information:

  ```
  i18n_uversion_info version_array;
  i18n_uchar_get_unicode_version(version_array);
  ```

### Normalizing Ustrings

To normalize a Ustring:

1. Get a Unormalizer instance using the `i18n_unormalization_get_instance()` function of the Unormalization API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UNORMALIZATION__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UNORMALIZATION__MODULE.html) applications).To use the built-in normalizer, set the first parameter to `NULL`.

    ```
    i18n_unormalizer_h normalizer;
    i18n_unormalization_get_instance(NULL, "nfc", I18N_UNORMALIZATION_DECOMPOSE, &normalizer);
    ```

2. Normalize a Ustring or Uchar with the obtained normalizer using the `i18n_unormalization_normalize()` function:

    ```
    i18n_uchar src = 0xACE0;
    i18n_uchar dest[4];
    int dest_str_len;
    i18n_unormalization_normalize(normalizer, &src, 1, dest, 4, &dest_str_len);
    ```

### Searching Text in a Ustring

To search for a substring in a Ustring:

1. Create a search iterator using the `i18n_usearch_create_new()` function of the Usearch API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__USEARCH__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__USEARCH__MODULE.html) applications):

    ```
    i18n_uchar text[BUF_SIZE];
    i18n_ustring_copy_ua(text, "TIZEN");
    i18n_uchar pattern[BUF_SIZE];
    i18n_ustring_copy_ua(pattern, "ZEN");
    i18n_usearch_h usearch;
    i18n_usearch_create_new(pattern, -1, text, -1, I18N_ULOCALE_US, NULL, &usearch);
    ```

2. Get the index of the first match (the first occurrence of the found pattern) using the `i18n_usearch_first()` function:

    ```
    int index;
    i18n_usearch_first(usearch, &index);
    ```

3. When no longer needed, destroy the search iterator using the `i18n_usearch_destroy()` function:

    ```
    i18n_usearch_destroy(usearch);
    ```

### Changing the Case in a Ustring

To change the case in a Ustring:

1. To change all characters' case in a Ustring, use the `i18n_ustring_to_upper()` or `i18n_ustring_to_lower()` function:

    ```
    i18n_uchar src[BUF_SIZE];
    i18n_ustring_copy_ua(src, "Tizen");
    i18n_uchar dest[BUF_SIZE];
    i18n_ustring_to_upper(dest, BUF_SIZE, src, -1, I18N_ULOCALE_US, &error_code);
    i18n_ustring_to_lower(dest, BUF_SIZE, src, -1, I18N_ULOCALE_US, &error_code);
    ```

2. To change the string case to title case, use the `i18n_ustring_to_title_new()` function:

    ```
    i18n_uchar src[BUF_SIZE];
    i18n_ustring_copy_ua(src, "Tizen");
    i18n_uchar dest[BUF_SIZE];
    i18n_ustring_to_title_new(dest, BUF_SIZE, src, BUF_SIZE, NULL, NULL);
    ```

### Concatenating Ustrings

To concatenate 2 Ustrings, use the `18n_ustring_cat()` or `18n_ustring_cat_n()` function.

The functions differ in that the latter takes a third parameter to define a maximum number of characters to append to the destination string.

```
i18n_uchar src[BUF_SIZE];
i18n_uchar dest[BUF_SIZE];

i18n_ustring_copy_ua(dest, "Destination string");
i18n_ustring_copy_ua(src, "Appended string");

i18n_ustring_cat_n(dest, src, BUF_SIZE);
/* Or */
i18n_ustring_cat(dest, src);
```

### Finding a Substring

To find a substring in a Ustring, use the `i18n_ustring_string()` function.

The result is a pointer to the first occurrence of the substring, or `NULL` if the substring is not found. You can use pointer arithmetic to find the index of the character at which the first occurrence begins.

```
i18n_uchar s[BUF_SIZE];
i18n_uchar substring[BUF_SIZE];

i18n_uchar *result = i18n_ustring_string(s, substr);

if (result == NULL)
    dlog_print(DLOG_DEBUG, LOG_TAG, "Substring not found");
else
    dlog_print(DLOG_DEBUG, LOG_TAG, "Substring index: %d", result - s);
```

## Managing Dates and Calendar

To create and use a calendar:

1. To manage dates and calendar, the Ucalendar (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html) applications), Udate (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UDATE__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UDATE__MODULE.html) applications), and Udatepg (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UDATEPG__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UDATEPG__MODULE.html) applications) APIs are used.

   - The Ucalendar API is used for converting between an `i18n_udate` object and a set of integer fields, such as `I18N_UCALENDAR_YEAR`, `I18N_UCALENDAR_MONTH`, `I18N_UCALENDAR_DAY`, and `I18N_UCALENDAR_HOUR`.
   - The Udate API is used to convert dates and times from their internal representations to a textual form and back again in a language-independent manner.
   - The Udatepg API is used to generate date format patterns, such as "yy-MM-dd".

2. To create a Ucalendar, use the `i18n_ucalendar_create()` function:

    ```
    i18n_uchar timezone[BUF_SIZE];
    const char *timezone_name = "America/New_York";
    int timezone_name_len = strlen(timezone_name);
    i18n_ustring_copy_ua_n(timezone, timezone_name, timezone_name_len + 1);
    i18n_ucalendar_h ucalendar;
    i18n_ucalendar_create(timezone, -1, I18N_ULOCALE_US, I18N_UCALENDAR_DEFAULT, &ucalendar);
    ```

3. To set a date in the Ucalendar, use the `i18n_ucalendar_set_date_time()` function.In the following example, the date is set as 1 July 2014, 9:00:00.To define the month, you can use numbers (month reduced by 1, such as 0 for January and 1 for February), or to avoid mistakes, the values of the `i18n_ucalendar_months_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html#ga094cacb2ef9ee4805e42e276fec5ae2f) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html#ga094cacb2ef9ee4805e42e276fec5ae2f) applications).`i18n_ucalendar_set_date_time(ucalendar, 2014, I18N_UCALENDAR_JULY, 1, 9, 0, 0);`To set a date using milliseconds from the epoch, use the `i18n_ucalendar_set_milliseconds()` function:`i18n_udate udate;/* udate must be set */i18n_ucalendar_set_milliseconds(ucalendar, udate);`To add a specified period to the Ucalendar, use the `i18n_ucalendar_add()` function.Specify the date field to modify (such as year, week, or day) using the `i18n_ucalendar_date_fields_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html#gaee345f9992035a07732d16d69c41c192) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCALENDAR__MODULE.html#gaee345f9992035a07732d16d69c41c192) applications) as the second parameter, and the amount to modify as the third parameter (use a negative value to subtract from the existing value).

    ```
    i18n_ucalendar_add(ucalendar, I18N_UCALENDAR_HOUR, 3);
    ```

4. To get a date from the Ucalendar, you can use various functions:

   - To get a specific date field from a Ucalendar instance, use the `i18n_ucalendar_get()` function and define the wanted date field with the `i18n_ucalendar_date_fields_e` enumeration:

    ```
    int uday;
    i18n_ucalendar_get(ucalendar, I18N_UCALENDAR_DAY_OF_YEAR, &uday);
    ```
   - To get a date from a Ucalendar in milliseconds from the epoch, use the `i18n_ucalendar_get_milliseconds()` function:

	```
    i18n_udate date;
    i18n_ucalendar_get_milliseconds(ucalendar, &date);
    ```

   - To get the actual current date from the system, use the `i18n_ucalendar_get_now()` function. The obtained date is represented as milliseconds from the epoch.

    ```
    i18n_udate now;
    i18n_ucalendar_get_now(&now);
    ```

   To check whether the Ucalendar date is in daylight saving time, use the `i18n_ucalendar_is_in_daylight_time()` function:

   ```
   bool dst;
   i18n_ucalendar_is_in_daylight_time(ucalendar, &dst);
   ```

5. To format a date, you can use a pattern generator or define a date format:

   - Using a pattern generator:
     1. To create a Udatepg pattern generator instance, use the `i18n_udatepg_create()` function and define the desired locale as the first parameter:

        ```
        i18n_udatepg_h udatepg;
        i18n_udatepg_create(I18N_ULOCALE_UK, &udatepg);
        ```

     2. To generate a date best pattern with the pattern generator, use the `i18n_udatepg_get_best_pattern()` function.As the second parameter, you need a draft format, which defines the fields to be displayed (for example, E for the day of the week, M for month, y for year, d for the day of the month, and D for day of the year).

        ```
        int pattern_len;
        i18n_uchar format[BUF_SIZE];
        i18n_ustring_copy_ua_n(format, "EEEdMMMyyyyHHmmssz", BUF_SIZE);
        i18n_uchar best_pattern[BUF_SIZE];
        i18n_udatepg_get_best_pattern(udatepg, format, BUF_SIZE, best_pattern, BUF_SIZE, &pattern_len);
        ```

   - Using a date format:
     1. To create a date format, use the `i18n_udate_create()` function.As the first and second parameter, specify the formatting style for time and date using the values of the `i18n_udate_format_style_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UDATE__MODULE.html#gaee2461e926bc151486d380c43bc4f2a3) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UDATE__MODULE.html#gaee2461e926bc151486d380c43bc4f2a3) applications).

        ```
        i18n_udate_format_h date_format;
        const char *timezone_name = "Asia/Seoul";
        int timezone_name_len = strlen(timezone_name);
        i18n_ustring_copy_ua_n(timezone, timezone_name, timezone_name_len + 1);
        i18n_udate_create(I18N_UDATE_FULL, I18N_UDATE_FULL, I18N_ULOCALE_UK, timezone, -1, best_pattern, -1, &date_format);
        ```

     2. To obtain a Ustring with a specified date and the created date format, use the `i18n_udate_format_date()` function:

        ```
        i18n_uchar date_result[BUF_SIZE];
        int date_len;
        i18n_udate_format_date(date_format, now, date_result, BUF_SIZE, NULL, &date_len);
        ```

6. When no longer needed, destroy the Ucalendar, Udatepg, and Udate instances using the `i18n_ucalendar_destroy()`, `i18n_udatepg_destroy()`, and `i18n_udate_destroy()` functions:

        ```
        i18n_ucalendar_destroy(ucalendar);
        i18n_udatepg_destroy(udatepg);
        i18n_udate_destroy(date_format);
        ```

## Managing Locales

To manage the features of a specific geographical, political, or cultural region:

- To get the language code associated with a locale, use the `i18n_ulocale_get_language()` function:

    ```
    char language[BUF_SIZE];
    int lang_len;
    i18n_ulocale_get_language(I18N_ULOCALE_GERMANY, language, BUF_SIZE, &lang_len);
    ```

- To get the language ISO-3 code for the specified locale, use the `i18n_ulocale_get_iso3_language()` function:

    ```
    const char *language_iso = i18n_ulocale_get_iso3_language(I18N_ULOCALE_GERMANY);
    ```

- To get the full name of the language for the specified locale, use the `i18n_ulocale_get_display_language()` function.In the following example, the name of the "fr_CA" locale is obtained in German:

    ```
    char *locale = I18N_ULOCALE_CANADA_FRENCH;
    i18n_uchar language_name[BUF_SIZE];
    int lang_len;
    i18n_ulocale_get_display_language(locale, I18N_ULOCALE_GERMANY, language_name, BUF_SIZE, &lang_len);
    ```

- To get the line orientation for the specified locale, use the `i18n_ulocale_get_line_orientation()` function:

    ```
    const char *locale = I18N_ULOCALE_ENGLISH;
    i18n_ulocale_layout_type_e type;
    i18n_ulocale_get_line_orientation(locale, &type);
    ```

- To get the character orientation for the specified locale, use the `i18n_ulocale_get_character_orientation()` function:

    ```
    const char *locale = I18N_ULOCALE_ENGLISH;
    i18n_ulocale_layout_type_e type;
    i18n_ulocale_get_character_orientation(locale, &type);
    ```

- To get the variant code for the specified locale, use the `i18n_ulocale_get_variant()` function.The function returns the actual size of the variant code.

    ```
    const char *locale = I18N_ULOCALE_ENGLISH;
    char *variant = malloc(sizeof(char) * BUF_SIZE);
    int32_t variant_len = i18n_ulocale_get_variant(locale, variant, BUF_SIZE);
    ```

- To get a full name for the specified locale, use the `i18n_ulocale_get_display_name()` function.In the following example, the name of the "fr_CA" locale is obtained in German:

    ```
    i18n_uchar name[BUF_SIZE];
    int name_len;
    i18n_ulocale_get_display_name(I18N_ULOCALE_CANADA_FRENCH, I18N_ULOCALE_GERMANY, name, BUF_SIZE, &name_len);
    ```

- To get or set the default locale, use the `i18n_ulocale_get_default()` or `i18n_ulocale_set_default()` function:

    ```
    /* Get */
    char *locale;
    i18n_ulocale_get_default(&locale);

    /* Set */
    i18n_ulocale_set_default(I18N_ULOCALE_KOREA);
    ```

## Managing Numbers

To format and parse numbers for a locale:

1. To create a number format, use the `i18n_unumber_create()` function.Define the style as the first parameter using the `i18n_unumber_format_style_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UNUMBER__MODULE.html#ga4edc8cb72e7f46e05d8cdfe24cf386f1) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UNUMBER__MODULE.html#ga4edc8cb72e7f46e05d8cdfe24cf386f1) applications).The fourth parameter sets the locale (`NULL` for default). Some string shortcuts for specific locales are defined in the `utils_i18n_types.h` header file. For example, `I18N_ULOCALE_US` is equal to "en_US".

    ```
    i18n_unumber_format_h num_format;
    i18n_unumber_format_style_e format_style = I18N_UNUMBER_CURRENCY;
    const char* locale = I18N_ULOCALE_US;
    i18n_unumber_create(format_style, NULL, -1, locale, NULL, &num_format);
    ```

2. To use the created number format to format a given number based on the rules of a specified locale, you can use various `i18n_unumber_format_XXX()` functions.The following example formats a double-type number:

    ```
    #define BUF_SIZE 64
    i18n_uchar myString[BUF_SIZE];
    double myNumber = 4.5;
    i18n_unumber_format_double(num_format, myNumber, myString, BUF_SIZE, NULL);
    ```

	The result set in the `myString` variable is equal to:
    ```
    $4.50
    ```
    
3. To get a symbol associated with the created number format, use the `i18n_unumber_get_symbol()` function.The second parameter uses the values of the `i18n_unumber_format_symbol_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UNUMBER__MODULE.html#ga9abb496f12b9fd47244060af5ecbc39e) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UNUMBER__MODULE.html#ga9abb496f12b9fd47244060af5ecbc39e) applications) to define the symbol to be retrieved.The function returns the symbol used in the given locale. In the following example, it returns the currency `$` sign:

    ```
    i18n_uchar buffer[BUF_SIZE];
    int buf_len;
    i18n_unumber_format_symbol_e symbol = I18N_UNUMBER_CURRENCY_SYMBOL;
    i18n_unumber_get_symbol(num_format, symbol, buffer, BUF_SIZE, &buf_len);
    ```

4. When no longer needed, destroy the number format with the `i18n_unumber_destroy()` function:

    ```
    i18n_unumber_destroy(num_format);
    ```

## Managing Iteration Using Ubrk

To manipulate or iterate through strings, you can use the Ubrk library. It helps you to treat strings as a set of characters, words, or sentences:

1. To create an iterator to iterate through a string, use the `i18n_ubrk_create()` function.The first parameter defines the type of the iterator:
	- `I18N_UBRK_WORD` for word iteration
	- `I18N_UBRK_CHARACTER` for character iteration
	- `I18N_UBRK_LINE` for line iteration
	- `I18N_UBRK_SENTENCE` for sentence iteration

 ```
 i18n_ubreak_iterator_h boundary;
 const char *str = "Twinkle, twinkle little star";
 int str_len = strlen(str);
 i18n_uchar* stringToExamine = malloc(sizeof(i18n_uchar)*(str_len + 1));
 i18n_ustring_copy_ua(stringToExamine, str);
 i18n_ubrk_create(I18N_UBRK_WORD, I18N_ULOCALE_US, stringToExamine, -1, &boundary);
 ```

2. To change the position of the iterator, you can use several functions, such as `i18n_ubrk_first()`, `i18n_ubrk_last()`, `i18n_ubrk_next()`, and `i18n_ubrk_previous()`.The following example retrieves the boundaries of the first word in the `stringToExamine` string. The `start` and `end` variables represent the boundaries of the first word, in this example 0 and 7.

    ```
    int32_t start = i18n_ubrk_first(boundary);
    int32_t end = i18n_ubrk_next(boundary);
    ```

3. To retrieve a string delimited with the `start` and `end` boundary variables, use the `i18n_ustring_copy_n()` function.The second parameter defines the source string, and the third parameter defines the maximum number of characters to copy.

    ```
    i18n_ustring_copy_n(result, &str[start], end-start);
    ```

4. When no longer needed, destroy the ubreak iterator with the `i18n_ubrk_destroy()` function. Remember to free all allocated memory with the `free()` function.

    ```
    i18n_ubrk_destroy(boundary);
    ```

## Managing Enumerations

To create collections of strings and iterate through them, [create an enumeration](#create_enum). You can also [obtain enumerations from specific functions](#get_enum).

### Creating an Enumeration

To create an enumeration based on existing strings:

1. Define an array of strings (pointers to `char`):

    ```
    const char* strings[] = {"First", "Second", "Third", "Fourth"};

    /* Length of the pointers array (the number of strings) */
    int32_t size = sizeof(strings) / sizeof(strings[0]);
    ```

2. Create an enumeration of the `char` strings:

    ```
    i18n_uenumeration_h strings_enum;

    i18n_uenumeration_char_strings_enumeration_create(strings, size, &strings_enum);
    ```

    For `i18n_uchar` strings, use the `i18n_uenumeration_uchar_strings_enumeration_create()` function.

3. Get the number of elements:

   ```
   int32_t count = i18n_uenumeration_count(strings_enum);
   ```

   If the enumeration was created successfully, the value is equal to the `size` variable used above.

4. Iterate through the `char` elements using the `i18n_uenumeration_next()` function, until it returns `NULL`.The string is null-terminated, and the `len` variable is the length of the string.Do not free the returned string. The returned pointer is valid until a function is called for the enumeration.

    ```
    const char *element = NULL;
    int len;

    element = i18n_uenumeration_next(strings_enum, &len);
    while (element != NULL) {
        /* Use the returned string */

        element = i18n_uenumeration_next(strings_enum, &len);
    }
    ```

    For `i18n_uchar` strings, use the `i18n_uenumeration_unext()` function.

5. When no longer needed, destroy the enumeration with the `18n_uenumeration_destroy()` function:

    ```
    18n_uenumeration_destroy(strings_enum);
    ```

### Obtaining an Enumeration

Certain functions in the i18n module provide enumerations of values related to them. After the enumeration is obtained, you can iterate through its values.

- To get an enumeration of available time zones and iterate through them, use the `i18n_ucalendar_timezones_create()` function:

    ```
    i18n_uenumeration_h timezones;
    i18n_ucalendar_timezones_create(&timezones);

    int32_t count = i18n_uenumeration_count(timezones);

    const char *tz = NULL;
    int len;

    tz = i18n_uenumeration_next(timezones, &len);
    while (tz != NULL) {
        /* Use the time zone string */

        tz = i18n_uenumeration_next(timezones, &len);
    }

    i18n_uenumeration_destroy(timezones);
    ```

- After creating a date pattern generator for a given locale, you can obtain an enumeration of all the pattern skeletons in a canonical form.

  To get the enumeration and iterate through the skeletons, use the `i18n_udatepg_skeletons_create()` function:

  ```
  i18n_udatepg_h udatepg;
  i18n_udatepg_create(I18N_ULOCALE_UK, &udatepg);

  i18n_uenumeration_h skeletons;
  i18n_udatepg_skeletons_create(udatepg, &skeletons);

  i18n_udatepg_destroy(udatepg);

  int32_t count = i18n_uenumeration_count(skeletons);

  const char *sk = NULL;
  int len;

  sk = i18n_uenumeration_next(skeletons, &len);
  while (sk != NULL) {
      /* Use the skeleton string */

      sk = i18n_uenumeration_next(skeletons, &len);
  }

  i18n_uenumeration_destroy(skeletons);
  ```

- To get an enumeration of keywords for a given locale string and iterate through the keywords, use the `i18n_ulocale_keywords_create()` function:

    ```
    const char *loc_string = "en_US@collation=PHONEBOOK;calendar=GREGORIAN;currency=USD";

    i18n_uenumeration_h keywords;
    i18n_ulocale_keywords_create(loc_string, &keywords);

    int32_t count = i18n_uenumeration_count(keywords);

    const char *keyword = NULL;
    int len;

    keyword = i18n_uenumeration_next(keywords, &len);
    while (keyword != NULL) {
        /* Use the keyword string */

        keyword = i18n_uenumeration_next(keywords, &len);
    }

    i18n_uenumeration_destroy(keywords);
    ```

## Managing Time Zones

To manage time zone details, such as the time zone offset and daylight savings:

1. To retrieve time zone information:

   - To get the default time zone based on the time zone where the program is running, use the `i18n_timezone_create_default()` function:

     ```
     i18n_timezone_h tmz;
     i18n_timezone_create_default(&tmz);
     ```

   - To get the display name of the time zone, use the `i18n_timezone_get_display_name()` function:

     ```
     char *display_name;
     i18n_timezone_get_display_name(tmz, &display_name);
     ```

   - To get the time zone ID, use the `i18n_timezone_get_id()` function:

     ```
     char *timezone_id;
     i18n_timezone_get_id(tmz, &timezone_id);
     ```

   - To check whether a given time zone uses daylight savings time (DST), use the `i18n_timezone_use_daylight_time()` function:

     ```
     bool dst_savings;
     i18n_timezone_use_daylight_time(tmz, &dst_savings);
     ```

   - To get the daylight savings (the amount of time to be added to the local standard time to get the local wall clock time), use the `i18n_timezone_get_dst_savings()` function.

     The result is returned in milliseconds (3600000 ms = 1 hour). In the following example, milliseconds are changed to minutes (1 min = 60000 ms).

     ```
     #define MS_TO_MIN 60000
     int32_t dst_savings;
     i18n_timezone_get_dst_savings(tmz, &dst_savings/MS_TO_MIN);
     ```

   - To get the raw GMT offset, use the `i18n_timezone_get_raw_offset()` function.

     The result is the number of milliseconds to add to GMT to get the local time, before taking DST into account, and it is returned in milliseconds. In the following example, milliseconds are changed to minutes (1 min = 60000 ms).

     ```
     #define MS_TO_MIN 60000
     int32_t offset_milliseconds;
     i18n_timezone_get_raw_offset(tmz, &offset_milliseconds/MS_TO_MIN);
     ```

   - To get the region code associated with the time zone ID, use the `i18n_timezone_get_region()` function:

     ```
     char region[BUF_SIZE];
     int32_t region_len = -1;
     i18n_timezone_get_region(timezone_id, region, &region_len, BUF_SIZE);
     ```

2. When no longer needed, destroy the time zone instance with the `i18n_timezone_destroy()` function:

   ```
   i18n_timezone_destroy(tmz);
   ```

## Managing Sets

You can create sets, which contain characters and strings. You can iterate through the set elements and carry out various operations on the set.

To manage sets:

1. To create a set, use various `i18n_uset_create_XXX()` functions.The following example creates an empty set:

    ```
    i18n_uset_h set;
    i18n_uset_create_empty(&set);
    ```

2. To manage character sets:

   A character set contains characters as its elements.

   - Add characters from a string to the set using the `i18n_uset_add_all_code_points()` function:

    ```
    const char *text = "Example string";
    i18n_uchar u_input_text[BUF_SIZE];
    i18n_ustring_copy_ua(u_input_text, text);

    i18n_uset_add_all_code_points(set, u_input_text, -1);
    ```

   - Get the list of characters in the set using the `i18n_uset_char_at()` function:

    ```
    int chars_count = i18n_uset_size(set);
    int i;

    /* Get all characters in the set */
    for (i = 0; i < chars_count; i++)
        i18n_uchar32 uchar = i18n_uset_char_at(set, i);
    ```
    
   - Check whether the set contains a specific character using the `i18n_uset_contains()` function:

    ```
    i18n_ubool contains_character = i18n_uset_contains(set, 'a');
    ```

   - Check whether the set contains characters from a specific range using the `i18n_uset_contains_range()` function.The following example uses the range "a-c".

    ```
    i18n_ubool contains_character = i18n_uset_contains_range(set, 'a', 'c');
    ```

   - Check whether the set contains characters from another set using the `i18n_uset_contains_all()` function:

    ```
    i18n_uset_h compare_set = NULL;
    i18n_uset_create_empty(&compare_set);
    /* Fill the second set */

    i18n_ubool contains_character = i18n_uset_contains_all(set, compare_set);
    ```

3. To manage string sets:

   A string set contains strings as its elements.

   - Add a string to the set using the `i18n_uset_add_string()` function.The entire string is a single element.

    ```
    const char *text = "Example string";
    i18n_uchar u_input_text[BUF_SIZE];
    i18n_ustring_copy_ua(u_input_text, text);

    i18n_uset_add_string(set, u_input_text, -1);
    ```

   - List all strings in the set using the `i18n_uset_get_item()` function.The function returns the length of a string item, or 0, if the item is a range.

    ```
    int strings_count = i18n_uset_get_item_count(set);
    int32_t len = 0;
    int32_t i;
    for (i = 0; i < strings_count; ++i) {
        i18n_uchar32 start, end;
        i18n_uchar string[100];
        len = i18n_uset_get_item(set, i, &start, &end, string, 100);
        if (len != 0)
            /* String was found, use the 'string' variable */
    }
    ```

   - Check whether the set contains a string using the `i18n_uset_contains_string()` function:

    ```
    const char *input_string = "Input string";
    int input_string_len = strlen(input_string);
    i18n_uchar *input_ustring = malloc(sizeof(i18n_uchar) * (input_string_len + 1));
    i18n_ustring_copy_ua(input_ustring, input_string);

    i18n_ubool contains = i18n_uset_contains_string(set, input_ustring, -1);
    ```

## Retrieving the ICU Version

Since Tizen 4.0, you can retrieve the current ICU library version by using the Uversion API.

To retrieve the current version:

1. To get the current ICU version, use the `i18n_uversion_get_version()` function, which returns the version number in a `uversion` array, in hexadecimal format:

    ```
    i18n_uversion_info array;
    i18n_uversion_get_version(array);
    ```

2. To convert the version number between hexadecimal and dotted decimal format:
   - To convert the version number from hexadecimal format into a string in dotted decimal format, use the `i18n_uversion_to_string()` function:

    ```
    char *decimal_version;
    i18n_uversion_to_string(array, decimal_version);
    ```

   - To convert the version number from a string in dotted decimal format to hexadecimal format, use the `i18n_uversion_from_string()` function:

    ```
    char *decimal_version = "57.1";
    i18n_uversion_from_string(decimal_version, version);
    ```

    If your source string is of the `i18n_uchar` type, use the `i18n_uversion_from_ustring()` function instead.

## Iterating through Strings

Since Tizen 4.0, you can use UcharIter API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__BASE__UTILS__I18N__UCHARITER__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__BASE__UTILS__I18N__UCHARITER__MODULE.html) applications) to safely iterate through strings:

1. Create a UCharIter pointer:

   ```
   i18n_uchar_iter_h uchar_iter;
   i18n_uchar_iter_create(&uchar_iter);
   ```

2. Set up iteration over a string of a specific type:

   - `i18n_uchar` string:

    ```
    i18n_uchar *uchar_string = "UChar test string";
    int32_t ulen = i18n_ustring_get_length(uchar_string);
    i18n_uchar_iter_set_string(uchar_iter, uchar_string, ulen);
    ```

   - UTF-16BE string:

     ```
     i18n_uchar *utf16be_string = "UTF-16BE test string";
     int32_t ulen = i18n_ustring_get_length(utf16be_string);
     i18n_uchar_iter_set_utf16be(uchar_iter, utf16be_string, ulen);
     ```

   - UTF-8 string:

     ```
     i18n_uchar *utf8_string = "UTF-8 test string";
     int32_t ulen = i18n_ustring_get_length(utf8_string);
     i18n_uchar_iter_set_utf16be(uchar_iter, utf8_string, ulen);
     ```

3. Retrieve the iterator index:

   - To retrieve the start position:

     ```
     int32_t index;
     i18n_uchar_iter_get_index(uchar_iter, I18N_UCHAR_ITER_START, &index);
     ```

   - To retrieve the current position:

     ```
     int32_t index;
     i18n_uchar_iter_get_index(uchar_iter, I18N_UCHAR_ITER_CURRENT, &index);
     ```

   - To retrieve the string length:

     ```
     int32_t index;
     i18n_uchar_iter_get_index(uchar_iter, I18N_UCHAR_ITER_LENGTH, &index);
     ```

4. Move the iterator to a desired position:

   - To move to the beginning:

     ```
     int32_t delta = 0;
     i18n_uchar_iter_move(uchar_iter, delta, I18N_UCHAR_ITER_START, &index);
     ```

   - To move to the current position:

     ```
     int32_t delta = 0;
     i18n_uchar_iter_move(uchar_iter, delta, I18N_UCHAR_ITER_CURRENT, &index);
     ```

   - To move to the end of a string:

     ```
     int32_t delta = 0;
     i18n_uchar_iter_move(uchar_iter, delta, I18N_UCHAR_ITER_LIMIT, &index);
     ```

   - To move 3 characters forward from the current position:

     ```
     int32_t delta = 3;
     i18n_uchar_iter_move(uchar_iter, delta, I18N_UCHAR_ITER_CURRENT, &index);
     ```

   - To move 3 characters backward from the end:

     ```
     int32_t delta = -3;
     i18n_uchar_iter_move(uchar_iter, delta, I18N_UCHAR_ITER_LIMIT, &index);
     ```

5. Check whether it is possible to move:

   - Forward:

     ```
     bool has_next;
     i18n_uchar_iter_has_next(uchar_iter, &has_next);
     ```

   - Backward:

     ```
     bool has_previous;
     i18n_uchar_iter_has_previous(uchar_iter, &has_previous);
     ```

6. Retrieve code units:

   - To retrieve the code unit from the current position:

     ```
     i18n_uchar32 current;
     i18n_uchar_iter_current(uchar_iter, &current);
     ```

   - To retrieve the previous character from the current position:

     ```
     i18n_uchar32 previous;
     i18n_uchar_iter_previous(uchar_iter, &previous);
     ```

   - To retrieve the next character from the current position:

     ```
     i18n_uchar32 next;
     i18n_uchar_iter_next(uchar_iter, &next);
     ```

7. Manage states:

   States are iterator positions saved in the `int32_t` variable. When you need to be able to retrieve a previous position, it is more efficient to store and retrieve states than to use the `i18n_uchar_iter_get_index()` and `i18n_uchar_iter_move()` functions.

   - To set a state:

     ```
     int32_t state = 4;
     i18n_uchar_iter_set_state(uchar_iter, state);
     ```

   - To retrieve a state:

     ```
     int32_t state;
     i18n_uchar_iter_get_state(uchar_iter, &state);
     ```

8. When the iteration is no longer needed, destroy it:

   ```
   i18n_uchar_iter_destroy(uchar_iter);
   ```