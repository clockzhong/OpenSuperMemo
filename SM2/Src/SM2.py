#! /usr/bin/env python

class Card(object):
    def __init__(self):
        self.EF=2.0 #init the EF(Easiness Factor) value to 2.0
        self.interval=1*24*3600#The first interval is 1 day(24*3600secs), and the second interval is 6 days, I(1)=1

        #I use needRelearn to indicate whether the user need re-study this entry after anwser() it
        # The following copied from sm2.html, 
        #"After each repetition session of a given day repeat again all items that scored below four in the quality assessment. Continue the repetitions until all of these items score at least four."
        self.needRelearn=False
    def updateEF(self, easiness):
        newEF=self.EF+(0.1-(5-easiness)*(0.08+(5-easiness)*0.02))
        if (newEF<1.3):
            newEF=1.3
        self.EF=newEF
        return self.EF
    def updateInterval(self, easiness):
        if self.interval==1*24*3600:
            self.interval =6*24*3600 #I(2)=6
        else:
            self.interval=int(self.interval*self.EF)
        return self.interval
    def answer(self, easiness):
        if (easiness<3):
            self.interval=1*24*3600 #when the user response as 0,1 or 2, we need restart the SR process
            self.EF=2.0                   # I don't think the EF need to be reset, but SM2 request it clearly
            self.needRelearn=True
            return

        #should we use the newer EF to calculate the next interval? if yes, we need switch the following lines, 
        #if not, just keep it. According to my understanding on the https://www.supermemo.com/english/ol/sm2.htm
        #It's very possible that we need use the old EF value to calculate the next interval, and the new EF value
        #need be used in the NEXT NEXT interval's calculation
        self.updateInterval(easiness)
        self.updateEF(easiness)

        #check whether we need relearn this card today
        if (easiness<4):
            self.needRelearn=True


