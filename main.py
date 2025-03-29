from rich.console import Console
from input_output.console_input import ConsoleInput
from input_output.console_output import ConsoleOutput
from input_output.base import Message, Table
from commands.registry import registry


def main():
    console = Console()
    input = ConsoleInput(console)
    output = ConsoleOutput(console)

    exit_commands = ["exit", "quit", "bye"]

    output.display_message(Message("Hello, how can I help you today?"))
    output.display_message(Message("Available commands:"))
    output.table(
        Table(
            headers=["Command", "Description"],
            data=[
                [command.call_name, command.description]
                for command in registry.get_all_commands()
            ],
        )
    )

    while True:
        try:
            user_input = input.input(
                [
                    *exit_commands,
                    *[command.call_name for command in registry.get_all_commands()],
                ]
            )

            if not user_input.command:
                continue

            command = registry.get_command(user_input.command)
            if command:
                command.execute(input, output, user_input.args)
            elif user_input.command in exit_commands:
                output.display_message(Message("Goodbye!"))
                break
            else:
                output.display_message(Message("Invalid command. Please try again."))
        except Exception as e:
            output.error(Message("Whoops! Something went wrong."))
            output.error(Message(str(e)))
            output.display_message(Message("Sorry, I'll try again."))


if __name__ == "__main__":
    main()
