# import the code

import json
import requests

# send a get request to get obj
response = requests.get('https://formulae.brew.sh/api/analytics/install-on-request/30d.json')

## get a status code (returns int on success)
#print(response.status_code)

# get data
#print(response.json())
obj = (response.json())
#print(obj)

# format the text into strings
str = json.dumps(obj, indent=2)
print(str)










