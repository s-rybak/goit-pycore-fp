import re
from datetime import datetime


def validate_email(email: str) -> bool:
    if not email.strip():
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    if not phone.strip():
        return False
    pattern = r"^\+?[0-9]{5,15}$"
    return re.match(pattern, phone) is not None


def validate_name(name: str) -> bool:
    if not name.strip():
        return False
    pattern = r"^[0-9a-zA-Zа-яА-ЯёЁїЇєЄіІäöüßÄÖÜéáíóúūñçàèùâêîôûœæūōß\s,.'\-]{2,50}$"
    return re.match(pattern, name) is not None


def validate_address(address: str) -> bool:
    return bool(address.strip()) and bool(
        re.match(r"^[0-9a-zA-Zа-яА-ЯёЁїЇєЄіІäöüßÄÖÜéáíóúūñçàèùâêîôûœæūōß\s,.'\-]{5,200}$", address)
    )


def validate_birthday(birthday: str) -> bool:
    if not birthday.strip():
        return False
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
        return True
    except ValueError:
        return False
