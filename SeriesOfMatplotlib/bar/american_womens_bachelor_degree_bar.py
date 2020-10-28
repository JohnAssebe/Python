'''
@Author:Yohannes Assebe(John Assebe)
Draw Bar Graph From csv File using Panda
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#print(plt.style.available)
plt.style.use('fivethirtyeight')
plt.title('Bachelor degree percents of women in USA(2000-2011)')
df=pd.read_csv('../percent_bachelors_degrees_women_usa.csv')
agriculture=df['Agriculture'].loc[df['Year']>=2000]
Architecture=df['Architecture'].loc[df['Year']>=2000]
art=df['Art and Performance'].loc[df['Year']>=2000]
Biology=df['Biology'].loc[df['Year']>=2000]
year=df['Year'].loc[df['Year']>=2000]
x_index=np.arange(len(year))
width=0.2
plt.bar(x_index-2*width,agriculture,width=width,label="Agriculture")
plt.bar(x_index-width,Architecture,width=width,label="Architecture")
plt.bar(x_index,art,width=width,label="Art and Performance")
plt.bar(x_index+width,Biology,width=width,label="Biology")
plt.xticks(ticks=x_index,labels=year)
plt.xlabel('Year')
plt.ylabel('Percent')
plt.legend(loc='lower left')
# plt.tight_layout()
plt.show()
