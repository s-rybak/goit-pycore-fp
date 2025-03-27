from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from entities.contact import Contact


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
        output.display_message(Message("Enter the name of the contact:"))
        name = input.input().text

        output.display_message(Message("Enter the phone number of the contact:"))
        phone = input.input().text

        output.display_message(Message("Enter the email of the contact:"))
        email = input.input().text

        output.display_message(Message("Enter the address of the contact:"))
        address = input.input().text

        output.display_message(Message("Enter the birthday (YYYY-MM-DD):"))
        birthday = input.input().text

        contact = Contact(name, phone, email, address, birthday)
        self.repository.create(contact)

        output.display_message(Message(f"Contact {contact.name} added successfully!"))
