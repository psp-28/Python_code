from cryptography.fernet import Fernet

#### Load the key
def load_key():
    return open("secret.key","rb").read()

#Get stored credentials::
def get_creds():
    key= load_key()
    f = Fernet(key)
    with open("credentials.enc","rb") as cred_file:
        encrypted = cred_file.read()
    decrypted = f.decrypt(encrypted).decode()
    user, passw = decrypted.split(":",1)
    return user, passw

# Usage
username, password = get_creds()
print(f"\nUsername ::: {username}")
print(f"\nPassword ::: {password}")
