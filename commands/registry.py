from commands.base import CommandInterface
from commands.greet_command import GreetCommand
from commands.test_add_contact import TestAddContactCommand
from commands.test_get_all_contacts import TestAllContactsCommand
from repositories.contact_repository import ContactRepository
from storage.pickle_storage import PickleStorage
from commands.add_contact import AddContactCommand
from typing import Optional  # Додайте імпорт

class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register_command(self, command: CommandInterface):
        self.commands[command.call_name] = command


    def get_command(self, name: str) -> Optional[CommandInterface]:  
        return self.commands.get(name)


    def get_all_commands(self) -> list[CommandInterface]:
        return list(self.commands.values())

    def get_command_names(self) -> list[str]:
        return list(self.commands.keys())
    
    
    

registry = CommandRegistry()
registry.register_command(GreetCommand())
registry.register_command(TestAddContactCommand(ContactRepository(PickleStorage("var/data/contacts.pkl"))))
registry.register_command(TestAllContactsCommand(ContactRepository(PickleStorage("var/data/contacts.pkl"))))
registry.register_command(AddContactCommand(ContactRepository(PickleStorage("var/data/contacts.pkl"))))
