from dataclasses import dataclass
from datetime import date

@dataclass
class Contact:
    id: str
    name: str
    phone: str
    email: str
    address: str
    birthday: str

    #Add a constructor becouse we need to ingonre creation of id
    def __init__(self, name: str, phone: str, email: str, address: str, birthday: str):
        self.id = ""
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
