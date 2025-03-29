from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.note_repository import NoteRepository
from entities.note import Note

class AddNoteCommand(CommandInterface):
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    @property
    def name(self):
        return "Add note"
    
    @property
    def description(self):
        return "Add a new note"
    
    @property
    def call_name(self):
        return "add_note"
    
    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.display_message(Message("Enter the note title:"))
        title = input.input().text

        output.display_message(Message("Enter the note:"))
        note = input.input().text

        note = Note(title, note)
        self.repository.create(note)

        output.display_message(Message(f"Note {note.title} added successfully!"))
