from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def save(self, data: any) -> str:
        pass

    def get_next_id(self) -> str:
        pass

    @abstractmethod
    def get_all(self) -> list[any]:
        pass

    @abstractmethod
    def find(self, filter: callable) -> list[any]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> any:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
