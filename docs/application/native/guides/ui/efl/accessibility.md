# Accessibility

Accessibility features have become an essential part of high quality software. Their goal is to empower disabled users to use new technologies. This is especially important to low-vision and visually-impaired users who possibly have no access whatsoever to software unless it incorporates appropriate accessibility solutions.

Tizen provides accessibility features for developing applications for disabled users:

- [Accessibility Architecture](./accessibility-architecture.md)

  The accessibility implementation for Tizen platform is based on the Elementary ATSPI, which enables applications to interact with graphical Elementary components visible on the screen. For example, a screen reader can access the text in the labels and descriptions of any application running on the screen and read it to the user.

- [Configuring Accessibility on a Device](./accessibility-config.md)

  Tizen provides 2 accessibility features primarily aimed at low-vision and visually-impaired users. These accessibility solutions allow you to adjust the font size on the Tizen device and to use the built-in screen reader application.

- [Implementing Accessible Applications](./accessibility-implementation.md)

  You can make your application accessible by following good accessibility practices. Using an EFL Elementary sample application, you can see in practice how to implement readable components for the Screen Reader, and customize the UI reading order and the highlight frame appearance.

## Benefits of Accessibility

Adding accessibility features in your application brings various benefits:

- Using a universal design

  Developing products that can be used by everyone, including often neglected minorities, such as disabled or elderly users, is a good software design practice and as such must be reinforced whenever possible.

- Considering disabled users' needs

  Disabled users often find it difficult or even completely impossible to use regular applications. Putting a little effort into making your application accessible can make all the difference.

- Increasing the audience of your application

  Disabled people make up a considerable portion of society. It is estimated that 10 to 15% of the global population is disabled. In Europe alone, there are about 80 million people with disabilities. Making your application accessible can increase its potential audience.

- Distinguishing your application

  Many of the applications currently available on the market are not accessible. Making yours accessible positively distinguishes it from your competitors' products, and can create a marketing advantage.

- Complying with legal acts and policies

  Some organizations can be required by law or internal policies to make their products accessible. One of the examples  is Section 508 of the Rehabilitation Act of 1973 which obliges federal agencies in the United States to make their electronic and information technology accessible to disabled users.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
