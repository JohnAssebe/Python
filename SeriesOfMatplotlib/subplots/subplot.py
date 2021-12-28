'''

@Author:Yohannes Assebe(John Assebe)

'''

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

# start count from 100

index=count(100)

# Generate a Fake Data

x3_value=[x for x in range(100)]
y3_value=[random.randint(1,25) for i in range(100)]


# Create one figure with three rows and one column

fig,(ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1)  
# it has a sharex argument to share x ticks. Set True to enable that feature 
# it has a sharey argument too


# create a function that generates a live data figure

def animator(i):
	x3_value.append(next(index))
	y3_value.append(random.randint(0,20))
	ax3.cla()
	ax3.plot(x3_value,y3_value,label="4th Fig",linewidth=1)
	ax3.legend()

# create a Fake Data

x1_value=[x for x in range(100)]
y1_value=[random.randint(1,25) for i in range(100)]
y2_value=[random.randint(1,25) for i in range(100)]
y3_value=[random.randint(1,25) for i in range(100)]

#plot

ax1.plot(x1_value,y1_value,label="1st Fig")
ax2.plot(x1_value,y2_value,label="2nd Fig")
ax2.plot(x1_value,y3_value,label="3rd Fig")
fig1=FuncAnimation(fig,animator,interval=1000)

#set title,ylabel and its legend for the first axis  plot

ax1.set_title("Subplot with fig(Fake Data)")
ax1.set_ylabel("y values")
ax1.legend()

#set ylabel and its legend for the second axis  plots

ax2.set_ylabel("y2 values")
ax2.legend()

#set xlabel and legend for livedata figure 

ax3.set_xlabel("x values")
ax3.legend()

# tight_layout for padding fix

plt.tight_layout()
plt.style.use('fivethirtyeight')
plt.show()