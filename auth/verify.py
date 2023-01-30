from database.crud import read

def login_verification(username: str, password: str) ->bool:
    '''
    This is a function that verifies a user and returns True/False if the login information is correct
    '''
    db = read()

    if username in db:
        if db[username]['password'] == password:
            print('Login Successfull')
            return True
        else:
            print('Invalid username or password')
            return False
    else:
        print('Invalid username or password')
        return False
