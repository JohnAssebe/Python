'''
@Author:Yohannes Assebe(John Assebe)

'''
from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('seaborn')
df=pd.read_csv('../percent_bachelors_degrees_women_usa.csv')
cols=df.columns.values
data=[df[cols[i+1]].loc[df['Year']==2011].values for i in range(len(cols)-1)]
labels=[cols[i+1] for i in range(len(cols)-1)]
plt.pie(data,labels=labels,
	    autopct="%1.1f%%",
	    wedgeprops={'edgecolor':'white'})
plt.title("Women bachelor degree at 2011(USA)")
plt.show()
