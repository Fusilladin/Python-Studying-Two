# import the code
import json
import requests
import csv


# send a get request to get obj
result = requests.get('https://raw.githubusercontent.com/kfrawee/SalesAnalysis/master/data/Sales_April_2019.csv')


# get a status code (returns int on success)
print(result.status_code)

# get data

print(obj = (result.json()))
#str = json.dumps(obj[0], indent=2)
#print(str)
