from abc import ABC, abstractmethod
from storage.base import StorageInterface


class StorageRepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, storage: StorageInterface):
        pass
