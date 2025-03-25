from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from entities.contact import Contact

class TestAddContactCommand(CommandInterface):
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    @property
    def name(self):
        return "test_add_contact"
    
    @property
    def description(self):
        return "Test add contact"
    
    @property
    def call_name(self):
        return "test_add_contact"
    

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.display_message(Message("Enter the name of the contact:"))
        contacts = self.repository.getAll()
        name = input.input([contact.name for contact in self.repository.getAll()])
        output.display_message(Message("Enter the phone number of the contact:"))
        phone = input.input()
        contact = Contact(name.text, phone.command)
        self.repository.create(contact)
        output.display_message(Message(f"Contact {contact.name} with phone number {contact.phone} created successfully"))