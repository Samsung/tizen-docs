# Unit Test with Code Coverage

**Code Coverage** is a profiling tool used to measure how much of your application's source code is executed while running unit tests. It helps evaluate **code quality** and identify untested parts of your codebase.  

A higher coverage percentage indicates that most of your source code has been tested, which reduces the likelihood of undetected software bugs. By using **Unit Tests**, you can verify the correctness of your code, improve reliability, and maintain high software quality.

The **Tizen Studio Extension for Visual Studio** provides tools for:
- Creating, building, and editing unit tests  
- Running and analyzing test results  
- Measuring and visualizing code coverage  

---

## Native Application

For **Native Applications**, the Code Coverage feature in the **Tizen Extension for Visual Studio** is powered by the **`llvm-cov`** tool.  
It helps you:
- Detect code segments that are not covered by unit tests  
- Ensure that uncovered code does not cause runtime issues  
- Measure different types of coverage:
  - **Functional coverage**
  - **Statement coverage**
  - **Branch coverage**

The extension uses the **Google Test (gtest)** framework to create and execute test cases.  

> 📘 **Learn more:**  
> Get started with [Unit Test With Code Coverage for Native Applications on Visual Studio](../getting-started/test-profile-app-unit-test-code-coverage.md)

---

## Web Application

For **Web Applications**, you can also create and run unit tests within the **Tizen Extension for Visual Studio**.  
These tools allow you to:
- Write test cases for web projects  
- Execute them on an emulator or target device  
- View and analyze test results directly in Visual Studio

> 📘 **Learn more:**  
> Get started with [Unit Test for Web Applications on Visual Studio](../getting-started/web-app-unit-test.md)

---