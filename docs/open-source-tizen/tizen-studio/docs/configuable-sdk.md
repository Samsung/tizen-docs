
# About Configurable SDK
One of the main goals of the Tizen 4.0 platform is Configurablity.
It does not limit the platform type to a device or profile. Vendor or platform developers can customize the functionality they need.
Tizen Studio provides a feature to develop applications in a configurable tizen platform environment.

## New Feature in Tizen Platform 4.0

- Rather than providing a package according to the profile, the user selects a package suitable for the device type
- Choosing a package for a device type is called a recipe.
- To facilitate recipe, API and Feature-set package selection function is provided.
- It also provides a single build environment
![](image/configuable_sdk/tizen-platform-configurable.PNG)

## Provide Tizen Custom Platform Image
- Support Tizen Image Creator System
- Open System (Requirement Collection, Bug Report Process etc)
- Build Tool – Support for various ARM devices for individual developers and Team developers
- Guide document – Development Environment Setup, Component by Technical Article
- An environment where you can select a desired feature and develop a product
![](image/configuable_sdk/tizen-platform-image-creator.PNG)

# Tizen Studio for the Configurable SDK
- Tizen Studio also provides the main features of the same life cycle of the App as the existing Profile (Mobile, Wearable, TV) to the Configurable SDK.
- The Configurable SDK is installed and managed by the Extension SDK from Pakcage Manager.
  - Create new project
  - Config.xml, manifest.xml validation
  - API code assist
  - Build
  - Packaging
  - Run As
  - Debug As

![](image/configuable_sdk/configurable-tizen-flow.PNG)

## Step 1 : Installing the Configuralbe SDK
To install Extension Configurable SDK, proceed as follows.

1. Setting IOT-Headed-4.0 in Package Manager\
    a. Run Package Manager.\
    b. Configuration > Extension SDK > Click (+) \
    c. Enter Extension Name and Repository address > Click OK\

![](image/configuable_sdk/package-manager-config.PNG)

2. Install IOT-Headed-4.0\
    a. Click IOT-Headed-4.0 Install on the Extension SDK tab.\
![](image/configuable_sdk/package-manager-install.PNG)

## Step 2 : Create the Project

1. Run Tizen Studio
2. Select the File > New > Tizen Project
![](image/configuable_sdk/create-project-new.PNG)

3. Profile & Version > Select the Custom Box > Select Iot-Headed v4.0 and Click the Next
![](image/configuable_sdk/create-project-profile-select.PNG)

4. Application Type >  Select the Native Box 
![](image/configuable_sdk/create-project-apptype-select.PNG)

5. Template > Select the Basic UI Template and Click the Next
![](image/configuable_sdk/create-project-template-select.PNG)

6. Enter the project name and click the Finsh, 
![](image/configuable_sdk/create-project-finish.PNG)

7. When the project creation is completed, the BasicUI project is created in the Project Explorer in Iot-headed-4.0 as follows.
![](image/configuable_sdk/create-project-explorer.PNG)

## Step 3 : Build and Packaging Your Application

1. Right-click on the project created in the Project Explorer and select Build and signed package.
![](image/configuable_sdk/build-packaging.PNG)

2. BasicUI > Debug > org.example.basicui-1.0.0-arm.tpk is generated.
![](image/configuable_sdk/build-packaging-result.PNG)

