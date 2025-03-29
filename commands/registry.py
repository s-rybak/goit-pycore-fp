from commands.base import CommandInterface
from commands.greet_command import GreetCommand
from commands.test_get_all_contacts import TestAllContactsCommand
from commands.find_contact import FindContactCommand
from commands.edit_contact import EditContactCommand
from commands.delete_contact import DeleteContactCommand
from repositories.contact_repository import ContactRepository
from storage.pickle_storage import PickleStorage
from commands.add_contact import AddContactCommand

from repositories.note_repository import NoteRepository
from commands.add_note import AddNoteCommand
from commands.get_all_notes import GetAllNotesCommand
from commands.edit_note import EditNoteCommand
from commands.delete_note import DeleteNoteCommand
from commands.find_note import FindNoteCommand

from commands.help_command import HelpCommand
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
note_repository = NoteRepository(PickleStorage("var/data/notes.pkl"))

registry = CommandRegistry()
help_command = HelpCommand(registry)
registry.register_command(help_command)
registry.register_command(GreetCommand())

registry.register_command(TestAllContactsCommand(contact_repository))
registry.register_command(AddContactCommand(contact_repository))
registry.register_command(FindContactCommand(contact_repository))
registry.register_command(EditContactCommand(contact_repository))
registry.register_command(DeleteContactCommand(contact_repository))

registry.register_command(AddNoteCommand(note_repository))
registry.register_command(GetAllNotesCommand(note_repository))
registry.register_command(EditNoteCommand(note_repository))
registry.register_command(FindNoteCommand(note_repository))
registry.register_command(DeleteNoteCommand(note_repository))

registry.register_command(BirthdayInDaysCommand(contact_repository))
