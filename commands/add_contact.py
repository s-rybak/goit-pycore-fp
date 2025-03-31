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
        output.info(Message("Enter the name of the contact (or type 'exit' to cancel):"))
        while True:
            name = input.input().text
            if name.lower() == "exit":
                output.info(Message("Contact creation cancelled."))
                return
            if not validate_name(name):
                output.error(Message("Please enter a valid name (2-10 letters)."))
                continue
            if self.repository.find_by_name(name):
                output.error(Message(f"A contact with the name '{name}' already exists. Please enter a different name."))
                continue
            break
        
        output.info(Message("Enter the phone number of the contact (or type 'exit' to cancel):"))
        while True:
            phone = input.input().text
            if phone.lower() == "exit":
                output.info(Message("Contact creation cancelled."))
                return
            if not validate_phone(phone):
                output.error(Message("Please enter a valid phone number. Example: +380971234567 or 380971234567"))
                continue
            break
        
        output.info(Message("Enter the email of the contact (or type 'exit' to cancel):"))
        while True:
            email = input.input().text
            if email.lower() == "exit":
                output.info(Message("Contact creation cancelled."))
                return
            if not validate_email(email):
                output.error(Message("Please enter a valid email. Example: user@example.com"))
                continue
            break
        
        output.info(Message("Enter the address of the contact (or type 'exit' to cancel):"))
        while True:
            address = input.input().text
            if address.lower() == "exit":
                output.info(Message("Contact creation cancelled."))
                return
            if not validate_address(address):
                output.error(Message("Address must be at least 5 characters long."))
                continue
            break
        
        output.info(Message("Enter the birthday (YYYY-MM-DD) (or type 'exit' to cancel):"))
        while True:
            birthday = input.input().text
            if birthday.lower() == "exit":
                output.info(Message("Contact creation cancelled."))
                return
            if not validate_birthday(birthday):
                output.error(Message("Invalid birthday format. Please enter a valid date in YYYY-MM-DD format."))
                continue
            break
        
        contact = Contact(name, phone, email, address, birthday)
        self.repository.create(contact)

        output.success(Message(f"Contact {contact.name} added successfully!"))