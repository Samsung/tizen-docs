# Overview

<style>
/* Reset */

html, body, div, span, applet, object, iframe, {
		font-size: inherit;
		vertical-align: baseline;
	}
	body {
		font-size: inherit;
		-webkit-text-size-adjust: none;
	}

/* Box Model */

	*, *:before, *:after {
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}

/* Section/Article */

	section.special, article.special, header.special {
		text-align: center;
	}

/* Feature */

	.features {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-wrap: wrap;
		-webkit-flex-wrap: wrap;
		-ms-flex-wrap: wrap;
		flex-wrap: wrap;
		-moz-justify-content: center;
		-webkit-justify-content: center;
		-ms-justify-content: center;
	}

	.feature {
		padding: 1em 1em 1em 1em;
		margin-left: -1px;
		margin-top: -1px;
		width: 33.33333%;
	}


		@media screen and (max-width: 1280px) {

			.feature {
				padding: 2em 1.5em 0.1em 1.5em;
			}

		}

		@media screen and (max-width: 736px) {

			.feature {
				padding: 2em 1em 0.1em 1em;
				width: 50%;
			}

		}

		@media screen and (max-width: 480px) {

			.feature {
				padding: 2em 0.5em 0.1em 0.5em;
				width: 100%;
			}

		}

	.feature {
		border-color: #e3e3e3;
	}
img {
  display: inline-block;
  margin: 25px;
}
</style>
<section id ="main">

This page guides you with various options available to install Tizen Studio on your development hardware. Tizen Studio runs on all major operating systems such as Windows®, Ubuntu®, and macOS®.  It is recommended to install the latest version of Tizen Studio. 
For a seamless development experience: 
- **Plan your installation:** check for the necessary hardware and software requirements. 
- **Install Tizen Studio:**  follow the installation instructions for each operating system.
- **Configure Tizen Studio:**  get the optimal experience after installation by configuring various Tizen Studio components.  

Based on your target operating system, choose the installation guide from the following: 

<!-- tiles-->
<section id="one" class="wrapper special">
		<div class="inner">
			<header class="major">
			</header>
                        <div class="features">
                        <div class="feature">
                        <img src="./media/win.png">
                        <div style="width:100%;text-align:center;">
						<a href="./install.md"> Windows&reg
						</a>
						</div>	
                        </div>
						<div class="feature">
							<img src="./media/linux1.png">
							<div style="width:100%;text-align:center;">
							<a href= "./install.md">Ubuntu&reg</a>
							</div>
						</div>
						<div class="feature">
							<img src="./media/apple1.png">
                            <div style="width:100%;text-align:center;">
							<a href= "./install.md">macOS&reg</a>
							</div>
						</div>
					</div>
				</div>
			</section>