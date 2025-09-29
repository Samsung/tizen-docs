# Tizen System Logger

Tizen has a basic system logger called `dlog`. For instructions on how to read them later via CLI tools please check out [the `dlogutil` section of the general dlog guide](../../../native/guides/error/system-logs.md#dlogutil). Other C# guides for other specific functionality will also usually contain logging examples if you'd like to know more.

### Basic concepts

Other than the message contents, a dlog log has two main traits: a priority level, and a string "tag":
 * priority is one of a few named, ordered levels such as "error" or "verbose". See [the list in the native guide](../../../native/guides/error/system-logs.md#message). It is used for categorizing and filtering unimportant logs out.
 * tag is an arbitrary string intended to help identify who sent the log, such as "MY_EXAMPLE_APP". Also used for filtering.

### Example

Nothing clever here, the priority level is just the function name within `Tizen.Log`, and the tag is the first arg. Apply priority level as appropriate, generally keep the tag consistent but unique to your app such that when reading you'd see all of your logs and no others.

```csharp
float ExampleReciprocal (float x) {
	if (flag_verbose)
		Tizen.Log.Verbose("MY_RECIPROCAL_CALCULATOR", "Calculating 1 / {}...", x);

	if (x == 0.0f) {
		Tizen.Log.Error("MY_RECIPROCAL_CALCULATOR", "Cannot divide by 0");
		throw new Exception(...);
	}

	var result = 1.0f / x;

	Tizen.Log.Debug("MY_RECIPROCAL_CALCULATOR", "Result was {}", result);
	return result;
}
```

