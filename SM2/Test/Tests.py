#! /usr/bin/env python
import sys
import os
sys.path.append('../Src')
from SM2 import SM2
from SM2 import Card
import unittest

class TestSM2(unittest.TestCase):
    def setUp(self):
        self.SM2=SM2()
        self.card=Card()
        pass
    def tearDown(self):
        pass
    def testEFValue(self):
        self.assertEqual(self.card.EF, 2.0)
        print self.SM2.updateEF(self.card, 5)


if __name__ == '__main__':
	unittest.main()

