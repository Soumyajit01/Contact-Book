import json, os
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
book.add("John", 9876543210, 'imgood@gmail.com')
book.add("Johny", 9876543210, 'imgoodagain@gmail.com')
# book.view()
# print(book.data)
book.view()

book.edit('John', 9898989898, 'johnnyIsHere@cmail.com')
with open('data_.json', 'w') as f:
    json.dump(book.data, f)

# book.view()
# book.view()