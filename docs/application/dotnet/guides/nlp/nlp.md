# Natural Language Processing (Nlp)


Tizen enables you to use Natural Language Process (Nlp) functionalities, such as language detect, word_tokenize, lemmatize, ne_chunk, and pos_tag. Nlp is a subset of natural language toolkit that specifies an interface and a protocol for basic natural language processing. For more information, see the [nltk Forum](http://www.nltk.org/).

The main features of the Tizen.Nlp namespace include:

-   Word Tokenize suppport

    You can [get tokens from a sentence](#word_tokenize_get_tokens). the type of return is [WordTokenizeResult](#word_tokenize_result);

-   Part Of Speech support

    You can [get tokens and tags from a sentence](#pos_tag_get_tokens_tags). the type of return is [PosTagResult](#pos_Tag_result);

-   Named Entity Detection support

    You can [get tokens and tags from a sentence](#ne_chunk_get_tokens_tags). the type of return is [NamedEntityRecognitionResult](#ne_chunk_result);

-   Lemmatizing

    You can [get actual word from a word](#lemmatize_get_actual_word). the type of return is [LemmatizeResult](#lemmatize_result);

-   Language Detect support

    You can [get language from a sentence](#language_detect_get_language). the type of return is [LanguageDetectedResult](#langdetect_result);

<a name="word_tokenize_get_tokens"></a>
## Word Tokenize
this method break up the sentence into words and punctuation.


<a name="pos_tag_get_tokens_tags"></a>
## Part Of Speech
this method break up the sentence into words and punctuation with tag attributes.


<a name="ne_chunk_get_tokens_tags"></a>
## Named Entity Detection
this method break up the sentence into words and punctuation with tag attributes.


<a name="lemmatize_get_actual_word"></a>
## Lemmatizing
this method use to get actual word from a word.

<a name="language_detect_get_language"></a>
## Language Detect
this method use to detect the language of sentence.




## Prerequisites

To enable your application to use the Nlp functionality:

1.  To use the [Tizen.Nlp](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Nlp.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
       <privilege>http://tizen.org/privilege/datasharing</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the `Tizen.Network.Nlp` namespace, include it in your application:

    ```
    using Tizen.Network.Nlp;
    ```

<a name="word_tokenize_result"></a>
## To get the tokens of sentence 

To recieve the tokens from sentence:

1.  Construct an NaturalLanguageProcess on OnCreate(), and Connect the Nlp service on init of app :

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the WordTokenizeAsync(string msg) in a async Task method:

    ```
    public async Task OnTokenButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.WordTokenizeAsync(msg);
        WordTokenizeResult wr = await ret;
        ..
    }
    ```

3.  When nlp object is no longer needed, call Dispose() to release resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```


<a name="pos_Tag_result"></a>
## To get the tokens and tags of sentence 

To recieve the tokens and tags from sentence:

1.  Construct an NaturalLanguageProcess on OnCreate(), and Connect the Nlp service on init of app :

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the PosTagAsync(string msg) in a async Task method:

    ```
    public async Task OnPosButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.PosTagAsync(msg);
        PosTagResult pr = await ret;
        ..
    }
    ```

3.  When nlp object is no longer needed, call Dispose() to release resource of Nlp:

    ```
    protected override void OnTerminate()
        {
         ..
         nlp.Dispose();
         ..
        }
    ```


<a name="ne_chunk_result"></a>
## To get the tokens and tags of sentence 

To recieve the tokens and tags from sentence:

1.  Construct an NaturalLanguageProcess on OnCreate(), and Connect the Nlp service on init of app :

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the NamedEntityRecognitionAsync(string msg) in a async Task method:

    ```
    public async Task OnTokenButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.NamedEntityRecognitionAsync(msg);
        NamedEntityRecognitionResult nr = await ret;
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




<a name="lemmatize_result"></a>
## To get the actual word of sentence 

To recieve the actual word from sentence:

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



<a name="langdetect_result"></a>
## To get the language of sentence 

To recieve the language from sentence:

1.  Construct an NaturalLanguageProcess on OnCreate(), and Connect the Nlp service on init of app :

    ```
    protected override void OnCreate
    {
        ..
        nlp = new NaturalLanguageProcess();
        Task task = nlp.Connect();
        ..
    }
    ```

2.  Call the LanguageDetectAsync(string msg) in a async Task method:

    ```
    public async Task OnLangButtonPressedAsync(string msg)
    {
        ..
        var ret = nlp.LanguageDetectAsync(msg);
        LanguageDetectedResult lr = await ret;
        ..
    }
    ```

3.  When it is no longer needed, call Dispose() to release resource of Nlp:

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
