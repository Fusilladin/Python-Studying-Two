import pandas as pd
import json


#########
# Reading and writing to CSV using Pandas

# setting the file path as a variable
df = pd.read_csv(r'C:\Users\userTK427\Desktop\Studying\SQL\Project 6 Load Match and Export\Source\modified.csv', index_col='Id')

# schema_df = pd.read_csv(r'', index_col=)
# setting the max number to make it readable on output
pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
# print(df)

#using head() prints top 5
#print(df.head())

#filtering down by a column and reading it
filt = (df['Marital Status'] == 'Married')
married_df = df.loc[filt]

#print(married_df.head())

married_df.to_json(r'C:\Users\userTK427\Desktop\Studying\SQL\Project 6 Load Match and Export\Source\modified.json', orient='records', lines=True)

test = pd.read_json(r'C:\Users\userTK427\Desktop\Studying\SQL\Project 6 Load Match and Export\Source\modified.json', orient='records', lines=True)

print(test.head)

from sqlalchemy import create_engine
import psycopg2 

engine = create_engine('postgresql://dbuser:dbpass@localhost:1/API1')

married_df.to_sql('sample_table', engine)




# SELECT CURRENT_USER usr
#       ,inet_server_addr() host -- use inet_client_addr() to get address of the remote connection
#       ,inet_server_port() port -- use inet_client_port() to get port of the remote connection
#       ,inet_server_port() username
#       ,inet_server_port() password


