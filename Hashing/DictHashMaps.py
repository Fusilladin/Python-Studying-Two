#DICTIONARIES, HASH TABLES, HASH MAPS


# basic Dictionaries
my_dict = {'Dave':'001', 'Ava':'002', 'Joe':'003'}
print(my_dict)
print(type(my_dict))

new_dict=dict()
print(new_dict)
print(type(new_dict))

new_dict=dict(Dave='001', Ava='002')
print(new_dict)

# Nested dictionaries

emp_details={'Employee':{'Dave':{'ID':'001','Salary':'2000','Designation':'Team Lead'},
    'Ava':{'ID':'002','Salary':'1000','Designation':'Associate'}}}
print(emp_details)

# Operations on Hash Tables
    # {Accessing Items, Updating Values, Deleting Entries}

    # Accessing Items
print()
print(my_dict['Dave'])
# will print 001
print(my_dict)

# will print all keys and values
print(my_dict.keys())
print(my_dict.values())

# will print 002
print(my_dict.get('Ava'))
print()
for x in my_dict:
    print(x)
for x in my_dict.values():
    print(x)
for x,y in my_dict.items():
    print(x,y)

    # Updating Values
print()
my_dict['Dave']='004'
my_dict['Chris']='003'
print(my_dict)

    # Deleting Values
print()
print(my_dict.pop('Ava'))
my_dict.popitem()

del my_dict['Dave']
print(my_dict)

# Dictionary to Data Frame
print()
import pandas as pd
df = pd.DataFrame(emp_details['Employee'])
print(df)

















#
