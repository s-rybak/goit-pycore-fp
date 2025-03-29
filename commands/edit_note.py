from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.note_repository import NoteRepository
from entities.note import Note


class EditNoteCommand(CommandInterface):
    def __init__(self, note_repository: NoteRepository):
        self._note_repository = note_repository

    @property
    def name(self) -> str:
        return "Edit Note"

    @property
    def description(self) -> str:
        return "Edit note by title"

    @property
    def call_name(self) -> str:
        return "edit_note"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.info("Please enter the title of the note you want to edit:")

        notes = self._note_repository.getAll()

        hints = [f"{note.title} | {note.id} | {note.note}" for note in notes]

        user_input = input.input(hints).text

        if not user_input:
            output.display_message(Message("No matching note found."))
            return

        parts = user_input.split(" | ", maxsplit=2)

        if len(parts) < 2:
            output.error("Invalid input format. Please select a valid note.")
            return

        note_id_to_edit = parts[1]

        output.info(Message("Enter the field to edit (title, note):"))
        field = input.input(["title", "note"]).command

        if field not in ("title", "note"):
            output.error(Message("Invalid field."))
            return

        output.info(Message(f"Enter new value for {field}:"))
        new_value = input.input().text

        updated_note = self._note_repository.findById(note_id_to_edit)

        setattr(updated_note, field, new_value)

        self._note_repository.update(updated_note)

        output.success(Message("Note updated successfully."))
