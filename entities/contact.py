from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Contact:
    id: str
    name: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None
    birthday: Optional[str] = None  

    def __init__(self, name: str, phone: str, email: Optional[str] = None, address: Optional[str] = None, birthday: Optional[str] = None):
        self.id = ""
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
