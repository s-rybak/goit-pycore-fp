from rich.console import Console
from rich.table import Table as RichTable
from rich.panel import Panel
from rich.text import Text
from rich import box

from .base import OutputInterface, Message, Table

class ConsoleOutput(OutputInterface):
    def __init__(self, console: Console):
        self.console = console
        self.current_hints = []

    def _format_message(self, msg: Message, style: str, emoji: str = None):
        """Format message in chat style"""
        text = Text()
        if emoji:
            text.append(f"{emoji} ", style="bold")
        text.append(str(msg), style=style)
        self.console.print(
            Panel(
                text, 
                box=box.ROUNDED, 
                border_style=style,
                width=None,
                expand=False,
                padding=(0, 1)
            ),
            justify="right"
        )

    def success(self, msg: Message):
        """Print success message"""
        self._format_message(msg, "green", "✅")

    def error(self, msg: Message):
        """Print error message"""
        self._format_message(msg, "red", "❌")
    
    def warning(self, msg: Message):
        """Print warning message"""
        self._format_message(msg, "yellow", "⚠️")
    
    def info(self, msg: Message):
        """Print info message"""
        self._format_message(msg, "blue", "ℹ️")
    
    def hint(self, msg: Message):
        """Print hint message"""
        self._format_message(msg, "cyan", "💡")

    def display_message(self, msg: Message):
        """Display message"""
        self._format_message(msg, "white")
    
    def table(self, table: Table):
        """Display table"""
        rich_table = RichTable()
        
        # Add headers
        for header in table.headers:
            rich_table.add_column(header, style="bold")
        
        # Add data
        for row in table.data:
            rich_table.add_row(*[str(cell) for cell in row])
        
        self.console.print(rich_table)
