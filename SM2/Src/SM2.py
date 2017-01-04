#! /usr/bin/env python

class Card(object):
    def __init__(self):
        self.EF=2.0 #init the EF(Easiness Factor) value to 2.0
        self.interval=1*24*3600#The first interval is 1 day(24*3600secs), and the second interval is 6 days, I(1)=1
        
class SM2(object):
    def __init__(self):
        #print("SM2 inited")
        pass
    def updateEF(self, card, easiness):
        newEF=card.EF+(0.1-(5-easiness)*(0.08+(5-easiness)*0.02))
        if (newEF<1.3):
            newEF=1.3
        card.EF=newEF
        return newEF
    def updateInterval(self, card, easiness):
        if card.interval==1*24*3600:
            card.interval =6*24*3600 #I(2)=6
        else:
            card.interval=card.interval*card.EF
        return card.interval

