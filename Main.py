import hashlib
import sqlite3
import time
import pyperclip
import secrets
import string
import os
from cryptography.fernet import Fernet


# ---------------- DATABASE ---------------- #
conn = sqlite3.connect("vault.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    master_hash TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY,
    website TEXT,
    username TEXT,
    password BLOB
)
""")
conn.commit()





# ---------------- ENCRYPTION ---------------- #
KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(Fernet.generate_key())
    return open(KEY_FILE, "rb").read()

fernet = Fernet(load_key())






# ---------------- MASTER PASSWORD ---------------- #
def set_master_password():
    password = input("Set Master Password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO users (master_hash) VALUES (?)", (hashed,))
    conn.commit()
    print("Master password set successfully.\n")

def verify_master_password():
    password = input("Enter Master Password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("SELECT master_hash FROM users")
    stored_hash = cur.fetchone()[0]

    if hashed == stored_hash:
        print("Access Granted.\n")
        return True
    else:
        print("Access Denied! Wrong Password.")
        return False









# ---------------- PASSWORD GENERATOR ---------------- #
def generate_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(secrets.choice(chars) for _ in range(length))
    print("Generated Password:", password)

# ----PASSWORD_MANAGER--------- #
def add_password():
    site = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")
    encrypted = fernet.encrypt(password.encode())

    cur.execute(
        "INSERT INTO credentials (website, username, password) VALUES (?, ?, ?)",
        (site, username, encrypted)
    )
    conn.commit()
    print("Password saved securely.\n")

def view_password():
    site = input("Enter website: ")
    cur.execute("SELECT password FROM credentials WHERE website=?", (site,))
    row = cur.fetchone()

    if row:
        decrypted = fernet.decrypt(row[0]).decode()
        pyperclip.copy(decrypted)
        print("Password copied to clipboard for 10 seconds.")
        time.sleep(10)
        pyperclip.copy("")
        print("Clipboard cleared.\n")
    else:
        print("No record found.\n")

def delete_password():
    site = input("Enter website to delete: ")
    cur.execute("DELETE FROM credentials WHERE website=?", (site,))
    conn.commit()
    print("Password deleted.\n")
    
    
    
    
    
    
    

# ---- MENU ----- #
def menu():
    while True:
        print("1. Add Password")
        print("2. View Password")
        print("3. Generate Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            generate_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice.\n")
            
            
  
  
  
            

# ------- MAIN------#
def main():
    cur.execute("SELECT * FROM users")
    if not cur.fetchone():
        set_master_password()

    if verify_master_password():
        menu()

if __name__ == "__main__":
    main()
