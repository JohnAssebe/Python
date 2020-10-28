'''
@Author:Yohannes Assebe(John Assebe github account) 
'''
from matplotlib import pyplot as plt
# use plt.style.available to see the available styles
plt.style.use('ggplot')

# unique style(but for plots that is not serious)
# plt.xkcd()

age=[34,35,36,37,38,40,45,60]
income=[20000,24000,25000,30000,40000,60000,67000,70000]
py_income=[i+5000 for i in income ]
js_income=[22000,26000,35000,37000,46000,60000,67000,70000]
plt.title("Plot graphs(fake data)")
plt.xlabel("Age")
plt.ylabel("Annual income")		

# To make it readable and easy to remember we can use the following method
plt.plot(age,py_income,color='b',marker='*',label='Python Devs')
#----------------There are two ways of passing legends--------------------#
# plt.legend(['Developers','Python Developers'])
# or Use label for each plot and plt.legend without argument as follow this is less error prone 

# linewidth default is 1 to make its line bold set above 1
plt.plot(age,js_income,color='#adad4b',marker='o',linewidth=2,label='Javascript Devs')

# There is a string for marker(.),line style(--) and color (k stands for black and b for blue 
# If color is the only string format we want to pass we can use full name (green) or #008000
plt.plot(age,income,'.--k',label="All Developers")

plt.fill_between(age,py_income,js_income,
	interpolate=True,
	color='green',
	alpha=0.25,
	label="B/n Python and Js")

# plt.fill_between(age,py_income,js_income,
# 	where=(py_income>js_income),
# 	interpolate=True,
# 	color='green',
# 	alpha=0.25,
# 	label="Python salary above js")

# plt.fill_between(age,py_income,js_income,
# 	where=(py_income<=js_income),
# 	interpolate=True,
# 	color='red',
# 	alpha=0.25,
# 	label="Python salary below js")

plt.legend()
# plt.grid(True)
# plt.tight_layout()



# use plt.savefig('plot.png') pass a path for adjusting a place of save
# plt.savefig('plot.png') 
plt.show() 
print("Done:)")
