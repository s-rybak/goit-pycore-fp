from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from entities.contact import Contact


class EditContactCommand(CommandInterface):
    def __init__(self, contact_repository: ContactRepository):
        self._contact_repository = contact_repository

    @property
    def name(self) -> str:
        return "Edit Contact"

    @property
    def description(self) -> str:
        return "Edit contact by name"

    @property
    def call_name(self) -> str:
        return "edit_contact"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.info("Please enter the name of the user you want to delete:")

        contacts = self._contact_repository.getAll()

        hints = [f"{contact.name} {contact.phone} {contact.id}" for contact in contacts]

        user_input = input.input(hints)
        contact_id_to_edit = user_input.args[1]

        if not user_input:
            output.display_message(Message("No matching contact found."))
            return

        output.display_message(
            Message("Enter the field to edit (name, phone, email, address, birthday):")
        )
        field_input = input.input()
        field = field_input.command

        if field not in ("name", "phone", "email", "address", "birthday"):
            output.error(Message("Invalid field."))
            return

        output.display_message(Message(f"Enter new value for {field}:"))
        new_value = input.input().text

        updated_contact = self._contact_repository.findById(contact_id_to_edit)
        setattr(updated_contact, field, new_value)

        self._contact_repository.update(updated_contact)

        output.success(Message("Contact updated successfully."))
