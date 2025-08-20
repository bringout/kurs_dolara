import requests
import re
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

def get_usd_rate():
    url = "https://cbbh.ba/CurrencyExchange/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        match = re.search(r'840.*<td class="tbl-smaller tbl-highlight tbl-center middle-column">(\d+\.\d+)<\/td>', response.text, re.DOTALL)
        if match:
            return match.group(1)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    return "Rate not found"

class KursDolarApp(App):
    """A Textual app to display the USD exchange rate."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Static("Fetching USD rate...", id="rate")

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        rate = get_usd_rate()
        self.query_one("#rate", Static).update(f"Današnji kurs USD je {rate} KM.")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

def main():
    app = KursDolarApp()
    app.run()

if __name__ == "__main__":
    main()