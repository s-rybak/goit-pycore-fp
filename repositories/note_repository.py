from .base import StorageRepositoryInterface
from storage.pickle_storage import PickleStorage
from entities.note import Note


class NoteRepository(StorageRepositoryInterface):
    def __init__(self, storage: PickleStorage):
        self.storage = storage

    def __sort_notes(self, notes: list[Note], order_by: str, order: str) -> list[Note]:
        if order not in ["asc", "desc"]:
            raise ValueError("Invalid order value. Use: asc, desc")
        return sorted(
            notes,
            key=lambda note: getattr(note, order_by),
            reverse=order == "desc",
        )

    def create(self, data: Note) -> str:
        id = self.storage.get_next_id()
        data.id = id
        self.storage.save(data, id)
        return id

    def update(self, data: Note) -> str:
        self.storage.save(data, data.id)
        return data.id

    def delete(self, id: str) -> bool:
        return self.storage.delete(id)

    def find_contains(
        self, search: str, order_by: str = "title", order: str = "asc"
    ) -> list[Note]:
        return self.__sort_notes(
            self.storage.find(
                lambda note: note.note and search.lower() in note.note.lower()
            ),
            order_by,
            order,
        )

    def find_by_title(
        self, title: str, order_by: str = "title", order: str = "asc"
    ) -> list[Note]:
        return self.__sort_notes(
            self.storage.find(lambda note: note.title == title), order_by, order
        )

    def find_by_tag(
        self, tag: str, order_by: str = "title", order: str = "asc"
    ) -> list[Note]:
        return self.__sort_notes(
            self.storage.find(lambda note: tag in note.tags), order_by, order
        )

    def get_all_tags_sorted(self) -> set[str]:
        return set([tag for note in self.get_all() for tag in note.tags])

    def get_all(
        self,
        order_by: str = "title",
        order: str = "asc",
    ) -> list[Note]:
        return self.__sort_notes(self.storage.get_all(), order_by, order)

    def find_by_id(self, id: str) -> Note:
        return self.storage.get_by_id(id)
