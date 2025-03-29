from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from entities.contact import Contact
from validators.email_phone_validators import validate_email, validate_phone


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
        output.info("Please enter the name of the user you want to edit:")

        contacts = self._contact_repository.getAll()

        hints = [f"{contact.name} | {contact.phone} | {contact.id}" for contact in contacts]
        user_input = input.input(hints)
        
        if not user_input:
            output.display_message(Message("No matching contact found."))
            return

        contact_id_to_edit = user_input.text.split(" | ")[-1]
        
        output.display_message(
            Message("Enter the field to edit (name, phone, email, address, birthday):")
        )
        field_input = input.input()
        field = field_input.text

        if field not in ("name", "phone", "email", "address", "birthday"):
            output.error(Message("Invalid field."))
            return

        new_value = ""
        while True:
            output.display_message(Message(f"Enter new value for {field}:"))
            new_value = input.input().text

            if field == "email" and not validate_email(new_value):
                output.error(Message("Please enter a valid email. Example: user@example.com"))
                continue 

            if field == "phone" and not validate_phone(new_value):
                output.error(Message("Please enter a valid phone number. Example: +380971234567 or 380971234567"))
                continue 

            break

        updated_contact = self._contact_repository.findById(contact_id_to_edit)
        setattr(updated_contact, field, new_value)

        self._contact_repository.update(updated_contact)

        output.success("Contact updated successfully.")