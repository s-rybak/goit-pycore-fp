from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message, Table


class HelpCommand(CommandInterface):
    def __init__(self, registry=None):
        self.registry = registry

    @property
    def name(self) -> str:
        return "Help"

    @property
    def description(self) -> str:
        return "Display all available commands and their descriptions"

    @property
    def call_name(self) -> str:
        return "help"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        if not self.registry:
            from commands.registry import registry

            self.registry = registry

        if len(args) > 0:
            command_name = args[0]
            command = self.registry.get_command(command_name)

            if command:
                output.info(Message(f"Help for command: {command.name}"))
                output.info(Message(f"Description: {command.description}"))
                output.info(Message(f"Usage: {command.call_name}"))
            else:
                output.error(Message(f"Command '{command_name}' not found."))
        else:
            output.info(Message("Available commands:"))
            output.table(
                Table(
                    headers=["Command", "Description"],
                    data=[
                        [command.call_name, command.description]
                        for command in self.registry.get_all_commands()
                    ],
                )
            )
