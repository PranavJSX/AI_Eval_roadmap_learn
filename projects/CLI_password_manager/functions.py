from cryptography.fernet import Fernet
import json
import os


def add_credential(vault, cipher, service, username, password):
    if service in vault:
        print("Service already exists, please choose other option")
        return

    enc_pass = encrypt_password(cipher=cipher, plain_password=password)
    vault[service] = (username, enc_pass)
    save_vault(vault=vault)
    print("---CREDENTIALS ADDED TO VAULT---")
    return


def get_credential(vault, cipher, service):
    if service in vault:
        username, enc_pass = vault[service]
        dec_pass = decrypt_password(cipher=cipher, encrypt_password=enc_pass)
        print(
            f"###########   REQUIRED CREDENTIALS, {username} : {dec_pass}   ###########"
        )
        return
    print("SERVICE DOES NOT EXIST !")
    return


def update_password(vault, cipher, service, new_password):
    if service in vault:
        username = vault[service][0]
        enc_pass = encrypt_password(cipher=cipher, plain_password=new_password)
        vault[service] = (username, enc_pass)
        save_vault(vault=vault)
        print("---UPDATED !---")
        return
    print("---SERVICE DOES NOT EXIST---")
    return


def delete_credential(vault, service):
    if service in vault:
        vault.pop(service)
        save_vault(vault=vault)
        print("---CREDENTIAL REMOVED---")
        return
    print("---SERVICE DOES NOT EXIST---")
    return


def list_services(vault):
    if not vault:
        print("VAULT EMPTY, Please add some credentials !")
        return
    for i in vault:
        print(i)
    return


def load_or_generate_key():
    """Loads existing key or creates a new one if its missing"""

    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)


def encrypt_password(cipher, plain_password):
    return cipher.encrypt(plain_password.encode()).decode()


def decrypt_password(cipher, encrypt_password):
    return cipher.decrypt(encrypt_password.encode()).decode()


def load_vault():
    if not os.path.exists("vault.json"):
        return {}
    with open("vault.json", "r") as f:
        return json.load(f)


def save_vault(vault):
    with open("vault.json", "w") as f:
        json.dump(vault, f, indent=4)
