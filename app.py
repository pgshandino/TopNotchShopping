'''This is a shopping cart for to notch users'''

from auth import login, sign_up
from database import update
from cart import crud

print('WELCOME TO TOPNOTCHSHOPPING')
print(' A Wonderful shopping experience')

query = input('Login/Signup/update: ')
while True:
    if query == 'login':
        for i in range(3):
            if login():
                while True:
                    q = input('Add an item or view items[add/view/search/q]: ')
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
                    elif q == 'q':
                        print('Logging out...')
                        break
                    else:
                        print('Invalid Entry')
                        print('Only add, view, search and q allowed.')
                        q = input('Add an item or view items[add/view/search]: ')
            print(f'You have {2-i} tries left.')
        print('Account temporarily locked, try again later.')
        break
    elif query == 'signup':
        sign_up()
    elif query == 'update':
        update()
        print('Update successfull')
    else:
        print('Invalid Input')
        print('Only login, signup and update are allowed.')
        query = input('Login/Signup/update: ')

