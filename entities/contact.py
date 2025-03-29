from dataclasses import dataclass
from datetime import datetime



@dataclass
class Contact:
    id: str
    name: str
    phone: str
    email: str | None = None
    address: str | None = None
    birthday: str | None = None

    def __init__(
        self,
        name: str,
        phone: str,
        email: str | None = None,
        address: str | None = None,
        birthday: str | None = None,
    ):
        self.id = ""
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
