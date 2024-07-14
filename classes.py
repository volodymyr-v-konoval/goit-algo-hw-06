from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    # write smth here!
    def __init__(self, value):
        self.value = value
        if not self.value:
            print('Enter a name, please!')

class Phone(Field):
    # write smth here
    def __init__(self, value):
        if len(value) == 10 and str(value).isdigit:
            self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # write smth here
    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old, new):
        self.remove_phone(old)
        self.add_phone(new)

class AddressBook(UserDict):

    def add_record(self, data):
        self.data[data.name.value] = data

    def find(self, name):
        if name in self.data.keys():
            return self[name]
        return None
    
    def delete(self, name):
        if name in self.data.keys:
            self.data.pop(name)

 
if __name__ == '__main__':

    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print(book)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)