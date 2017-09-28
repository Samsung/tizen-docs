# How to develop Eclipse Theme Extension Plugin

## Step 1
- From Eclipse 4.x, you can contribute themes via CSS files
- Extension point
  - org.eclipse.e4.ui.css.swt.theme
  
  ```css
    id* : Id for the theme. 
          It is possible use the same id multiple times but then it has to have distinct OS and WS filter values
    label* : the label used when displayed to the user
    basestylesheeturi* : the base stylesheet uri relative to the bundle
    os : the operating system the theme is applicable for or empty to apply on all
    ws : the windowing system the theme is applicable for or empty to apply to all
    os_version : the version the operating system the theme is applicable for or empty to apply on all. 
            The value can be a comma-separated string to specify multiple versions.
  ```
  - For Example
  
  ```xml
  <extension point="org.eclipse.e4.ui.css.swt.theme">
   <theme
         basestylesheeturi="css/tizen.css"
         id="tizen.theme.id"
         label="Tizen">
   </theme>
   </extension>
  ```
## Step 2
- Describe a CSS file with Theme information
    - It is possible to inherit the existing Eclipse Theme using the `@import` syntax.
    
- For Example

```css
@import url("e4_basestyle.css");
.MTrimmedWindow {
    background-color: rgb(148,164,164) rgb(148,164,164) 100%;
    margin-top: 4px;
    margin-bottom: 4px;
    margin-left: 4px;
    margin-right: 4px;
}
.MPartStack {
    tab-renderer: 
    url('bundleclass://org.eclipse.e4.ui.workbench.renderers.swt/org.eclipse.e4.ui.workbench.renderers.swt.CTabRendering');
    swt-unselected-tabs-color: #FFFFFF #FFFFFF #FFFFFF 100% 100%;
    outer-keyline-color: #CDE8EC;
    inner-keyline-color: #FF0000;
    tab-outline: #B6BCCC;
    padding: 0px 9px 10px;
    shadow-visible: false;
}
 
.MPartStack.active {
    swt-unselected-tabs-color: #CDE8EC #CDE8EC #FFFFFF 100% 100%;
    inner-keyline-color: #FFFFFF;
    tab-outline: #A2C2C8;
    shadow-visible: false;
}
#org-eclipse-ui-main-toolbar {
    background-color:rgb(173,235,244) 100%;
}
#org-eclipse-ui-main-toolbar #PerspectiveSwitcher {
    background-color: rgb(179,192,192) rgb(148,164,164) 100%;
    handle-image: none;
    eclipse-perspective-keyline-color: rgb(10,89,101);
}
#org-eclipse-ui-trim-status{
    background-color:rgb(198,220,227);
}
```
    
## Step 3
  - Preference
    - Once the plug-in is loaded, you can select the theme contributed by the Preference.
    
    ![](/docs/image/theme-ext.png)
    
## Advanced
- If you want to apply the theme differently to each OS
```xml
<extension
    point="org.eclipse.e4.ui.css.swt.theme">
    <theme
        basestylesheeturi="css/e4_default.css"
        id="org.eclipse.e4.ui.css.theme.e4_default.noos"
        label="Default Theme">
        </theme>
    <theme
        basestylesheeturi="css/e4_classic_winxp.css"
        id="org.eclipse.e4.ui.css.theme.e4_classic"
        label="Classic">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_gtk.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="GTK"
        os="linux">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_mac.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="Mac"
        os="macosx">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_win7.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="Windows 7"
        os="win32"
        os_version="6.1">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_winxp_blu.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="Windows XP Blue"
        os="win32">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_winxp_olv.css"
        id="org.eclipse.e4.ui.css.theme.e4_default.xpolive"
        label="Windows XP Olive"
        os="win32">
    </theme>
    <theme
        basestylesheeturi="css/e4_classic_win7.css"
        id="org.eclipse.e4.ui.css.theme.e4_classic"
        label="Windows 7 Classic"
        os="win32"
        os_version="6.1">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_gtk.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="Solaris"
        os="solaris">
    </theme>
    <theme
        basestylesheeturi="css/e4_default_gtk.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="AIX"
        os="aix">
    </theme>
    <theme
        basestylesheeturi="css/e4_classic_winxp.css"
        id="org.eclipse.e4.ui.css.theme.e4_default"
        label="HPUX"
        os="hpux">
    </theme>
</extension>
```

## Tips
- If you do not launch Eclipse Launch after modifying CSS, press Restore Defaults button and select Tizen Theme again, Eclipse will reflect the changed design.
