from datetime import datetime
from input_output.base import InputInterface, OutputInterface, Message
from commands.base import CommandInterface
from repositories.contact_repository import ContactRepository


class BirthdayInDaysCommand(CommandInterface):
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    @property
    def name(self):
        return "birthday_in_days"

    @property
    def description(self):
        return "Display contacts with birthdays in the N days"

    @property
    def call_name(self):
        return "birthday_in_days"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):

        try:
            output.display_message(
                Message("Enter the number of days to filter birthdays.")
            )
            days_range_input = input.input().text.strip()
            days_range = int(days_range_input) if days_range_input else None
        except ValueError:
            output.error(Message("Invalid input. Showing all upcoming birthdays."))
            days_range = None

        today = datetime.today().date()
        upcoming_contacts = []

        contacts = self.repository.getAll()

        for contact in contacts:
            if not contact.birthday:
                output.warning(
                    Message(
                        f"Contact {contact.name} has no birthday information. Skipping..."
                    )
                )
                continue

            try:
                cleaned_birthday = contact.birthday.strip()
                birthday_date = datetime.strptime(cleaned_birthday, "%Y-%m-%d").date()
            except ValueError:
                output.error(
                    Message(
                        f"Invalid birthday format for contact {contact.name}. Expected format is YYYY-MM-DD."
                    )
                )
                continue

            current_year_birthday = birthday_date.replace(year=today.year)

            if current_year_birthday < today:
                current_year_birthday = current_year_birthday.replace(
                    year=today.year + 1
                )

            days_until = (current_year_birthday - today).days

            if days_range is None or days_until <= days_range:
                upcoming_contacts.append(
                    (contact.name, current_year_birthday.strftime("%d %B"), days_until)
                )

        if upcoming_contacts:
            output.display_message(Message("Upcoming birthdays:"))
            for name, birthday, days_until in sorted(
                upcoming_contacts, key=lambda x: x[2]
            ):
                output.display_message(
                    Message(f"{name}: {birthday} (in {days_until} days)")
                )
        else:
            output.warning(
                Message(
                    "No contacts have valid birthday information or no birthdays within the specified range."
                )
            )
