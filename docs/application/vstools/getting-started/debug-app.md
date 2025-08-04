# Debugging Tizen Application

### Introduction
Debugging is a crucial step in application development that allows you to analyze, troubleshoot, and fix issues within your **.NET, Web, and Native** Tizen applications. This guide explains how to debug each type of project using Visual Studio.

## Debugging .NET Application
1. **Open the Source Code File**<br>
In Visual Studio, open the **.cs** file of your Tizen .NET application where you want to debug.

2. **Add a Breakpoint**<br>
Click on the **left margin** of the code editor next to the line where you want execution to pause. Alternatively, select a line and press **F9** to set a breakpoint.
<img alt="Debugging application" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_debug_dotnet.png"/>

3. **Start the Debugging Session**<br>
Navigate to **Debug > Start Debugging**. Or, click the **green arrow (emulator name)** in the toolbar.You can also press **F5** to begin debugging.


## Debugging Web Application

1. **Setting Up Google Chrome for Debugging**<br>
Before starting web application debugging in Tizen, ensure that the **Google Chrome** path is correctly set in **Visual Studio**. Go to **Tools > Options > Tizen > Tools**, and check if the Chrome path is specified. If not, manually enter the path to the Chrome executable (e.g., C:\Program Files\Google\Chrome\Application\chrome.exe) and click **OK** to save the changes.
<img alt="Setting Goggle Chrome path" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_debug_web_option.png"/>

2. **Open the Source Code File**<br>
In Visual Studio, open the **.js** file of your Tizen Web application where you want to debug.

3. **Add a Breakpoint**<br>
Click on the **left margin** of the code editor next to the line where you want execution to pause. Alternatively, select a line and press **F9** to set a breakpoint.
<img alt="Debugging application" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_debug_web.png"/>

4. **Start the Debugging Session**<br>
Navigate to **Debug > Start Debugging**. Or, click the **green arrow (emulator name)** in the toolbar.You can also press **F5** to begin debugging.


## Debugging Native Application

1. **Open the Source Code File**<br>
In Visual Studio, open the **.c** file of your Tizen Native application where you want to debug.

2. **Add a Breakpoint**<br>
Click on the **left margin** of the code editor next to the line where you want execution to pause. Alternatively, select a line and press **F9** to set a breakpoint.
<img alt="Debugging application" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_debug_native.png"/>

3. **Start the Debugging Session**<br>
Navigate to **Debug > Start Debugging**. Or, click the **green arrow (emulator name)** in the toolbar.You can also press **F5** to begin debugging.


By following these steps, you can efficiently debug **.NET, Web, Native, and Hybrid** applications in  Visual Studio. Debugging tools like breakpoints, inspectors, and step-through execution will help you analyze and fix issues before deployment.