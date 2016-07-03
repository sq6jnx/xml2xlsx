# XML2XLSX -- XMLish API for OpenPyXL

Provided XML Element Tree will return `openpyxl.Workbook` object.

This XMLish API tries to mimic OpenPyXL API and is supposed to be thin
wrapper on it.

## Example

Given XML file like:

```xml
<workbook>
    <font bold="True">bold</font>
    <fill fill_type="solid" start_color="FFCCCCCC">gray</fill>
    <sheet title="one">
        <freeze row="3" column="5"/>
        <cell row="1" column="1">Hello World!</cell>
    </sheet>
    <sheet title="one">
        <freeze pos="K10"/>
        <c pos="A1">2</c>
        <c pos="A2">2</c>
        <c pos="A3" font="bold" fill="gray">=SUM(A1:A2)</c>
    </sheet>
</workbook>
```

... pass it through `xml2xlsx`:

```
xml2xlsx.py < input.xml > output.xlsx
```

... to get quite nice `xlsx` file.

Please note how to define and name formatting elements:

 ```xml
 <!-- (...) -->
<font bold="True">bold</font>
<fill fill_type="solid" start_color="FFCCCCCC">gray</fill>
<!-- (...) -->
<c pos="A3" font="bold" fill="gray">Hello, World</c>
<!-- (...) -->
```

`<font>` tag defines font style named `bold` and is the used in cell A3 using
`font` attribute. Similary, `gray` style is defined in `<fill>` tag.

## What can it do

Not much, actually. You can create worksheets, apply fonts and styles to it,
and freeze panes. That's all, actually, but is subject to change in the future.

In the future, however, I'd like XML2XLSX to cover most of what you can do
with OpenPyXL.

## Tricks

I'm not sure, if this is good idea, but:
 - to create cell you can use `<cell>` or `<c>` tag, for short.
 - for freezing panes: `<freeze_panes>`, `<freeze>`, `<freeze_pane>`
 - to define fills: `<pattern_fill>` or `<fill>`

Again, I'm not sure if these "shortcuts" are good idea.
