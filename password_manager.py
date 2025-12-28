def display_menu():
    print('PASSWORD MANAGER')
    print('-Select an Option-')
    print()
    print('1 = Add new account')
    print('2 = View all saved accounts')
    print('3 = Get password')
    print('4 = Update existing password')
    print('5 = Delete an account')
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
    for key in account[username]:
        print(key)    

def get_password(account):
    print('getting password')

def remove_site(account, username):
    site_name = input('What site would you like to remove: ')
    del account[username]['sites'][site_name]
    print('Site Removed')

accounts = {
    'colep': {
        'master_password': '123qwe',
        'sites': {
            'google.com': '123',
            'github.com': 'qwe'
        }
    },

    'ellab': {
        'master_password': '123qwe',
        'sites': {
            'google.com': '123',
            'github.com': 'qwe'
        }
    }
}    

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
        add_account(accounts)
        print()
    elif user_num == 2:
        view_accounts(accounts)
        print()
    elif user_num == 3:
        print('get password')
    elif user_num == 4:
        print('update password')
    elif user_num == 5:
        print('Delete Site')
        remove_site(accounts, username)
    elif user_num == 6:
        print('Save and exit')
        exit()
    else:
        print('Invalid input. Try again')

