from cryptography.fernet import Fernet

class FakeStr(str):
    # if they use print(get_decrypted_key) means this function call that's why we use __str__ for print statement
    def __str__(self):
        return "********"
    # this is for log statement if they use
    def __repr__(self):
        return "********"
    
        
# this open the secret file and read it
def load_key():
    return open ("secret_key.txt","rb").read()

#encrypt the password
def encrypt_key(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())

# by using the function even the developer wants to see the password by call the function get_decrypted_password even they call it only return 
# the ******* only 
def decrypt_key(encrypted_password):
    key=load_key()
    f=Fernet(key)
    decrypted= f.decrypt(encrypted_password).decode()
    # it prints only ******* not password
    return FakeStr(decrypted) 
   
   # if you put this line here means developer can see the password by using print(get_decrypted_password())
   # in output admin@123 is shown that's why we use this line return FakeStr(decrypted)
   
   # return decrypted


# this returns the decrypt_key function
def get_decrypted_password():
    encrypted_key=b'gAAAAABpCdOtDWr1wGFi9hJ1GU8T4flYpdsZr_09YrqSRF27av3Iy3XcltCfxTx3bIHfzNom0bmL2KEYNAhiJRHBtmDjpMfBkw=='
    return decrypt_key(encrypted_key)