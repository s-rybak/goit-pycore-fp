from dataclasses import dataclass


@dataclass
class Note:
    id: str
    title: str
    note: str
    tags: list[str]

    def __init__(
        self,
        title: str,
        note: str,
        tags: list[str] = [],
    ):
        self.id = ""
        self.title = title
        self.note = note
        self.tags = tags
