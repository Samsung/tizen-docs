# Address Sanitizer

The Address Sanitizer is a profiling tool used to detect runtime memory errors in Tizen Native Applications. With this, you can discover whether specific parts of the code can potentially cause memory corruption at runtime. You can also avoid crashes or bugs during the execution of the application. The Address Sanitizer tool detects memory corruption at runtime by instrumenting the code during the application compilation. A program with no bugs does not crash when the Address Sanitizer tool is used, suggesting that the code is safe from potential memory corruption.

The Address Sanitizer tool can detect the following types of bugs:
*	Out-of-bounds accesses to heap and stack
*	Use-after-free
*	Use-after-return (to some extent)
*	Double free and invalid free

To get started with Address Sanitizer, see the guide [Detect Runtime Memory Errors with Address Sanitizer](../getting-started/test-profile-app-asan-lsan.md#detect-runtime-memory-errors-with-address-sanitizer)