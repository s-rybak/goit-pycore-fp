from commands.base import CommandInterface
from input_output.base import InputInterface, OutputInterface, Message


class GreetCommand(CommandInterface):
    @property
    def name(self):
        return "Greet"

    @property
    def description(self):
        return "Greet the user"

    @property
    def call_name(self):
        return "greet"

    def execute(self, input: InputInterface, output: OutputInterface, args: list):
        output.display_message(Message("What is your name?"))
        text = input.input()
        output.display_message(Message(f"Hello, {text.text}!"))
