# Tizen Compliance Program

The Tizen Compliance Program consists of the following parts:

- [Tizen Compliance Specification (TCS)](compliance-specification.md)  
A definitive set of requirements for Tizen compliant devices.
- [Tizen Compliance Tests (TCT)](compliance-test.md)  
A suite of tests that verify each of the requirements in the TCS.
- Tizen Compliance certification  
A formal review and acceptance of a device that has passed all of the tests and is fully Tizen compliant.

The Tizen Compliance Program ensures that devices and applications work correctly together, by setting out requirements for common behavior and providing a validation mechanism to show that the requirements are followed. The Tizen Compliance Program is valuable to the following audiences:

- **Application developers:** Know how to create compatible applications that work across multiple devices, and how Tizen devices behave.
- **Tizen device implementers:** Know how to implement a Tizen-compliant device by satisfying software and hardware requirements.
- **Carriers:** Know how to customize and enhance a device, while remaining within compliance guidelines.
- **End users:** Know that applications work on their device and are assured of a consistent user experience among compliant devices and applications.

To become Tizen compliant, a device must obtain the Tizen Compliance certification.

## Tizen Compliance Model

To be called Tizen compliant, a Tizen device implementer must obtain the Tizen Compliance certification for the device for at least 1 Tizen profile. This involves satisfying the requirements of the Tizen Compliance Specification, passing all of the Tizen Compliance Tests, then applying to the Tizen Association for certification.

A Tizen profile describes the requirements for a category of Tizen devices that have a common application execution environment. Applications are created for a specific target profile and can run on devices compliant with that profile.

Each Tizen profile is based on the Tizen Common libraries, which are a set of libraries common across all Tizen platforms. The set of libraries helps to unify multiple device categories by sharing common platform components.

The currently-available profiles are:

- Mobile: for handsets and tablets
- Wearable: for watches
- TV: for DTV/STB/IPTV systems

Additional profiles are expected in the future, potentially including:

- IVI: for In-Vehicle Infotainment systems


**Figure: Tizen profiles**

![Tizen profiles](media/tizen-profiles-small.png)

The Tizen Compliance Tests measure conformance to the requirements of a given Tizen profile.

## Compliance Certification Steps

To get a Tizen device certified:

1. A Tizen device implementer gets the [Tizen source code](https://review.tizen.org/git/) and creates a new Tizen device.
2. A Tizen device implementer obtains the compliance specification (TCS), compliance tests (TCT), and [Tizen branding request form](media/tizen_branding_request_form_for_tizen_mobile_profile_v1.0_1.pdf) ![PDF icon](media/application-pdf.png).
3. Once the new Tizen device passes 100% of the compliance tests, the Tizen device implementer submits the test results with a Tizen branding request form to the Tizen Association.
4. The Tizen Association reviews, approves, and certifies the device as Tizen compliant. Any technical review required to decide approval or failure is referred to the Tizen Steering Group by the Tizen Association.

## Feedback

The Tizen Project welcomes feedback and input on Tizen Compliance. If a Tizen device implementer has questions or concerns about the specification or compliance tests, they are welcome to discuss these on the [Tizen compliance mailing list](https://lists.tizen.org/listinfo/compliance).
