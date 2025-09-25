# Leak Sanitizer

The Leak Sanitizer is a profiling tool designed to identify runtime memory leaks in Tizen Native applications. It helps developers pinpoint sections of code that may lead to memory leaks during execution. By instrumenting the code during application compilation, the tool can detect memory leaks at runtime. If the program runs without crashing under Leak Sanitizer, it indicates that the code is free from potential memory leaks. This ensures safer and more efficient memory management in Tizen applications.

To get started with Leak Sanitizer, see the guide [Detect Runtime Memory Leaks with Leak Sanitizer](../getting-started/test-profile-app/asan-lsan.md#to-detect-runtime-memory-errors-with-leak-sanitizer)
