# Application Start Process

You can show several screens of information to users when they initially launch your app.

![](media/pattern_9.1.0-850x187.png)  
*Apps provide essential and optional information to users during the initial launch.*

## Launch screens

Launch screens are shown when the user launches your app. Avoid leaving the screen blank as the home screen loads. Instead, display a logo, image, or brief animation that shows your brand identity. Launch screens are unnecessary when the app is already running or is launched through another app.

![](media/pattern_9.1.1-850x174.png)  
*Express your app's identity straight away.*


> **Tip**  
> Avoid using text in launch screens except as part of a brand logo.


## Welcome pages

Welcome pages appear after the launch screen, and provide the initial settings procedures or a tutorial. Keep the sequence of the welcome pages short and simple. If you have multiple pages to present, guide users to the next page with a Next button and complete the welcome process with a Done button.

![](media/9.1.2-900x186.png)  
*The wlecome pages provide initial setting procedures.*

## Legal nformation

Legal information appears after the welcome pages. There are 2 types of legal information:

-   Essential information like terms and conditions that users must agree to
-   Optional information like disclaimers and warnings

 

-   **Terms and conditions (essential)**

    These govern the contract between you and your users and seek the user's agreement on the rules for using the service. Users are informed that they may be denied the service or prosecuted if they don't follow the rules or abuse any information provided by the app. An Agreement checkbox should be included below the terms and conditions, with Next and Start buttons that only become tappable only after the user has checked the checkbox.

    ![](media/pattern_9.1.3_1-850x174.png)  
    *Terms and conditions provide a checkbox below the content so users can select agree/disagree.*

-   **Disclaimer (optional)**

     Disclaimers show a legal statement on device misuse or defects. It's only shown, as a pop-up, once when the user initially launches the app. Since disclaimers do not require the user's agreement, provide a Confirm button at the bottom of the screen. You can provide an additional link that leads to the Privacy Policy if you choose.


  ![](media/pattern_9.1.3_2-850x174.png)  
    The disclaimer provides a Confirm button at the bottom of the screen.

-   **Warnings (optional)**

    Warnings alert users to conditions that might cause them a problem such as privacy or traffic safety. You can make them appear every time the user starts the app. Warning pages disappear and transition to the next screen when a user taps anywhere on the screen.

-   **Privacy Policy (optional)**

    The Privacy Policy seeks the user's agreement on the rules regarding personal data protection. It must include the types of personal data your app collects, the purpose of collection and use, a list of third parties to whom the data will be disclosed (e.g. business partners), technical measures for personal data protection, and the people or departments responsible for personal data. Agree and Disagree options must be provided at the bottom of the screen with a checkbox to allow for selection.

-   **End User License Agreement (optional)**

    The End User License Agreement (also known as Software License Agreement), is a legal contract between the app developer and the user. The user agrees to pay for the service the software provides and abide by the rules of the agreement. Agree and Disagree options must be provided at the bottom of the screen with a checkbox to allow for selection.
