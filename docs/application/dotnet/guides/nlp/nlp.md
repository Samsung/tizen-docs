# Natural Language Processing (NLP)


Nlp is a subset of natural language toolkit that specifies an interface and a protocol for basic natural language processing. Tizen enables you to use Natural Language Process (Nlp) functionalities, such as language detection, parts of speech, word tokenize, lemmatize, and named entity detection. For more information, see the [nltk Forum](http://www.nltk.org/).

The main features of the Tizen.Nlp namespace include:

-   Word Tokenize suppport

    You can get tokens from a sentence, the type of return is WordTokenizeResult.

-   Part of Speech support

    You can get tokens and tags from a sentence, the type of return is PosTagResult.

-   Named Entity Detection support

    You can get tokens and tags from a sentence, the type of return is NamedEntityRecognitionResult.

-   Lemmatizing support

    You can get the actual word from a word, the type of return is LemmatizeResult.

-   Language Detect support

    You can get language from a sentence, the type of return is LanguageDetectedResult.

## Word Tokenize
This method break up the sentence into words and punctuation.


## Part of Speech
This method breaks up the sentence into words and punctuation with tags attributes.


## Named Entity Detection
This method breaks up the sentence into words and punctuation with tags attributes.

## Lemmatizing
This method is used to get the actual word from a word.

## Language Detect
This method is used to detect the language of a sentence.


## Prerequisites

Enable your application to use the Nlp functionality:

1.  Using the [Tizen.Nlp](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Nlp.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
       <privilege>http://tizen.org/privilege/datasharing</privilege>
    </privileges>
    ```

2.  Using the methods and properties of the `Tizen.Nlp` namespace, include it in your application:

    ```
    using Tizen.Nlp;
    ```

<h2>Receive WordTokenize Tokens</h2>
## Receive Tokens - WordTokenize

Receive the tokens from sentence:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the Nlp service on init of app:

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the WordTokenizeAsync(string msg) in a async task method:

    ```
    public async Task OnTokenButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.WordTokenizeAsync(msg);
        WordTokenizeResult wr = await ret;
        ..
    }
    ```

3.  When nlp object is no longer needed, call Dispose() to release the resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```

<h2>Receive PosTag Tokens and Tags</h2>
## Receive Tokens and Tags - PosTag

Receive the tokens and tags from sentence:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the Nlp service on init of app:

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the PosTagAsync(string msg) in a async task method:

    ```
    public async Task OnPosButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.PosTagAsync(msg);
        PosTagResult pr = await ret;
        ..
    }
    ```

3.  When nlp object is no longer needed, call Dispose() to release the resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```

<h2>Receive Named Entity Tokens and Tags</h2>
## Receive Tokens and Tags - Named Entity

Receive the tokens and tags from sentence:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the Nlp service on init of app:

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the NamedEntityRecognitionAsync(string msg) in a async task method:

    ```
    public async Task OnTokenButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.NamedEntityRecognitionAsync(msg);
        NamedEntityRecognitionResult nr = await ret;
        ..
    }
    ```

3.  When it is no longer needed, call Dispose() to release the resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```


<h2>Receive Lemmatize ActualWord</h2>
## Receive ActualWord - Lemmatizing

Receive the actual word from word:

1.  Construct an NaturalLanguageProcess object on OnCreate(), and Connect the Nlp service on init of app :

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the LemmatizeaAsync(string msg) in a async Task method:

    ```
    public async Task OnLemmButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.LemmatizeaAsync(msg);
        LemmatizeResult lr = await ret;
        ..
    }
    ```

3.  When it is no longer needed, call Dispose() to release resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```

<h2>Detect Language</h2>
## Detect Language from sentence - Detect Language

Detect the language from sentence:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the Nlp service on init of app:

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the LanguageDetectAsync(string msg) in a async task method:

    ```
    public async Task OnLangButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.LanguageDetectAsync(msg);
        LanguageDetectedResult lr = await ret;
        ..
    }
    ```

3.  When it is no longer needed, call Dispose() to release the resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         a.Dispose();
         ..
        }
    ```



## Related Information
* Dependencies
  -   Tizen 5.0 and Higher
