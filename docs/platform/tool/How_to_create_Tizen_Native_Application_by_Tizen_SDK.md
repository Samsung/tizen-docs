Scope
-----

A How-to page to show the example about How to create and Customize
Tizen Native Application(OSP) with Tizen [SDK](SDK "wikilink").

Installation
------------

Download Install Manager and SDK image from
<https://developer.tizen.org/downloads/tizen-sdk>, for example, try it
in Ubuntu® 32bits Below shows example about how to create and Customize
Tizen Native Application by Tizen SDK step by step

Create Native Application by SDK sample
---------------------------------------

-   Run Tizen IDE, then New -\> Project\... -\> Tizen Native Project,
    then choose Sample -\> UiControls

<File:1.png>\|

-   Then Run -\> Run As -\> Tizen Native Application in Emulator image

See Animation button

<File:2.png>\|

It is pretty easy to create the application by SDK.

Customize Native Application by UI Builder and source code changing
-------------------------------------------------------------------

Now we start to check how to customize the Animation button control.

-   Go to Project Explorer, double click \[Project Name\] -\> res -\>
    screen-size-normal -\> IDF\_FORM\_ANIMATION.xml to launch the UI
    Builder.
-   Drag and Drop the new button, set the ID as
    \"IDC\_BUTTON\_TESTTIZEN\"

<File:3.png>\|

-   Then Run it to see the new UI control in Emulator

<File:4.png>\|

-   Customize the source code in src\\AnimationForm.cpp and
    inc\\AnimationForm.h to define the new Tizen::Ui::Controls::Button
    ID and its ActionId etc

<File:5.png>\| inc\\AnimationForm.h <File:6.png>\|
src\\AnimationForm.cpp

-   Customize the button press event in OnActionPerformed Function

<File:7.png>\| src\\AnimationForm.cpp

-   Click the testTizen button to see the result

<File:Screenshot> from 2013-09-15 21\_38\_28.png\|

Now the customization of new UI control and button press event handle
has been done, we can see it is pretty easy for application developer to
do the customization.

[Category:Tool](Category:Tool "wikilink")
