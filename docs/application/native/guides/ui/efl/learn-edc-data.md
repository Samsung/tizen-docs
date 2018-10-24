# Data Block

The `data` block behaves in the same way as the `data` block inside the `parts` block, but the usage is different: this block is useful for data that covers the whole theme, such as license information, version, and authors.

**Figure: Data block**

![Data block](./media/diagram_data.png)

```
data {
   item: "key" "value";
   file: "otherkey" "filename.ext";
}
```

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
