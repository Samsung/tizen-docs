
# TizenX.ZLog (Utility)

**TizenX.ZLog** is a high-performance logging library designed specifically for performance-critical applications on Tizen. Its key feature is the **minimization of temporary string object creation** during logging operations, which significantly reduces garbage collector (GC) pressure.

## Key Features

### Zero-Allocation String Interpolation

ZLog uses an advanced string interpolation method that avoids allocating temporary string objects on the heap.

* **No Temporary Objects:** Drastically reduces GC pressure.
* **Memory Efficient:** Uses thread-local buffers for string building.
* **Stack-Based Allocation:** Utilizes stack allocation where possible.

### Comprehensive Logging Levels

ZLog supports all standard logging levels:

* Verbose: Detailed debugging information
* Debug: Debug-level messages
* Info: General informational messages
* Warn: Warning conditions
* Error: Error conditions
* Fatal: Critical error conditions

### Advanced Features

* **Automatic Caller Info:** Automatically captures the file path, function name, and line number of the log call.
* **UTF-8 Encoding:** Full support for UTF-8 encoding in log messages.
