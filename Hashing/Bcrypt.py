### Hashing with Bcrypt

# pip install bcrypt

import bcrypt
import json

### 1. Create password
password = input("Type your password: ") # bcrypt password must be a byte string
bytespw = bytes(password, "ascii")
print(bytespw) # test

# hash pasword
hashed = bcrypt.hashpw(bytespw, bcrypt.gensalt()) # method "hashpw" takes (password,salt) #15 is slow, but good.
# /// hashtest = bcrypt.hashpw(passwordtest, bcrypt.gensalt())

# print hashed password to test
print(hashed) #

### 2. Connect to config file
myjsonfile = open('test.json', 'r')
jsondata = myjsonfile.read()
obj = json.loads(jsondata)
testpw = bytes((obj['testpw']), "ascii")

### 3. bcrypt check password function - takes args ('plain text pw', 'hashed pw')
if bcrypt.checkpw(testpw, hashed):
    print("It matches!")
else:
    print("Does not match!")

# ### Work factor -- how much time it takes to brute force into the DB
# # default bcrypt.gensalt() has work mfactor of 12

# # time the program to test work factor
# import time

# start = time.time()
# hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=18)) # blank, (rounds=14)
# end = time.time()

# f = end - start
# print(f)


# ### 4. example web app
# user1 = request.form.get("username") # or email
# pass1 = request.form.get("password").encode("utf-8") # need to encode it into bytes so that we can verify the bytes pw with the hashed pass in the DB
# # -- look user up in DB using username
# # return redirect
# if bcrypt.checkpw(password, hashed):
#     print("It matches!")
#     return redirect(url_for("user_profile"))
# else:
#     print("Does not match!")
#     flash("Invalid credentials", "warning") # warning clause
