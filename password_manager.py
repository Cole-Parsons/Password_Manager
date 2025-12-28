import json
import os

def display_menu():
    print('PASSWORD MANAGER')
    print('-Select an Option-')
    print()
    print('1 = Add new website password')
    print('2 = View all sites')
    print('3 = Get password')
    print('4 = Update existing password')
    print('5 = Delete a website password')
    print('6 = Save and exit')

def add_account(account):
    while True:
        user_name = input('Enter username: ')
        if user_name in account:
            print('Usermname already exsts. Try again. ')
            continue

        master_password = input('Enter account password: ')
        account[user_name] = {
        'master_password': master_password,
        'sites': {}
        }
        break

def view_accounts(account, username):
    for key in account[username]['sites']:
        print(key)    

def get_password(account, username):
    print('What password would you like?')
    for site in account[username]['sites']:
        print(site)
    while True:
        site_choice = input('Enter Choice: ')
        if site_choice not in account[username]['sites']:
            print('Invalid choice. Try again.')
            continue
        print(account[username]['sites'][site_choice])
        return
        
def remove_site(account, username):
    for site in account[username]['sites']:
        print(site)
    site_name = input('What site would you like to remove: ')
    del account[username]['sites'][site_name]
    print('Site Removed')

def update_password(account, username):
    while True:
        print('Would you like to update master password or for a website password?')
        choice = int(input('Enter choice, 1 = Master ; 2 = Website: '))
        if choice == 1:
            choice2 = int(input('Are you sure you want to change master password? 1 = yes ; 2 = no: '))
            while True:
                if choice2 == 1:
                    new_master = input('New Master: ')
                    account[username]['master_password'] = new_master
                    print('Changed Master Password')
                    return
                elif choice2 == 2:
                    return
                else:
                    print('Invalid Input')
                    continue
        elif choice == 2:
            while True:
                print('What website would you like to change?')
                for site in account[username]['sites']:
                    print(site)
                site_choice = input('Enter site: ')
                if site_choice not in account[username]['sites']:
                    print('Not a valid site. Try again')
                    continue
                new_password = input('Enter new password for: ')
                account[username]['sites'][site_choice] = new_password
                print('Changed website password')
                return
        else:
            print('Invalid Input')
            continue

def add_password(account, username):
    new_site = input('Enter website name: ')
    new_password = input('Enter password for website: ')

    accounts[username]['sites'][new_site] = new_password

#start  main
#load from json file

if os.path.exists('accounts.json'):
    with open('accounts.json', 'r') as file:
        accounts = json.load(file)
else:
    accounts = {}  

#log in 
logged_in = False
while logged_in == False:
    username = input("Enter username (if new enter 0): ")

    if username == '0':
        add_account(accounts)
        continue

    if username not in accounts:
        print('User not found. Try again. ')
        continue

    password_check = False
    
    while password_check == False:
        temp_password = input('Enter Password: ')

        if temp_password == accounts[username]['master_password']:
            logged_in = True
            password_check = True
        else: 
            print('Password incorrect. Try again.')


#once logged in
while True:
    display_menu()
    user_num = int(input('Enter choice: '))
    if user_num == 1:
        add_password(accounts, username)
        #add website password
        print()
    elif user_num == 2:
        view_accounts(accounts, username)
        print()
    elif user_num == 3:
        get_password(accounts, username)
        print()
    elif user_num == 4:
        update_password(accounts, username)
        print()
    elif user_num == 5:
        remove_site(accounts, username)
        print()
    elif user_num == 6:
        with open('accounts.json', 'w') as file:
            json.dump(accounts, file, indent=4)
        print('Saved and exited')
        exit()
    else:
        print('Invalid input. Try again')
        print()