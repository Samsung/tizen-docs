# Tizen Studio

<style>
/* Reset */

html, body, div, span, applet, object, iframe, {
		vertical-align: baseline;
	}


/* Box Model */

	*, *:before, *:after {
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}

/* Button */
		input[type="submit"].special,
		input[type="reset"].special,
		input[type="button"].special,
		button.special,
		.button.special {
			background-color: #008aee;
			color: #ffffff !important;
		}


/* Section/Article */

	section.special, article.special, header.special {
		text-align: center;
	}

	header {
		margin-bottom: em;
	}

		header p {
			position: relative;
			margin: 0 0 1.5em 0;
			text-transform: uppercase;
		}

		header h2, header h3 {
			display: inline-block;
			padding-bottom: 0.4em;
			border-bottom-style: double;
			border-bottom-width: 4px;
		}
		@media screen and (max-width: 1280px) {

			header.major {
				margin-bottom: 2em;
			}

		}

		@media screen and (max-width: 736px) {

			header.major {
				margin-bottom: 1.5em;
			}

		}

		@media screen and (max-width: 480px) {

			header.major {
				margin-bottom: 1em;
			}

		}

	header h2, header h3 {
		border-bottom-color: #e3e3e3;
	}

	header p {
		color: #bbb;
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
		justify-content: center;
		margin-bottom: 2em;
	}

	.feature {
		padding: 2em 2em 0.1em 2em;
		border-style: hidden;
		border-width: 1px;
		margin-left: -1px;
		margin-top: -1px;
		width: 33.33333%;
	}

		.feature .fa {
			font-size: 2.8em;
			margin-bottom: 0.7em;
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

		.feature .fa {
			color: #00cdcf;
		}
	.button.special{
      margin-top: 15px;
      background-color: #008aee;
      border: none;
      color: white;
      text-align: center;
      display: inline-block;
      font-size: 16px;
	  cursor: pointer;
	  display: inline-block;
	  height: 2.85em;
	  line-height: 2.95em;
	  padding: 0 1.5em;
	  text-align: center;
	  text-transform: uppercase;
	  white-space: nowrap;
	  margin:20px;
 }	
 .container {
    &__text {
        display: inline;
    }
}	
.fa {
    color: #00cdcf;
}
a:link {
  color: #008aee;
  background-color: transparent;
  text-decoration: none;
}
a:visited {
  color: rgb(7, 3, 245);
  background-color: transparent;
  text-decoration: none;
}
a:hover {
  color: #008aee;
  background-color: transparent;
  text-decoration: underline;
}
a:active {
  color: y#008aee;
  background-color: transparent;
}
h1, h2, h3, h4, h5, h6 {
    color: ;
	font-weight: ;
	font-size: 1rem;
	
    line-height: 5em;
    margin: 0 0 1em 0;
    text-transform: inherit;
}
img {
  display: inline-block;
  margin: 10px;
}
</style>
<section id ="main">

Tizen Studio is an official Integrated Development Environment (IDE) for developing Tizen apps. This environment is built over Eclipse, it presents a unified environment where you can write, edit, debug, build, and publish your app. Tizen Studio runs on Windows®, Ubuntu®, and macOS®.

Tizen Studio primarily consists of: 

- set of fast and feature-rich emulators for devices based on Tizen, for example: Smartphone, TV emulator, Smart watch and much more
- extensive tool chains to capture performance, usability, version compatibility
- code templates, samples to help you get started 
- components to support new platforms
- system applications and drivers 
- utilities for compiling applications to Tizen RT (Tizen RTOS kernel variant)
<!-- tiles-->
<section id="one" class="wrapper special">
		<div class="inner">
			<header class="major">
			</header>

<div id="buttonzone">
							<a href="https://developer.tizen.org/development/tizen-studio/download" class="button special">Download</a>
							<a href="./setup/install-sdk" class="button special">Get Started</a>
						</div>
						
</header>
<p>Visit the following pages to explore more about Tizen Studio:</p>
                        <div class="features">
                        <div class="feature">
                        <img src="./media/Tools.png">
                         <div style="width:100%;text-align:center;">
						 <a href="native-tools/index.md">
						 Native Tools</a>
                        </div>
						</div>
						<div class="feature">
							<img src="./media/RT.png">
							<div style="width:100%;text-align:center;">
							<a href= "web-tools/index.md">Web Tools</a>
							</div>
						</div>
						<div class="feature">
							<img src="./media/Csdk.png">
                            <div style="width:100%;text-align:center;">
							<a href= "configurable-sdk/configurable-sdk.md">Configurable-IoT SDK</a></div>
						</div>
						<div class="feature">
							<img src="./media/SDK.png">
                            <div style="width:100%;text-align:center;">
							<a href= "extension-sdk/overview.md">Extension SDK</a>
							</div>
						</div>
						<div class="feature">
							<i class="fa fa-envelope-o"></i>
							<img src="./media/webtools.png">
							<div style="width:100%;text-align:center;">
							<a href= "rt-ide/overview.md">Tizen RT IDE</a>
							</div>
						</div>
					</div>
				</div>
			</section>