# Argon2 password creator

import sys
import argon2

class PasswordValidationError(Exception):
    '''Generic Password Error'''


class PasswordManager:

    def __init__(self):
        '''Bootstrap hashing strategy'''
        self.strategy = argon2.PasswordHasher()
    
    def hash_password(self, password):
        '''Return a hash value based on the "password" provided'''
        return self.strategy.hash(password)

    def verify_password(self, hashed, password):
        '''Check if the hash value is related to "password"'''
        try:
            self.strategy.verify(hashed, password)
        except argon2.exceptions.VerificationError:
            raise PasswordValidationError("VERIFICATION FAILED")

if __name__ == "__main__":
    mgr = PasswordManager()
    stored_hash = mgr.hash_password("correct password")

    user_pasword == sys.argv[0]
    try:
        mgr.verify_password(stored_hash, user_password)
    except PasswordValidationError as e:
        print(e)
    else:
        print("VERIFICATION SUCCEEDED")




























#