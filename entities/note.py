from dataclasses import dataclass


@dataclass
class Note:
    id: str
    title: str
    note: str

    def __init__(
        self,
        title: str,
        note: str,
    ):
        self.id = ""
        self.title = title
        self.note = note
