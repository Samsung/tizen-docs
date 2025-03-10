# Machine Learning Inference

Machine learning (ML) inference introduces how you can easily invoke the neural network model and get the inference output result effortlessly and efficiently.

You can use the following machine learning features in your .NET applications:

- [SingleShot](singleshot.md)

  You can use the `Tizen.MachineLearning.Inference.SingleShot` class, to load the existing neural network model or your own specific model from the storage.
  After loading the model, you can invoke it with a single instance of input data. Then, you can get the inference output result.

- [Pipeline](pipeline.md)

  You can use the `Tizen.MachineLearning.Inference.Pipeline` class to manage the topology of data and the interconnection between processors and models.
  Unlike the SingleShot class, you can compose a complex pipeline for changing media format and connecting multiple neural network models in the stream.

  > [!NOTE]
  > This feature is available in the .NET APIs since Tizen 6.0.

## Related information
- Dependencies
  - Tizen 5.5 and Higher

- API References
  - [Tizen.MachineLearning.Inference](/application/dotnet/api/TizenFX/latest/api/Tizen.MachineLearning.Inference.html) namespace
