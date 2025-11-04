# connects with the function from another file
from password_utinels import encrypt_key
from cryptography.fernet import Fernet
import os

# this function generates a random key stores it in a file
def generate_key():
    
    # it one time checks it has the scert key or not to prevent password confusion
    if not os.path.exists("secret_key.txt"):
        random_key = Fernet.generate_key()
        with open("secret_key.txt", "wb") as f:
            f.write(random_key)
        print("random key is generated and saved.")
    else:
        print("Key already exists. Skipping key generation.")
        
 # one time only run it after words don,t run the program
 # comment it after finish and check the program running
 
# generate_key()

# after generate a key or secret token remove your password from here and comment the function 
# removing the password dioes not cause any error 
encrypted_key = encrypt_key(" Your password enter it")
print("Encrypted password is done!")
# after the secret token is generated paste it to the password_utinels file inlast
print(encrypted_key)
