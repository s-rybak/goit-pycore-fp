import re

def validate_phone(phone: str):
    """Перевірка правильності номера телефону"""
    phone_pattern = r"^\+?\d{1,4}?[-.\s]?\(?\d+\)?[-.\s]?\d+[-.\s]?\d+$"
    if not re.match(phone_pattern, phone):
        raise ValueError(f"Invalid phone number format: {phone}")

def validate_email(email: str | None):
    """Перевірка правильності email адреси"""
    if email:
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            raise ValueError(f"Invalid email address format: {email}")
