from textual.app import App
from textual.widgets import Label

class MyWebApp(App):
    def compose(self):
        yield Label("Welcome to a terminal app... in your browser!")

if __name__ == "__main__":
    MyWebApp().run()
