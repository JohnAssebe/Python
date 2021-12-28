'''
Created on 7:04 AM 9/29/2019
@author:John(Yohannes Assebe)
From AAIT(Addis Ababa University of technology)
This is what we call bisection method used to guess the number
How it works?
the computer generate number randomly.
we guess first in the half of the range given by the instance
if our guess is high we leave the second half and assign the half to our stop
elif our guess is low we leave the first half and assign the half to our start
finally we get the number in a maximum guess of logN/log2
This is how bisection works
if we run program in different time we get different values
'''
import random as R
from time import time
t1=time()
class GuessGame:
    def __init__(self,start,stop):
            self.start=start
            self.stop=stop
            self.number=int(R.randrange(self.start,self.stop))
            print(self.number)
            self.guess=(self.start+self.stop)//2
            self.counter=1
            print("guess No "+str(self.counter)+":",self.guess)
            while self.guess!=self.number:
                self.counter+=1
                if self.guess>self.number:
                    self.stop=self.guess
                elif self.guess<self.number:
                    self.start=self.guess
                self.guess=(self.stop+self.start)//2
                print("guess No "+str(self.counter)+":",self.guess)
            print("\t\t\tNumber=>",self.number)
            t2=time()
            print(t2-t1,"seconds it takes to get the number")
            
game=GuessGame(0,10000000000000000000000000000)
#game2=GuessGame(0,10)
