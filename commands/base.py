from abc import ABC, abstractmethod

from input_output.base import InputInterface, OutputInterface


class CommandInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Command name"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Command description"""
        pass

    @property
    @abstractmethod
    def call_name(self) -> str:
        """Command call name"""
        pass

    @abstractmethod
    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        """Execute command"""
        pass
