# book.view()
# book.add()
# book.view()
# book.delete()
# book.edit()

import json, os
with open('data_.json','w') as f:
    pass
class Contact_Book:
    data = {}
    
    def add(self, name, phone, email):
        self.data[name] = (phone, email)

    def view(self):
        os.startfile('data_.json')

    def delete(self, name):
        self.data.pop(name)
    
    def edit(self, name, newPhone, email):
        self.data[name]= [newPhone, email] 

book = Contact_Book()
book.view()

book.add("Name", 9876543210, "email@gmail.com")

# book.view()
print(book.data)
book.view()

with open('data_.json', 'w') as f:
    json.dump(book.data, f)
