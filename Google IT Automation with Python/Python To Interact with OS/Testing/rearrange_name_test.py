#!/usr/bin/env python3

from rearrange_name import rearrange_name
import unittest

class TestRearrange_name(unittest.TestCase):
    def testbasic(self):
        testcase="John, Assebe"
        expected="Assebe John"
        self.assertEqual(rearrange_name(testcase),expected)
    def testempty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected)
    def test_double_name(self):
        testcase="John, Assebe s."
        expected="Assebe s. John"
        self.assertEqual(rearrange_name(testcase),expected)
    def test_single_name(self):
        testcase="John"
        expected="John"
        self.assertEqual(rearrange_name(testcase),expected)
unittest.main()

