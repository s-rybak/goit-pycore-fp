from commands.base import CommandInterface
from commands.greet_command import GreetCommand
from commands.test_get_all_contacts import TestAllContactsCommand
from commands.find_contact import FindContactCommand
from commands.edit_contact import EditContactCommand
from commands.delete_contact import DeleteContactCommand
from repositories.contact_repository import ContactRepository
from storage.pickle_storage import PickleStorage
from commands.add_contact import AddContactCommand
from commands.find_upcoming_birthdays import BirthdayInDaysCommand

class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register_command(self, command: CommandInterface):
        self.commands[command.call_name] = command

    def get_command(self, name: str) -> CommandInterface | None:
        return self.commands.get(name)

    def get_all_commands(self) -> list[CommandInterface]:
        return list(self.commands.values())

    def get_command_names(self) -> list[str]:
        return list(self.commands.keys())


contact_repository = ContactRepository(PickleStorage("var/data/contacts.pkl"))
registry = CommandRegistry()
registry.register_command(GreetCommand())

registry.register_command(TestAllContactsCommand(contact_repository))
registry.register_command(AddContactCommand(contact_repository))
registry.register_command(FindContactCommand(contact_repository))
registry.register_command(EditContactCommand(contact_repository))
registry.register_command(DeleteContactCommand(contact_repository))
registry.register_command(BirthdayInDaysCommand(contact_repository))
