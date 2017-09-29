## How to use Samsung Certificates and deploy it in devices ##

### Install Samsung Certificate Extension ##

1. Execute ```Tizen Package Manager``` in Tools menu

![Tools menu](../image/SamsungExt_packagemgr.png)

2. Run ```Tizen Package Manager``` and move ```Configuration``` menu

![Tools menu](../image/SamsungExt_packagemgrRun.png)

![Package Manager](../image/SamsungExt_packagemgrConf.png)]

* (Only under Develop stage) Set the repository server for Samsung Cerificate Extension
   * Extension SDK > '+' > Add ```http://10.113.138.168/packages/sec_cert_extension```

![Set Repository](../image/SamsungExt_packagemgrSetrepo.png)

3. Install Samsung Certificate Manager

![Install Extension](../image/SamsungExt_install.png)

---

### Make Samsung Certificate ###

1. Execute ```Tizen Certificate Manager```

2. Click the plus icon ('+') to create a new profile

![Certificate Manager](../image/CertificateMgr_step1.png)

3. Select Samsung certificate

![Select Samsung Certificate](../image/SamsungExt_newProfile.png)

4. Refer [Certificate Manager](certificate-manager.md) from next step
   * Except for loging to Samsung account and adding DUIDs, almost is same between Samsung and Tizen

---

### Activate Samsung Certificate in option ###

1. Go to option menu (Tools > Options > Tizen > Certification)

![Option menu](../image/SamsungExt_option.png)

---

### Push ```device_profiler.xml``` (in case of using 1.0 distribute certificate)

1. Execute ```Tizen Device Manager``` and Connect device or emulator

![Device Manager](../image/SamsungExt_deviceMgr.png)

2. Click ```Permit to install applications``` in folder hierarchy window

![Permit to Install](../image/SamsungExt_permitToInstall.png)

3. Check the success message

![Success Message](../image/SamsungExt_success.png)

* If Device Manager shows below message, check that DUIDs which you added is compatible with connected devices

![Faile Message](../image/SamsungExt_failDUID.png)
