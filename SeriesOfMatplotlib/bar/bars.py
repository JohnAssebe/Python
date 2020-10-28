'''
@Author:Yohannes Assebe(John Assebe) github account
'''
from matplotlib import pyplot as plt
import random as ra 
plt.style.use('fivethirtyeight')
plt.title("Multiple bars")
color=['red' for i in range(2,100)]
x_value=[i for i in range(2,100)]
y_value=[ra.randint(200,1000) for k in range(2,100)]
for i in range(len(y_value)):
	if y_value[i]>=500:
		color[i]='green'

plt.bar(x_value,y_value,color=color)
plt.xlabel("time")
plt.ylabel('sold items')
plt.tight_layout()
plt.show()