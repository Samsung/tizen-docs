
# Web/Native IDE extension development guide

### Tizen IDE extension overview
- The Tizen IDE is based on [Eclipse](http://www.eclipse.org/) and can be extended based on Eclipse's plugin extension platform.
- Therefore, the extensible part of the Eclipse platform can contribute.
    - Technically, all of the functions of Tizen IDE that provide extension points in the Eclipse Platform can be extended and added / changed.
    - For example Menu, Context Menu, Toolbar, View, Editor etc ...
- Note that the Tizen IDE has modified some of the icon images for Tizen Studio identity and modified some of the Eclipse platform upstream sources to customize unnecessary parts of menus and settings, so some extension points may not work properly . 

### Tizen IDE extension Development Guide
- Tizen IDE extension development method is basically same as Eclipse plugin development method.
- If you are new to Eclipse plugin development or need more information, please refer to the following site.
    - [Eclipse Official Help](https://help.eclipse.org/neon/index.jsp?topic=%2Forg.eclipse.platform.doc.isv%2Fguide%2Ffirstplugin.htm)
    - [Eclipse expert Lars Vogella's blog](http://www.vogella.com/tutorials/EclipsePlugin/article.html)
    
### Prepare the development environment
- For Tizen IDE development, Eclipse PDE development environment should be prepared by default, and local IDE source should be cloned.
1. Preparing the Eclipse Plugin Development Environment (PDE)
2. Fork the Tizen IDE source

### Tizen IDE extension point

![](/docs/image/ext-point.png)   
    
Tizen IDE provides the following extension points for IDE functionality:
---
1. Launch(Web)
    - Web app. Application Provides extension points for launch (Run As) and unittest launch
        - org.tizen.web.zimlaunch.launchStepFactory
            - web application launch step
             ![](/docs/image/lauch-ext.png)   
        - org.tizen.web.unittest.launchStepFactory
            - web application unit test launch step
     
2. Certificate
    - Provides extension points for Tizen certificate generation
    - Example : [Modifying the text in Certificate Manager](example-web-certi-ext.md)
    
3. ETC
    - Provided extension-point Lists
        - org.eclipse.ui.commands
        - org.eclipse.ui.handlers
        - org.eclipse.ui.bindings
        - org.ecilpse.ui.menus
        - org.ecilpse.ui.popupMenus
        - org.eclipse.ui.newWizards
        - org.eclipse.ui.editors
        - org.ecilpse.ui.propertyPages
        - org.eclipse.ui.perspectiveExtensions
        - org.eclipse.help.toc 
    - Example : [Modifying the Theme in IDE](https://github.sec.samsung.net/RS-TizenStudio/home/blob/master/docs/example-web-theme-ext.md)
    
※ Please contact us if you have any additional extension points.
