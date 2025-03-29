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
        return "find_contact"

    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.info(
            "Enter the field to search by (name, phone, email, address, birthday):"
        )
        field = input.input().text

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

        output.info(Message(f"Enter the {field} to search for:"))
        value = input.input().text

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
