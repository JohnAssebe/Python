# stack plot uses to examine activies of more than one participants over  time(Usually)
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
days=[1,2,3,4,5,6,7]
# dev1=[4,5,6,6,7,8,9]
# dev2=[2,1,3,1,4,3,5]
# dev3=[2,2,3,3,1,5,6]
labels=['Dev1','Dev2','Dev3']
colors=['#123eee','#444dad','#564325'] # We can use the default color as well 
dev1=[4,5,6,6,3,2,1]
dev2=[2,1,1,1,3,4,2]
dev3=[2,2,1,1,2,2,5]
plt.stackplot(days,dev1,dev2,dev3,labels=labels,colors=colors) # The first argument is for x-axis
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
