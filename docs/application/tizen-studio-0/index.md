# Tizen Studio

<style>
/* Reset */

html, body, div, span, applet, object, iframe, {
		margin:;
		padding: 0;
		border: 0;
		font-size: 100%;
		font: inherit;
		vertical-align: baseline;
	}

	article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section {
		display: block;
	}

	body {
		line-height: 1;
	}

	ol, ul{
		list-style-type: circle;
		list-style-position:inside;
	}

	blockquote, q {
		quotes: none;
	}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

	table {
		border-collapse: collapse;
		border-spacing: 0;
	}

	body {
		-webkit-text-size-adjust: none;
	}

/* Box Model */

	*, *:before, *:after {
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}


/* Type */

	body {
		background-color: #fff;
		color: #444;
	}

	body, input, select, textarea {
		font-family: "Raleway", Arial, Helvetica, sans-serif;
		font-size: 14pt;
		font-weight: 300;
		letter-spacing: 0.09em;
		line-height: 1.65em;
	}
		@media screen and (max-width: 1680px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 1280px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 980px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 736px) {

			body, input, select, textarea {
				font-size: 11pt;
			}

		}


/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		border-radius: 0;
		border: 0;
		cursor: pointer;
		display: inline-block;
		height: 2.85em;
		line-height: 2.95em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		text-transform: uppercase;
		white-space: nowrap;
	}


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

		header h2 + p {
			font-size: 1.25em;
			margin-top: -0.5em;
			line-height: 1.5em;
		}

		header h3 + p {
			font-size: 1.1em;
			line-height: 1.5em;
		}

		header h4 + p,
		header h5 + p,
		header h6 + p {
			font-size: 0.9em;
			line-height: 1.5em;
		}

		header.major {
			margin-bottom: 4em;
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
		border-style: solid;
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
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
	  cursor: pointer;
	  border-radius: 0;
	  border: 0;
	  cursor: pointer;
	  display: inline-block;
	  height: 2.85em;
	  line-height: 2.95em;
	  padding: 0 1.5em;
	  text-align: center;
	  text-decoration: none;
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
</style>
<section id ="main">

Tizen Studio is an official integrated development environment (IDE) for developing Tizen apps. This environment is built over Eclipse, it presents a unified environment where you can write, edit, debug, build, and publish your app. Tizen Studio runs on Windows®, Ubuntu, and macOS.

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
							<a href="https://developer.tizen.org/development/tizen-studio/download" class="button special">Download</i></a>
							<a href="./setup/install-sdk" class="button special">Get Started</a>
						</div>
						
</header>
<p>Visit the following pages to explore more about Tizen Studio:</p>
                        <div class="features">
                        <div class="feature">
                        <img src="./media/Tools.png">
                         <h3><a href="native-tools/index.md">Native Tools</a></h3>	
                        </div>
						<div class="feature">
							<i class="fa fa-copy"></i>
							<img src="./media/RT.png">
							<h3><a href= "web-tools/index.md">Web Tools</a></h3>
						</div>
						<div class="feature">
							<i class="fa fa-paper-plane-o"></i>
							<img src="./media/Csdk.png">
                            <h3><a href= "configurable-sdk/configurable-sdk.md">Configurable - IoT SDK</a></h3>
						</div>
						<div class="feature">
							<i class="fa fa-save"></i>
							<img src="./media/Tools.png">
                            <h3><a href= "extension-sdk/overview.md">Extension SDK</a></h3>
						</div>
						<div class="feature">
							<i class="fa fa-envelope-o"></i>
							<img src="./media/webtools.png">
							<h3><a href= "rt-ide/overview.md">Tizen RT IDE</a></h3>
						</div>
					</div>
				</div>
			</section>