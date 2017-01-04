#! /usr/bin/env python
import sys
import os
sys.path.append('../Src')
from SM2 import SM2
import unittest

class TestSM2(unittest.TestCase):
    def setUp(self):
        self.mySM2=SM2()
        pass
    def tearDown(self):
        pass
    def testAAA1(self):
        pass

if __name__ == '__main__':
	unittest.main()

