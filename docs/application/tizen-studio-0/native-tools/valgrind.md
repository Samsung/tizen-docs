# Profiling Memory with Valgrind

Valgrind is a memory profiling tool, which can detect memory errors and memory leaks in an application. The Valgrind tool consists of a core module and various debugging and profiling tools. For more information, see the [Valgrind User Manual](http://valgrind.org/docs/manual/manual.html).

The Tizen Studio supports the following tools:

- Memcheck

  Memcheck is a default tool that detects memory errors, memory leaks, incorrect freeing of memory, and usage of undefined or uninitialized values.

- Massif

  Massif is a heap profiler to measure the amount of memory your program uses.

The Tizen Studio provides the interface for [running Valgrind with your application](../../native/tutorials/process/performance.md#running-valgrind) easily. After performance profiling is terminated, you can see the [profiling result](../../native/tutorials/process/performance.md#viewing-valgrind-result) and use it for improving performance.

> **Note**  
> Valgrind is not supported since Tizen 3.0. As an alternative, you can use the [Leak Sanitizer](../common-tools/dynamic-analyzer/memory-analysis.md#leaks) for heap allocation tracing.

## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
