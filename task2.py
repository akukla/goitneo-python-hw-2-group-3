from collections import UserDict
from typing import Optional

class GITException(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        if not Phone.is_valid(value):
            raise GITException("Incorrect phone format")
        super().__init__(value)

    @staticmethod
    def is_valid(phone: str) -> bool:
        return isinstance(phone, str) and phone.isdigit() and len(phone) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones:[Phone] = []

    def add_phone(self, phone: str) -> bool:
        if self.find_phone(phone) is not None:
            print("Phone already added")
            return False
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        except GITException:
            print("Incorrect phone format")
            return False
        return True

    def remove_phone(self, phone: str) -> bool:
        phone_obj = self.find_phone(phone)
        if phone_obj is None:
            print("Phone doesn't exist")
            return False
        self.phones.remove(phone_obj)

    def edit_phone(self, phone: str, new_phone: str) -> bool:
        if not Phone.is_valid(new_phone):
            print("Incorrect phone format")
            return False
        phone_obj = self.find_phone(phone)
        if phone_obj is None:
            print("Phone doesn't exist")
            return False
        phone_obj.value = new_phone
        return True

    def find_phone(self, phone: str) -> Optional[Phone]:
        ret_list = list(filter(lambda x: x.value == phone, self.phones))
        return ret_list[0] if len(ret_list) else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record) -> bool:
        self.data[record.name.value] = record
        return True

    def find(self, name: str) -> Optional[Record]:
        if name in self.data.keys():
            return self.data[name]
        return None

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
            return True
        return False

# # Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# print(john_record.add_phone("1234567890"))
# print(john_record.add_phone("5555555555"))

# # Додавання запису John до адресної книги
# print(book.add_record(john_record))

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# print(jane_record.add_phone("9876543210"))
# print(book.add_record(jane_record))

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# print(john.edit_phone("1234567890", "1112223333"))

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print("john.find_phone('5555555555')", found_phone)
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# print(book.delete("Jane"))
