'''
@Author:yohannes Assebe
prints a row that have a maximum ratio of death to cases day from a dataset
'''
import pandas as pd
df = pd.read_csv("/usercode/files/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df['ratio']=df['deaths']/df['cases']
max_=df['ratio'].max()
print(df[df['ratio']==max_])
