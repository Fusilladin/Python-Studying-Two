# Encrypt Strings and Files

# 1. -pip install cryptography

### Generate encryption key

from cryptography.fernet import Fernet

#generate the key
key = Fernet.generate_key()
# print(key)

#create the key file
file = open('key.key','wb')
file.write(key)
#file.close()

# salt and hash
import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = 'password1234' #input in the form of a string
password = password_provided.encode() # convert to type bytes

salt = b'\x8b\x87?n\xc0TF\xcc\xc2\x1a\x9d?\xe6\x00\x8e\xa5'
kdf = PBKDF2HMAC(
	algorithm=hashes.SHA256(),
	length=32,
	salt=salt,
	iterations=100000,
	backend=default_backend()
	)
key = base64.urlsafe_b64encode(kdf.derive(password)) # can only use kdf once

print(key)


### Encrypt strings

from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.key', 'rb') # read bytes
key = file.read() # the key will be type bytes
file.close()

# Encode the message
message = "my hidden key lol"
encoded = message.encode()

# Encrypt the message
f = Fernet(key)
encrypted = f.encrypt(encoded)
# print(encrypted)

### Decrypt the message
# Get the key again (for demonstration)
file = open('key.key', 'rb')
key2 =file.read() # type bytes
file.close()

# Decrypt the encrypted message
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted)

# return to str type
original_message = decrypted.decode()
print(original_message)
print()

### Encypting a file

# Get the key from the file
file = open('key.key', 'rb') # read bytes
key = file.read() # the key will be type bytes
file.close()

# Open the file to encrypt
with open('encryp.txt','rb') as f:
	data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Write the encrypted file
with open('encryp.txt.encrypted', 'wb') as f:
	f.write(encrypted)
	

















#
