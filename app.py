'''This is a shopping cart for to notch users'''

from auth import login, sign_up
from database import update
from cart import crud


query = input('Login/Signup: ')
if query == 'login':
    if login():
        q = input('Add an item or view items[add/view]: ')
        if q == 'add':
            crud.create_item()
        elif q == 'view':
            print(crud.read_item())
        else:
            print('Invalid Entry')
elif query == 'signup':
    sign_up()
elif query == 'update':
    update()
    print('Update successfull')
else:
    print('Invalid Input')