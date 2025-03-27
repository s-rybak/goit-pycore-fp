from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.contact_repository import ContactRepository

class EditContactCommand(CommandInterface):
    @property
    def name(self) -> str:
        return "Edit Contact"

    @property
    def description(self) -> str:
        return "Edit contact"

    @property
    def call_name(self) -> str:
        return "edit"

    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        # Крок 1: Запит команди edit
        output.display_message(Message("Enter the contact name:"))
        contacts = self.contact_repository.getAll()

        # Крок 2: Підготовка підказок з іменем та ID
        hints = [f"{c.name} {c.phone} {c.email} {c.address} {c.birthday} {c.id}" for c in contacts]

        # Крок 3: Введення імені для пошуку контакту
        user_input = input.input(hints)
        
        # Знайдемо контакт за введеним id
        selected_contact = None
        for c in contacts:
            contact_str = f"{c.name} {c.phone} {c.email} {c.address} {c.birthday} {c.id}"
            if contact_str == user_input.args:
                selected_contact = c
                break

        if not selected_contact:
            output.display_message(Message("No matching contact found."))
            return
        

        # Крок 4: Виведення поля для редагування
        output.display_message(Message("Enter the field to edit (name, phone, email, address, birthday):"))
        field_input = input.input()
        field = field_input.full.lower()

        if field not in ("name", "phone", "email", "address", "birthday"):
            output.display_message(Message("Invalid field."))
            return

        # Крок 5: Введення нового значення для вибраного поля
        output.display_message(Message(f"Enter new value for {field}:"))
        new_value = input.input().full

        # Крок 6: Оновлення поля в обраному контакті
        setattr(selected_contact, field, new_value)
        self.contact_repository.update(selected_contact)

        # Крок 7: Підтвердження успішного редагування
        output.display_message(Message(f"Contact {selected_contact.id} updated successfully."))
