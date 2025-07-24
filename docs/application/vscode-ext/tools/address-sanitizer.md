# Address Sanitizer

- The Address Sanitizer is a tool that helps find memory errors in Tizen Native apps. It checks if certain parts of the code might cause memory problems while running. This tool can prevent crashes or bugs during app use. It works by adding extra code during app compilation. If the app doesn't crash with the Address Sanitizer, it means the code is safe from memory issues. The tool can find different types of bugs. The Address Sanitizer tool can detect the following types of bugs:

- Out-of-bounds accesses to heap and stack
- Use-after-free
- Use-after-return (to some extent)
- Double free and invalid free

To get started with Address Sanitizer, see the guide [Detect Runtime Memory Leaks with Address Sanitizer](../getting-started/test-profile-app/asan-lsan.md#to-detect-runtime-memory-errors-with-address-sanitizer)