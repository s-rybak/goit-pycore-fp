from .base import StorageRepositoryInterface
from storage.pickle_storage import PickleStorage
from entities.contact import Contact


class ContactRepository(StorageRepositoryInterface):
    def __init__(self, storage: PickleStorage):
        self.storage = storage

    def create(self, data: Contact) -> str:
        id = self.storage.get_next_id()
        data.id = id
        self.storage.save(data, id)
        return id

    def update(self, data: Contact) -> str:
        self.storage.save(data, data.id)
        return data.id

    def delete(self, id: str) -> bool:
        return self.storage.delete(id)

    def find_starts_with(self, search: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.name.startswith(search))

    def find_by_name(self, name: str) -> list[Contact]:
        return self.storage.find(lambda contact: name.lower() in contact.name.lower())

    def find_by_phone(self, phone: str) -> list[Contact]:
        return self.storage.find(lambda contact: phone.lower() in contact.phone.lower())

    def find_by_email(self, email: str) -> list[Contact]:
        return self.storage.find(lambda contact: email.lower() in contact.email.lower())

    def find_by_address(self, address: str) -> list[Contact]:
        return self.storage.find(lambda contact: address.lower() in contact.address.lower())

    def find_by_birthday(self, birthday: str) -> list[Contact]:
        return self.storage.find(lambda contact: birthday.lower() in contact.birthday.lower())

    def get_all(self) -> list[Contact]:
        return self.storage.get_all()

    def find_by_id(self, id: str) -> Contact | None:
        return self.storage.get_by_id(id)
