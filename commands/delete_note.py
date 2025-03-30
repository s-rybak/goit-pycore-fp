from commands.base import CommandInterface
from repositories.note_repository import NoteRepository
from input_output.base import InputInterface, OutputInterface, Message, Table


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
        output.info("Please enter the title of the note you want to delete:")

        notes = self._note_repository.get_all()

        hints = [
            f"{note.title} | {note.id} | {', '.join(note.tags[:3])}" for note in notes
        ]

        user_input = input.input(hints).text

        if not user_input:
            output.display_message(Message("No matching note found."))
            return

        parts = user_input.split("|", maxsplit=2)
        parts = [part.strip() for part in parts]

        if len(parts) < 2:
            output.error("Invalid input format. Please select a valid note.")
            return

        note_title_to_delete = parts[0]
        note_id_to_delete = parts[1]
        print(note_id_to_delete)

        note_to_delete = self._note_repository.find_by_id(note_id_to_delete)

        if not note_to_delete:
            output.error("Note not found.")
            return

        output.warning(
            "Are you sure you want to delete this note?\n\nType 'yes' to confirm, or anything else to cancel."
        )
        output.table(
            Table(
                headers=["ID", "Title", "Note", "Tags"],
                data=[
                    [
                        note_to_delete.id,
                        note_to_delete.title,
                        note_to_delete.note,
                        ", ".join(note_to_delete.tags),
                    ]
                ],
            )
        )

        user_confirmation = input.input(["yes", "no"]).text

        if user_confirmation != "yes":
            output.display_message(Message("Deletion cancelled."))
            return

        if self._note_repository.delete(note_id_to_delete):
            output.success(
                f'Note "{note_title_to_delete}" has been deleted successfully.'
            )
        else:
            output.error(f"Failed to delete the note with ID {note_id_to_delete}.")
