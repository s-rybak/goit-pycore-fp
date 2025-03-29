import re
from datetime import datetime


def validate_email(email: str) -> bool:
    if not email.strip():
        return False
    pattern = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)])"
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    if not phone.strip():
        return False
    pattern = r"^\+?[0-9]{7,15}$"
    return re.match(pattern, phone) is not None


def validate_name(name: str) -> bool:
    if not name.strip():
        return False
    pattern = r"^[a-zA-Zа-яА-ЯїЇєЄіІ' -]{2,10}$"
    return re.match(pattern, name) is not None


def validate_address(address: str) -> bool:
    return bool(address.strip()) and bool(
        re.match(r"^[a-zA-Zа-яА-Я0-9\s,.'-]{5,100}$", address)
    )


def validate_birthday(birthday: str) -> bool:
    return bool(birthday.strip()) and bool(
        re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday)
    )
