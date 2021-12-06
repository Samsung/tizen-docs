<!-- omit in toc -->
# TIC Frequently Asked Questions

- [What is the building block?](#what-is-the-building-block)
- [What are the "Easy" and "Advanced" mode?](#what-are-the-easy-and-advanced-mode)
- [How to get a recipe for TIC?](#how-to-get-a-recipe-for-tic)
- [How to add my applications to the Tizen binary?](#how-to-add-my-applications-to-the-tizen-binary)
- [How to add my platform packages to the Tizen binary?](#how-to-add-my-platform-packages-to-the-tizen-binary)
- [Can I find artifacts of TIC in my host PC?](#can-i-find-artifacts-of-tic-in-my-host-pc)

## What is the building block?

- The building block is the package which defines a set of combined packages for a specific propose.
  You can see pre-defined building blocks and their structure in [the repository of building blocks](https://git.tizen.org/cgit/tools/building-blocks/tree/?h=tizen).
  You can also define by yourself your own blocks by creating `.inc` files and adding them to the [building-block.spec](https://git.tizen.org/cgit/tools/building-blocks/tree/packaging/building-blocks.spec?h=tizen) file.

## What are the "Easy" and "Advanced" mode?

- If you select "Easy" mode, you can create exactly the same binaries as the officially released [Tizen binaries](http://download.tizen.org/releases/milestone/tizen/unified/latest/images/standard/). Also, you can create your own binary based on the official one by importing your own packages in this mode.

- On the other hand, in "Advanced" mode, you can customize your own binary from scratch. At first, you can select the architecture in the `Settings` tab,
  then you can select the building block packages one by one in the `Packages` tab.
  We recommand you to select a building block in `Preset` category first, and `Domain` category later. 
  It will help you to select essential packages.

## How to get a recipe for TIC?

- You can get the reference recipe by clicking the `Export` button in "Advanced" mode in the `Settings` tab, or by clicking the `Recipe` button in the `Images` tab if you have binaries already built.

## How to add my applications to the Tizen binary?

- You can add your application packages (`tpk` packages) in the `Settings` tab in both "Easy" and "Advanced" mode by clicking the `Import` button and selecting the radio button for `tpk` file.

## How to add my platform packages to the Tizen binary?

- You can add your platform module packages (`rpm` packages) in the `Settings` tab in "Advanced" mode. Just click the `Import` button and select the radio button for `rpm` file. However, in order to add your `rpm` packages to the binary, you have to check them in the tree view of the `Packages` tab.

## Can I find artifacts of TIC in my host PC?

- You can find them in the `tic-artifacts` directory in your home directory, if you use the [docker-compose](https://s3-us-west-1.amazonaws.com/tizenschool/257/docker-compose.yaml) file provided by us.
