from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from entities.contact import Contact
from validators.contact_validators import (
    validate_email,
    validate_phone,
    validate_name,
    validate_address,
    validate_birthday,
)


class AddContactCommand(CommandInterface):
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    @property
    def name(self):
        return "add_contact"

    @property
    def description(self):
        return "Add a new contact"

    @property
    def call_name(self):
        return "add_contact"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):

        name = ""
        while not validate_name(name):
            output.info(Message("Enter the name of the contact:"))
            name = input.input().text
            if not validate_name(name):
                output.error(Message("Please enter a valid name (2-10 letters)."))

            if self.repository.find_by_name(name):
                output.error(
                    Message(
                        f"A contact with the name '{name}' already exists. Please enter a different name."
                    )
                )
                name = ""

        phone = ""
        while not validate_phone(phone):
            output.info(Message("Enter the phone number of the contact:"))
            phone = input.input().text
            if not validate_phone(phone):
                output.error(
                    Message(
                        "Please enter a valid phone number. Example: +380971234567 or 380971234567"
                    )
                )

        email = ""
        while not validate_email(email):
            output.info(Message("Enter the email of the contact:"))
            email = input.input().text
            if not validate_email(email):
                output.error(
                    Message("Please enter a valid email. Example: user@example.com")
                )

        address = ""
        while not validate_address(address):
            output.info(Message("Enter the address of the contact:"))
            address = input.input().text
            if not validate_address(address):
                output.error(Message("Address must be at least 5 characters long."))

        birthday = ""
        while not validate_birthday(birthday):
            output.info(Message("Enter the birthday (YYYY-MM-DD):"))
            birthday = input.input().text
            if not validate_birthday(birthday):
                output.error(
                    Message(
                        "Invalid birthday format. Please enter a valid date in YYYY-MM-DD format."
                    )
                )

        contact = Contact(name, phone, email, address, birthday)
        self.repository.create(contact)

        output.success(Message(f"Contact {contact.name} added successfully!"))
