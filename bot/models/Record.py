from .Fields import Phone, Name, Birthday, Id
from nanoid import generate as generateId

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.id = Id(generateId('1234567890abcdef', size=4))

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        phone = self.find_phone(number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone number {number} not found.")
    
    def edit_phone(self, old_number: str, new_number: str):
        old_phone_number = self.find_phone(old_number)
        if not old_phone_number:
            raise ValueError(f"Phone number {old_number} not found.")
        new_phone_number = Phone(new_number)
        old_phone_number.value = new_phone_number.value
    
    def find_phone(self, number: str):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"{self.id} | {self.name} | phones: {'; '.join(p.value for p in self.phones)} | birthday: {self.birthday}"