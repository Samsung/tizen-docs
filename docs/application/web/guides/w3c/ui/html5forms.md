# HTML5 Forms

The HTML5 forms provide a convenient way to create consistent screens in your application for accepting user input.

In the past, the Web form allowed you to accept user input before transmitting it to a server. With HTML5, you can now improve the user experience without having to use JavaScript by [adding simple features](#creating-a-basic-login-form), for example, email validity checks and date pickers, and [using more advanced functionality](#creating-an-advanced-login-form), such as security checks and input value pattern definitions.

With HTML5 forms, you can use new [elements](#new-html5-elements), [input element types](#new-input-element-types), and [input element attributes](#new-input-element-attributes).

## Creating a Basic Login Form

To create simple user input forms, you must learn to use the HTML5 features in Web forms:

1. Create a simple form where the user can enter their login details (email address and password):

   ```
   <form action="" method="">
      <label>email: <input type="text"/></label>
      <label>password: <input type="password"/></label>

      <input type="submit" value="Login"/>
   </form>
   ```

2. To check the validity of the entered email address automatically, add the `required` attribute to the `input` element with the `email` type:

   ```
   <label>email: <input type="email" required /></label>
   ```

3. Define the password field as mandatory by using the `required` attribute in that `input` element too:

   ```
   <label>password: <input type="password" required /></label>
   ```

4. Because a device has limited space on the screen, remove the field labels and replace them with hint texts using the `placeholder` attribute:

   ```
   <input type="email" placeholder="e-mail address" required />
   <input type="password" placeholder="password" required />
   ```

The final form that checks the email validity and requires the mandatory password input is complete:

```
<form action="" method="">
   <fieldset>
      <legend>Login</legend>
      <input type="email" placeholder="e-mail address" required />
      <input type="password" placeholder="password" required />
   </fieldset>

   <input type="submit" value="Login"/>
</form>
```

### Source Code

For the complete source code related to this use case, see the following file:

- [basicLogin.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/html5_forms)

## Creating an Advanced Login Form

To create advanced user input forms, you must learn to use the HTML5 features in Web forms:

1. [Create a login form](#creating-a-basic-login-form) that checks the email validity and requires the mandatory password input:

   ```
   <form action="" method="">
      <fieldset>
         <legend>Login</legend>
         <input type="email" placeholder="e-mail address" required />
         <input type="password" placeholder="password" required />
      </fieldset>

      <input type="submit" value="Login"/>
   </form>
   ```

2. When the form page is loaded on the screen, put the focus automatically to the email field by using the `autofocus` attribute:

   ```
   <input type="email" placeholder="e-mail address" required autofocus />
   ```

3. To spare the user from filling in information that they have given previously, use the `autocomplete` attribute, which shows the previously successfully inserted entries in a `datalist`, from which the user can select and use them.

   You can apply the `autocomplete` attribute to  a specific field by adding it to the appropriate `input` element. If you add it to the `form` element, it applies to all child elements within the form.

   ```
   <form action="" method="" autocomplete="on">
   ```

4. In general, apply the `autocomplete` attribute to the `form` element, and then separately set it to `off` for those fields that must not use it.

   In the following example, the password field must not use autocomplete, to prevent unauthorized access by any user.

   ```
   <input type="password" placeholder="password" required autocomplete="off"/>
   ```

5. Protect the password with private and public key pair using the `keygen` element.

   The element is used to transform the data sent from the connected form to a pair of encrypted keys using the RSA (Rivest Shamir Adleman) method. When the input data is sent from the form, the private key is saved in the local computer, and the public key is delivered to the server. Only if the keys match, the login process proceeds forwards.

   ```
   <keygen name="keyvalue">
   ```

6. Use the `pattern` attribute to perform a validity check that ensures that the password field value matches the given regular expression. The `required` attribute is used to ensure that the field value must be entered and then the validity check can be performed.

   In the following example, the password only accepts numbers and letters of the alphabet. If an invalid value is entered, the login cannot proceed.

   ```
   <input type="password" placeholder="password" required
          pattern="[a-zA-Z]+[0-9]+[a-zA-Z0-9]*|[0-9]+[a-zA-Z]+[a-zA-Z0-9]*"
          autocomplete="off"/>
   ```

7. Define the required length of the password within the `pattern` attribute.

   In the following example, the password must be 6 to 12 characters long.

   ```
   <input type="password" placeholder="password" required
          pattern="(?=([a-zA-Z]+[0-9]+[a-zA-Z0-9]*|[0-9]+[a-zA-Z]+[a-zA-Z0-9]*)).{6,12}"
          autocomplete="off"/>
   ```

The final form with autofocus and autocomplete features, strengthened security, and password value requirements is complete:

```
<form action="" method="" autocomplete="on">
   <fieldset>
      <legend>Login</legend>
      <input type="email" placeholder="e-mail address" required autofocus />
      <input type="password" placeholder="password" required
             pattern="(?=([a-zA-Z]+[0-9]+[a-zA-Z0-9]*|[0-9]+[a-zA-Z]+[a-zA-Z0-9]*)).{6,12}"
             autocomplete="off"/>
   </fieldset>

   <keygen name="keyvalue">

   <input type="submit" value="Login"/>
</form>
```

## New HTML5 Elements

The following table lists the new elements available for your forms in HTML5. For a complete source code, see [elements.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/html5_forms).

**Table: New HTML5 elements**

<table>
<tbody>
	<tr>
		<th>Element</th>
		<th>Description</th>
		<th>Example</th>
	</tr>
	<tr>
		<td><code>datalist</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-datalist-element" target="_blank">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-datalist-element" target="_blank">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-datalist-element" target="_blank">TV</a> applications)</td>
		<td>Defines a set of option elements that represent predefined options for other controls. The element is used together with the <code>input</code> element to predefine its value.
			<p>In Tizen, the value selected in the <code>datalist</code> element can be edited.</p>
		</td>
		<td>
<pre class="prettyprint">
&lt;input type="text" list="search"/&gt;
&lt;datalist id="search"&gt;
   &lt;option value="Tomato"&gt;Tomato&lt;/option&gt;
   &lt;option value="banana"&gt;banana&lt;/option&gt;
   &lt;option value="Watermelon"&gt;Watermelon&lt;/option&gt;
&lt;/datalist&gt;
</pre>
		</td>
	</tr>
	<tr>
		<td><code>keygen</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-keygen-element" target="_blank">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-keygen-element" target="_blank">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-keygen-element" target="_blank">TV</a> applications)</td>
		<td>Defines a control for generating a public-private key pair and for submitting the public key from that key pair. The element creates an encrypted key with the value of the <code>name</code> attribute, saves it in the user's computer and Web server, and activates the next procedure when the 2 values match.</td>
		<td rowspan="1" colspan="1">
<pre class="prettyprint">
&lt;label&gt;user:&lt;input type="text" name="user_name"/&gt;&lt;/label&gt;
&lt;label&gt;keygen:&lt;keygen name="keygen"/&gt;&lt;/label&gt;
</pre>
		</td>
	</tr>
	<tr>
		<td><code>meter</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-meter-element" target="_blank">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-meter-element" target="_blank">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-meter-element" target="_blank">TV</a> applications)</td>
		<td>Represents a scalar measurement within a known range (the distribution of the assigned range), or a fractional value.</td>
		<td>
<pre class="prettyprint">
&lt;meter value="75" min="0" max="100" low="60" high="80" optimum="81"&gt;
   75/100
&lt;/meter&gt;
</pre>
		</td>
	</tr>
	<tr>
		<td><code>output</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-output-element" target="_blank">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-output-element" target="_blank">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-output-element" target="_blank">TV</a> applications)</td>
		<td>Represents the result of a calculation. The element generally shows the calculated result of the value that the user has entered, and is used within the <code>form</code> element.</td>
		<td rowspan="1" colspan="1">
<pre class="prettyprint">
&lt;fieldset onsubmit="return false"
          oninput="foobar.value = parseInt(foo.value) * parseInt(bar.value)"&gt;
   &lt;input type="number" id="foo" name="foo"/&gt; *
   &lt;input type="number" id="bar" name="bar"/&gt; =
   &lt;output for="foo bar" name="foobar"&gt;&lt;/output&gt;
&lt;/fieldset&gt;
</pre>
		</td>
	</tr>
	<tr>
		<td><code>progress</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-progress-element" target="_blank">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-progress-element" target="_blank">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-progress-element" target="_blank">TV</a> applications)</td>
		<td>Represents the progress of a task.</td>
		<td>
<pre class="prettyprint">
&lt;progress value="75" max="100"&gt;
   75/100
&lt;/progress&gt;
</pre>
		</td>
	</tr>
</tbody>
</table>


## New Input Element Types

The following table lists the new input element types available for your forms in HTML5. Many of the new elements activate a specific keyboard suitable for the type of value the user is expected to enter (for example, an email or URL). For a complete source code, see [types.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/html5_forms).

**Table: New input element types**

<table>
	<tr>
		<th>Type</th><th>Description</th><th>Example</th>
	</tr>
	<tr>
		<td><code>color</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#color-state-(type=color)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#color-state-(type=color)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#color-state-(type=color)">TV</a> applications)</td>
		<td> Select an HSL color from the color picker. The value format is HEX (#0099ff).</td>
		<td rowspan="13">
<pre class="prettyprint">
&lt;input type="color"
       value="#ff0000"/&gt;
&lt;input type="datetime"
       value="2012-12-12T03:30Z"/&gt;
&lt;input type="email"
       required /&gt;
&lt;input type="number"
       step="3"/&gt;
&lt;input type="range"
       min="1" max="10"/&gt;
&lt;input type="tel"/&gt;
&lt;input type="url"/&gt;
</pre>
		</td>
	</tr>
	<tr>
		<td><code>date</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#date-state-(type=date)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#date-state-(type=date)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#date-state-(type=date)">TV</a> applications)</td>
		<td>Enter a date with no time zone (yyyy-mm-dd).</td>
	</tr>
	<tr>
		<td><code>datetime</code></td>
		<td>Enter a date and time with the (UTC) time zone (yyyy-mm-ddTtt:mmZ).</td>
	</tr>
	<tr>
		<td><code>datetime-local</code></td>
		<td>Enter a date and time with no time zone (yyyy-mm-ddTtt:mm).</td>
	</tr>
	<tr>
		<td><code>email</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#e-mail-state-(type=email)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#e-mail-state-(type=email)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#e-mail-state-(type=email)">TV</a> applications) </td><td>Enter an email address with the email keyboard.<br> If the <code>required</code> attribute is used, the system checks whether the input format is in line with the ABNF regular expression (<code>1*(atext / ".") "@" ldh-str 1*("." ldh-str)</code>).</td>
	</tr>
	<tr>
		<td><code>month</code></td>
		<td> Enter a year and month with no time zone (yyyy-mm).</td>
	</tr>
	<tr>
		<td><code>number</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#number-state-(type=number)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#number-state-(type=number)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#number-state-(type=number)">TV</a> applications)</td><td>Enter numbers with the number keyboard. </td>
	</tr>
	<tr>
		<td><code>range</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#range-state-(type=range)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#range-state-(type=range)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#range-state-(type=range)">TV</a> applications)</td><td> Select a value from the slider.</td>
	</tr>
	<tr>
		<td><code>search</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#text-(type=text)-state-and-search-state-(type=search)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#text-(type=text)-state-and-search-state-(type=search)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#text-(type=text)-state-and-search-state-(type=search)">TV</a> applications) </td><td>No specific functionality is defined for this element in the HTML5 specifications.</td>
	</tr>
	<tr>
		<td><code>tel</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#telephone-state-(type=tel)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#telephone-state-(type=tel)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#telephone-state-(type=tel)">TV</a> applications)</td><td> Enter a phone number with the number keyboard.</td>
	</tr>
	<tr>
		<td><code>time</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#time-state-(type=time)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#time-state-(type=time)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#time-state-(type=time)">TV</a> applications) </td><td>Enter a time with no time zone (tt:mm:ss).</td>
	</tr>
	<tr>
		<td><code>url</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#url-state-(type=url)">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#url-state-(type=url)">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#url-state-(type=url)">TV</a> applications)</td><td>Enter a URL with the URL keyboard.</td>
	</tr>
	<tr>
		<td><code>week</code></td>
		<td> Enter a year and week with no time zone (yyyy-week).</td>
	</tr>
</table>

## New Input Element Attributes

The following table lists the new input element attributes available for your forms in HTML5. For a complete source code, see [attributes.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/html5_forms).

**Table: New input element attributes**

<table>
	<tr>
		<th>Attribute</th>
		<th>Description</th>
		<th>Example</th>
	</tr>
	<tr>
		<td><code>autocomplete</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#autofilling-form-controls:-the-autocomplete-attribute">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#autofilling-form-controls:-the-autocomplete-attribute">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#autofilling-form-controls:-the-autocomplete-attribute">TV</a> applications)</td>
		<td>Prefilling feature, which helps the users by, for example, prefilling the user's address based on earlier user input.<p>The text used by the user before (such as an <code>input</code> element) is listed in a <code>datalist</code> form. The attribute can be used in all form elements, and is activated if the value is "on" and deactivated if the value is "off".</p></td>
		<td rowspan="6">
<pre class="prettyprint">
&lt;input type="range" min="1" max="10"/&gt;
&lt;input type="tel" pattern="[0-9]+" required /&gt;
&lt;input placeholder="You know what to do, huh?"/&gt;
&lt;input type="number" step="3"/&gt;
</pre>
		</td>
	</tr>
	<tr>
		<td><code>min</code> and <code>max</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-min-and-max-attributes">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-min-and-max-attributes">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-min-and-max-attributes">TV</a> applications)</td><td>Allowed range of values for the element.</td>
	</tr>
	<tr>
		<td><code>pattern</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-pattern-attribute">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-pattern-attribute">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-pattern-attribute">TV</a> applications)</td>
		<td>Regular expression against which the control's value is checked.<p>The attribute can be used to check the validity of the form data. During service, a guide requiring the input format from the user is necessary.</p></td>
	</tr>
	<tr>
		<td><code>placeholder</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-placeholder-attribute">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-placeholder-attribute">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-placeholder-attribute">TV</a> applications)</td>
		<td>Short hint intended to aid the user with the data entry.<p>The attribute can be used in the majority of form elements for various purposes, such as hint text or advertisement.</p></td>
	</tr>
	<tr>
		<td><code>required</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-required-attribute">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-required-attribute">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-required-attribute">TV</a> applications)</td>
		<td>Boolean attribute which, when specified, defines that the element is mandatory.</td>
	</tr>
	<tr>
		<td><code>step</code> (in <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-step-attribute">mobile</a>, <a href="https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-step-attribute">wearable</a>, and <a href="http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-step-attribute">TV</a> applications)</td>
		<td>Granularity expected of the value, limiting the allowed values.</td>
	</tr>
</table>


## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
