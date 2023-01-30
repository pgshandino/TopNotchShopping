from datetime import datetime as dt


def sign_up():
    f_name = input('First Name: ')
    l_name = input('Last Name: ')
    age = int(input('Age: '))
    street = input('Street: ')
    city = input('City: ')
    state = input('State: ')
    country = input('Country: ')
    username = input('Username: ')
    password = input('Password: ')

    user = {
        username: {
            'password': password,
            'first_name': f_name,
            'last_name': l_name,
            'age': age,
            'address': {
                'street': street,
                'city': city,
                'state': state,
                'country': country
            },
            'signup': {
                'year': dt.now().year,
                'month': dt.now().month,
                'day': dt.now().day,
                'hour': dt.now().hour,
                'minute': dt.now().minute,
                'second': dt.now().second
            }

        }
    }

    return user

