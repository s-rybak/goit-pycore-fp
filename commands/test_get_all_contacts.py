from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from entities.contact import Contact
from input_output.base import Table

class TestAllContactsCommand(CommandInterface):
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    @property
    def name(self):
        return "test all contacts"
    
    @property
    def description(self):
        return "Test all contact"
    
    @property
    def call_name(self):
        return "test_all_contacts"
    

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.display_message(Message("Enter the name of the contact:"))
        contacts = self.repository.getAll()
        output.table(Table(headers=["Name", "Phone"], data=[[contact.name, contact.phone] for contact in contacts]))