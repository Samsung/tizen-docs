
# Unit & Scale

## Units

There are 3 major units that developers can take.

Unit | Example| Description | Formula to px
--|--|--|--
px | `view.DesiredWidth = 15f;` | Pixels | value 
spx | `view.DesiredWidth = 15f.Spx();` | Scaled pixels | value * scalingFactor 
dp | `view.DesiredWidth = 15f.Dp();` | Density-independent pixels | value * Dpi / BaselineDpi

⚠️ To set float-type property, please do not forget to use proper float literal to prevent data loss.

For example, when a scaling factor is 1.2f,

 Bad | Good
--|--
`8.Spx()` | `8f.Spx()`
 9 pixels (X) | 9.2 pixels (O)

## Customizing unit

### Custom ScalingFactor

Define `UIConfig` inherited class to set baseline dpi.

```C#
public class CustomOneUIConfig : UIConfig
{
    public CustomOneUIConfig()
    {
        ScalingFactor = 2.5f;
    }
}
```

Then apply it to the application,

```C#
public class YourApplication: OneUIApplication
{
    protected override OneUIConfig CreateConfig() => new CustomOneUIConfig();
}

```
