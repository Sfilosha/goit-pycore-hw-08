from .Fields import Id, Text
from nanoid import generate as generateId

class Note:
    def __init__(self, value):
        self.value = Text(value)
        self.id = Id(generateId('1234567890abcdef', size=4))

    def __str__(self):
        return f"{self.id} | {self.value}"