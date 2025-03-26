from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion

from .base import InputInterface, Message, Table, UserInput


class HintsCompleter(Completer):
    def __init__(self, hints):
        self.hints = hints

    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        for hint in self.hints:
            if hint.startswith(word):
                yield Completion(hint, start_position=-len(word))


class ConsoleInput(InputInterface):
    def __init__(self, console: Console):
        self.console = console
        self.current_hints = []

    def _parse_user_input(self, input: str) -> UserInput:
        """Parse user input"""
        input = input.strip()
        if len(input) == 0:
            return UserInput(input, "", [])
        cmd, *args = input.split()
        cmd = cmd.strip().lower()
        return UserInput(input, cmd, args)

    def input(self, hints: list = []) -> UserInput:
        """Input from user with autocompletion"""
        self.current_hints = hints if hints else []

        completer = HintsCompleter(self.current_hints)

        user_input = prompt(">>> ", completer=completer)

        print("\033[A\033[2K", end="", flush=True)

        text = Text(f"🧑 {user_input}")
        self.console.print(
            Panel(
                text,
                box=box.ROUNDED,
                border_style="purple",
                width=None,
                expand=False,
                padding=(0, 1),
            )
        )

        return self._parse_user_input(user_input)
