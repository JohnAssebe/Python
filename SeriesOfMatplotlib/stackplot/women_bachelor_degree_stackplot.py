'''
@Author:Yohannes Assebe(John Assebe) github
stack plot 
'''
from matplotlib import pyplot as plt 
import pandas as pd 
plt.style.use('fivethirtyeight')
df=pd.read_csv('../percent_bachelors_degrees_women_usa.csv')
cols=df.columns.values # list of columns name assigned to cols  
plt.stackplot(df[cols[0]],# Assign values for x-value
	df[cols[1]],df[cols[2]],df[cols[3]], 
	# list of column values  Forexample df[cols[1]]=df['Agriculture']
	labels=[cols[1],cols[2],cols[3]])
plt.xlabel("Year")
plt.ylabel('Total')
plt.title("Women bachelor degree percents in USA")
plt.legend(loc='upper left')
# plt.tight_layout()
plt.show()