# CREATING A PASSWORD MANAGER

######
#parts 1,2,3 work correctly. 
######

from cryptography.fernet import Fernet 

class PasswordManager:

	def __init__(self):
		self.key = None
		self.password_file = None
		self.password_dict = {}

	def create_key(self, path):
		self.key = Fernet.generate_key()
		# print(self.key)
		with open(path, 'wb') as f:
			f.write(self.key) # this creates the key

	def load_key(self, path):
		with open(path, 'rb') as f:
			self.key = f.read()

	def create_password_file(self, path, initial_values=None): # initial values are dictionary passwords if already have them
		self.password_file = path

		if initial_values is not None:
			for key, value in initial_values.items(): #.items methods iterates the tuples
				self.add_password(key, value)
				# main function is set the path of the attr
	def load_password_file(self, path):
		self.password_file = path


# load the password file for each line, seperate at the colon, read line by line, decrypt the value part, to decrypt the password, then load the kv pairs decrypted into the password dictionary   
		with open(path, 'r') as f:
			for line in f: # always going to encrypt the password, not the file
				#site:password
				site, encrypted = line.split(":") # seperate kv by char
				self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode() # need the key loaded or created for this to work

### Adding of the password - the encryption part
	def add_password(self, site, password):
		self.password_dict[site] = password_file # in the dictionary that the pw for the site is the pw
		if self.password_file is not None: # if we have not already loaded or created it, then open and write into it
			with open(self.password_file, 'a+') as f: # open in appending mode
				encrypted = Fernet(self.key).encrypt(password.encode()) # has to be the same we used for the decryption
				f.write(site + ":" + encrypted_decode() +"\n")

# gives us the password once we pass an identifier for a site
# password would have to be loaded 
	def get_password(self, site):
		return self.password_dict[site]

# examples 
def main():
	password = {
		"email": "1234567",
		"facebook": "myfbpassword",
		"youtube": "helloworld123",
		"something": "myfavoritepassword_123"
	}

pm = PasswordManager()

print("""What do you want to do?
(1) Create a new key
(2) Load an existing key
(3) Create new password file
(4) Load existing password file
(5) Add a new password
(6) Get a password
(q) Quit
""")

done = False

while not done:
	choice = input("enter your choice: ")
	if choice == "1":
		path = input("Enter path: ")
		pm.create_key(path)
	elif choice == "2":
		path = input("Enter path: ")
		pm.load_key(path)
	elif choice == "3":
		path = input("Enter path: ")
		pm.create_password_file(path, password)
	elif choice == "4":
		path = input("Enter path: ")	
		pm.load_password_file(path)
	elif choice == "5":
		site = input("Enter the site: ")
		password - input("Enter the password: ")
		pm.add_password(site, password)
	elif choice == "6":
		site = input("What site do you want: ")
		print(f"Password for {site} is {pm.get_password(site)}")
	elif choice == "q":
		done = True
		print("Bye")
	else:
		print("Invalid choice!")
if __name__ == "__main__":
	main()



##this creates the key file
# pm = PasswordManager()
# pm.create_key('mykey.key')


### Creates a key that can be used for encryption-decryption
# pm = PasswordManager()
# pm.create_key(None)
# b'1WrlMR0seSTorns33_UXAITk-I1doiyz4SoPSgcMI_M='























#