from matplotlib import pyplot as plt
import numpy as np
plt.title("Average Developers Annual Salary(Fake data)")
#print(plt.style.available)
plt.style.use('Solarize_Light2')
age=[34,35,36,37,38,40,45,60]
x_index=np.arange(len(age))
width=0.25
income=[20000,24000,25000,30000,40000,60000,67000,70000]
# plt.bar(x_index,income,label="All Developers")
# plt.xticks(ticks=x_index,labels=age)

py_income=[i+5000 for i in income]
js_income=[i+2000 for i in income]
plt.bar(x_index-width,income,width=width,label="All Dev") # use plt.barh for horizontal draws use if the data is much more
plt.bar(x_index,js_income,width=width,label="JS Dev")
plt.bar(x_index+width,py_income,width=width,label="Python Dev")
plt.xticks(ticks=x_index,labels=age)
plt.xlabel("Age")
plt.ylabel("Annual average Salary")
plt.legend()
plt.show()