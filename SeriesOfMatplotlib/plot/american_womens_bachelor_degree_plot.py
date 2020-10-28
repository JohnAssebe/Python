'''
@Author:Yohannes Assebe(John Assebe github)
'''
import pandas as pd
import random as ra
from matplotlib import pyplot as plt
plt.style.use('ggplot')
df=pd.read_csv('../percent_bachelors_degrees_women_usa.csv')
year=df['Year']
fields=[]
cols=df.columns.values
colors=['black','#521222','#155888','yellow','red','green','purple','blue']
for i in range(len(cols)-1):
      fields.append(list(df[str(cols[i+1])]))
for i in range(len(cols)-1):
	if i>=9:
		plt.plot(year,fields[i],color=colors[16-i],label=cols[i+1],linewidth=2) # To avoid color repeat
	else:
		plt.plot(year,fields[i],label=cols[i+1],linewidth=2)	  
plt.title("Women bachelor degree percents in USA")
plt.xlabel("Year")
plt.ylabel("Bachelor degree percent")
plt.legend()
plt.tight_layout()
#plt.savefig('americanwomenliteracy.png')
plt.show()

