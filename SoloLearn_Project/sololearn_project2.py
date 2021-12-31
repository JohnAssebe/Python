'''
@author Yohannes Assebe
sololearn python data science course project 2 question answer 
'''
import numpy as np
data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
mean_value=np.mean(data)
std_data=np.std(data)
total_n=data.size
counter=0
for i in range(total_n):
    if mean_value-std_data<=data[i]<=mean_value+std_data:
        counter+=1
print((counter/total_n)*100)
