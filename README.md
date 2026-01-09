# Secure_Password_Manager
A secure command-line based Password Manager built using Python that stores and manages user credentials safely using encryption and hashing techniques.

This project implements secure storage of passwords using Fernet encryption, protects access using a master password hashed with SHA-256, and stores data locally in a SQLite database.

Developed as part of the Python Development – Foundation Track Internship (Phase 2 Project).



📌 Project Overview

The goal of this project is to build a secure vault system where:

     ✅Passwords are never stored in plain text.

     ✅Only authorized users can access stored credentials.

     ✅Sensitive data is encrypted before saving to the database.

     ✅Users can generate strong random passwords.

     ✅Clipboard is automatically cleared after copying a password.



🚀 Features

    ✅ Master Password Authentication (SHA-256 Hashing)

    ✅ Encrypted Password Storage using Fernet

    ✅ SQLite Database Storage (vault.db)

    ✅Add New Credentials

    ✅ View Stored Credentials

    ✅Delete Credentials

    ✅Strong Password Generator

    ✅Clipboard Auto-Clear after 10 seconds

    ✅Menu-driven CLI Interface





🛠️ Technologies Used

    ✅Python 3

    ✅SQLite3 Database

    ✅Cryptography Library (Fernet Encryption)

    ✅hashlib (SHA-256 Hashing)

    ✅pyperclip (Clipboard Handling)




📂 Project Structure
├── Main.py
├── README.md
├── .gitignore





⚙️ Installation & Setup

1️⃣ Clone the Repository
         git clone <your-github-repository-link>

2️⃣ Navigate into Project Folder
         cd Secure-Password-Manager

3️⃣ Install Required Libraries
         pip install cryptography pyperclip

4️⃣ Run the Application
         python Main.py





▶️ How to Use

 ✅Run the application.

✅If no master password exists, you will be asked to create one.

✅Enter your master password to access the vault.

Choose from the menu:
    ✅Add Password
    
    ✅View Password (auto copies to clipboard)
    
    ✅Generate Password
    
    ✅Delete Password
    
    ✅Exit
    
    ✅Passwords are encrypted automatically before storing.





🔐 Security Implementation

    ✅Master Password Hashing:
        The master password is hashed using SHA-256 and stored securely in the database.

    ✅Password Encryption:
        All saved passwords are encrypted using Fernet symmetric encryption.

    ✅Encrypted Storage:
        Even if someone accesses the database file, the passwords remain unreadable.

    ✅Clipboard Protection:
        Copied passwords are automatically cleared after 10 seconds.




✅ Expected Outcomes

     ✅Secure encrypted password storage

     ✅Functional password management system

     ✅Understanding of encryption and Python security concepts

     ✅Clean, modular, and maintainable code






  
👉✅secret.key is generated locally

