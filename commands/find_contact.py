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
        field = input.input(["name", "phone", "email", "address", "birthday"]).text

        search_methods = {
            "name": self.contact_repository.find_by_name,
            "phone": self.contact_repository.find_by_phone,
            "email": self.contact_repository.find_by_email,
            "address": self.contact_repository.find_by_address,
            "birthday": self.contact_repository.find_by_birthday,
        }

        if field not in search_methods:
            output.display_message(
                Message("Invalid field. Use: name, phone, email, address or birthday")
            )
            return

        if field == "birthday":
            output.info(Message("Enter the birthday to filter by (YYYY-MM-DD):"))
        else:
            output.info(Message(f"Enter the {field} to filter by:"))
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
