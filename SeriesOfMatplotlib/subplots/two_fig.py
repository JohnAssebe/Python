from matplotlib import pyplot as plt
import random as ra

plt.style.use('ggplot') # set a style for both figure

fig,ax1=plt.subplots() # create a figure 1  
fig2,ax2=plt.subplots() # create a figure 2

# ------------------- Generate a Fake Data-------------------------#

x=[i for i in range(1,100)]
y1=[ra.randint(1,100) for i in range(1,100)]
y2=[ra.randint(1,100) for i in range(1,100)]

# --------------------plot both figures---------------------------#
ax1.plot(x,y1,label="Fig 1")
ax2.plot(x,y2,label="Fig 2")

# ----------------------set a title,xlabel,ylabel and legends of fig1---------------#

ax1.set_title("First Fig")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.legend()

# ----------------------set a title,xlabel,ylabel and legends of fig2---------------#

ax2.set_title("Second Fig")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.legend()


# --------------------save both figures---------------------------------#
fig.savefig('Figure1.png')
fig2.savefig('Figure2.png')

# display the figures
plt.show()



