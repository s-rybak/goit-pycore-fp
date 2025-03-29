from commands.base import CommandInterface
from repositories.note_repository import NoteRepository
from input_output.base import InputInterface, OutputInterface, Message


class DeleteNoteCommand(CommandInterface):
    def __init__(self, note_repository: NoteRepository):
        self._note_repository = note_repository

    @property
    def name(self) -> str:
        return "Delete Note"

    @property
    def description(self) -> str:
        return "Delete note by title"

    @property
    def call_name(self) -> str:
        return "delete_note"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.info("Please enter the title of the user you want to delete:")

        notes = self._note_repository.getAll()

        hints = [f"{note.title} | {note.id} | {note.note}" for note in notes]

        user_input = input.input(hints)
        user_input = str(user_input) 

        if not user_input:
            output.display_message(Message("No matching note found."))
            return

        parts = user_input.split(" | ", maxsplit=2)

        if len(parts) < 2:
            output.error("Invalid input format. Please select a valid note.")
            return

        note_title_to_delete = parts[0]
        note_id_to_delete = parts[1]

        if self._note_repository.delete(note_id_to_delete):
            output.success(
                f"Note \"{note_title_to_delete}\" has been deleted successfully."
            )
        else:
            output.error(
                f"Failed to delete the note with ID {note_id_to_delete}."
            )
