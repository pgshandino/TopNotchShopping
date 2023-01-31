import random
from hashids import Hashids

hid = Hashids(salt='remember this is a random string', min_length=9)

def create_db():
    with open('database/data/Items_db.json', 'w') as f:
        f.write('{}')


def create_item():
    name = input('Item name: ')
    price = input('Item price: ')
    desc = input('Item description: ')

    item = {
        hid.encode(random.randint(1, 10000)): {
            'name': name,
            'price': price,
            'desc': desc,
        }
    }

    return item

def read_item():
    pass

def update_item():
    pass

def delete_item():
    pass

create_db()
# print([create_item() for i in range(5)])