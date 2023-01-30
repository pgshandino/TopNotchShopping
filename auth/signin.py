from .verify import login_verification

def login():
    username = input('Username: ')
    password = input('Password: ')

    if login_verification(username=username, password=password):
        print('Login Successfull')

