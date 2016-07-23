# XML2XLSX -- XMLish API for OpenPyXL

[![Build Status](https://travis-ci.org/sq6jnx/xml2xlsx.svg?branch=master)](https://travis-ci.org/sq6jnx/xml2xlsx)

Provided XML Element Tree will return `openpyxl.Workbook` object.

This XMLish API tries to mimic OpenPyXL API and is supposed to be thin
wrapper on it.

## Example

Given XML file like:

```xml
<workbook>
    <font bold="True">bold</font>
    <pattern_fill fill_type="solid" start_color="FFCCCCCC">gray</pattern_fill>
    <sheet title="one">
        <freeze_panes row="3" column="5"/>
        <cell row="1" column="1">Hello World!</cell>
    </sheet>
    <sheet title="one">
        <freeze_panes pos="K10"/>
        <cell pos="A1">2</cell>
        <cell pos="A2">2</cell>
        <cell pos="A3" font="bold" fill="gray">=SUM(A1:A2)</cell>
    </sheet>
</workbook>
```

... pass it through `xml2xlsx`:

```bash
xml2xlsx.py < input.xml > output.xlsx
```

... to get quite nice `xlsx` file.

Please note how to define and name formatting elements:

 ```xml
 <!-- (...) -->
<font bold="True">bold</font>
<pattern_fill fill_type="solid" start_color="FFCCCCCC">gray</pattern_fill>
<!-- (...) -->
<cell="A3" font="bold" fill="gray">Hello, World</cell
<!-- (...) -->

```

`<font>` tag defines font style named `bold` and is the used in cell A3 using
`font` attribute. Similary, `gray` style is defined in `<fill>` tag.

## What can it do

Not much, actually. You can create worksheets, apply fonts and styles to it,
and freeze panes. That's all, actually, but is subject to change in the future.

In the future, however, I'd like XML2XLSX to cover most of what you can do
with OpenPyXL.