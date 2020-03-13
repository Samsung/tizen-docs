# Git Repository Structure

<style type="text/css">

#main:before, #main:after {
  content: "";
  display: block;
}

@media (max-width: 768px)
.docs-grid-container {
  margin: 12px auto 10px;
  background-position: 0px 6px;
}

.docs-grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
  background-color: #FFFFFF;
  margin: 10px auto 10px;
  padding: 0px;
  grid-gap: 0px;
  border-top: 1px solid rgba(200, 200, 200, 0.9);
  border-bottom: 1px solid rgba(200, 200, 200, 0.9);
  border-left: 1px;
  border-right: 1px;
  grid-template-rows: 85px 40px;

  display: -ms-grid;
  -ms-grid-columns: 1fr 1vw 1fr 1vw 1fr;
  -ms-grid-rows: 85 20px 20px;
}

.docs-grid-container > div {
  background-color: rgba(255, 255, 255, 0.9);
  text-align: left;
  padding:2px 2px;
  font-size: 14px;
}

/* Explicit placement for IE */
/* Omitting default value of -ms-grid-column: 1 and -ms-grid-row: 1 where possible */
.grid-item:nth-child(2) {
  -ms-grid-column: 3;
}

.grid-item:nth-child(3) {
  -ms-grid-column: 5;
}

h3.grid-title {
  text-transform: uppercase;
  font-size: 1.5em;
  line-height: 1;
  margin-top: 10px;
}
</style>

<section id ="main">
Tizen source codes run on the PC emulator and an ARM-based reference device. This release allows OEMs to begin considering Tizen platform for their commercial devices, and open source developers to look into Tizen to find what they can improve and contribute.

<div class="docs-grid-container">

<div class="grid-item">
<header>
  <h3 class="grid-title">Tizen Source</h3>
</header>
<p> Find all Tizen Components and Source Code. </p>
<a href="https://review.tizen.org/git/">Source Code ></a>
</div>

<div class="grid-item">
<header>
  <h3 class="grid-title">Code Review</h3>
</header>
<p>Download and review the latest Tizen code.</p>
<a href="https://review.tizen.org/gerrit">Code Review ></a>
</div>

<div class="grid-item">
<header>
  <h3 class="grid-title">Latest Snapshots</h3>
</header>
<p>Get the latest images, repos and kickstart files.</p>
<a href="http://download.tizen.org/releases/milestone/tizen/unified/">Snapshots ></a>
</div>

<div>
</section>

The following table describes the Git repository structure for Tizen 3.0 and higher.

| First depth | Second depth  | Third depth | Description                              |
| --------- | ---------- | --------- | ---------------------------------------- |
| Platform  |            |           | Platform component                       |
|           | upstream   |           | Code from upstream open source (Wayland, GStreamer, .NET Engine) |
|           | adaptation |           | Adaptation layer for supporting various kind of devices |
|           | framework  |           | Web Framework                            |
|           |            | web       | Web Framework (Web Engine)               |
|           | core       |           | Core Framework                           |
|           |            | api       | Native APIs for Core Framework           |
|           |            | csapi     | TizenFX API for Tizen .NET (C#) |
|           |            | webapi    | Web APIs for Web Framework               |
|           | kernel     |           | Kernel for supporting various kind of devices |
| Apps      |            |           | Common application                       |
|           | native     |           | Common native application                |
|           | Web        |           | Common Web application                   |
| Tools     |            |           | Tools constituting the Tizen platform development environment |
|           | Upstream   |           | Code from upstream open source (valgrind, oprofile) |
| Services  |            |           | Services constituting Tizen build services |
| SDK       |            |           | SDK                                      |
|           | ide        |           | IDE tools with which you can develop Tizen applications |
| SCM       |            |           | Privilege setting and metadata for configuration |
| Test      |            |           | Code for testing a profile (ex Common)   |
|           | tools      |           | Tools for testing a profile              |
| Profile   |            |           | Profile-specific                         |
|           | Mobile     |           | Mobile profile-specific                  |
|           |            | platform  | Platform component                       |
|           |            | apps      | Mobile profile-specific application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | wearable   |           | Wearable profile-specific                |
|           |            | platform  | Platform component                       |
|           |            | apps      | Wearable profile-specific application    |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | common     |           | Common profile-specific                  |
|           |            | platform  | Platform component                       |
|           |            | apps      | Common profile-specific application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | ivi        |           | IVI profile-specific                             |
|           |            | platform  | Platform component                       |
|           |            | apps      | IVI profile-specific application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
| Product   |            |           | Product-specific                         |
|           | upstream   |           | Code from upstream open source           |

> **Note**
>
> If the Git repository is not listed above, it does not belong to Tizen 3.0 and higher.
