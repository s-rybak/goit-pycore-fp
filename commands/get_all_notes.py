from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.note_repository import NoteRepository
from input_output.base import Table


class GetAllNotesCommand(CommandInterface):
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    @property
    def name(self):
        return "get all notes"

    @property
    def description(self):
        return "Get all notes"

    @property
    def call_name(self):
        return "get_all_notes"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        notes = self.repository.getAll()
        output.table(
            Table(
                headers=["Title", "Note"],
                data=[[note.title, note.note] for note in notes],
            )
        )
