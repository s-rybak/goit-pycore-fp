import pickle
import uuid
import os
from .base import StorageInterface


class PickleStorage(StorageInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = {}
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        try:
            with open(self.file_path, "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            pass

    def get_next_id(self) -> str:
        return str(uuid.uuid4())

    def save(self, data: any, id: str = None) -> str:
        if id is None:
            id = self.get_next_id()
        self.data[id] = data
        with open(self.file_path, "wb") as f:
            pickle.dump(self.data, f)
        return id

    def get_all(self) -> list[any]:
        return list(self.data.values())

    def find(self, filter: callable) -> list[any]:
        return [item for item in self.data.values() if filter(item)]

    def get_by_id(self, id: str) -> any:
        return self.data.get(id)

    def delete(self, id: str) -> bool:
        if id in self.data:
            del self.data[id]
            with open(self.file_path, "wb") as f:
                pickle.dump(self.data, f)
            return True
        return False
