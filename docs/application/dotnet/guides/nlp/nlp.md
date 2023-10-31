# Natural Language Processing (NLP)

NLP is a subset of Natural Language Toolkit that specifies an interface and a protocol for basic natural language processing. Tizen enables you to use Natural Language Process (NLP) functionalities, such as language detection, parts of speech, word tokenization, and named entity detection. For more information, see the [NLTK Forum](http://www.nltk.org/){:target="_blank"}.

> [!NOTE]
> NLP API is deprecated since Tizen 8.0 and will be removed after two releases without any alternatives.

The main features of the [Tizen.Nlp](/application/dotnet/api/TizenFX/latest/api/Tizen.Nlp.html) namespace include the following:

-   Word tokenize support

    You can get tokens from a sentence, the type of return is [WordTokenizeResult](#wordtokenize). 
    This method breaks up the sentence into words and punctuation.

-   Part-of-speech support

    You can get tokens and tags from a sentence, the type of return is [PosTagResult](#postag). This method breaks up the sentence into words and punctuation with tag attributes.

-   Named entity recognizer support

    You can get tokens and tags from a sentence, the type of return is [NamedEntityRecognitionResult](#nechunk). This method breaks up the sentence into words and punctuation with tag attributes.

-   Language detect support

    You can get language from a sentence, the type of return is [LanguageDetectedResult](#langdetect). This method is used to detect the language of a sentence.


## Prerequisites

To enable your application to use the NLP functionality, follow the steps below:

1.  To use the [Tizen.Nlp](/application/dotnet/api/TizenFX/latest/api/Tizen.Nlp.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
       <privilege>http://tizen.org/privilege/datasharing</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the `Tizen.Nlp` namespace, include it in your application:

    ```csharp
    using Tizen.Nlp;
    ```
<a name="wordtokenize"></a>
## Receive WordTokenize tokens

To receive the tokens from sentence, follow the steps below:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the NLP service on init of app:

    ```csharp
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the WordTokenizeAsync(string msg) in a async task method:

    ```csharp
    public async Task OnTokenButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.WordTokenizeAsync(msg);
        WordTokenizeResult wr = await ret;
        ..
    }
    ```

3.  When NLP object is no longer needed, call Dispose() to release the resource of NLP:

    ```csharp
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```

<a name="postag"></a>
## Receive PosTag tokens and tags

To receive the tokens and tags from sentence, follow the steps below:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the NLP service on init of app:

    ```csharp
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the PosTagAsync(string msg) in a async task method:

    ```csharp
    public async Task OnPosButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.PosTagAsync(msg);
        PosTagResult pr = await ret;
        ..
    }
    ```

3.  When NLP object is no longer needed, call Dispose() to release the resource of NLP:

    ```csharp
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```

<a name="nechunk"></a>
## Receive named entity tokens and tags

To receive the tokens and tags information from sentence, follow the steps below:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the NLP service on init of app:

    ```csharp
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the NamedEntityRecognitionAsync(string msg) in a async task method:

    ```csharp
    public async Task OnTokenButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.NamedEntityRecognitionAsync(msg);
        NamedEntityRecognitionResult nr = await ret;
        ..
    }
    ```

3.  When NLP object is no longer needed, call Dispose() to release the resource of NLP:

    ```csharp
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```

<a name="langdetect"></a>
## Detect language

To detect the language from sentence, follow the steps below:

1.  Construct NaturalLanguageProcess on OnCreate(), and connect the NLP service on init of app:

    ```csharp
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the LanguageDetectAsync(string msg) in a async task method:

    ```csharp
    public async Task OnLangButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.LanguageDetectAsync(msg);
        LanguageDetectedResult lr = await ret;
        ..
    }
    ```

3.  When NLP object is no longer needed, call Dispose() to release the resource of NLP:

    ```csharp
    protected override void OnTerminate()
        {
         ..
         a.Dispose();
         ..
        }
    ```


## Related information
- Dependencies
  -   Tizen 5.0 and Higher
