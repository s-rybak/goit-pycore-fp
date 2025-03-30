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
            output.info(
                Message("Usage: find_note <field> <value>. Fields: title, note, tag")
            )
            return

        field, value = args[0], " ".join(args[1:])
        search_methods = {
            "title": self.note_repository.find_by_title,
            "note": self.note_repository.find_contains,
            "tag": self.note_repository.find_by_tag,
        }

        if field not in search_methods:
            output.error(Message("Invalid field. Use: title, note, tag"))
            return

        results = search_methods[field](value)
        if results:
            output.table(
                Table(
                    headers=["ID", "Title", "Note", "Tags"],
                    data=[
                        [c.id, c.title, c.note, ", ".join(c.tags[:3])] for c in results
                    ],
                )
            )
        else:
            output.display_message(Message("No notes found."))
