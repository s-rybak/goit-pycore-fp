from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository
from input_output.base import Table


class AllContactsCommand(CommandInterface):
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    @property
    def name(self):
        return "all contacts"

    @property
    def description(self):
        return "Get all contacts"

    @property
    def call_name(self):
        return "all_contacts"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        contacts = self.repository.getAll()
        output.table(
            Table(
                headers=["Name", "Phone", "Email", "Address", "Birthday"],
                data=[
                    [
                        contact.name,
                        contact.phone,
                        contact.email,
                        contact.address,
                        contact.birthday,
                    ]
                    for contact in contacts
                ],
            )
        )
