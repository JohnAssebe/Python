#!/usr/bin/env python3

from rearrange_name import rearrange_name
import unittest

class TestRearrange_name(unittest.TestCase):
    def testbasic(self):
        testcase="John, Assebe"
        expected="Assebe John"
        self.assertEqual(rearrange_name(testcase),expected)
unittest.main()
