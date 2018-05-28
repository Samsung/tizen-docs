# PWM

[PWM](https://en.wikipedia.org/wiki/Pulse-width_modulation) (Pulse-Width Modulation) is a programmable interface that allows you to, for example, control motor speed or change light brightness.

Peripherals that support PWM are controlled by the current strength. To modulate the current, the voltage needs to be modulated. The voltage is proportional to the intensity of the current.

To modulate the voltage, you must set the duty cycle and polarity:

-   The period is a constant interval at which the pulse repeats.
-   The duty cycle is the constant time within 1 period in which a signal is active.
-   A "polarity high" signal starts high for the duration of the duty cycle and goes low for the remainder of the period. Conversely, a "polarity low" signal starts low for the duration of the duty cycle and goes high for the remainder of the period.
-   The pulse repeats if repetition has been enabled.

**Figure: Duty cycle**

![Duty cycle](media/peri_api_duty_cycle.png)

For example, if the period is 10,000,000 nanoseconds and the polarity high duty cycle is 7,000,000 nanoseconds, the average voltage is at 70%.

**Figure: Average voltage per duty cycle**

![Average voltage per duty cycle](media/peri_api_duty_cycle_voltage.png)

## Opening and Closing a Handle

To open and close a handle:

1.  To open a PWM handle, use the `peripheral_pwm_open()` function:

    ```
    int chip = 0;
    int pin = 2;
    peripheral_pwm_h pwm_h;
    peripheral_pwm_open(chip, pin, &pwm_h);
    ```

    The `chip` and `pin` parameters required for this function must be set according to the following table.

    **Table: ARTIK 530**

      Pin name  |Chip (parameter 1)  |Pin (parameter 2)
      ----------|--------------------|-------------------
      PWM0      |0                   |2

    > **Note**
    >
    > For more information on the pin names and locations, see [Supported Protocols](peripheral-io-api.md#protocol).

2.  To close a PWM handle that is no longer used, use the `peripheral_pwm_close()` function:

    ```
    peripheral_pwm_close(pwm_h);
    ```

## Setting the Period

To set the period, use the `peripheral_pwm_set_period()` function.

The following example sets the period to 20 milliseconds. The unit is nanoseconds.

```
Uint32_t period = 20000000;
peripheral_pwm_set_period(pwm_h, period);
```

## Setting the Duty Cycle

To set the duty cycle, use the `peripheral_pwm_set_duty_cycle()` function.

The following example sets the duty cycle to 2 milliseconds. The unit is nanoseconds.

```
uint32_t duty_cycle = 2000000;
peripheral_pwm_set_duty_cycle(pwm_h, duty_cycle);
```

## Setting the Polarity

To set the polarity, use the `peripheral_gpio_set_polarity()` function with 1 of the following polarity types:

-   `PERIPHERAL_PWM_POLARITY_ACTIVE_HIGH`: Polarity is high.
-   `PERIPHERAL_PWM_POLARITY_ACTIVE_LOW`: Polarity is low.

```
peripheral_pwm_set_polarity(pwm_h, PERIPHERAL_PWM_POLARITY_ACTIVE_HIGH);
```

## Enabling Repetition

To enable repetition, use the `peripheral_pwm_set_enabled()` function:

```
bool enable = true;
peripheral_pwm_set_enabled(pwm_h, enable);
```
