'''
 @Author : Yohannes Assebe(John Assebe)
'''
import matplotlib.pyplot as plt 
# we can plot for csv data too 
from itertools import count
from matplotlib.animation import FuncAnimation
import random
c=count()
x=[]
y=[]
y1=[]
# This function name may be anything but always takes 1 positional argument of any name 
def animator(i):
	x.append(next(c))
	y.append(random.randint(-3,2))
	y1.append(random.randint(-2,3))
	plt.cla() # cla stands for clear axis (to avoid color change every seconds)
	plt.plot(x,y,label="First")
	plt.plot(x,y1,label="Second")
	plt.xlabel("random x")
	plt.ylabel("random y")
	plt.title("Plot Live Data(Fake Data)")
	plt.legend()
	plt.tight_layout() # to adjust a padding relative to figure position

ani=FuncAnimation(plt.gcf(),animator,interval=1000) 
# gcf stands for get current figure 
# 1000 interval mean 1 sec

plt.show()
