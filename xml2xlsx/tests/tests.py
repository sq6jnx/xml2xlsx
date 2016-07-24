import lxml
import openpyxl
import xml2xlsx

import unittest


class TestXml2Xlsx(unittest.TestCase):
    def docstring_tree(self):
        return lxml.etree.fromstring(
            self._testMethodDoc[self._testMethodDoc.index("<workbook>"):])

    def test_hello_world(self):
        """"Test if workbook is created and if first row contains
        "Hello World"

        <workbook>
        <sheet>
        <cell pos="A1">Hello</cell>
        <cell row="1" column="2">World!</cell>
        </sheet>
        </workbook>"""
        etree = self.docstring_tree()
        wb = xml2xlsx.process(etree)

        s = wb.active
        self.assertEqual("Hello", s['A1'].value)
        self.assertEqual("World!", s['B1'].value)
    
    def test_sheet_names(self):
        """"Create 2 sheets with defined names

        <workbook>
        <sheet title="foo"/>
        <sheet title="bar"/>
        </workbook>"""
        etree = self.docstring_tree()
        wb = xml2xlsx.process(etree)

        self.assertEqual(wb.sheetnames, ['foo', 'bar'])

    def test_freeze_panes(self):
        """"Only first instruction for freeze_panes is executed.

        <workbook>
        <sheet>
        <freeze_panes pos="K10"/>
        <freeze_panes pos="L11"/>
        </sheet>
        </workbook>"""
        etree = self.docstring_tree()
        wb = xml2xlsx.process(etree)

        s = wb.active
        self.assertEqual(s.freeze_panes, 'K10')
