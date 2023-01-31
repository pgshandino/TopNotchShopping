import random
import json
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

    db = read_item()

    db.update(item)

    with open('database/data/Items_db.json', 'w') as f:
        f.write(json.dumps(db))

    return item

def read_item():
    with open('database/data/Items_db.json', 'r') as f:
        db = f.read()

        return json.loads(db)

def update_item():
    pass

def delete_item():
    pass

def search(q: str, by='id') ->list:
    db = read_item()
    
    if by == 'name':
        for i in db:
            # print(db[i]['name'].lower())
            if db[i]['name'].lower() == q.lower():
                print(db[i])
    else:
        return db.get(q, 'No such item')

# create_db()
# print(read_item())
# print([create_item() for i in range(2)])

# search('cups', by='name')