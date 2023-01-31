'''This is a shopping cart for to notch users'''

from auth import login, sign_up
from database import update
from cart import crud

print('WELCOME TO TOPNOTCHSHOPPING')
print(' A Wonderful shopping experience')

query = input('Login/Signup: ')
if query == 'login':
    if login():
        q = input('Add an item or view items[add/view/search]: ')
        if q == 'add':
            crud.create_item()
        elif q == 'view':
            print(crud.read_item())
        elif q == 'search':
            search_term = input('Search: ')
            by_term = input('filter: ')
            if by_term == '':
                crud.search(q=search_term)
            elif by_term == 'name':
                crud.search(q=search_term, by=by_term)
            else:
                print('Invalid entry for filter. Should be name')
        else:
            print('Invalid Entry')
elif query == 'signup':
    sign_up()
elif query == 'update':
    update()
    print('Update successfull')
else:
    print('Invalid Input')