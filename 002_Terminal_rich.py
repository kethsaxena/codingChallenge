# from rich.console import Console
# from rich.table import Table

# console = Console()

# # Print styled text
# console.print("[bold red]Hello, World![/bold red]")

# # Create a table
# table = Table(title="User Data")
# table.add_column("Name", style="cyan", justify="left")
# table.add_column("Age", style="magenta")
# table.add_column("City", style="green")

# table.add_row("Alice", "30", "New York")
# table.add_row("Bob", "25", "Los Angeles")

# console.print(table)


from textual.app import App, ComposeResult
from textual.widgets import Button, Label

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Welcome to MyApp!", id="title")
        yield Button("Click Me", id="button")

if __name__ == "__main__":
    MyApp().run()
