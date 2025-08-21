import argparse
import requests
import re
import importlib.metadata
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Center

def get_usd_rate():
    url = "https://cbbh.ba/CurrencyExchange/"
    try:

        response = requests.get(url, timeout=10)
        
        response.raise_for_status()  # Raise an exception for bad status codes
        match = re.search(r'840.*?<td class="tbl-smaller tbl-highlight tbl-center middle-column">(\d+\.\d+)<\/td>', response.text, re.DOTALL)
        if match:
            return match.group(1)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    return "Rate not found"

class KursDolarApp(App):
    """A Textual app to display the USD exchange rate."""

    def __init__(self, theme='textual-dark', **kwargs):
        super().__init__(**kwargs)
        self.theme = theme

    CSS = """
    #rate_box {
        align: center middle;
        height: 100%;
    }
    #rate {
        background: green;
        padding: 1 2;
        text-align: center;
    }
    """

    BINDINGS = [
        ("enter", "exit_app", "Izlaz"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        with Center(id="rate_box"):
            yield Static("Fetching USD rate...", id="rate")

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        rate = get_usd_rate()
        self.query_one("#rate", Static).update(f"Današnji kurs USD je {rate} KM.")

    def action_exit_app(self) -> None:
        """An action to exit the app."""
        self.exit()

def main():
    parser = argparse.ArgumentParser(description='Display USD exchange rate.')
    parser.add_argument('--light', action='store_true', help='Enable light theme.')
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {importlib.metadata.version("kurs-dolara")}',
    )
    args = parser.parse_args()

    theme = 'textual-light' if args.light else 'textual-dark'
    app = KursDolarApp(theme=theme)
    app.run()

if __name__ == "__main__":
    main()