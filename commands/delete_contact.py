from commands.base import CommandInterface
from repositories.contact_repository import ContactRepository
from input_output.base import InputInterface, OutputInterface, Message


class DeleteContactCommand(CommandInterface):
    def __init__(self, contact_repository: ContactRepository):
        self._contact_repository = contact_repository

    @property
    def name(self) -> str:
        return "Delete Contact"

    @property
    def description(self) -> str:
        return "Delete contact by name"

    @property
    def call_name(self) -> str:
        return "delete_contact"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.info("Please enter the name of the user you want to delete:")

        contacts = self._contact_repository.getAll()

        hints = [f"{contact.name} {contact.id} {contact.phone}" for contact in contacts]

        user_input = input.input(hints)

        if not user_input:
            output.display_message(Message("No input received. Operation aborted."))
            return

        contact_id_to_delete = user_input.args[0]

        if self._contact_repository.delete(contact_id_to_delete):
            output.success(
                f"Contact with ID {contact_id_to_delete} has been deleted successfully."
            )
        else:
            output.error(
                f"Failed to delete the contact with ID {contact_id_to_delete}."
            )
