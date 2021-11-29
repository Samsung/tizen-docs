<!-- omit in toc -->
# TIC Frequently Asked Questions

- [What is for the easy mode and the advanced mode ?](#what-is-for-the-easy-mode-and-the-advanced-mode-)
- [What is the building block ?](#what-is-the-building-block-)
- [How to get a recipe for TIC ?](#how-to-get-a-recipe-for-tic-)
- [How to add my application to the Tizen binary ?](#how-to-add-my-application-to-the-tizen-binary-)
- [How to add my platform packages to the Tizen binary ?](#how-to-add-my-platform-packages-to-the-tizen-binary-)
- [Can I find artifacts of TIC in my host PC ?](#can-i-find-artifacts-of-tic-in-my-host-pc-)

## What is for the easy mode and the advanced mode ?

- If you select the easy mode, and click the `apply changes` button, the configurations for building binary are same as the [Tizen public binaries](http://download.tizen.org/releases/milestone/tizen/unified/latest/images/standard/).
  So, you can make same binaries as the Tizen public binaries.

- Regarding to the advanced mode, you can combine packages as you want by selecting building blocks. At first, you can select the architecture in the `Setting` tab,
  And then, you can select building block packages in order by category and step by step in `Packages` tab.

## What is the building block ?

- The building block is the package which defines a set of combined packages for specific propose.
  You can see pre-defined building blocks and the structure of them in [the repository of building blocks](https://git.tizen.org/cgit/tools/building-blocks/tree/?h=tizen).
  You also can define by yourself your own blocks by creating `.inc` files and add them to [building-block.spec](https://git.tizen.org/cgit/tools/building-blocks/tree/packaging/building-blocks.spec?h=tizen) file

## How to get a recipe for TIC ?

- You can get the reference recipe by clicking the `Export` button in the advanced mode in the `Setting` tab, or by clicking the `Recipe` button in the `Images` tab if you have binaries already built.

## How to add my applications to the Tizen binary ?

- You can add your application packages(`tpk` packages) in `setting` tab in both of the easy and advanced mode by clicking the `import` button and selecting the radio button for `tpk` file.

## How to add my platform packages to the Tizen binary ?

- You can your platform module packages(`rpm` packages) in `setting` tab in the advanced mode, by clicking the `import` button and selecting the radio button for `rpm` file . But, to add your `rpm` packages to the binary, you have to check them in the tree view of the `Packages` tab.

## Can I find artifacts of TIC in my host PC ?

- You can find them in the `tif-artifaces` directory in your home directory, if you use `docker-compose`(https://s3-us-west-1.amazonaws.com/tizenschool/257/docker-compose.yaml) file provided by us.
