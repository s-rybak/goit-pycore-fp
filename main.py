from rich.console import Console
from input_output.console_input import ConsoleInput
from input_output.console_output import ConsoleOutput
from commands.greet_command import GreetCommand
from input_output.base import Message, Table
from commands.registry import registry

def main():
    console = Console()
    input = ConsoleInput(console)
    output = ConsoleOutput(console)

    output.display_message(Message("Hello, how can I help you today?"))
    output.display_message(Message("Available commands:"))
    output.table(Table(headers=["Command", "Description"], data=[[command.call_name, command.description] for command in registry.get_all_commands()]))

    while True:
        user_input = input.input([command.call_name for command in registry.get_all_commands()])
        command = registry.get_command(user_input.command)
        if command:
            command.execute(input, output,user_input.args)
        else:
            output.display_message(Message("Invalid command. Please try again."))


if __name__ == "__main__":
    main()