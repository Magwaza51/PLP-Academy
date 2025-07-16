from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os


# Generate a key and store it once
# Only run once to generate salt and ke

'''
def write_key():
    salt = os.urandom(16)
    with open("salt.salt", "wb") as f:
        f.write(salt)
write_key()'''


def load_key(master_pwd):
    with open("salt.salt", "rb") as f:
        salt = f.read()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
    return key


master_pwd = input("What is the master password? ")
key = load_key(master_pwd)
fer = Fernet(key)


def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_pwd = data.split("|")
                decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
                print(f"User: {user} | Password: {decrypted_pwd}")
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted = fer.encrypt(pwd.encode()).decode()

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted + "\n")

while True:
    mode = input("Would you like to add a new password or view existing one (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")