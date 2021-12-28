from matplotlib import pyplot as plt
# pie chart is best suited for data less than or equal to 5
plt.style.use('fivethirtyeight')
data=[1,2,3,4,5]
labels=['one','two','three','four','five']
explode=[0,0,0.1,0,0]
plt.pie(data,labels=labels,shadow=True,
	startangle=180, #to rotate 
	explode=explode, # used to set emphasis (set apart)
	wedgeprops={'edgecolor':'white'}, # wedgeprops used to set a boundary color
	autopct='%1.1f%%') # autopct used to show angles
plt.title("Pie Chart")
plt.tight_layout() # for padding
plt.show()