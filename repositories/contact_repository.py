from .base import StorageRepositoryInterface
from storage.pickle_storage import PickleStorage
from entities.contact import Contact


class ContactRepository(StorageRepositoryInterface):
    def __init__(self, storage: PickleStorage):
        self.storage = storage

    def create(self, data: Contact) -> str:
        id = self.storage.getNextId()
        data.id = id
        self.storage.save(data, id)
        return id

    def update(self, data: Contact) -> str:
        self.storage.save(data, data.id)
        return data.id

    def delete(self, id: str) -> bool:
        return self.storage.delete(id)

    def findStartsWith(self, search: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.name.startswith(search))

    def findByName(self, name: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.name == name)

    def findByPhone(self, phone: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.phone == phone)

    def findByEmail(self, email: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.email == email)

    def findByAddress(self, address: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.address == address)

    def findByBirthday(self, birthday: str) -> list[Contact]:
        return self.storage.find(lambda contact: contact.birthday == birthday)

    def getAll(self) -> list[Contact]:
        return self.storage.getAll()

    def findById(self, id: str) -> Contact | None:
        return self.storage.getById(id)
