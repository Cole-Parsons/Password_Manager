# Password Manager
A simple command-line password manager in Python that securely stores user accounts and website passwords using encryption and hashed master passwords.

## Features
* Add new accounts with a master password (hased with bcrypt)
* Login with master password verification
* Add, view, update and delete website passwords
* Encrypts all account data using cryptography.fernet

## Installation
Make sure python3 is installed: `python3 --version`
Install required packages: `pip3 install cryptography bcrypt`

## How to Run
1. Open terminal and navigate to project directory
2. Run program: `python3 password_manager.py`

## Future improvements
* Add password generator for websites
* Implement password strength checker
* Add a GUI interface
