import json
from datetime import datetime as dt
from auth import signup

user = {'jDoe': {'password': 'password', 'first_name': 'Jane', 'last_name': 'Doe', 'age': 20, 'address': {'street': 'abcxyz', 'city': 'Abujs', 'state': 'FCT', 'country': 'Nigeria'}, 'signup': {'year': 2023, 'month': 1, 'day': 27, 'hour': 10, 'minute': 41, 'second': 22}}}

def create_db():
    '''This function create our database'''

    

    with open('./database/data/user_db.json', 'w') as file:
        file.write('{}')

def create(user: dict):
    '''
    This function creates a new record
    '''

    db = read()
    if tuple(user.keys())[0] in db:
        print('A user exists with this username')
    else:
        db.update(user)

    with open('./database/data/user_db.json', 'w') as file:
        db = file.write(json.dumps(db))


def read():
    with open('./database/data/user_db.json', 'r') as file:
        db = file.read()

        return json.loads(db)

def update():
    new_user = signup.sign_up()
    update_info = {
        'update': {
                'year': dt.now().year,
                'month': dt.now().month,
                'day': dt.now().day,
                'hour': dt.now().hour,
                'minute': dt.now().minute,
                'second': dt.now().second
            }
    }

    db = read()
    print(db)
    print('-------------')
    print(new_user)

    if tuple(new_user.keys())[0] in db:
        new_user.update(update_info)
        db.update(new_user)
        print(db)
        with open('./database/data/user_db.json', 'w') as file:
            file.write(json.dumps(db))
    else:
        print('No such user exist')
        q = input('Would you like to create an account? [y/n]: ')
        if q.lower() == 'y':
            create(new_user)
            print('Created Successfully!!')
        else:
            print('OK')

def delete():
    pass

create(user=user)