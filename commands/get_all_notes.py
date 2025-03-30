from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message
from repositories.note_repository import NoteRepository
from input_output.base import Table


class GetAllNotesCommand(CommandInterface):
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    @property
    def name(self):
        return "get all notes"

    @property
    def description(self):
        return "Get all notes"

    @property
    def call_name(self):
        return "all_notes"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        notes = self.repository.get_all("title", "desc")
        tags = self.repository.get_all_tags_sorted()

        search_methods = {
            "title": self.repository.find_by_title,
            "note": self.repository.find_contains,
            "tag": self.repository.find_by_tag,
            "show_all": self.repository.get_all,
        }
        sort_methods = ["title", "note"]
        order_methods = ["asc", "desc"]

        output.table(
            Table(
                headers=["Title", "Note", "Tags"],
                data=[[note.title, note.note, ", ".join(note.tags)] for note in notes],
            )
        )

        while True:
            output.info(
                Message(
                    "You are in the active table. Type 'filter' to filter table rows, 'sort' to sort table rows, 'exit' to go back."
                )
            )
            subcmd = input.input(["filter", "sort", "exit"]).command
            if subcmd == "exit":
                break

            match (subcmd):
                case "filter":
                    output.info(Message("Enter the field to filter by:"))
                    filter = input.input(search_methods.keys()).command
                    if filter not in search_methods.keys():
                        output.warning(
                            Message(
                                "Invalid field. Use: "
                                + ", ".join(search_methods.keys())
                            )
                        )
                        continue

                    autocomplete = []
                    if filter == "tag":
                        autocomplete = tags

                    if filter == "show_all":
                        notes = search_methods[filter]()
                    else:
                        output.info(Message("Enter the value to filter by:"))
                        value = input.input(autocomplete).text
                        notes = search_methods[filter](value)

                case "sort":
                    output.info(
                        Message(
                            "Enter the field to sort by: " + ", ".join(sort_methods)
                        )
                    )
                    sort = input.input(sort_methods).command
                    if sort not in sort_methods:
                        output.warning(
                            Message("Invalid field. Use: " + ", ".join(sort_methods))
                        )
                        continue

                    output.info(Message("Enter the order: " + ", ".join(order_methods)))
                    order = input.input(order_methods).command
                    if order not in order_methods:
                        output.warning(
                            Message("Invalid order. Use: " + ", ".join(order_methods))
                        )
                        continue

                    notes = sorted(
                        notes, key=lambda x: getattr(x, sort), reverse=order == "desc"
                    )

            output.table(
                Table(
                    headers=["Title", "Note", "Tags"],
                    data=[
                        [note.title, note.note, ", ".join(note.tags)] for note in notes
                    ],
                )
            )
