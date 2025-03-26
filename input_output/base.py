from abc import ABC, abstractmethod


class Message:
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class Table:
    def __init__(self, headers: list, data: list):
        self.headers = headers
        self.data = data

    def __str__(self):
        return f"{self.headers}\n{self.data}"


class UserInput:
    def __init__(self, text: str = "", command: str = "", args: list = []):
        self.text = text
        self.command = command
        self.args = args

    def __str__(self):
        return f"{self.text} {self.command}"


class OutputInterface(ABC):

    @abstractmethod
    def success(self, msg: Message):
        """Print success message"""
        pass

    @abstractmethod
    def error(self, msg: Message):
        """Print error message"""
        pass

    @abstractmethod
    def warning(self, msg: Message):
        """Print warning message"""
        pass

    @abstractmethod
    def info(self, msg: Message):
        """Print info message"""
        pass

    @abstractmethod
    def hint(self, msg: Message):
        """Print hint message"""
        pass

    @abstractmethod
    def display_message(self, msg: Message):
        """Display message"""
        pass

    @abstractmethod
    def table(self, table: Table):
        """Display table"""
        pass


class InputInterface(ABC):
    @abstractmethod
    def input(self, hints: list) -> UserInput:
        """Input from user"""
        pass
