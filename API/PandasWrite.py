import pandas as pd

#########
# Reading and writing to CSV using Pandas

# setting the file path as a variable
df = pd.read_csv(r'C:\Users\userTK427\Desktop\Studying\SQL\Project 6 Load Match and Export\Source\HumanResources.Employee.csv', index_col='Id')

# schema_df = pd.read_csv(r'', index_col=)
# setting the max number to make it readable on output
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
# print(df)

#using head() prints top 5
print(df.head())

#filtering down by a column and reading it
filt = (df['Marital Status'] == 'Married')
married_df = df.loc[filt]

print(married_df.head())

#taking the filtered information and printing it into a new file in the same dir
married_df.to_csv(r'C:\Users\userTK427\Desktop\Studying\SQL\Project 6 Load Match and Export\Source\modified.csv')

############