# HTML5 Forms

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

The HTML5 forms provide a convenient way to create consistent screens in your application for accepting user input.

This feature is supported in mobile and wearable applications only.

In the past, the Web form allowed you to accept user input before transmitting it to a server. With HTML5, you can now improve the user experience without having to use JavaScript by [adding simple features](./w3c/ui/html5forms-w.md#basic), for example, email validity checks and date pickers, and [using more advanced functionality](./w3c/ui/html5forms-w.md#advanced), such as security checks and input value pattern definitions.

With HTML5 forms, you can use new [elements](./w3c/ui/html5forms-w.md#element), [input element types](./w3c/ui/html5forms-w.md#input), and [input element attributes](./w3c/ui/html5forms-w.md#attribute).

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

1. [Create a login form](./w3c/ui/html5forms-w.md#basic) that checks the email validity and requires the mandatory password input:

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

| Element                                  | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `datalist` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-datalist-element) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-datalist-element) applications) | Defines a set of option elements that represent predefined options for other controls. The element is used together with the `input` element to predefine its value.In Tizen, the value selected in the `datalist` element can be edited. | `<input type="text" list="search"/><datalist id="search">   <option value="Tomato">Tomato</option>   <option value="banana">banana</option>   <option value="Watermelon">Watermelon</option></datalist>` |
| `keygen` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-keygen-element) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-keygen-element) applications) | Defines a control for generating a public-private key pair and for submitting the public key from that key pair. The element creates an encrypted key with the value of the `name` attribute, saves it in the user's computer and Web server, and activates the next procedure when the 2 values match. | `<label>user:<input type="text" name="user_name"/></label><label>keygen:<keygen name="keygen"/></label>` |
| `meter` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-meter-element) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-meter-element) applications) | Represents a scalar measurement within a known range (the distribution of the assigned range), or a fractional value. | `<meter value="75" min="0" max="100" low="60" high="80" optimum="81">   75/100</meter>` |
| `output` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-output-element) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-output-element) applications) | Represents the result of a calculation. The element generally shows the calculated result of the value that the user has entered, and is used within the `form` element. | `<fieldset onsubmit="return false"          oninput="foobar.value = parseInt(foo.value) * parseInt(bar.value)">   <input type="number" id="foo" name="foo"/> *   <input type="number" id="bar" name="bar"/> =   <output for="foo bar" name="foobar"></output></fieldset>` |
| `progress` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-progress-element) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-progress-element) applications) | Represents the progress of a task.       | `<progress value="75" max="100">   75/100</progress>` |

## New Input Element Types

The following table lists the new input element types available for your forms in HTML5. Many of the new elements activate a specific keyboard suitable for the type of value the user is expected to enter (for example, an email or URL). For a complete source code, see [types.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/html5_forms).

**Table: New input element types**

| Type                                     | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `color` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#color-state-(type=color)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#color-state-(type=color)) applications) | Select an HSL color from the color picker. The value format is HEX (#0099ff). | `<input type="color"       value="#ff0000"/><input type="datetime"       value="2012-12-12T03:30Z"/><input type="email"       required /><input type="number"       step="3"/><input type="range"       min="1" max="10"/><input type="tel"/><input type="url"/>` |
| `date` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#date-state-(type=date)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#date-state-(type=date)) applications) | Enter a date with no time zone (yyyy-mm-dd). |                                          |
| `datetime`                               | Enter a date and time with the (UTC) time zone (yyyy-mm-ddTtt:mmZ). |                                          |
| `datetime-local`                         | Enter a date and time with no time zone (yyyy-mm-ddTtt:mm). |                                          |
| `email` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#e-mail-state-(type=email)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#e-mail-state-(type=email)) applications) | Enter an email address with the email keyboard.     If the `required` attribute is used, the system checks whether the input format is in line with the ABNF regular expression (`1*(atext / ".") "@" ldh-str 1*("." ldh-str)`). |                                          |
| `month`                                  | Enter a year and month with no time zone (yyyy-mm). |                                          |
| `number` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#number-state-(type=number)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#number-state-(type=number)) applications) | Enter numbers with the number keyboard.  |                                          |
| `range` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#range-state-(type=range)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#range-state-(type=range)) applications) | Select a value from the slider.          |                                          |
| `search` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#text-(type=text)-state-and-search-state-(type=search)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#text-(type=text)-state-and-search-state-(type=search)) applications) | No specific functionality is defined for this element in the HTML5 specifications. |                                          |
| `tel` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#telephone-state-(type=tel)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#telephone-state-(type=tel)) applications) | Enter a phone number with the number keyboard. |                                          |
| `time` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#time-state-(type=time)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#time-state-(type=time)) applications) | Enter a time with no time zone (tt:mm:ss). |                                          |
| `url` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#url-state-(type=url)) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#url-state-(type=url)) applications) | Enter a URL with the URL keyboard.       |                                          |
| `week`                                   | Enter a year and week with no time zone (yyyy-week). |                                          |

## New Input Element Attributes

The following table lists the new input element attributes available for your forms in HTML5. For a complete source code, see [attributes.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/html5_forms).

**Table: New input element attributes**

| Attribute                                | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `autocomplete` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#autofilling-form-controls:-the-autocomplete-attribute) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#autofilling-form-controls:-the-autocomplete-attribute) applications) | Prefilling feature, which helps the users by, for example, prefilling the user's address based on earlier user input.     The text used by the user before (such as an `input` element) is listed in a `datalist` form. The attribute can be used in all form elements, and is activated if the value is "on" and deactivated if the value is "off". | `<input type="range" min="1" max="10"/><input type="tel" pattern="[0-9]+" required /><input placeholder="You know what to do, huh?"/><input type="number" step="3"/>` |
| `min` and `max` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-min-and-max-attributes) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-min-and-max-attributes) applications) | Allowed range of values for the element. |                                          |
| `pattern` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-pattern-attribute) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-pattern-attribute) applications) | Regular expression against which the control's value is checked.     The attribute can be used to check the validity of the form data. During service, a guide requiring the input format from the user is necessary. |                                          |
| `placeholder` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-placeholder-attribute) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-placeholder-attribute) applications) | Short hint intended to aid the user with the data entry.     The attribute can be used in the majority of form elements for various purposes, such as hint text or advertisement. |                                          |
| `required` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-required-attribute) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-required-attribute) applications) | Boolean attribute which, when specified, defines that the element is mandatory. |                                          |
| `step` (in [mobile](http://www.w3.org/TR/2014/REC-html5-20141028/forms.html#the-step-attribute) and [wearable](https://www.w3.org/TR/2014/CR-html5-20140429/forms.html#the-step-attribute) applications) | Granularity expected of the value, limiting the allowed values. |                                          |