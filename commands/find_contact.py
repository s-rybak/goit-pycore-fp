from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message, Table
from repositories.contact_repository import ContactRepository


class FindContactCommand(CommandInterface):
    @property
    def name(self) -> str:
        return "Find Contact"

    @property
    def description(self) -> str:
        return "Find contacts by name, phone, email, address or birthday"

    @property
    def call_name(self) -> str:
        return "find"

    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        if len(args) < 2:
            output.display_message(
                Message(
                    "Usage: find <field> <value>. Fields: name, phone, email, address, birthday"
                )
            )
            return

        field, value = args[0], " ".join(args[1:])
        search_methods = {
            "name": self.contact_repository.findByName,
            "phone": self.contact_repository.findByPhone,
            "email": self.contact_repository.findByEmail,
            "address": self.contact_repository.findByAddress,
            "birthday": self.contact_repository.findByBirthday,
        }

        if field not in search_methods:
            output.display_message(
                Message("Invalid field. Use: name, phone, email, address or birthday")
            )
            return

        results = search_methods[field](value)
        if results:
            output.table(
                Table(
                    headers=["ID", "Name", "Phone", "Email", "Address", "Birthday"],
                    data=[
                        [c.id, c.name, c.phone, c.email, c.address, c.birthday]
                        for c in results
                    ],
                )
            )
        else:
            output.display_message(Message("No contacts found."))
