'''This is a shopping cart for to notch users'''

from auth import login, sign_up
from database import update


query = input('Login/Signup: ')
if query == 'login':
    login()
elif query == 'signup':
    sign_up()
elif query == 'update':
    update()
else:
    print('Invalid Input')