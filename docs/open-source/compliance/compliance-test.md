# Tizen Compliance Tests

## 1 Overview

Tizen Compliance Tests (TCT) verify conformance to the [Tizen Compliance Specification](https://source.tizen.org/compliance/compliance-specification) (TCS). These tests are intended to be used by Tizen device implementers to enable the Tizen-compliant development environment for Tizen application developers.

## 2 TCT Introduction

Tizen Compliance Tests consist of Web TCT and Native TCT, which include test suites and tools for testing on the Tizen web stack and the native stack, respectively.

### 2.1 Web TCT

### 2.1.1 Bill of Materials

Web TCT is a set of tools and test suites to test the web requirements defined in the Tizen Compliance Specification. It includes:

- Web Test Suites cover Tizen Web APIs, Tizen Web Runtime, Web UI Framework, and device capability features.
- Web TCT Manager is a GUI tool that runs on the host machine, managing the whole testing procedure, from plan to test report, supporting both automated and manual web testing.
- Web TCT Behavior Test tool is used to test behavior of hardware and software features in interactive mode.
- Web TCT Shell is a lightweight console tool that runs on the host machine, allowing users to debug single failed test cases or trigger TCT testing with an existing test plan. Web TCT Shell is an optional tool.
- User guide documents and installation scripts.

[![Web TCT Workflow](https://source.tizen.org/sites/default/files/page/webtct_workflow.png)](./media/webtct_workflow.png)

### 2.1.2 Using Web TCT

Make sure the prerequisites are met before starting:

- Host machine with one of the following Linux distribution versions installed:

  ​

  - Ubuntu 12.04 (32-bits)
  - Ubuntu 12.04 (64-bits)
  - Ubuntu 12.10 (32-bits)
  - Ubuntu 12.10 (64-bits)

- Host machine is connected to the internet through Ethernet or WiFi, and attached to the Target device through a USB line.

- Target device is installed with a Tizen image and is bootable.

- Target device supports to unzipping packages

To install and use web TCT, perform the following procedure:

- Download the Web TCT tarball package to the Host machine.
- Untar the Web TCT tarball under your work folder on the Host machine.
- Follow the Web_TCT_<version>_User_Guide_v1.0.pdf in ./doc/ folder to set up a Host machine and a Target device, and run Web TCT.
- Use Web TCT Manager to run all Web TCT tests and show the test results automatically.
- Use Web TCT Behavior Test tool on a Target device to run manual test cases step-by-step

### 2.2 Native TCT

### 2.2.1 Bill of Materials

Native TCT is a set of tools and test cases to test Native requirements defined in the Tizen Compliance Specification (TCS). It includes:

- Native TCT covers Signature, Native API, App Control, Privilege, Resource, Device Capability Features
- Native TCT consists of TCT, TBT(Tizen Behavior Test), EFL-UTC Packages
- TCT manager is a GUI tool to manage whole tests, from planning to results
- TCT Package includes Unit Test Case, Integration Test Case, Compatibility Test Case TCT
- There are separate TBT(Tizen Behavior Test), EFL-UTC application to test the behavior of hardware and software features in interactive mode                   

### [![img](https://source.tizen.org/sites/default/files/images/nativetct_workflow.png)](./media/nativetct_workflow.png)

### 2.2.2 Using Native TCT

Make sure the prerequisites are met before starting:

- Make a USB connection between the Target and the Host
- The Target device is installed with a Tizen image and is bootable
- The Target device supports the sdb command

To install and use Native TCT, perform this procedure:

- Download the Native TCT, TBT, EFL-UTC Packages
- Follow the User_Guide_pdf in each projects’ folder to set up the Host and the Target, then run the Native TCT
- The TCT manager runs all the TCT TCs and shows test results automatically
- Install Native TBT onto the Target and run manual test cases step-by-step
- Install Native EFL-UTC onto the Target and run automated test cases.

## 3 TCT Report Submission

TCT will generate following test reports:

- Web TCT Test Report
- Web TCT Behavior Test Report
- Native TCT Test Report
- Native TBT Test Report
- Native EFL Test Report

Follow the [Compliance Program Steps ](https://source.tizen.org/compliance)to submit the test reports above.

## 4 TCT Releases

- [http://download.tizen.org/tct/](http://download.tizen.org/tct/)

