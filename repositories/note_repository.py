from .base import StorageRepositoryInterface
from storage.pickle_storage import PickleStorage
from entities.note import Note


class NoteRepository(StorageRepositoryInterface):
    def __init__(self, storage: PickleStorage):
        self.storage = storage

    def create(self, data: Note) -> str:
        id = self.storage.getNextId()
        data.id = id
        self.storage.save(data, id)
        return id

    def update(self, data: Note) -> str:
        self.storage.save(data, data.id)
        return data.id

    def delete(self, id: str) -> bool:
        return self.storage.delete(id)

    def findContains(self, search: str) -> list[Note]:
        return self.storage.find(lambda note: note.note and search.lower() in note.note.lower())

    def findByTitle(self, title: str) -> list[Note]:
        return self.storage.find(lambda note: note.title == title)

    def getAll(self) -> list[Note]:
        return self.storage.getAll()