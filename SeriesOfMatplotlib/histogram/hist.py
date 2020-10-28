from matplotlib import pyplot as plt 
import numpy as np
# use histogram to draw a graph for a distributed data 
plt.style.use('fivethirtyeight')
age=[20,12,24,67,80,10,34,38,42,23,45,56,55,57,78,90,102,68,71,87]
age_difference=[10,20,30,40,50,60,70,80,90,100]
median_age=np.median(age)
plt.hist(age,bins=age_difference,edgecolor='black') 
# we can pass an integer value for bin argument 
# pass a log argument True if the data is to much varing to see the effect
plt.axvline(median_age,color='#fc4531',linewidth=1,label="Median Age")	
# axvline stands for axis vertical line 
plt.title('Questionary About Health System')
plt.xlabel('Age')
plt.ylabel('Respondant numbers')
plt.tight_layout()
plt.legend()
plt.show()