#! /usr/bin/env python
import sys
import os
sys.path.append('../Src')
from SM2 import Card
import unittest

class TestSM2(unittest.TestCase):
    def setUp(self):
        self.card=Card()
        pass
    def tearDown(self):
        pass
    def testInitValue(self):
        self.assertEqual(self.card.EF, 2.0)
        self.assertEqual(self.card.interval, 1*24*3600)
    def testAnswer(self):
        #when answer easiness as 0, the EF and interval should be same as the init values
        self.card.answer(0)
        self.assertEqual(self.card.EF, 2.0)
        self.assertEqual(self.card.interval, 1*24*3600)
        self.assertEqual(self.card.needRelearn, True)
        #when answer easiness as 1, the EF and interval should be same as the init values
        self.card.answer(1)
        self.assertEqual(self.card.EF, 2.0)

        self.assertEqual(self.card.interval, 1*24*3600)
        self.assertEqual(self.card.needRelearn, True)
        #when answer easiness as 2, the EF and interval should be same as the init values
        self.card.answer(2)
        self.assertEqual(self.card.EF, 2.0)
        self.assertEqual(self.card.interval, 1*24*3600)
        self.assertEqual(self.card.needRelearn, True)


        self.card.answer(3)
        #print self.card.EF
        #print self.card.interval
        self.assertEqual(self.card.EF, 1.86)
        self.assertEqual(self.card.interval, 6*24*3600)
        self.assertEqual(self.card.needRelearn, True)

        self.card.answer(4)
        #print self.card.EF
        #print self.card.interval
        self.assertEqual(self.card.EF, 1.86)
        self.assertEqual(self.card.interval, int(6*24*3600*1.86))
        self.assertEqual(self.card.needRelearn, False)

if __name__ == '__main__':
	unittest.main()

