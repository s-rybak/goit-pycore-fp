from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def save(self, data: any) -> str:
        pass

    def getNextId(self) -> str:
        pass

    @abstractmethod
    def getAll(self) -> list[any]:
        pass

    @abstractmethod
    def find(self, filter: callable) -> list[any]:
        pass

    @abstractmethod
    def getById(self, id: str) -> any:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
