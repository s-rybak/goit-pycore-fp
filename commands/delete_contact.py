from commands.base import CommandInterface
from repositories.contact_repository import ContactRepository
from input_output.base import InputInterface, OutputInterface, Message, Table


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

        hints = [
            f"{contact.name} | {contact.phone} | {contact.id}" for contact in contacts
        ]
        user_input = input.input(hints).text

        if not user_input:
            output.display_message(Message("No input received. Operation aborted."))
            return

        contact_id_to_delete = user_input.split(" | ")[-1]
        contact_to_delete = self._contact_repository.findById(contact_id_to_delete)

        output.warning(
            "Are you sure you want to delete this contact?\n\nType 'yes' to confirm, or anything else to cancel."
        )
        output.table(
            Table(
                headers=["ID", "Name", "Phone", "Email", "Address", "Birthday"],
                data=[
                    [
                        contact_to_delete.id,
                        contact_to_delete.name,
                        contact_to_delete.phone,
                        contact_to_delete.email,
                        contact_to_delete.address,
                        contact_to_delete.birthday,
                    ]
                ],
            )
        )

        confirmation = input.input(["yes", "no"]).command.lower()
        if confirmation != "yes":
            output.display_message("Operation cancelled.")
            return

        if self._contact_repository.delete(contact_id_to_delete):
            output.success(
                f"Contact {contact_to_delete.name} has been deleted successfully."
            )
        else:
            output.error(f"Failed to delete the contact.")
