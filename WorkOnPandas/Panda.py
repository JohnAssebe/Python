'''
@author:Yohannes Assebe
@github:John Assebe
'''
import re
import pandas as pd
# use read_excel method to read from Excel files
# to specify the way of read we can set a delimiter as a second argument for text files
df=pd.read_csv('african_crisess.csv')

#--------------------The head method read top lists of 5---------------------------------#

# print(df.head(5))
# print(df.head()) #the same as head(5)
# print(df.tail(4))
# print(df.tail()) #the same as tail(5)

#------------------------------read headers in panda-------------------------------------#

# cols=df.columns
# print(cols.values)

#-----------------read selected columns-----------------------------------#

# print(df[['country','year','independence']])

# print(df[['year','country','sovereign_external_debt_default']][0:10]) # read selected column [Fromrow:Torow]



#-----------------------------read data in index anywhere we wants-----------------------------#

# print(df.iloc[0]) #reads row 1 

# print(df.iloc[100:109]) # iloc stands for index location(fromrow:torow)

# print(df.iloc[2,2]) # read a specific location(row,column)

# print(df.loc[df['year']==2000]) # prints All rows Of year 2000

# print(df[['country','year','independence']].loc[df['year']==2000]) # Display all rows of year 2000 with the selected columns only



#---------------------describe method do all the math neccesary for a dataframe------------------#

# print(df.describe())



#---------------------the next code will produce a 'total' column from the sum of case and inflation_crises --------------#

# df['total']=df['case']+df['inflation_crises']

#-----------------------sort values----------------------------------#
# print(df.sort_values(['cc3','case'],ascending=[1,0])) # sort the values in ascending order of cc3 and descending order of case

#-------------------------------------- drop column-------------------------------------------#

# df=df.drop(columns=['case']) # drop a case column

# print(df.iloc[:,4:10]) # Display all rows of columns between 4 and 10(exclusive)

# df['total']=df.iloc[:,4:10].sum(axis=1) # sum method axis set to 1 for specifying horizontal sum set 0 for verical sum




#--------------------------Reorder the columns------------------#

# cols=list(df.columns)
# df=df[cols[0:2]+[cols[-1]]+cols[2:-1]]

#-------------------------Write a modified feature to other file-----------------------#

# df.to_csv('updated.csv') # write the modified feature in the updated csv file
# to remove the index set df.to_csv('updated.csv',index=False)
# to create a tab separated file use df.to_csv('updated.txt',index=False,sep='\t')  
# to write in excel file use df.to_excel('updated.xlsx',index=False)
# print("Done succesfully")



#-------------------------Filter Data---------------------------#

# use | for or logic
# new_df=df.loc[(df['country']=='Angola') & (df['case']==2)]
# print(new_df.head(5))
# use reset_index() to create the index from zero
# new_df.reset_index(drop=True,inplace=True)
# print(new_df)

# to get datas that don't have gol substring in their words use df.loc[~df['country'].str.contains('gol')] negation in panda uses ~
# print(df.loc[df['country'].str.contains('gol')])

# to do more complicated filter we should use regular expressions
# print(df.loc[df['country'].str.contains('gol|ivo',flags=re.I,regex=True)])

# this search for words that starts with eg
# print(df.loc[df['country'].str.contains('^eg[a-z]*',flags=re.I,regex=True)])



#---------------------Conditional changes-------------------------#

 
# df.loc[df['country']=='Algeria','banking_crisis']='crises' # set a banking_crisis column values for crises if the country is Algeria
# print(df.head(20))

# ----------change multiple columns if condition is True----------

# df.loc[df['country']=='Algeria',['banking_crisis','total']]=['crisis',0]
# print(df.head(20))





#------------------Aggregate Statics(groupby)--------------------#

# df=df.groupby(['total']).mean()
# print(df.head(20))
# df=df.groupby(['total']).sum().sort_values('case',ascending=False)
# print(df.head(20))
# df=df.groupby(['total']).count()
# print(df.head(20))





#-------------------Load a chunks of data at a time-----------------#

# This will fetch 5 rows at a time
# new_df=pd.DataFrame(columns=df.columns)
# for df in pd.read_csv('african_crisess.csv',chunksize=5):
#     print("Chunks")
#     print(df)
#     results=df.groupby(['country']).count()
#     new_df=pd.concat([new_df,results])
# print(new_df)







#To use this panda snippet documentation in practice uncomment step by step and see the changes 
