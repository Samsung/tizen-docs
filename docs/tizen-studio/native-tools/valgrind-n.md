# Profiling Memory with Valgrind
## Dependencies

- Tizen Studio 1.0 and Higher


Valgrind is a memory profiling tool, which can detect memory errors and memory leaks in an application. The Valgrind tool consists of a core module and various debugging and profiling tools. For more information, see the [Valgrind User Manual](http://valgrind.org/docs/manual/manual.html).

The Tizen Studio supports the following tools:

- Memcheck

  Memcheck is a default tool that detects memory errors, memory leaks, incorrect freeing of memory, and usage of undefined or uninitialized values.

- Massif

  Massif is a heap profiler to measure the amount of memory your program uses.

The Tizen Studio provides the interface for [running Valgrind with your application](../../../org.tizen.training/html/native/process/performance_n.htm#running_valgrind) easily. After performance profiling is terminated, you can see the [profiling result](../../../org.tizen.training/html/native/process/performance_n.htm#valgrind_result) and use it for improving performance.

**Note**
Valgrind is not supported since Tizen 3.0. As an alternative, you can use the [Leak Sanitizer](../common-tools/da-memory.md#leaks) for heap allocation tracing.