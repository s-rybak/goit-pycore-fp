from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message, Table
from repositories.note_repository import NoteRepository


class FindNoteCommand(CommandInterface):
    @property
    def name(self) -> str:
        return "Find note"

    @property
    def description(self) -> str:
        return "Find notes by title and content"

    @property
    def call_name(self) -> str:
        return "find_note"

    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        if len(args) < 2:
            output.display_message(
                Message("Usage: find_note <field> <value>. Fields: title, note")
            )
            return

        field, value = args[0], " ".join(args[1:])
        search_methods = {
            "title": self.note_repository.findByTitle,
            "note": self.note_repository.findContains,
        }

        if field not in search_methods:
            output.display_message(Message("Invalid field. Use: title, note"))
            return

        results = search_methods[field](value)
        if results:
            output.table(
                Table(
                    headers=["ID", "Title", "Note"],
                    data=[[c.id, c.title, c.note] for c in results],
                )
            )
        else:
            output.display_message(Message("No notes found."))
